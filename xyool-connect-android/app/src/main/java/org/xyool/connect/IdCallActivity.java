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
    private SharedPreferences prefs;
    private String id, token;
    private TextView stateLabel;
    private EditText targetInput,serverInput,stunInput,turnInput,turnUser,turnPass;
    private LinearLayout body, advancedPanel;
    private WebSocketClient ws;
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
    private String callStatus="Not connected to a Xyool calling server.";
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
        render();
        connect();
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
        LinearLayout root=column();root.setBackgroundColor(BG);
        ScrollView scroll=new ScrollView(this);
        body=column();body.setPadding(dp(15),dp(15),dp(15),dp(20));
        scroll.addView(body);root.addView(scroll,new LinearLayout.LayoutParams(-1,0,1f));
        button(root,"← Xyool Connect",false,v->finish());
        setContentView(root);

        body.addView(text("XYOOL CONNECT",12,ACCENT,true));space(body,4);
        body.addView(text("Call by ID",28,FG,true));space(body,6);
        body.addView(text("Your ID is like a phone number for internet calls.",14,MUTED,false));
        space(body,15);

        LinearLayout self=panel();
        self.addView(text("YOUR XYOOL ID",12,MUTED,true));space(self,8);
        TextView address=text(id,23,ACCENT,true);
        address.setTextIsSelectable(true);address.setGravity(Gravity.CENTER_HORIZONTAL);
        self.addView(address);space(self,12);
        button(self,"Copy my ID",true,v->{
            ClipboardManager clip=(ClipboardManager)getSystemService(Context.CLIPBOARD_SERVICE);
            if(clip!=null)clip.setPrimaryClip(ClipData.newPlainText("Xyool ID",id));
            status("Your ID is copied. Share it with someone you trust.");
        });
        space(self,8);
        button(self,"Share my ID",false,v->{
            Intent send=new Intent(Intent.ACTION_SEND);send.setType("text/plain");
            send.putExtra(Intent.EXTRA_TEXT,"Call my Xyool ID: "+id);
            try{startActivity(Intent.createChooser(send,"Share Xyool ID"));}
            catch(ActivityNotFoundException ex){status("No sharing app found.");}
        });

        LinearLayout dialing=panel();
        dialing.addView(text("CALL SOMEONE",12,MUTED,true));space(dialing,8);
        targetInput=input(dialing,"Enter their Xyool ID",null);
        space(dialing,12);
        button(dialing,"Call",true,v->call());
        space(dialing,9);
        button(dialing,"Hang up",false,v->hangup());

        LinearLayout state=panel();
        state.addView(text("CALL STATUS",12,MUTED,true));space(state,7);
        stateLabel=text(callStatus,14,MUTED,false);state.addView(stateLabel);
        space(state,9);
        button(state,"Mute / Unmute microphone",false,v->toggleMute());

        LinearLayout advanced=panel();
        Button configure=button(advanced,"⚙  Connection settings",false,v->{
            advancedPanel.setVisibility(
                advancedPanel.getVisibility()==View.GONE?View.VISIBLE:View.GONE);
        });
        space(advanced,8);
        advancedPanel=column();
        advancedPanel.setVisibility(View.GONE);
        advanced.addView(advancedPanel);
        advancedPanel.addView(text("Xyool's own WSS server is needed for ID calls. This alpha has no default server yet.",12,MUTED,false));
        space(advancedPanel,8);
        serverInput=input(advancedPanel,"wss://your-domain/v1/id",prefs.getString("xyool_id_server",""));
        space(advancedPanel,7);
        stunInput=input(advancedPanel,"Optional STUN: stun:host:3478",prefs.getString("xyool_stun",""));
        space(advancedPanel,7);
        turnInput=input(advancedPanel,"Optional TURN: turn:host:3478",prefs.getString("xyool_turn",""));
        space(advancedPanel,7);
        turnUser=input(advancedPanel,"TURN username",prefs.getString("xyool_turn_user",""));
        space(advancedPanel,7);
        turnPass=input(advancedPanel,"TURN password",prefs.getString("xyool_turn_pass",""));
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
            }catch(Exception e){status("Invalid URL. Use wss://your-server/v1/id");return;}
            prefs.edit().putString("xyool_id_server",url)
                .putString("xyool_stun",stunInput.getText().toString().trim())
                .putString("xyool_turn",turnInput.getText().toString().trim())
                .putString("xyool_turn_user",turnUser.getText().toString())
                .putString("xyool_turn_pass",turnPass.getText().toString()).apply();
            disconnect();connect();
            advancedPanel.setVisibility(View.GONE);
        });
        space(body,3);
        body.addView(text("Both people must have Xyool Connect open and connected. No background ringing or emergency calls in this alpha. Never depend on this app for 911.",12,MUTED,false));
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
        String raw=prefs.getString("xyool_id_server","").trim();
        if(raw.isEmpty()){registered=false;status("Your ID is ready. Calling needs a Xyool server—open Connection settings.");return;}
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
                    runOnUiThread(()->received(message));
                }catch(Exception ex){status("Unrecognized server response.");}
            }
            @Override public void onClose(int code,String reason,boolean remote){
                runOnUiThread(()->{
                    registered=false;
                    if(!disposed)status("Connection lost. Open the calling screen to reconnect.");
                });
            }
            @Override public void onError(Exception ex){
                status("Xyool server unreachable. Check Connection settings.");
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
        if(ws!=null&&ws.isOpen())ws.send(obj.toString());
    }
    private void packet(String type){
        try{JSONObject obj=new JSONObject();obj.put("type",type);send(obj);}
        catch(Exception ex){status("Could not send call command.");}
    }
    private void call(){
        if(!registered){status("Not connected. Set up a Xyool calling server first.");return;}
        if(peerActive||waitingId!=null){status("Finish your current call first.");return;}
        String dest=normalize(targetInput.getText().toString());
        if(dest==null){status("Enter a valid Xyool ID, like XY-ABCD-EFGH-JKLM.");return;}
        if(dest.equals(id)){status("You cannot call your own ID.");return;}
        requestMicrophone(()->{
            if(!initPeer())return;
            outgoing=true;waitingId=dest;
            try{
                JSONObject obj=new JSONObject();obj.put("type","call");obj.put("to",dest);send(obj);
                status("Calling "+dest+" …");
            }catch(Exception ex){endMedia();status("Could not request call.");}
        });
    }
    private void received(JSONObject msg){
        String type=msg.optString("type","");
        switch(type){
            case "registered":
                registered=true;
                status("Online. Share your ID or enter an ID to call.");
                break;
            case "ringing":
                status("Ringing… waiting for the other person.");
                break;
            case "incoming":
                if(peerActive||waitingId!=null){packet("reject");return;}
                waitingId=msg.optString("from");
                outgoing=false;
                incomingDialog(waitingId);
                break;
            case "accepted":
                callAuthorized=true;
                status("Call accepted. Connecting encrypted audio…");
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
                endMedia();status("That Xyool ID is on another call.");
                break;
            case "unavailable":
                endMedia();status("That ID isn't online. Both phones must have Xyool Connect open.");
                break;
            case "error":
                String detail=msg.optString("message","Server reported an error");
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
        super.onDestroy();
    }
}
