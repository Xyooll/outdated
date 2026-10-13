package org.xyool.connect;

import android.content.Context;
import android.content.SharedPreferences;
import android.security.keystore.KeyGenParameterSpec;
import android.security.keystore.KeyProperties;
import android.util.Base64;
import java.security.KeyFactory;
import java.security.KeyPairGenerator;
import java.security.KeyStore;
import java.security.MessageDigest;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.SecureRandom;
import java.security.Signature;
import java.security.spec.ECGenParameterSpec;
import java.security.spec.X509EncodedKeySpec;
import java.nio.charset.StandardCharsets;
import org.json.JSONObject;

/**
 * Permanent, nonexportable, Android-keystore P-256 device identity.
 * Authenticates nearby signaling peers; first contact is TOFU unless the
 * peer's 64-character SHA-256 public key fingerprint was scanned from QR.
 * Does NOT authenticate legacy central rendezvous, global peers, or WebRTC
 * SDP outside the signed local protocol. Never claim E2EE identity globally.
 */
public final class PhoneIdentity {
    private static final String ALIAS="xyool-lan-node-identity-p256-v1";
    private static final String STORE="xyool_private";
    private static final String PIN_PREFIX="xyool_verified_lan_peer_";
    private PhoneIdentity(){}

    private static synchronized KeyStore store()throws Exception{
        KeyStore k=KeyStore.getInstance("AndroidKeyStore");
        k.load(null);
        if(!k.containsAlias(ALIAS)){
            KeyPairGenerator generator=KeyPairGenerator.getInstance(
                KeyProperties.KEY_ALGORITHM_EC,"AndroidKeyStore");
            generator.initialize(new KeyGenParameterSpec.Builder(ALIAS,
                KeyProperties.PURPOSE_SIGN | KeyProperties.PURPOSE_VERIFY)
                .setAlgorithmParameterSpec(new ECGenParameterSpec("secp256r1"))
                .setDigests(KeyProperties.DIGEST_SHA256)
                .build());
            generator.generateKeyPair();
        }
        return k;
    }
    public static String publicKey()throws Exception{
        byte[] encoded=store().getCertificate(ALIAS).getPublicKey().getEncoded();
        return Base64.encodeToString(encoded,Base64.NO_WRAP);
    }
    public static String fingerprint()throws Exception{
        return fingerprintFor(publicKey());
    }
    public static String fingerprintFor(String key)throws Exception{
        byte[] encoded=Base64.decode(key,Base64.NO_WRAP);
        if(encoded.length<80||encoded.length>160)throw new IllegalArgumentException("Bad public key size");
        byte[] digest=MessageDigest.getInstance("SHA-256").digest(encoded);
        StringBuilder hex=new StringBuilder(64);
        for(byte b:digest)hex.append(String.format(java.util.Locale.US,"%02x",b&255));
        return hex.toString();
    }
    public static String sign(String message)throws Exception{
        KeyStore.PrivateKeyEntry entry=(KeyStore.PrivateKeyEntry)store().getEntry(ALIAS,null);
        Signature sig=Signature.getInstance("SHA256withECDSA");
        sig.initSign(entry.getPrivateKey());
        sig.update(message.getBytes(StandardCharsets.UTF_8));
        return Base64.encodeToString(sig.sign(),Base64.NO_WRAP);
    }
    public static boolean verify(String key,String signature,String message){
        try{
            if(key==null||signature==null||key.length()>280||signature.length()>220)
                return false;
            byte[] pub=Base64.decode(key,Base64.NO_WRAP);
            PublicKey p=KeyFactory.getInstance("EC").generatePublic(
                new X509EncodedKeySpec(pub));
            if(!(p instanceof java.security.interfaces.ECPublicKey)||
                ((java.security.interfaces.ECPublicKey)p).getParams().getCurve()
                    .getField().getFieldSize()!=256)return false;
            Signature v=Signature.getInstance("SHA256withECDSA");
            v.initVerify(p);
            v.update(message.getBytes(StandardCharsets.UTF_8));
            return v.verify(Base64.decode(signature,Base64.NO_WRAP));
        }catch(Exception bad){return false;}
    }
    public static boolean pinOrVerify(Context context,String remoteId,String publicKey){
        try{
            String fingerprint=fingerprintFor(publicKey);
            String key=PIN_PREFIX+remoteId;
            SharedPreferences pref=context.getSharedPreferences(STORE,Context.MODE_PRIVATE);
            String pinned=pref.getString(key,null);
            if(pinned==null){
                pref.edit().putString(key,fingerprint).apply();
                return true;
            }
            return MessageDigest.isEqual(pinned.getBytes(StandardCharsets.US_ASCII),
                fingerprint.getBytes(StandardCharsets.US_ASCII));
        }catch(Exception bad){return false;}
    }
    public static void pinFromQr(Context context,String remoteId,String fingerprint){
        if(remoteId==null||!remoteId.matches("^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$")||
           fingerprint==null||!fingerprint.matches("^[a-f0-9]{64}$"))
            throw new IllegalArgumentException("Invalid identity fingerprint");
        // Keep QR provenance separate from first-contact/TOFU pins. Older
        // stored fingerprints are NOT automatically treated as QR verified.
        context.getSharedPreferences(STORE,Context.MODE_PRIVATE).edit()
            .putString(PIN_PREFIX+remoteId,fingerprint)
            .putString("xyool_qr_verified_"+remoteId,fingerprint).apply();
    }
    public static String pinnedFingerprint(Context context,String id){
        if(id==null)return null;
        return context.getSharedPreferences(STORE,Context.MODE_PRIVATE)
            .getString(PIN_PREFIX+id,null);
    }
    /** Only a key explicitly scanned from QR qualifies as identity-verified. */
    public static String qrVerifiedFingerprint(Context context,String id){
        String pin=pinnedFingerprint(context,id);
        if(pin==null)return null;
        String verified=context.getSharedPreferences(STORE,Context.MODE_PRIVATE)
            .getString("xyool_qr_verified_"+id,null);
        return pin.equals(verified)?pin:null;
    }
    public static String meshEnableProof(String id,long when){
        return "xyool-peer-enable-v1|"+canonicalFields(id,Long.toString(when));
    }
    public static String meshSignalProof(String from,String to,String kind,long when,
        String sdp,String candidate,String mid,int index){
        return "xyool-peer-signal-v1|"+canonicalFields(from,to,kind,
            Long.toString(when),sdp,candidate,mid,Integer.toString(index));
    }
    private static String canonicalFields(String... values){
        StringBuilder output=new StringBuilder();
        for(String value:values)field(output,value);
        return output.toString();
    }
    public static String newNonce(){
        byte[] b=new byte[16];new SecureRandom().nextBytes(b);
        StringBuilder text=new StringBuilder(32);
        for(byte octet:b)text.append(String.format(java.util.Locale.US,"%02x",octet&255));
        return text.toString();
    }
    public static String callProof(String from,String to,long ts,String nonce){
        return "xyool-lan-v2|call|"+from+"|"+to+"|"+ts+"|"+nonce;
    }
    public static String packetProof(String sender,String nonce,int seq,JSONObject packet){
        StringBuilder s=new StringBuilder("xyool-lan-v2|frame|");
        field(s,sender);field(s,nonce);field(s,Long.toString(seq));
        for(String key:new String[]{"type","kind","sdp","candidate","mid","index","reason"})
            field(s,packet.optString(key,""));
        return s.toString();
    }
    private static void field(StringBuilder out,String value){
        out.append(value.length()).append(':').append(value);
    }
}
