package org.xyool.connect;

public final class TurnLeasePolicySelfTest {
  private static int passes;
  static void check(String label,String url,boolean expected){
    if(TurnLeasePolicy.validUrl(url)!=expected)throw new AssertionError(label);
    passes++;
  }
  public static void main(String[] args){
    check("stun", "stun:stun.cloudflare.com:3478",true);
    check("udp TURN", "turn:relay.example.com:3478?transport=udp",true);
    check("tcp TURN", "turn:relay.example.com:3478?transport=tcp",true);
    check("TLS TURN", "turns:relay.example.com:5349?transport=tcp",true);
    check("ssl STUN", "stuns:stun.example.com:5349",true);
    check("not HTTPS", "https://relay.example.com:3478",false);
    check("not file", "turn:file:///etc/passwd:3478",false);
    check("invalid port", "turn:relay.example.com:99999",false);
    check("zero port", "turn:relay.example.com:00000",false);
    check("credentials in url", "turn:password@relay.example.com:3478",false);
    check("no route", "turn:relay.example.com",false);
    check("not arbitrary query", "turn:relay.example.com:3478?secret=token",false);
    check("not IPv4 literal with spaces", "turn:192.168. 1.1:3478",false);
    System.out.println("TURN lease URI policy "+passes+"/"+passes+" PASS");
  }
}
