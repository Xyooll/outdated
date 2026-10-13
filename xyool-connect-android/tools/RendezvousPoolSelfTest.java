package org.xyool.connect;

public final class RendezvousPoolSelfTest {
    private static void ok(boolean b,String message){
        if(!b)throw new AssertionError(message);
    }
    private static void invalid(String primary,String more){
        try{new RendezvousPool(primary,more);}
        catch(IllegalArgumentException expected){return;}
        throw new AssertionError("Accepted unsafe bootstrap: "+primary);
    }
    public static void main(String[] args){
        final String first="wss://node-one.example/v1/id";
        final String second="wss://node-two.example/v1/id";
        RendezvousPool nodes=new RendezvousPool(first,second+","+first);
        ok(nodes.count()==2,"deduplicates nodes");
        ok(nodes.current().toString().equals(first),"preferred first");
        ok(nodes.failover().toString().equals(second),"failed peer rotated");
        ok(nodes.failover().toString().equals(first),"wraps");
        nodes.failover(); nodes.reset();
        ok(nodes.current().toString().equals(first),"resets");
        invalid("ws://node.example/v1/id","");
        invalid("wss://alice:password@node.example/v1/id","");
        invalid("wss://node.example/private","");
        invalid("wss://node.example/v1/id?token=oops","");
        invalid(first,"ws://node.example/v1/id");
        invalid(first,"wss://a.example/v1/id,wss://b.example/v1/id,wss://c.example/v1/id,wss://d.example/v1/id,wss://e.example/v1/id");
        ok(new RendezvousPool("",null).count()==1,"default node");
        System.out.println("RendezvousPoolSelfTest passed");
    }
}
