package org.xyool.connect;

import android.Manifest;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Color;
import android.net.Uri;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.provider.Settings;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.google.zxing.BarcodeFormat;
import com.google.zxing.ResultPoint;
import com.journeyapps.barcodescanner.BarcodeCallback;
import com.journeyapps.barcodescanner.BarcodeResult;
import com.journeyapps.barcodescanner.CameraPreview;
import com.journeyapps.barcodescanner.DecoratedBarcodeView;
import com.journeyapps.barcodescanner.DefaultDecoderFactory;

import java.util.Arrays;
import java.util.List;
import java.util.Locale;

/**
 * Standalone foreground camera-preview scanner.
 * Shows explicit camera-permission, preview and camera-error states rather
 * than silently returning from the default ZXing intent capture activity.
 * Only an exact public Xyool ID is returned. No auto calling or network IO.
 */
public final class QrScannerActivity extends Activity {
    public static final String EXTRA_ID = "org.xyool.connect.SCANNED_PUBLIC_ID";
    public static final String EXTRA_KEY_PIN = "org.xyool.connect.SCANNED_KEY_FINGERPRINT";
    private static final int CAMERA_REQUEST = 830;
    private static final int BG = 0xff0c1822;
    private static final int FG = 0xffe8f8f4;
    private static final int ACCENT = 0xff68dbc3;
    private static final int MUTED = 0xffb5c8ce;

    private DecoratedBarcodeView scanner;
    private TextView status;
    private Button settingsButton;
    private boolean isPreviewVisible;
    private boolean finished;
    private boolean torch;
    private boolean scanning;
    private final Handler ui = new Handler(Looper.getMainLooper());
    private final Runnable previewTimeout = () -> {
        if (!isPreviewVisible && !isFinishing() && !finished && scanner != null &&
            checkSelfPermission(Manifest.permission.CAMERA) == PackageManager.PERMISSION_GRANTED) {
            message("Camera preview has not started. Check Android's Camera access switch, close other camera apps, or tap Retry.");
        }
    };

    private int dp(int n) {
        return (int)(n * getResources().getDisplayMetrics().density + .5f);
    }
    private TextView label(String s, int size, int color) {
        TextView v = new TextView(this);
        v.setText(s);
        v.setTextSize(size);
        v.setTextColor(color);
        v.setGravity(Gravity.CENTER_HORIZONTAL);
        return v;
    }
    private void message(String msg) {
        runOnUiThread(() -> {
            if (status != null) status.setText(msg);
        });
    }
    private Button button(String name, LinearLayout parent, View.OnClickListener click) {
        Button b = new Button(this);
        b.setText(name);
        b.setAllCaps(false);
        b.setTextColor(BG);
        b.setBackgroundTintList(android.content.res.ColorStateList.valueOf(ACCENT));
        b.setOnClickListener(click);
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(-1, dp(50));
        lp.topMargin = dp(7);
        parent.addView(b, lp);
        return b;
    }

    @Override public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setStatusBarColor(BG);
        getWindow().setNavigationBarColor(BG);

        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setBackgroundColor(BG);
        root.setPadding(dp(14), dp(14), dp(14), dp(14));
        root.addView(label("Scan a Xyool ID", 23, FG));
        TextView directions = label("Point your camera at the other person's Xyool QR code.", 14, MUTED);
        directions.setPadding(0, dp(8), 0, dp(12));
        root.addView(directions);

        scanner = new DecoratedBarcodeView(this);
        scanner.setStatusText("Align the QR code inside the viewfinder");
        scanner.getBarcodeView().setDecoderFactory(
            new DefaultDecoderFactory(Arrays.asList(BarcodeFormat.QR_CODE)));
        scanner.getBarcodeView().addStateListener(new CameraPreview.StateListener() {
            @Override public void previewSized() {}
            @Override public void previewStarted() {
                isPreviewVisible = true;
                ui.removeCallbacks(previewTimeout);
                message("Camera ready. Scan the other phone's QR code.");
            }
            @Override public void previewStopped() {
                isPreviewVisible = false;
            }
            @Override public void cameraError(Exception error) {
                isPreviewVisible = false;
                ui.removeCallbacks(previewTimeout);
                message("Camera couldn't open (" + error.getClass().getSimpleName() +
                        "). Check camera access or tap Retry.");
            }
            @Override public void cameraClosed() {}
        });
        LinearLayout.LayoutParams preview = new LinearLayout.LayoutParams(-1, 0, 1f);
        root.addView(scanner, preview);

        status = label("Waiting for camera permission…", 13, MUTED);
        status.setPadding(0, dp(10), 0, dp(9));
        root.addView(status);

        button("Retry camera", root, v -> retryCamera());
        button("Flashlight on / off", root, v -> toggleTorch());
        settingsButton = button("Open camera permissions", root, v -> openSettings());
        settingsButton.setVisibility(View.GONE);
        button("Enter ID manually", root, v -> finish());

        setContentView(root);
        scanner.decodeContinuous(new BarcodeCallback() {
            @Override public void barcodeResult(BarcodeResult result) {
                if (finished || result == null) return;
                String raw = result.getText();
                if (raw == null) return;
                String value = raw.trim().toUpperCase(Locale.US);
                String id=value;
                String fingerprint=null;
                if(value.startsWith("XYOOL2:")){
                    String[] parts=value.split(":",-1);
                    if(parts.length!=3){
                        message("Unrecognized Xyool identity QR.");return;
                    }
                    id=parts[1];
                    fingerprint=parts[2].toLowerCase(Locale.US);
                    if(!fingerprint.matches("^[a-f0-9]{64}$")){
                        message("Invalid public-key fingerprint.");return;
                    }
                }
                if (!id.matches("^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$")) {
                    message("This is not a valid Xyool ID QR code.");
                    return;
                }
                finished = true;
                scanner.pause();
                Intent data = new Intent();
                data.putExtra(EXTRA_ID, id);
                if(fingerprint!=null)data.putExtra(EXTRA_KEY_PIN,fingerprint);
                setResult(RESULT_OK, data);
                finish();
            }
            @Override public void possibleResultPoints(List<ResultPoint> points) {}
        });
    }

    private void beginCamera() {
        if (finished || scanner == null) return;
        if (!getPackageManager().hasSystemFeature(PackageManager.FEATURE_CAMERA_ANY)) {
            message("Android reports no compatible camera. Enter the ID manually.");
            return;
        }
        if (checkSelfPermission(Manifest.permission.CAMERA) != PackageManager.PERMISSION_GRANTED) {
            message("Allow camera access to scan IDs.");
            requestPermissions(new String[]{Manifest.permission.CAMERA}, CAMERA_REQUEST);
            return;
        }
        settingsButton.setVisibility(View.GONE);
        isPreviewVisible = false;
        message("Opening the camera…");
        try {
            scanner.resume();
            ui.removeCallbacks(previewTimeout);
            ui.postDelayed(previewTimeout, 7000);
        } catch (RuntimeException e) {
            message("Camera startup failed (" + e.getClass().getSimpleName() +
                    "). Check camera access or tap Retry.");
        }
    }
    private void retryCamera() {
        if (scanner != null) scanner.pause();
        ui.removeCallbacks(previewTimeout);
        beginCamera();
    }
    private void toggleTorch() {
        if (!isPreviewVisible) {
            message("Wait for the camera to load before using the flashlight.");
            return;
        }
        try {
            torch = !torch;
            if (torch) scanner.setTorchOn();
            else scanner.setTorchOff();
        } catch (Exception e) {
            torch = false;
            message("Flashlight isn't available with this camera.");
        }
    }
    private void openSettings() {
        Intent intent = new Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS,
            Uri.fromParts("package", getPackageName(), null));
        startActivity(intent);
    }
    @Override protected void onResume() {
        super.onResume();
        beginCamera();
    }
    @Override protected void onPause() {
        ui.removeCallbacks(previewTimeout);
        if (scanner != null) scanner.pause();
        super.onPause();
    }
    @Override public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] results) {
        super.onRequestPermissionsResult(requestCode, permissions, results);
        if (requestCode != CAMERA_REQUEST) return;
        if (results.length > 0 && results[0] == PackageManager.PERMISSION_GRANTED) {
            beginCamera();
        } else {
            settingsButton.setVisibility(View.VISIBLE);
            new AlertDialog.Builder(this)
                .setTitle("Camera permission needed")
                .setMessage("Allow camera permission in Android Settings to scan a QR code. You can always type an ID instead.")
                .setPositiveButton("Open settings", (dialog, which) -> openSettings())
                .setNegativeButton("Not now", null)
                .show();
            message("Camera permission denied. Open permissions or enter the ID.");
        }
    }
    @Override protected void onDestroy() {
        ui.removeCallbacks(previewTimeout);
        super.onDestroy();
    }
}
