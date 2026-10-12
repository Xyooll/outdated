# Xyool Voice Signaling (experimental, self-hostable)

This is **Xyool's own** lightweight, ephemeral two-person WebRTC signaling service.

It isn't a Jitsi server, SIP provider, media relay, TURN server, contact directory, or phone-number gateway. It carries only room join/offer/answer/candidate messages. Actual audio is carried directly through WebRTC DTLS-SRTP, or through a separately configured TURN relay.

## Development

With Node.js 20+:

```sh
npm install
npm test
npm start
```

Default `127.0.0.1:8787`; health endpoint `http://127.0.0.1:8787/health`; websocket endpoint `ws://127.0.0.1:8787/v1/voice`. Set `HOST` and `PORT` as environment variables.

For internet use, deploy behind a TLS reverse proxy (HTTPS and **WSS only**). Do not expose `ws://` to the public internet. Use a trusted domain and real certificate. Deploy a separate [coturn](https://github.com/coturn/coturn) server with temporary authenticated TURN credentials, especially for mobile carrier networks.

## Wire protocol

The caller creates a cryptographically random, Base64url-encoded 16-byte room secret (22 characters). Share it privately. Each client sends `{"type":"join","room":"<22-char-token>"}` to the WebSocket service. The first gets `{"type":"joined","peers":1}`. On second join each receives `{"type":"peer-ready"}`, then the caller sends `{"type":"offer","payload":"<SDP>"}`; receiver responds with `{"type":"answer","payload":"<SDP>"}`. `candidate` messages are relayed. The server indicates `peer-left` upon disconnect.

*Two-person room and 2-hour ephemeral lifetime; no accounts, log storage, public room list, or historical messages.*

## Threat model and known limits

- Anyone who possesses a room secret can attempt to join. No independent user identity/authentication, device key verification, or abuse reporting exists yet.
- **WebRTC encryption is not enough to protect against an actively malicious signaling service without separately authenticated fingerprints.** This is not a production-grade verified E2EE service.
- SDP/ICE metadata (including IP addresses) is available to the signaling server/peer. Use TURN relay-only ICE when requiring IP address obfuscation.
- Rooms are process-local. Restarts disconnect users. Horizontal scaling requires a shared state/relay. The service doesn't yet enforce per-IP quotas; add reverse-proxy rate controls, DDoS protection, monitoring, TLS, and verification before public deployment.
- An untrusted relay can observe network metadata and traffic volume. It should not be able to read DTLS-SRTP media plaintext when negotiated correctly.
- This server is **not deployed** and the first Android-native v0.3 alpha still uses manual offer/answer. Integrating WebSockets and hosted TURN is the next milestone.
