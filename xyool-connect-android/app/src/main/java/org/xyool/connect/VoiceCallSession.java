package org.xyool.connect;

import android.content.Context;
import android.media.AudioManager;
import android.os.Handler;
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
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Media belongs to the persistent foreground phone service, never to an Activity.
 * A new/recreated calling screen may attach/detach without dropping the call.
 * Android force-stop, revoked microphone permission, or service termination
 * will still end audio; this is not an indefinite background process guarantee.
 */
public final class VoiceCallSession {
    public interface Host {
        boolean enableMicrophoneForeground();
        boolean send(JSONObject message,boolean local);
        boolean dialLocal(String id);
        void closeLocal();
        java.util.List<PeerConnection.IceServer> currentTurnServers();
        void status(String message);
        void sessionChanged();
    }
    private static final String DEFAULT_STUN="stun:stun.cloudflare.com:3478";
    private final Context context;
    private final Handler main;
    private final Host host;
    private String remoteId, lastStatus="Ready for Xyool calls.";
    private boolean local,outgoing,authorized,remoteReady,muted,connected,relayOnlyTest;
    private PeerConnectionFactory factory;
    private PeerConnection peer;
    private AudioSource audioSource;
    private AudioTrack microphone;
    private AudioManager audioManager;
    private int oldMode=AudioManager.MODE_NORMAL;
    private boolean oldSpeaker=false;
    private final List<IceCandidate> pendingCandidates=new ArrayList<>();
    private IcePathInspector inspector=new IcePathInspector();
    private int iceRestartAttempts;
    private Runnable pendingIceRecovery;
    private Runnable pendingCheckingTimeout;
    private Runnable pendingRestartOutcome;
    private String lastIceState="NEW";
    private String lastIceReport="No previous call diagnostics.";
    private String iceRecoveryDecision="No recovery requested.";

    public VoiceCallSession(Context context,Handler main,Host host){
        this.context=context.getApplicationContext();
        this.main=main;this.host=host;
    }
    public boolean hasSession(){return remoteId!=null;}
    public boolean isIncoming(){return remoteId!=null&&!outgoing&&peer==null;}
    public boolean hasAudio(){return peer!=null;}
    public String peerId(){return remoteId;}
    public String state(){return lastStatus;}
    /** Safe to copy: counts and categories only; no IPs, keys, IDs or SDP. */
    public String diagnostics(){
        return peer==null?lastIceReport:
            inspector.summary()+
            "\nForce relay-only test: "+relayOnlyTest+
            "\nCall role: "+(outgoing?"caller":"receiver")+
            "\nRemote answer applied: "+remoteReady+
            "\nAutomatic ICE restarts: "+iceRestartAttempts+"/"+
                IceRecoveryPolicy.MAX_AUTOMATIC_RESTARTS+
            "\nRecovery: "+iceRecoveryDecision+
            "\nICE checking watchdog: "+(pendingCheckingTimeout!=null?"armed":"idle")+
            "\nRestart outcome watchdog: "+(pendingRestartOutcome!=null?"armed":"idle");
    }

    public boolean dial(String target,boolean localRoute){
        return dial(target,localRoute,false);
    }
    /** Explicit diagnostic call: force WebRTC to gather only relay paths. */
    public boolean dial(String target,boolean localRoute,boolean forceRelay){
        if(hasSession()||!SavedContacts.validId(target)||
            (localRoute&&forceRelay))return false;
        relayOnlyTest=forceRelay;
        remoteId=target;outgoing=true;local=localRoute;
        if(!startMedia()){clear(false);return false;}
        if(localRoute){
            if(!host.dialLocal(target)){clear(false);state("Nearby phone could not be reached.");return false;}
            state("Calling nearby "+target+"…");
        }else{
            try{
                JSONObject call=new JSONObject().put("type","call").put("to",target);
                if(!host.send(call,false)){clear(false);state("Signaling offline; could not call.");return false;}
                state("Calling "+target+" across networks…");
            }catch(Exception ignored){clear(false);return false;}
        }
        host.sessionChanged();
        return true;
    }
    public boolean accept(){
        if(!isIncoming())return false;
        if(!startMedia()){reject();return false;}
        // Local data-channel call invitations are signed at LocalPeerNode.
        if(local)authorized=true;
        try{
            if(!host.send(new JSONObject().put("type","accept"),local)){
                clear(false);state("Unable to accept call.");return false;
            }
        }catch(Exception ignored){clear(false);return false;}
        state("Call accepted. Connecting voice…");
        host.sessionChanged();
        return true;
    }
    public void reject(){
        if(!isIncoming())return;
        try{host.send(new JSONObject().put("type","reject"),local);}catch(Exception ignored){}
        clear(false);state("Call declined.");
    }
    public void hangup(){
        if(!hasSession())return;
        try{host.send(new JSONObject().put("type","hangup"),local);}catch(Exception ignored){}
        clear(false);state("Call ended.");
    }
    public void toggleMute(){
        if(microphone==null){state("No active voice call.");return;}
        muted=!muted;microphone.setEnabled(!muted);
        state(muted?"Microphone muted.":"Microphone unmuted.");
    }
    public void toggleSpeaker(){
        if(audioManager==null){state("No active voice call.");return;}
        boolean speaker=!audioManager.isSpeakerphoneOn();
        audioManager.setSpeakerphoneOn(speaker);
        state(speaker?"Speaker ON.":"Earpiece ON.");
    }

    /** Called by CallReachabilityService, whether or not the UI is attached. */
    public void onPacket(JSONObject msg,boolean localPacket){
        String type=msg.optString("type","");
        if("incoming".equals(type)){
            if(hasSession())return;
            String caller=msg.optString("from","");
            if(!SavedContacts.validId(caller))return;
            remoteId=caller;local=localPacket;outgoing=false;
            state("Incoming call from "+caller);
            host.sessionChanged();
            return;
        }
        if(!hasSession()||localPacket!=local)return;
        switch(type){
            case "ringing":
                state("Ringing "+remoteId+"…");break;
            case "accepted":
                if(peer==null)return;
                // The server sends accepted to BOTH participants. The callee
                // must authorize the incoming offer too, not just the caller.
                authorized=true;
                state("Call accepted. Connecting voice…");
                if(outgoing)createOffer();
                break;
            case "signal":
                signal(msg);break;
            case "ended":
                clear(false);state("Call ended: "+msg.optString("reason","disconnected"));break;
            case "busy":
                clear(false);state("That Xyool ID is already on a call.");break;
            case "unavailable":
                clear(false);state("That Xyool ID is currently unavailable.");break;
            case "error":
                clear(false);state("Signaling error: "+msg.optString("message","network error"));break;
            default: break;
        }
    }
    /** Rejected/expired incoming invitation while UI was away. */
    public void expired(){
        if(isIncoming()){clear(false);state("Missed Xyool call.");}
    }
    private void state(String message){
        lastStatus=message;
        main.post(()->host.status(message));
    }
    private boolean startMedia(){
        if(!host.enableMicrophoneForeground()){
            state("Microphone permission or Android foreground audio service unavailable.");
            return false;
        }
        try{
            final IcePathInspector diag=new IcePathInspector();
            diag.setDiscovery(local?"Verified local Wi-Fi signaling":"Xyool internet ID signaling");
            inspector=diag;
            PeerConnectionFactory.initialize(PeerConnectionFactory.InitializationOptions
                .builder(context).createInitializationOptions());
            factory=PeerConnectionFactory.builder().createPeerConnectionFactory();
            if(factory==null)throw new IllegalStateException("WebRTC unavailable");
            List<PeerConnection.IceServer> servers=new ArrayList<>();
            android.content.SharedPreferences config=context.getSharedPreferences(
                "xyool_private",Context.MODE_PRIVATE);
            String stun=config.getString("xyool_stun","").trim();
            if(!local&&stun.isEmpty())stun=DEFAULT_STUN;
            if("off".equalsIgnoreCase(stun))stun="";
            if(!stun.isEmpty()){
                if(!stun.matches("^stuns?:[A-Za-z0-9._-]+:[0-9]{2,5}$"))
                    throw new IllegalArgumentException("Stored STUN server invalid");
                servers.add(PeerConnection.IceServer.builder(stun).createIceServer());
            }
            String turn=config.getString("xyool_turn","").trim();
            if(!local&&!turn.isEmpty()){
                if(!turn.matches("^turns?:[A-Za-z0-9._-]+:[0-9]{2,5}(\\?transport=(udp|tcp))?$"))
                    throw new IllegalArgumentException("Stored TURN server invalid");
                String username=config.getString("xyool_turn_user","");
                String password=config.getString("xyool_turn_pass","");
                if(username.isEmpty()||password.isEmpty())
                    throw new IllegalArgumentException("Stored TURN credentials missing");
                servers.add(PeerConnection.IceServer.builder(turn)
                    .setUsername(username).setPassword(password).createIceServer());
            }
            // Short-lived credentials from the registered signaling service
            // are preferred over optional legacy manual TURN settings.
            java.util.List<PeerConnection.IceServer> ephemeral=
                local?java.util.Collections.emptyList():host.currentTurnServers();
            if(ephemeral!=null&&!ephemeral.isEmpty())servers.addAll(ephemeral);
            boolean turnReady=!local&&(!turn.isEmpty()||
                (ephemeral!=null&&!ephemeral.isEmpty()));
            if(relayOnlyTest&&!turnReady)
                throw new IllegalStateException("TURN credentials unavailable for relay test");
            diag.setTurnConfigured(turnReady);
            iceRestartAttempts=0;
            lastIceState="NEW";
            iceRecoveryDecision="No recovery requested.";
            PeerConnection.RTCConfiguration configuration=new PeerConnection.RTCConfiguration(servers);
            if(relayOnlyTest)configuration.iceTransportsType=PeerConnection.IceTransportsType.RELAY;
            peer=factory.createPeerConnection(configuration,new PeerConnection.Observer(){
                @Override public void onSignalingChange(PeerConnection.SignalingState state){}
                @Override public void onIceConnectionChange(PeerConnection.IceConnectionState state){
                    main.post(()->{
                        if(inspector!=diag||peer==null||remoteId==null)return;
                        diag.setState(state.name());
                        lastIceState=state.name();
                        if(state==PeerConnection.IceConnectionState.CHECKING){
                            // ICE may never emit FAILED on restrictive Wi-Fi.
                            // A watchdog prevents an indefinite spinner.
                            armCheckingTimeout(diag);
                            VoiceCallSession.this.state("Connecting audio across networks…");
                        }else if(state==PeerConnection.IceConnectionState.CONNECTED||
                            state==PeerConnection.IceConnectionState.COMPLETED){
                            connected=true;
                            cancelIceRecovery();
                            cancelCheckingTimeout();
                            cancelRestartOutcomeTimeout();
                            iceRecoveryDecision=IceRecoveryPolicy.connectedOutcome(
                                iceRestartAttempts);
                            VoiceCallSession.this.state(iceRestartAttempts>0?
                                "Encrypted voice connected after ICE restart.":
                                "Encrypted voice connected.");
                        }else if(state==PeerConnection.IceConnectionState.FAILED){
                            connected=false;
                            cancelCheckingTimeout();
                            if(iceRestartAttempts>=IceRecoveryPolicy.MAX_AUTOMATIC_RESTARTS){
                                cancelRestartOutcomeTimeout();
                                iceRecoveryDecision="ICE failed after one automatic retry; no confirmed media path";
                                VoiceCallSession.this.state(
                                    "Voice ICE failed after recovery; TURN relay may be needed.");
                            }else{
                                scheduleIceRecovery(diag,1200L);
                                if(pendingIceRecovery!=null)
                                    VoiceCallSession.this.state("ICE failed. Preparing recovery…");
                                else
                                    VoiceCallSession.this.state("Voice ICE failed: "+diag.interpretation());
                            }
                        }else if(state==PeerConnection.IceConnectionState.DISCONNECTED){
                            connected=false;
                            cancelCheckingTimeout();
                            if(iceRestartAttempts==0)
                                scheduleIceRecovery(diag,10000L);
                            VoiceCallSession.this.state("Voice disconnected; checking network…");
                        }
                    });
                }
                @Override public void onIceConnectionReceivingChange(boolean receiving){}
                @Override public void onIceGatheringChange(PeerConnection.IceGatheringState state){}
                @Override public void onIceCandidate(IceCandidate candidate){
                    if(inspector!=diag)return;
                    diag.record(candidate.sdp);
                    try{
                        JSONObject frame=new JSONObject().put("type","signal")
                            .put("kind","candidate").put("candidate",candidate.sdp)
                            .put("mid",candidate.sdpMid==null?"":candidate.sdpMid)
                            .put("index",candidate.sdpMLineIndex);
                        host.send(frame,local);
                    }catch(Exception ignored){}
                }
                @Override public void onIceCandidatesRemoved(IceCandidate[] candidates){}
                @Override public void onAddStream(MediaStream stream){}
                @Override public void onRemoveStream(MediaStream stream){}
                @Override public void onDataChannel(DataChannel channel){}
                @Override public void onRenegotiationNeeded(){}
                @Override public void onAddTrack(RtpReceiver receiver,MediaStream[] streams){}
            });
            if(peer==null)throw new IllegalStateException("WebRTC peer unavailable");
            audioSource=factory.createAudioSource(new MediaConstraints());
            microphone=factory.createAudioTrack("xyool-microphone",audioSource);
            microphone.setEnabled(true);
            if(peer.addTrack(microphone,Collections.singletonList("xyool-media"))==null)
                throw new IllegalStateException("Unable to attach microphone");
            audioManager=(AudioManager)context.getSystemService(Context.AUDIO_SERVICE);
            if(audioManager!=null){
                oldMode=audioManager.getMode();oldSpeaker=audioManager.isSpeakerphoneOn();
                audioManager.setMode(AudioManager.MODE_IN_COMMUNICATION);
                // Earpiece default avoids piercing feedback when phones are close.
                audioManager.setSpeakerphoneOn(false);
            }
            muted=false;connected=false;remoteReady=false;pendingCandidates.clear();
            cancelIceRecovery();
            return true;
        }catch(Exception e){
            state("Audio failed: "+e.getClass().getSimpleName());
            releaseMedia();
            return false;
        }
    }
    /** Time out an ICE CHECKING state that never emits FAILED. */
    private void armCheckingTimeout(IcePathInspector diag){
        if(pendingCheckingTimeout!=null||pendingRestartOutcome!=null)return;
        final PeerConnection expected=peer;
        Runnable timeout=()->{
            pendingCheckingTimeout=null;
            if(peer!=expected||inspector!=diag||
                !IceRecoveryPolicy.shouldWatchChecking(lastIceState,hasSession(),connected))
                return;
            if(iceRestartAttempts>=IceRecoveryPolicy.MAX_AUTOMATIC_RESTARTS){
                iceRecoveryDecision="ICE still checking after restart; no working media path";
                state("ICE still checking after retry. TURN relay may be needed.");
                return;
            }
            if(!outgoing){
                iceRecoveryDecision="Receiver cannot initiate ICE restart on current signaling server";
                state("ICE checking timed out. Caller must retry; TURN relay may be needed.");
                return;
            }
            scheduleIceRecovery(diag,0L);
            if(pendingIceRecovery!=null){
                state("ICE checking timed out; attempting one automatic restart…");
            }else{
                state("ICE checking timed out: "+iceRecoveryDecision+".");
            }
        };
        pendingCheckingTimeout=timeout;
        main.postDelayed(timeout,IceRecoveryPolicy.CHECKING_TIMEOUT_MS);
    }
    private void cancelCheckingTimeout(){
        if(pendingCheckingTimeout!=null){
            main.removeCallbacks(pendingCheckingTimeout);
            pendingCheckingTimeout=null;
        }
    }
    /** Prevent the restarted offer from leaving the screen stuck forever. */
    private void armRestartOutcomeTimeout(IcePathInspector diag){
        cancelRestartOutcomeTimeout();
        final PeerConnection expected=peer;
        Runnable timeout=()->{
            pendingRestartOutcome=null;
            if(peer!=expected||inspector!=diag||remoteId==null||connected)return;
            iceRecoveryDecision="No connected ICE pair within 30 seconds of automatic restart";
            state("Audio restart timed out. Direct paths failed; TURN relay may be needed.");
        };
        pendingRestartOutcome=timeout;
        main.postDelayed(timeout,IceRecoveryPolicy.RESTART_OUTCOME_TIMEOUT_MS);
    }
    private void cancelRestartOutcomeTimeout(){
        if(pendingRestartOutcome!=null){
            main.removeCallbacks(pendingRestartOutcome);
            pendingRestartOutcome=null;
        }
    }
    /** Only the original caller may send an SDP offer through current server. */
    private void scheduleIceRecovery(IcePathInspector diag,long delayMs){
        boolean stable=peer!=null&&
            peer.signalingState()==PeerConnection.SignalingState.STABLE;
        if(!outgoing||!authorized||remoteId==null||peer==null||
            iceRestartAttempts>=IceRecoveryPolicy.MAX_AUTOMATIC_RESTARTS){
            iceRecoveryDecision=IceRecoveryPolicy.reason(outgoing,hasSession(),
                authorized,remoteReady,stable,iceRestartAttempts);
            return;
        }
        if(pendingIceRecovery!=null){
            iceRecoveryDecision="ICE retry waiting for scheduled attempt";
            return;
        }
        final PeerConnection expected=peer;
        Runnable retry=()->{
            pendingIceRecovery=null;
            if(peer!=expected||inspector!=diag||remoteId==null||connected){
                iceRecoveryDecision="Recovery canceled: call or ICE state changed";
                return;
            }
            boolean nowStable=expected.signalingState()==PeerConnection.SignalingState.STABLE;
            iceRecoveryDecision=IceRecoveryPolicy.reason(outgoing,hasSession(),
                authorized,remoteReady,nowStable,iceRestartAttempts);
            if(!IceRecoveryPolicy.mayRestart(outgoing,hasSession(),authorized,
                remoteReady,nowStable,iceRestartAttempts)){
                state("ICE retry not possible. "+iceRecoveryDecision+".");
                return;
            }
            iceRestartAttempts++;
            cancelCheckingTimeout();
            armRestartOutcomeTimeout(diag);
            iceRecoveryDecision="ICE restart offer being negotiated";
            remoteReady=false;
            pendingCandidates.clear();
            state("Reconnecting voice (ICE restart 1/1)…");
            MediaConstraints constraints=new MediaConstraints();
            constraints.mandatory.add(new MediaConstraints.KeyValuePair(
                "IceRestart","true"));
            expected.createOffer(new SdpCallbacks(){
                @Override public void onCreateSuccess(SessionDescription offer){
                    if(peer==expected&&remoteId!=null)setLocalAndSend(offer);
                }
            },constraints);
        };
        pendingIceRecovery=retry;
        iceRecoveryDecision="ICE retry scheduled";
        main.postDelayed(retry,delayMs);
    }
    private void cancelIceRecovery(){
        if(pendingIceRecovery!=null){
            main.removeCallbacks(pendingIceRecovery);
            pendingIceRecovery=null;
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
                try{host.send(new JSONObject().put("type","signal")
                    .put("kind",desc.type.canonicalForm())
                    .put("sdp",desc.description),local);
                }catch(Exception ignored){state("Unable to signal audio setup.");}
            }
        },desc);
    }
    private void signal(JSONObject message){
        if(peer==null||!authorized)return;
        String kind=message.optString("kind","");
        if("candidate".equals(kind)){
            String mid=message.optString("mid",""),sdp=message.optString("candidate","");
            int index=message.optInt("index",-1);
            if(sdp.length()>4000||index<0||index>50||mid.length()>50)return;
            IceCandidate candidate=new IceCandidate(mid,index,sdp);
            inspector.recordRemote(sdp);
            if(remoteReady)peer.addIceCandidate(candidate);
            else if(pendingCandidates.size()<96)pendingCandidates.add(candidate);
            return;
        }
        if(!("offer".equals(kind)||"answer".equals(kind)))return;
        if(outgoing&&!kind.equals("answer"))return;
        if(!outgoing&&!kind.equals("offer"))return;
        String sdp=message.optString("sdp","");
        if(!sdp.startsWith("v=0")||sdp.length()<80||sdp.length()>32000)return;
        // A renegotiated ICE offer/answer must not reuse the old remote
        // description when incoming trickle candidates arrive early.
        remoteReady=false;
        SessionDescription desc=new SessionDescription("offer".equals(kind)?
            SessionDescription.Type.OFFER:SessionDescription.Type.ANSWER,sdp);
        peer.setRemoteDescription(new SdpCallbacks(){
            @Override public void onSetSuccess(){
                remoteReady=true;
                for(IceCandidate candidate:pendingCandidates)
                    if(peer!=null)peer.addIceCandidate(candidate);
                pendingCandidates.clear();
                if(!outgoing&&peer!=null)
                    peer.createAnswer(new SdpCallbacks(){
                        @Override public void onCreateSuccess(SessionDescription localDesc){
                            setLocalAndSend(localDesc);
                        }
                    },new MediaConstraints());
            }
        },desc);
    }
    private abstract class SdpCallbacks implements SdpObserver{
        @Override public void onCreateSuccess(SessionDescription desc){}
        @Override public void onSetSuccess(){}
        @Override public void onCreateFailure(String why){state("Audio offer failed.");}
        @Override public void onSetFailure(String why){state("Audio negotiation failed.");}
    }
    private void clear(boolean unused){
        lastIceReport=diagnostics();
        boolean wasLocal=local;
        remoteId=null;outgoing=false;authorized=false;remoteReady=false;
        local=false;connected=false;relayOnlyTest=false;
        releaseMedia();
        if(wasLocal)host.closeLocal();
        host.sessionChanged();
    }
    private void releaseMedia(){
        cancelIceRecovery();
        cancelCheckingTimeout();
        cancelRestartOutcomeTimeout();
        inspector=new IcePathInspector();
        pendingCandidates.clear();
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
    public void destroy(){clear(false);}
}
