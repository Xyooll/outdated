package org.xyool.connect;

import org.json.JSONArray;
import org.json.JSONObject;
import org.webrtc.PeerConnection;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Short-lived TURN settings supplied over the authenticated Xyool WSS channel.
 * Never persist credentials on disk; never show them in diagnostics.
 * Provider long-lived keys stay on the backend.
 */
public final class TurnLease {
    private final List<PeerConnection.IceServer> iceServers;
    private final long expiresAtMs;
    private TurnLease(List<PeerConnection.IceServer> iceServers,long expiry){
        this.iceServers=Collections.unmodifiableList(iceServers);expiresAtMs=expiry;
    }
    public boolean validAt(long now){return now<expiresAtMs;}
    public List<PeerConnection.IceServer> servers(long now){
        return validAt(now)?iceServers:Collections.emptyList();
    }
    public static TurnLease fromMessage(JSONObject packet,long now){
        if(packet==null||!"turn-credentials".equals(packet.optString("type")))return null;
        int ttl=packet.optInt("ttlSec",0);
        if(ttl<120||ttl>86400)return null;
        JSONArray array=packet.optJSONArray("iceServers");
        if(array==null||array.length()<1||array.length()>8)return null;
        List<PeerConnection.IceServer> result=new ArrayList<>();
        boolean foundRelay=false;
        for(int i=0;i<array.length();i++){
            JSONObject object=array.optJSONObject(i);
            if(object==null)return null;
            JSONArray urls=object.optJSONArray("urls");
            if(urls==null||urls.length()<1||urls.length()>8)return null;
            String username=object.optString("username","");
            String password=object.optString("credential","");
            if(username.length()>256||password.length()>512)return null;
            for(int u=0;u<urls.length();u++){
                String url=urls.optString(u,"");
                if(!TurnLeasePolicy.validUrl(url))return null;
                boolean relay=url.startsWith("turn");
                if(relay&&(username.isEmpty()||password.isEmpty()))return null;
                PeerConnection.IceServer.Builder builder=PeerConnection.IceServer.builder(url);
                if(relay){
                    builder.setUsername(username).setPassword(password);
                    foundRelay=true;
                }
                result.add(builder.createIceServer());
            }
        }
        if(!foundRelay)return null;
        long safetyMs=30000L;
        return new TurnLease(result,now+ttl*1000L-safetyMs);
    }
}
