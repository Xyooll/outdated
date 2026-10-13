package org.xyool.connect;

import android.content.Context;
import android.net.ConnectivityManager;
import android.net.Network;
import android.net.NetworkCapabilities;
import android.net.nsd.NsdManager;
import android.net.nsd.NsdServiceInfo;
import android.net.wifi.WifiManager;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.URI;
import java.nio.charset.StandardCharsets;
import java.util.ArrayDeque;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import org.java_websocket.WebSocket;
import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ClientHandshake;
import org.java_websocket.handshake.ServerHandshake;
import org.java_websocket.server.WebSocketServer;
import org.json.JSONObject;

/**
 * Experimental Xyool phone-as-server mode for trusted Wi-Fi networks.
 *
 * Every Android phone exposes a local WS signaling endpoint, advertises its
 * PUBLIC Xyool ID over mDNS/NSD, discovers other nodes, and forwards WebRTC
 * call setup directly between phones. No Railway, Google, public IP or
 * cloud account needed on the same LAN.
 *
 * mDNS advertisement is not authenticated, but LAN signaling frames are
 * signed by an AndroidKeyStore device key and WebRTC SDP is covered by the
 * signature. ID-to-device binding is TOFU on first contact unless an XYOOl2
 * identity QR with a key fingerprint was scanned from a trusted device.
 * Signatures provide integrity, NOT confidentiality of ws:// LAN metadata.
 * Never run this listener on untrusted public Wi-Fi networks.
 *
 * Lifecycle: starts only while the calling Activity is in foreground
 * on a Wi-Fi network and closes on screen exit/network loss.
 */
public final class LocalPeerNode {
    public interface Listener {
        void onPeerChanged(String id, boolean online);
        void onPacket(JSONObject packet);
        void onNodeStatus(String status);
    }
    public static final String SERVICE_TYPE="_xyoolcall._tcp.";
    private static final String PATH="/xyool-lan-v1";
    private static final int PORT=18788;
    private static final String ID_RE="^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$";
    private final Context context;
    private final String myId;
    private final Listener listener;
    private final NsdManager nsd;
    private final ConcurrentHashMap<String, InetSocketAddress> discovered=new ConcurrentHashMap<>();
    private final ConcurrentHashMap<String,Long> recentInvites=new ConcurrentHashMap<>();
    private final ArrayDeque<NsdServiceInfo> resolveQueue=new ArrayDeque<>();
    private boolean resolving;
    private WebSocketServer server;
    private NsdManager.DiscoveryListener discovery;
    private NsdManager.RegistrationListener registration;
    private WifiManager.MulticastLock lock;
    private WebSocket incoming;
    private WebSocketClient outgoing;
    private boolean started;
    private String inboundPeerId,inboundPeerKey,inboundNonce;
    private String outboundPeerId,outboundPeerKey,outboundNonce;
    private int inboundSent,inboundSeen,outboundSent,outboundSeen;

    public LocalPeerNode(Context context,String id,Listener listener) {
        this.context=context.getApplicationContext();
        this.myId=id;
        this.listener=listener;
        this.nsd=(NsdManager)this.context.getSystemService(Context.NSD_SERVICE);
    }

    public static boolean onWifi(Context context) {
        ConnectivityManager mgr=(ConnectivityManager)context.getSystemService(Context.CONNECTIVITY_SERVICE);
        if(mgr==null)return false;
        NetworkCapabilities caps=mgr.getNetworkCapabilities(mgr.getActiveNetwork());
        if(caps!=null&&caps.hasTransport(NetworkCapabilities.TRANSPORT_WIFI))return true;
        // Rethink DNS and other VPN clients can be the active network while
        // the underlying Wi-Fi is still available for local node discovery.
        for(Network network:mgr.getAllNetworks()){
            NetworkCapabilities underlying=mgr.getNetworkCapabilities(network);
            if(underlying!=null&&underlying.hasTransport(NetworkCapabilities.TRANSPORT_WIFI))
                return true;
        }
        return false;
    }

    public synchronized void start(){
        if(started)return;
        if(nsd==null||!onWifi(context)){
            listener.onNodeStatus("Nearby calling requires both phones on the same Wi-Fi.");
            return;
        }
        started=true;
        try{
            WifiManager wifi=(WifiManager)context.getApplicationContext().getSystemService(Context.WIFI_SERVICE);
            if(wifi!=null){
                lock=wifi.createMulticastLock("xyool-local-discovery");
                lock.setReferenceCounted(false);
                lock.acquire();
            }
            server=new WebSocketServer(new InetSocketAddress(PORT)){
                @Override public void onOpen(WebSocket conn,ClientHandshake handshake){
                    if(!PATH.equals(handshake.getResourceDescriptor()) || !onWifi(LocalPeerNode.this.context)){
                        conn.close(1008,"Local Wi-Fi only");return;
                    }
                }
                @Override public void onMessage(WebSocket conn,String raw){
                    if(raw.length()>45000){conn.close(1009);return;}
                    try{
                        JSONObject msg=new JSONObject(raw);
                        String type=msg.optString("type","");
                        if(incoming!=conn){
                            String caller=msg.optString("from","");
                            long ts=msg.optLong("authTs",-1L);
                            String nonce=msg.optString("authNonce","");
                            String key=msg.optString("authKey","");
                            if(!"call".equals(type)||!msg.optString("to","").equals(myId)
                                ||!caller.matches(ID_RE)||ts<System.currentTimeMillis()-30000L
                                ||ts>System.currentTimeMillis()+30000L
                                ||!nonce.matches("^[a-f0-9]{32}$")
                                ||!PhoneIdentity.verify(key,msg.optString("authSig",""),
                                    PhoneIdentity.callProof(caller,myId,ts,nonce))
                                ||!PhoneIdentity.pinOrVerify(context,caller,key)){
                                conn.close(1008,"Unauthenticated caller");return;
                            }
                            synchronized(LocalPeerNode.this){
                                long now=System.currentTimeMillis();
                                if(recentInvites.size()>256)recentInvites.entrySet().removeIf(
                                    e->e.getValue()<now);
                                String challengeKey=caller+"|"+nonce;
                                if(recentInvites.size()>512 ||
                                    recentInvites.putIfAbsent(challengeKey,now+60000L)!=null){
                                    conn.close(1008,"Repeated call invitation");return;
                                }
                                if(incoming!=null||outgoing!=null){
                                    conn.send("{\"type\":\"busy\"}");
                                    conn.close(1000);return;
                                }
                                incoming=conn;
                                inboundPeerId=caller;inboundPeerKey=key;inboundNonce=nonce;
                                inboundSent=0;inboundSeen=0;
                            }
                            JSONObject event=new JSONObject();
                            event.put("type","incoming");event.put("from",caller);
                            listener.onPacket(event);
                            JSONObject ringing=new JSONObject();
                            ringing.put("type","ringing");
                            conn.send(authenticated(ringing,true).toString());
                            return;
                        }
                        if(!validPacket(msg)||!verifyIncoming(msg,true)){
                            conn.close(1008,"Unauthenticated packet");return;
                        }
                        if("hangup".equals(type)||"reject".equals(type)){
                            JSONObject ended=new JSONObject();
                            ended.put("type","ended");
                            ended.put("reason","peer-ended");
                            listener.onPacket(ended);
                            conn.close(1000,"Call ended");
                        }else listener.onPacket(msg);
                    }catch(Exception ex){conn.close(1008,"Bad JSON");}
                }
                @Override public void onClose(WebSocket conn,int code,String reason,boolean remote){
                    boolean wasActive;
                    synchronized(LocalPeerNode.this){
                        wasActive=incoming==conn;
                        if(wasActive)incoming=null;
                    }
                    if(wasActive){
                        inboundPeerId=null;inboundPeerKey=null;inboundNonce=null;
                        notifyEnded();
                    }
                }
                @Override public void onError(WebSocket conn,Exception ex){
                    listener.onNodeStatus("Nearby listener error; use the internet connection.");
                }
                @Override public void onStart(){
                    if(started)advertise();
                }
            };
            server.setReuseAddr(true);
            server.start();
            beginDiscovery();
        }catch(Exception e){
            listener.onNodeStatus("Nearby node couldn't start: "+e.getClass().getSimpleName());
            stop();
        }
    }

    private boolean validPacket(JSONObject m){
        String t=m.optString("type","");
        if("accept".equals(t)||"reject".equals(t)||"hangup".equals(t))return true;
        if(!"signal".equals(t))return false;
        String kind=m.optString("kind","");
        if("offer".equals(kind)||"answer".equals(kind)){
            String sdp=m.optString("sdp","");
            return sdp.length()>80&&sdp.length()<40000&&sdp.startsWith("v=0");
        }
        if("candidate".equals(kind)){
            return m.optString("candidate","").length()<4000&&
                m.optString("mid","").length()<50&&m.optInt("index",-1)>=0;
        }
        return false;
    }

    private synchronized void advertise(){
        if(!started||registration!=null)return;
        NsdServiceInfo info=new NsdServiceInfo();
        info.setServiceType(SERVICE_TYPE);
        info.setServiceName("Xyool-"+myId);
        info.setPort(PORT);
        info.setAttribute("id",myId);
        registration=new NsdManager.RegistrationListener(){
            @Override public void onRegistrationFailed(NsdServiceInfo i,int error){
                listener.onNodeStatus("Nearby ID advertisement failed.");
            }
            @Override public void onUnregistrationFailed(NsdServiceInfo i,int error){}
            @Override public void onServiceRegistered(NsdServiceInfo i){
                listener.onNodeStatus("This phone is a local Xyool node.");
            }
            @Override public void onServiceUnregistered(NsdServiceInfo i){}
        };
        try{nsd.registerService(info,NsdManager.PROTOCOL_DNS_SD,registration);}
        catch(Exception ex){registration=null;listener.onNodeStatus("Couldn't advertise nearby ID.");}
    }

    private synchronized void beginDiscovery(){
        if(!started||discovery!=null)return;
        discovery=new NsdManager.DiscoveryListener(){
            @Override public void onDiscoveryStarted(String type){}
            @Override public void onStartDiscoveryFailed(String type,int error){
                listener.onNodeStatus("Nearby search unavailable on this Wi-Fi.");
            }
            @Override public void onStopDiscoveryFailed(String type,int error){}
            @Override public void onDiscoveryStopped(String type){}
            @Override public void onServiceFound(NsdServiceInfo info){
                if(!info.getServiceType().contains("_xyoolcall"))return;
                synchronized(LocalPeerNode.this){
                    if(!started)return;
                    resolveQueue.offer(info);
                    resolveNext();
                }
            }
            @Override public void onServiceLost(NsdServiceInfo info){
                String id=extractId(info);
                if(id!=null&&discovered.remove(id)!=null)listener.onPeerChanged(id,false);
            }
        };
        try{nsd.discoverServices(SERVICE_TYPE,NsdManager.PROTOCOL_DNS_SD,discovery);}
        catch(Exception ex){discovery=null;listener.onNodeStatus("Nearby discovery couldn't start.");}
    }
    private String extractId(NsdServiceInfo info){
        byte[] b=info.getAttributes().get("id");
        if(b!=null){
            String raw=new String(b,StandardCharsets.UTF_8);
            if(raw.matches(ID_RE))return raw;
        }
        String name=info.getServiceName();
        int p=name.indexOf("XY-");
        if(p>=0&&name.length()>=p+17){
            String candidate=name.substring(p,p+17);
            if(candidate.matches(ID_RE))return candidate;
        }
        return null;
    }
    private synchronized void resolveNext(){
        if(resolving||!started)return;
        NsdServiceInfo next=resolveQueue.poll();
        if(next==null)return;
        resolving=true;
        try{
            nsd.resolveService(next,new NsdManager.ResolveListener(){
                @Override public void onResolveFailed(NsdServiceInfo service,int error){
                    finish();
                }
                @Override public void onServiceResolved(NsdServiceInfo service){
                    String peerId=extractId(service);
                    InetAddress addr=service.getHost();
                    if(started&&peerId!=null&&!peerId.equals(myId)&&addr!=null
                        &&service.getPort()>0&&service.getPort()<65536){
                        discovered.put(peerId,new InetSocketAddress(addr,service.getPort()));
                        listener.onPeerChanged(peerId,true);
                    }
                    finish();
                }
                private void finish(){
                    synchronized(LocalPeerNode.this){
                        resolving=false;
                        resolveNext();
                    }
                }
            });
        }catch(Exception e){
            resolving=false;
            resolveNext();
        }
    }

    public boolean hasPeer(String id){return discovered.containsKey(id);}
    public int peerCount(){return discovered.size();}
    public synchronized boolean call(String to){
        InetSocketAddress address=discovered.get(to);
        if(!started||address==null||!onWifi(context)||incoming!=null||outgoing!=null)return false;
        try{
            String ip=address.getAddress().getHostAddress();
            // Include square brackets for IPv6 literals.
            String host=ip.contains(":")?"["+ip.replace("%","%25")+"]":ip;
            URI endpoint=URI.create("ws://"+host+":"+address.getPort()+PATH);
            outboundPeerId=to;outboundPeerKey=null;
            outboundNonce=PhoneIdentity.newNonce();
            outboundSent=0;outboundSeen=0;
            outgoing=new WebSocketClient(endpoint){
                @Override public void onOpen(ServerHandshake handshake){
                    try{
                        JSONObject data=new JSONObject();
                        long ts=System.currentTimeMillis();
                        data.put("type","call");data.put("from",myId);data.put("to",to);
                        data.put("authKey",PhoneIdentity.publicKey());
                        data.put("authTs",ts);data.put("authNonce",outboundNonce);
                        data.put("authSig",PhoneIdentity.sign(
                            PhoneIdentity.callProof(myId,to,ts,outboundNonce)));
                        send(data.toString());
                    }catch(Exception e){listener.onNodeStatus("Nearby calling failed.");}
                }
                @Override public void onMessage(String raw){
                    if(raw.length()>45000)return;
                    try{
                        JSONObject msg=new JSONObject(raw);
                        String type=msg.optString("type","");
                        if("busy".equals(type)){listener.onPacket(msg);return;}
                        if(("ringing".equals(type)||"accepted".equals(type)||
                            "signal".equals(type)||"ended".equals(type))
                            &&verifyIncoming(msg,false))
                            listener.onPacket(msg);
                    }catch(Exception ignored){}
                }
                @Override public void onClose(int code,String reason,boolean remote){
                    boolean active;
                    synchronized(LocalPeerNode.this){
                        active=outgoing==this;
                        if(active)outgoing=null;
                    }
                    if(active){
                        outboundPeerId=null;outboundPeerKey=null;outboundNonce=null;
                        notifyEnded();
                    }
                }
                @Override public void onError(Exception e){
                    listener.onNodeStatus("Nearby peer isn't reachable on this Wi-Fi.");
                }
            };
            outgoing.connect();
            return true;
        }catch(Exception e){
            outgoing=null;
            return false;
        }
    }
    private synchronized JSONObject authenticated(JSONObject packet,boolean inbound)throws Exception{
        String nonce=inbound?inboundNonce:outboundNonce;
        if(nonce==null)throw new IllegalStateException("No authenticated call session");
        JSONObject result=new JSONObject(packet.toString());
        int seq=inbound?++inboundSent:++outboundSent;
        result.put("authSeq",seq);
        result.put("authNonce",nonce);
        result.put("authKey",PhoneIdentity.publicKey());
        result.put("authSig",PhoneIdentity.sign(
            PhoneIdentity.packetProof(myId,nonce,seq,result)));
        return result;
    }
    private synchronized boolean verifyIncoming(JSONObject packet,boolean inbound){
        String nonce=inbound?inboundNonce:outboundNonce;
        String id=inbound?inboundPeerId:outboundPeerId;
        String key=inbound?inboundPeerKey:outboundPeerKey;
        if(nonce==null||id==null||!nonce.equals(packet.optString("authNonce","")))
            return false;
        int seq=packet.optInt("authSeq",-1);
        int last=inbound?inboundSeen:outboundSeen;
        if(seq<1||seq<=last)return false;
        String announced=packet.optString("authKey","");
        if(key==null){
            if(inbound||announced.isEmpty()||
                !PhoneIdentity.verify(announced,packet.optString("authSig",""),
                    PhoneIdentity.packetProof(id,nonce,seq,packet))||
                !PhoneIdentity.pinOrVerify(context,id,announced))return false;
            key=announced;
        }else if(!key.equals(announced))return false;
        if(!PhoneIdentity.verify(key,packet.optString("authSig",""),
            PhoneIdentity.packetProof(id,nonce,seq,packet)))return false;
        if(inbound)inboundSeen=seq;
        else{outboundSeen=seq;outboundPeerKey=key;}
        return true;
    }
    /** Only send authenticated frames on the current trusted-LAN connection. */
    public synchronized boolean send(JSONObject msg){
        String type=msg.optString("type","");
        if(!validPacket(msg))return false;
        try{
            if(outgoing!=null&&outgoing.isOpen()){
                outgoing.send(authenticated(msg,false).toString());return true;
            }
            if(incoming!=null&&incoming.isOpen()){
                JSONObject result=msg;
                if("accept".equals(type)){
                    result=new JSONObject();result.put("type","accepted");
                }else if("reject".equals(type)||"hangup".equals(type)){
                    result=new JSONObject();result.put("type","ended");
                    result.put("reason","peer-ended");
                }
                incoming.send(authenticated(result,true).toString());
                return true;
            }
        }catch(Exception ignored){}
        return false;
    }

    public synchronized boolean hasSession(){return incoming!=null||outgoing!=null;}
    public synchronized void closeSession(){
        WebSocketClient a=outgoing;outgoing=null;
        WebSocket b=incoming;incoming=null;
        if(a!=null)a.close();
        if(b!=null)b.close();
        inboundPeerId=null;inboundPeerKey=null;inboundNonce=null;
        outboundPeerId=null;outboundPeerKey=null;outboundNonce=null;
    }
    private void notifyEnded(){
        try{
            JSONObject ended=new JSONObject();ended.put("type","ended");
            ended.put("reason","nearby-disconnected");
            listener.onPacket(ended);
        }catch(Exception ignored){}
    }

    public synchronized void stop(){
        if(!started)return;
        started=false;
        closeSession();
        discovered.clear();
        recentInvites.clear();
        resolveQueue.clear();
        if(discovery!=null){
            try{nsd.stopServiceDiscovery(discovery);}catch(Exception ignored){}
            discovery=null;
        }
        if(registration!=null){
            try{nsd.unregisterService(registration);}catch(Exception ignored){}
            registration=null;
        }
        if(server!=null){
            try{server.stop(500);}catch(Exception ignored){}
            server=null;
        }
        if(lock!=null&&lock.isHeld()){lock.release();lock=null;}
    }
}
