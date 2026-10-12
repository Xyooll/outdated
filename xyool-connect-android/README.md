# Xyool Connect — ID-to-ID Calling v0.4

The normal workflow now is **Get ID → Share ID → Enter another ID → Call → Accept/Decline**. No manually exchanging WebRTC offers, SDP, network candidates, meeting links, or long secret rooms. The old diagnostic tools remain under **Phone → Advanced SIP / diagnostic calling**.

## What is actually available

- A first-run Xyool ID such as `XY-ABCD-EFGH-JKLM`, randomly generated and stored in private Android preferences.
- A separate 256-bit secret stored in the app to authenticate ID ownership with the Xyool server. The secret is **not** displayed or shared with contacts.
- A dedicated **Call by ID** screen with Copy/Share ID, Call, Hang up, Mute, and incoming Accept/Decline dialog.
- Xyool's Node signaling service `signaling/server-id.mjs` supports durable ID registration, caller lookup, incoming-call delivery, call state, and automatic WebRTC offer/answer/ICE candidate relay.
- The actual voice is still built on the native WebRTC audio engine and DTLS-SRTP. Calls and audio are not recorded by this service.
- Ordinary carrier telephone calls/SMS and optional SIP fallback are retained.

## Important: no live server yet

**This is a completed compiled APK prototype, not yet a completed global calling network.** Currently the app can generate your ID offline, but **ID calls cannot connect until the separate Xyool signaling server is deployed behind HTTPS/WSS** and configured in Connection settings. There is no public Xyool service endpoint hardcoded into the APK, and GitHub Pages cannot host this WebSocket service.

**First setup on your own server:** start the Node 20+ process `node signaling/server-id.mjs` behind a TLS/WSS reverse proxy. WSS endpoint must be `wss://your-domain/v1/id`. Run coturn for relay-capable calls across carriers. Once a real endpoint exists, the next APK will ship with it preconfigured so nobody needs to type a server address.

The signaling server is independent of the existing Our Space Supabase project and does not alter its two-person authorization/database.

## Initial two-phone alpha test

1. Install the v0.4 debug APK on both Android phones. Note it uses the **same app ID as v0.3** but the CI debug signature can vary, so an existing v0.3 might fail to upgrade. Uninstalling v0.3 would erase that alpha's locally saved contacts and settings. Back up important information manually first.
2. Open Xyool Connect → **Phone → My ID / Call a Xyool ID**, then **Connection settings**.
3. Enter the same deployed Xyool WSS URL on both phones; optional STUN and authenticated TURN as needed.
4. Both phones must stay in the calling screen, online. Share the caller/recipient's Xyool ID (not the secret).
5. Enter the recipient's ID and tap **Call**. Recipient taps **Accept**. The app automatically negotiates WebRTC media. Check two-way audio on same Wi-Fi, then across different Wi-Fi/mobile networks.

**Not working yet:** incoming calls while app closed, reliable push notifications, identity verification against malicious signaling, persistent accounts across reinstall, easy ID recovery/migration, global signaling hosting, deployed TURN, self-hosted SIP-to-phone-number gateway, call quality verification or emergency dialing. The ID owner secret is stored in private preferences but not Android Keystore hardware-backed encryption. A compromised unlocked phone can still compromise its credentials. Never use this alpha for emergency calls.

## Server ownership and security

`signaling/server-id.mjs` persists SHA-256 hashes of ID-authentication tokens in a private local JSON file, not raw tokens, and accepts only one currently connected socket per ID. Protect and back up this registry; a lost registry permits unauthorized first-claim of a known ID. This alpha relies on WSS/TLS authentication of the server; its WebRTC media is encrypted but identity-binding/verified peer fingerprints are still missing. The server is single-instance and requires rate-limits, abuse controls and audits before exposure to the public.

GitHub Actions tests confirm registration, ID ownership, call delivery, accept/reject, SDP/ICE relay and offline/busy errors. Green tests are **not** proof of working voice over real devices. Physical two-way calls have not been tested.

---

# Xyool Connect Native Voice Alpha — Android v0.3

This **separate Android install** is Xyool's first built-in native microphone-to-speaker WebRTC calling implementation. Package ID: `org.xyool.connect.nativealpha`. Previous v0.1 and v0.2 apps are left installed and their private contacts/avatars are not migrated.

## What is new

- **Xyool native P2P voice:** Direct WebRTC audio, independent of Jitsi rooms or Linphone's SIP app. PeerConnectionFactory captures microphone audio, creates SDP offers/answers, negotiates ICE connectivity and delivers DTLS-SRTP-protected audio. WebRTC supplies mature cryptography, network stack and Opus codec, not a new unreviewed cipher.
- **Manual P2P pairing:** Caller creates offer and privately sends a long `XYOOL1:` setup message. Receiver pastes offer, creates and sends answer. Caller pastes answer. When ICE connects, both should be able to talk if media/network permission and routing are functional.
- **Self-hosted Xyool signaling pairing:** The Android app can instead connect to your `wss://your-domain/v1/voice` with a randomly generated 128-bit bearer room secret, then exchange offer/answer automatically. See `signaling/README.md` for the Xyool signaling server. **No public hosted Xyool signaling server exists yet.**
- Optional user-configurable STUN and TURN server connection settings. There is no mandatory Google account or preset Google STUN service.
- Legacy Android cellular/SMS handoff, avatar, local contacts, Jitsi fallback and SIP-app fallback from v0.2 stay present.

## Important limits before real testing

- This is **not** a finished communications app, phone service, native SIP dialer, verified E2EE, or replacement for emergency calling.
- Android requires microphone consent. The app has `INTERNET`, `RECORD_AUDIO`, and `MODIFY_AUDIO_SETTINGS` permissions for native voice, but **no** `CALL_PHONE`, `READ_CONTACTS`, `READ_SMS`, or `SEND_SMS` permissions.
- The app uses microphone in the foreground; moving it to background may interrupt voice because a properly designed Android foreground-service calling subsystem isn't built yet.
- Direct audio is encrypted with WebRTC DTLS-SRTP, but **identity/fingerprint authentication is not implemented**. Attackers controlling the signaling route could impersonate a peer. Do not discuss sensitive information until authenticated calling is implemented.
- SDP offers and answers can contain private/public IP metadata. Distributing a setup message, room secret or TURN credentials publicly is unsafe. Servers/peers handling signaling can see some metadata.
- On some Android/carrier NATs, direct peer-to-peer calling fails without an authenticated TURN relay. A TURN relay is not free in operating costs, although [coturn](https://github.com/coturn/coturn) itself is free and open source.
- Xyool-to-Xyool call invitation is not an ordinary phone number. SIP/PSTN calls still require a SIP provider or gateway. Emergency calling continues through Android's proper dialer.

## Test on two Android phones without an internet server

1. Install the **v0.3 Alpha** APK on both phones. Keep your existing Motorola dialer installed.
2. Put both phones on the same Wi-Fi network; open Xyool Connect Native > Phone > Xyool voice / SIP calls > Xyool native voice.
3. Leave STUN/TURN settings blank (LAN test only). On phone A select **A · Create offer (caller)** and grant microphone access.
4. Wait for ICE gathering to finish, then copy/share the full `XYOOL1:` offer with phone B through a trusted channel.
5. On phone B paste the offer and tap **B · Accept pasted offer (receiver)**. Grant microphone permission and wait for its `XYOOL1:` answer.
6. Send/paste the answer back to phone A and tap **A · Complete with pasted answer**.
7. Look for `ICE connection: CONNECTED`, test two-way microphone/speaker audio, mute/hang-up behavior, and re-test with Wi-Fi/mobile networks. Do not conclude success based only on successful compilation.

## Test with your own server

1. Deploy the `signaling/` Node service behind a TLS reverse proxy, and configure TURN when needed.
2. Both phones enter the same `wss://your-domain/v1/voice` URL and securely shared room code generated with **Generate private room code**. Select caller/host on one and joiner on the other.
3. The Xyool server relays the offer/answer; media still flows via WebRTC, not through the signaling server.
4. Call states, microphone, network transitions, identity verification, reconnection and a real carrier-network test remain pending.

## Implementation, licenses, and provenance

- **Xyool-specific code**: Android Java native UI, state machine, call setup helpers, self-hostable WSS signaling server, room-code generation and tests live in this repository.
- **WebRTC Android**: `io.github.webrtc-sdk:android:150.7871.01` (BSD 3-Clause; upstream: https://github.com/webrtc-sdk/android). Review third-party notices and native dependency licenses for redistribution.
- **Java-WebSocket**: `org.java-websocket:Java-WebSocket:1.6.0` (MIT).
- **Xyool signaling server**: Node.js + pinned `ws@8.18.3` package (MIT).
- **Research references**: https://github.com/jitsi/jitsi-meet (Apache 2.0), https://github.com/BelledonneCommunications/linphone-sdk (GPL/AGPL dual license), https://github.com/coturn/coturn (3-Clause BSD-style). We studied these components; their source has **not** been copied or relicensed into Xyool.

The GitHub Actions workflow compiles this APK. The signaling workflow executes isolated room/relay tests. **Both green jobs do not establish that physical two-way calling works.** Never use an experimental app as your only means of emergency contact.

---

# Xyool Connect Calls Beta — Android v0.2

This standalone native Android app can coexist with the original `org.xyool.connect` v0.1 debug APK. Its temporary application ID is `org.xyool.connect.callsbeta` because GitHub-hosted debug builds do **not** yet share a stable production signing key, and replacing the original might lose locally stored contacts.

## Working calling paths

- **Cellular**: launches Android's normal dialer with `ACTION_DIAL` (you place the call using your carrier).
- **SMS**: opens Android's native text composer with `ACTION_SENDTO`.
- **Xyool-to-Xyool voice invitations**: generates a cryptographically random 128-bit Jitsi meeting path, lets you share it, and opens the actual Jitsi voice/video service. The organizer must usually authenticate on public meet.jit.si; invitees can join without signing in. Both people connect through Jitsi, **not yet a native, Xyool-owned WebRTC network**. Disable the camera for audio-only use. Public service infrastructure can see metadata, and end-to-end encryption is NOT asserted.
- **SIP internet calls**: accepts a SIP address (`user@sip.example.org`) and hands it to an installed SIP app through an Android `sip:` intent. A SIP account and SIP provider/endpoint are required. SIP-to-ordinary-phone number calls typically need a paid gateway.

## Installation (no PC)

GitHub Actions builds a signed development APK on every update to `xyool-connect-android/`. From [Android build workflow](https://github.com/Xyooll/outdated/actions/workflows/xyool-connect-android.yml), open the successful run and download `xyool-connect-android-debug-apk`. Extract the ZIP, then install `app-debug.apk`.

The Xyool Connect Calls Beta APK runs next to the v0.1 APK without uninstalling the old app. Contacts and avatar settings are private per app; they don't automatically migrate. Until we establish a durable user-controlled release signing key, later debug builds may need to be installed alongside or uninstalled/reinstalled. Never delete the old app without preserving data you still need.

No microphone permission is requested by Xyool Connect itself: the external Jitsi browser/app or installed SIP client asks for microphone permission and actually carries the call.

## Real-world tests to perform on two phones

1. Install the same Xyool Connect Calls Beta on both phones.
2. On phone A: Phone > Xyool voice / SIP calls > Create new voice invite > Share invitation.
3. Send the invitation privately to phone B; both phones open the room link. The first participant authenticates if Jitsi requests it. Turn off cameras for voice-only.
4. Confirm audio in both directions, hang up, check network interruptions and headset routing. No connection claim is made before these are tested.
5. For SIP: configure a Linphone (or other SIP) account on each phone, enter the other's SIP URI in Xyool and tap Call with installed SIP app. Test registration, outbound/inbound voice, and provider charges.
6. Verify normal Android dialer, SMS, contact storage, and avatar customization still work.

## Deliberate limits

Jitsi links are **bearer invites**: anyone who receives one may try to enter the meeting, subject to Jitsi lobby controls. Treat invites as private. This beta does not support direct incoming call ringing, phone-to-phone presence, push notifications, persistent Xyool account identities, dedicated signaling/TURN, or native E2EE voice. A separate backend and reviewed WebRTC engine are required for that. No emergency calls are handled by the beta.

---

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
