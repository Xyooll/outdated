package org.xyool.connect;

import android.Manifest;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.ActivityNotFoundException;
import android.content.ClipData;
import android.content.ClipboardManager;
import android.content.Context;
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
import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;
import java.util.EnumMap;
import java.util.Map;
import android.media.AudioManager;
import android.os.Bundle;
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
    private static final int CAMERA_REQUEST=482;
    private SharedPreferences prefs;
    private String id, token;
    private TextView stateLabel;
    private EditText targetInput,serverInput,stunInput,turnInput,turnUser,turnPass;
    private LinearLayout body, advancedPanel;
    private WebSocketClient ws;
    private LocalPeerNode nearby;
    private boolean usingLocal;
    private boolean registered, outgoing, peerActive, remoteReady, callAuthorized, disposed;
    private String waitingId;
    private PeerConnectionFactory factory;
    private PeerConnection peer;
    private AudioSource audioSource;
    private AudioTrack microphone;
    private AudioManager audioManager;
    private int oldMode=AudioManager.MODE_NORMAL;
    private boolean oldSpeaker;
    private final List<IceCandidate> pendingCandidates=new ArrayList<>();
    private Runnable pendingMicrophone;
    private String callStatus="Checking Xyool calling service…";
    private boolean muted;

    @Override public void onCreate(Bundle b){
        super.onCreate(b);
        prefs=getSharedPreferences("xyool_private",MODE_PRIVATE);
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
    @Override protected void onResume(){
        super.onResume();
        if(nearby!=null)nearby.start();
    }
    @Override protected void onStop(){
        if(nearby!=null)nearby.stop();
        if(usingLocal&&waitingId!=null){
            endMedia();
            status("Nearby call ended when the calling screen closed.");
        }
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
    private void render(){
        LinearLayout root=column();
        root.setBackgroundColor(BG);
        ScrollView scroll=new ScrollView(this);
        body=column();
        body.setPadding(dp(15),dp(15),dp(15),dp(20));
        scroll.addView(body);
        root.addView(scroll,new LinearLayout.LayoutParams(-1,0,1f));
        button(root,"← Xyool Connect",false,v->finish());
        setContentView(root);

        body.addView(text("XYOOL CONNECT",12,ACCENT,true));
        space(body,5);
        body.addView(text("Call by ID",28,FG,true));
        space(body,8);

        LinearLayout connection=panel();
        connection.addView(text("CALLING NETWORK",12,MUTED,true));
        space(connection,6);
        stateLabel=text(callStatus,14,MUTED,false);
        connection.addView(stateLabel);
        space(connection,9);
        button(connection,"Check connection",false,v->{
            if(nearby!=null)nearby.start();
            if(registered)connectionStatus();
            else {disconnect();connect();}
        });

        LinearLayout self=panel();
        self.addView(text("YOUR XYOOL ID",12,MUTED,true));
        space(self,6);
        TextView address=text(id,23,ACCENT,true);
        address.setTextIsSelectable(true);
        address.setGravity(Gravity.CENTER_HORIZONTAL);
        self.addView(address);
        space(self,5);
        self.addView(text("Save this ID or share it with a friend. Don't share your private account key.",12,MUTED,false));
        space(self,12);
        button(self,"Copy my ID",true,v->{
            ClipboardManager clip=(ClipboardManager)getSystemService(Context.CLIPBOARD_SERVICE);
            if(clip!=null)clip.setPrimaryClip(ClipData.newPlainText("Xyool ID",id));
            status("Your ID was copied.");
        });
        space(self,8);
        button(self,"Show my QR code",false,v->showMyQr());
        space(self,8);
        button(self,"Share my ID",false,v->{
            Intent send=new Intent(Intent.ACTION_SEND);
            send.setType("text/plain");
            send.putExtra(Intent.EXTRA_TEXT,"Call me on Xyool Connect: "+id);
            try{startActivity(Intent.createChooser(send,"Share Xyool ID"));}
            catch(ActivityNotFoundException ex){status("No sharing app found.");}
        });

        LinearLayout dialing=panel();
        dialing.addView(text("CALL SOMEONE",12,MUTED,true));
        space(dialing,8);
        targetInput=input(dialing,"Type their Xyool ID",null);
        space(dialing,11);
        button(dialing,"Scan someone's QR code",false,v->scanIdQr());
        space(dialing,9);
        button(dialing,"Call",true,v->call());
        space(dialing,5);
        dialing.addView(text("The other person needs Xyool Connect open and online to answer.",12,MUTED,false));
        space(dialing,12);
        button(dialing,"Hang up",false,v->hangup());
        space(dialing,8);
        button(dialing,"Mute / Unmute",false,v->toggleMute());

        LinearLayout help=panel();
        help.addView(text("How calling works",17,FG,true));
        space(help,5);
        help.addView(text("For nearby calls, put both phones on the same trusted Wi-Fi and leave this screen open. Other calls use Xyool’s online connection service automatically. No setup needed.",13,MUTED,false));
        space(help,10);
        button(help,"Developer setup (optional)",false,v->{
            advancedPanel.setVisibility(advancedPanel.getVisibility()==View.GONE?View.VISIBLE:View.GONE);
        });
        space(help,9);
        advancedPanel=column();
        advancedPanel.setVisibility(View.GONE);
        help.addView(advancedPanel);
        advancedPanel.addView(text("Only for testing a server you control. Normal callers should never need these fields.",12,MUTED,false));
        space(advancedPanel,10);
        serverInput=input(advancedPanel,"Secure server address",prefs.getString("xyool_id_server",DEFAULT_SERVER));
        space(advancedPanel,7);
        stunInput=input(advancedPanel,"STUN server (optional)",prefs.getString("xyool_stun",""));
        space(advancedPanel,7);
        turnInput=input(advancedPanel,"TURN relay (optional)",prefs.getString("xyool_turn",""));
        space(advancedPanel,7);
        turnUser=input(advancedPanel,"TURN username (optional)",prefs.getString("xyool_turn_user",""));
        space(advancedPanel,7);
        turnPass=input(advancedPanel,"TURN password (optional)",prefs.getString("xyool_turn_pass",""));
        turnPass.setInputType(InputType.TYPE_CLASS_TEXT|InputType.TYPE_TEXT_VARIATION_PASSWORD);
        space(advancedPanel,10);
        button(advancedPanel,"Save and connect",true,v->{
            String url=serverInput.getText().toString().trim();
            try{
                URI uri=URI.create(url);
                if(!"wss".equalsIgnoreCase(uri.getScheme())||uri.getHost()==null||
                    !"/v1/id".equals(uri.getPath())||
                    uri.getUserInfo()!=null||uri.getQuery()!=null||uri.getFragment()!=null)
                    throw new IllegalArgumentException();
            }catch(Exception ex){
                status("Developer server address must start with wss:// and end in /v1/id.");
                return;
            }
            prefs.edit().putString("xyool_id_server",url)
                .putString("xyool_stun",stunInput.getText().toString().trim())
                .putString("xyool_turn",turnInput.getText().toString().trim())
                .putString("xyool_turn_user",turnUser.getText().toString())
                .putString("xyool_turn_pass",turnPass.getText().toString()).apply();
            disconnect();
            connect();
            advancedPanel.setVisibility(View.GONE);
        });

        space(body,5);
        body.addView(text("This alpha cannot ring while closed and isn't for emergency calls. Use the regular Android phone app for 911.",12,MUTED,false));
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
    private void scanIdQr(){
        if(!getPackageManager().hasSystemFeature(PackageManager.FEATURE_CAMERA_ANY)){
            Toast.makeText(this,"This device has no camera scanner.",Toast.LENGTH_LONG).show();
            return;
        }
        if(checkSelfPermission(Manifest.permission.CAMERA)!=PackageManager.PERMISSION_GRANTED){
            requestPermissions(new String[]{Manifest.permission.CAMERA},CAMERA_REQUEST);
            return;
        }
        openCameraScanner();
    }
    private void openCameraScanner(){
        try{
            new IntentIntegrator(this)
                .setDesiredBarcodeFormats(IntentIntegrator.QR_CODE)
                .setPrompt("Scan the other person's Xyool ID")
                .setBeepEnabled(false)
                .setOrientationLocked(false)
                .initiateScan();
        }catch(Exception e){
            Toast.makeText(this,"Camera scanner couldn't start. Enter the ID manually.",Toast.LENGTH_LONG).show();
        }
    }
    @Override protected void onActivityResult(int requestCode,int resultCode,Intent data){
        IntentResult scanned=IntentIntegrator.parseActivityResult(requestCode,resultCode,data);
        if(scanned==null){super.onActivityResult(requestCode,resultCode,data);return;}
        if(scanned.getContents()==null){status("QR scan canceled.");return;}
        String raw=scanned.getContents().trim().toUpperCase(Locale.US);
        // Allow only a public Xyool ID. Never navigate to web links, install APKs,
        // execute scan content, or auto-place a call based on an untrusted QR.
        if(!raw.matches("^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$")){
            status("That QR isn't a Xyool ID. Try scanning a Xyool Connect QR.");
            return;
        }
        if(raw.equals(id)){
            status("That's your own QR code. Scan the other person's.");
            return;
        }
        targetInput.setText(raw);
        new AlertDialog.Builder(this)
            .setTitle("Xyool ID scanned")
            .setMessage("Ready to call "+raw+"? Check the ID before tapping Call.")
            .setPositiveButton("OK",null)
            .show();
        status("ID scanned. Tap Call when you're ready.");
    }
    private void connectionStatus(){
        int n=nearby==null?0:nearby.peerCount();
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
        String raw=prefs.getString("xyool_id_server",DEFAULT_SERVER).trim();
        if(raw.isEmpty()){registered=false;connectionStatus();return;}
        URI uri;
        try{
            uri=URI.create(raw);
            if(!"wss".equalsIgnoreCase(uri.getScheme())||uri.getHost()==null||
                !"/v1/id".equals(uri.getPath())||uri.getUserInfo()!=null||
                uri.getQuery()!=null||uri.getFragment()!=null)throw new IllegalArgumentException();
        }catch(Exception ex){status("Invalid server configuration.");return;}
        final String ownId=id,ownToken=token;
        registered=false;
        status("Connecting to Xyool...");
        ws=new WebSocketClient(uri){
            @Override public void onOpen(ServerHandshake handshake){
                try{
                    JSONObject msg=new JSONObject();msg.put("type","register");
                    msg.put("id",ownId);msg.put("token",ownToken);send(msg.toString());
                }catch(Exception ex){status("ID registration failed.");}
            }
            @Override public void onMessage(String raw){
                try{
                    if(raw.length()>50000)return;
                    JSONObject message=new JSONObject(raw);
                    runOnUiThread(()->received(message,false));
                }catch(Exception ex){status("Unrecognized server response.");}
            }
            @Override public void onClose(int code,String reason,boolean remote){
                runOnUiThread(()->{
                    registered=false;
                    if(!disposed)connectionStatus();
                });
            }
            @Override public void onError(Exception ex){
                connectionStatus();
            }
        };
        ws.setConnectionLostTimeout(30);
        ws.connect();
    }
    private void disconnect(){
        registered=false;
        if(ws!=null){ws.close();ws=null;}
    }
    private void send(JSONObject obj){
        if(usingLocal && nearby!=null){
            nearby.send(obj);
            return;
        }
        sendCloud(obj);
    }
    private void sendCloud(JSONObject obj){
        if(ws!=null&&ws.isOpen())ws.send(obj.toString());
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
        boolean localAvailable=nearby!=null&&nearby.hasPeer(dest)&&LocalPeerNode.onWifi(this);
        if(!localAvailable&&!registered){
            status("That ID isn't nearby. Internet calling is offline. Both phones must be online.");
            return;
        }
        requestMicrophone(()->{
            if(!initPeer())return;
            outgoing=true;
            waitingId=dest;
            usingLocal=localAvailable;
            try{
                if(localAvailable){
                    if(!nearby.call(dest)){
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
                    if(fromLocal && nearby!=null)nearby.send(reject);
                    else sendCloud(reject);
                    if(fromLocal && nearby!=null)nearby.closeSession();
                }catch(Exception ignored){}
                return;
            }
            usingLocal=fromLocal;
            waitingId=msg.optString("from");
            outgoing=false;
            incomingDialog(waitingId);
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
                status("That ID isn't online. The other person's app needs to be open.");
                break;
            case "error":
                String detail=msg.optString("message","The calling network reported an error");
                if(waitingId!=null)endMedia();
                status(detail);
                break;
            default:break;
        }
    }
    private void incomingDialog(String from){
        status("Incoming call from "+from);
        new AlertDialog.Builder(this)
            .setTitle("Incoming Xyool call")
            .setMessage(from+" wants to talk.")
            .setCancelable(false)
            .setNegativeButton("Decline",(d,w)->{packet("reject");endMedia();status("Call declined.");})
            .setPositiveButton("Accept",(d,w)->requestMicrophone(()->{
                if(!initPeer()){packet("reject");return;}
                outgoing=false;
                if(usingLocal)callAuthorized=true;
                packet("accept");
                status("Accepted. Waiting for connection…");
            })).show();
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
        if(request==CAMERA_REQUEST){
            if(grants.length>0&&grants[0]==PackageManager.PERMISSION_GRANTED)openCameraScanner();
            else {
                boolean showHint=!shouldShowRequestPermissionRationale(Manifest.permission.CAMERA);
                new AlertDialog.Builder(this)
                    .setTitle("Camera access needed")
                    .setMessage(showHint?"Enable Camera in Android Settings → Apps → Xyool Connect → Permissions to scan IDs. You can still enter an ID manually.":"Allow camera access to scan a Xyool ID. You can also type the ID.")
                    .setPositiveButton("OK",null).show();
            }
            return;
        }
        if(request!=MIC_REQUEST)return;
        Runnable next=pendingMicrophone;pendingMicrophone=null;
        if(grants.length>0&&grants[0]==PackageManager.PERMISSION_GRANTED&&next!=null)next.run();
        else{packet("reject");endMedia();status("Microphone permission is required for Xyool voice.");}
    }
    private boolean initPeer(){
        try{
            PeerConnectionFactory.initialize(PeerConnectionFactory.InitializationOptions.builder(
                getApplicationContext()).createInitializationOptions());
            factory=PeerConnectionFactory.builder().createPeerConnectionFactory();
            if(factory==null)throw new IllegalStateException("WebRTC unavailable");
            List<PeerConnection.IceServer> ice=new ArrayList<>();
            String s=prefs.getString("xyool_stun","").trim();
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
            peer=factory.createPeerConnection(new PeerConnection.RTCConfiguration(ice),
                new PeerConnection.Observer(){
                    @Override public void onSignalingChange(PeerConnection.SignalingState state){}
                    @Override public void onIceConnectionChange(PeerConnection.IceConnectionState state){
                        if(state==PeerConnection.IceConnectionState.CONNECTED||
                            state==PeerConnection.IceConnectionState.COMPLETED){
                            status("Connected · Encrypted voice call");
                        }else if(state==PeerConnection.IceConnectionState.FAILED){
                            status("Connection failed. A TURN relay may be required.");
                        }else if(state==PeerConnection.IceConnectionState.DISCONNECTED){
                            status("Audio disconnected. Check internet.");
                        }
                    }
                    @Override public void onIceConnectionReceivingChange(boolean value){}
                    @Override public void onIceGatheringChange(PeerConnection.IceGatheringState state){}
                    @Override public void onIceCandidate(IceCandidate c){
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
