package org.xyool.connect;

/** Native JVM tests for consent-gated Xyool Network boot recovery. */
public final class NetworkBootPolicySelfTest {
    private static final String ID="XY-ABCD-EFGH-JKLM";
    private static final String TOKEN="0123456789abcdef".repeat(4);
    private static int checks=0;
    private static void expect(boolean actual,boolean expected,String name){
        if(actual!=expected)throw new AssertionError(name);
        checks++;
    }
    public static void main(String[] args){
        expect(NetworkBootPolicy.canRestore(true,ID,TOKEN),true,"enabled valid identity");
        expect(NetworkBootPolicy.canRestore(false,ID,TOKEN),false,"disabled stays off");
        expect(NetworkBootPolicy.canRestore(true,null,TOKEN),false,"missing id");
        expect(NetworkBootPolicy.canRestore(true,"",TOKEN),false,"empty id");
        expect(NetworkBootPolicy.canRestore(true,"XY-IIII-IIII-IIII",TOKEN),false,"invalid alphabet");
        expect(NetworkBootPolicy.canRestore(true,"not-an-id",TOKEN),false,"invalid id");
        expect(NetworkBootPolicy.canRestore(true,ID,null),false,"missing token");
        expect(NetworkBootPolicy.canRestore(true,ID,""),false,"empty token");
        expect(NetworkBootPolicy.canRestore(true,ID,TOKEN.substring(0,63)),false,"short token");
        expect(NetworkBootPolicy.canRestore(true,ID,TOKEN+"a"),false,"long token");
        expect(NetworkBootPolicy.canRestore(true,ID,TOKEN.toUpperCase()),false,"noncanonical token");
        System.out.println("Network boot policy "+checks+"/"+checks+" PASS (Android boot delivery not tested)");
    }
}
