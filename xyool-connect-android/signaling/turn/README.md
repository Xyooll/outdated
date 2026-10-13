# Xyool Connect — self-hostable TURN fallback

**Status:** Provisioning template and verified credential-generation implementation. No TURN relay is deployed by this commit. No real carrier/Wi-Fi two-phone voice test has been completed.

## Why this exists

WebRTC tries direct ICE paths first. A TURN relay is a **last resort** when NAT/firewalls prevent direct UDP transport. The Xyool rendezvous server only forwards setup messages; it does not relay audio. An ordinary website or an HTTP/WSS-only service is **not** a TURN media relay.

## Deploy (Linux VPS with public IPv4)

1. Choose a host where you control UDP 3478 and UDP 49160–49260 (and optionally TCP 3478). Do not place this on the current HTTP-only Railway signaling gateway.
2. Make a private `.env` file next to the Compose file with `XYOOL_TURN_SHARED_SECRET` (cryptographically random 32+ characters, kept **off GitHub**) and `XYOOL_TURN_REALM` (hostname of this TURN host). Restrict access to this file; e.g. `chmod 600 .env`. Generate the secret with `openssl rand -hex 32`.
3. Set the host firewall to permit UDP 3478, TCP 3478, and UDP 49160–49260. A cloud network firewall must allow them too.
4. From this folder, run `docker compose -f coturn-compose.yml up -d`. This uses **Linux host networking**, so the UDP relay addresses are directly reachable. On a host behind NAT, explicitly configure `--external-ip=PUBLIC_IP/PRIVATE_IP` and forward the relay port range one-to-one.
5. For a pilot, generate per-phone expiring credentials with `XYOOL_TURN_SHARED_SECRET=... node turn-credentials.mjs XY-ABCD-EFGH-JKLM` on a trusted host. In Xyool Connect's Advanced settings use `turn:TURN_HOST:3478?transport=udp`, plus returned username/password. Both phones need independently issued credentials.
6. Test two real Android devices: one over cellular and the other over unrelated Wi-Fi. Record their Xyool network reports (which omit private IDs and IPs); confirm an ICE **relay** candidate is selected on restrictive networks, establish bidirectional voice, decline and hang up normally.

The shipped Android app's current Advanced TURN settings are manual testing controls. Credential auto-provisioning needs an authenticated, abuse-limited broker at a rendezvous node: **never send the TURN shared secret to phones**. A registration token for an easily self-created ID is not adequate on its own to prevent relay abuse.

## Security / operations

- Expiring TURN usernames protect credentials, but do not make media relay anonymous. The TURN operator sees network metadata and bandwidth usage.
- Coturn consumes network bandwidth and can incur hosting costs. Monitor traffic, abuse, and relay exhaustion before inviting arbitrary users.
- Restrict relay peers to avoid access to private address space; these defaults disable loopback/multicast peers but a full production review and provider firewall rules are needed.
- This Compose template uses regular TURN on UDP/TCP, **not** TURN-over-TLS. For networks permitting only TLS 443, add a correctly configured TLS certificate and `turns:` listener (or use a managed TURN service). Do not falsely advertise TLS from this template.
- No WebRTC media is decrypted by coturn (WebRTC uses DTLS-SRTP), but identity-to-fingerprint pinning is still missing. Xyool Connect remains alpha software and is **not for emergency calls**.

Upstream references: https://github.com/coturn/coturn and https://hub.docker.com/r/coturn/coturn
