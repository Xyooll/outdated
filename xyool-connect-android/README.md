# Xyool Connect — Native Android app v0.1

**Standalone Android app** for the Moto G Power 5G (2024) XT2415V and other phones running Android 8+ (API 26+).

Unlike the companion browser version, this app is written in Java using the native Android UI toolkit. It does not use a website, WebView, Supabase, Google Play Services, any third-party SDK, or a server. The entire v0.1 UI runs offline.

## Included
- Native home and five-tab UI (Home, Phone, People, Messages, Avatar).
- Original 2D avatar rendered from Android Canvas shapes: skin, hair and shirt colors.
- Persistent local avatar name/appearance in private app SharedPreferences.
- Contacts stored locally within the app, with add/remove and confirm-before-delete.
- Phone number entry with native Android `ACTION_DIAL` handoff.
- SMS number entry with native Android `ACTION_SENDTO` and `smsto:` handoff.
- Erase local app data control.

## Not included yet
- No actual self-contained cellular dialer or SMS inbox. System apps perform calling and SMS, so this does not replace Android Telecom, Android's SMS provider, or the carrier.
- No SIP/VoIP, Xyool-to-Xyool voice or messaging, secure group chat, or push notifications.
- No NFTs, crypto wallets, gamification, online accounts or custom OS.
- No direct Android Contacts access/sync; contacts are in this app only.
- No network permissions. There is no internet connectivity in the native app.

## Security
- No runtime permissions are requested; in particular, **no INTERNET, CALL_PHONE, READ_CONTACTS, READ_SMS or SEND_SMS permissions**.
- `android:allowBackup=false`; installed app data stays in its app sandbox. Private preferences are not a general encrypted messaging store. Physical access to an unlocked device may expose the data.
- A call/SMS is not sent by tapping a Xyool button: the Android dialer/SMS composer opens, and the user must explicitly confirm there.
- Emergency calling must remain with the operating system's certified dialer. Never rely on this experiment for emergency calls.
- No root, Shizuku, bootloader unlock or custom firmware required.
- **Build provenance:** GitHub Actions builds a debug APK signed with a testing/debug key, not a production release signature. Distinct CI builds may use different debug keys, so uninstalling an old APK could be necessary to install a new one. That deletes locally saved Xyool contacts/appearance; export is a future feature. Only install artifacts from your own GitHub repository.

## Build on GitHub (no PC)
1. Open [GitHub Actions](https://github.com/Xyooll/outdated/actions/workflows/xyool-connect-android.yml).
2. Open the most recent `Build Xyool Connect Android` run. The automated workflow is triggered whenever files under `xyool-connect-android/**` change. Alternatively use **Run workflow**.
3. If the build is green, download the `xyool-connect-android-debug-apk` artifact ZIP, extract it on Android and tap `app-debug.apk`.
4. Android may ask to allow your file manager/browser to install unknown apps; authorize only the trusted APK from your repository. Android Play Protect may inspect the app.

For local builds using JDK17, Android SDK platform 35 and Gradle 8.9:
```bash
cd xyool-connect-android
gradle :app:assembleDebug
```

Output: `app/build/outputs/apk/debug/app-debug.apk`.

## Offline source and test status
The Java source, manifest, Gradle configs, and launcher vector icon are committed. Compilation is delegated to GitHub Actions; a **green run** is required before claiming an installable APK has been successfully built. On-device calling/SMS handoff and avatar persistence must be validated on the XT2415V.

The older web prototype stays separately available at `../xyool-connect/`. The unrelated Our Space project is untouched.
