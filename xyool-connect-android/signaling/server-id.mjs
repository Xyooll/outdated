import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { createHash, randomUUID, timingSafeEqual } from 'node:crypto';
import { WebSocket, WebSocketServer } from 'ws';

const ID = /^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$/;
const HEX = /^[0-9a-f]{64}$/;
const MAX_MSG = 48_000;
const LIMIT = 50;

const hash = token => createHash('sha256').update(token).digest('hex');
const safeCompare = (a,b) => {
  const one=Buffer.from(a,'hex'), two=Buffer.from(b,'hex');
  return one.length===two.length && timingSafeEqual(one,two);
};
const deliver=(socket,obj)=>{
  if(socket && socket.readyState===WebSocket.OPEN)socket.send(JSON.stringify(obj));
};

export function createIdServer({ host='127.0.0.1',port=8788,
  registryPath=process.env.XYOOL_ID_REGISTRY || './xyool-id-registry.json'}={}){
  // Fail closed rather than silently issuing non-persistent IDs.
  // On Railway, attach a persistent volume before booting this service.
  const storageDir=path.dirname(path.resolve(registryPath));
  if(!fs.existsSync(storageDir))throw new Error('Missing identity registry directory: '+storageDir);
  const probe=path.join(storageDir,'.xyool-writecheck-'+randomUUID());
  try {
    fs.writeFileSync(probe,'ok',{flag:'wx',mode:0o600});
    fs.unlinkSync(probe);
  } catch(err) {
    throw new Error('Identity registry storage must be writable and persistent: '+err.message);
  }
  const registry = new Map();
  if (fs.existsSync(registryPath)) {
    const persisted=JSON.parse(fs.readFileSync(registryPath,'utf8'));
    for(const [id,value] of Object.entries(persisted)) {
      if(ID.test(id)&&typeof value==='string'&&HEX.test(value)) registry.set(id,value);
    }
  }
  const online=new Map();
  const sessions=new Map();
  const callFor=socket=>socket.session&&sessions.get(socket.session);
  function persist() {
    const data=Object.fromEntries(registry);
    const tmp=registryPath+'.tmp';
    fs.writeFileSync(tmp,JSON.stringify(data),{mode:0o600,flag:'w'});
    fs.renameSync(tmp,registryPath);
  }
  function stopCall(session, actor, reason) {
    if(!session||!sessions.has(session.key))return;
    sessions.delete(session.key);
    for(const person of [session.a,session.b]){
      if(person.session===session.key)person.session=null;
      if(person!==actor)deliver(person,{type:'ended',reason});
    }
  }
  const app=http.createServer((req,res)=>{
    if(req.url==='/health'&&req.method==='GET') {
      res.writeHead(200,{'Content-Type':'application/json','Cache-Control':'no-store'});
      res.end('{"ok":true}');
    } else {res.writeHead(404);res.end();}
  });
  const wss=new WebSocketServer({server:app,path:'/v1/id',maxPayload:MAX_MSG,
    perMessageDeflate:false});
  wss.on('connection',socket=>{
    socket.xyid=null;
    socket.session=null;
    socket.windowAt=Date.now();
    socket.messages=0;
    socket.alive=true;
    socket.on('pong',()=>{socket.alive=true;});
    socket.on('message',(raw,binary)=>{
      if(binary){socket.close(1008,'Text only');return;}
      const now=Date.now();
      if(now-socket.windowAt>10_000){socket.windowAt=now;socket.messages=0;}
      if(++socket.messages>LIMIT){socket.close(1008,'Rate limit');return;}
      let msg;
      try{msg=JSON.parse(raw.toString('utf8'));}catch{socket.close(1008,'Bad JSON');return;}
      if(!msg||typeof msg!=='object'||Array.isArray(msg)||
        typeof msg.type!=='string'){socket.close(1008,'Bad message');return;}
      if(msg.type==='register'){
        if(socket.xyid||!ID.test(msg.id||'')||!HEX.test(msg.token||'')){
          socket.close(1008,'Bad registration');return;
        }
        const proof=hash(msg.token);
        const registered=registry.get(msg.id);
        if(registered && !safeCompare(registered,proof)){
          deliver(socket,{type:'error',message:'This ID is already registered'});
          socket.close(1008,'ID ownership mismatch');return;
        }
        if(online.has(msg.id)){
          deliver(socket,{type:'error',message:'This ID is already online'});
          socket.close(1008,'Already online');return;
        }
        if(!registered){
          if(registry.size>=100_000){socket.close(1013,'Registry full');return;}
          registry.set(msg.id,proof);
          try{persist();}catch{registry.delete(msg.id);socket.close(1011,'Storage failure');return;}
        }
        socket.xyid=msg.id;
        online.set(socket.xyid,socket);
        deliver(socket,{type:'registered',id:socket.xyid});
        return;
      }
      if(!socket.xyid){socket.close(1008,'Register first');return;}
      if(msg.type==='call'){
        if(socket.session){deliver(socket,{type:'error',message:'Already in call'});return;}
        if(!ID.test(msg.to||'')||msg.to===socket.xyid){
          deliver(socket,{type:'error',message:'Invalid target ID'});return;
        }
        const receiver=online.get(msg.to);
        if(!receiver){deliver(socket,{type:'unavailable'});return;}
        if(receiver.session){deliver(socket,{type:'busy'});return;}
        const session={key:randomUUID(),a:socket,b:receiver,phase:'ringing',created:now};
        sessions.set(session.key,session);
        socket.session=receiver.session=session.key;
        deliver(socket,{type:'ringing'});
        deliver(receiver,{type:'incoming',from:socket.xyid});
        return;
      }
      const session=callFor(socket);
      if(msg.type==='hangup'||msg.type==='reject'){
        stopCall(session,socket,msg.type==='reject'?'declined':'hung-up');
        deliver(socket,{type:'ended',reason:'local'});
        return;
      }
      if(msg.type==='accept'){
        if(!session||session.b!==socket||session.phase!=='ringing')return;
        session.phase='active';
        deliver(session.a,{type:'accepted'});
        deliver(session.b,{type:'accepted'});
        return;
      }
      if(msg.type==='signal'){
        if(!session||session.phase!=='active')return;
        const type=msg.kind;
        if(type==='offer'||type==='answer'){
          if(typeof msg.sdp!=='string'||msg.sdp.length>40_000||
            msg.sdp.length<80||!msg.sdp.startsWith('v=0'))return;
          if(type==='offer'&&socket!==session.a)return;
          if(type==='answer'&&socket!==session.b)return;
          deliver(socket===session.a?session.b:session.a,
            {type:'signal',kind:type,sdp:msg.sdp});
        } else if(type==='candidate'){
          if(typeof msg.candidate!=='string'||msg.candidate.length>4_000 ||
            typeof msg.mid!=='string'||msg.mid.length>50 ||
            !Number.isInteger(msg.index)||msg.index<0||msg.index>50)return;
          deliver(socket===session.a?session.b:session.a,
            {type:'signal',kind:'candidate',candidate:msg.candidate,mid:msg.mid,index:msg.index});
        }
      }
    });
    socket.on('close',()=>{
      if(socket.xyid&&online.get(socket.xyid)===socket)online.delete(socket.xyid);
      stopCall(callFor(socket),socket,'peer-offline');
    });
    socket.on('error',()=>{});
  });
  const ticker=setInterval(()=>{
    const now=Date.now();
    for(const session of sessions.values()) {
      if(now-session.created>60*60*1000)stopCall(session,null,'timeout');
      else if(session.phase==='ringing'&&now-session.created>45_000)
        stopCall(session,null,'no-answer');
    }
    for(const socket of wss.clients) {
      if(!socket.alive)socket.terminate();
      else {socket.alive=false;socket.ping();}
    }
  },15_000);ticker.unref();
  async function close(){
    clearInterval(ticker);
    for(const socket of wss.clients)socket.terminate();
    await new Promise(resolve=>wss.close(resolve));
    await new Promise(resolve=>app.close(resolve));
  }
  return {listen:()=>new Promise(resolve=>app.listen(port,host,resolve)),
    address:()=>app.address(),close,online:()=>online.size};
}

if(process.argv[1]&&import.meta.url===new URL('file://'+process.argv[1]).href){
  // The platform provides TLS at the edge and a writable registry volume.
  // A Railway deploy without a volume is rejected to avoid losing all IDs.
  if(process.env.RAILWAY_ENVIRONMENT && !process.env.RAILWAY_VOLUME_MOUNT_PATH){
    throw new Error('Attach a Railway Volume at /data before deployment. Refusing ephemeral Xyool IDs.');
  }
  if(process.env.NODE_ENV==='production' && !process.env.XYOOL_ID_REGISTRY){
    throw new Error('Set XYOOL_ID_REGISTRY to a durable volume path.');
  }
  const port=Number(process.env.PORT||8788);
  const host=process.env.HOST||'127.0.0.1';
  if(!Number.isInteger(port)||port<1||port>65535)throw new Error('Invalid PORT');
  const service=createIdServer({port,host});
  service.listen().then(()=>{
    console.log('Xyool ID signaling ready at '+host+':'+port);
    console.log('Expose via HTTPS/WSS; do not expose plaintext WebSocket on the public internet.');
  }).catch(err=>{console.error('Startup error: '+err.message);process.exit(1);});
  process.on('SIGTERM',()=>service.close().then(()=>process.exit(0)));
  process.on('SIGINT',()=>service.close().then(()=>process.exit(0)));
}
