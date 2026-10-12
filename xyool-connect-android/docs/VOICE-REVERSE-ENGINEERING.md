# Xyool Connect: reverse-engineering and ownership map (2026-10-12)

## Goal and definition of "ours"

Build a Xyool-controlled, reproducible, Google-account-free Android communications stack. We must own the app UI, peer identity, invite protocol, call state machine, signaling deployment, storage rules, service selection, update/signing infrastructure, security testing and recovery procedures. We can depend on interoperable, licensed open-source engines; we do **not** need to reinvent cryptography, codecs or network standards. Owning source and the right to run/fork components is different from writing each dependency from scratch.

This is a **source-level architecture review**, not a decompilation of proprietary binaries. We examined published open-source repositories and designs. No upstream Jitsi, Linphone, or WebRTC code has been copied and relabeled as proprietary Xyool code.

## 1. Decompose three systems

| Reference | Underlying mechanisms | Xyool decision |
|---|---|---|
| [Jitsi Meet](https://github.com/jitsi/jitsi-meet), Apache-2.0 | User-facing calling and conference management, rooms/invitations, video, multiple media/session components; self-hostable conferencing | Keep as an optional compatibility fallback; not our basic phone-to-phone engine. Study call UX, TURN/SFU, meeting lifecycle and abuse controls. |
| [Linphone SDK](https://github.com/BelledonneCommunications/linphone-sdk), GPL/AGPL dual license (commercial alternative) | SIP account registration and signaling, SIP user-agent stack belle-sip, Mediastreamer2, oRTP, audio devices and codecs | Use for eventual native SIP/PSTN integration only if we can comply with the applicable copyleft and redistribution obligations. Currently the beta delegates SIP links to an external app. |
| [WebRTC](https://webrtc.googlesource.com/src/), [Android distribution](https://github.com/webrtc-sdk/android), BSD-3-Clause with third-party notices | PeerConnection, ICE path finding, STUN/TURN interaction, DTLS-SRTP media protection, Opus audio, JNI audio engine | The v0.3 alpha embeds the Android WebRTC library. Xyool owns the app interaction, handshake, peer state and signaling protocol. |
| [coturn](https://github.com/coturn/coturn), BSD-style license | TURN/STUN relay to connect users behind carrier-grade NAT and restrictive firewalls | Self-host authenticated TURN with expiring credentials when deploying internet calls. Not deployed in v0.3. |

## 2. Construct a Xyool call

1. **Identity / address book**: initial alpha generates a temporary 128-bit secret room code. This is not verified user identity. Future: authenticated device keys, verification and call permissions.
2. **Signaling**: optional Xyool `signaling/server.mjs` receives `join`, `offer`, `answer`, `candidate`, emits `peer-ready` and `peer-left`; pairs only two clients with matching room secret. Enforce WSS/TLS at deployment. Current alpha can also exchange signed-by-nobody SDP messages manually over a trusted external channel.
3. **Media**: Android `NativeVoiceActivity` creates `PeerConnectionFactory` and microphone audio track. WebRTC negotiates ICE and uses DTLS-SRTP to encrypt the peer connection.
4. **Traversal**: local LAN candidates can work without a server. Internet connectivity requires STUN or TURN in many cases, particularly across mobile carriers. Users configure ICE servers; none are silently hard-coded to Google.
5. **Call control**: the alpha exposes start/answer/hang-up status and leaves cellular/SMS to stock Android. It lacks reliable ringing, resume/background service and device audio routing UI.
6. **Ownership**: Xyool retains source, deployable signaling, chosen servers, native UI, and build pipeline. We will not force the public Jitsi infrastructure or third-party SIP apps for Xyool-to-Xyool voice once native testing passes.

## 3. Security defects and tests we must not skip

- **Authentication gap**: WebRTC DTLS-SRTP protects transport, not peer identity. A compromised signaling service could substitute keys/SDP. Implement account/device public keys and bind the call fingerprint to a verified contact key; independent review before claiming verified E2EE.
- **Network metadata**: SDP often exposes candidate IP information. TURN relay-only ICE helps hide endpoints from one another but creates server bandwidth cost.
- **Secret room token**: 128-bit randomness prevents practical guessing, but whoever receives the invitation can try to join. Bind invites to authenticated users, expire rapidly and enforce consent.
- **Server hardening**: currently in-memory 2-peer room service with limited message size, protocol checks, heartbeat, expiry, simple rate protection and no recording. Missing production TLS termination, reverse proxy abuse controls, horizontal scaling, observability and security audits.
- **Device compatibility**: test physical Moto XT2415V microphone playback, Bluetooth, speakerphone, headset route, Android 14 background behavior and interruptions.
- **Telecom responsibilities**: real default dialer replacement and SMS access require Android roles and platform integration. Normal PSTN and emergency calls are separate and cannot be assumed to work through the experimental network.

## 4. Verification ledger

- PASS: GitHub Actions compiles the native Android source with the WebRTC audio dependency; debug artifact produced.
- PASS: Node signaling tests exercise two-party offer/answer relay, third-peer rejection, invalid token rejection and room isolation.
- NOT TESTED: Android hardware peer-to-peer bidirectional audio.
- NOT DEPLOYED: Public WSS signaling, authenticated TURN, production SIP interconnect.
- NOT BUILT: Durable identities, contact ringing/presence, encrypted chat, verified E2EE, foreground service, production key signing, formal threat-model audit.

## 5. Next closed-loop milestones

1. Two physical Android phones exchange a manual SDP offer and answer on the same WLAN. Verify ICE `CONNECTED` and both directions of audio. Capture local non-sensitive crash diagnostics for fixes.
2. Deploy a Xyool-owned WSS endpoint and coturn on infrastructure under our control, securely provision time-limited credentials. Repeat the call on Wi-Fi and on separate mobile carriers.
3. Add durable signed identities and short-lived invite capability, authentication-bound SDP fingerprint verification and privacy controls.
4. Build native ringing/answer/reject, contact discovery, Android foreground service with audio focus/headset/Bluetooth routing, lifecycle recovery and accessibility.
5. Only after these pass, evaluate a GPL-compliant native SIP stack or a self-hosted SIP gateway for phone-number dialing; keep emergency calls delegated to the tested system phone app.

**Current maturity: engineering alpha, NOT an independent production phone network.**
