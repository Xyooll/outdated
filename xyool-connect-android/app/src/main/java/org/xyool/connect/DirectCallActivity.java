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
import android.graphics.Color;
import android.media.AudioManager;
import android.os.Bundle;
import android.text.InputFilter;
import android.text.InputType;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Locale;
import org.json.JSONArray;
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

/**
 * Standalone DIRECT peer-to-peer voice call lab. There is NO WebSocket, HTTP,
 * Railway or Xyool server connection in this Activity.
 *
 * Users exchange two compressed WebRTC SDP+ICE codes through an
 * out-of-band trusted channel. Once ICE succeeds, WebRTC sends DTLS-SRTP
 * encrypted voice directly between the devices.
 *
 * WARNING: This is NOT verified caller identity. A malicious intermediary
 * modifying the shared codes could replace the DTLS fingerprints.
 * An external STUN service is contacted unless disabled by the user.
 * Some routers/CGNAT prevent direct peer connectivity without a relay.
 */
public final class DirectCallActivity extends Activity {
    private static final int BG=0xff0c1822,FG=0xfff0faf7,ACCENT=0xff68dbc3,MUTED=0xffaec8cf;
    private static final int MICROPHONE_PERMISSION=927;
    private static final String DEFAULT_STUN="stun:stun.cloudflare.com:3478";
    private static final String ID_PATTERN="^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$";

    private String myId,remoteId,sessionId,lastCode;
    private EditText targetInput;
    private TextView state;
    private SharedPreferences prefs;
    private PeerConnectionFactory factory;
    private PeerConnection peer;
    private AudioSource audioSource;
    private AudioTrack microphone;
    private AudioManager audioManager;
    private int previousAudioMode=AudioManager.MODE_NORMAL;
    private boolean previousSpeaker;
    private boolean outgoing,remoteReady,localReady,iceComplete,codeEmitted,ended;
    private Runnable pendingMic;
    private final Object candidatesLock=new Object();
    private JSONArray localCandidates=new JSONArray();
    private final List<IceCandidate> remoteCandidates=new ArrayList<>();

    private int dp(int v){return (int)(v*getResources().getDisplayMetrics().density+0.5f);}
    private LinearLayout column(){
        LinearLayout l=new LinearLayout(this);
        l.setOrientation(LinearLayout.VERTICAL);
        return l;
    }
    private TextView label(String s,int size,int color){
        TextView t=new TextView(this);
        t.setText(s);t.setTextSize(size);t.setTextColor(color);
        t.setGravity(Gravity.CENTER_HORIZONTAL);
        return t;
    }
    private Button button(LinearLayout parent,String title,View.OnClickListener action){
        Button b=new Button(this);
        b.setText(title);b.setTextSize(15);b.setAllCaps(false);b.setOnClickListener(action);
        parent.addView(b,new LinearLayout.LayoutParams(-1,dp(52)));
        return b;
    }
    private void status(String s){
        runOnUiThread(()->{if(!isFinishing()&&state!=null)state.setText(s);});
    }
    @Override public void onCreate(Bundle b){
        super.onCreate(b);
        prefs=getSharedPreferences("xyool_private",MODE_PRIVATE);
        myId=prefs.getString("xyool_id","");
        if(!myId.matches(ID_PATTERN)){
            new AlertDialog.Builder(this).setTitle("Xyool ID required")
                .setMessage("Open Call by ID once to generate your Xyool ID first.")
                .setPositiveButton("OK",(dialog,which)->finish()).show();
            return;
        }
        getWindow().setStatusBarColor(BG);getWindow().setNavigationBarColor(BG);
        LinearLayout root=column();root.setBackgroundColor(BG);
        ScrollView scroll=new ScrollView(this);
        LinearLayout body=column();
        body.setPadding(dp(16),dp(16),dp(16),dp(22));
        scroll.addView(body);root.addView(scroll,new LinearLayout.LayoutParams(-1,0,1f));
        setContentView(root);

        body.addView(label("DIRECT PHONE-TO-PHONE LAB",20,ACCENT));
        TextView description=label("No Railway or Xyool calling server. Exchange an offer and answer, then WebRTC tries encrypted direct audio over any reachable network.",14,MUTED);
        description.setPadding(0,dp(9),0,dp(12));body.addView(description);
        body.addView(label("My Xyool ID",13,MUTED));
        TextView idLabel=label(myId,18,FG);
        idLabel.setTextIsSelectable(true);
        body.addView(idLabel);
        state=label("Ready. Both phones must have this screen open.",14,FG);
        state.setPadding(dp(4),dp(18),dp(4),dp(15));
        body.addView(state);

        targetInput=new EditText(this);
        targetInput.setHint("Other phone's XY-.... ID");
        targetInput.setHintTextColor(MUTED);
        targetInput.setTextColor(FG);
        targetInput.setSingleLine(true);
        targetInput.setInputType(InputType.TYPE_CLASS_TEXT);
        body.addView(targetInput,new LinearLayout.LayoutParams(-1,dp(56)));
        button(body,"1. Create direct offer",v->startOffer());
        button(body,"2. Paste received offer or answer",v->pasteCode());
        button(body,"Copy current code",v->copyCode());
        button(body,"Share current code",v->shareCode());
        button(body,"Mute / Unmute",v->toggleMute());
        button(body,"Hang up",v->{hangup();status("Direct call ended.");});
        TextView notice=label("Test-only: codes can expose IP addresses and are NOT identity-authenticated. Cloudflare STUN is used by default for NAT traversal; set STUN to 'off' in the Calling screen's Developer setup to disable it. Some routers require a relay, so these calls may fail.",12,MUTED);
        notice.setPadding(0,dp(14),0,dp(12));body.addView(notice);
        button(root,"← Back to calling",v->finish());
    }
    private String normalize(String raw){
        String clean=raw.toUpperCase(Locale.US).replaceAll("[^A-Z0-9]","");
        if(clean.startsWith("XY"))clean=clean.substring(2);
        if(!clean.matches("^[A-HJ-NP-Z2-9]{12}$"))return null;
        return "XY-"+clean.substring(0,4)+"-"+clean.substring(4,8)+"-"+clean.substring(8);
    }
    private void microphonePermission(Runnable work){
        if(checkSelfPermission(Manifest.permission.RECORD_AUDIO)==PackageManager.PERMISSION_GRANTED)
            work.run();
        else{
            pendingMic=work;
            requestPermissions(new String[]{Manifest.permission.RECORD_AUDIO},MICROPHONE_PERMISSION);
        }
    }
    @Override public void onRequestPermissionsResult(int code,String[] permissions,int[] grants){
        super.onRequestPermissionsResult(code,permissions,grants);
        if(code!=MICROPHONE_PERMISSION)return;
        Runnable work=pendingMic;pendingMic=null;
        if(grants.length>0&&grants[0]==PackageManager.PERMISSION_GRANTED&&work!=null)work.run();
        else status("Microphone permission is required for a direct voice call.");
    }
    private void reset(String other,String callId,boolean isOutgoing){
        outgoing=isOutgoing;remoteId=other;sessionId=callId;
        ended=false;remoteReady=false;localReady=false;iceComplete=false;codeEmitted=false;
        lastCode=null;
        localCandidates=new JSONArray();remoteCandidates.clear();
    }
    private String randomCallId(){
        byte[] bytes=new byte[16];new SecureRandom().nextBytes(bytes);
        StringBuilder hex=new StringBuilder(32);
        for(byte b:bytes)hex.append(String.format(Locale.US,"%02x",b&255));
        return hex.toString();
    }
    private void startOffer(){
        if(peer!=null){status("Hang up the active direct session first.");return;}
        String other=normalize(targetInput.getText().toString());
        if(other==null||other.equals(myId)){
            status("Enter the other person's valid Xyool ID first.");return;
        }
        microphonePermission(()->{
            reset(other,randomCallId(),true);
            if(!initPeer())return;
            status("Creating offer and gathering direct network paths…");
            peer.createOffer(new SdpEvents(){
                @Override public void onCreateSuccess(SessionDescription offer){
                    setLocal(offer);
                }
            },new MediaConstraints());
        });
    }
    private boolean initPeer(){
        try{
            PeerConnectionFactory.initialize(PeerConnectionFactory.InitializationOptions.builder(
                getApplicationContext()).createInitializationOptions());
            factory=PeerConnectionFactory.builder().createPeerConnectionFactory();
            List<PeerConnection.IceServer> ice=new ArrayList<>();
            String stun=prefs.getString("xyool_stun","").trim();
            if(stun.isEmpty())stun=DEFAULT_STUN;
            if(!"off".equalsIgnoreCase(stun)){
                if(!stun.matches("^stuns?:[A-Za-z0-9._-]+:[0-9]{2,5}$"))
                    throw new IllegalArgumentException("STUN server configuration is invalid");
                ice.add(PeerConnection.IceServer.builder(stun).createIceServer());
            }
            // This mode has NO TURN relay and NO cloud signaling.
            peer=factory.createPeerConnection(new PeerConnection.RTCConfiguration(ice),
                new PeerConnection.Observer(){
                    @Override public void onSignalingChange(PeerConnection.SignalingState s){}
                    @Override public void onIceConnectionChange(PeerConnection.IceConnectionState s){
                        if(s==PeerConnection.IceConnectionState.CHECKING)
                            status("Direct ICE checks in progress…");
                        if(s==PeerConnection.IceConnectionState.CONNECTED||
                            s==PeerConnection.IceConnectionState.COMPLETED)
                            status("DIRECT encrypted audio connected. No Xyool media relay.");
                        if(s==PeerConnection.IceConnectionState.FAILED)
                            status("Direct connection blocked. These networks may need IPv6, hole punching or a voluntary peer bridge.");
                        if(s==PeerConnection.IceConnectionState.DISCONNECTED)
                            status("Direct audio disconnected.");
                    }
                    @Override public void onIceConnectionReceivingChange(boolean v){}
                    @Override public void onIceGatheringChange(PeerConnection.IceGatheringState s){
                        if(s==PeerConnection.IceGatheringState.COMPLETE){
                            iceComplete=true;emitCodeIfReady();
                        }
                    }
                    @Override public void onIceCandidate(IceCandidate c){
                        try{
                            JSONObject obj=new JSONObject();
                            obj.put("candidate",c.sdp);
                            obj.put("mid",c.sdpMid==null?"":c.sdpMid);
                            obj.put("index",c.sdpMLineIndex);
                            synchronized(candidatesLock){localCandidates.put(obj);}
                        }catch(Exception e){status("Couldn't collect an ICE candidate.");}
                    }
                    @Override public void onIceCandidatesRemoved(IceCandidate[] c){}
                    @Override public void onAddStream(MediaStream s){}
                    @Override public void onRemoveStream(MediaStream s){}
                    @Override public void onDataChannel(DataChannel c){}
                    @Override public void onRenegotiationNeeded(){}
                    @Override public void onAddTrack(RtpReceiver receiver,MediaStream[] streams){}
                });
            if(peer==null)throw new IllegalStateException("WebRTC unavailable");
            audioSource=factory.createAudioSource(new MediaConstraints());
            microphone=factory.createAudioTrack("xyool-direct-mic",audioSource);
            microphone.setEnabled(true);
            if(peer.addTrack(microphone,Collections.singletonList("xyool-direct-audio"))==null)
                throw new IllegalStateException("Microphone track unavailable");
            audioManager=(AudioManager)getSystemService(Context.AUDIO_SERVICE);
            if(audioManager!=null){
                previousAudioMode=audioManager.getMode();
                previousSpeaker=audioManager.isSpeakerphoneOn();
                audioManager.setMode(AudioManager.MODE_IN_COMMUNICATION);
                audioManager.setSpeakerphoneOn(true);
            }
            return true;
        }catch(Exception e){
            status("Direct audio initialization error: "+e.getMessage());
            hangup();
            return false;
        }
    }
    private void setLocal(SessionDescription desc){
        if(peer==null)return;
        peer.setLocalDescription(new SdpEvents(){
            @Override public void onSetSuccess(){
                localReady=true;
                emitCodeIfReady();
            }
        },desc);
    }
    private void emitCodeIfReady(){
        if(!localReady||!iceComplete||codeEmitted||peer==null||ended)return;
        codeEmitted=true;
        runOnUiThread(()->{
            try{
                if(peer==null||ended)return;
                SessionDescription sdp=peer.getLocalDescription();
                if(sdp==null)throw new IllegalStateException("Local offer/answer missing");
                JSONArray candidates;
                synchronized(candidatesLock){candidates=new JSONArray(localCandidates.toString());}
                lastCode=DirectInviteCodec.encode(sdp.type.canonicalForm(),
                    myId,remoteId,sessionId,sdp.description,candidates);
                status(outgoing?
                    "Offer ready. Share it and wait for the other phone's answer.":
                    "Answer ready. Share it with the caller, then wait for direct ICE to connect.");
                new AlertDialog.Builder(this)
                    .setTitle(outgoing?"Direct offer ready":"Direct answer ready")
                    .setMessage("Copy or share the invitation. It contains network addresses, not your Xyool private account key.")
                    .setPositiveButton("Share",(d,w)->shareCode())
                    .setNeutralButton("Copy",(d,w)->copyCode())
                    .setNegativeButton("Close",null).show();
            }catch(Exception e){codeEmitted=false;status("Can't create direct code: "+e.getMessage());}
        });
    }
    private void copyCode(){
        if(lastCode==null){status("No code generated yet.");return;}
        ClipboardManager board=(ClipboardManager)getSystemService(Context.CLIPBOARD_SERVICE);
        if(board!=null){
            board.setPrimaryClip(ClipData.newPlainText("Xyool direct SDP",lastCode));
            status("Direct code copied. Send it through a trusted channel.");
        }
    }
    private void shareCode(){
        if(lastCode==null){status("No code generated yet.");return;}
        Intent share=new Intent(Intent.ACTION_SEND);
        share.setType("text/plain");
        share.putExtra(Intent.EXTRA_TEXT,lastCode);
        try{startActivity(Intent.createChooser(share,"Share direct call code"));}
        catch(ActivityNotFoundException e){copyCode();}
    }
    private void pasteCode(){
        EditText field=new EditText(this);
        field.setInputType(InputType.TYPE_CLASS_TEXT|InputType.TYPE_TEXT_FLAG_MULTI_LINE);
        field.setSingleLine(false);field.setMinLines(3);field.setMaxLines(8);
        field.setFilters(new InputFilter[]{new InputFilter.LengthFilter(85000)});
        ClipboardManager board=(ClipboardManager)getSystemService(Context.CLIPBOARD_SERVICE);
        try{
            if(board!=null&&board.hasPrimaryClip()){
                CharSequence text=board.getPrimaryClip().getItemAt(0).coerceToText(this);
                if(text!=null&&text.toString().startsWith(DirectInviteCodec.PREFIX))
                    field.setText(text);
            }
        }catch(Exception ignored){}
        new AlertDialog.Builder(this)
            .setTitle("Paste direct call code")
            .setMessage("Paste their offer or answer. No Xyool server is contacted.")
            .setView(field)
            .setNegativeButton("Cancel",null)
            .setPositiveButton("Continue",(d,w)->consumeCode(field.getText().toString()))
            .show();
    }
    private void consumeCode(String raw){
        try{
            JSONObject invite=DirectInviteCodec.decode(raw);
            String sender=invite.getString("from");
            String recipient=invite.getString("to");
            String call=invite.getString("call");
            String kind=invite.getString("kind");
            if(!recipient.equals(myId)||sender.equals(myId))
                throw new IllegalArgumentException("Code is for another Xyool ID");
            if("answer".equals(kind)){
                if(peer==null||!outgoing||!call.equals(sessionId)||!sender.equals(remoteId))
                    throw new IllegalArgumentException("Answer doesn't match your current outgoing offer");
                applyRemote(invite);
                status("Answer accepted. Attempting direct encrypted audio…");
                return;
            }
            if(peer!=null)throw new IllegalArgumentException("Hang up before taking a new call");
            new AlertDialog.Builder(this)
                .setTitle("Direct call invitation")
                .setMessage(sender+" wants to call. Direct invitations are not yet cryptographically identity-verified.")
                .setNegativeButton("Decline",null)
                .setPositiveButton("Accept",(d,w)->microphonePermission(()->{
                    reset(sender,call,false);
                    if(!initPeer())return;
                    status("Offer accepted. Creating direct answer…");
                    applyRemote(invite);
                })).show();
        }catch(Exception e){status("Invalid direct code: "+e.getMessage());}
    }
    private void applyRemote(JSONObject invite){
        try{
            if(peer==null)throw new IllegalStateException("Start a direct call first");
            JSONArray ice=invite.getJSONArray("ice");
            remoteCandidates.clear();
            for(int i=0;i<ice.length();i++){
                JSONObject c=ice.getJSONObject(i);
                remoteCandidates.add(new IceCandidate(c.getString("mid"),
                    c.getInt("index"),c.getString("candidate")));
            }
            String kind=invite.getString("kind");
            SessionDescription remote=new SessionDescription(
                "offer".equals(kind)?SessionDescription.Type.OFFER:SessionDescription.Type.ANSWER,
                invite.getString("sdp"));
            peer.setRemoteDescription(new SdpEvents(){
                @Override public void onSetSuccess(){
                    remoteReady=true;
                    if(peer==null)return;
                    for(IceCandidate c:remoteCandidates)peer.addIceCandidate(c);
                    remoteCandidates.clear();
                    if(!outgoing && peer!=null){
                        peer.createAnswer(new SdpEvents(){
                            @Override public void onCreateSuccess(SessionDescription answer){
                                setLocal(answer);
                            }
                        },new MediaConstraints());
                    }
                }
            },remote);
        }catch(Exception e){status("Direct connection setup error: "+e.getMessage());}
    }
    private abstract class SdpEvents implements SdpObserver{
        @Override public void onCreateSuccess(SessionDescription desc){}
        @Override public void onSetSuccess(){}
        @Override public void onCreateFailure(String error){status("WebRTC offer/answer error: "+error);}
        @Override public void onSetFailure(String error){status("WebRTC session error: "+error);}
    }
    private void toggleMute(){
        if(microphone==null){status("No active direct audio track.");return;}
        boolean next=!microphone.enabled();
        microphone.setEnabled(next);
        status(next?"Microphone unmuted":"Microphone muted");
    }
    private void hangup(){
        ended=true;
        remoteCandidates.clear();
        lastCode=null;
        localReady=false;iceComplete=false;codeEmitted=false;remoteReady=false;
        if(peer!=null){peer.close();peer.dispose();peer=null;}
        if(microphone!=null){microphone.dispose();microphone=null;}
        if(audioSource!=null){audioSource.dispose();audioSource=null;}
        if(factory!=null){factory.dispose();factory=null;}
        if(audioManager!=null){
            audioManager.setSpeakerphoneOn(previousSpeaker);
            audioManager.setMode(previousAudioMode);
            audioManager=null;
        }
        remoteId=null;sessionId=null;
    }
    @Override protected void onDestroy(){
        hangup();super.onDestroy();
    }
}
