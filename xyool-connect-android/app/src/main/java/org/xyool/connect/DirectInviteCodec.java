package org.xyool.connect;

import android.util.Base64;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.nio.charset.StandardCharsets;
import java.util.Locale;
import java.util.zip.GZIPInputStream;
import java.util.zip.GZIPOutputStream;
import org.json.JSONArray;
import org.json.JSONObject;

/**
 * Explicit out-of-band WebRTC signaling: two user-exchanged codes (offer,
 * answer), zero Xyool servers. The codes are unencrypted network metadata;
 * exchange them only with the intended partner over a trusted channel.
 *
 * IMPORTANT: Direct calls do NOT authenticate who controls an Xyool ID.
 * No WebRTC media is routed through this codec.
 */
public final class DirectInviteCodec {
    public static final String PREFIX="XYD1:";
    private static final int MAX_CODE=85000;
    private static final int MAX_JSON=240000;
    private static final String ID="^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$";

    private DirectInviteCodec(){}

    public static String encode(String type,String from,String to,String callId,
            String sdp,JSONArray candidates) throws Exception {
        check(type,from,to,callId,sdp,candidates);
        JSONObject object=new JSONObject();
        object.put("v",1);
        object.put("kind",type);
        object.put("from",from);
        object.put("to",to);
        object.put("call",callId);
        object.put("sdp",sdp);
        object.put("ice",candidates);
        ByteArrayOutputStream compressed=new ByteArrayOutputStream();
        try(GZIPOutputStream zip=new GZIPOutputStream(compressed)){
            zip.write(object.toString().getBytes(StandardCharsets.UTF_8));
        }
        String encoded=PREFIX+Base64.encodeToString(compressed.toByteArray(),
            Base64.NO_WRAP|Base64.URL_SAFE|Base64.NO_PADDING);
        if(encoded.length()>MAX_CODE)throw new IllegalArgumentException("Direct code too large");
        return encoded;
    }

    public static JSONObject decode(String raw) throws Exception {
        if(raw==null)throw new IllegalArgumentException("No direct code supplied");
        String clean=raw.replaceAll("\\s+","");
        if(!clean.startsWith(PREFIX)||clean.length()>MAX_CODE||clean.length()<25)
            throw new IllegalArgumentException("Not a Xyool direct-call code");
        byte[] compressed;
        try{
            compressed=Base64.decode(clean.substring(PREFIX.length()),
                Base64.NO_WRAP|Base64.URL_SAFE);
        }catch(IllegalArgumentException e){throw new IllegalArgumentException("Invalid direct-call encoding");}
        ByteArrayOutputStream plain=new ByteArrayOutputStream();
        try(GZIPInputStream zip=new GZIPInputStream(new ByteArrayInputStream(compressed))){
            byte[] buffer=new byte[4096];int n;
            while((n=zip.read(buffer))!=-1){
                if(plain.size()+n>MAX_JSON)
                    throw new IllegalArgumentException("Direct code exceeds size limit");
                plain.write(buffer,0,n);
            }
        }
        JSONObject data=new JSONObject(plain.toString(StandardCharsets.UTF_8.name()));
        if(data.optInt("v")!=1)throw new IllegalArgumentException("Unsupported Xyool direct format");
        check(data.optString("kind"),data.optString("from"),data.optString("to"),
            data.optString("call"),data.optString("sdp"),data.optJSONArray("ice"));
        return data;
    }

    private static void check(String kind,String from,String to,String call,
            String sdp,JSONArray ice) throws Exception {
        if(!"offer".equals(kind)&&!"answer".equals(kind))
            throw new IllegalArgumentException("Invalid direct call type");
        if(from==null||!from.matches(ID)||to==null||!to.matches(ID)||from.equals(to))
            throw new IllegalArgumentException("Invalid sender or recipient");
        if(call==null||!call.matches("^[a-f0-9]{32}$"))
            throw new IllegalArgumentException("Invalid direct call session");
        if(sdp==null||!sdp.startsWith("v=0")||sdp.length()<80||sdp.length()>40000)
            throw new IllegalArgumentException("Invalid WebRTC invitation");
        if(ice==null||ice.length()>80)
            throw new IllegalArgumentException("Too many network candidates");
        for(int i=0;i<ice.length();i++){
            JSONObject item=ice.getJSONObject(i);
            String line=item.optString("candidate","");
            String mid=item.optString("mid","");
            int index=item.optInt("index",-1);
            if(line.length()<8||line.length()>4000||!line.startsWith("candidate:")||
                mid.length()>50||index<0||index>50)
                throw new IllegalArgumentException("Malformed network candidate");
        }
    }
}
