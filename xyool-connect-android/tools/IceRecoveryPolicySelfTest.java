package org.xyool.connect;

/** Native JVM policy tests. These do not simulate NAT or Android ICE media. */
public final class IceRecoveryPolicySelfTest {
    private static int total=0;
    private static void test(String name,boolean actual,boolean expected){
        if(actual!=expected)throw new AssertionError(name);
        total++;
    }
    public static void main(String[] args){
        test("caller live stable retry",IceRecoveryPolicy.mayRestart(true,true,true,true,true,0),true);
        test("callee may not offer",IceRecoveryPolicy.mayRestart(false,true,true,true,true,0),false);
        test("hungup may not restart",IceRecoveryPolicy.mayRestart(true,false,true,true,true,0),false);
        test("not accepted may not restart",IceRecoveryPolicy.mayRestart(true,true,false,true,true,0),false);
        test("without answer may not restart",IceRecoveryPolicy.mayRestart(true,true,true,false,true,0),false);
        test("unstable signaling may not restart",IceRecoveryPolicy.mayRestart(true,true,true,true,false,0),false);
        test("no infinite retries",IceRecoveryPolicy.mayRestart(true,true,true,true,true,1),false);
        test("over budget",IceRecoveryPolicy.mayRestart(true,true,true,true,true,10),false);
        test("invalid negative attempts",IceRecoveryPolicy.mayRestart(true,true,true,true,true,-1),false);
        if(!IceRecoveryPolicy.reason(false,true,true,true,true,0)
            .contains("Receiving phone"))throw new AssertionError("receiver reason");
        total++;
        if(!IceRecoveryPolicy.reason(true,true,true,false,true,0)
            .contains("remote SDP answer"))throw new AssertionError("missing remote answer");
        total++;
        if(!IceRecoveryPolicy.reason(true,true,true,true,false,0)
            .contains("not stable"))throw new AssertionError("unstable reason");
        total++;
        if(!IceRecoveryPolicy.reason(true,true,true,true,true,1)
            .contains("budget exhausted"))throw new AssertionError("budget reason");
        total++;
        if(!IceRecoveryPolicy.connectedOutcome(0)
            .equals("ICE connected without a restart"))
            throw new AssertionError("initial direct ICE report");
        total++;
        if(!IceRecoveryPolicy.connectedOutcome(1)
            .equals("ICE connected after automatic restart"))
            throw new AssertionError("recovered ICE must supersede pending negotiation");
        total++;
        test("long CHECKING must be watched",
            IceRecoveryPolicy.shouldWatchChecking("CHECKING",true,false),true);
        test("recovered ICE cannot timeout",
            IceRecoveryPolicy.shouldWatchChecking("COMPLETED",true,true),false);
        test("disconnected state uses separate recovery",
            IceRecoveryPolicy.shouldWatchChecking("DISCONNECTED",true,false),false);
        test("ended call cannot timeout",
            IceRecoveryPolicy.shouldWatchChecking("CHECKING",false,false),false);
        test("connected state cannot timeout",
            IceRecoveryPolicy.shouldWatchChecking("CHECKING",true,true),false);
        if(IceRecoveryPolicy.CHECKING_TIMEOUT_MS!=30000L ||
            IceRecoveryPolicy.RESTART_OUTCOME_TIMEOUT_MS!=30000L)
            throw new AssertionError("Bounded ICE watchdog timings");
        total++;
        System.out.println("ICE recovery policy "+total+"/"+total+" PASS (network paths not tested)");
    }
}
