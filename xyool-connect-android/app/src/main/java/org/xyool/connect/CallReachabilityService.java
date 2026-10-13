package org.xyool.connect;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.media.Ringtone;
import android.media.RingtoneManager;
import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.media.AudioAttributes;
import android.net.Uri;
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

/**
 * Opt-in, user-visible persistent rendezvous connection for incoming Xyool ID calls.
 * The service owns the only remote /v1/id socket, including when IdCallActivity is
 * bound to it, so a notification's Answer action can reuse the existing call.
 * Media remains owned by IdCallActivity. No microphone is started in this service.
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
    private boolean incomingLocal=false;
    private RendezvousPool bootstrap;
    private URI connectedUri;

    private Listener listener;
    private JSONObject incoming;
    private Ringtone ringtone;
    private boolean registered=false,foreground=false,destroyed=false;
    private int reconnectDelayMs=2000;
    private final Runnable retry=()->openSocket();
    private final Runnable ringTimeout=()->{
        if(incoming!=null){
            sendType("reject");
            clearIncoming();
        }
    };

    @Override public void onCreate(){
        super.onCreate();
        prefs=getSharedPreferences("xyool_private",MODE_PRIVATE);
        notices=(NotificationManager)getSystemService(Context.NOTIFICATION_SERVICE);
        installChannels();
        if(prefs.getBoolean(PREF_ENABLED,false))startLocalNode();
        openSocket();
    }
    @Override public IBinder onBind(Intent intent){return binder;}
    @Override public int onStartCommand(Intent intent,int flags,int startId){
        String action=intent==null?ACTION_ENABLE:intent.getAction();
        if(ACTION_DECLINE.equals(action)){
            if(incoming!=null){sendType("reject");clearIncoming();}
            return foreground?START_STICKY:START_NOT_STICKY;
        }
        if(ACTION_DISABLE.equals(action)){
            prefs.edit().putBoolean(PREF_ENABLED,false).apply();
            foreground=false;
            stopForeground(STOP_FOREGROUND_REMOVE);
            if(incoming!=null){sendType("reject");clearIncoming();}
            stopLocalNode();
            stopSelf();
            return START_NOT_STICKY;
        }
        if(prefs.getBoolean(PREF_ENABLED,false)){
            foreground=true;
            showForeground();
            startLocalNode();
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
            if(incoming!=null){
                if(incomingLocal)next.onLocalPacket(incoming);
                else next.onPacket(incoming);
            }
        }else if(incoming!=null && foreground){
            showIncoming(incoming.optString("from","Unknown Xyool ID"));
        }
    }
    public boolean isRegistered(){return registered;}
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
        main.removeCallbacks(retry);
        bootstrap=null;
        WebSocketClient old=socket;socket=null;registered=false;
        if(old!=null)old.close();
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
        connectedUri=uri;
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
        boolean wasRegistered=registered;
        socket=null;registered=false;
        if(incoming!=null&&!incomingLocal)clearIncoming();
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
            if(incoming!=null){
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
        if(listener!=null)listener.onLocalPacket(packet);
    }

    private void process(JSONObject message){
        String type=message.optString("type","");
        if("registered".equals(type)){
            registered=true;reconnectDelayMs=2000;
            notifyConnection(true,"Internet calling online.");
        }
        if("incoming".equals(type)){
            if(incoming!=null){sendType("reject");return;}
            incoming=message;
            main.removeCallbacks(ringTimeout);
            main.postDelayed(ringTimeout,RING_LIMIT_MS);
            if(listener==null)showIncoming(message.optString("from","Unknown Xyool ID"));
        }
        if(("ended".equals(type)||"busy".equals(type)||"unavailable".equals(type)) && !incomingLocal){
            clearIncoming();
        }
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
    private void showForeground(){
        Notification n=new Notification.Builder(this,CHANNEL_STATUS)
            .setSmallIcon(android.R.drawable.ic_menu_call)
            .setContentTitle("Xyool Connect • reachability enabled")
            .setContentText(registered?"Local node + internet rendezvous online":
                (localNode!=null?"Local node active; internet reconnecting":"Connecting to Xyool Network…"))
            .setOngoing(true).setCategory(Notification.CATEGORY_SERVICE)
            .setContentIntent(launch(ACTION_VIEW,1931)).build();
        if(Build.VERSION.SDK_INT>=34)
            startForeground(STATUS_ID,n,ServiceInfo.FOREGROUND_SERVICE_TYPE_SPECIAL_USE);
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
        main.removeCallbacks(retry);main.removeCallbacks(ringTimeout);
        clearIncoming();
        stopLocalNode();
        WebSocketClient old=socket;socket=null;
        if(old!=null)old.close();
        super.onDestroy();
    }
}
