# Xyool TURN media relay deployment (test/alpha)

**Status:** Opt-in integration code and automated mock tests. A working TURN relay is **not deployed** merely by merging this code.

## Important network boundary

Railway's public ingress offers HTTP(S) and TCP proxy, **not UDP**. Keep the durable `xyool-id-signaling` WSS registry on Railway, but do not mistake a Railway coturn container for working external UDP media relay. Use a provider with publicly reachable UDP for media.

Xyool clients use direct/STUN candidates first in normal calls; relay candidates may be used when needed. A deliberately forced `Test TURN relay-only call` should only be used with actual credentials.

## Option A: Cloudflare Realtime TURN (easy alpha path)

1. In your **own Cloudflare account**, open Realtime → TURN and create a TURN key.
2. From the TURN key page, get the **TURN Key ID** and **TURN Key API token**. These are credentials, not a public service key.
3. In Railway → **Xyool Calling** → **xyool-id-signaling** → Variables, create:
   - `XYOOL_TURN_PROVIDER=cloudflare`
   - `XYOOL_CF_TURN_KEY_ID` = Cloudflare TURN key ID
   - `XYOOL_CF_TURN_API_TOKEN` = long-lived TURN key API token (**sealed/secret variable**)
4. **Never** put these in a mobile APK, GitHub commit, issue, QR code, chat message, logs, or file uploaded publicly.
5. Review pending changes; switch the signaling deployment to the vetted TURN-enabled branch only after the secrets are present. Retain the existing registry volume `/data` and `XYOOL_ID_REGISTRY` setting. Do not reinitialize persistent IDs.
6. Both Android phones must run the TURN-enabled APK and have Xyool Network ON. Wait for `Server-issued TURN lease usable: yes` in sanitized diagnostics before call testing.

Cloudflare provider API: POST `https://rtc.live.cloudflare.com/v1/turn/keys/KEY_ID/credentials/generate-ice-servers` with a server-only bearer token. The backend requests 2-hour temporary credentials and issues them **only on successfully registered Xyool WebSocket sessions**. Credential refresh is bounded on both ends.

Official docs:
https://developers.cloudflare.com/realtime/turn/generate-credentials/
https://developers.cloudflare.com/realtime/turn/
https://developers.cloudflare.com/realtime/sfu/platform/pricing/

Cloudflare documented October 2026 pricing: first **1,000 GB/month** shared SFU/TURN allowance free, then **$0.05 per GB** egress. Confirm plan/account terms before enabling live traffic.

## Option B: user-owned coturn on a UDP-capable VPS

Install [coturn](https://github.com/coturn/coturn/) on a separately provisioned VPS or server with a stable public IPv4 address, and open **UDP 3478** and the configured **UDP relay port range** in its firewall; optionally TCP/TLS listening for restricted clients.

Use `use-auth-secret`, `static-auth-secret` (random 32+ character secret), `realm`, a bounded relay port range, sane quotas and anti-abuse limits. Configure Railway signaling variables:
- `XYOOL_TURN_PROVIDER=coturn`
- `XYOOL_TURN_SHARED_SECRET` = same long random secret (sealed/secret)
- `XYOOL_TURN_URLS=turn:relay.yourdomain.example:3478?transport=udp,turn:relay.yourdomain.example:3478?transport=tcp`

The backend issues REST-style time-limited HMAC credentials; the app never receives the signing secret. Use actual public hostnames and certificates as applicable. Control bandwidth and costs. The currently connected Railway environment has no standalone VPS/coturn hosting already established.

## Acceptance checklist (two real phones, separate Wi-Fi)

- Before provider enablement: `Server-issued TURN lease usable: no`; existing STUN-only calls still behave as before.
- After deployment and registration: both phones show `... usable: yes`. **No provider tokens** in the report.
- Caller enters saved contact and taps `Test TURN relay-only call`. In diagnostics, caller must show **relay candidates >0** and ICE **CONNECTED/COMPLETED**.
- Verify **audible two-way voice**, not just ICE, with phones in separate rooms.
- Test outgoing and incoming both directions, three consecutive calls each, speaker toggle, mute, Home, rotation, screen lock, hang-up, re-dial, Wi-Fi changes, and temporarily disabling relay.
- Confirm fallback: normal calls work directly if TURN disabled on server; users don't lose contact IDs when upgrading.
- Inspect provider usage metrics and set a budget alert before broad release.
- Record any failing ICE and WebRTC media stats without leaking IP addresses, passwords or SDP.

## Automated test scope

- Node unit tests: Cloudflare mock API, coturn REST-style HMAC signing, invalid URLs/secrets, fail closed.
- WebSocket integration: only registered IDs receive leases; anonymous requests close; refresh throttle.
- Android CI: app compile, JDK URL validation, signed update-compatible ARM64 APK.
- **Not** included: real UDP allocation against a paid/managed relay, two-phone audible audio, network transitions or Android OEM battery termination. Those must be tested on physical phones after provider setup.

No production signaling source or variables should be replaced merely by committing this document.
