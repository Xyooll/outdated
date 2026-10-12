package org.xyool.connect;

import android.Manifest;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.ActivityNotFoundException;
import android.content.ClipData;
import android.content.ClipboardManager;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.media.AudioManager;
import android.os.Bundle;
import android.text.InputType;
import android.util.Base64;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import android.graphics.drawable.GradientDrawable;
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
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

/**
 * Xyool's experimental NATIVE one-to-one encrypted WebRTC audio.
 *
 * Signaling is exchanged manually via out-of-band encrypted messenger;
 * no third-party conference, SIP app, server, account or WebView is used.
 * A configurable STUN / TURN server is OPTIONAL for connectivity outside LAN.
 *
 * Not a dialer, not a production calling service, and not yet an identity-
 * authenticated or independently audited encrypted calling application.
 */
public final class NativeVoiceActivity extends Activity {
    private static final int BG = 0xff0c1822, CARD = 0xff192f3b;
    private static final int FG = 0xfff0faf7, SUB = 0xffaec8cf, ACC = 0xff68dbc3;
    private static final int MICROPHONE_PERMISSION = 910;
    private PeerConnectionFactory factory;
    private PeerConnection peer;
    private AudioSource source;
    private AudioTrack localAudio;
    private AudioManager audioManager;
    private int oldAudioMode = AudioManager.MODE_NORMAL;
    private boolean oldSpeakerphone;
    private TextView status, output;
    private EditText incoming, stun, turn, user, secret;
    private String generated = "";
    private boolean closed;
    private boolean caller;
    private boolean gatheringComplete;

    @Override public void onCreate(Bundle savedState) {
        super.onCreate(savedState);
        getWindow().setStatusBarColor(BG);
        getWindow().setNavigationBarColor(BG);
        build();
    }

    private int dp(float value) {
        return (int)(value * getResources().getDisplayMetrics().density + 0.5f);
    }
    private TextView text(String s, int size, int color, boolean bold) {
        TextView t = new TextView(this);
        t.setText(s);
        t.setTextSize(size);
        t.setTextColor(color);
        if (bold) t.setTypeface(null, 1);
        t.setTextIsSelectable(false);
        return t;
    }
    private GradientDrawable bg(int c) {
        GradientDrawable d = new GradientDrawable();
        d.setCornerRadius(dp(13));
        d.setColor(c);
        d.setStroke(dp(1), 0xff385766);
        return d;
    }
    private LinearLayout column() {
        LinearLayout l = new LinearLayout(this);
        l.setOrientation(LinearLayout.VERTICAL);
        return l;
    }
    private void gap(LinearLayout col, int h) {
        col.addView(new View(this), new LinearLayout.LayoutParams(dp(1), dp(h)));
    }
    private LinearLayout card(LinearLayout parent) {
        LinearLayout result = column();
        result.setPadding(dp(14),dp(14),dp(14),dp(14));
        result.setBackground(bg(CARD));
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(-1,-2);
        lp.bottomMargin=dp(12);
        parent.addView(result,lp);
        return result;
    }
    private Button button(LinearLayout parent, String label, boolean primary, View.OnClickListener action) {
        Button b = new Button(this);
        b.setText(label);
        b.setAllCaps(false);
        b.setTextSize(14);
        b.setTextColor(primary ? BG : FG);
        b.setBackground(bg(primary ? ACC : 0xff274c55));
        b.setOnClickListener(action);
        parent.addView(b,new LinearLayout.LayoutParams(-1,dp(49)));
        return b;
    }
    private EditText entry(LinearLayout parent, String hint, boolean multiline) {
        EditText e = new EditText(this);
        e.setTextColor(FG); e.setHintTextColor(0xff96aeb6);
        e.setTextSize(multiline ? 12 : 14);
        e.setHint(hint);
        e.setPadding(dp(11),dp(11),dp(11),dp(11));
        e.setBackground(bg(0xff0e2531));
        if (multiline) {
            e.setSingleLine(false);
            e.setInputType(InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_FLAG_MULTI_LINE);
            e.setMinLines(3);
            e.setMaxLines(6);
            e.setGravity(Gravity.TOP);
        } else {
            e.setSingleLine(true);
            e.setInputType(InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_URI);
        }
        parent.addView(e,new LinearLayout.LayoutParams(-1,-2));
        return e;
    }
    private void build() {
        LinearLayout root = column();
        root.setBackgroundColor(BG);
        ScrollView scroll = new ScrollView(this);
        LinearLayout content = column();
        content.setPadding(dp(15),dp(16),dp(15),dp(14));
        scroll.addView(content);
        root.addView(scroll,new LinearLayout.LayoutParams(-1,0,1f));
        button(root,"← Back to Xyool Connect",false,v->finish());
        setContentView(root);

        content.addView(text("XYOOL NATIVE VOICE · ALPHA",11,ACC,true));
        gap(content,7);
        content.addView(text("Direct peer-to-peer call",27,FG,true));
        gap(content,8);
        content.addView(text("A real native WebRTC microphone-to-speaker connection. No Jitsi room, Linphone app, accounts, or Xyool server is used. Both people need this app installed.",13,SUB,false));
        gap(content,14);

        LinearLayout connection=card(content);
        connection.addView(text("Connectivity settings (optional)",17,FG,true));
        gap(connection,5);
        connection.addView(text("On the same Wi-Fi LAN, try leaving these blank. Across the internet, set your STUN and, ideally, a TURN server. Both phones need reachable connectivity. No Google STUN server is preconfigured.",12,SUB,false));
        gap(connection,9);
        stun=entry(connection,"stun:your-stun.example:3478",false);
        gap(connection,7);
        turn=entry(connection,"turn:your-turn.example:3478 (optional)",false);
        gap(connection,7);
        user=entry(connection,"TURN username (optional)",false);
        gap(connection,7);
        secret=entry(connection,"TURN password (optional)",false);
        secret.setInputType(InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_PASSWORD);

        LinearLayout actions=card(content);
        actions.addView(text("Start the handshake",17,FG,true));
        gap(actions,7);
        button(actions,"A · Create offer (caller)",true,v->startOffer());
        gap(actions,9);
        button(actions,"B · Accept pasted offer (receiver)",false,v->applyIncoming(true));
        gap(actions,9);
        button(actions,"A · Complete with pasted answer",false,v->applyIncoming(false));

        LinearLayout exchange=card(content);
        exchange.addView(text("Exchange setup messages privately",17,FG,true));
        gap(exchange,6);
        exchange.addView(text("Caller sends OFFER to receiver. Receiver pastes it, presses B, waits for ANSWER, and sends that back. Caller pastes ANSWER and presses A complete. These setup messages can be several KB.",12,SUB,false));
        gap(exchange,9);
        incoming=entry(exchange,"Paste XYOOL1: offer or answer here",true);
        gap(exchange,12);
        output=text("No handshake message created yet.",12,ACC,false);
        output.setTextIsSelectable(true);
        exchange.addView(output);
        gap(exchange,10);
        button(exchange,"Copy my generated message",false,v->copyGenerated());
        gap(exchange,8);
        button(exchange,"Share my generated message",false,v->shareGenerated());

        LinearLayout call=card(content);
        call.addView(text("Connection status",17,FG,true));
        gap(call,8);
        status=text("Idle. Microphone permission is requested only when you start.",13,SUB,false);
        call.addView(status);
        gap(call,10);
        button(call,"Hang up / Reset",false,v->reset());
        gap(call,11);
        call.addView(text("Important: This is foreground-only experimental audio with no verified identity, push ringing, call history, failover, or guaranteed emergency access. Never use it for 911. SDP setup messages can expose local/public IP addresses and must be exchanged through a trusted private channel.",12,SUB,false));
    }

    private void say(String s) {
        runOnUiThread(()->{if(status!=null)status.setText(s);});
    }
    private void startOffer() {
        if (peer!=null) { say("Hang up and reset before starting another call."); return; }
        caller=true;
        withMicrophone(()->{
            if (!newPeer()) return;
            say("Creating offer...");
            peer.createOffer(new SimpleSdp() {
                @Override public void onCreateSuccess(SessionDescription sdp) {
                    if(peer!=null)peer.setLocalDescription(new SimpleSdp() {
                        @Override public void onSetSuccess() {
                            say("Offer saved locally. Gathering network paths...");
                            publishIfGathered();
                        }
                    },sdp);
                }
            },new MediaConstraints());
        });
    }
    private void applyIncoming(boolean offer) {
        if (incoming==null) return;
        SessionDescription remote=parse(incoming.getText().toString(),offer);
        if(remote==null) { say("Invalid or wrong handshake message. Paste the full XYOOL1 message."); return; }
        if (offer) {
            if (peer!=null) { say("Hang up and reset before accepting a new offer."); return; }
            caller=false;
            withMicrophone(()->{
                if(!newPeer())return;
                peer.setRemoteDescription(new SimpleSdp() {
                    @Override public void onSetSuccess() {
                        say("Offer accepted. Creating answer...");
                        if(peer==null)return;
                        peer.createAnswer(new SimpleSdp(){
                            @Override public void onCreateSuccess(SessionDescription reply) {
                                if(peer!=null)peer.setLocalDescription(new SimpleSdp(){
                                    @Override public void onSetSuccess() {
                                        say("Answer saved locally. Gathering network paths...");
                                        publishIfGathered();
                                    }
                                },reply);
                            }
                        },new MediaConstraints());
                    }
                },remote);
            });
        } else {
            if (peer==null||!caller||peer.getRemoteDescription()!=null) {
                say("Start as caller first. Only a caller with an offer can accept an answer.");
                return;
            }
            peer.setRemoteDescription(new SimpleSdp(){
                @Override public void onSetSuccess(){ say("Remote answer applied. Waiting for encrypted connection..."); }
            },remote);
        }
    }
    private void withMicrophone(Runnable action) {
        if(checkSelfPermission(Manifest.permission.RECORD_AUDIO)==PackageManager.PERMISSION_GRANTED)action.run();
        else {
            pending=action;
            requestPermissions(new String[]{Manifest.permission.RECORD_AUDIO},MICROPHONE_PERMISSION);
        }
    }
    private Runnable pending;
    @Override public void onRequestPermissionsResult(int req,String[] perms,int[] grants) {
        super.onRequestPermissionsResult(req,perms,grants);
        if(req!=MICROPHONE_PERMISSION)return;
        Runnable run=pending; pending=null;
        if(grants.length>0 && grants[0]==PackageManager.PERMISSION_GRANTED && run!=null)run.run();
        else say("Microphone access denied. Voice calling cannot start.");
    }
    private List<PeerConnection.IceServer> servers() {
        List<PeerConnection.IceServer> list=new ArrayList<>();
        String s=stun.getText().toString().trim();
        String t=turn.getText().toString().trim();
        if (!s.isEmpty()) {
            if(!s.matches("^stuns?:[a-zA-Z0-9._-]{3,253}:[0-9]{2,5}$"))throw new IllegalArgumentException("Invalid STUN server URL.");
            list.add(PeerConnection.IceServer.builder(s).createIceServer());
        }
        if (!t.isEmpty()) {
            if(!t.matches("^turns?:[a-zA-Z0-9._-]{3,253}:[0-9]{2,5}(\\?transport=(udp|tcp))?$"))
                throw new IllegalArgumentException("Invalid TURN server URL.");
            String username=user.getText().toString();
            String password=secret.getText().toString();
            if(username.isEmpty()||password.isEmpty())throw new IllegalArgumentException("TURN credentials are required.");
            list.add(PeerConnection.IceServer.builder(t).setUsername(username).setPassword(password).createIceServer());
        }
        return list;
    }
    private boolean newPeer() {
        try {
            closed=false;
            gatheringComplete=false;
            generated="";
            output.setText("Waiting for ICE gathering...");
            List<PeerConnection.IceServer> ice=servers();
            PeerConnectionFactory.initialize(PeerConnectionFactory.InitializationOptions.builder(getApplicationContext()).createInitializationOptions());
            factory=PeerConnectionFactory.builder().createPeerConnectionFactory();
            if(factory==null) throw new IllegalStateException("WebRTC library not initialized");
            PeerConnection.RTCConfiguration config=new PeerConnection.RTCConfiguration(ice);
            peer=factory.createPeerConnection(config,new PeerConnection.Observer() {
                @Override public void onSignalingChange(PeerConnection.SignalingState value) { }
                @Override public void onIceConnectionChange(PeerConnection.IceConnectionState value) {
                    say("ICE connection: "+value+". "+(value==PeerConnection.IceConnectionState.CONNECTED||value==PeerConnection.IceConnectionState.COMPLETED?"Native encrypted audio path established.":"Keep app open."));
                }
                @Override public void onIceConnectionReceivingChange(boolean value) { }
                @Override public void onIceGatheringChange(PeerConnection.IceGatheringState value) {
                    if(value==PeerConnection.IceGatheringState.COMPLETE) {
                        gatheringComplete=true;
                        publishIfGathered();
                    }
                }
                @Override public void onIceCandidate(IceCandidate candidate) { }
                @Override public void onIceCandidatesRemoved(IceCandidate[] candidates) { }
                @Override public void onAddStream(MediaStream stream) { }
                @Override public void onRemoveStream(MediaStream stream) { }
                @Override public void onDataChannel(DataChannel channel) { }
                @Override public void onRenegotiationNeeded() { }
                @Override public void onAddTrack(RtpReceiver receiver,MediaStream[] streams) { }
            });
            if(peer==null)throw new IllegalStateException("Cannot create P2P connection");
            source=factory.createAudioSource(new MediaConstraints());
            localAudio=factory.createAudioTrack("xyool-audio",source);
            localAudio.setEnabled(true);
            if(peer.addTrack(localAudio,java.util.Collections.singletonList("xyool-stream"))==null)
                throw new IllegalStateException("Cannot attach audio track");
            audioManager=(AudioManager)getSystemService(Context.AUDIO_SERVICE);
            if(audioManager!=null) {
                oldAudioMode=audioManager.getMode();
                oldSpeakerphone=audioManager.isSpeakerphoneOn();
                audioManager.setMode(AudioManager.MODE_IN_COMMUNICATION);
                audioManager.setSpeakerphoneOn(true);
            }
            say("Local native microphone connected. Waiting for handshake...");
            return true;
        } catch(Exception e) {
            say("Cannot start: "+e.getMessage());
            cleanup();
            return false;
        }
    }
    private void publishIfGathered() {
        if(!gatheringComplete||peer==null||peer.getLocalDescription()==null)return;
        SessionDescription local=peer.getLocalDescription();
        try {
            JSONObject data=new JSONObject();
            data.put("version",1);
            data.put("type",local.type.canonicalForm());
            data.put("sdp",local.description);
            String encoded="XYOOL1:"+Base64.encodeToString(data.toString().getBytes(StandardCharsets.UTF_8),
                Base64.URL_SAFE|Base64.NO_PADDING|Base64.NO_WRAP);
            runOnUiThread(()->{
                generated=encoded;
                output.setText(encoded);
                say(local.type==SessionDescription.Type.OFFER?
                    "Offer ready. Copy/share it with the receiver; then paste their answer.":
                    "Answer ready. Copy/share it back to the caller. Stay in this app for the voice call.");
            });
        } catch(Exception e) { say("Could not encode handshake: "+e.getMessage()); }
    }
    private SessionDescription parse(String raw,boolean expectedOffer) {
        String trimmed=raw.trim();
        if(!trimmed.startsWith("XYOOL1:")||trimmed.length()>50000)return null;
        try {
            byte[] data=Base64.decode(trimmed.substring(7),Base64.URL_SAFE|Base64.NO_WRAP);
            if(data.length>36000)return null;
            JSONObject obj=new JSONObject(new String(data,StandardCharsets.UTF_8));
            String type=expectedOffer?"offer":"answer";
            if(obj.getInt("version")!=1||!type.equals(obj.getString("type")))return null;
            String sdp=obj.getString("sdp");
            if(sdp.length()<80||sdp.length()>32000||!sdp.startsWith("v=0"))return null;
            return new SessionDescription(expectedOffer?SessionDescription.Type.OFFER:SessionDescription.Type.ANSWER,sdp);
        } catch(Exception e) { return null; }
    }
    private void copyGenerated() {
        if(generated.isEmpty()) {say("No message to copy yet.");return;}
        ClipboardManager m=(ClipboardManager)getSystemService(Context.CLIPBOARD_SERVICE);
        if(m!=null)m.setPrimaryClip(ClipData.newPlainText("Xyool connection handshake",generated));
        say("Handshake copied. Share it privately. Clipboard data may be visible to other software.");
    }
    private void shareGenerated() {
        if(generated.isEmpty()) {say("No message to share yet.");return;}
        Intent share=new Intent(Intent.ACTION_SEND);
        share.setType("text/plain");
        share.putExtra(Intent.EXTRA_TEXT,generated);
        try {startActivity(Intent.createChooser(share,"Share Xyool handshake securely"));}
        catch(ActivityNotFoundException e){say("No text-sharing app was found.");}
    }
    private void reset() {
        cleanup();
        generated="";
        incoming.setText("");
        output.setText("No handshake message created yet.");
        say("Call ended. Ready to start another one.");
    }
    private void cleanup() {
        closed=true;
        if(peer!=null){peer.close();peer.dispose();peer=null;}
        if(localAudio!=null){localAudio.dispose();localAudio=null;}
        if(source!=null){source.dispose();source=null;}
        if(factory!=null){factory.dispose();factory=null;}
        if(audioManager!=null) {
            audioManager.setSpeakerphoneOn(oldSpeakerphone);
            audioManager.setMode(oldAudioMode);
            audioManager=null;
        }
        gatheringComplete=false;
    }
    @Override protected void onDestroy(){cleanup();super.onDestroy();}

    private abstract class SimpleSdp implements SdpObserver {
        @Override public void onCreateSuccess(SessionDescription desc) { }
        @Override public void onSetSuccess() { }
        @Override public void onCreateFailure(String reason){say("SDP creation failed: "+reason);}
        @Override public void onSetFailure(String reason){say("SDP application failed: "+reason);}
    }
}
