package org.xyool.connect;

/** Native-JDK negative tests; executable by CI without Android or network. */
public final class PeerHintSelfTest {
    private static final String A="XY-ABCD-EFGH-JKLM";
    private static final String B="XY-MNPQ-RSTU-VWXY";
    private static final String C="XY-2345-6789-ABCD";
    private static final String FP="0123456789abcdef".repeat(4);
    private static int passed=0;
    private static void expect(boolean actual, boolean wanted, String caseName){
        if(actual!=wanted)throw new AssertionError(caseName);
        passed++;
    }
    public static void main(String[] args){
        expect(PeerHintPolicy.sendable(A,B,C,FP,FP,true),true,"explicit send");
        expect(PeerHintPolicy.sendable(A,B,C,FP,FP,false),false,"no unprompted send");
        expect(PeerHintPolicy.sendable(A,B,C,null,FP,true),false,"recipient not QR verified");
        expect(PeerHintPolicy.sendable(A,B,C,FP,null,true),false,"candidate not QR verified");
        expect(PeerHintPolicy.sendable(A,A,C,FP,FP,true),false,"send to self");
        expect(PeerHintPolicy.sendable(A,B,B,FP,FP,true),false,"suggest recipient");
        expect(PeerHintPolicy.sendable(A,B,A,FP,FP,true),false,"suggest self");
        expect(PeerHintPolicy.sendable(A,B,"192.0.2.1",FP,FP,true),false,"no IP");
        expect(PeerHintPolicy.sendable(A,B,C,"ABCD",FP,true),false,"bad QR fingerprint");
        expect(PeerHintPolicy.receivable(B,A,A,B,C,FP,true,true),true,"validated untrusted hint");
        expect(PeerHintPolicy.receivable(B,A,A,B,C,FP,false,true),false,"receiver opt out");
        expect(PeerHintPolicy.receivable(B,A,A,B,C,FP,true,false),false,"introducer not QR verified");
        expect(PeerHintPolicy.receivable(B,A,C,B,C,FP,true,true),false,"claimed origin mismatch");
        expect(PeerHintPolicy.receivable(B,A,A,C,C,FP,true,true),false,"wrong target");
        expect(PeerHintPolicy.receivable(B,A,A,B,B,FP,true,true),false,"suggest self");
        expect(PeerHintPolicy.receivable(B,A,A,B,A,FP,true,true),false,"suggest origin");
        expect(PeerHintPolicy.receivable(B,A,A,B,C,FP+"ab",true,true),false,"oversized fingerprint");
        expect(PeerHintPolicy.receivable(B,A,A,B,C,"not-a-key",true,true),false,"malformed fingerprint");
        expect(PeerHintPolicy.receivable(B,A,A,B,C,FP,true,true),true,"no implicit trust promotion");
        System.out.println("Peer hint policy "+passed+"/"+passed+" PASS (pure policy only)");
    }
}
