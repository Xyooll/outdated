package org.xyool.connect;

/**
 * Xyool's routing policy is deliberately independent of any one infrastructure
 * provider. It decides only which ALREADY-IMPLEMENTED transports may be used.
 *
 * NOTE: federated Web3 discovery and volunteer peer relays are future adapters,
 * not available paths. Never label an unimplemented path "connected".
 */
public final class BridgePolicy {
    public static final String PREF_MODE = "xyool_bridge_mode";
    public static final String DIRECT_ONLY = "direct_only";
    public static final String HYBRID = "hybrid";

    public enum Route {
        LOCAL_DIRECT,
        WEB2_SIGNAL_DIRECT_MEDIA,
        MANUAL_DIRECT_REQUIRED
    }

    private BridgePolicy() { }

    public static String sanitize(String mode) {
        return DIRECT_ONLY.equals(mode) ? DIRECT_ONLY : HYBRID;
    }

    public static boolean allowsCloud(String mode) {
        return HYBRID.equals(sanitize(mode));
    }

    public static Route choose(String mode, boolean nearbyPeer, boolean
            cloudRegistered) {
        if (nearbyPeer) return Route.LOCAL_DIRECT;
        if (allowsCloud(mode) && cloudRegistered)
            return Route.WEB2_SIGNAL_DIRECT_MEDIA;
        return Route.MANUAL_DIRECT_REQUIRED;
    }

    public static String description(String mode) {
        if (DIRECT_ONLY.equals(sanitize(mode))) {
            return "Direct-only: no Xyool cloud registration, nearby calls or " +
                "manually shared direct WebRTC codes. Cross-network calling " +
                "depends on reachable ICE paths.";
        }
        return "Hybrid: nearby phones connect directly; other IDs use Xyool's " +
            "optional Web2 signaling server to coordinate WebRTC. No Web3 " +
            "discovery or automatic TURN fallback has been implemented yet.";
    }
}
