package org.xyool.connect;

/**
 * A BitTorrent-inspired peer introduction is an UNTRUSTED hint, never a contact,
 * transport credential, authorization, or command to connect. Pure policy code
 * is kept Android-free for independent JDK regression checks.
 */
public final class PeerHintPolicy {
    private PeerHintPolicy(){}
    private static final String ID="^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$";
    private static final String FP="^[0-9a-f]{64}$";
    public static boolean validId(String id){return id!=null&&id.matches(ID);}
    public static boolean validFingerprint(String fp){return fp!=null&&fp.matches(FP);}
    public static boolean sendable(String self,String receiver,String suggestion,
            String receiverQrPin,String suggestionQrPin,boolean explicitUserAction) {
        return explicitUserAction && validId(self) && validId(receiver) &&
            validId(suggestion) && !receiver.equals(self) && !suggestion.equals(self) &&
            !suggestion.equals(receiver) && validFingerprint(receiverQrPin) &&
            validFingerprint(suggestionQrPin);
    }
    public static boolean receivable(String self,String linkedPeer,String signedOrigin,
            String target,String subject,String subjectFingerprint,
            boolean locallyEnabled,boolean introducerQrVerified) {
        return locallyEnabled && introducerQrVerified &&
            validId(self) && validId(linkedPeer) && validId(signedOrigin) &&
            validId(target) && validId(subject) && validFingerprint(subjectFingerprint) &&
            self.equals(target) && linkedPeer.equals(signedOrigin) &&
            !subject.equals(self) && !subject.equals(linkedPeer);
    }
}
