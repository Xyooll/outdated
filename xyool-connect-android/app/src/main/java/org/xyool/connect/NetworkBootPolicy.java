package org.xyool.connect;

/** Android-independent policy for restoring an explicitly enabled phone node. */
public final class NetworkBootPolicy {
    private NetworkBootPolicy(){}

    private static final String ID="^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$";
    private static final String TOKEN="^[0-9a-f]{64}$";

    public static boolean canRestore(boolean enabled,String id,String token){
        return enabled && id!=null && id.matches(ID) &&
            token!=null && token.matches(TOKEN);
    }
}
