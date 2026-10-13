package org.xyool.connect;

/**
 * Fail-closed recovery policy for WebRTC calls.
 * Server enforces that only the ORIGINAL caller may send SDP offers; a
 * receiver cannot start an ICE renegotiation without server protocol changes.
 */
public final class IceRecoveryPolicy {
    public static final int MAX_AUTOMATIC_RESTARTS=1;
    private IceRecoveryPolicy(){}

    public static String reason(boolean caller,boolean sessionLive,
        boolean accepted,boolean remoteReady,boolean stable,int attempts){
        if(!sessionLive)return "No active Xyool call";
        if(!caller)return "Receiving phone: current signaling permits only caller-initiated ICE restarts";
        if(attempts<0)return "Invalid restart count";
        if(attempts>=MAX_AUTOMATIC_RESTARTS)return "Automatic retry budget exhausted";
        if(!accepted)return "Waiting for call acceptance";
        if(!remoteReady)return "Waiting for remote SDP answer";
        if(!stable)return "Signaling negotiation not stable";
        return "Ready to restart";
    }

    public static boolean mayRestart(boolean caller,boolean sessionLive,
        boolean accepted,boolean remoteReady,boolean stable,int attempts) {
        return caller && sessionLive && accepted && remoteReady &&
            stable && attempts>=0 && attempts<MAX_AUTOMATIC_RESTARTS;
    }
}
