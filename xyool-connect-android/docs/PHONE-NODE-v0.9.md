# Xyool Connect: phone-node network (v0.9 alpha)

## Actual state — do not confuse node capability with a public DHT

This alpha **hosts a real local WebSocket + NSD phone node** on trusted Wi-Fi while the Xyool call UI is open. When the user explicitly enables Background Call Alerts, `CallReachabilityService` owns that local node and can keep it alive with an ongoing foreground notification even after the UI closes. Android can nevertheless restrict or stop it.

The same Android service connects outward to one of up to five explicitly configured **trusted** `wss://.../v1/id` rendezvous nodes. It rotates to another address after a failed connection and eventually retries. That makes the user less dependent on a *single* hostname when the operator provides additional endpoints, but it is **not** a multi-active global phone-to-phone routing mesh, and relay hosts are not deployed automatically.

The repo has a separate three-server *trusted* Xyool federation prototype in `signaling/network-node.mjs`, with automated peer-network tests. Operator node-to-node `/v1/mesh` links require a private shared secret and server deployment. Phones do **not** join that protocol as untrusted public routers; publishing the operator secret inside an APK would compromise the network.

## Device identity upgrade

- AndroidKeyStore P-256 keypair: private material is nonexportable through app APIs; actual hardware backing is device-dependent.
- `Show my QR code` now encodes `XYOOL2:XY-....:<sha256 public key fingerprint>`, not the account token.
- Scanning the new QR securely *pins the observed fingerprint*, so future signed LAN calls from that ID must use that device key.
- Local Wi-Fi invitations and signaling frames carry signatures bound to the caller identity, per-call nonce, and increasing frame sequence numbers.
- Legacy ID-only QRs still work as IDs, but first contact is **trust on first use**, not verified identity. Share the new QR in person or via an already trusted channel to prevent active first-contact substitution.
- Old clients that use the unsigned LAN protocol cannot make local direct calls to the new authenticated LAN listener until updated. The internet rendezvous protocol is unchanged.
- **Limit:** The public ID/token-based Internet registration is not cryptographically bound to a device key. Relay operators and initial rendezvous remain trusted with signaling metadata and credential handling. Verified local QR pinning must not be advertised as securing the global federation.

## User controls

Under Advanced network settings, choose Direct-only (no hosted discovery) or Hybrid. Additional WSS nodes must be operated by parties you **trust**, because the present `/v1/id` protocol submits the same long-lived Xyool registration token on every selected server.

Background node is **OFF by default**. The user must grant notification permission, start the foreground service from the visible app, and may disable it any time. This turns off local discovery and background rendezvous. The app does not silently proxy third-party calls or route Internet traffic for strangers.

## Remaining to call it a full global BitTorrent-style node

1. **Signed global identity**: challenge-based registration and per-device signatures, independent of server operator; key rotation/recovery and ID collision controls.
2. **Authentic distributed peer discovery**: DHT/Kademlia or signed peer-record gossip implemented on mobile and wired to bootstrap peers (not only federation servers), with TTLs, anti-Sybil and memory limits.
3. **Private mobile NAT traversal**: WebRTC peer data channels, ICE/STUN/TURN, signed SDP/fingerprint pinning, no inbound public listening assumed on consumer cellular CGNAT; relay fallback with expiring credentials.
4. **Optional consent-based encrypted relaying**: phones choose explicit bandwidth/CPU/battery quotas, hop limits and permissions. Third-party traffic is encrypted and cryptographically authenticated; no open proxies, unsolicited file sharing or exposing the private zone.
5. **OS lifecycle**: incoming call delivery and active audio must survive lock screen, network handoffs, and realistic Android 14+ foreground-service restrictions; don't pretend an alarm can bypass OS background limits.
6. **Deployment**: at least two independently operated public rendezvous/relay nodes and one TURN pilot; check identity pinning, direct vs relay ICE paths, bandwidth, costs, abuse, denial-of-service and restore behavior.

## Current acceptance gates

- CI: `Build Xyool Connect Android` assembles a signed ARM64 APK, runs bridge and bootstrap unit tests, verifies native WebRTC library and signing key. `Test Xyool Peer Network` exercises trusted federation including multiple nodes. These tests do **not** exercise real Android background behavior or DHT.
- Must be tested with two phones running the same new APK: (A) QR scan, (B) same trusted Wi-Fi in foreground, (C) incoming ringtone while UI closed with node enabled, (D) answer/decline/hangup, (E) cellular/Wi-Fi cross-network with deployed TURN pilot.
- Not an emergency dialer.
