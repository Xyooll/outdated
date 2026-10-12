import http from 'node:http';
import { WebSocketServer, WebSocket } from 'ws';
import { createHash } from 'node:crypto';

const DEFAULT_PORT = Number(process.env.PORT || 8787);
const DEFAULT_HOST = process.env.HOST || '127.0.0.1';
const MAX_ROOMS = 2000;
const ROOM_TTL = 2 * 60 * 60 * 1000;
const MAX_MESSAGE = 48 * 1024;
const ROOM_RE = /^[A-Za-z0-9_-]{22}$/;
const allowedTypes = new Set(['offer', 'answer', 'candidate']);
const rooms = new Map();

// Bearer room secret is never used as the map key or written to logs.
// The server can still see SDP (including IP/ICE metadata), so do not
// treat an untrusted server as an identity-authenticated E2EE service.
const roomKey = token => createHash('sha256').update(token).digest('hex');
const deliver = (client, object) => {
  if (client.readyState === WebSocket.OPEN) client.send(JSON.stringify(object));
};

export function createSignalingServer({
  port = DEFAULT_PORT,
  host = DEFAULT_HOST
} = {}) {
  const app = http.createServer((req, res) => {
    if (req.url === '/health' && req.method === 'GET') {
      res.writeHead(200, { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' });
      res.end('{"ok":true}');
    } else {
      res.writeHead(404);
      res.end();
    }
  });
  const socketServer = new WebSocketServer({
    server: app, path: '/v1/voice', maxPayload: MAX_MESSAGE,
    perMessageDeflate: false
  });

  socketServer.on('connection', client => {
    let joinedKey = null;
    let messageCount = 0;
    let windowStart = Date.now();
    let alive = true;
    client.on('pong', () => { alive = true; });

    client.on('message', (buffer, binary) => {
      const now = Date.now();
      if (now - windowStart > 10_000) { windowStart = now; messageCount = 0; }
      if (++messageCount > 50 || binary) { client.close(1008, 'Rate limit or binary'); return; }

      let msg;
      try { msg = JSON.parse(buffer.toString('utf8')); }
      catch { client.close(1008, 'Invalid JSON'); return; }
      if (!msg || typeof msg !== 'object' || Array.isArray(msg)) {
        client.close(1008, 'Invalid message'); return;
      }

      if (msg.type === 'join') {
        if (joinedKey || typeof msg.room !== 'string' || !ROOM_RE.test(msg.room)) {
          client.close(1008, 'Invalid join'); return;
        }
        const key = roomKey(msg.room);
        let room = rooms.get(key);
        if (!room) {
          if (rooms.size >= MAX_ROOMS) { client.close(1013, 'Busy'); return; }
          room = { peers: new Set(), created: now };
          rooms.set(key, room);
        }
        if (room.peers.size >= 2) { client.close(1008, 'Room full'); return; }
        room.peers.add(client);
        joinedKey = key;
        deliver(client, { type: 'joined', peers: room.peers.size });
        if (room.peers.size === 2) {
          for (const p of room.peers) deliver(p, {type:'peer-ready'});
        }
        return;
      }

      if (!joinedKey || !allowedTypes.has(msg.type) || typeof msg.payload !== 'string'
        || msg.payload.length > 40_000) {
        client.close(1008, 'Invalid signal'); return;
      }
      const room = rooms.get(joinedKey);
      if (!room || !room.peers.has(client) || room.peers.size !== 2) {
        deliver(client, { type:'waiting' }); return;
      }
      for (const peer of room.peers) {
        if (peer !== client) deliver(peer, { type:msg.type, payload:msg.payload });
      }
    });
    client.on('close', () => {
      if (!joinedKey) return;
      const room = rooms.get(joinedKey);
      if (!room) return;
      room.peers.delete(client);
      for (const peer of room.peers) deliver(peer, {type:'peer-left'});
      if (!room.peers.size) rooms.delete(joinedKey);
    });
    client.on('error', () => { /* Never log SDP, bearer secrets, or personal data */ });
    client._xyoolPing = () => {
      if (!alive) { client.terminate(); return; }
      alive = false;
      client.ping();
    };
  });

  const sweeper = setInterval(() => {
    const now=Date.now();
    for (const [key, room] of rooms) {
      if (now - room.created >= ROOM_TTL) {
        for (const peer of room.peers) peer.close(1000, 'Room expired');
        rooms.delete(key);
      }
    }
    for (const client of socketServer.clients) client._xyoolPing?.();
  }, 30_000);
  sweeper.unref();

  async function close() {
    clearInterval(sweeper);
    for (const client of socketServer.clients) client.terminate();
    await new Promise(resolve => socketServer.close(resolve));
    await new Promise(resolve => app.close(resolve));
  }
  return { listen: () => new Promise(resolve => app.listen(port, host, resolve)),
    close, address: () => app.address(), roomCount: () => rooms.size };
}

if (process.argv[1] && import.meta.url === new URL('file://' + process.argv[1]).href) {
  const service = createSignalingServer();
  service.listen().then(() => {
    console.log('Xyool signaling ready on '+DEFAULT_HOST+':'+DEFAULT_PORT);
    console.log('Put this process behind a TLS reverse proxy. Never expose plaintext WS publicly.');
  });
  process.on('SIGTERM', () => service.close().then(() => process.exit(0)));
  process.on('SIGINT', () => service.close().then(() => process.exit(0)));
}
