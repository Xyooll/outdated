package org.xyool.connect;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.util.Log;

/**
 * Re-establish the user-enabled reachability service after a normal boot,
 * once credential-encrypted preferences are available. Android still decides
 * whether a foreground service may start; no stealth restart/force-stop bypass.
 */
public final class NetworkBootReceiver extends BroadcastReceiver {
    private static final String TAG="XyoolNetworkBoot";
    @Override public void onReceive(Context context,Intent intent){
        if(intent==null ||
            !Intent.ACTION_BOOT_COMPLETED.equals(intent.getAction()))return;
        SharedPreferences prefs=context.getSharedPreferences("xyool_private",Context.MODE_PRIVATE);
        if(!NetworkBootPolicy.canRestore(
            prefs.getBoolean(CallReachabilityService.PREF_ENABLED,false),
            prefs.getString("xyool_id",""),prefs.getString("xyool_auth","")))return;
        try{
            context.startForegroundService(new Intent(context,CallReachabilityService.class)
                .setAction(CallReachabilityService.ACTION_ENABLE));
        }catch(RuntimeException restricted){
            // Some Android/OEM configurations prohibit starting after reboot.
            // Preserve consent; recover on the user's next explicit app open.
            Log.w(TAG,"Background service restart was restricted",restricted);
        }
    }
}
