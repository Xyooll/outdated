# Xyool Hybrid Calling v0.6 — each phone is a local node

**Status: compiled engineering alpha; live two-phone audio not yet verified.**

## Actual behavior

Xyool Connect now creates an on-device, foreground-only calling node whenever its ID Calling screen is open on a Wi-Fi connection.

| Context | How it works | Central server? |
|---|---|---|
| Two Xyool phones on the same Wi-Fi | Each phone exposes a `ws://<local IP>:18788/xyool-lan-v1` call setup service and announces its Xyool ID using Android NSD/mDNS `_xyoolcall._tcp.`. Dialing a discovered ID uses a **direct phone-to-phone** WebSocket setup link and WebRTC ICE audio, with no Railway in the call path. | **No** for local call setup |
| Phones on different networks | If recipient ID is not discovered on LAN, the app connects to our default `wss://xyool-id-signaling-production.up.railway.app/v1/id` service to locate the other online ID and negotiate WebRTC. | Yes, *discovery and signaling only*; WebRTC attempts direct media |
| Restrictive cellular NAT/firewalls | WebRTC may require authenticated STUN/TURN servers. Currently optional user configuration; automatic secure short-lived TURN credentials have **not** been built. | TURN media relay only when needed |
| Nearby without a Wi-Fi access point | Future: Wi-Fi Direct, Android Nearby Connections or Bluetooth. | Not implemented |
| Distributed global ID directory (DHT) | Future: authenticated, privacy-preserving rendezvous/gossip or distributed directory. | Not implemented |

**Everyday UI remains Get ID → Scan QR or type ID → Call → Accept/Decline.** No user should manually exchange SDP, ICE candidates or server details.

## Phone-as-server design

- `LocalPeerNode.java` runs a local WebSocket server on Wi-Fi TCP port 18788, advertises the public Xyool ID over Android's NSD, discovers other Xyool services, and opens one-to-one WS signaling connections.
- `IdCallActivity.java` prefers a discovered nearby ID; otherwise it uses the hosted Railway WSS signaling server. Both paths use the same native WebRTC microphone/media engine.
- A Wi-Fi network can prohibit device-to-device traffic (guest network client isolation), and Android firewalls or VPNs can block local multicast/WebSocket discovery.
- For Rethink DNS or other VPNs, the app checks available underlying networks for Wi-Fi even if the VPN is the active/default network. A VPN may still block local peer traffic; users may need its **allow local network** option.
- This node is **not** a general-purpose HTTP server or web page. It does not open the device's SMS/cellular modem to public access.
- Node server and NSD discovery run only while the calling screen is visible. On stop, the node unregisters service, releases its multicast lock, closes WebSocket connections and ends local calls; this saves battery. **No background incoming calls yet.**
- Local calls without Railway still need the native app installed on **both** phones.

## Important security boundaries

- **Local discovery is not authenticated.** Another device on the same Wi-Fi could impersonate a public Xyool ID or alter plain LAN WebSocket signaling. WebRTC uses encrypted transport, but binding that transport cryptographically to the expected **person/device** is still missing. This is not verified end-to-end authentication. **Use only trusted Wi-Fi for LAN testing.**
- No certificates, identity keys or SDP fingerprint verification are yet pinned to public Xyool IDs; implement signed device keys before production or use on hostile shared networks.
- On LAN, any local machine can attempt a call to the device's public ID on port 18788 while its activity is running. Incoming calls require user acceptance. Rate-limit and abuse defenses are not yet production grade.
- The Railway ID server remains a single-instance experimental gateway; persistent IDs reside on its attached volume. Backups, identity recovery, call spam prevention, and server authenticity policies need additional engineering.
- No Google Play Services are required by the native app itself; Android OS/network components provide Wi-Fi discovery.
- Cellular phone-number dialing, SMS, and emergency calls still depend on the regular Android apps/carrier and are not replaced by local Xyool nodes.

## Two-device test on trusted home Wi-Fi

1. Install the Xyool **v0.6 Hybrid Alpha APK** on two Android phones and grant microphone permission when starting a call. It has its own test package `org.xyool.connect.hybridalpha`; old alphas stay installed and data is not migrated. **A new ID is generated for this test app.**
2. Put both phones on the **same trusted home Wi-Fi**; avoid guest Wi-Fi/client isolation. Open `Xyool Connect → Phone → My ID / Call a Xyool ID` on both phones and leave the screens open.
3. Wait for the status to show nearby phone discovery. Exchange or scan the public Xyool IDs.
4. Phone A enters B's ID → taps **Call**. Phone B sees **Incoming Xyool call**, taps **Accept**. Check two-way voice. Call status may show ICE `CONNECTED` if the media path forms.
5. If nearby discovery fails, verify local network access in any VPN/firewall application and try trusted Wi-Fi with LAN isolation disabled. Report exact status/crash behavior; don't infer a working call from a successful build.
6. Then test phones on different Wi-Fi/mobile networks through the Railway rendezvous gateway. This may still fail without TURN and cannot be considered production-ready.

GitHub Actions compiles the source and reports debug APK artifacts. **No physical two-phone test has yet been performed.**

## Build, license and support

- Native Android code in `app/src/main/java/org/xyool/connect/`; original WebRTC/Java-WebSocket/ZXing licensing must be preserved and included in release notices.
- Railway server source in `signaling/server-id.mjs` and `signaling/DEPLOY-RAILWAY.md`.
- Future milestones: stable Android APK signing and encrypted identity export/import; on-device keypair and verified fingerprints; call/QR identity verification; foreground phone call service/notifications; durable directory or DHT; server-less Bluetooth/Wi-Fi Direct setup; short-lived authenticated TURN credentials; routing, battery/network transition tests; accessibility.
