package org.xyool.connect;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Handler;
import android.util.Base64;
import org.json.JSONArray;
import org.json.JSONObject;
import org.webrtc.DataChannel;
import org.webrtc.IceCandidate;
import org.webrtc.MediaConstraints;
import org.webrtc.MediaStream;
import org.webrtc.PeerConnection;
import org.webrtc.PeerConnectionFactory;
import org.webrtc.RtpReceiver;
import org.webrtc.SdpObserver;
import org.webrtc.SessionDescription;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.LinkedHashMap;
import java.util.Iterator;

/**
 * Experimental global phone-to-phone WebRTC DATA overlay. Signaling is supplied
 * by a chosen rendezvous server only to find and connect peers; packets then
 * travel directly via DTLS-encrypted data channels, when ICE connectivity works.
 *
 * No hidden open proxy. Forwarding is opt-in, capped at 3 neighbors / 3 hops
 * and 4 KiB frames. This alpha routes signed ping/pong control packets ONLY:
 * it does not forward calls, arbitrary Internet traffic, media, files or SDP.
 *
 * The registration authority is still a trusted server; local device-key
 * signatures provide packet integrity, but first-contact peer-ID binding is
 * not globally verified. Mobile NATs may require the user's TURN relay.
 */
public final class GlobalPhoneMesh {
    public static final String PREF_RELAY="xyool_global_relay_opt_in";
    public static final String PREF_PEER_HINTS="xyool_peer_hints_receive_opt_in";
    private static final int MAX_NEIGHBORS=3;
    private static final int MAX_FRAME=4096;
    private static final String DEFAULT_STUN="stun:stun.cloudflare.com:3478";
    private static final String ID_RE="^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$";
    public interface Transport {
        void send(JSONObject message);
        void status(String message);
    }
    private final Context context;
    private final Handler main;
    private final Transport transport;
    private final String self;
    private final SharedPreferences prefs;
    private final HashMap<String,Link> links=new HashMap<>();
    private final HashMap<String,String> serverKeys=new HashMap<>();
    private final HashMap<String,List<IceCandidate>> earlyCandidates=new HashMap<>();
    private final LinkedHashMap<String,Long> seen=new LinkedHashMap<>();
    private PeerConnectionFactory factory;
    private boolean online;
    private boolean closed;
    private boolean forwarding;
    private long window=System.currentTimeMillis();
    private int trafficCount=0;

    private static final class Link {
        final String id;
        PeerConnection pc;
        DataChannel dc;
        boolean remoteReady;
        final List<IceCandidate> queued=new ArrayList<>();
        Link(String id){this.id=id;}
        boolean open(){return dc!=null&&dc.state()==DataChannel.State.OPEN;}
    }
    public GlobalPhoneMesh(Context context,Handler main,String id,Transport transport){
        this.context=context.getApplicationContext();
        this.main=main;
        self=id;
        this.transport=transport;
        prefs=context.getSharedPreferences("xyool_private",Context.MODE_PRIVATE);
        forwarding=prefs.getBoolean(PREF_RELAY,false);
    }
    public void setForwarding(boolean enabled){
        forwarding=enabled;
        prefs.edit().putBoolean(PREF_RELAY,enabled).apply();
        transport.status(enabled?"Limited peer control-packet forwarding enabled.":
            "Peer forwarding disabled.");
    }
    /** Receive hints only after the owner explicitly opts in. Off by default. */
    public void setPeerHintReceiving(boolean enabled){
        prefs.edit().putBoolean(PREF_PEER_HINTS,enabled).apply();
        transport.status(enabled?"Peer introductions enabled (hints only; no auto-connect).":
            "Peer introductions disabled.");
    }
    public boolean peerHintReceiving(){return prefs.getBoolean(PREF_PEER_HINTS,false);}
    /**
     * Explicit user-action only. Share ONE QR-verified contact's ID/key
     * fingerprint with at most three QR-verified, directly connected peers.
     * Nothing here updates contacts, dials another peer, or exposes IPs.
     */
    public int sharePeerHint(String suggestedId,boolean explicitlyConfirmed){
        if(!explicitlyConfirmed||closed||!PeerHintPolicy.validId(suggestedId))return 0;
        String subjectKey=PhoneIdentity.qrVerifiedFingerprint(context,suggestedId);
        if(subjectKey==null)return 0;
        int sent=0;
        for(Link link:links.values()){
            String recipientKey=PhoneIdentity.qrVerifiedFingerprint(context,link.id);
            if(!PeerHintPolicy.sendable(self,link.id,suggestedId,
                recipientKey,subjectKey,true)||!link.open()||
                link.dc.bufferedAmount()>131072L||!allowPacket())continue;
            try {
                JSONObject body=new JSONObject();
                body.put("kind","peer-hint");
                body.put("subject",suggestedId);
                body.put("fingerprint",subjectKey);
                String payload=body.toString();
                JSONObject frame=signFrame(link.id,"peer-hint");
                frame.put("payload",payload);
                frame.put("ttl",1); // Hints are never multi-hop forwarded.
                frame.put("signature",PhoneIdentity.sign(canonical(self,link.id,
                    frame.getString("nonce"),frame.getLong("when"),payload)));
                byte[] bytes=frame.toString().getBytes(StandardCharsets.UTF_8);
                if(bytes.length<=MAX_FRAME &&
                    link.dc.send(new DataChannel.Buffer(ByteBuffer.wrap(bytes),false)))sent++;
            }catch(Exception ignored){}
        }
        return sent;
    }
    public int neighbors(){
        int n=0;
        for(Link l:links.values())if(l.open())n++;
        return n;
    }
    public boolean forwarding(){return forwarding;}
    public void connected(){
        if(closed)return;
        online=true;
        try{
            if(factory==null){
                PeerConnectionFactory.initialize(
                    PeerConnectionFactory.InitializationOptions.builder(context)
                    .createInitializationOptions());
                factory=PeerConnectionFactory.builder().createPeerConnectionFactory();
            }
            if(factory!=null){
                JSONObject msg=new JSONObject();
                long when=System.currentTimeMillis();
                msg.put("type","mesh-enable");msg.put("authTs",when);
                msg.put("authKey",PhoneIdentity.publicKey());
                msg.put("authSig",PhoneIdentity.sign(PhoneIdentity.meshEnableProof(self,when)));
                transport.send(msg);
            }
        }catch(Exception error){
            transport.status("Phone mesh unavailable on this Android device.");
        }
    }
    /** Keep existing encrypted peer links alive when the rendezvous node goes away. */
    public void rendezvousOffline(){
        online=false;
    }
    public void disconnected(){
        online=false;
        for(Link link:new ArrayList<>(links.values()))closeLink(link);
        links.clear();
        serverKeys.clear();
        earlyCandidates.clear();
        seen.clear();
    }
    public void stop(){
        closed=true;
        disconnected();
        if(factory!=null){factory.dispose();factory=null;}
    }
    public void fromRendezvous(JSONObject msg){
        if(!online||closed||factory==null)return;
        String type=msg.optString("type","");
        if("mesh-peers".equals(type)){
            JSONArray peers=msg.optJSONArray("ids");
            if(peers==null)return;
            JSONObject pins=msg.optJSONObject("pins");
            if(pins==null)return;
            for(int i=0;i<peers.length();i++){
                String id=peers.optString(i,"");
                String fingerprint=pins.optString(id,"");
                if(id.matches(ID_RE)&&fingerprint.matches("^[a-f0-9]{64}$"))
                    serverKeys.put(id,fingerprint);
            }
            // The smaller ID initiates each pair; prevents conflicting offers.
            for(int i=0;i<peers.length()&&links.size()<MAX_NEIGHBORS;i++){
                String id=peers.optString(i,"");
                if(!id.matches(ID_RE)||self.equals(id)||links.containsKey(id)||
                    !serverKeys.containsKey(id))continue;
                if(self.compareTo(id)<0){
                    Link l=createLink(id);
                    if(l!=null)makeOffer(l);
                }
            }
            return;
        }
        if(!"mesh-signal".equals(type))return;
        String from=msg.optString("from","");
        String kind=msg.optString("kind","");
        if(!from.matches(ID_RE)||self.equals(from)||!verifySignal(msg,from,kind))return;
        Link l=links.get(from);
        if("offer".equals(kind)){
            if(l==null){
                if(links.size()>=MAX_NEIGHBORS)return;
                l=createLink(from);
            }
            if(l!=null)applyRemote(l,msg,"offer");
        }else if("candidate".equals(kind) && l==null){
            IceCandidate ice=parseCandidate(msg);
            if(ice!=null && earlyCandidates.size()<16){
                List<IceCandidate> queue=earlyCandidates.get(from);
                if(queue==null){queue=new ArrayList<>();earlyCandidates.put(from,queue);}
                if(queue.size()<40)queue.add(ice);
            }
        }else if(l!=null){
            if("answer".equals(kind))applyRemote(l,msg,"answer");
            else if("candidate".equals(kind)){
                String candidate=msg.optString("candidate","");
                int index=msg.optInt("index",-1);
                String mid=msg.optString("mid","");
                if(candidate.length()<4000&&index>=0&&index<=50&&mid.length()<50){
                    IceCandidate ice=new IceCandidate(mid,index,candidate);
                    if(l.remoteReady)l.pc.addIceCandidate(ice);
                    else if(l.queued.size()<40)l.queued.add(ice);
                }
            }else if("close".equals(kind))closeLink(l);
        }
    }
    private static String evidence(JSONObject data,String key){
        return data.optString(key,"");
    }
    private JSONObject authenticatedSignal(String to,String kind,String sdp,
        String candidate,String mid,int index)throws Exception{
        long when=System.currentTimeMillis();
        JSONObject m=new JSONObject();
        m.put("type","mesh-signal");m.put("to",to);m.put("kind",kind);
        if(!sdp.isEmpty())m.put("sdp",sdp);
        if(!candidate.isEmpty())m.put("candidate",candidate);
        if(!mid.isEmpty())m.put("mid",mid);
        if(index>=0)m.put("index",index);
        m.put("authTs",when);m.put("authKey",PhoneIdentity.publicKey());
        m.put("authSig",PhoneIdentity.sign(
            PhoneIdentity.meshSignalProof(self,to,kind,when,sdp,candidate,mid,index)));
        return m;
    }
    private boolean verifySignal(JSONObject packet,String from,String kind){
        try{
            long when=packet.optLong("authTs",-1L);
            String key=packet.optString("authKey","");
            String fingerprint=PhoneIdentity.fingerprintFor(key);
            String expected=serverKeys.get(from);
            if(expected==null||!expected.equals(fingerprint)||
                Math.abs(System.currentTimeMillis()-when)>30000L)return false;
            String manuallyPinned=PhoneIdentity.pinnedFingerprint(context,from);
            if(manuallyPinned!=null&&!manuallyPinned.equals(fingerprint))return false;
            return PhoneIdentity.verify(key,packet.optString("authSig",""),
                PhoneIdentity.meshSignalProof(from,self,kind,when,
                    packet.optString("sdp",""),packet.optString("candidate",""),
                    packet.optString("mid",""),packet.optInt("index",-1)));
        }catch(Exception invalid){return false;}
    }
    private IceCandidate parseCandidate(JSONObject msg){
        String candidate=msg.optString("candidate","");
        int index=msg.optInt("index",-1);
        String mid=msg.optString("mid","");
        if(candidate.isEmpty()||candidate.length()>4000||index<0||index>50||mid.length()>50)
            return null;
        return new IceCandidate(mid,index,candidate);
    }
    private List<PeerConnection.IceServer> iceServers(){
        ArrayList<PeerConnection.IceServer> servers=new ArrayList<>();
        String stun=prefs.getString("xyool_stun","").trim();
        if(stun.isEmpty())stun=DEFAULT_STUN;
        if(!"off".equalsIgnoreCase(stun)&&stun.matches("^stuns?:[A-Za-z0-9._-]+:[0-9]{2,5}$"))
            servers.add(PeerConnection.IceServer.builder(stun).createIceServer());
        String turn=prefs.getString("xyool_turn","").trim();
        String user=prefs.getString("xyool_turn_user",""),pass=prefs.getString("xyool_turn_pass","");
        if(!user.isEmpty()&&!pass.isEmpty()&&
            turn.matches("^turns?:[A-Za-z0-9._-]+:[0-9]{2,5}(\\?transport=(udp|tcp))?$"))
            servers.add(PeerConnection.IceServer.builder(turn)
                .setUsername(user).setPassword(pass).createIceServer());
        return servers;
    }
    private Link createLink(String id){
        if(links.size()>=MAX_NEIGHBORS||links.containsKey(id))return links.get(id);
        Link l=new Link(id);
        PeerConnection.RTCConfiguration cfg=new PeerConnection.RTCConfiguration(iceServers());
        cfg.sdpSemantics=PeerConnection.SdpSemantics.UNIFIED_PLAN;
        l.pc=factory.createPeerConnection(cfg,new PeerConnection.Observer(){
            @Override public void onSignalingChange(PeerConnection.SignalingState state){}
            @Override public void onIceConnectionChange(PeerConnection.IceConnectionState state){
                if(state==PeerConnection.IceConnectionState.FAILED||
                    state==PeerConnection.IceConnectionState.CLOSED)
                    main.post(()->closeLink(l));
            }
            @Override public void onIceConnectionReceivingChange(boolean value){}
            @Override public void onIceGatheringChange(PeerConnection.IceGatheringState state){}
            @Override public void onIceCandidate(IceCandidate c){
                try{
                    JSONObject m=authenticatedSignal(id,"candidate","",c.sdp,
                        c.sdpMid==null?"":c.sdpMid,c.sdpMLineIndex);
                    main.post(()->transport.send(m));
                }catch(Exception ignored){}
            }
            @Override public void onIceCandidatesRemoved(IceCandidate[] cs){}
            @Override public void onAddStream(MediaStream stream){}
            @Override public void onRemoveStream(MediaStream stream){}
            @Override public void onDataChannel(DataChannel channel){
                main.post(()->observe(l,channel));
            }
            @Override public void onRenegotiationNeeded(){}
            @Override public void onAddTrack(RtpReceiver receiver,MediaStream[] streams){}
        });
        if(l.pc==null)return null;
        links.put(id,l);
        List<IceCandidate> early=earlyCandidates.remove(id);
        if(early!=null)l.queued.addAll(early);
        return l;
    }
    private void observe(Link l,DataChannel dc){
        if(closed)return;
        l.dc=dc;
        dc.registerObserver(new DataChannel.Observer(){
            @Override public void onBufferedAmountChange(long amount){}
            @Override public void onStateChange(){
                if(dc.state()==DataChannel.State.OPEN)
                    main.post(()->{
                        transport.status("Direct network node connected.");
                        ping(l.id);
                    });
            }
            @Override public void onMessage(DataChannel.Buffer b){
                if(b.binary||b.data.remaining()>MAX_FRAME)return;
                byte[] data=new byte[b.data.remaining()];
                b.data.get(data);
                final String packet=new String(data,StandardCharsets.UTF_8);
                main.post(()->readPacket(l,packet));
            }
        });
    }
    private void sendSignal(Link l,String kind,SessionDescription description){
        try{
            JSONObject m=authenticatedSignal(l.id,kind,description.description,"","",-1);
            transport.send(m);
        }catch(Exception ignored){}
    }
    private abstract class SdpCallbacks implements SdpObserver {
        @Override public void onSetSuccess(){}
        @Override public void onSetFailure(String error){}
        @Override public void onCreateFailure(String error){}
        @Override public void onCreateSuccess(SessionDescription sdp){}
    }
    private void makeOffer(Link l){
        if(l.pc==null)return;
        DataChannel.Init init=new DataChannel.Init();
        DataChannel dc=l.pc.createDataChannel("xyool-global-control-v1",init);
        if(dc==null)return;
        observe(l,dc);
        l.pc.createOffer(new SdpCallbacks(){
            @Override public void onCreateSuccess(SessionDescription sd){
                l.pc.setLocalDescription(new SdpCallbacks(){
                    @Override public void onSetSuccess(){
                        main.post(()->sendSignal(l,"offer",sd));
                    }
                },sd);
            }
        },new MediaConstraints());
    }
    private void applyRemote(Link l,JSONObject msg,String kind){
        String sdp=msg.optString("sdp","");
        if(sdp.length()<80||sdp.length()>32000||!sdp.startsWith("v=0"))return;
        SessionDescription sd=new SessionDescription("offer".equals(kind)?
            SessionDescription.Type.OFFER:SessionDescription.Type.ANSWER,sdp);
        l.pc.setRemoteDescription(new SdpCallbacks(){
            @Override public void onSetSuccess(){
                main.post(()->{
                    l.remoteReady=true;
                    for(IceCandidate candidate:l.queued)l.pc.addIceCandidate(candidate);
                    l.queued.clear();
                    if("offer".equals(kind))makeAnswer(l);
                });
            }
        },sd);
    }
    private void makeAnswer(Link l){
        l.pc.createAnswer(new SdpCallbacks(){
            @Override public void onCreateSuccess(SessionDescription sd){
                l.pc.setLocalDescription(new SdpCallbacks(){
                    @Override public void onSetSuccess(){
                        main.post(()->sendSignal(l,"answer",sd));
                    }
                },sd);
            }
        },new MediaConstraints());
    }
    private void closeLink(Link l){
        if(links.get(l.id)!=l)return;
        links.remove(l.id);
        if(l.dc!=null){l.dc.unregisterObserver();l.dc.dispose();l.dc=null;}
        if(l.pc!=null){l.pc.close();l.pc.dispose();l.pc=null;}
    }
    private boolean allowPacket(){
        long now=System.currentTimeMillis();
        if(now-window>10000){window=now;trafficCount=0;}
        return trafficCount++<45;
    }
    private boolean dedup(String id){
        long now=System.currentTimeMillis();
        Iterator<Map.Entry<String,Long>> iter=seen.entrySet().iterator();
        while(iter.hasNext())if(iter.next().getValue()<now)iter.remove();
        if(seen.containsKey(id))return false;
        if(seen.size()>512)seen.remove(seen.keySet().iterator().next());
        seen.put(id,now+120000);
        return true;
    }
    private static String canonical(String origin,String target,String nonce,long when,String payload){
        return "xyool-overlay-v1|"+origin+"|"+target+"|"+nonce+"|"+when+"|"+payload;
    }
    private JSONObject signFrame(String to,String kind)throws Exception{
        JSONObject msg=new JSONObject();
        String nonce=PhoneIdentity.newNonce();
        long now=System.currentTimeMillis();
        msg.put("kind",kind);
        String payload=msg.toString();
        JSONObject frame=new JSONObject();
        frame.put("v",1);frame.put("origin",self);frame.put("target",to);
        frame.put("nonce",nonce);frame.put("when",now);
        frame.put("payload",payload);frame.put("key",PhoneIdentity.publicKey());
        frame.put("signature",PhoneIdentity.sign(canonical(self,to,nonce,now,payload)));
        frame.put("ttl",3);
        dedup(nonce);
        return frame;
    }
    public boolean ping(String id){
        if(!id.matches(ID_RE)||id.equals(self))return false;
        try{return broadcast(signFrame(id,"ping"),null);}
        catch(Exception ex){return false;}
    }
    private boolean broadcast(JSONObject frame,String except){
        if(!allowPacket())return false;
        boolean sent=false;
        String data=frame.toString();
        if(data.getBytes(StandardCharsets.UTF_8).length>MAX_FRAME)return false;
        for(Link l:links.values()){
            if(l.id.equals(except)||!l.open()||l.dc.bufferedAmount()>131072L)continue;
            ByteBuffer bytes=ByteBuffer.wrap(data.getBytes(StandardCharsets.UTF_8));
            if(l.dc.send(new DataChannel.Buffer(bytes,false)))sent=true;
        }
        return sent;
    }
    private void readPacket(Link via,String raw){
        if(!allowPacket()||raw.length()>MAX_FRAME)return;
        try{
            JSONObject packet=new JSONObject(raw);
            String from=packet.optString("origin",""),to=packet.optString("target","");
            String nonce=packet.optString("nonce","");
            String pub=packet.optString("key","");
            String sig=packet.optString("signature","");
            String payload=packet.optString("payload","");
            long ts=packet.optLong("when",-1);
            int ttl=packet.optInt("ttl",-1);
            if(packet.optInt("v")!=1||!from.matches(ID_RE)||!to.matches(ID_RE)||
               !nonce.matches("^[a-f0-9]{32}$")||payload.length()>256||
               ttl<1||ttl>3||Math.abs(System.currentTimeMillis()-ts)>60000L||
               !PhoneIdentity.verify(pub,sig,canonical(from,to,nonce,ts,payload))||
               !dedup(nonce))return;
            if(self.equals(to)){
                String manuallyPinned=PhoneIdentity.pinnedFingerprint(context,from);
                if(manuallyPinned==null ||
                    !manuallyPinned.equals(PhoneIdentity.fingerprintFor(pub)))return;
                JSONObject body=new JSONObject(payload);
                String kind=body.optString("kind","");
                if("ping".equals(kind)){
                    // A routed pong establishes packet reachability without
                    // revealing or forwarding phone audio or other user data.
                    broadcast(signFrame(from,"pong"),null);
                }else if("pong".equals(kind)){
                    transport.status("Authenticated multi-hop phone route reached "+from);
                }else if("peer-hint".equals(kind) && ttl==1){
                    // Only the directly linked, explicitly QR-verified sender
                    // may introduce a candidate. An introduction NEVER pins,
                    // enrolls, connects to, or authorizes the suggested peer.
                    String verified=PhoneIdentity.qrVerifiedFingerprint(context,from);
                    String subject=body.optString("subject","");
                    String subjectFingerprint=body.optString("fingerprint","");
                    if(PeerHintPolicy.receivable(self,via.id,from,to,subject,
                        subjectFingerprint,peerHintReceiving(),
                        verified!=null &&
                        verified.equals(PhoneIdentity.fingerprintFor(pub)))){
                        transport.status("Unverified peer introduction: "+subject+
                            ". Verify this person's identity QR independently.");
                    }
                }
            }else if(forwarding && ttl>1 && !self.equals(from)){
                packet.put("ttl",ttl-1);
                broadcast(packet,via.id);
            }
        }catch(Exception ignored){}
    }
}
