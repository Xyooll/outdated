# Xyool Connect — direct cross-Wi-Fi calling lab

**Scope:** Test serverless WebRTC voice between two phones on separate Wi-Fi networks before integrating OpenDHT or other automatic peer discovery. This feature uses the existing signed, updatable Xyool APK identity; no new Android package is needed.

## How it works

- Open **Call by ID → Direct call lab · No Xyool server** on both phones.
- Both phones need Xyool IDs (created by the original Call by ID screen).
- Phone A enters Phone B's ID, taps **Create direct offer**, grants microphone permission, waits for the compressed `XYD1:` code, and shares it through a trusted out-of-band channel.
- Phone B selects **Paste received offer or answer**, pastes Phone A's code, confirms the caller, then waits for the **direct answer** code.
- Phone B shares its answer code to Phone A; Phone A pastes it into the same dialog.
- WebRTC tries ICE candidate pairs and carries encrypted audio DIRECTLY if it finds a reachable path. **No Railway, Xyool signaling server, or Xyool-owned media relay is contacted by DirectCallActivity.**
- The optional external STUN service defaults to Cloudflare `stun:stun.cloudflare.com:3478`; it can see connecting IP addresses. Set STUN to `off` through the Calling screen's Developer setup to disable it, but public NAT traversal may then fail.
- The **sharing channel** (SMS, messenger, direct QR transfer, etc.) may itself be an intermediary; this is not automatic decentralized discovery. The code contains public/private network addresses and WebRTC setup data. There is no token from Xyool's private account preferences in these codes.

## Important limitations

- **No guarantee across arbitrary networks.** NAT and firewalls may prevent a direct connection; no TURN fallback in this mode.
- **Codes are not cryptographically tied to Xyool identities yet.** An attacker changing the exchanged codes could impersonate peers or alter DTLS fingerprints. Exchange only with a trusted partner, and treat this as an alpha, not verified end-to-end authenticity.
- Both phone screens must remain available; no background ringing. The user should return to Xyool after sharing a code.
- This is a two-step manual P2P proof. The desired future UX is normal **Call → Answer**. Automatic address discovery through OpenDHT/libp2p and a genuinely decentralized identity system are **not implemented by this patch**.
- No emergency calling, traditional mobile numbers, or PSTN gateway.
- A built APK proves that Java code compiles; only tests between actual phones on different Wi-Fi networks can verify audio.

## Next milestones

1. Collect results showing which network conditions allow direct ICE (IPv6 global reachability vs NAT traversal).
2. Add Xyool identity public keys, signing/verifying call invitations, and fingerprint binding. Avoid relying on bare 12-character labels.
3. Integrate an Android-capable DHT/discovery transport with peer-to-peer bootstrap and self-hosted nodes, keeping any bootstrap directory optional and replaceable. OpenDHT and libp2p are candidates, **not yet dependencies**.
4. Automate connection negotiation and invitation delivery, implement background notification/ringing using Android Telecom, and restore failed calls.
5. Evaluate volunteer peer-bridge mode for networks that cannot connect directly. Bridges are network intermediaries even when not centralized and should not receive decrypted voice media.

This lab is deliberately kept separate from the existing same-Wi-Fi / optional Railway calling UI so the confirmed local call path is unchanged.
