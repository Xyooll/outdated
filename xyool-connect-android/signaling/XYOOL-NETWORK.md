# Xyool Network v0.1 — peer rendezvous network

Status: SOURCE + AUTOMATED FEDERATION TESTS PASS. NOT DEPLOYED AS A PUBLIC MULTI-NODE NETWORK. REAL TWO-PHONE CROSS-NETWORK AUDIO NOT VERIFIED.

## Architecture

- Every phone is its own client node. Phones are not required to host websites or relay strangers' media.
- Separate independently operated rendezvous nodes discover online phone identities through limited-hop presence gossip.
- Each Android phone connects to its preferred rendezvous node using the EXISTING WebSocket client protocol at /v1/id.
- Nodes exchange call invitations and SDP/ICE signaling using authenticated WebSocket peer links at /v1/mesh.
- WebRTC media travels directly between phones when possible; a separately provisioned TURN server is necessary on restrictive networks.
- This is a trusted operator federation inspired by BitTorrent discovery, NOT a public trustless DHT.

## Built and tested

- network-node.mjs: WSS-compatible existing Xyool ID registration and call event protocol.
- HMAC-authenticated peer links, presence gossip, bounded message forwarding, duplicate protection, heartbeats and route expiry.
- Ringing acknowledgment only once the receiver node processes the invitation, not at initial dialing.
- Call, incoming, ringing, accept, decline, hangup, SDP offer/answer, and ICE candidate forwarding.
- Local hashed identity token registry on persistent disk, optional detection of duplicate IDs on connected peer nodes.
- GET /health reports node health and neighbor count, not contact IDs.
- Automated real WebSocket tests across TWO and THREE nodes in test/network-node.test.mjs, and rejection of invalid mesh credentials.
- Dockerfile.network for separate deployment while preserving the older Railway server and Android app.

## Development

Requires Node.js 22+ and the existing signaling package's ws dependency.

    cd xyool-connect-android/signaling
    npm install
    npm run test:network
    npm test

On two independently hosted nodes, configure:

    HOST=0.0.0.0
    PORT=<hosting-provider-port>
    XYOOL_NODE_ID=<unique-node-name>
    XYOOL_ID_REGISTRY=/data/registry.json
    XYOOL_MESH_SECRET=<same-high-entropy-secret-32-or-more-chars>

On node B also configure:

    XYOOL_MESH_PEERS=wss://<node-A-hostname>/v1/mesh

Node B initiates the mesh connection to node A. The network node service requires a durable /data volume on Railway. Give each node its own persistent volume. Use the repository root as the Docker build context and Dockerfile.network at xyool-connect-android/signaling/Dockerfile.network. TLS/WSS should terminate at the hosting reverse proxy. NEVER commit the shared mesh secret.

The server listens on /v1/id for Android clients. Point the Android App A advanced signaling server to wss://<node-A>/v1/id and Phone B to wss://<node-B>/v1/id. Use Hybrid mode, open Call by ID on both phones, then test Call > Incoming Popup > Answer > Two-way Voice > Hangup. The existing APK wire protocol can use either node; no APK update is necessary to attempt this test.

Do not confuse an online call invitation with a successful ICE media connection. The relay is not built into the network node. Existing Android client supports an optional TURN URL and credentials, but there is no provisioned, tested shared TURN service yet. For calls across arbitrary restrictive networks, set up authenticated coturn/managed TURN with time-limited credentials. The network has NOT yet been deployed or real-device-tested.

## Known security limits

The federation trusts each operator holding one shared secret. Peer operators and intermediate nodes can see signaling metadata and SDP (which can reveal IPs). Device keys and SDP fingerprints are NOT yet cryptographically pinned end-to-end. The ID registration token is locally stored and remote presence collisions are only partly detected. Network partitions or malicious operators can allow collisions. No global identity registry, public DHT, unauthenticated volunteer peering, reputation system, spam defense, media relay, push notifications, or reliable Android background wakeup exists. Not an emergency calling service.

Do not deploy publicly to strangers as a secure calling platform yet. Build signed portable device identity and verified calls before exposing unrestricted peer federation.

## Next test milestone

Deploy two independently reachable rendezvous nodes; provide an authenticated TURN media relay; verify a real two-way voice call between two Android phones on separate networks. The receiving phone must currently keep the Call by ID activity open. Once the voice test succeeds, implement Android ringtone/answer/decline notification delivery and finally test sleeping-phone wakeups.
