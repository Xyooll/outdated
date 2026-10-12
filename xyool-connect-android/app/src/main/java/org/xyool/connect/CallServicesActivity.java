package org.xyool.connect;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.drawable.GradientDrawable;
import android.net.Uri;
import android.os.Bundle;
import android.text.InputType;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;
import java.security.SecureRandom;
import android.util.Base64;
import java.util.regex.Pattern;

/**
 * Functional call handoff for Xyool Connect.
 *
 * Xyool-to-Xyool calls: invitation + Jitsi conference hosted by the provider.
 * SIP calls: deep-link into an installed SIP client with its own configured account.
 * Android telephony is still handled by Android Telecom, not this Activity.
 *
 * This activity does not collect credentials, hold microphone permission, create
 * an in-app media session, or claim to provide end-to-end encryption.
 */
public final class CallServicesActivity extends Activity {
    private static final int BG = 0xff0c1822;
    private static final int PANEL = 0xff192f3b;
    private static final int FG = 0xfff1faf7;
    private static final int SECONDARY = 0xffaec8cf;
    private static final int ACCENT = 0xff68dbc3;
    private static final Pattern SIP_ADDRESS = Pattern.compile(
       "^[a-zA-Z0-9_.+%\\-]{1,64}@[a-zA-Z0-9\\-]+(?:\\.[a-zA-Z0-9\\-]+)+(?:\\:[0-9]{1,5})?$");
    private static final Pattern ROOM = Pattern.compile("^Xyool-[A-Za-z0-9_-]{22}$");
    private final SecureRandom random = new SecureRandom();
    private SharedPreferences state;
    private LinearLayout parent;
    private EditText sipAddress;
    private EditText joinLink;
    private String invitation;

    @Override public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        state = getSharedPreferences("xyool_private", MODE_PRIVATE);
        getWindow().setStatusBarColor(BG);
        getWindow().setNavigationBarColor(BG);
        invitation = state.getString("last_invite", "");
        draw();
    }

    private int d(float n) { return (int)(n * getResources().getDisplayMetrics().density + .5f); }
    private GradientDrawable shape(int c) {
        GradientDrawable gd = new GradientDrawable();
        gd.setColor(c); gd.setCornerRadius(d(15));
        gd.setStroke(d(1), 0xff335868);
        return gd;
    }
    private TextView text(String value, int size, int color, boolean bold) {
        TextView t = new TextView(this);
        t.setText(value); t.setTextColor(color); t.setTextSize(size);
        if (bold) t.setTypeface(null, 1);
        return t;
    }
    private Button button(String label, boolean primary, View.OnClickListener action) {
        Button b = new Button(this);
        b.setAllCaps(false);
        b.setText(label);
        b.setTextSize(14);
        b.setTextColor(primary ? BG : FG);
        b.setBackground(shape(primary ? ACCENT : 0xff294e5a));
        b.setOnClickListener(action);
        b.setMinHeight(d(50));
        return b;
    }
    private void space(LinearLayout box, int px) {
        box.addView(new View(this), new LinearLayout.LayoutParams(d(1), d(px)));
    }
    private LinearLayout card() {
        LinearLayout box = new LinearLayout(this); box.setOrientation(LinearLayout.VERTICAL);
        box.setPadding(d(17),d(17),d(17),d(17)); box.setBackground(shape(PANEL));
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(-1,-2); lp.bottomMargin=d(13);
        parent.addView(box,lp);
        return box;
    }
    private EditText input(String hint, int type) {
        EditText t = new EditText(this);
        t.setSingleLine(true); t.setInputType(type);
        t.setTextSize(16); t.setHint(hint); t.setHintTextColor(0xff9ab6bc);
        t.setTextColor(FG); t.setBackground(shape(0xff0c2532));
        t.setPadding(d(12), d(12), d(12), d(12));
        return t;
    }

    private void draw() {
        LinearLayout root=new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL); root.setBackgroundColor(BG);
        ScrollView scroll = new ScrollView(this);
        parent = new LinearLayout(this); parent.setOrientation(LinearLayout.VERTICAL);
        parent.setPadding(d(16),d(16),d(16),d(18));
        scroll.addView(parent);
        root.addView(scroll,new LinearLayout.LayoutParams(-1,0,1f));
        Button back = button("‹  Back to Xyool Connect",false,v->finish());
        root.addView(back,new LinearLayout.LayoutParams(-1,d(54)));
        setContentView(root);

        parent.addView(text("XYOOL CONNECT", 11, ACCENT, true));
        space(parent,5);
        parent.addView(text("Internet calling", 29, FG, true));
        space(parent,9);
        parent.addView(text("Two internet options alongside your normal cellular calls.",14,SECONDARY,false));
        space(parent,16);

        LinearLayout xyool = card();
        xyool.addView(text("Xyool-to-Xyool voice",19,FG,true));
        space(xyool,6);
        xyool.addView(text("Create an invite for another person. Both join the same real-time voice meeting through Jitsi, an open-source service. Your invited person does not need cellular service.",13,SECONDARY,false));
        space(xyool,12);
        xyool.addView(button("Create a new voice invite",true,v->createInvite()));
        space(xyool,10);
        if (!invitation.isEmpty()) {
            xyool.addView(text("Your latest invite (not yet a connected call)",12,SECONDARY,true));
            space(xyool,7);
            TextView link = text(invitation, 12, ACCENT, false);
            link.setTextIsSelectable(true);
            xyool.addView(link);
            space(xyool,9);
            xyool.addView(button("Share invitation",false,v->shareInvite()));
            space(xyool,7);
            xyool.addView(button("Open this voice room",false,v->openJitsi(invitation)));
            space(xyool,9);
        }
        joinLink = input("Paste a Xyool invite link", InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_URI);
        xyool.addView(joinLink);
        space(xyool,8);
        xyool.addView(button("Join an existing voice room",false,v->{
            String valid = verifiedInvite(joinLink.getText().toString());
            if (valid==null) {
                Toast.makeText(this,"Paste a valid Xyool voice invite URL.",Toast.LENGTH_LONG).show();
                return;
            }
            openJitsi(valid);
        }));
        space(xyool,10);
        xyool.addView(text("The room creator must sign in to public meet.jit.si (a GitHub, Google, or Facebook account may be offered). The receiver normally joins without signing in. Meeting provider can process call metadata; this is NOT yet Xyool-operated end-to-end encryption.",12,SECONDARY,false));

        LinearLayout sip = card();
        sip.addView(text("SIP / Internet phone calls",19,FG,true));
        space(sip,6);
        sip.addView(text("Call a SIP address through a SIP app such as open-source Linphone. Both parties need SIP-capable accounts or endpoints. Calling ordinary phone numbers usually needs paid SIP/PSTN service.",13,SECONDARY,false));
        space(sip,10);
        sipAddress=input("friend@sip.example.org",InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_EMAIL_ADDRESS);
        sip.addView(sipAddress);
        space(sip,10);
        sip.addView(button("Call with installed SIP app",true,v->callSip()));
        space(sip,9);
        sip.addView(button("Get Linphone (official website)",false,v->launchWeb("https://www.linphone.org/")));
        space(sip,10);
        sip.addView(text("SIP credentials are never collected by Xyool Connect. Your selected SIP app authenticates and handles the voice call.",12,SECONDARY,false));
    }

    private void createInvite() {
        byte[] entropy = new byte[16];
        random.nextBytes(entropy);
        String room = "Xyool-" + Base64.encodeToString(entropy, Base64.URL_SAFE | Base64.NO_PADDING | Base64.NO_WRAP);
        invitation="https://meet.jit.si/"+room;
        state.edit().putString("last_invite",invitation).apply();
        draw();
        new AlertDialog.Builder(this)
            .setTitle("Voice invite created")
            .setMessage("Share the invite with the other person. Then open the room and sign in as the organizer when Jitsi asks. An invitation alone does not start or connect a call.")
            .setPositiveButton("Share invite",(dialog,which)->shareInvite())
            .setNegativeButton("Later",null).show();
    }
    private String verifiedInvite(String raw) {
        if (raw == null || raw.length()>300) return null;
        try {
            Uri uri=Uri.parse(raw.trim());
            if (!"https".equalsIgnoreCase(uri.getScheme())) return null;
            if (!"meet.jit.si".equalsIgnoreCase(uri.getHost())) return null;
            if (uri.getPort()!=-1 || uri.getUserInfo()!=null || uri.getQuery()!=null || uri.getFragment()!=null) return null;
            String room=uri.getLastPathSegment();
            if (room==null || !ROOM.matcher(room).matches() || uri.getPathSegments().size()!=1) return null;
            return "https://meet.jit.si/"+room;
        } catch (RuntimeException e) { return null; }
    }
    private void shareInvite() {
        if (invitation.isEmpty()) return;
        Intent send=new Intent(Intent.ACTION_SEND);
        send.setType("text/plain");
        send.putExtra(Intent.EXTRA_TEXT,"Join my Xyool voice call: "+invitation+"\nPlease keep this invite private.");
        try { startActivity(Intent.createChooser(send,"Share Xyool voice invite")); }
        catch (ActivityNotFoundException e) { Toast.makeText(this,"No sharing app found",Toast.LENGTH_LONG).show(); }
    }
    private void openJitsi(String link) {
        String valid=verifiedInvite(link);
        if (valid==null) {
            Toast.makeText(this,"Invalid invitation link",Toast.LENGTH_LONG).show();return;
        }
        launchWeb(valid);
    }
    private void launchWeb(String url) {
        try { startActivity(new Intent(Intent.ACTION_VIEW, Uri.parse(url))); }
        catch (ActivityNotFoundException e) { Toast.makeText(this,"A browser or compatible app is required.",Toast.LENGTH_LONG).show(); }
    }
    private void callSip() {
        String addr=sipAddress.getText().toString().trim();
        if (addr.startsWith("sip:")) addr=addr.substring(4);
        if (addr.startsWith("sips:")) addr=addr.substring(5);
        if (addr.length()>180 || !SIP_ADDRESS.matcher(addr).matches()) {
            Toast.makeText(this,"Use a SIP address like friend@sip.example.org",Toast.LENGTH_LONG).show();
            return;
        }
        Intent dial=new Intent(Intent.ACTION_VIEW,Uri.parse("sip:"+addr));
        try { startActivity(dial); }
        catch (ActivityNotFoundException e) {
            new AlertDialog.Builder(this)
                .setTitle("SIP app not found")
                .setMessage("Install an open-source SIP phone (for example Linphone), set up a SIP account, and retry.")
                .setPositiveButton("Open Linphone website",(dialog,which)->launchWeb("https://www.linphone.org/"))
                .setNegativeButton("Cancel",null).show();
        }
    }
}
