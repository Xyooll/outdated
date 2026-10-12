# Deploy Xyool ID Calling on Railway (MVP pilot)

This is the Node WebSocket server that lets two Xyool phones **call each other's IDs**. It registers an ID with a private proof, notifies another online phone of incoming calls, relays call accept/decline and the WebRTC SDP/ICE handshake. **Actual microphone audio never flows through this signaling server.**

## Status

- The server source and automated protocol tests are in GitHub.
- A public server **has not been deployed** until a separate Railway deployment shows healthy, a domain is generated and both phones connect.
- This is a pilot, not a production-grade secure communications service. Calling over LTE/5G may also need a separate TURN relay; Railway hosts the signaling service, not automatically an inbound UDP TURN server.

## Deploy with the Railway app or website

1. Connect your Railway account and authorize deployment from **`Xyooll/outdated`**. Railway access is an explicit user action; Xyool doesn't need access to unrelated repositories.
2. Create a new Railway project named **Xyool Calling** with one service sourced from that repository's **`main`** branch. Set **Root Directory** to **`/xyool-connect-android/signaling`**. Railway should detect the `Dockerfile` in that directory. Keep **exactly one replica** because presence and sessions are in memory.
3. **Before enabling public traffic**, attach a persistent **Volume mounted at `/data`**. The service intentionally refuses to start on Railway without a volume so registered Xyool IDs aren't discarded on restart.
4. Configure the service variables: `NODE_ENV=production`, `HOST=0.0.0.0`, `XYOOL_ID_REGISTRY=/data/registry.json`. Railway will normally provide `PORT` dynamically; do not hard-code port 443 or create a public raw WS endpoint. The container has these defaults; explicitly set only if the host doesn't inherit them.
5. In the service's **Settings → Networking**, **Generate Domain** to obtain a `https://<your-service-domain>` address with TLS. Under the service healthcheck, choose **`/health`**. Enable/review spending limits, logs, and billing alerts; this is an always-on service, so ongoing hosting may cost money.
6. Confirm **`https://<your-service-domain>/health`** returns `{"ok":true}`. The Android signaling URL becomes **`wss://<your-service-domain>/v1/id`** (same hostname, WSS scheme and specific path).
7. For the first pair of phones, open **Xyool Connect → Call by ID → Developer setup** and enter that WSS URL on each device. Save and connect; status should become **Online**. Share only the **public Xyool ID** and use Call/Accept.
8. After checking stability, we can build the known server URL directly into the next Android APK and remove the need for any connection settings. We must implement **ID migration** before changing app signing/package IDs; reinstalling a different debug build can lose the old locally held identity secret.

The Railway root directory is important because this repository also contains unrelated Xyool software. Do not deploy the entire repository as a service.

## Persistent IDs and safe operation

The server keeps **only hashes** of 256-bit ID registration secrets in `/data/registry.json` (mode 0600) and current calls/presence in process memory. This small JSON registry is an MVP storage mechanism, not an audited identity database. Back up and protect the volume; if lost, previous registered IDs can be taken over on the replacement empty server by first registrants. A malicious user who learns an *unregistered* new ID could attempt to claim it first. Before public rollout, implement signed device keys, authenticated identity registration, backup/migration, rotating credentials, rate limits at the proxy, monitoring and privacy controls.

Health checks show that the server process is reachable. They do **not** mean two phones can exchange audio, nor certify that calls are end-to-end identity-verified. A server able to tamper with SDP could impersonate a call unless fingerprints are authenticated separately.

The current Android app must stay open to receive an incoming call. It does not support reliable background notifications. Calls can't replace regular/emergency cellular service.

## TURN is different from signaling

WSS signaling handles **finding a phone and arranging the call**. Two devices behind restrictive carrier NAT can negotiate successfully but **still have no media path**. Host a separate authenticated [coturn](https://github.com/coturn/coturn) relay (suitable provider permitting TURN UDP/TCP) with short-lived credentials. Avoid putting permanent shared TURN secrets in a distributed APK. Add server-issued expiring per-call TURN credentials before a wider rollout.

## Technical tests

From `xyool-connect-android/signaling` run `npm install && npm test`. GitHub Actions runs those tests automatically. This is an initial private alpha for two phones; do not rely on it for emergency calls.
