import {WebSocket} from 'ws';
import {randomBytes} from 'node:crypto';

// Live public-internet smoke test for Xyool's deployed ID signaling service.
// Creates two throwaway IDs, verifies network registration, call ringing,
// accept, SDP/ICE relay and hangup. No microphone data is transmitted.
// The live registry retains two harmless test ID hashes per run.
const endpoint=process.env.XYOOL_LIVE_WSS;
if(!endpoint || !/^wss:\/\/[^/]+\/v1\/id$/.test(endpoint)){
  throw new Error('Set XYOOL_LIVE_WSS to the trusted Xyool wss://.../v1/id endpoint');
}
const ABC='ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
const letters=()=>Array.from(randomBytes(12),n=>ABC[n%ABC.length]).join('');
const id=()=>{const v=letters();return 'XY-'+v.slice(0,4)+'-'+v.slice(4,8)+'-'+v.slice(8);};
const token=()=>randomBytes(32).toString('hex');
const waitFor=(socket,type,timeoutMs=10000)=>new Promise((res,rej)=>{
  const timer=setTimeout(()=>{socket.off('message',onMessage);rej(Error('Timeout waiting '+type));},timeoutMs);
  function onMessage(data){
    let m;try{m=JSON.parse(String(data));}catch{return;}
    if(m.type!==type)return;
    clearTimeout(timer);socket.off('message',onMessage);res(m);
  }
  socket.on('message',onMessage);
});
const send=(socket,m)=>socket.send(JSON.stringify(m));
const open=()=>new Promise((res,rej)=>{
  const socket=new WebSocket(endpoint,{handshakeTimeout:12000});
  socket.once('open',()=>res(socket));socket.once('error',rej);
});
const sockets=[];
try{
  const a=await open();sockets.push(a);
  const b=await open();sockets.push(b);
  const ida=id(),idb=id();
  const ar=waitFor(a,'registered');
  send(a,{type:'register',id:ida,token:token()});await ar;
  const br=waitFor(b,'registered');
  send(b,{type:'register',id:idb,token:token()});await br;
  console.log('LIVE PASS: both devices registered over public TLS WebSockets');
  const incoming=waitFor(b,'incoming'), ringing=waitFor(a,'ringing');
  send(a,{type:'call',to:idb});
  const incomingMsg=await incoming;await ringing;
  if(incomingMsg.from!==ida)throw Error('Wrong incoming caller');
  console.log('LIVE PASS: ID dialing rang the intended device');
  const acceptedA=waitFor(a,'accepted'),acceptedB=waitFor(b,'accepted');
  send(b,{type:'accept'});
  await Promise.all([acceptedA,acceptedB]);
  console.log('LIVE PASS: accept delivered to both phones');
  const sdp='v=0\r\n'+'s=x\r\n'.repeat(20);
  const receivedOffer=waitFor(b,'signal');
  send(a,{type:'signal',kind:'offer',sdp});
  if((await receivedOffer).sdp!==sdp)throw Error('Missing offer');
  const receivedAnswer=waitFor(a,'signal');
  send(b,{type:'signal',kind:'answer',sdp});
  if((await receivedAnswer).kind!=='answer')throw Error('Missing answer');
  const receivedCandidate=waitFor(b,'signal');
  send(a,{type:'signal',kind:'candidate',candidate:'candidate:1 1 udp 1 192.0.2.1 5000 typ host',mid:'0',index:0});
  if((await receivedCandidate).kind!=='candidate')throw Error('Missing candidate');
  console.log('LIVE PASS: SDP and ICE candidate messages relayed');
  const ended=waitFor(b,'ended');
  send(a,{type:'hangup'});await ended;
  console.log('LIVE PASS: hangup delivered');
}finally{
  for(const s of sockets)s.terminate();
}
