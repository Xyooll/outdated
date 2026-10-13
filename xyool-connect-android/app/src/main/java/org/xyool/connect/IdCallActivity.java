package org.xyool.connect;

import android.Manifest;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.ActivityNotFoundException;
import android.content.ClipData;
import android.content.ClipboardManager;
import android.content.Context;
import android.content.ComponentName;
import android.content.ServiceConnection;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.graphics.drawable.GradientDrawable;
import android.graphics.Bitmap;
import android.graphics.Color;
import android.widget.ImageView;
import android.widget.Toast;
import com.google.zxing.BarcodeFormat;
import com.google.zxing.EncodeHintType;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.common.BitMatrix;
import java.util.EnumMap;
import java.util.Map;
import android.media.Ringtone;
import android.media.RingtoneManager;
import android.os.Bundle;
import android.os.Build;
import android.os.IBinder;
import android.text.InputType;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import java.security.SecureRandom;
import java.util.List;
import java.util.Locale;
import org.json.JSONObject;

/** Xyool's simplified ID-to-ID calling alpha.
 * Open both phones, share ID, enter ID, tap Call, Accept or Decline.
 * The user never exchanges SDP/ICE setup strings.
 *
 * This requires a separately hosted WSS Xyool signaling service; it is not
 * usable as an always-online phone service until a real endpoint exists.
 */
public final class IdCallActivity extends Activity {
    private static final int BG=0xff0c1822, PANEL=0xff192f3b, FG=0xfff1faf7,
        MUTED=0xffaec8cf, ACCENT=0xff68dbc3, ERROR=0xffffb9a7;
    private static final String ALPHABET="ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
    private static final int MIC_REQUEST=481;
    private static final String DEFAULT_SERVER="wss://xyool-id-signaling-production.up.railway.app/v1/id";
    // Public STUN gives WebRTC public/translated ICE candidates when on separate networks.
    // This is used ONLY for internet calls. Enter "off" in Advanced to disable it.
    // Cloudflare receives source IP and basic binding metadata, not call audio.
    private static final String DEFAULT_STUN="stun:stun.cloudflare.com:3478";
    private SharedPreferences prefs;
    private SavedContacts savedContacts;
    private String id, token;
    private TextView stateLabel;
    private EditText targetInput;
    private LinearLayout body, contactsList;
    private CallReachabilityService cloud;
    private boolean cloudBound;
    private boolean autoAnswerRequested;
    private Button reachabilityButton;
    private final ServiceConnection cloudLink=new ServiceConnection(){
        @Override public void onServiceConnected(ComponentName name,IBinder binder){
            cloud=((CallReachabilityService.LocalBinder)binder).service();
            cloud.setListener(new CallReachabilityService.Listener(){
                @Override public void onPacket(JSONObject message){received(message,false);}
                @Override public void onLocalPacket(JSONObject message){received(message,true);}
                @Override public void onConnection(boolean online,String explanation){
                    registered=online;
                    if(!disposed&&(cloud==null||!cloud.hasVoiceSession()))connectionStatus();
                }
                @Override public void onVoiceStatus(String message){
                    if(!disposed)status(message);
                }
            });
            if(autoAnswerRequested){
                // A previously expired notification must not auto-answer the next call.
                if(!cloud.hasIncoming()){
                    autoAnswerRequested=false;
                    status("That incoming call is no longer available.");
                }
            }
        }
        @Override public void onServiceDisconnected(ComponentName name){
            cloud=null;registered=false;
            if(!disposed)connectionStatus();
        }
    };
    private boolean registered,disposed;
    private AlertDialog incomingAlert;
    private Ringtone incomingRingtone;
    private Runnable pendingMicrophone;
    private String callStatus="Checking Xyool calling service…";

    private String bridgeMode(){
        return BridgePolicy.sanitize(prefs.getString(BridgePolicy.PREF_MODE,BridgePolicy.HYBRID));
    }
    @Override public void onCreate(Bundle b){
        super.onCreate(b);
        prefs=getSharedPreferences("xyool_private",MODE_PRIVATE);
        savedContacts=new SavedContacts(this);
        autoAnswerRequested=CallReachabilityService.ACTION_ANSWER.equals(getIntent().getAction());
        id=prefs.getString("xyool_id","");
        token=prefs.getString("xyool_auth","");
        if(!id.matches("^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$")||
            !token.matches("^[0-9a-f]{64}$")){
            makeIdentity();
        }
        getWindow().setStatusBarColor(BG);
        getWindow().setNavigationBarColor(BG);
        render();
        if(hasReachability())connect();
    }
    @Override protected void onNewIntent(Intent intent){
        super.onNewIntent(intent);
        setIntent(intent);
        if(CallReachabilityService.ACTION_ANSWER.equals(intent.getAction())){
            autoAnswerRequested=true;
            if(cloud!=null&&cloud.hasIncomingVoice()){
                autoAnswerRequested=false;
                acceptIncomingCall();
            }
        }
    }
    @Override protected void onResume(){
        super.onResume();
        // Explicitly enabled nodes recover if Android stopped the foreground
        // service while the UI was closed. Never auto-enable a disabled node.
        if(hasReachability() && NetworkBootPolicy.canRestore(true,id,token)){
            try{
                startForegroundService(new Intent(this,CallReachabilityService.class)
                    .setAction(CallReachabilityService.ACTION_ENABLE));
            }catch(RuntimeException restricted){
                status("Xyool Network restart blocked by Android. Check notification and battery settings.");
            }
        }
        updateReachabilityButton();
        if(prefs!=null && !cloudBound && hasReachability())connect();
    }
    @Override protected void onStop(){
        // The foreground service owns WebRTC media. Detach the visible screen
        // but do not hang up when Home is pressed or the app is backgrounded.
        stopIncomingRing();
        disconnect();
        super.onStop();
    }
    private void makeIdentity(){
        SecureRandom random=new SecureRandom();
        StringBuilder letters=new StringBuilder();
        for(int i=0;i<12;i++)letters.append(ALPHABET.charAt(random.nextInt(ALPHABET.length())));
        id="XY-"+letters.substring(0,4)+"-"+letters.substring(4,8)+"-"+letters.substring(8);
        byte[] secret=new byte[32];random.nextBytes(secret);
        StringBuilder hex=new StringBuilder(64);
        for(byte b:secret)hex.append(String.format(Locale.US,"%02x",b&0xff));
        token=hex.toString();
        prefs.edit().putString("xyool_id",id).putString("xyool_auth",token).apply();
    }
    private int dp(int n){return (int)(n*getResources().getDisplayMetrics().density+.5f);}
    private LinearLayout column(){LinearLayout l=new LinearLayout(this);l.setOrientation(1);return l;}
    private TextView text(String v,int size,int color,boolean bold){
        TextView t=new TextView(this);t.setText(v);t.setTextSize(size);t.setTextColor(color);
        if(bold)t.setTypeface(null,1);
        return t;
    }
    private GradientDrawable background(int c){
        GradientDrawable g=new GradientDrawable();g.setColor(c);g.setCornerRadius(dp(14));
        g.setStroke(dp(1),0xff365968);return g;
    }
    private void space(LinearLayout l,int n){l.addView(new View(this),new LinearLayout.LayoutParams(dp(1),dp(n)));}
    private LinearLayout panel(){
        LinearLayout l=column();l.setPadding(dp(15),dp(15),dp(15),dp(15));
        l.setBackground(background(PANEL));
        LinearLayout.LayoutParams lp=new LinearLayout.LayoutParams(-1,-2);lp.bottomMargin=dp(13);
        body.addView(l,lp);return l;
    }
    private Button button(LinearLayout parent,String label,boolean primary,View.OnClickListener action){
        Button b=new Button(this);b.setAllCaps(false);b.setText(label);b.setTextSize(15);
        b.setTextColor(primary?BG:FG);b.setBackground(background(primary?ACCENT:0xff294d59));
        b.setOnClickListener(action);parent.addView(b,new LinearLayout.LayoutParams(-1,dp(48)));return b;
    }
    private EditText input(LinearLayout parent,String hint,String value){
        EditText e=new EditText(this);e.setSingleLine(true);
        e.setTextSize(16);e.setTextColor(FG);e.setHintTextColor(0xff91adb6);e.setHint(hint);
        e.setInputType(InputType.TYPE_CLASS_TEXT);
        e.setPadding(dp(12),dp(12),dp(12),dp(12));e.setBackground(background(0xff0e2532));
        if(value!=null)e.setText(value);
        parent.addView(e,new LinearLayout.LayoutParams(-1,-2));
        return e;
    }
    // Calling-first single-screen UI. Debug and relay controls remain in Settings.
    private void render(){
        LinearLayout root=column();
        root.setBackgroundColor(BG);
        ScrollView scroll=new ScrollView(this);
        scroll.setFillViewport(false);
        body=column();
        body.setPadding(dp(16),dp(18),dp(16),dp(28));
        scroll.addView(body);
        root.addView(scroll,new LinearLayout.LayoutParams(-1,0,1f));
        setContentView(root);

        body.addView(text("XYOOL CONNECT",14,ACCENT,true));
        space(body,3);
        body.addView(text("Call by Xyool ID",26,FG,true));
        space(body,10);

        LinearLayout net=panel();
        net.addView(text("NETWORK",12,MUTED,true));
        space(net,4);
        stateLabel=text(callStatus,14,FG,false);
        net.addView(stateLabel);
        space(net,9);
        reachabilityButton=button(net,"Xyool Network: OFF",true,v->toggleReachability());
        updateReachabilityButton();
        space(net,7);
        net.addView(text("Turn ON to receive calls by ID, including while this screen is closed. Internet registration uses a signaling service; Android may interrupt background access.",12,MUTED,false));
        space(net,6);
        button(net,"Copy call diagnostics",false,v->{
            if(cloud==null){
                status("Network service unavailable. Turn on Xyool Network.");return;
            }
            String report=cloud.voiceDiagnostics();
            ClipboardManager cb=(ClipboardManager)getSystemService(Context.CLIPBOARD_SERVICE);
            if(cb!=null){
                cb.setPrimaryClip(ClipData.newPlainText("Xyool voice ICE report",report));
                status("Sanitized call diagnostics copied. Paste into ChatGPT for troubleshooting.");
            }
        });

        LinearLayout self=panel();
        self.addView(text("YOUR ID",12,MUTED,true));
        space(self,7);
        TextView address=text(id,21,ACCENT,true);
        address.setTextIsSelectable(true);
        address.setGravity(Gravity.CENTER_HORIZONTAL);
        self.addView(address);
        space(self,8);
        button(self,"Copy my ID",false,v->{
            ClipboardManager clip=(ClipboardManager)getSystemService(Context.CLIPBOARD_SERVICE);
            if(clip!=null)clip.setPrimaryClip(ClipData.newPlainText("Xyool ID",id));
            status("ID copied.");
        });
        space(self,6);
        button(self,"Show my QR code",false,v->showMyQr());
        space(self,6);
        button(self,"Share my ID",false,v->{
            Intent send=new Intent(Intent.ACTION_SEND);
            send.setType("text/plain");
            send.putExtra(Intent.EXTRA_TEXT,"Call me on Xyool Connect: "+id);
            try{startActivity(Intent.createChooser(send,"Share Xyool ID"));}
            catch(ActivityNotFoundException ex){status("No sharing app found.");}
        });

        LinearLayout dial=panel();
        dial.addView(text("CALL SOMEONE",12,MUTED,true));
        space(dial,7);
        targetInput=input(dial,"Xyool ID",null);
        space(dial,7);
        button(dial,"Scan their QR code",false,v->scanIdQr());
        space(dial,6);
        button(dial,"Save entered ID",false,v->saveEnteredContact());
        space(dial,11);
        button(dial,"Call",true,v->call());
        space(dial,6);
        button(dial,"Hang up",false,v->hangup());
        space(dial,6);
        button(dial,"Mute / Unmute",false,v->toggleMute());
        space(dial,6);
        button(dial,"Speaker / Earpiece",false,v->{
            if(cloud==null)status("Xyool Network service unavailable.");
            else cloud.speakerVoice();
        });

        LinearLayout contacts=panel();
        contacts.addView(text("SAVED CONTACTS",12,MUTED,true));
        space(contacts,7);
        contacts.addView(text("Scan a QR code once, or save an ID manually. Tap a saved contact to call. Unverified IDs stay labeled unverified.",12,MUTED,false));
        space(contacts,5);
        contactsList=column();
        contacts.addView(contactsList);
        showSavedContacts();

        space(body,7);
        body.addView(text("Test build • Network reachability depends on Android and connectivity. Not for emergency calls.",12,MUTED,false));
    }

    private void showMyQr(){
        try{
            // QR carries public Xyool ID + public key fingerprint, not any secret.
            Map<EncodeHintType,Object> hints=new EnumMap<>(EncodeHintType.class);
            hints.put(EncodeHintType.MARGIN,2);
            String fingerprint=PhoneIdentity.fingerprint();
            String qrPayload="XYOOL2:"+id+":"+fingerprint;
            BitMatrix grid=new MultiFormatWriter().encode(qrPayload,BarcodeFormat.QR_CODE,640,640,hints);
            int width=grid.getWidth(),height=grid.getHeight();
            Bitmap bitmap=Bitmap.createBitmap(width,height,Bitmap.Config.ARGB_8888);
            int[] pixels=new int[width*height];
            for(int y=0;y<height;y++){
                int offset=y*width;
                for(int x=0;x<width;x++)pixels[offset+x]=grid.get(x,y)?Color.BLACK:Color.WHITE;
            }
            bitmap.setPixels(pixels,0,width,0,0,width,height);
            ImageView qr=new ImageView(this);
            qr.setImageBitmap(bitmap);
            qr.setContentDescription("QR code for your Xyool ID "+id);
            qr.setAdjustViewBounds(true);
            qr.setPadding(dp(18),dp(18),dp(18),dp(18));
            qr.setBackgroundColor(Color.WHITE);
            LinearLayout frame=column();
            frame.setPadding(dp(16),dp(12),dp(16),dp(5));
            frame.addView(qr,new LinearLayout.LayoutParams(-1,-2));
            TextView label=text(id,18,FG,true);
            label.setGravity(Gravity.CENTER);
            frame.addView(label);
            TextView pinLabel=text("Device key: "+fingerprint,11,MUTED,false);
            pinLabel.setTextIsSelectable(true);
            frame.addView(pinLabel);
            new AlertDialog.Builder(this)
                .setTitle("My Xyool ID")
                .setView(frame)
                .setMessage(null)
                .setPositiveButton("Done",null)
                .show();
        }catch(Exception e){
            status("Android Keystore unavailable. Secure identity QR could not be displayed.");
        }
    }
    private static final int QR_SCAN_REQUEST = 493;

    private void scanIdQr(){
        try{
            Intent scanner = new Intent(this, QrScannerActivity.class);
            startActivityForResult(scanner, QR_SCAN_REQUEST);
        }catch(Exception e){
            status("Unable to start QR scanner. Enter their ID manually.");
            Toast.makeText(this,"QR scanner couldn't open. Try Camera permission in app settings.",Toast.LENGTH_LONG).show();
        }
    }
    @Override protected void onActivityResult(int requestCode,int resultCode,Intent data){
        if(requestCode != QR_SCAN_REQUEST){
            super.onActivityResult(requestCode,resultCode,data);
            return;
        }
        if(resultCode != RESULT_OK || data == null){
            status("No ID scanned. You can also type an ID.");
            return;
        }
        String scanned = data.getStringExtra(QrScannerActivity.EXTRA_ID);
        if(scanned == null)return;
        String raw = scanned.trim().toUpperCase(Locale.US);
        // Only the exact public Xyool ID is allowed; never execute QR contents.
        if(!raw.matches("^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$")){
            status("That QR wasn't a valid Xyool ID.");
            return;
        }
        if(raw.equals(id)){
            status("That's your own QR. Scan the other person's code.");
            return;
        }
        String fingerprint=data.getStringExtra(QrScannerActivity.EXTRA_KEY_PIN);
        if(fingerprint!=null){
            try{PhoneIdentity.pinFromQr(this,raw,fingerprint);}
            catch(IllegalArgumentException bad){status("Invalid QR public-key fingerprint.");return;}
        }
        targetInput.setText(raw);
        if(savedContacts!=null){
            // Save the public ID once. QR key verification is held independently
            // in PhoneIdentity; manual contacts never become QR-verified.
            boolean exists=false;
            for(SavedContacts.Entry c:savedContacts.all())if(c.id.equals(raw))exists=true;
            if(!exists)savedContacts.save(raw,raw);
            showSavedContacts();
        }
        new AlertDialog.Builder(this)
            .setTitle("Xyool ID scanned")
            .setMessage(raw + (fingerprint!=null?
                " • Device key pinned from QR. Tap Call.":
                " • Legacy QR has no verified device key. Verify identity separately before calling."))
            .setPositiveButton("OK",null)
            .show();
        status("ID scanned successfully.");
    }

    private void showSavedContacts(){
        if(contactsList==null||savedContacts==null)return;
        contactsList.removeAllViews();
        List<SavedContacts.Entry> entries=savedContacts.all();
        if(entries.isEmpty()){
            contactsList.addView(text("No saved Xyool IDs yet.",13,MUTED,false));return;
        }
        for(SavedContacts.Entry contact:entries){
            final String target=contact.id;
            space(contactsList,5);
            boolean verified=PhoneIdentity.qrVerifiedFingerprint(this,target)!=null;
            button(contactsList,contact.name+" • "+(verified?"QR verified":"Unverified")+
                " • Call",false,v->{
                targetInput.setText(target);
                call();
            });
            space(contactsList,3);
            button(contactsList,"Edit / remove "+contact.name,false,v->editContact(contact));
        }
    }
    private void saveEnteredContact(){
        String target=normalize(targetInput.getText().toString());
        if(target==null||target.equals(id)){
            status("Enter a valid different Xyool ID to save.");return;
        }
        promptSaveContact(target,target);
    }
    private void promptSaveContact(String target,String currentName){
        EditText name=new EditText(this);
        name.setSingleLine(true);
        name.setInputType(InputType.TYPE_CLASS_TEXT|InputType.TYPE_TEXT_FLAG_CAP_WORDS);
        name.setText(currentName.equals(target)?"":currentName);
        name.setHint("Contact name (optional)");
        new AlertDialog.Builder(this)
            .setTitle("Save Xyool contact")
            .setMessage("Saved only on this phone. A typed ID is not identity verification.")
            .setView(name)
            .setNegativeButton("Cancel",null)
            .setPositiveButton("Save",(d,w)->{
                if(!savedContacts.save(target,name.getText().toString())){
                    status("Contact could not be saved.");return;
                }
                showSavedContacts();
                status("Saved "+target+" to Xyool contacts.");
            }).show();
    }
    private void editContact(SavedContacts.Entry entry){
        new AlertDialog.Builder(this)
            .setTitle(entry.name)
            .setItems(new String[]{"Rename contact","Remove saved contact"},(d,which)->{
                if(which==0)promptSaveContact(entry.id,entry.name);
                else new AlertDialog.Builder(this)
                    .setTitle("Remove saved contact?")
                    .setMessage("Remove "+entry.name+" from this app's saved contact list? This does not remove separately pinned QR keys.")
                    .setNegativeButton("Cancel",null)
                    .setPositiveButton("Remove",(dialog,choice)->{
                        if(savedContacts.remove(entry.id)){
                            showSavedContacts();status("Contact removed.");
                        }
                    }).show();
            }).show();
    }

    private void connectionStatus(){
        if(!hasReachability()){
            status("Xyool Network OFF · Turn it on to become reachable by ID.");return;
        }
        if(cloud!=null&&cloud.hasVoiceSession()){
            status(cloud.voiceState());return;
        }
        int n=cloud==null?0:cloud.localPeerCount();
        if(!BridgePolicy.allowsCloud(bridgeMode())){
            status(n>0?"Local Xyool peers: "+n:"Local-only mode · no internet registration.");
        }else if(registered){
            status(n>0?"Internet online · "+n+" nearby phones.":"Internet calling online.");
        }else if(n>0){
            status("Nearby Xyool phones: "+n+" · Wi-Fi calling available.");
        }else{
            status("Connecting to Xyool Network…");
        }
    }
    private void status(String message){
        callStatus=message;
        runOnUiThread(()->{
            if(stateLabel!=null)stateLabel.setText(message);
        });
    }
    private String normalize(String raw){
        String clean=raw.toUpperCase(Locale.US).replaceAll("[^A-Z0-9]","");
        if(clean.startsWith("XY"))clean=clean.substring(2);
        if(clean.length()!=12||!clean.matches("^[A-HJ-NP-Z2-9]{12}$"))return null;
        return "XY-"+clean.substring(0,4)+"-"+clean.substring(4,8)+"-"+clean.substring(8);
    }
    private void connect(){
        if(!hasReachability()){
            registered=false;connectionStatus();return;
        }
        if(cloudBound)return;
        cloudBound=bindService(new Intent(this,CallReachabilityService.class),
            cloudLink,Context.BIND_AUTO_CREATE);
        if(!cloudBound)status("Xyool calling service couldn't start.");
    }
    private void disconnect(){
        registered=false;
        if(cloud!=null){cloud.setListener(null);cloud=null;}
        if(cloudBound){
            unbindService(cloudLink);
            cloudBound=false;
        }
    }
    private boolean hasReachability(){return prefs.getBoolean(CallReachabilityService.PREF_ENABLED,false);}
    private void updateReachabilityButton(){
        if(reachabilityButton!=null)reachabilityButton.setText(
            hasReachability()?"Xyool Network: ON • Tap to stop":
                "Xyool Network: OFF • Tap to enable");
    }
    private void enableReachability(){
        if(Build.VERSION.SDK_INT>=33 &&
            checkSelfPermission(Manifest.permission.POST_NOTIFICATIONS)!=PackageManager.PERMISSION_GRANTED){
            requestPermissions(new String[]{Manifest.permission.POST_NOTIFICATIONS},482);
            return;
        }
        prefs.edit().putBoolean(CallReachabilityService.PREF_ENABLED,true).apply();
        try{
            Intent start=new Intent(this,CallReachabilityService.class)
                .setAction(CallReachabilityService.ACTION_ENABLE);
                startForegroundService(start);
            if(!cloudBound)connect();
            updateReachabilityButton();
            status("Xyool Network enabled. Reachable by ID while the foreground service runs.");
        }catch(RuntimeException ex){
            prefs.edit().putBoolean(CallReachabilityService.PREF_ENABLED,false).apply();
            updateReachabilityButton();
            status("Android couldn't start Xyool Network. Check app permissions.");
        }
    }
    private void disableReachability(){
        if(cloud!=null)cloud.hangupVoice();
        prefs.edit().putBoolean(CallReachabilityService.PREF_ENABLED,false).apply();
        startService(new Intent(this,CallReachabilityService.class)
            .setAction(CallReachabilityService.ACTION_DISABLE));
        disconnect();
        updateReachabilityButton();
        status("Xyool Network OFF. ID registration, local discovery, and incoming listening stopped.");
    }
    private void toggleReachability(){
        if(hasReachability()){disableReachability();return;}
        // Legacy Direct-only settings are a privacy preference. Do not
        // silently turn them into internet registration when removing
        // the developer routing controls.
        if(!BridgePolicy.allowsCloud(bridgeMode())){
            new AlertDialog.Builder(this)
                .setTitle("Enable internet reachability?")
                .setMessage("This replaces your previous local-only mode. Xyool will use a signaling server to register your ID across networks. The operator can see registration metadata such as your ID and IP address.")
                .setNegativeButton("Cancel",null)
                .setPositiveButton("Enable network",(dialog,which)->{
                    prefs.edit().putString(BridgePolicy.PREF_MODE,BridgePolicy.HYBRID).apply();
                    enableReachability();
                }).show();
            return;
        }
        enableReachability();
    }
    private void call(){
        if(!hasReachability()){status("Turn on Xyool Network before calling by ID.");return;}
        if(cloud==null){status("Connecting to Xyool Network. Try again.");return;}
        if(cloud.hasVoiceSession()){status("Finish the current call first.");return;}
        String dest=normalize(targetInput.getText().toString());
        if(dest==null){status("Enter a valid Xyool ID, like XY-ABCD-EFGH-JKLM.");return;}
        if(dest.equals(id)){status("You cannot call your own ID.");return;}
        boolean localAvailable=LocalPeerNode.onWifi(this)&&cloud.hasLocalPeer(dest);
        BridgePolicy.Route route=BridgePolicy.choose(bridgeMode(),localAvailable,registered);
        if(route==BridgePolicy.Route.MANUAL_DIRECT_REQUIRED){
            status("No network route to that ID yet.");return;
        }
        requestMicrophone(()->{
            if(cloud==null || !cloud.dialVoice(dest,route==BridgePolicy.Route.LOCAL_DIRECT))
                status("Unable to start the call. Check network and microphone permissions.");
        });
    }
    private void received(JSONObject message,boolean fromLocal){
        String type=message.optString("type","");
        if("incoming".equals(type)){
            if(cloud==null||!cloud.hasIncomingVoice())return;
            if(autoAnswerRequested){
                autoAnswerRequested=false;
                acceptIncomingCall();
            }else if(incomingAlert==null){
                incomingDialog(cloud.voicePeerId());
            }
            return;
        }
        if("ended".equals(type)||"busy".equals(type)||
            "unavailable".equals(type)||"error".equals(type)){
            stopIncomingRing();
            if(incomingAlert!=null){
                AlertDialog shown=incomingAlert;incomingAlert=null;shown.dismiss();
            }
            if(cloud!=null)status(cloud.voiceState());
        }
    }
    // The ringtone is deliberately tied to the visible, user-accepted call
    // invitation. This alpha does not claim background or push call delivery.
    private void startIncomingRing(){
        stopIncomingRing();
        try{
            android.net.Uri sound=RingtoneManager.getDefaultUri(RingtoneManager.TYPE_RINGTONE);
            if(sound==null)sound=RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION);
            if(sound==null)return;
            incomingRingtone=RingtoneManager.getRingtone(getApplicationContext(),sound);
            if(incomingRingtone!=null){
                incomingRingtone.setAudioAttributes(new android.media.AudioAttributes.Builder()
                    .setUsage(android.media.AudioAttributes.USAGE_NOTIFICATION_RINGTONE)
                    .setContentType(android.media.AudioAttributes.CONTENT_TYPE_SONIFICATION)
                    .build());
                incomingRingtone.play();
            }
        }catch(RuntimeException ignored){incomingRingtone=null;}
    }
    private void stopIncomingRing(){
        if(incomingRingtone==null)return;
        try{incomingRingtone.stop();}catch(RuntimeException ignored){}
        incomingRingtone=null;
    }
    private void incomingDialog(String from){
        status("Incoming call from "+from);
        startIncomingRing();
        incomingAlert=new AlertDialog.Builder(this)
            .setTitle("Incoming Xyool call")
            .setMessage(from+" wants to talk.")
            .setCancelable(false)
            .setNegativeButton("Decline",(d,w)->{
                stopIncomingRing();
                if(cloud!=null)cloud.declineVoice();
                status("Call declined.");
            })
            .setPositiveButton("Accept",(d,w)->acceptIncomingCall())
            .create();
        incomingAlert.setOnDismissListener(d->{
            stopIncomingRing();
            if(incomingAlert==d)incomingAlert=null;
        });
        incomingAlert.show();
    }
    private void acceptIncomingCall(){
        stopIncomingRing();
        if(incomingAlert!=null){
            AlertDialog dialog=incomingAlert;incomingAlert=null;dialog.dismiss();
        }
        if(cloud==null||!cloud.hasIncomingVoice()){
            status("Incoming call is no longer available.");return;
        }
        requestMicrophone(()->{
            if(cloud==null||!cloud.acceptVoice())
                status("Could not accept call or start foreground microphone.");
        });
    }
    private void requestMicrophone(Runnable next){
        if(checkSelfPermission(Manifest.permission.RECORD_AUDIO)==PackageManager.PERMISSION_GRANTED)next.run();
        else{
            pendingMicrophone=next;
            requestPermissions(new String[]{Manifest.permission.RECORD_AUDIO},MIC_REQUEST);
        }
    }
    @Override public void onRequestPermissionsResult(int request,String[] permissions,int[] grants){
        super.onRequestPermissionsResult(request,permissions,grants);
        if(request==482){
            if(grants.length>0&&grants[0]==PackageManager.PERMISSION_GRANTED)
                enableReachability();
            else status("Notification permission is needed for background call alerts.");
            return;
        }
        if(request!=MIC_REQUEST)return;
        Runnable next=pendingMicrophone;pendingMicrophone=null;
        if(grants.length>0&&grants[0]==PackageManager.PERMISSION_GRANTED&&next!=null)next.run();
        else{
            if(cloud!=null&&cloud.hasIncomingVoice())cloud.declineVoice();
            status("Microphone permission is required for Xyool voice.");
        }
    }
    private void toggleMute(){
        if(cloud==null)status("Xyool Network service unavailable.");
        else cloud.muteVoice();
    }
    private void hangup(){
        stopIncomingRing();
        if(cloud!=null)cloud.hangupVoice();
        else status("No active call.");
    }
    @Override protected void onDestroy(){
        disposed=true;
        stopIncomingRing();
        // Never hang up or dispose service-owned media when Activity exits.
        disconnect();
        super.onDestroy();
    }
}
