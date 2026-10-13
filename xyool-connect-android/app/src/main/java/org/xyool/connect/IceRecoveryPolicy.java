package org.xyool.connect;

/**
 * Fail-closed recovery policy for WebRTC calls.
 * Server enforces that only the ORIGINAL caller may send SDP offers; a
 * receiver cannot start an ICE renegotiation without server protocol changes.
 */
public final class IceRecoveryPolicy {
    public static final int MAX_AUTOMATIC_RESTARTS=1;
    private IceRecoveryPolicy(){}

    public static boolean mayRestart(boolean caller,boolean sessionLive,
        boolean accepted,boolean remoteReady,boolean stable,int attempts) {
        return caller && sessionLive && accepted && remoteReady &&
            stable && attempts>=0 && attempts<MAX_AUTOMATIC_RESTARTS;
    }
}
