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
        System.out.println("ICE recovery policy "+total+"/"+total+" PASS (network paths not tested)");
    }
}
