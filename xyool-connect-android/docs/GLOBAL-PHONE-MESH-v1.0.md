# Xyool Connect Global Phone Mesh v1.0 (experimental)

**Deployment status: live bootstrap release must be checked independently. Automated tests do not prove cellular/Wi-Fi calls.**

## What is now implemented

- Each phone can host a local, signed WebSocket/NSD signaling node on trusted Wi-Fi. An opt-in Android foreground service can retain this role when the calling UI closes, while Android allows the process to run.
- Each phone can become a **global WebRTC data-channel node** using signed registration at a trusted Xyool rendezvous server. A bounded ring-sampling algorithm recommends peers; phones negotiate their DTLS-protected direct data channel using authenticated P-256 SDP/ICE messages forwarded through the rendezvous.
- Peers on different trusted **federated rendezvous servers** can discover and bootstrap a direct WebRTC connection using `mesh-presence` gossip and signed `mesh-signal` messages over `/v1/mesh`. Multiple servers are optional but each must be deployed and configured with the same **private** federation operator secret. No federation secret is included in the APK.
- A real direct data channel can remain connected when the rendezvous socket disconnects: the bootstrap server is not the transport for direct control packets.
- The phone can send a signed and time-bounded **ping/pong reachability packet** toward a paired Xyool ID, and can opt into forwarding those packets up to **3 hops** over as many as **3 direct peer connections**. Relayed control messages have a 4 KiB maximum frame size and explicit buffer/rate controls. Neither voice data nor arbitrary Internet traffic is forwarded.
- The receiver requires a matching public-key fingerprint previously pinned from the other phone's `XYOOL2` identity QR. The relay verifies packet signatures but cannot treat a self-declared user ID alone as verified. Server enrollment persists each node's signed public key fingerprint alongside the legacy ID registry.
- Existing Xyool voice calling still uses local P2P WebRTC or the ordinary rendezvous signaling channel, with direct ICE media preferred and manual TURN fallback. **Voice does not traverse the three-hop data relay.**

## What this is not

This is a **working-source overlay and automated federated test implementation**, not a production-scale untrusted Kademlia DHT, anonymous overlay, always-on mobile daemon, or self-hosted TURN network. Server and client code have CI test coverage, but reliable real-device end-to-end behavior has not been independently verified.

The initial peer roster depends on an operator-controlled server. Subsequent transport uses direct WebRTC channels when those channels succeed. This is decentralized-first at the transport layer **after bootstrap**, centralized-second at discovery. The trusted federation prototype is operational in automated tests, but other public federation nodes are not deployed by this code.

The operator can see bootstrap participant IDs, IP addresses, and WebRTC ICE/SDP metadata. Third-party forwarding is opt-in; hop-level DTLS encryption does not provide end-to-end confidentiality of intermediate control frames. Calls still require device-to-device WebRTC media and TURN on restrictive NATs.

## How to test

1. Install the same signed ARM64 APK on two Android phones. Scan one another's new **Show my QR code** output, which pins the corresponding key.
2. Enable **Background call alerts** on each phone. In **Advanced network settings**, turn on **Mesh forwarding** only if you want the phone to forward capped reachability probes for other peers. An ongoing system notification indicates the service.
3. Join unrelated networks: cellular for one phone and Wi-Fi for the other. Verify that the configured Xyool rendezvous supports `mesh-enable`, `mesh-peers`, and signed `mesh-signal`.
4. Copy the other person's ID into the calling field. Use **Probe entered Xyool ID through peer mesh**; watch the status for an authenticated pong. A successful direct data-channel setup may require TURN if both cellular connections are behind restrictive NATs.
5. Call normally, answer/decline, hang up, and test two-way audio. Call signaling is still routed through the rendezvous (or local Wi-Fi node), even when mesh probe routing works.
6. Disable data, switch Wi-Fi, lock the screen, and kill the app to document OS limitations. A force-stopped Android app cannot be guaranteed to ring.

## Gate to truly 'full'

The remaining work is user-consented **end-to-end encrypted call signaling over signed phone routes**, authenticated arbitrary peer discovery without a required operator directory, production multi-relay deployment with bandwidth quotas, automatic short-lived TURN credential provisioning, and actual multi-phone validation. A full distributed routing protocol also needs partitions/rejoin, abuse resistance, key recovery, maintenance, and a scalable peer table.

Do not advertise this as an emergency dialer or as anonymous messaging.

## Automated checks

- `npm test`: current ID signaling, signed overlay, and fair peer-sampling tests.
- `npm run test:network`: 2–3 node authenticated federation and signed overlay signaling.
- Android CI: signed ARM64 APK compile, WebRTC library and signing key verification, rendezvous pool Java unit tests.
- Broad unrelated Python checks remain known red due to missing `requests` and `alpaca` dependencies.
