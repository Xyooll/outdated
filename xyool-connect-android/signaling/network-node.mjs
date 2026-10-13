/**
 * Xyool Network rendezvous node (prototype).
 *
 * Each Android phone connects to its chosen node via /v1/id, retaining the
 * existing Xyool Android calling wire protocol. Trusted operator nodes connect
 * over /v1/mesh, authenticate with HMAC, and gossip short-lived presence.
 *
 * Like BitTorrent, there are multiple independently hosted discovery nodes;
 * unlike BitTorrent, real-time call signaling uses routed ephemeral messages.
 * This is a TRUSTED federation prototype, NOT a public DHT or an anonymous
 * mesh. Do not advertise it as end-to-end authenticated identity. WebRTC media
 * is handled by the phones; TURN must be independently configured if needed.
 */
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import {createHash,createHmac,randomBytes,randomUUID,timingSafeEqual} from 'node:crypto';
import {WebSocket,WebSocketServer} from 'ws';

const ID=/^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$/;
const HEX=/^[a-f0-9]{64}$/;
const NODE=/^[A-Za-z0-9_.-]{3,64}$/;
const hash=v=>createHash('sha256').update(v).digest('hex');
const send=(ws,v)=>{if(ws?.readyState===WebSocket.OPEN)ws.send(JSON.stringify(v));};
const safe=(a,b)=>a.length===b.length&&timingSafeEqual(Buffer.from(a),Buffer.from(b));
const MAX_TEXT=48000;
const MESH_TTL=5;

export function createXyoolNetworkNode({
  host='127.0.0.1',port=8788,nodeId='node-1',peerUrls=[],
  networkSecret='',registryPath='./xyool-network-identity.json'
}={}){
  if(!NODE.test(nodeId))throw Error('Invalid NODE_ID');
  if(peerUrls.length && networkSecret.length<32)throw Error('Mesh peers require a 32+ character shared network secret');
  if(peerUrls.length>24)throw Error('Too many peer URLs');
  const realDir=path.dirname(path.resolve(registryPath));
  if(!fs.existsSync(realDir))throw Error('Persistent ID registry directory missing: '+realDir);
  const registry=new Map();
  if(fs.existsSync(registryPath)){
    for(const [id,proof] of Object.entries(JSON.parse(fs.readFileSync(registryPath,'utf8'))))
      if(ID.test(id)&&HEX.test(proof))registry.set(id,proof);
  }
  function persist(){
    const tmp=registryPath+'.tmp';
    fs.writeFileSync(tmp,JSON.stringify(Object.fromEntries(registry)),{mode:0o600});
    fs.renameSync(tmp,registryPath);
  }

  const local=new Map();     // Xyool ID -> client WebSocket
  const calls=new Map();     // local Xyool ID -> one active call record
  const routes=new Map();    // remote Xyool ID -> {via, proof, expires}
  const neighbors=new Set(); // authenticated mesh websockets
  const seen=new Map();      // de-duplicate gossip and delivered messages
  const nonces=new Map();    // reject replayed mesh handshake
  const outbound=new Map();
  const timers=[];
  let stopped=false;

  const app=http.createServer((req,res)=>{
    if(req.url!=='/health'){res.writeHead(404);res.end();return;}
    res.writeHead(200,{'content-type':'application/json','cache-control':'no-store'});
    res.end(JSON.stringify({ok:true,node:nodeId,localPhones:local.size,meshNeighbors:neighbors.size}));
  });
  const phonesWss=new WebSocketServer({noServer:true,maxPayload:MAX_TEXT,perMessageDeflate:false});
  const meshWss=new WebSocketServer({noServer:true,maxPayload:MAX_TEXT,perMessageDeflate:false});
  app.on('upgrade',(req,socket,head)=>{
    const part=req.url?.split('?')[0];
    if(part==='/v1/id') phonesWss.handleUpgrade(req,socket,head,ws=>phonesWss.emit('connection',ws));
    else if(part==='/v1/mesh'&&networkSecret.length>=32)
      meshWss.handleUpgrade(req,socket,head,ws=>meshWss.emit('connection',ws));
    else socket.destroy();
  });
  function remember(eid){
    if(typeof eid!=='string'||eid.length>80)return false;
    if(seen.has(eid))return false;
    seen.set(eid,Date.now()+120000);
    return true;
  }
  function gossip(packet,source){
    if(!remember(packet.eid))return;
    if(packet.online && ID.test(packet.id)){
      if(!local.has(packet.id) && typeof packet.proof==='string' && HEX.test(packet.proof)){
        routes.set(packet.id,{via:source,proof:packet.proof,expires:Date.now()+55000});
      }
    }else if(packet.online===false && ID.test(packet.id)){
      const record=routes.get(packet.id);
      if(record && record.via===source)routes.delete(packet.id);
    }else return;
    if(packet.ttl>1)for(const ws of neighbors)
      if(ws!==source)send(ws,{...packet,ttl:packet.ttl-1});
  }
  function announce(id,online=true){
    const packet={op:'presence',eid:randomUUID(),ttl:MESH_TTL,id,online,
      proof:registry.get(id),origin:nodeId};
    remember(packet.eid);
    for(const ws of neighbors)send(ws,packet);
  }
  function route(msg,arrival=null){
    if(!ID.test(msg.to)||!ID.test(msg.from)||
      !Number.isInteger(msg.ttl)||msg.ttl<1||msg.ttl>MESH_TTL)return false;
    if(!remember(msg.eid))return false;
    const dest=local.get(msg.to);
    if(dest){receiveOnPhone(msg);return true;}
    const entry=routes.get(msg.to);
    if(entry && entry.expires>Date.now() && neighbors.has(entry.via) &&
      entry.via!==arrival && msg.ttl>1){
      send(entry.via,{...msg,ttl:msg.ttl-1});return true;
    }
    // Deliberately do not flood SDP/call metadata to unknown nodes.
    return false;
  }
  function dispatch(from,to,kind,callId,payload={}){
    return route({op:'route',eid:randomUUID(),ttl:MESH_TTL,
      from,to,kind,callId,payload});
  }
  function closeCall(id,reason,sendPeer=true){
    const c=calls.get(id);
    if(!c)return;
    calls.delete(id);
    if(sendPeer)dispatch(id,c.peer,'ended',c.callId,{reason});
  }
  function deliverError(id,type){
    const ws=local.get(id);
    if(ws)send(ws,{type});
  }
  function receiveOnPhone(m){
    const ws=local.get(m.to);
    if(!ws)return;
    const existing=calls.get(m.to);
    if(m.kind==='call'){
      if(existing){dispatch(m.to,m.from,'busy',m.callId);return;}
      if(!routes.has(m.from)&&!local.has(m.from)){
        // A route may have expired in transit; the incoming invitation can
        // still be displayed, but the reply must have a known way back.
        return;
      }
      calls.set(m.to,{peer:m.from,callId:m.callId,role:'callee',
        phase:'ringing',at:Date.now()});
      send(ws,{type:'incoming',from:m.from});
      dispatch(m.to,m.from,'ringing',m.callId);
      return;
    }
    if(!existing || existing.peer!==m.from || existing.callId!==m.callId)return;
    if(m.kind==='ringing' && existing.role==='caller'&&existing.phase==='ringing')
      send(ws,{type:'ringing'});
    else if(m.kind==='accepted' && existing.role==='caller'&&existing.phase==='ringing'){
      existing.phase='active';send(ws,{type:'accepted'});
    }else if(m.kind==='signal'&&existing.phase==='active'&&validSignal(m.payload)){
      send(ws,{type:'signal',...m.payload});
    }else if(m.kind==='busy'||m.kind==='unavailable'){
      calls.delete(m.to);send(ws,{type:m.kind});
    }else if(m.kind==='ended'){
      calls.delete(m.to);send(ws,{type:'ended',reason:m.payload?.reason||'remote-ended'});
    }
  }
  function validSignal(p){
    if(!p||typeof p!=='object')return false;
    if(p.kind==='offer'||p.kind==='answer')
      return typeof p.sdp==='string'&&p.sdp.length>=80&&p.sdp.length<=40000&&p.sdp.startsWith('v=0');
    if(p.kind==='candidate')return typeof p.candidate==='string'&&
      p.candidate.length<4000&&typeof p.mid==='string'&&p.mid.length<=50&&
      Number.isInteger(p.index)&&p.index>=0&&p.index<=50;
    return false;
  }
  function messageFromPhone(ws,raw){
    if(++ws.msgCount>60 && Date.now()-ws.windowAt<10000){ws.close(1008,'Rate limit');return;}
    if(Date.now()-ws.windowAt>=10000){ws.msgCount=1;ws.windowAt=Date.now();}
    let m;try{m=JSON.parse(raw.toString('utf8'));}catch{ws.close(1008,'Invalid JSON');return;}
    if(!m||typeof m!=='object'||Array.isArray(m))return;
    if(m.type==='register'){
      if(ws.xyid||!ID.test(m.id||'')||!HEX.test(m.token||'')){ws.close(1008,'Invalid registration');return;}
      const proof=hash(m.token);
      const own=registry.get(m.id);
      const distant=routes.get(m.id);
      if(own && !safe(own,proof)){send(ws,{type:'error',message:'Xyool ID is already registered here'});return;}
      if(distant&&distant.expires>Date.now()&&!safe(distant.proof,proof)){
        send(ws,{type:'error',message:'Xyool ID is active on another node with a different key'});return;
      }
      if(local.has(m.id)){send(ws,{type:'error',message:'Xyool ID already online'});return;}
      if(!own){registry.set(m.id,proof);try{persist();}catch{
        registry.delete(m.id);send(ws,{type:'error',message:'Node identity storage unavailable'});return;
      }}
      ws.xyid=m.id;local.set(m.id,ws);routes.delete(m.id);
      send(ws,{type:'registered',id:m.id});announce(m.id);return;
    }
    if(!ws.xyid)return;
    const me=ws.xyid,c=calls.get(me);
    if(m.type==='call'){
      if(c){send(ws,{type:'busy'});return;}
      if(!ID.test(m.to||'')||m.to===me){send(ws,{type:'error',message:'Invalid Xyool ID'});return;}
      const peer=m.to;
      const info=routes.get(peer);
      if(!local.has(peer)&&(!info||info.expires<Date.now())){
        send(ws,{type:'unavailable'});return;
      }
      const callId=randomUUID();
      calls.set(me,{peer,callId,role:'caller',phase:'ringing',at:Date.now()});
      if(!dispatch(me,peer,'call',callId)){
        calls.delete(me);send(ws,{type:'unavailable'});
      }
    }else if(m.type==='accept' && c?.role==='callee'&&c.phase==='ringing'){
      c.phase='active';send(ws,{type:'accepted'});
      if(!dispatch(me,c.peer,'accepted',c.callId)){closeCall(me,'peer-unreachable',false);send(ws,{type:'ended',reason:'peer-unreachable'});}
    }else if(m.type==='reject'||m.type==='hangup'){
      if(c)closeCall(me,m.type==='reject'?'declined':'hung-up',true);
      send(ws,{type:'ended',reason:'local'});
    }else if(m.type==='signal'&&c?.phase==='active'&&validSignal(m)){
      dispatch(me,c.peer,'signal',c.callId,{kind:m.kind,sdp:m.sdp,candidate:m.candidate,mid:m.mid,index:m.index});
    }
  }
  phonesWss.on('connection',ws=>{
    ws.xyid=null;ws.windowAt=Date.now();ws.msgCount=0;
    ws.on('message',(raw,binary)=>{if(binary){ws.close(1008);return;}messageFromPhone(ws,raw);});
    ws.on('close',()=>{
      if(ws.xyid&&local.get(ws.xyid)===ws){
        closeCall(ws.xyid,'peer-offline',true);
        local.delete(ws.xyid);announce(ws.xyid,false);
      }
    });
    ws.on('error',()=>{});
  });
  function sign(id,ts,nonce){
    return createHmac('sha256',networkSecret).update(id+'|'+ts+'|'+nonce).digest('hex');
  }
  function hello(ws){
    const ts=Date.now(),nonce=randomBytes(16).toString('hex');
    send(ws,{op:'hello',id:nodeId,ts,nonce,proof:sign(nodeId,ts,nonce)});
  }
  function meshSocket(ws){
    ws.authed=false;
    ws.on('message',(raw,binary)=>{
      if(binary||raw.length>MAX_TEXT){ws.close(1008);return;}
      let m;try{m=JSON.parse(raw.toString('utf8'));}catch{ws.close(1008);return;}
      if(!ws.authed){
        if(m.op!=='hello'||!NODE.test(m.id||'')||m.id===nodeId||
          !Number.isSafeInteger(m.ts)||Math.abs(Date.now()-m.ts)>30000||
          !/^[a-f0-9]{32}$/.test(m.nonce||'')||
          !/^[a-f0-9]{64}$/.test(m.proof||'')||
          !safe(sign(m.id,m.ts,m.nonce),m.proof)||
          nonces.has(m.id+'|'+m.nonce)){ws.close(1008,'Invalid mesh proof');return;}
        nonces.set(m.id+'|'+m.nonce,Date.now()+60000);
        ws.authed=true;ws.peerId=m.id;neighbors.add(ws);
        for(const id of local.keys()){
          send(ws,{op:'presence',eid:randomUUID(),ttl:MESH_TTL,id,online:true,
            proof:registry.get(id),origin:nodeId});
        }
        return;
      }
      if(m.op==='presence'&&Number.isInteger(m.ttl)&&m.ttl>0&&m.ttl<=MESH_TTL&&
        ID.test(m.id||'')&&typeof m.origin==='string'&&NODE.test(m.origin)){
        gossip(m,ws);
      }else if(m.op==='route'&&typeof m.callId==='string'&&
        /^[0-9a-f-]{36}$/.test(m.callId)&&
        ['call','ringing','accepted','signal','busy','unavailable','ended'].includes(m.kind)){
        route(m,ws);
      }
    });
    ws.on('close',()=>{
      neighbors.delete(ws);
      for(const [id,r] of routes)if(r.via===ws)routes.delete(id);
    });
    ws.on('error',()=>{});
  }
  meshWss.on('connection',ws=>{meshSocket(ws);hello(ws);});
  function connectMesh(url){
    if(stopped||outbound.get(url)?.readyState===WebSocket.OPEN||
      outbound.get(url)?.readyState===WebSocket.CONNECTING)return;
    if(!/^wss:\/\//.test(url)&&!/^ws:\/\/(localhost|127\.0\.0\.1)(:\d+)?\/v1\/mesh$/.test(url)){
      throw Error('Only WSS mesh peers allowed outside localhost');
    }
    const ws=new WebSocket(url,{perMessageDeflate:false,handshakeTimeout:8000});
    outbound.set(url,ws);meshSocket(ws);
    ws.on('open',()=>hello(ws));
    ws.on('close',()=>{if(outbound.get(url)===ws)outbound.delete(url);});
  }
  timers.push(setInterval(()=>{
    const now=Date.now();
    for(const [eid,expiry] of seen)if(expiry<now)seen.delete(eid);
    for(const [nonce,expiry] of nonces)if(expiry<now)nonces.delete(nonce);
    for(const [id,r] of routes)if(r.expires<now||!neighbors.has(r.via))routes.delete(id);
    for(const [id,c] of calls){
      if(now-c.at>(c.phase==='ringing'?45000:7200000)){
        closeCall(id,'timeout',true);
        send(local.get(id),{type:'ended',reason:c.phase==='ringing'?'no-answer':'timeout'});
      }
    }
    // Fresh presence is necessary for sleeping or newly joined mesh nodes.
    for(const id of local.keys())announce(id);
    for(const url of peerUrls)connectMesh(url);
  },10000).unref());
  async function close(){
    stopped=true;for(const timer of timers)clearInterval(timer);
    for(const ws of phonesWss.clients)ws.terminate();
    for(const ws of meshWss.clients)ws.terminate();
    for(const ws of outbound.values())ws.terminate();
    await new Promise(resolve=>phonesWss.close(resolve));
    await new Promise(resolve=>meshWss.close(resolve));
    await new Promise(resolve=>app.close(resolve));
  }
  return {listen:()=>new Promise(resolve=>app.listen(port,host,()=>{for(const url of peerUrls)connectMesh(url);resolve();})),
    address:()=>app.address(),close,stats:()=>({phones:local.size,neighbors:neighbors.size,remote:routes.size})};
}
if(process.argv[1] && import.meta.url===new URL('file://'+process.argv[1]).href){
  const peerUrls=(process.env.XYOOL_MESH_PEERS||'').split(',').map(v=>v.trim()).filter(Boolean);
  const registryPath=process.env.XYOOL_ID_REGISTRY||'./xyool-network-identity.json';
  if(process.env.RAILWAY_ENVIRONMENT&&!process.env.RAILWAY_VOLUME_MOUNT_PATH)
    throw Error('Railway requires durable identity volume');
  const service=createXyoolNetworkNode({
    host:process.env.HOST||'0.0.0.0',port:Number(process.env.PORT||8788),
    nodeId:process.env.XYOOL_NODE_ID||'xyool-001',
    peerUrls,networkSecret:process.env.XYOOL_MESH_SECRET||'',registryPath
  });
  await service.listen();console.log('Xyool rendezvous node listening; node id: '+(process.env.XYOOL_NODE_ID||'xyool-001'));
  process.on('SIGTERM',()=>service.close().then(()=>process.exit(0)));
  process.on('SIGINT',()=>service.close().then(()=>process.exit(0)));
}
