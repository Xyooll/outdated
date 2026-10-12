package org.xyool.connect;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Path;
import android.graphics.drawable.GradientDrawable;
import android.net.Uri;
import android.os.Bundle;
import android.text.InputType;
import android.view.Gravity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public final class MainActivity extends Activity {
    private static final int BACKGROUND = 0xff0c1822;
    private static final int PANEL = 0xff192f3b;
    private static final int BORDER = 0xff345766;
    private static final int PRIMARY = 0xff68dbc3;
    private static final int FOREGROUND = 0xfff1faf7;
    private static final int SECONDARY = 0xffaec8cf;
    private static final String[] TABS = {"Home", "Phone", "People", "Messages", "Avatar"};
    private static final String[] SKIN_LABELS = {"Light", "Tan", "Brown", "Deep"};
    private static final int[] SKIN_COLORS = {0xfff2c9a0, 0xffdba574, 0xffab734e, 0xff70472f};
    private static final String[] HAIR_LABELS = {"Dark", "Brown", "Blond", "Red"};
    private static final int[] HAIR_COLORS = {0xff26232e, 0xff6b402b, 0xffc79a52, 0xffa14e40};
    private static final String[] SHIRT_LABELS = {"Teal", "Blue", "Purple", "Pink"};
    private static final int[] SHIRT_COLORS = {0xff50b5bb, 0xff577ee3, 0xffa477d1, 0xffd76e8a};

    private SharedPreferences state;
    private LinearLayout content;
    private String screen = "Home";

    @Override public void onCreate(Bundle savedState) {
        super.onCreate(savedState);
        state = getSharedPreferences("xyool_private", MODE_PRIVATE);
        getWindow().setStatusBarColor(BACKGROUND);
        getWindow().setNavigationBarColor(BACKGROUND);
        drawScreen();
    }

    private int dp(float value) {
        return (int) (value * getResources().getDisplayMetrics().density + 0.5f);
    }
    private GradientDrawable shape(int fill, int radius, int line) {
        GradientDrawable drawable = new GradientDrawable();
        drawable.setColor(fill);
        drawable.setCornerRadius(dp(radius));
        if (line != 0) drawable.setStroke(dp(1), line);
        return drawable;
    }
    private TextView text(String value, int size, int color, boolean bold) {
        TextView t = new TextView(this);
        t.setText(value);
        t.setTextSize(size);
        t.setTextColor(color);
        if (bold) t.setTypeface(null, 1);
        t.setIncludeFontPadding(true);
        return t;
    }
    private LinearLayout column() {
        LinearLayout l = new LinearLayout(this);
        l.setOrientation(LinearLayout.VERTICAL);
        return l;
    }
    private LinearLayout row() {
        LinearLayout l = new LinearLayout(this);
        l.setOrientation(LinearLayout.HORIZONTAL);
        l.setGravity(Gravity.CENTER_VERTICAL);
        return l;
    }
    private void gap(LinearLayout parent, int height) {
        View v = new View(this);
        parent.addView(v, new LinearLayout.LayoutParams(1, dp(height)));
    }
    private void title(String eyebrow, String heading) {
        content.addView(text(eyebrow.toUpperCase(), 11, PRIMARY, true));
        gap(content, 6);
        content.addView(text(heading, 28, FOREGROUND, true));
        gap(content, 16);
    }
    private LinearLayout panel() {
        LinearLayout p = column();
        p.setPadding(dp(17), dp(17), dp(17), dp(17));
        p.setBackground(shape(PANEL, 18, BORDER));
        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(-1, -2);
        params.bottomMargin = dp(13);
        content.addView(p, params);
        return p;
    }
    private Button button(String value, boolean primary, View.OnClickListener listener) {
        Button b = new Button(this);
        b.setText(value);
        b.setAllCaps(false);
        b.setTextSize(14);
        b.setTextColor(primary ? BACKGROUND : FOREGROUND);
        b.setBackground(shape(primary ? PRIMARY : 0xff274952, 12, primary ? 0 : BORDER));
        b.setMinHeight(dp(49));
        b.setPadding(dp(12), dp(8), dp(12), dp(8));
        b.setOnClickListener(listener);
        return b;
    }
    private EditText entry(String hint, int inputType) {
        EditText e = new EditText(this);
        e.setHint(hint);
        e.setHintTextColor(0xff93afba);
        e.setTextColor(FOREGROUND);
        e.setTextSize(16);
        e.setSingleLine(true);
        e.setInputType(inputType);
        e.setPadding(dp(12), dp(10), dp(12), dp(10));
        e.setBackground(shape(0xff0f2532, 10, BORDER));
        return e;
    }
    private void drawScreen() {
        LinearLayout root = column();
        root.setBackgroundColor(BACKGROUND);

        TextView brand = text("✦  Xyool Connect", 23, FOREGROUND, true);
        brand.setPadding(dp(18), dp(15), dp(12), dp(13));
        root.addView(brand);

        ScrollView scroller = new ScrollView(this);
        scroller.setFillViewport(true);
        content = column();
        content.setPadding(dp(16), dp(8), dp(16), dp(26));
        scroller.addView(content, new ScrollView.LayoutParams(-1, -2));
        root.addView(scroller, new LinearLayout.LayoutParams(-1, 0, 1f));

        LinearLayout navigation = row();
        navigation.setBackgroundColor(0xff142936);
        navigation.setPadding(dp(3), dp(7), dp(3), dp(7));
        for (String tab : TABS) {
            TextView b = text(tab, 12, tab.equals(screen) ? PRIMARY : SECONDARY, tab.equals(screen));
            b.setGravity(Gravity.CENTER);
            b.setPadding(dp(1), dp(14), dp(1), dp(14));
            if (tab.equals(screen)) b.setBackground(shape(0xff26535a, 10, 0));
            navigation.addView(b, new LinearLayout.LayoutParams(0, -2, 1f));
            b.setOnClickListener(v -> { screen = tab; drawScreen(); });
        }
        root.addView(navigation);
        setContentView(root);

        switch (screen) {
            case "Phone": showPhone(); break;
            case "People": showPeople(); break;
            case "Messages": showMessages(); break;
            case "Avatar": showProfile(); break;
            default: showHome();
        }
    }
    private void showHome() {
        title("MY SPACE", "Welcome, " + state.getString("name", "Friend") + ".");
        LinearLayout card = panel();
        LinearLayout horizontal = row();
        Avatar avatar = new Avatar();
        horizontal.addView(avatar, new LinearLayout.LayoutParams(dp(112), dp(140)));
        LinearLayout info = column();
        info.addView(text("Your 2D avatar", 18, FOREGROUND, true));
        gap(info, 6);
        info.addView(text("A simple, private beginning for Xyool Connect.", 13, SECONDARY, false));
        gap(info, 9);
        info.addView(button("Customize", false, v -> { screen = "Avatar"; drawScreen(); }));
        LinearLayout.LayoutParams right = new LinearLayout.LayoutParams(0, -2, 1f);
        right.leftMargin = dp(11);
        horizontal.addView(info, right);
        card.addView(horizontal);

        LinearLayout actions = panel();
        actions.addView(text("Quick actions", 18, FOREGROUND, true));
        gap(actions, 12);
        actions.addView(button("Call a number", true, v -> {screen = "Phone"; drawScreen();}));
        gap(actions, 9);
        actions.addView(button("People", false, v -> {screen = "People"; drawScreen();}));
        gap(actions, 9);
        actions.addView(button("Send an SMS", false, v -> {screen = "Messages"; drawScreen();}));
        gap(content, 8);
        content.addView(text("No Google Play Services or account are required. The experimental native voice module uses the Internet and microphone only when you choose to start an audio session.", 12, SECONDARY, false));
    }
    private void showPhone() {
        title("PHONE", "Make a call");
        LinearLayout p = panel();
        p.addView(text("Number", 13, SECONDARY, true));
        gap(p, 8);
        EditText number = entry("+1 555 123 4567", InputType.TYPE_CLASS_PHONE);
        p.addView(number);
        gap(p, 13);
        p.addView(button("Open Android dialer", true, v -> launchNumber(number.getText().toString(), false)));
        gap(p, 10);
        p.addView(button("Write an SMS", false, v -> launchNumber(number.getText().toString(), true)));
        content.addView(text("Xyool opens your existing Android calling or SMS app. A cellular plan is normally required for regular calls and texts.", 13, SECONDARY, false));
        gap(content, 16);
        LinearLayout internet = panel();
        internet.addView(text("Internet voice calling", 18, FOREGROUND, true));
        gap(internet, 6);
        internet.addView(text("Call another Xyool user with a private room invitation, or use a SIP provider to reach a SIP address.", 13, SECONDARY, false));
        gap(internet, 12);
        internet.addView(button("Xyool voice / SIP calls", true, v ->
            startActivity(new Intent(this, CallServicesActivity.class))));
    }
    private void showMessages() {
        title("MESSAGES", "Text someone");
        LinearLayout p = panel();
        p.addView(text("Send an SMS", 18, FOREGROUND, true));
        gap(p, 8);
        p.addView(text("Enter the phone number. Your Android messaging app handles delivery.", 13, SECONDARY, false));
        gap(p, 12);
        EditText number = entry("Recipient phone number", InputType.TYPE_CLASS_PHONE);
        p.addView(number);
        gap(p, 12);
        p.addView(button("Open SMS composer", true, v -> launchNumber(number.getText().toString(), true)));
        LinearLayout box = panel();
        box.addView(text("Xyool-to-Xyool chat", 18, FOREGROUND, true));
        gap(box, 8);
        box.addView(text("Not active yet. We'll add authenticated, end-to-end encrypted internet messaging later.", 13, SECONDARY, false));
    }
    private String cleanedNumber(String raw) {
        String result = raw.trim().replaceAll("[\\s()\\-.]", "");
        if (!result.matches("\\+?[0-9]{3,15}")) return null;
        return result;
    }
    private void launchNumber(String raw, boolean sms) {
        String number = cleanedNumber(raw);
        if (number == null) { Toast.makeText(this, "Enter a valid phone number", Toast.LENGTH_LONG).show(); return; }
        Uri uri = Uri.fromParts(sms ? "smsto" : "tel", number, null);
        Intent intent = new Intent(sms ? Intent.ACTION_SENDTO : Intent.ACTION_DIAL, uri);
        try { startActivity(intent); }
        catch (ActivityNotFoundException e) {
            Toast.makeText(this, "No compatible phone or SMS app is installed", Toast.LENGTH_LONG).show();
        }
    }
    private JSONArray contacts() {
        try { return new JSONArray(state.getString("contacts", "[]")); }
        catch (JSONException e) { return new JSONArray(); }
    }
    private void saveContacts(JSONArray contacts) {
        state.edit().putString("contacts", contacts.toString()).apply();
    }
    private void showPeople() {
        title("LOCAL ADDRESS BOOK", "People");
        LinearLayout addPanel = panel();
        addPanel.addView(button("+ Add contact", true, v -> addContactDialog()));
        JSONArray list = contacts();
        if (list.length() == 0) {
            content.addView(text("No contacts yet. Add someone to call or message them.", 14, SECONDARY, false));
        }
        for (int i=0; i<list.length(); i++) {
            JSONObject obj = list.optJSONObject(i);
            if (obj == null) continue;
            final int index = i;
            String name = obj.optString("name", "Contact");
            String number = obj.optString("number", "");
            LinearLayout p = panel();
            p.addView(text(name, 17, FOREGROUND, true));
            gap(p, 4);
            p.addView(text(number, 13, SECONDARY, false));
            gap(p, 10);
            LinearLayout buttons = row();
            Button call = button("Call", true, v -> launchNumber(number, false));
            Button sms = button("SMS", false, v -> launchNumber(number, true));
            Button delete = button("Remove", false, v -> removeContact(index));
            LinearLayout.LayoutParams one = new LinearLayout.LayoutParams(0, -2, 1);
            one.rightMargin = dp(6);
            buttons.addView(call, one);
            LinearLayout.LayoutParams two = new LinearLayout.LayoutParams(0, -2, 1);
            two.rightMargin = dp(6);
            buttons.addView(sms, two);
            buttons.addView(delete, new LinearLayout.LayoutParams(0, -2, 1));
            p.addView(buttons);
        }
        gap(content, 4);
        content.addView(text("Contacts are private to this app and stay on this phone. They are not synced or backed up.", 12, SECONDARY, false));
    }
    private void addContactDialog() {
        LinearLayout form = column();
        form.setPadding(dp(20), dp(10), dp(20), dp(6));
        EditText name = entry("Name", InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_FLAG_CAP_WORDS);
        EditText number = entry("Phone number", InputType.TYPE_CLASS_PHONE);
        form.addView(name);
        gap(form, 12);
        form.addView(number);
        AlertDialog dialog = new AlertDialog.Builder(this)
            .setTitle("New contact")
            .setView(form)
            .setNegativeButton("Cancel", null)
            .setPositiveButton("Save", null).create();
        dialog.setOnShowListener(v -> dialog.getButton(AlertDialog.BUTTON_POSITIVE).setOnClickListener(w -> {
            String label = name.getText().toString().trim();
            String phone = cleanedNumber(number.getText().toString());
            if (label.isEmpty() || label.length()>64 || phone == null) {
                Toast.makeText(this, "Enter a name and valid phone number", Toast.LENGTH_LONG).show();
                return;
            }
            JSONArray current = contacts();
            JSONObject obj = new JSONObject();
            try { obj.put("name", label); obj.put("number", phone); }
            catch (JSONException ignored) { return; }
            current.put(obj);
            saveContacts(current);
            dialog.dismiss();
            drawScreen();
        }));
        dialog.show();
    }
    private void removeContact(int removeIndex) {
        new AlertDialog.Builder(this).setTitle("Remove contact?")
            .setMessage("This removes the contact only from Xyool Connect.")
            .setNegativeButton("Cancel", null)
            .setPositiveButton("Remove", (dialog, which) -> {
                JSONArray all = contacts();
                JSONArray changed = new JSONArray();
                for (int i=0; i<all.length(); i++) if (i != removeIndex) changed.put(all.opt(i));
                saveContacts(changed);
                drawScreen();
            }).show();
    }
    private int selected(String key, int maximum, int initial) {
        int value = state.getInt(key, initial);
        return Math.max(0, Math.min(maximum-1, value));
    }
    private void showProfile() {
        title("YOUR AVATAR", "Customize");
        LinearLayout p = panel();
        Avatar avatar = new Avatar();
        LinearLayout wrapper = row();
        wrapper.setGravity(Gravity.CENTER);
        wrapper.addView(avatar, new LinearLayout.LayoutParams(dp(140), dp(177)));
        p.addView(wrapper);
        gap(p, 14);
        p.addView(text("Display name", 13, SECONDARY, true));
        gap(p, 6);
        EditText name = entry("Friend", InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_FLAG_CAP_WORDS);
        name.setText(state.getString("name", "Friend"));
        name.setFilters(new android.text.InputFilter[]{new android.text.InputFilter.LengthFilter(40)});
        p.addView(name);
        gap(p, 12);
        p.addView(button("Skin tone: " + SKIN_LABELS[selected("skin", 4, 1)], false,
            v -> choose("skin", SKIN_LABELS, 1)));
        gap(p, 9);
        p.addView(button("Hair: " + HAIR_LABELS[selected("hair", 4, 0)], false,
            v -> choose("hair", HAIR_LABELS, 0)));
        gap(p, 9);
        p.addView(button("Shirt: " + SHIRT_LABELS[selected("shirt", 4, 0)], false,
            v -> choose("shirt", SHIRT_LABELS, 0)));
        gap(p, 13);
        p.addView(button("Save avatar", true, v -> {
            String newName = name.getText().toString().trim();
            state.edit().putString("name", newName.isEmpty() ? "Friend" : newName).apply();
            screen = "Home";
            drawScreen();
        }));
        LinearLayout privacy = panel();
        privacy.addView(text("Local data", 18, FOREGROUND, true));
        gap(privacy, 6);
        privacy.addView(text("Xyool stores your contacts and avatar in private Android app storage. Native calls use Internet and optional microphone permission, but the app does not request Contacts, Phone, or SMS data access.", 13, SECONDARY, false));
        gap(privacy, 12);
        privacy.addView(button("Erase Xyool data", false, v ->
            new AlertDialog.Builder(this).setTitle("Erase local data?")
                .setMessage("Your saved contacts and avatar will be permanently erased from Xyool Connect.")
                .setNegativeButton("Cancel", null)
                .setPositiveButton("Erase", (dialog, which) -> {
                    state.edit().clear().apply();
                    screen = "Home";
                    drawScreen();
                }).show()
        ));
    }
    private void choose(String key, String[] choices, int defaultIndex) {
        new AlertDialog.Builder(this)
            .setTitle("Choose " + key)
            .setSingleChoiceItems(choices, selected(key, choices.length, defaultIndex),
                (dialog, which) -> {
                    state.edit().putInt(key, which).apply();
                    dialog.dismiss();
                    drawScreen();
                })
            .setNegativeButton("Cancel", null).show();
    }
    private final class Avatar extends View {
        private final Paint paint = new Paint(Paint.ANTI_ALIAS_FLAG);
        Avatar() { super(MainActivity.this); setContentDescription("Your customized 2D avatar"); }
        private void fill(Canvas c, int color, float l, float t, float r, float b) {
            paint.setColor(color); paint.setStyle(Paint.Style.FILL);
            c.drawOval(l,t,r,b,paint);
        }
        @Override protected void onDraw(Canvas c) {
            super.onDraw(c);
            c.save();
            c.scale(getWidth()/120f, getHeight()/150f);
            paint.setColor(0xff315765);
            paint.setStyle(Paint.Style.FILL);
            c.drawRoundRect(0,0,120,150,16,16,paint);
            fill(c,0x55091b24,17,133,104,147);
            paint.setColor(SHIRT_COLORS[selected("shirt",4,0)]);
            Path torso = new Path();
            torso.moveTo(12,148); torso.lineTo(15,119);
            torso.cubicTo(19,101,38,99,60,99);
            torso.cubicTo(82,99,101,101,105,119);
            torso.lineTo(108,148); torso.close();
            c.drawPath(torso,paint);
            fill(c,SKIN_COLORS[selected("skin",4,1)],31,35,89,108);
            paint.setColor(HAIR_COLORS[selected("hair",4,0)]);
            Path hair = new Path();
            hair.moveTo(30,75); hair.cubicTo(12,23,41,14,62,18);
            hair.cubicTo(95,13,105,44,90,75); hair.lineTo(86,52);
            hair.cubicTo(71,37,49,38,34,52); hair.close();
            c.drawPath(hair,paint);
            fill(c,0xff1d2430,43,72,49,78);
            fill(c,0xff1d2430,71,72,77,78);
            paint.setColor(0xff985b50);
            paint.setStyle(Paint.Style.STROKE);
            paint.setStrokeWidth(2.5f);
            Path smile = new Path();
            smile.moveTo(52,91); smile.quadTo(60,99,69,91);
            c.drawPath(smile,paint);
            c.restore();
        }
    }
}
