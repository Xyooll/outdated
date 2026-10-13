# Xyool Connect — Decentralized-First Hybrid Bridge Plan

Status: **Android hybrid policy and privacy-safe diagnostics implemented for test**, not a fully deployed Web3 network. Web3 discovery, authenticated identity, volunteer relaying, and background ringing are **not yet implemented**.

## Architecture invariant

**Users own identities and each phone is a privately controlled node.**
Routing order is direct-first. Centralized Web2 services may only be optional, replaceable helpers, not compulsory authorities over contacts, identity, call media, or network participation.

| Capability | Existing Android implementation | Next milestone |
|---|---|---|
| Same-Wi-Fi local discovery and calling | LocalPeerNode mDNS/NSD + WebRTC | Authenticate LAN peers before using on untrusted Wi-Fi |
| Different-Wi-Fi direct voice | Manual offer/answer WebRTC ICE via DirectCallActivity | Test using ICE reports from two real networks |
| Automatic remote-ID ringing | Existing optional Railway Web2 WebSocket signaling | Independently operable Web3 peer rendezvous |
| Direct-only sovereign mode | BridgePolicy mode disables Railway; LAN and manual P2P work | Add reachable IPv6 and automatic DHT lookup |
| NAT traversal | WebRTC ICE + external STUN by default (opt-out) | Determine real-world success matrix, add peer-reflexive/IPv6 diagnostics |
| Relay fallback | Not deployed | Voluntary community-hosted TURN/peer relay with consent and E2EE identity verification |
| Cryptographic ID authentication | **Not implemented**; XY labels are not proof of identity | Android Keystore-generated keys, public-key contact verification, signed and expiring peer records |
| Background phone ringing | Not implemented | Android Telecom integration and user-selected background notification transport |

## Request flow

1. Determine user-selected **direct-only** or **hybrid** policy before any network calls.
2. Attempt mDNS/local peer when both phones are nearby.
3. Try direct IPv6/WebRTC ICE using an authenticated, expiring invitation received over an available decentralized rendezvous network (future).
4. If ICE cannot complete, optionally try a consented independently operated peer bridge (future).
5. If user selected **hybrid**, allow an interchangeable Web2 signaling provider; voice still attempts direct ICE first and uses any explicitly configured TURN only if permission and credentials are available.
6. Report the **observed** path. Do not infer that ICE candidate discovery means connectivity; do not claim data passed P2P if using a relay.

## Candidate Web3 signaling backends (research, not integrated)

- **Waku**: decentralized message routing for call invitations and replies. Android support, mobile resource requirements, bandwidth, network stability, spam defense, delivery acknowledgment and available operator coverage require a prototype and measurements.
- **OpenDHT/libp2p**: authenticated peer records and reachability discovery. Android integration and open bootstrap/peer discoverability still require validation.
- **Nostr**: interoperable relay federation, but use NIP-17/44 encrypted and authenticated messages for personal call invitations. Plaintext events leak call data and metadata; Nostr relays are still intermediaries and may censor/drop events.

Avoid inventing a bare public `XY-XXXX-...` routing topic or publishing live IP addresses, WebRTC SDP, or call invitations to public unencrypted topics. Use opaque inboxes and authenticated, short-lived records. Blockchain/NFT usernames must stay **optional**, and never carry live voice or sensitive signaling in a permanent ledger.

## Testing to do next (two phones, separate networks)

* Install same current GitHub test-signing APK on both devices.
* **Test 1 — direct-only**: open **Direct call lab**, exchange two codes, and try audio. Use **Copy direct connectivity diagnostic** on each phone. Reports must show ICE state, candidate classes and counts, not addresses.
* **Test 2 — hybrid**: attempt normal Call by ID while both on separate Wi-Fi. If the other phone rings and accepts but audio fails, the key blocker is ICE connectivity, not signaling. If the phone never rings, inspect registration and ID state.
* **Test 3 — NAT variation**: repeat with one device on cellular/mobile hotspot; compare IPv6 candidate counts, STUN candidates, and ICE state without collecting IPs.
* **Pass criteria**: successful two-way audio between separate networks, using either confirmed direct ICE or explicitly opted-in and identified relay path. No incorrect claims about topology.
* **Fail safely**: no silent mode downgrade, no untrusted arbitrary signal relaying, no recording or publishing personal network addresses, no false claims that ringing will work with the app closed.

## Order of work after ICE testing

1. Harden identity and signed/expiring WebRTC invitations (authentication before opening public rendezvous).
2. Build a single replaceable `RendezvousTransport` adapter behind call setup with one mobile-friendly decentralized implementation, plus signed-message replay protection, short TTL, delivery ACK, and spam limits.
3. Test Web3 network from devices on different consumer ISPs; measure wakeup latency, failure rates, battery, missed rings.
4. Make multiple independent peer rendezvous providers possible, and add voluntary relays for failures without forcing a centralized vendor.
5. Use Android Telecom + foreground service/background notification policy to achieve an ordinary Call → Answer experience.

Evidence targets: `BridgeSelfTest` runs in GitHub Actions for deterministic route decisions and report privacy, and Android APK build verifies package and permanent test certificate. No real-device cross-network voice success is yet asserted.
