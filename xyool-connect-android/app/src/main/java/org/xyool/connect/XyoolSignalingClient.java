package org.xyool.connect;

import java.net.URI;
import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;
import org.json.JSONObject;

/** Client for Xyool's own ephemeral two-party signaling protocol.
 * A TLS WSS socket carries setup messages; WebRTC carries the media.
 */
public final class XyoolSignalingClient extends WebSocketClient {
    public interface Listener {
        void onReady();
        void onSignal(String type, String sdp);
        void onPeerLeft();
        void onError(String problem);
        void onJoined(int peers);
    }
    private final String room;
    private final Listener listener;
    private volatile boolean shuttingDown=false;

    public XyoolSignalingClient(URI uri,String room,Listener listener) {
        super(uri);
        this.room=room;
        this.listener=listener;
        setConnectionLostTimeout(35);
    }
    @Override public void onOpen(ServerHandshake handshake) {
        try {
            JSONObject payload=new JSONObject();
            payload.put("type","join");
            payload.put("room",room);
            send(payload.toString());
        } catch(Exception ex) {listener.onError("Could not register call.");}
    }
    @Override public void onMessage(String message) {
        if(message.length()>50000)return;
        try {
            JSONObject obj=new JSONObject(message);
            String type=obj.optString("type","");
            switch(type) {
                case "joined": listener.onJoined(obj.optInt("peers",0));break;
                case "peer-ready": listener.onReady();break;
                case "offer":
                case "answer": {
                    String sdp=obj.optString("payload","");
                    if(sdp.length()>80&&sdp.length()<=32000&&sdp.startsWith("v=0"))
                        listener.onSignal(type,sdp);
                    else listener.onError("Server supplied invalid SDP.");
                    break;
                }
                case "peer-left":listener.onPeerLeft();break;
                case "waiting":listener.onJoined(1);break;
                default: break;
            }
        } catch(Exception ex) {
            listener.onError("Signaling data was invalid.");
        }
    }
    @Override public void onClose(int code,String reason,boolean remote) {
        if(!shuttingDown) listener.onError("Signaling server disconnected ("+code+").");
    }
    @Override public void onError(Exception ex) {
        if(!shuttingDown)listener.onError("Couldn't connect to the Xyool signaling server.");
    }
    public void transmit(String type,String sdp) {
        if(!isOpen()){listener.onError("Signaling is not connected.");return;}
        if(!("offer".equals(type)||"answer".equals(type)))return;
        try {
            JSONObject obj=new JSONObject();
            obj.put("type",type);
            obj.put("payload",sdp);
            send(obj.toString());
        }catch(Exception e){listener.onError("Could not send call setup.");}
    }
    public void end() {
        shuttingDown=true;
        close();
    }
}
