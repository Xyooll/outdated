package org.xyool.connect;

/** No JUnit needed: compile and run this with stock JDK 17 in GitHub Actions. */
public final class BridgeSelfTest {
    private static int passed;
    private static void require(boolean v,String message){
        if(!v)throw new AssertionError(message);
        passed++;
    }
    public static void main(String[] args) {
        require(BridgePolicy.HYBRID.equals(BridgePolicy.sanitize("other")),
            "unknown mode must safely default to existing hybrid behavior");
        require(!BridgePolicy.allowsCloud(BridgePolicy.DIRECT_ONLY),
            "direct-only cannot register with Web2 signaling");
        require(BridgePolicy.allowsCloud(BridgePolicy.HYBRID),
            "hybrid supports optional existing Web2 signaling");
        require(BridgePolicy.choose(BridgePolicy.DIRECT_ONLY,true,false)
            ==BridgePolicy.Route.LOCAL_DIRECT,"direct local");
        require(BridgePolicy.choose(BridgePolicy.HYBRID,true,true)
            ==BridgePolicy.Route.LOCAL_DIRECT,"local always first");
        require(BridgePolicy.choose(BridgePolicy.DIRECT_ONLY,false,true)
            ==BridgePolicy.Route.MANUAL_DIRECT_REQUIRED,"direct never silently falls back");
        require(BridgePolicy.choose(BridgePolicy.HYBRID,false,true)
            ==BridgePolicy.Route.WEB2_SIGNAL_DIRECT_MEDIA,"Web2 only when permitted");
        require(BridgePolicy.choose(BridgePolicy.HYBRID,false,false)
            ==BridgePolicy.Route.MANUAL_DIRECT_REQUIRED,"no fake decentralized route");
        IcePathInspector inspector=new IcePathInspector();
        inspector.setDiscovery("Direct manual P2P");
        inspector.record("candidate:1 1 UDP 2122260223 192.168.1.52 51234 typ host");
        inspector.record("candidate:2 1 udp 123 203.0.113.9 50222 typ srflx raddr 192.168.1.52 rport 51234");
        inspector.record("candidate:3 1 udp 123 2001:db8::7 50800 typ host");
        require(inspector.hasServerReflexiveCandidates(),"STUN observation");
        String summary=inspector.summary();
        require(summary.contains("STUN 1")&&summary.contains("IPv6 candidates: 1"),
            "candidate family counts");
        require(!summary.contains("192.168.")&&!summary.contains("203.0.113")&&
            !summary.contains("2001:db8")&&!summary.contains("candidate:"),
            "never copy actual addresses or raw SDP into reports");
        inspector.setState("FAILED");
        require(inspector.interpretation().contains("No TURN relay is configured"),
            "failure must distinguish missing TURN fallback");
        inspector.recordRemote("candidate:4 1 udp 123 198.51.100.7 50222 typ srflx");
        inspector.setTurnConfigured(true);
        String safe=inspector.summary();
        require(safe.contains("Remote trickle frames: 1")&&
            safe.contains("TURN fallback configured: yes")&&
            !safe.contains("198.51.100.7"),
            "remote ICE report must be sanitized");
        require(inspector.interpretation().contains("TURN connectivity"),
            "failure after configured relay is different");
        System.out.println("PASS: "+passed+" privacy-preserving bridge policy checks");
    }
}
