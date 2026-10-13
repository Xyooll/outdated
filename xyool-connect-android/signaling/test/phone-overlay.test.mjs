import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {WebSocket} from 'ws';
import {createIdServer} from '../server-id.mjs';

const A='XY-ABCD-EFGH-JKLM', B='XY-MNPQ-RSTU-VWXY', C='XY-2345-6789-ABCD';
async function phone(port,id,token){
  const ws=new WebSocket('ws://127.0.0.1:'+port+'/v1/id');
  await new Promise((resolve,reject)=>{
    ws.once('open',resolve);ws.once('error',reject);
  });
  const received=[];
  ws.on('message',data=>received.push(JSON.parse(data.toString())));
  ws.send(JSON.stringify({type:'register',id,token:token.repeat(64)}));
  await until(()=>received.some(x=>x.type==='registered'));
  return {ws,received,send:m=>ws.send(JSON.stringify(m))};
}
async function until(fn,ms=4000){
  const end=Date.now()+ms;
  while(Date.now()<end){
    if(fn())return;
    await new Promise(resolve=>setTimeout(resolve,25));
  }
  throw Error('Overlay event not delivered');
}
test('independent phone nodes discover each other and bootstrap an ICE connection',async()=>{
  const dir=fs.mkdtempSync(path.join(os.tmpdir(),'xyool-phone-mesh-'));
  const server=createIdServer({port:0,host:'127.0.0.1',
    registryPath:path.join(dir,'registry.json')});
  let a,b,c;
  try{
    await server.listen();
    const port=server.address().port;
    a=await phone(port,A,'a');b=await phone(port,B,'b');c=await phone(port,C,'c');
    a.send({type:'mesh-enable'});b.send({type:'mesh-enable'});
    await until(()=>a.received.some(x=>x.type==='mesh-peers'&&x.ids.includes(B)) &&
      b.received.some(x=>x.type==='mesh-peers'&&x.ids.includes(A)));
    assert(!a.received.find(x=>x.type==='mesh-peers').ids.includes(C),
      'nonparticipating phone must not be listed');
    const offer='v=0\r\n'+'x'.repeat(140);
    a.send({type:'mesh-signal',to:B,kind:'offer',sdp:offer});
    await until(()=>b.received.some(x=>x.type==='mesh-signal'&&x.kind==='offer'));
    const msg=b.received.find(x=>x.type==='mesh-signal');
    assert.equal(msg.from,A);
    assert.equal(msg.sdp,offer);
    // Hidden nonparticipating phones do not receive private signaling.
    a.send({type:'mesh-signal',to:C,kind:'offer',sdp:offer});
    await new Promise(resolve=>setTimeout(resolve,125));
    assert.equal(c.received.filter(x=>x.type==='mesh-signal').length,0);
    // Reject malformed signaling before emitting it.
    a.send({type:'mesh-signal',to:B,kind:'offer',sdp:'fake'});
    await new Promise(resolve=>setTimeout(resolve,125));
    assert.equal(b.received.filter(x=>x.type==='mesh-signal').length,1);
    b.send({type:'mesh-signal',to:A,kind:'candidate',
      candidate:'candidate:1 1 udp 1 192.0.2.1 10000 typ host',mid:'data',index:0});
    await until(()=>a.received.some(x=>x.type==='mesh-signal'&&x.kind==='candidate'));
    b.send({type:'mesh-disable'});
    await until(()=>a.received.some(x=>x.type==='mesh-peers'&&!x.ids.includes(B)));
  } finally {
    for(const p of [a,b,c])p?.ws.terminate();
    await server.close();
    fs.rmSync(dir,{recursive:true,force:true});
  }
});
