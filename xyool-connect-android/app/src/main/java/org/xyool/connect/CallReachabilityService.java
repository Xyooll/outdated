package org.xyool.connect;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.media.Ringtone;
import android.media.RingtoneManager;
import android.app.Service;
import android.Manifest;
import android.content.pm.PackageManager;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.media.AudioAttributes;
import android.net.Uri;
import android.net.ConnectivityManager;
import android.net.Network;
import android.net.NetworkCapabilities;
import android.net.NetworkRequest;
import android.os.Binder;
import android.os.Build;
import android.os.Handler;
import android.os.IBinder;
import android.os.Looper;
import android.content.pm.ServiceInfo;
import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;
import org.json.JSONObject;
import java.net.URI;
import java.util.List;
import java.util.Collections;
import org.webrtc.PeerConnection;

/**
 * Opt-in, user-visible persistent rendezvous connection for incoming Xyool ID calls.
 * The service owns the only remote /v1/id socket, including when IdCallActivity is
 * bound to it, so a notification's Answer action can reuse the existing call.
 * Active call media is owned by VoiceCallSession inside this service, not Activity.
 * The microphone is only promoted after an explicit user-authorized call.
 *
 * This is not a reliable wake-from-force-stop solution, an E2E identity guarantee,
 * or a replacement for Android Telecom / emergency calls.
 */
public final class CallReachabilityService extends Service {
    public static final String PREF_ENABLED="xyool_background_calls";
    public static final String ACTION_ENABLE="org.xyool.connect.ENABLE_REACHABILITY";
    public static final String ACTION_DISABLE="org.xyool.connect.DISABLE_REACHABILITY";
    public static final String ACTION_DECLINE="org.xyool.connect.DECLINE_INCOMING";
    public static final String ACTION_ANSWER="org.xyool.connect.ANSWER_INCOMING";
    public static final String ACTION_VIEW="org.xyool.connect.VIEW_INCOMING";
    public static final String ACTION_HANGUP="org.xyool.connect.HANGUP_ACTIVE_CALL";
    private static final String DEFAULT_SERVER="wss://xyool-id-signaling-production.up.railway.app/v1/id";
    private static final String CHANNEL_STATUS="xyool_call_reachability_v1";
    private static final String CHANNEL_INCOMING="xyool_incoming_calls_v1";
    private static final int STATUS_ID=18271;
    private static final int INCOMING_ID=18272;
    private static final long RING_LIMIT_MS=45000L;

    public interface Listener {
        void onPacket(JSONObject value);
        void onLocalPacket(JSONObject value);
        void onConnection(boolean online,String explanation);
        default void onVoiceStatus(String status){}
    }
    public final class LocalBinder extends Binder {
        public CallReachabilityService service(){return CallReachabilityService.this;}
    }
    private final IBinder binder=new LocalBinder();
    private final Handler main=new Handler(Looper.getMainLooper());
    private SharedPreferences prefs;
    private NotificationManager notices;
    private WebSocketClient socket;
    private LocalPeerNode localNode;
    private VoiceCallSession voice;
    private TurnLease currentTurnLease;
    private GlobalPhoneMesh globalMesh;
    private boolean incomingLocal=false;
    private RendezvousPool bootstrap;
    private ConnectivityManager networkManager;
    private ConnectivityManager.NetworkCallback networkCallback;

    private Listener listener;
    private JSONObject incoming;
    private Ringtone ringtone;
    private boolean registered=false,foreground=false,destroyed=false;
    private int reconnectDelayMs=2000;
    private final Runnable retry=()->openSocket();
    private final Runnable renewTurn=new Runnable(){
        @Override public void run(){
            if(!registered||socket==null||!socket.isOpen())return;
            sendType("turn-refresh");
            main.postDelayed(this,60L*60L*1000L);
        }
    };
    private final Runnable ringTimeout=()->{
        if(incoming!=null){
            sendType("reject");
            if(voice!=null)voice.expired();
            clearIncoming();
        }
    };

    @Override public void onCreate(){
        super.onCreate();
        prefs=getSharedPreferences("xyool_private",MODE_PRIVATE);
        notices=(NotificationManager)getSystemService(Context.NOTIFICATION_SERVICE);
        installChannels();
        voice=new VoiceCallSession(this,main,new VoiceCallSession.Host(){
            @Override public boolean enableMicrophoneForeground(){
                if(!foreground || !prefs.getBoolean(PREF_ENABLED,false) ||
                    checkSelfPermission(Manifest.permission.RECORD_AUDIO)!=PackageManager.PERMISSION_GRANTED)
                    return false;
                try{showForeground(true);return true;}
                catch(RuntimeException blocked){return false;}
            }
            @Override public boolean send(JSONObject frame,boolean local){
                return local?localSend(frame):CallReachabilityService.this.send(frame);
            }
            @Override public boolean dialLocal(String target){return localCall(target);}
            @Override public void closeLocal(){localClose();}
            @Override public List<PeerConnection.IceServer> currentTurnServers(){
                return currentTurnLease==null?Collections.emptyList():
                    currentTurnLease.servers(System.currentTimeMillis());
            }
            @Override public void status(String message){
                main.post(()->{
                    if(listener!=null)listener.onVoiceStatus(message);
                    if(foreground)showForeground();
                });
            }
            @Override public void sessionChanged(){
                main.post(()->{if(foreground)showForeground();});
            }
        });
        // Never open a socket or local node from onCreate. On Android 14+
        // foreground promotion must precede reachability initialization.
        // onStartCommand checks opt-in before starting any network listeners.
    }
    @Override public IBinder onBind(Intent intent){return binder;}
    @Override public int onStartCommand(Intent intent,int flags,int startId){
        String action=intent==null?ACTION_ENABLE:intent.getAction();
        if(ACTION_DECLINE.equals(action)){
            if(voice!=null&&voice.isIncoming())voice.reject();
            else if(incoming!=null)sendType("reject");
            clearIncoming();
            return foreground?START_STICKY:START_NOT_STICKY;
        }
        if(ACTION_HANGUP.equals(action)){
            if(voice!=null)voice.hangup();
            clearIncoming();
            return foreground?START_STICKY:START_NOT_STICKY;
        }
        if(ACTION_DISABLE.equals(action)){
            currentTurnLease=null;
            main.removeCallbacks(renewTurn);
            prefs.edit().putBoolean(PREF_ENABLED,false).apply();
            foreground=false;
            stopForeground(STOP_FOREGROUND_REMOVE);
            if(voice!=null)voice.hangup();
            if(incoming!=null){sendType("reject");clearIncoming();}
            stopLocalNode();
            unwatchWifi();
            stopGlobalMesh();
            stopSelf();
            return START_NOT_STICKY;
        }
        if(prefs.getBoolean(PREF_ENABLED,false)){
            // Developer mesh-forwarding and introduction switches have been
            // removed from the calling UI. Never preserve old hidden opt-ins:
            // keep both disabled until user-facing consent is redesigned.
            boolean relay=prefs.getBoolean(GlobalPhoneMesh.PREF_RELAY,false);
            boolean hints=prefs.getBoolean(GlobalPhoneMesh.PREF_PEER_HINTS,false);
            if(relay||hints){
                prefs.edit().putBoolean(GlobalPhoneMesh.PREF_RELAY,false)
                    .putBoolean(GlobalPhoneMesh.PREF_PEER_HINTS,false).apply();
                if(globalMesh!=null){
                    globalMesh.setForwarding(false);
                    globalMesh.setPeerHintReceiving(false);
                }
            }
            foreground=true;
            showForeground();
            watchWifi();
            startLocalNode();
            startGlobalMesh();
            if(cloudAllowed())openSocket();
            return START_STICKY;
        }
        stopSelf();
        return START_NOT_STICKY;
    }
    public void setListener(Listener next){
        listener=next;
        if(next!=null){
            stopRing();
            notices.cancel(INCOMING_ID);
            next.onConnection(registered,registered?"Internet calling online.":"Connecting to Xyool calling network…");
            if(voice!=null&&voice.hasSession())next.onVoiceStatus(voice.state());
            if(incoming!=null){
                if(incomingLocal)next.onLocalPacket(incoming);
                else next.onPacket(incoming);
            }
        }else if(incoming!=null && foreground){
            showIncoming(incoming.optString("from","Unknown Xyool ID"));
        }
    }
    public boolean isRegistered(){return registered;}
    public int globalPeerCount(){return globalMesh==null?0:globalMesh.neighbors();}
    public boolean hasVoiceSession(){return voice!=null&&voice.hasSession();}
    public boolean hasVoiceAudio(){return voice!=null&&voice.hasAudio();}
    public boolean hasIncomingVoice(){return voice!=null&&voice.isIncoming();}
    public String voicePeerId(){return voice==null?null:voice.peerId();}
    public String voiceState(){return voice==null?"":voice.state();}
    public String voiceDiagnostics(){
        String base=voice==null?"No call diagnostics.":voice.diagnostics();
        return base+"\nServer-issued TURN lease usable: "+
            (currentTurnLease!=null&&currentTurnLease.validAt(System.currentTimeMillis())?
                "yes":"no");
    }
    public boolean dialVoice(String target,boolean local){
        return foreground&&voice!=null&&voice.dial(target,local);
    }
    public boolean dialRelayTest(String target){
        return foreground&&registered&&voice!=null&&
            currentTurnLease!=null&&
            currentTurnLease.validAt(System.currentTimeMillis())&&
            voice.dial(target,false,true);
    }
    public boolean acceptVoice(){return voice!=null&&voice.accept();}
    public void declineVoice(){if(voice!=null)voice.reject();clearIncoming();}
    public void hangupVoice(){if(voice!=null)voice.hangup();clearIncoming();}
    public void muteVoice(){if(voice!=null)voice.toggleMute();}
    public void speakerVoice(){if(voice!=null)voice.toggleSpeaker();}
    public boolean hasIncoming(){return incoming!=null;}
    public boolean hasLocalPeer(String id){return localNode!=null&&localNode.hasPeer(id);}
    public int localPeerCount(){return localNode==null?0:localNode.peerCount();}
    public boolean localCall(String to){return localNode!=null&&localNode.call(to);}
    public boolean localSend(JSONObject message){
        if(localNode==null)return false;
        boolean ok=localNode.send(message);
        if(ok && ("accept".equals(message.optString("type")) ||
            "reject".equals(message.optString("type"))))clearIncoming();
        return ok;
    }
    public void localClose(){if(localNode!=null)localNode.closeSession();}
    public void reloadNetworkPolicy(){
        if(cloudAllowed())reconnectNow();
        else{
            main.removeCallbacks(retry);
            bootstrap=null;
            WebSocketClient old=socket;socket=null;registered=false;
            if(old!=null)old.close();
            notifyConnection(false,"Direct-only local node mode.");
        }
    }
    public void refreshLocal(){
        if(localNode!=null)stopLocalNode();
        if(prefs.getBoolean(PREF_ENABLED,false))startLocalNode();
    }
    public boolean send(JSONObject message){
        if(socket==null||!socket.isOpen())return false;
        try{
            socket.send(message.toString());
            if("accept".equals(message.optString("type"))||
                "reject".equals(message.optString("type")))clearIncoming();
            return true;
        }catch(RuntimeException ignored){return false;}
    }
    public void reconnectNow(){
        currentTurnLease=null;
        main.removeCallbacks(renewTurn);
        main.removeCallbacks(retry);
        bootstrap=null;
        WebSocketClient old=socket;socket=null;registered=false;
        if(old!=null)old.close();
        if(globalMesh!=null)globalMesh.rendezvousOffline();
        openSocket();
    }
    private void sendType(String type){
        try{JSONObject j=new JSONObject();j.put("type",type);
            if(incomingLocal)localSend(j); else send(j);}
        catch(Exception ignored){}
    }
    private boolean cloudAllowed(){
        return BridgePolicy.allowsCloud(BridgePolicy.sanitize(
            prefs.getString(BridgePolicy.PREF_MODE,BridgePolicy.HYBRID)));
    }
    private void openSocket(){
        if(destroyed||!cloudAllowed()||socket!=null)return;
        String id=prefs.getString("xyool_id",""),token=prefs.getString("xyool_auth","");
        if(!id.matches("^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$")
            ||!token.matches("^[0-9a-f]{64}$"))return;
        URI uri;
        try{
            if(bootstrap==null)bootstrap=new RendezvousPool(
                prefs.getString("xyool_id_server",DEFAULT_SERVER),
                prefs.getString(RendezvousPool.PREF_NODES,""));
            uri=bootstrap.current();
        }catch(Exception invalid){notifyConnection(false,"Invalid Xyool bootstrap settings.");return;}
        final String ownId=id,ownToken=token;
        WebSocketClient candidate=new WebSocketClient(uri){
            @Override public void onOpen(ServerHandshake handshake){
                try{
                    JSONObject registration=new JSONObject();
                    registration.put("type","register");
                    registration.put("id",ownId);
                    registration.put("token",ownToken);
                    send(registration.toString());
                }catch(Exception ignored){}
            }
            @Override public void onMessage(String raw){
                if(raw.length()>50000)return;
                try{
                    JSONObject packet=new JSONObject(raw);
                    main.post(()->{
                        if(socket==this&&!destroyed)process(packet);
                    });
                }catch(Exception ignored){}
            }
            @Override public void onClose(int code,String reason,boolean remote){
                main.post(()->lost(this));
            }
            @Override public void onError(Exception error){
                main.post(()->lost(this));
            }
        };
        socket=candidate;
        candidate.setConnectionLostTimeout(30);
        notifyConnection(false,"Connecting to Xyool calling network…");
        candidate.connect();
    }
    private void lost(WebSocketClient failed){
        if(socket!=failed||destroyed)return;
        currentTurnLease=null;
        main.removeCallbacks(renewTurn);
        boolean wasRegistered=registered;
        socket=null;registered=false;
        if(incoming!=null&&!incomingLocal)clearIncoming();
        if(globalMesh!=null)globalMesh.rendezvousOffline();
        if(bootstrap!=null)bootstrap.failover();
        if(wasRegistered || listener!=null)packetEnded();
        notifyConnection(false,"Xyool signaling disconnected; reconnecting…");
        if(listener!=null||foreground){
            main.removeCallbacks(retry);
            main.postDelayed(retry,reconnectDelayMs);
            reconnectDelayMs=Math.min(60000,reconnectDelayMs*2);
        }
    }
    private void packetEnded(){
        if(listener!=null){
            try{JSONObject ended=new JSONObject();ended.put("type","ended");
                ended.put("reason","network-disconnected");listener.onPacket(ended);
            }catch(Exception ignored){}
        }
    }
    private void startGlobalMesh(){
        if(globalMesh!=null||!prefs.getBoolean(PREF_ENABLED,false))return;
        String id=prefs.getString("xyool_id","");
        if(!id.matches("^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$"))return;
        globalMesh=new GlobalPhoneMesh(this,main,id,new GlobalPhoneMesh.Transport(){
            @Override public void send(JSONObject packet){
                if(socket!=null&&socket.isOpen())socket.send(packet.toString());
            }
            @Override public void status(String message){
                main.post(()->{
                    if(listener!=null)listener.onConnection(registered,message);
                    if(foreground)showForeground();
                });
            }
        });
        if(registered)globalMesh.connected();
    }
    private void stopGlobalMesh(){
        GlobalPhoneMesh old=globalMesh;
        globalMesh=null;
        if(old!=null){
            if(socket!=null&&socket.isOpen())
                socket.send("{\"type\":\"mesh-disable\"}");
            old.stop();
        }
    }
    private void watchWifi(){
        if(networkCallback!=null)return;
        networkManager=(ConnectivityManager)getSystemService(Context.CONNECTIVITY_SERVICE);
        if(networkManager==null)return;
        networkCallback=new ConnectivityManager.NetworkCallback(){
            @Override public void onAvailable(Network network){
                main.post(()->{
                    if(prefs.getBoolean(PREF_ENABLED,false))startLocalNode();
                });
            }
            @Override public void onLost(Network network){
                main.post(()->{
                    if(!LocalPeerNode.onWifi(CallReachabilityService.this))stopLocalNode();
                });
            }
        };
        try{
            NetworkRequest request=new NetworkRequest.Builder()
                .addTransportType(NetworkCapabilities.TRANSPORT_WIFI).build();
            networkManager.registerNetworkCallback(request,networkCallback);
        }catch(RuntimeException ex){networkCallback=null;}
    }
    private void unwatchWifi(){
        if(networkManager!=null&&networkCallback!=null){
            try{networkManager.unregisterNetworkCallback(networkCallback);}
            catch(RuntimeException ignored){}
        }
        networkCallback=null;
    }
    private void startLocalNode(){
        if(localNode!=null||!LocalPeerNode.onWifi(this))return;
        String id=prefs.getString("xyool_id","");
        if(!id.matches("^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$"))return;
        localNode=new LocalPeerNode(this,id,new LocalPeerNode.Listener(){
            @Override public void onPeerChanged(String id,boolean online){
                main.post(()->notifyConnection(registered,online?"Local peer discovered.":"Local peer disconnected."));
            }
            @Override public void onPacket(JSONObject packet){
                main.post(()->processLocal(packet));
            }
            @Override public void onNodeStatus(String explanation){
                main.post(()->notifyConnection(registered,explanation));
            }
        });
        localNode.start();
    }
    private void stopLocalNode(){
        LocalPeerNode old=localNode;localNode=null;
        if(old!=null)old.stop();
    }
    private void processLocal(JSONObject packet){
        if(destroyed)return;
        String type=packet.optString("type","");
        if("incoming".equals(type)){
            if(incoming!=null||(voice!=null&&voice.hasSession())){
                if(localNode!=null){
                    try{JSONObject rejected=new JSONObject();rejected.put("type","reject");
                        localNode.send(rejected);}catch(Exception ignored){}
                }
                return;
            }
            incomingLocal=true;
            incoming=packet;
            main.removeCallbacks(ringTimeout);
            main.postDelayed(ringTimeout,RING_LIMIT_MS);
            if(listener==null)showIncoming(packet.optString("from","Unknown nearby ID"));
        }else if(("ended".equals(type)||"busy".equals(type)||"unavailable".equals(type)) && incomingLocal){
            clearIncoming();
        }
        if(voice!=null)voice.onPacket(packet,true);
        if(listener!=null)listener.onLocalPacket(packet);
    }

    private void process(JSONObject message){
        String type=message.optString("type","");
        if("mesh-peers".equals(type)||"mesh-signal".equals(type)){
            if(globalMesh!=null)globalMesh.fromRendezvous(message);
            return;
        }
        if("registered".equals(type)){
            registered=true;reconnectDelayMs=2000;
            main.removeCallbacks(renewTurn);
            main.postDelayed(renewTurn,60L*60L*1000L);
            if(globalMesh!=null)globalMesh.connected();
            notifyConnection(true,"Internet calling online.");
        }
        if("turn-credentials".equals(type)){
            TurnLease lease=TurnLease.fromMessage(message,System.currentTimeMillis());
            if(lease!=null){
                currentTurnLease=lease;
                notifyConnection(registered,"Xyool TURN fallback ready for new calls.");
            }
            return; // TURN credentials never reach the Activity or diagnostics.
        }
        if("turn-unavailable".equals(type)){
            currentTurnLease=null;
            return;
        }
        if("incoming".equals(type)){
            if(incoming!=null||(voice!=null&&voice.hasSession())){
                // Reject this new internet invitation without accidentally rejecting
                // an already-ringing nearby call or clearing its notification.
                if(socket!=null&&socket.isOpen())socket.send("{\"type\":\"reject\"}");
                return;
            }
            incomingLocal=false;
            incoming=message;
            main.removeCallbacks(ringTimeout);
            main.postDelayed(ringTimeout,RING_LIMIT_MS);
            if(listener==null)showIncoming(message.optString("from","Unknown Xyool ID"));
        }
        if(("ended".equals(type)||"busy".equals(type)||"unavailable".equals(type)) && !incomingLocal){
            clearIncoming();
        }
        if(voice!=null)voice.onPacket(message,false);
        if(listener!=null)listener.onPacket(message);
    }
    private void notifyConnection(boolean online,String message){
        if(listener!=null)listener.onConnection(online,message);
        if(foreground)showForeground();
    }
    private void installChannels(){
        if(notices==null)return;
        NotificationChannel status=new NotificationChannel(CHANNEL_STATUS,
            "Xyool background reachability",NotificationManager.IMPORTANCE_LOW);
        status.setDescription("Opt-in online Xyool ID call connection");
        notices.createNotificationChannel(status);
        NotificationChannel ringing=new NotificationChannel(CHANNEL_INCOMING,
            "Xyool incoming calls",NotificationManager.IMPORTANCE_HIGH);
        ringing.setDescription("Incoming Xyool ID invitations");
        ringing.setSound(null,null); // Ringtone is started/stopped by the service.
        notices.createNotificationChannel(ringing);
    }
    private PendingIntent launch(String action,int request){
        Intent i=new Intent(this,IdCallActivity.class);
        i.setAction(action);
        i.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP|Intent.FLAG_ACTIVITY_SINGLE_TOP);
        return PendingIntent.getActivity(this,request,i,
            PendingIntent.FLAG_UPDATE_CURRENT|PendingIntent.FLAG_IMMUTABLE);
    }
    private void showForeground(){showForeground(voice!=null&&voice.hasAudio());}
    private void showForeground(boolean withMicrophone){
        boolean active=voice!=null&&voice.hasSession();
        Notification.Builder builder=new Notification.Builder(this,CHANNEL_STATUS)
            .setSmallIcon(android.R.drawable.ic_menu_call)
            .setContentTitle(active?"Xyool Connect • call in progress":
                "Xyool Connect • reachability enabled")
            .setContentText(active?("Voice "+voice.peerId()+" • tap to return"):
                globalPeerCount()>0?
                ("P2P mesh online • "+globalPeerCount()+" direct nodes"):
                (registered?"Xyool rendezvous registered":
                (!cloudAllowed()?"Direct-only local node mode":
                (localNode!=null?"Local node active; bootstrap reconnecting":"Connecting to Xyool Network…"))))
            .setOngoing(true).setCategory(active?Notification.CATEGORY_CALL:Notification.CATEGORY_SERVICE)
            .setContentIntent(launch(ACTION_VIEW,1931));
        if(active){
            Intent hangup=new Intent(this,CallReachabilityService.class)
                .setAction(ACTION_HANGUP);
            PendingIntent end=PendingIntent.getService(this,1940,hangup,
                PendingIntent.FLAG_UPDATE_CURRENT|PendingIntent.FLAG_IMMUTABLE);
            builder.addAction(android.R.drawable.ic_menu_close_clear_cancel,"Hang up",end);
        }
        Notification n=builder.build();
        if(Build.VERSION.SDK_INT>=34)
            startForeground(STATUS_ID,n,ServiceInfo.FOREGROUND_SERVICE_TYPE_SPECIAL_USE|
                (withMicrophone?ServiceInfo.FOREGROUND_SERVICE_TYPE_MICROPHONE:0));
        else startForeground(STATUS_ID,n);
    }
    private void showIncoming(String from){
        if(!foreground)return;
        Intent decline=new Intent(this,CallReachabilityService.class);
        decline.setAction(ACTION_DECLINE);
        PendingIntent declinePending=PendingIntent.getService(this,1934,decline,
            PendingIntent.FLAG_UPDATE_CURRENT|PendingIntent.FLAG_IMMUTABLE);
        Notification n=new Notification.Builder(this,CHANNEL_INCOMING)
            .setSmallIcon(android.R.drawable.ic_menu_call)
            .setContentTitle("Incoming Xyool call")
            .setContentText("From "+from)
            .setCategory(Notification.CATEGORY_CALL)
            .setVisibility(Notification.VISIBILITY_PRIVATE)
            .setOngoing(true)
            .setContentIntent(launch(ACTION_VIEW,1932))
            .addAction(android.R.drawable.ic_menu_call,"Answer",launch(ACTION_ANSWER,1933))
            .addAction(android.R.drawable.ic_menu_close_clear_cancel,"Decline",declinePending)
            .build();
        notices.notify(INCOMING_ID,n);
        ring();
    }
    private void ring(){
        stopRing();
        try{
            Uri uri=RingtoneManager.getDefaultUri(RingtoneManager.TYPE_RINGTONE);
            if(uri==null)return;
            ringtone=RingtoneManager.getRingtone(getApplicationContext(),uri);
            if(ringtone!=null){
                ringtone.setAudioAttributes(new AudioAttributes.Builder()
                    .setUsage(AudioAttributes.USAGE_NOTIFICATION_RINGTONE)
                    .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION).build());
                ringtone.play();
            }
        }catch(RuntimeException ignored){ringtone=null;}
    }
    private void stopRing(){
        if(ringtone==null)return;
        try{ringtone.stop();}catch(RuntimeException ignored){}
        ringtone=null;
    }
    private void clearIncoming(){
        incoming=null;
        incomingLocal=false;
        main.removeCallbacks(ringTimeout);
        stopRing();
        if(notices!=null)notices.cancel(INCOMING_ID);
    }
    @Override public void onDestroy(){
        destroyed=true;foreground=false;listener=null;
        currentTurnLease=null;
        main.removeCallbacks(renewTurn);
        main.removeCallbacks(retry);main.removeCallbacks(ringTimeout);
        clearIncoming();
        if(voice!=null)voice.destroy();
        unwatchWifi();
        stopGlobalMesh();
        stopLocalNode();
        WebSocketClient old=socket;socket=null;
        if(old!=null)old.close();
        super.onDestroy();
    }
}
