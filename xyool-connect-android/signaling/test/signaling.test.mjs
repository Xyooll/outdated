import { test } from 'node:test';
import assert from 'node:assert/strict';
import { once } from 'node:events';
import { WebSocket } from 'ws';
import { randomBytes } from 'node:crypto';
import { createSignalingServer } from '../server.mjs';

function next(ws, type) {
  return new Promise((resolve,reject) => {
    const timeout=setTimeout(() => {
      ws.off('message',onMessage);
      reject(new Error('Timed out: '+type));
    }, 3000);
    function onMessage(data) {
      const msg=JSON.parse(String(data));
      if (msg.type!==type) return;
      clearTimeout(timeout);
      ws.off('message',onMessage);
      resolve(msg);
    }
    ws.on('message',onMessage);
  });
}
const token=()=>randomBytes(16).toString('base64url');

async function connect(url) {
  const client=new WebSocket(url);
  await once(client,'open');
  return client;
}
async function withServer(fn) {
  const service=createSignalingServer({port:0,host:'127.0.0.1'});
  await service.listen();
  const port=service.address().port;
  try{await fn('ws://127.0.0.1:'+port+'/v1/voice',service);}
  finally{await service.close();}
}

test('two private participants connect and relay offer and answer',async()=>{
 await withServer(async(url,service)=>{
  const first=await connect(url);
  const second=await connect(url);
  const room=token();
  const firstJoined=next(first,'joined');
  first.send(JSON.stringify({type:'join',room}));
  assert.equal((await firstJoined).peers,1);
  const firstReady=next(first,'peer-ready');
  const secondJoined=next(second,'joined');
  const secondReady=next(second,'peer-ready');
  second.send(JSON.stringify({type:'join',room}));
  assert.equal((await secondJoined).peers,2);
  await Promise.all([firstReady,secondReady]);
  assert.equal(service.roomCount(),1);
  const offer=next(second,'offer');
  first.send(JSON.stringify({type:'offer',payload:'sdp-offer-data'}));
  assert.equal((await offer).payload,'sdp-offer-data');
  const answer=next(first,'answer');
  second.send(JSON.stringify({type:'answer',payload:'sdp-answer-data'}));
  assert.equal((await answer).payload,'sdp-answer-data');
  const left=next(second,'peer-left');
  first.close();
  await left;
  second.close();
 });
});

test('reject invalid tokens and third participant',async()=>{
 await withServer(async(url)=>{
  const invalid=await connect(url);
  const invalidClose=once(invalid,'close');
  invalid.send(JSON.stringify({type:'join',room:'bad'}));
  await invalidClose;

  const room=token();
  const c1=await connect(url);
  const c2=await connect(url);
  const c3=await connect(url);
  const j1=next(c1,'joined');c1.send(JSON.stringify({type:'join',room}));await j1;
  const j2=next(c2,'joined');c2.send(JSON.stringify({type:'join',room}));await j2;
  const fullClose=once(c3,'close');
  c3.send(JSON.stringify({type:'join',room}));
  await fullClose;
  c1.close();c2.close();
 });
});

test('separate secrets have isolated sessions',async()=>{
 await withServer(async(url)=>{
  const a=await connect(url);
  const b=await connect(url);
  const aJoin=next(a,'joined');
  a.send(JSON.stringify({type:'join',room:token()}));
  await aJoin;
  const bJoin=next(b,'joined');
  b.send(JSON.stringify({type:'join',room:token()}));
  await bJoin;
  const waiting=next(a,'waiting');
  a.send(JSON.stringify({type:'offer',payload:'not-forwarded'}));
  await waiting;
  a.close();b.close();
 });
});
