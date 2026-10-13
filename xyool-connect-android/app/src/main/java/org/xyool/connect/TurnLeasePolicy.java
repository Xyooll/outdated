package org.xyool.connect;

/** Strict provider-independent ICE URL validation with no network requests. */
public final class TurnLeasePolicy {
    private TurnLeasePolicy(){}
    public static boolean validUrl(String value){
        if(value==null||value.length()>320)return false;
        return value.matches("^(stun|stuns|turn|turns):[A-Za-z0-9.-]{1,253}:[0-9]{2,5}(\\?transport=(udp|tcp))?$")
            &&validPort(value);
    }
    private static boolean validPort(String value){
        int start=value.lastIndexOf(':');
        int end=value.indexOf('?',start);
        if(end<0)end=value.length();
        try{
            int port=Integer.parseInt(value.substring(start+1,end));
            return port>0&&port<=65535;
        }catch(NumberFormatException bad){return false;}
    }
}
