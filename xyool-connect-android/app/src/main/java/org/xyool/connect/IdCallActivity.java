package org.xyool.connect;

import android.Manifest;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.ActivityNotFoundException;
import android.content.ClipData;
import android.content.ClipboardManager;
import android.content.Context;
import android.content.ComponentName;
import android.content.ServiceConnection;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.graphics.drawable.GradientDrawable;
import android.graphics.Bitmap;
import android.graphics.Color;
import android.widget.ImageView;
import android.widget.Toast;
import com.google.zxing.BarcodeFormat;
import com.google.zxing.EncodeHintType;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.common.BitMatrix;
import java.util.EnumMap;
import java.util.Map;
import android.media.AudioManager;
import android.media.Ringtone;
import android.media.RingtoneManager;
import android.os.Bundle;
import android.os.Build;
import android.os.IBinder;
import android.text.InputType;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import java.net.URI;
import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;
import org.json.JSONObject;
import org.webrtc.AudioSource;
import org.webrtc.AudioTrack;
import org.webrtc.DataChannel;
import org.webrtc.IceCandidate;
import org.webrtc.MediaConstraints;
import org.webrtc.MediaStream;
import org.webrtc.PeerConnection;
import org.webrtc.PeerConnectionFactory;
import org.webrtc.RtpReceiver;
import org.webrtc.SdpObserver;
import org.webrtc.SessionDescription;

/** Xyool's simplified ID-to-ID calling alpha.
 * Open both phones, share ID, enter ID, tap Call, Accept or Decline.
 * The user never exchanges SDP/ICE setup strings.
 *
 * This requires a separately hosted WSS Xyool signaling service; it is not
 * usable as an always-online phone service until a real endpoint exists.
 */
public final class IdCallActivity extends Activity {
    private static final int BG=0xff0c1822, PANEL=0xff192f3b, FG=0xfff1faf7,
        MUTED=0xffaec8cf, ACCENT=0xff68dbc3, ERROR=0xffffb9a7;
    private static final String ALPHABET="ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
    private static final int MIC_REQUEST=481;
    private static final String DEFAULT_SERVER="wss://xyool-id-signaling-production.up.railway.app/v1/id";
    // Public STUN gives WebRTC public/translated ICE candidates when on separate networks.
    // This is used ONLY for internet calls. Enter "off" in Advanced to disable it.
    // Cloudflare receives source IP and basic binding metadata, not call audio.
    private static final String DEFAULT_STUN="stun:stun.cloudflare.com:3478";
    private SharedPreferences prefs;
    private String id, token;
    private TextView stateLabel;
    private EditText targetInput,serverInput,stunInput,turnInput,turnUser,turnPass,nodesInput;
    private LinearLayout body, advancedPanel;
    private CallReachabilityService cloud;
    private boolean cloudBound;
    private boolean autoAnswerRequested;
    private Button reachabilityButton;
    private final ServiceConnection cloudLink=new ServiceConnection(){
        @Override public void onServiceConnected(ComponentName name,IBinder binder){
            cloud=((CallReachabilityService.LocalBinder)binder).service();
            if(hasReachability()&&nearby!=null)nearby.stop();
            cloud.setListener(new CallReachabilityService.Listener(){
                @Override public void onPacket(JSONObject message){received(message,false);}
                @Override public void onLocalPacket(JSONObject message){received(message,true);}
                @Override public void onConnection(boolean online,String explanation){
                    registered=online;
                    if(!disposed && waitingId==null)connectionStatus();
                }
            });
            if(autoAnswerRequested){
                // A previously expired notification must not auto-answer the next call.
                if(!cloud.hasIncoming()){
                    autoAnswerRequested=false;
                    status("That incoming call is no longer available.");
                }
            }
        }
        @Override public void onServiceDisconnected(ComponentName name){
            cloud=null;registered=false;
            if(!disposed)connectionStatus();
        }
    };
    private LocalPeerNode nearby;
    private boolean usingLocal;
    private boolean registered, outgoing, peerActive, remoteReady, callAuthorized, disposed;
    private String waitingId;
    private PeerConnectionFactory factory;
    private PeerConnection peer;
    private AudioSource audioSource;
    private AudioTrack microphone;
    private AudioManager audioManager;
    private AlertDialog incomingAlert;
    private Ringtone incomingRingtone;
    private int oldMode=AudioManager.MODE_NORMAL;
    private boolean oldSpeaker;
    private final List<IceCandidate> pendingCandidates=new ArrayList<>();
    private Runnable pendingMicrophone;
    private String callStatus="Checking Xyool calling service…";
    private boolean muted;
    private IcePathInspector iceDiagnostics=new IcePathInspector();

    private String bridgeMode(){
        return BridgePolicy.sanitize(prefs.getString(BridgePolicy.PREF_MODE,BridgePolicy.HYBRID));
    }
    private void selectBridgeMode(String next){
        String mode=BridgePolicy.sanitize(next);
        if(waitingId!=null || peerActive){
            status("Finish your current call before changing network mode.");
            return;
        }
        prefs.edit().putString(BridgePolicy.PREF_MODE,mode).apply();
        if(cloud!=null)cloud.reloadNetworkPolicy();
        else{
            disconnect();
            if(BridgePolicy.allowsCloud(mode)||hasReachability())connect();
        }
        connectionStatus();
        status(BridgePolicy.description(mode));
    }
    private void copyNetworkReport(){
        String report="Xyool Connect network report (no IDs/IP addresses)\n" +
            "Mode: "+bridgeMode()+
            "\nLocal Wi-Fi available: "+LocalPeerNode.onWifi(this)+
            "\nNearby peers: "+(cloud!=null&&hasReachability()?cloud.localPeerCount():(nearby==null?0:nearby.peerCount()))+
            "\nCloud registered: "+(BridgePolicy.allowsCloud(bridgeMode())&&registered)+
            "\n"+iceDiagnostics.summary()+
            "\n"+iceDiagnostics.interpretation();
        ClipboardManager cb=(ClipboardManager)getSystemService(Context.CLIPBOARD_SERVICE);
        if(cb!=null){
            cb.setPrimaryClip(ClipData.newPlainText("Xyool network report",report));
            status("Sanitized network report copied. No IDs, SDP or IP addresses included.");
        }
    }

    @Override public void onCreate(Bundle b){
        super.onCreate(b);
        prefs=getSharedPreferences("xyool_private",MODE_PRIVATE);
        autoAnswerRequested=CallReachabilityService.ACTION_ANSWER.equals(getIntent().getAction());
        id=prefs.getString("xyool_id","");
        token=prefs.getString("xyool_auth","");
        if(!id.matches("^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$")||
            !token.matches("^[0-9a-f]{64}$")){
            makeIdentity();
        }
        getWindow().setStatusBarColor(BG);
        getWindow().setNavigationBarColor(BG);
        nearby=new LocalPeerNode(this,id,new LocalPeerNode.Listener(){
            @Override public void onPeerChanged(String peerId,boolean online){
                runOnUiThread(()->{
                    if(!peerActive&&waitingId==null)connectionStatus();
                });
            }
            @Override public void onPacket(JSONObject packet){
                runOnUiThread(()->received(packet,true));
            }
            @Override public void onNodeStatus(String message){
                // Local discovery is informational, never proof of peer identity.
                if(message.contains("failed")||message.contains("couldn't")||message.contains("requires"))
                    status(message);
                else connectionStatus();
            }
        });
        render();
        connect();
    }
    @Override protected void onNewIntent(Intent intent){
        super.onNewIntent(intent);
        setIntent(intent);
        if(CallReachabilityService.ACTION_ANSWER.equals(intent.getAction())){
            autoAnswerRequested=true;
            if(waitingId!=null && !outgoing && !peerActive){
                autoAnswerRequested=false;
                acceptIncomingCall();
            }
        }
    }
    @Override protected void onResume(){
        super.onResume();
        if(nearby!=null && !hasReachability())nearby.start();
        if(prefs!=null && !cloudBound && (hasReachability()||BridgePolicy.allowsCloud(bridgeMode())))
            connect();
    }
    @Override protected void onStop(){
        stopIncomingRing();
        // WebRTC media is activity-owned in this alpha. A background calling
        // service must not leave a ghost active call after the UI stops.
        if(waitingId!=null){
            packet("hangup");
            endMedia();
            status("Call ended when the calling screen closed.");
        }
        disconnect();
        if(nearby!=null)nearby.stop();
        super.onStop();
    }
    private void makeIdentity(){
        SecureRandom random=new SecureRandom();
        StringBuilder letters=new StringBuilder();
        for(int i=0;i<12;i++)letters.append(ALPHABET.charAt(random.nextInt(ALPHABET.length())));
        id="XY-"+letters.substring(0,4)+"-"+letters.substring(4,8)+"-"+letters.substring(8);
        byte[] secret=new byte[32];random.nextBytes(secret);
        StringBuilder hex=new StringBuilder(64);
        for(byte b:secret)hex.append(String.format(Locale.US,"%02x",b&0xff));
        token=hex.toString();
        prefs.edit().putString("xyool_id",id).putString("xyool_auth",token).apply();
    }
    private int dp(int n){return (int)(n*getResources().getDisplayMetrics().density+.5f);}
    private LinearLayout column(){LinearLayout l=new LinearLayout(this);l.setOrientation(1);return l;}
    private TextView text(String v,int size,int color,boolean bold){
        TextView t=new TextView(this);t.setText(v);t.setTextSize(size);t.setTextColor(color);
        if(bold)t.setTypeface(null,1);
        return t;
    }
    private GradientDrawable background(int c){
        GradientDrawable g=new GradientDrawable();g.setColor(c);g.setCornerRadius(dp(14));
        g.setStroke(dp(1),0xff365968);return g;
    }
    private void space(LinearLayout l,int n){l.addView(new View(this),new LinearLayout.LayoutParams(dp(1),dp(n)));}
    private LinearLayout panel(){
        LinearLayout l=column();l.setPadding(dp(15),dp(15),dp(15),dp(15));
        l.setBackground(background(PANEL));
        LinearLayout.LayoutParams lp=new LinearLayout.LayoutParams(-1,-2);lp.bottomMargin=dp(13);
        body.addView(l,lp);return l;
    }
    private Button button(LinearLayout parent,String label,boolean primary,View.OnClickListener action){
        Button b=new Button(this);b.setAllCaps(false);b.setText(label);b.setTextSize(15);
        b.setTextColor(primary?BG:FG);b.setBackground(background(primary?ACCENT:0xff294d59));
        b.setOnClickListener(action);parent.addView(b,new LinearLayout.LayoutParams(-1,dp(48)));return b;
    }
    private EditText input(LinearLayout parent,String hint,String value){
        EditText e=new EditText(this);e.setSingleLine(true);
        e.setTextSize(16);e.setTextColor(FG);e.setHintTextColor(0xff91adb6);e.setHint(hint);
        e.setInputType(InputType.TYPE_CLASS_TEXT);
        e.setPadding(dp(12),dp(12),dp(12),dp(12));e.setBackground(background(0xff0e2532));
        if(value!=null)e.setText(value);
        parent.addView(e,new LinearLayout.LayoutParams(-1,-2));
        return e;
    }
    // Calling-first single-screen UI. Debug and relay controls remain in Settings.
    private void render(){
        LinearLayout root=column();
        root.setBackgroundColor(BG);
        ScrollView scroll=new ScrollView(this);
        scroll.setFillViewport(false);
        body=column();
        body.setPadding(dp(16),dp(18),dp(16),dp(28));
        scroll.addView(body);
        root.addView(scroll,new LinearLayout.LayoutParams(-1,0,1f));
        setContentView(root);

        body.addView(text("XYOOL CONNECT",14,ACCENT,true));
        space(body,3);
        body.addView(text("Call by Xyool ID",26,FG,true));
        space(body,10);

        LinearLayout net=panel();
        net.addView(text("NETWORK",12,MUTED,true));
        space(net,4);
        stateLabel=text(callStatus,14,FG,false);
        net.addView(stateLabel);

        LinearLayout self=panel();
        self.addView(text("YOUR ID",12,MUTED,true));
        space(self,7);
        TextView address=text(id,21,ACCENT,true);
        address.setTextIsSelectable(true);
        address.setGravity(Gravity.CENTER_HORIZONTAL);
        self.addView(address);
        space(self,8);
        button(self,"Copy my ID",false,v->{
            ClipboardManager clip=(ClipboardManager)getSystemService(Context.CLIPBOARD_SERVICE);
            if(clip!=null)clip.setPrimaryClip(ClipData.newPlainText("Xyool ID",id));
            status("ID copied.");
        });
        space(self,6);
        button(self,"Show my QR code",false,v->showMyQr());
        space(self,6);
        button(self,"Share my ID",false,v->{
            Intent send=new Intent(Intent.ACTION_SEND);
            send.setType("text/plain");
            send.putExtra(Intent.EXTRA_TEXT,"Call me on Xyool Connect: "+id);
            try{startActivity(Intent.createChooser(send,"Share Xyool ID"));}
            catch(ActivityNotFoundException ex){status("No sharing app found.");}
        });

        LinearLayout dial=panel();
        dial.addView(text("CALL SOMEONE",12,MUTED,true));
        space(dial,7);
        targetInput=input(dial,"Xyool ID",null);
        space(dial,7);
        button(dial,"Scan their QR code",false,v->scanIdQr());
        space(dial,11);
        button(dial,"Call",true,v->call());
        space(dial,6);
        button(dial,"Hang up",false,v->hangup());
        space(dial,6);
        button(dial,"Mute / Unmute",false,v->toggleMute());

        LinearLayout settings=panel();
        settings.addView(text("CALL SETTINGS",12,MUTED,true));
        space(settings,7);
        reachabilityButton=button(settings,"Background call alerts: OFF",false,
            v->toggleReachability());
        updateReachabilityButton();
        space(settings,6);
        button(settings,"Advanced network settings ▾",false,v->
            advancedPanel.setVisibility(advancedPanel.getVisibility()==View.GONE?
                View.VISIBLE:View.GONE));
        space(settings,4);
        advancedPanel=column();
        advancedPanel.setVisibility(View.GONE);
        settings.addView(advancedPanel);
        advancedPanel.addView(text("Direct-only uses nearby Wi-Fi discovery; Hybrid tries nearby first and uses rendezvous nodes when needed. Internet media prefers direct WebRTC; TURN is optional fallback.",12,MUTED,false));
        space(advancedPanel,8);
        button(advancedPanel,"Direct-only • Local calls",false,
            v->selectBridgeMode(BridgePolicy.DIRECT_ONLY));
        space(advancedPanel,5);
        button(advancedPanel,"Hybrid • Across networks",false,
            v->selectBridgeMode(BridgePolicy.HYBRID));
        space(advancedPanel,8);
        button(advancedPanel,"Refresh network",false,v->{
            if(cloud!=null&&hasReachability())cloud.refreshLocal();
            else if(nearby!=null)nearby.start();
            if(cloud!=null)cloud.reloadNetworkPolicy();
            else if(BridgePolicy.allowsCloud(bridgeMode())){disconnect();connect();}
            else connectionStatus();
        });
        space(advancedPanel,6);
        button(advancedPanel,"Copy connection report",false,v->copyNetworkReport());
        space(advancedPanel,9);
        serverInput=input(advancedPanel,"Signaling WSS address",prefs.getString("xyool_id_server",DEFAULT_SERVER));
        space(advancedPanel,7);
        advancedPanel.addView(text("Only add nodes run by operators you trust. These nodes receive your current Xyool registration credential; this is not a public trustless DHT.",12,MUTED,false));
        space(advancedPanel,6);
        nodesInput=input(advancedPanel,"Trusted additional WSS nodes (comma separated)",
            prefs.getString(RendezvousPool.PREF_NODES,""));
        space(advancedPanel,7);
        stunInput=input(advancedPanel,"STUN (blank=automatic, off=disabled)",prefs.getString("xyool_stun",""));
        space(advancedPanel,7);
        turnInput=input(advancedPanel,"TURN (optional)",prefs.getString("xyool_turn",""));
        space(advancedPanel,7);
        turnUser=input(advancedPanel,"TURN username",prefs.getString("xyool_turn_user",""));
        space(advancedPanel,7);
        turnPass=input(advancedPanel,"TURN password",prefs.getString("xyool_turn_pass",""));
        turnPass.setInputType(InputType.TYPE_CLASS_TEXT|InputType.TYPE_TEXT_VARIATION_PASSWORD);
        space(advancedPanel,9);
        button(advancedPanel,"Save network settings",true,v->{
            String url=serverInput.getText().toString().trim();
            try{
                URI uri=URI.create(url);
                if(!"wss".equalsIgnoreCase(uri.getScheme())||uri.getHost()==null||
                    !"/v1/id".equals(uri.getPath())||
                    uri.getUserInfo()!=null||uri.getQuery()!=null||uri.getFragment()!=null)
                    throw new IllegalArgumentException();
            }catch(Exception ex){
                status("Signaling address must be wss://.../v1/id.");
                return;
            }
            try{new RendezvousPool(url,nodesInput.getText().toString());}
            catch(IllegalArgumentException invalid){
                status("Each additional node must be a valid wss:// address ending /v1/id (maximum 5).");
                return;
            }
            prefs.edit().putString("xyool_id_server",url)
                .putString(RendezvousPool.PREF_NODES,nodesInput.getText().toString().trim())
                .putString("xyool_stun",stunInput.getText().toString().trim())
                .putString("xyool_turn",turnInput.getText().toString().trim())
                .putString("xyool_turn_user",turnUser.getText().toString())
                .putString("xyool_turn_pass",turnPass.getText().toString()).apply();
            if(cloud!=null)cloud.reloadNetworkPolicy();
            else {disconnect();connect();}
            advancedPanel.setVisibility(View.GONE);
        });
        space(body,7);
        body.addView(text("Early test build. Background alerts require permission and aren't guaranteed after a force-stop. Not for emergency calls.",12,MUTED,false));
    }

    private void showMyQr(){
        try{
            // The QR holds the public ID only. Never include the private auth token.
            Map<EncodeHintType,Object> hints=new EnumMap<>(EncodeHintType.class);
            hints.put(EncodeHintType.MARGIN,2);
            BitMatrix grid=new MultiFormatWriter().encode(id,BarcodeFormat.QR_CODE,640,640,hints);
            int width=grid.getWidth(),height=grid.getHeight();
            Bitmap bitmap=Bitmap.createBitmap(width,height,Bitmap.Config.ARGB_8888);
            int[] pixels=new int[width*height];
            for(int y=0;y<height;y++){
                int offset=y*width;
                for(int x=0;x<width;x++)pixels[offset+x]=grid.get(x,y)?Color.BLACK:Color.WHITE;
            }
            bitmap.setPixels(pixels,0,width,0,0,width,height);
            ImageView qr=new ImageView(this);
            qr.setImageBitmap(bitmap);
            qr.setContentDescription("QR code for your Xyool ID "+id);
            qr.setAdjustViewBounds(true);
            qr.setPadding(dp(18),dp(18),dp(18),dp(18));
            qr.setBackgroundColor(Color.WHITE);
            LinearLayout frame=column();
            frame.setPadding(dp(16),dp(12),dp(16),dp(5));
            frame.addView(qr,new LinearLayout.LayoutParams(-1,-2));
            TextView label=text(id,18,FG,true);
            label.setGravity(Gravity.CENTER);
            frame.addView(label);
            new AlertDialog.Builder(this)
                .setTitle("My Xyool ID")
                .setView(frame)
                .setMessage(null)
                .setPositiveButton("Done",null)
                .show();
        }catch(Exception e){
            status("Unable to display QR code. You can still copy your ID.");
        }
    }
    private static final int QR_SCAN_REQUEST = 493;

    private void scanIdQr(){
        try{
            Intent scanner = new Intent(this, QrScannerActivity.class);
            startActivityForResult(scanner, QR_SCAN_REQUEST);
        }catch(Exception e){
            status("Unable to start QR scanner. Enter their ID manually.");
            Toast.makeText(this,"QR scanner couldn't open. Try Camera permission in app settings.",Toast.LENGTH_LONG).show();
        }
    }
    @Override protected void onActivityResult(int requestCode,int resultCode,Intent data){
        if(requestCode != QR_SCAN_REQUEST){
            super.onActivityResult(requestCode,resultCode,data);
            return;
        }
        if(resultCode != RESULT_OK || data == null){
            status("No ID scanned. You can also type an ID.");
            return;
        }
        String scanned = data.getStringExtra(QrScannerActivity.EXTRA_ID);
        if(scanned == null)return;
        String raw = scanned.trim().toUpperCase(Locale.US);
        // Only the exact public Xyool ID is allowed; never execute QR contents.
        if(!raw.matches("^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$")){
            status("That QR wasn't a valid Xyool ID.");
            return;
        }
        if(raw.equals(id)){
            status("That's your own QR. Scan the other person's code.");
            return;
        }
        targetInput.setText(raw);
        new AlertDialog.Builder(this)
            .setTitle("Xyool ID scanned")
            .setMessage(raw + " is ready. Tap Call when you're ready.")
            .setPositiveButton("OK",null)
            .show();
        status("ID scanned successfully.");
    }

    private void connectionStatus(){
        int n=cloud!=null&&hasReachability()?cloud.localPeerCount():
            (nearby==null?0:nearby.peerCount());
        if(!BridgePolicy.allowsCloud(bridgeMode())){
            status(n>0?"Direct-only · "+n+" local peers · Railway disconnected.":
                "Direct-only · Local or manual direct calls · No Railway.");
            return;
        }
        if(registered){
            status(n>0?"Nearby phones: "+n+" · Internet calling online.":"Internet calling online · Nearby Wi-Fi discovery on.");
        }else if(n>0){
            status("Nearby Xyool phones: "+n+" · Wi-Fi calling available.");
        }else if(LocalPeerNode.onWifi(this)){
            status("Searching for Xyool phones nearby · Internet calling offline.");
        }else{
            status("Internet calling offline · Join Wi-Fi for direct nearby calls.");
        }
    }
    private void status(String message){
        callStatus=message;
        runOnUiThread(()->{
            if(stateLabel!=null)stateLabel.setText(message);
        });
    }
    private String normalize(String raw){
        String clean=raw.toUpperCase(Locale.US).replaceAll("[^A-Z0-9]","");
        if(clean.startsWith("XY"))clean=clean.substring(2);
        if(clean.length()!=12||!clean.matches("^[A-HJ-NP-Z2-9]{12}$"))return null;
        return "XY-"+clean.substring(0,4)+"-"+clean.substring(4,8)+"-"+clean.substring(8);
    }
    private void connect(){
        if(!BridgePolicy.allowsCloud(bridgeMode())&&!hasReachability()){
            registered=false;connectionStatus();return;
        }
        if(cloudBound)return;
        cloudBound=bindService(new Intent(this,CallReachabilityService.class),
            cloudLink,Context.BIND_AUTO_CREATE);
        if(!cloudBound)status("Xyool calling service couldn't start.");
    }
    private void disconnect(){
        registered=false;
        if(cloud!=null){cloud.setListener(null);cloud=null;}
        if(cloudBound){
            unbindService(cloudLink);
            cloudBound=false;
        }
    }
    private boolean hasReachability(){return prefs.getBoolean(CallReachabilityService.PREF_ENABLED,false);}
    private void updateReachabilityButton(){
        if(reachabilityButton!=null)reachabilityButton.setText(
            hasReachability()?"Background call alerts: ON • Tap to disable":
                "Background call alerts: OFF • Tap to enable");
    }
    private void enableReachability(){
        if(Build.VERSION.SDK_INT>=33 &&
            checkSelfPermission(Manifest.permission.POST_NOTIFICATIONS)!=PackageManager.PERMISSION_GRANTED){
            requestPermissions(new String[]{Manifest.permission.POST_NOTIFICATIONS},482);
            return;
        }
        prefs.edit().putBoolean(CallReachabilityService.PREF_ENABLED,true).apply();
        try{
            Intent start=new Intent(this,CallReachabilityService.class)
                .setAction(CallReachabilityService.ACTION_ENABLE);
            if(nearby!=null)nearby.stop();
            startForegroundService(start);
            if(!cloudBound)connect();
            updateReachabilityButton();
            status("Background alerts enabled while Android permits the service to run.");
        }catch(RuntimeException ex){
            prefs.edit().putBoolean(CallReachabilityService.PREF_ENABLED,false).apply();
            updateReachabilityButton();
            status("Android couldn't start persistent call listening.");
        }
    }
    private void disableReachability(){
        prefs.edit().putBoolean(CallReachabilityService.PREF_ENABLED,false).apply();
        startService(new Intent(this,CallReachabilityService.class)
            .setAction(CallReachabilityService.ACTION_DISABLE));
        if(nearby!=null)nearby.start();
        updateReachabilityButton();
        status("Background call alerts disabled; calls work while the screen is open.");
    }
    private void toggleReachability(){
        if(hasReachability())disableReachability();
        else enableReachability();
    }
    private void send(JSONObject obj){
        if(usingLocal){
            if(cloud!=null&&hasReachability())cloud.localSend(obj);
            else if(nearby!=null)nearby.send(obj);
            return;
        }
        sendCloud(obj);
    }
    private void sendCloud(JSONObject obj){
        if(cloud!=null&&!cloud.send(obj))status("Internet signaling is not connected.");
    }
    private void packet(String type){
        try{JSONObject obj=new JSONObject();obj.put("type",type);send(obj);}
        catch(Exception ex){status("Could not send call command.");}
    }
    private void call(){
        if(peerActive||waitingId!=null){status("Finish your current call first.");return;}
        String dest=normalize(targetInput.getText().toString());
        if(dest==null){status("Enter a valid Xyool ID, like XY-ABCD-EFGH-JKLM.");return;}
        if(dest.equals(id)){status("You cannot call your own ID.");return;}
        boolean localAvailable=LocalPeerNode.onWifi(this)&&
            (cloud!=null&&hasReachability()?cloud.hasLocalPeer(dest):
                nearby!=null&&nearby.hasPeer(dest));
        BridgePolicy.Route route=BridgePolicy.choose(bridgeMode(),localAvailable,registered);
        if(route==BridgePolicy.Route.MANUAL_DIRECT_REQUIRED){
            status("No nearby route to this ID. Try Hybrid for other networks.");
            return;
        }
        requestMicrophone(()->{
            usingLocal=route==BridgePolicy.Route.LOCAL_DIRECT;
            if(!initPeer()){usingLocal=false;return;}
            outgoing=true;
            waitingId=dest;
            try{
                if(localAvailable){
                    boolean started=cloud!=null&&hasReachability()?cloud.localCall(dest):
                        nearby!=null&&nearby.call(dest);
                    if(!started){
                        endMedia();
                        status("Couldn't reach the nearby phone. Try again.");
                        return;
                    }
                    status("Calling nearby Xyool phone directly…");
                }else{
                    JSONObject obj=new JSONObject();
                    obj.put("type","call");
                    obj.put("to",dest);
                    sendCloud(obj);
                    status("Calling "+dest+" over the internet…");
                }
            }catch(Exception ex){endMedia();status("Could not request call.");}
        });
    }
    private void received(JSONObject msg,boolean fromLocal){
        String type=msg.optString("type","");
        if("incoming".equals(type)){
            if(peerActive||waitingId!=null){
                try{
                    JSONObject reject=new JSONObject();reject.put("type","reject");
                    if(fromLocal && cloud!=null&&hasReachability())cloud.localSend(reject);
                    else if(fromLocal && nearby!=null)nearby.send(reject);
                    else sendCloud(reject);
                    if(fromLocal && cloud!=null&&hasReachability())cloud.localClose();
                    else if(fromLocal && nearby!=null)nearby.closeSession();
                }catch(Exception ignored){}
                return;
            }
            usingLocal=fromLocal;
            waitingId=msg.optString("from");
            outgoing=false;
            if(autoAnswerRequested){
                autoAnswerRequested=false;
                acceptIncomingCall();
            }else incomingDialog(waitingId);
            return;
        }
        // Never allow a LAN session to consume signaling from a parallel
        // Railway session or vice versa.
        if((waitingId!=null||peerActive)&&fromLocal!=usingLocal)return;
        switch(type){
            case "registered":
                registered=true;
                connectionStatus();
                break;
            case "ringing":
                status(fromLocal?"Ringing nearby phone…":"Ringing… waiting for the other person.");
                break;
            case "accepted":
                callAuthorized=true;
                status("Call accepted. Connecting voice…");
                if(outgoing)createOffer();
                break;
            case "signal":
                signal(msg);
                break;
            case "ended":
                endMedia();
                status("Call ended: "+msg.optString("reason","disconnected"));
                break;
            case "busy":
                endMedia();
                status("That Xyool ID is on another call.");
                break;
            case "unavailable":
                endMedia();
                status("That ID is currently unreachable. They may be offline or background listening is blocked.");
                break;
            case "error":
                String detail=msg.optString("message","The calling network reported an error");
                if(waitingId!=null)endMedia();
                status(detail);
                break;
            default:break;
        }
    }
    // The ringtone is deliberately tied to the visible, user-accepted call
    // invitation. This alpha does not claim background or push call delivery.
    private void startIncomingRing(){
        stopIncomingRing();
        try{
            android.net.Uri sound=RingtoneManager.getDefaultUri(RingtoneManager.TYPE_RINGTONE);
            if(sound==null)sound=RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION);
            if(sound==null)return;
            incomingRingtone=RingtoneManager.getRingtone(getApplicationContext(),sound);
            if(incomingRingtone!=null){
                incomingRingtone.setAudioAttributes(new android.media.AudioAttributes.Builder()
                    .setUsage(android.media.AudioAttributes.USAGE_NOTIFICATION_RINGTONE)
                    .setContentType(android.media.AudioAttributes.CONTENT_TYPE_SONIFICATION)
                    .build());
                incomingRingtone.play();
            }
        }catch(RuntimeException ignored){incomingRingtone=null;}
    }
    private void stopIncomingRing(){
        if(incomingRingtone==null)return;
        try{incomingRingtone.stop();}catch(RuntimeException ignored){}
        incomingRingtone=null;
    }
    private void incomingDialog(String from){
        status("Incoming call from "+from);
        startIncomingRing();
        incomingAlert=new AlertDialog.Builder(this)
            .setTitle("Incoming Xyool call")
            .setMessage(from+" wants to talk.")
            .setCancelable(false)
            .setNegativeButton("Decline",(d,w)->{
                stopIncomingRing();
                packet("reject");endMedia();status("Call declined.");
            })
            .setPositiveButton("Accept",(d,w)->acceptIncomingCall())
            .create();
        incomingAlert.setOnDismissListener(d->{
            stopIncomingRing();
            if(incomingAlert==d)incomingAlert=null;
        });
        incomingAlert.show();
    }
    private void acceptIncomingCall(){
        stopIncomingRing();
        if(incomingAlert!=null){
            AlertDialog current=incomingAlert;incomingAlert=null;current.dismiss();
        }
        if(waitingId==null||outgoing||peerActive)return;
        requestMicrophone(()->{
            if(waitingId==null)return;
            if(!initPeer()){packet("reject");return;}
            outgoing=false;
            if(usingLocal)callAuthorized=true;
            packet("accept");
            status("Accepted. Negotiating audio connection…");
        });
    }
    private void requestMicrophone(Runnable next){
        if(checkSelfPermission(Manifest.permission.RECORD_AUDIO)==PackageManager.PERMISSION_GRANTED)next.run();
        else{
            pendingMicrophone=next;
            requestPermissions(new String[]{Manifest.permission.RECORD_AUDIO},MIC_REQUEST);
        }
    }
    @Override public void onRequestPermissionsResult(int request,String[] permissions,int[] grants){
        super.onRequestPermissionsResult(request,permissions,grants);
        if(request==482){
            if(grants.length>0&&grants[0]==PackageManager.PERMISSION_GRANTED)
                enableReachability();
            else status("Notification permission is needed for background call alerts.");
            return;
        }
        if(request!=MIC_REQUEST)return;
        Runnable next=pendingMicrophone;pendingMicrophone=null;
        if(grants.length>0&&grants[0]==PackageManager.PERMISSION_GRANTED&&next!=null)next.run();
        else{packet("reject");endMedia();status("Microphone permission is required for Xyool voice.");}
    }
    private boolean initPeer(){
        try{
            final IcePathInspector diag=new IcePathInspector();
            diag.setDiscovery(usingLocal?"Local Wi-Fi signaling":"Web2 ID signaling (Railway)");
            iceDiagnostics=diag;
            PeerConnectionFactory.initialize(PeerConnectionFactory.InitializationOptions.builder(
                getApplicationContext()).createInitializationOptions());
            factory=PeerConnectionFactory.builder().createPeerConnectionFactory();
            if(factory==null)throw new IllegalStateException("WebRTC unavailable");
            List<PeerConnection.IceServer> ice=new ArrayList<>();
            String s=prefs.getString("xyool_stun","").trim();
            if(!usingLocal && s.isEmpty())s=DEFAULT_STUN;
            if("off".equalsIgnoreCase(s))s="";
            String t=prefs.getString("xyool_turn","").trim();
            if(!s.isEmpty()){
                if(!s.matches("^stuns?:[A-Za-z0-9._-]+:[0-9]{2,5}$"))
                    throw new IllegalArgumentException("STUN address invalid");
                ice.add(PeerConnection.IceServer.builder(s).createIceServer());
            }
            if(!t.isEmpty()){
                if(!t.matches("^turns?:[A-Za-z0-9._-]+:[0-9]{2,5}(\\?transport=(udp|tcp))?$"))
                    throw new IllegalArgumentException("TURN address invalid");
                String username=prefs.getString("xyool_turn_user","");
                String password=prefs.getString("xyool_turn_pass","");
                if(username.isEmpty()||password.isEmpty())
                    throw new IllegalArgumentException("TURN credentials missing");
                ice.add(PeerConnection.IceServer.builder(t).setUsername(username)
                    .setPassword(password).createIceServer());
            }
            PeerConnection.RTCConfiguration iceConfig=new PeerConnection.RTCConfiguration(ice);
            // Keep direct host routes first; ICE will also try a public STUN path.
            peer=factory.createPeerConnection(iceConfig,
                new PeerConnection.Observer(){
                    @Override public void onSignalingChange(PeerConnection.SignalingState state){}
                    @Override public void onIceConnectionChange(PeerConnection.IceConnectionState state){
                        diag.setState(state.name());
                        if(iceDiagnostics!=diag)return;
                        if(state==PeerConnection.IceConnectionState.CHECKING){
                            status("ICE is checking direct audio paths across networks…");
                        }else if(state==PeerConnection.IceConnectionState.CONNECTED||
                            state==PeerConnection.IceConnectionState.COMPLETED){
                            status("Encrypted WebRTC connected. Copy report to examine ICE discovery.");
                        }else if(state==PeerConnection.IceConnectionState.FAILED){
                            status("Direct audio ICE failed. "+diag.interpretation()+
                                " Copy network report for diagnosis.");
                        }else if(state==PeerConnection.IceConnectionState.DISCONNECTED){
                            status("WebRTC disconnected. Check both networks.");
                        }
                    }
                    @Override public void onIceConnectionReceivingChange(boolean value){}
                    @Override public void onIceGatheringChange(PeerConnection.IceGatheringState state){
                        if(state==PeerConnection.IceGatheringState.COMPLETE && iceDiagnostics==diag
                            && waitingId!=null && !peerActive){
                            status("Network candidate gathering finished. Waiting for ICE connection.");
                        }
                    }
                    @Override public void onIceCandidate(IceCandidate c){
                        diag.record(c.sdp);
                        try{
                            JSONObject payload=new JSONObject();payload.put("type","signal");
                            payload.put("kind","candidate");payload.put("candidate",c.sdp);
                            payload.put("mid",c.sdpMid==null?"":c.sdpMid);
                            payload.put("index",c.sdpMLineIndex);send(payload);
                        }catch(Exception ex){status("Couldn't transmit network candidate.");}
                    }
                    @Override public void onIceCandidatesRemoved(IceCandidate[] list){}
                    @Override public void onAddStream(MediaStream stream){}
                    @Override public void onRemoveStream(MediaStream stream){}
                    @Override public void onDataChannel(DataChannel channel){}
                    @Override public void onRenegotiationNeeded(){}
                    @Override public void onAddTrack(RtpReceiver receiver,MediaStream[] streams){}
                });
            if(peer==null)throw new IllegalStateException("WebRTC connection unavailable");
            audioSource=factory.createAudioSource(new MediaConstraints());
            microphone=factory.createAudioTrack("xyool-microphone",audioSource);
            microphone.setEnabled(true);
            if(peer.addTrack(microphone,java.util.Collections.singletonList("xyool-media"))==null)
                throw new IllegalStateException("Microphone track unavailable");
            audioManager=(AudioManager)getSystemService(Context.AUDIO_SERVICE);
            if(audioManager!=null){
                oldMode=audioManager.getMode();oldSpeaker=audioManager.isSpeakerphoneOn();
                audioManager.setMode(AudioManager.MODE_IN_COMMUNICATION);
                audioManager.setSpeakerphoneOn(true);
            }
            peerActive=true;remoteReady=false;muted=false;pendingCandidates.clear();
            return true;
        }catch(Exception e){
            status("Audio initialization failed: "+e.getMessage());
            endMedia();
            return false;
        }
    }
    private void createOffer(){
        if(peer==null)return;
        peer.createOffer(new SdpCallbacks(){
            @Override public void onCreateSuccess(SessionDescription desc){setLocalAndSend(desc);}
        },new MediaConstraints());
    }
    private void setLocalAndSend(SessionDescription desc){
        if(peer==null)return;
        peer.setLocalDescription(new SdpCallbacks(){
            @Override public void onSetSuccess(){
                try{
                    JSONObject data=new JSONObject();data.put("type","signal");
                    data.put("kind",desc.type.canonicalForm());data.put("sdp",desc.description);
                    send(data);
                }catch(Exception e){status("Call setup failed.");}
            }
        },desc);
    }
    private void signal(JSONObject msg){
        if(peer==null||!callAuthorized)return;
        String kind=msg.optString("kind","");
        if("candidate".equals(kind)){
            String mid=msg.optString("mid",""),sdp=msg.optString("candidate","");
            int index=msg.optInt("index",-1);
            if(sdp.length()>4000||index<0||index>50||mid.length()>50)return;
            IceCandidate c=new IceCandidate(mid,index,sdp);
            if(remoteReady)peer.addIceCandidate(c);
            else pendingCandidates.add(c);
            return;
        }
        if(!(kind.equals("offer")||kind.equals("answer")))return;
        String sdp=msg.optString("sdp","");
        if(!sdp.startsWith("v=0")||sdp.length()<80||sdp.length()>32000)return;
        if(outgoing&&!kind.equals("answer"))return;
        if(!outgoing&&!kind.equals("offer"))return;
        SessionDescription desc=new SessionDescription(kind.equals("offer")?
            SessionDescription.Type.OFFER:SessionDescription.Type.ANSWER,sdp);
        peer.setRemoteDescription(new SdpCallbacks(){
            @Override public void onSetSuccess(){
                remoteReady=true;
                for(IceCandidate c:pendingCandidates)if(peer!=null)peer.addIceCandidate(c);
                pendingCandidates.clear();
                if(!outgoing&&peer!=null)peer.createAnswer(new SdpCallbacks(){
                    @Override public void onCreateSuccess(SessionDescription local){setLocalAndSend(local);}
                },new MediaConstraints());
            }
        },desc);
    }
    private abstract class SdpCallbacks implements SdpObserver{
        @Override public void onCreateSuccess(SessionDescription desc){}
        @Override public void onSetSuccess(){}
        @Override public void onCreateFailure(String err){status("Call setup error: "+err);}
        @Override public void onSetFailure(String err){status("Call setup error: "+err);}
    }
    private void toggleMute(){
        if(microphone==null){status("There is no active microphone call.");return;}
        muted=!muted;microphone.setEnabled(!muted);
        status(muted?"Microphone muted":"Microphone unmuted");
    }
    private void hangup(){
        packet("hangup");
        endMedia();
        status("Call ended.");
    }
    private void endMedia(){
        stopIncomingRing();
        if(incomingAlert!=null){
            AlertDialog dialog=incomingAlert;
            incomingAlert=null;
            dialog.dismiss();
        }
        if(usingLocal&&nearby!=null)nearby.closeSession();
        usingLocal=false;
        pendingCandidates.clear();
        waitingId=null;
        peerActive=false;remoteReady=false;callAuthorized=false;outgoing=false;
        if(peer!=null){peer.close();peer.dispose();peer=null;}
        if(microphone!=null){microphone.dispose();microphone=null;}
        if(audioSource!=null){audioSource.dispose();audioSource=null;}
        if(factory!=null){factory.dispose();factory=null;}
        if(audioManager!=null){
            audioManager.setSpeakerphoneOn(oldSpeaker);
            audioManager.setMode(oldMode);
            audioManager=null;
        }
    }
    @Override protected void onDestroy(){
        disposed=true;
        if(waitingId!=null)packet("hangup");
        disconnect();endMedia();
        if(nearby!=null){nearby.stop();nearby=null;}
        super.onDestroy();
    }
}
