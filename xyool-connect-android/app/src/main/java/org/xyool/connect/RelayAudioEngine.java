package org.xyool.connect;

import android.content.Context;
import android.media.AudioFormat;
import android.media.AudioManager;
import android.media.AudioRecord;
import android.media.AudioTrack;
import android.media.MediaRecorder;
import android.os.Process;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.security.KeyFactory;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.MessageDigest;
import java.security.PublicKey;
import java.security.SecureRandom;
import java.security.spec.ECGenParameterSpec;
import java.security.spec.X509EncodedKeySpec;
import java.util.Arrays;
import java.util.Base64;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.atomic.AtomicBoolean;
import javax.crypto.Cipher;
import javax.crypto.KeyAgreement;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;

/**
 * Experimental Xyool WSS audio relay fallback.
 *
 * Uses low-bandwidth mono 8kHz PCM (40ms/640B frames), P-256 ephemeral
 * ECDH and AES-GCM-128. The signaling relay handles ciphertext only;
 * no audio is written to disk. Both devices must be foregrounded.
 *
 * WARNING: ECDH keys are NOT authenticated against the expected person's
 * Xyool ID. A malicious/corrupted signaling endpoint may MITM the initial
 * exchange. TLS protects client-server transport, not peer identity.
 *
 * This is a voice-functionality alpha, NOT a verified E2EE messenger.
 */
public final class RelayAudioEngine {
    public interface Sender {
        void sendEncryptedAudio(byte[] frame);
        void report(String message);
    }
    public static final int FRAME_BYTES = 640;
    public static final int MAX_CIPHERTEXT_BYTES = 768;
    private static final int SAMPLE_RATE = 8000;
    private static final int FRAME_INTERVAL_MS = 40;
    private static final byte VERSION = 1;
    private static final byte[] AAD =
        "XYOOL-WSS-AUDIO-v1".getBytes(StandardCharsets.UTF_8);

    private final Context context;
    private final Sender sender;
    private final SecureRandom secureRandom = new SecureRandom();
    private final KeyPair keyPair;
    private final byte[] localPublic;
    private final ArrayBlockingQueue<byte[]> playback = new ArrayBlockingQueue<>(30);
    private volatile SecretKeySpec aesKey;
    private final AtomicBoolean running = new AtomicBoolean(false);
    private AudioRecord recorder;
    private AudioTrack player;
    private Thread captureThread;
    private Thread playbackThread;

    public RelayAudioEngine(Context context,Sender sender) throws Exception {
        this.context=context.getApplicationContext();
        this.sender=sender;
        KeyPairGenerator gen=KeyPairGenerator.getInstance("EC");
        gen.initialize(new ECGenParameterSpec("secp256r1"),secureRandom);
        keyPair=gen.generateKeyPair();
        localPublic=keyPair.getPublic().getEncoded();
    }
    public String getPublicKey(){
        return Base64.getEncoder().encodeToString(localPublic);
    }
    public boolean hasKey(){return aesKey!=null;}
    public synchronized void receivePeerKey(String encoded) throws Exception {
        if(aesKey!=null)return;
        if(encoded==null||encoded.length()<75||encoded.length()>512)
            throw new IllegalArgumentException("Invalid relay key size");
        byte[] peer=Base64.getDecoder().decode(encoded);
        if(peer.length<80||peer.length>300||Arrays.equals(peer,localPublic))
            throw new IllegalArgumentException("Invalid peer public key");
        PublicKey publicKey=KeyFactory.getInstance("EC")
            .generatePublic(new X509EncodedKeySpec(peer));
        KeyAgreement agreement=KeyAgreement.getInstance("ECDH");
        agreement.init(keyPair.getPrivate());
        agreement.doPhase(publicKey,true);
        byte[] secret=agreement.generateSecret();
        // Sort both encoded public keys lexicographically so both clients
        // independently derive the identical key.
        byte[] first=localPublic, second=peer;
        if(compare(first,second)>0){first=peer;second=localPublic;}
        MessageDigest hash=MessageDigest.getInstance("SHA-256");
        hash.update(AAD);hash.update(first);hash.update(second);hash.update(secret);
        byte[] digest=hash.digest();
        aesKey=new SecretKeySpec(Arrays.copyOf(digest,16),"AES");
        Arrays.fill(secret,(byte)0);
        Arrays.fill(digest,(byte)0);
    }
    private static int compare(byte[] a,byte[] b){
        int n=Math.min(a.length,b.length);
        for(int i=0;i<n;i++){
            int v=(a[i]&255)-(b[i]&255);
            if(v!=0)return v;
        }
        return a.length-b.length;
    }
    private byte[] encrypt(byte[] pcm) throws Exception {
        SecretKeySpec key=aesKey;
        if(key==null)throw new IllegalStateException("No shared relay key");
        byte[] nonce=new byte[12];
        secureRandom.nextBytes(nonce);
        Cipher cipher=Cipher.getInstance("AES/GCM/NoPadding");
        cipher.init(Cipher.ENCRYPT_MODE,key,new GCMParameterSpec(128,nonce));
        cipher.updateAAD(AAD);
        byte[] ciphertext=cipher.doFinal(pcm);
        ByteBuffer packet=ByteBuffer.allocate(1+nonce.length+ciphertext.length);
        packet.put(VERSION).put(nonce).put(ciphertext);
        return packet.array();
    }
    private byte[] decrypt(byte[] packet) throws Exception {
        SecretKeySpec key=aesKey;
        if(key==null||packet.length<30||packet.length>MAX_CIPHERTEXT_BYTES||
            packet[0]!=VERSION)return null;
        Cipher cipher=Cipher.getInstance("AES/GCM/NoPadding");
        cipher.init(Cipher.DECRYPT_MODE,key,new GCMParameterSpec(128,packet,1,12));
        cipher.updateAAD(AAD);
        byte[] pcm=cipher.doFinal(packet,13,packet.length-13);
        return pcm.length==FRAME_BYTES?pcm:null;
    }
    public void receiveAudio(byte[] packet) {
        if(!running.get())return;
        try{
            byte[] decoded=decrypt(packet);
            if(decoded==null)return;
            if(!playback.offer(decoded)){
                playback.poll();
                playback.offer(decoded);
            }
        }catch(Exception e){
            // Do not play packets which fail AES-GCM authentication.
        }
    }

    public synchronized boolean start() {
        if(running.get())return true;
        if(aesKey==null)return false;
        int minIn=AudioRecord.getMinBufferSize(SAMPLE_RATE,
            AudioFormat.CHANNEL_IN_MONO,AudioFormat.ENCODING_PCM_16BIT);
        int minOut=AudioTrack.getMinBufferSize(SAMPLE_RATE,
            AudioFormat.CHANNEL_OUT_MONO,AudioFormat.ENCODING_PCM_16BIT);
        if(minIn<=0||minOut<=0){
            sender.report("This phone cannot start the 8kHz audio relay");
            return false;
        }
        try{
            recorder=new AudioRecord(MediaRecorder.AudioSource.VOICE_COMMUNICATION,
                SAMPLE_RATE,AudioFormat.CHANNEL_IN_MONO,
                AudioFormat.ENCODING_PCM_16BIT,Math.max(minIn,FRAME_BYTES*8));
            player=new AudioTrack(AudioManager.STREAM_VOICE_CALL,SAMPLE_RATE,
                AudioFormat.CHANNEL_OUT_MONO,AudioFormat.ENCODING_PCM_16BIT,
                Math.max(minOut,FRAME_BYTES*12),AudioTrack.MODE_STREAM);
            if(recorder.getState()!=AudioRecord.STATE_INITIALIZED ||
                player.getState()!=AudioTrack.STATE_INITIALIZED)
                throw new IllegalStateException("Audio hardware initialization failed");
            recorder.startRecording();
            player.play();
            running.set(true);
            captureThread=new Thread(this::recordLoop,"Xyool-Relay-Capture");
            playbackThread=new Thread(this::playLoop,"Xyool-Relay-Playback");
            captureThread.start();playbackThread.start();
            return true;
        }catch(Exception e){
            sender.report("Relay audio start failed: "+e.getClass().getSimpleName());
            stop();
            return false;
        }
    }

    private void recordLoop(){
        Process.setThreadPriority(Process.THREAD_PRIORITY_AUDIO);
        final byte[] frame=new byte[FRAME_BYTES];
        while(running.get()){
            int total=0;
            while(total<frame.length && running.get()){
                int count;
                try{
                    count=recorder.read(frame,total,frame.length-total,AudioRecord.READ_BLOCKING);
                }catch(Exception e){count=-1;}
                if(count<=0){running.set(false);break;}
                total+=count;
            }
            if(!running.get())break;
            try{sender.sendEncryptedAudio(encrypt(frame));}
            catch(Exception e){
                if(running.get())sender.report("Relay audio transmission failed");
                break;
            }
        }
    }
    private void playLoop(){
        Process.setThreadPriority(Process.THREAD_PRIORITY_AUDIO);
        while(running.get()){
            try{
                byte[] decoded=playback.take();
                if(!running.get())break;
                int i=0;
                while(i<decoded.length && running.get()){
                    int sent=player.write(decoded,i,decoded.length-i,AudioTrack.WRITE_BLOCKING);
                    if(sent<=0)break;
                    i+=sent;
                }
            }catch(InterruptedException ex){break;}
            catch(Exception ex){break;}
        }
    }
    public synchronized void stop(){
        running.set(false);
        if(captureThread!=null)captureThread.interrupt();
        if(playbackThread!=null)playbackThread.interrupt();
        // Stop recording first to wake any blocking read.
        try{if(recorder!=null)recorder.stop();}catch(Exception ignored){}
        try{if(player!=null)player.pause();}catch(Exception ignored){}
        try{if(player!=null)player.flush();}catch(Exception ignored){}
        if(recorder!=null){try{recorder.release();}catch(Exception ignored){}recorder=null;}
        if(player!=null){try{player.release();}catch(Exception ignored){}player=null;}
        captureThread=null;playbackThread=null;
        playback.clear();
    }
}
