# v0.7 cross-network calling test

## Confirmed baseline
The user reported a successful Xyool voice call, with two-way audio, on one network. They also reported that calling **did not work across different networks**. No crash reports or connection-stage details were provided.

## Root-cause candidates
1. **ICE NAT traversal missing:** earlier app builds used zero STUN servers unless someone manually entered one. This means an internet-routed peer may have only local/private ICE candidates and may fail even though WSS signaling succeeds.
2. **TURN missing:** a STUN server alone is insufficient through carrier-grade NAT, symmetric NAT, some VPNs, and firewalls. A separate TURN relay with UDP/TCP/TLS endpoint, authenticated time-limited credentials and geographic/bandwidth planning is required for reliable cross-network calls.
3. **Signaling vs media:** if the other phone never rings or appears offline, check that both instances are running the ID Calling screen and the Railway WSS service is reachable. If Accept works but ICE fails/no audio, focus on ICE/STUN/TURN.

## Implemented in v0.7 alpha
- Cloudflare's documented public STUN endpoint `stun:stun.cloudflare.com:3478` is used **by default for internet calls only**, when no custom STUN is set. Same-LAN calls remain fully local and don't use this external STUN.
- Settings accept **off** to disable default public STUN. Cloudflare can observe the client's public IP when queried, but cannot read encrypted call audio; Xyool should provide a self-hosted alternative later.
- WebRTC `IceConnectionState.CHECKING` and `FAILED` now report a more helpful message, including relay requirement.
- Railway WSS signaling remains `wss://xyool-id-signaling-production.up.railway.app/v1/id`.
- v0.7 uses a **separate alpha package ID** `org.xyool.connect.crossnetworkalpha`, preserving any older app's local ID and contact data. The new test installation generates a new ID; both phones must test compatible releases and exchange their new public IDs.
- Existing QR fix remains part of this build.

## What this does NOT solve
- No configured TURN relay yet, no media-network performance guarantee, no reliable background ringing.
- Successful compilation or Railway /health response does not establish successful media over carrier NAT.
- Never rely on alpha calling for emergencies; default system phone/dialer is needed.
- An explicitly verifiable caller device identity and stable signed APK upgrades are not done.

## Next experiment
1. On each phone, install v0.7; open the calling screen and confirm it shows Internet calling online.
2. First phone stays on Wi-Fi, other on mobile data (or different Wi-Fi); both must have the app open. Enter ID, Call, Accept.
3. Record only the displayed status transitions, no private IDs/token/SDP. Distinguish `Ringing`, `Accepted`, `Trying direct encrypted audio`, `Connected`, and `Audio path blocked`.
4. If the call rings/accepts but media fails, deploy or provision a real TURN relay (a UDP-capable platform; Railway's public hosting does not support inbound UDP as of the cited October 2026 forum discussion). TURN credentials must be short-lived, served securely, and not hardcoded permanently into APK.
5. Test bidirectional audio and transitions on at least two different carrier configurations, then only mark as verified if the phones actually work.

Reference:
- https://developers.cloudflare.com/realtime/sfu/get-started/connection-patterns/ (Cloudflare public STUN address)
- https://www.rfc-editor.org/info/rfc8445/ (ICE candidate discovery)
- https://www.rfc-editor.org/info/rfc8656/ (TURN relays)
- https://station.railway.com/feedback/allow-outbound-udp-traffic-0f74101c (Railway inbound UDP limitation)
