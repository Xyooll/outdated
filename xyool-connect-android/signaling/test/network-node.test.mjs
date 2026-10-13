import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {WebSocket} from 'ws';
import {generateKeyPairSync,sign} from 'node:crypto';
import {enableProof,signalProof} from '../overlay-auth.mjs';
import {createXyoolNetworkNode} from '../network-node.mjs';

const A='XY-ABCD-EFGH-JKLM';
const B='XY-MNPQ-RSTU-VWXY';
const C='XY-2345-6789-ABCD';
const KEY='xyool-network-test-bootstrap-secret-00000001';
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function until(check,timeout=12000){
  const started=Date.now();
  while(Date.now()-started<timeout){
    if(check())return;
    await sleep(30);
  }
  throw Error('Network path not ready before timeout');
}
async function client(port){
  const ws=new WebSocket('ws://127.0.0.1:'+port+'/v1/id');
  await new Promise((ok,fail)=>{
    ws.once('open',ok);ws.once('error',fail);
  });
  const queued=[],waiting=[];
  ws.on('message',raw=>{
    const v=JSON.parse(raw.toString());
    const at=waiting.findIndex(x=>x.type===v.type);
    if(at>=0){const q=waiting.splice(at,1)[0];clearTimeout(q.timer);q.resolve(v);}
    else queued.push(v);
  });
  return {
    ws,
    send:v=>ws.send(JSON.stringify(v)),
    next:(type,timeout=7000)=>{
      const i=queued.findIndex(x=>x.type===type);
      if(i>=0)return Promise.resolve(queued.splice(i,1)[0]);
      return new Promise((resolve,reject)=>{
        const waiter={type,resolve,timer:null};
        waiter.timer=setTimeout(()=>{
          const at=waiting.indexOf(waiter);
          if(at>=0)waiting.splice(at,1);
          reject(Error('Missing '+type+'; observed '+JSON.stringify(queued.map(x=>x.type))));
        },timeout);
        waiting.push(waiter);
      });
    }
  };
}
async function node(dir,id,peerUrls=[],secret=KEY){
  const inst=createXyoolNetworkNode({
    port:0,host:'127.0.0.1',nodeId:id,peerUrls,networkSecret:secret,
    registryPath:path.join(dir,id+'.json')
  });
  await inst.listen();
  return {inst,port:inst.address().port};
}
function reg(c,id,t){
  c.send({type:'register',id,token:t.repeat(64)});
  return c.next('registered');
}
test('two independent Xyool nodes deliver Call → Ring → Answer → SDP/ICE → Hang Up',async()=>{
  const dir=fs.mkdtempSync(path.join(os.tmpdir(),'xyool-net-'));
  let n1,n2,alice,bob;
  try{
    n1=await node(dir,'origin');
    n2=await node(dir,'neighbor',['ws://127.0.0.1:'+n1.port+'/v1/mesh']);
    alice=await client(n1.port);bob=await client(n2.port);
    assert.equal((await reg(alice,A,'a')).id,A);
    assert.equal((await reg(bob,B,'b')).id,B);
    await until(()=>n1.inst.stats().remote===1&&n2.inst.stats().remote===1);
    assert.equal(n1.inst.stats().neighbors,1);
    assert.equal(n2.inst.stats().neighbors,1);
    alice.send({type:'call',to:B});
    assert.equal((await bob.next('incoming')).from,A);
    await alice.next('ringing'); // only once the receiver node accepts the invitation
    bob.send({type:'accept'});
    await alice.next('accepted');await bob.next('accepted');
    const offer='v=0\r\n'+'a'.repeat(100);
    const answer='v=0\r\n'+'b'.repeat(100);
    alice.send({type:'signal',kind:'offer',sdp:offer});
    assert.equal((await bob.next('signal')).sdp,offer);
    bob.send({type:'signal',kind:'answer',sdp:answer});
    assert.equal((await alice.next('signal')).sdp,answer);
    alice.send({type:'signal',kind:'candidate',candidate:'candidate:1 1 udp 1 192.0.2.1 1000 typ host',mid:'audio',index:0});
    assert.equal((await bob.next('signal')).kind,'candidate');
    alice.send({type:'hangup'});
    assert.equal((await bob.next('ended')).reason,'hung-up');
    await alice.next('ended');
    alice.send({type:'call',to:C});
    await alice.next('unavailable');
  }finally{
    alice?.ws.terminate();bob?.ws.terminate();
    await n2?.inst.close();await n1?.inst.close();
    fs.rmSync(dir,{recursive:true,force:true});
  }
});
test('presence gossip and audio signaling traverse multiple independent nodes',async()=>{
  const dir=fs.mkdtempSync(path.join(os.tmpdir(),'xyool-net-'));
  let a,b,c,caller,receiver;
  try{
    a=await node(dir,'mesh-one');
    b=await node(dir,'mesh-two',['ws://127.0.0.1:'+a.port+'/v1/mesh']);
    c=await node(dir,'mesh-three',['ws://127.0.0.1:'+b.port+'/v1/mesh']);
    caller=await client(a.port);receiver=await client(c.port);
    await reg(caller,A,'a');await reg(receiver,C,'c');
    // Re-announcement every 10 sec also synchronizes peers joining mid-flight.
    await until(()=>a.inst.stats().remote===1&&c.inst.stats().remote===1,15000);
    caller.send({type:'call',to:C});
    assert.equal((await receiver.next('incoming')).from,A);
    await caller.next('ringing');
    receiver.send({type:'reject'});
    assert.equal((await caller.next('ended')).reason,'declined');
  }finally{
    caller?.ws.terminate();receiver?.ws.terminate();
    await c?.inst.close();await b?.inst.close();await a?.inst.close();
    fs.rmSync(dir,{recursive:true,force:true});
  }
});
test('mesh rejects peers without matching operator secret',async()=>{
  const dir=fs.mkdtempSync(path.join(os.tmpdir(),'xyool-net-'));
  let a,b;
  try{
    a=await node(dir,'correct');
    b=await node(dir,'wrong',['ws://127.0.0.1:'+a.port+'/v1/mesh'],
      'different-secret-0000000000000000000000000000000');
    await sleep(450);
    assert.equal(a.inst.stats().neighbors,0);
    assert.equal(b.inst.stats().neighbors,0);
  }finally{
    await b?.inst.close();await a?.inst.close();
    fs.rmSync(dir,{recursive:true,force:true});
  }
});

function meshIdentity(id){
  const {publicKey,privateKey}=generateKeyPairSync('ec',{namedCurve:'prime256v1'});
  const authKey=publicKey.export({format:'der',type:'spki'}).toString('base64');
  const signature=message=>sign('sha256',Buffer.from(message),privateKey).toString('base64');
  return {
    enable:client=>{
      const authTs=Date.now();
      client.send({type:'mesh-enable',authTs,authKey,
        authSig:signature(enableProof(id,authTs))});
    },
    signal:(client,to,kind,details={})=>{
      const authTs=Date.now();
      const sdp=details.sdp||'',candidate=details.candidate||'',
        mid=details.mid||'',index=details.index??-1;
      client.send({type:'mesh-signal',to,kind,...details,authTs,authKey,
        authSig:signature(signalProof(id,to,kind,authTs,sdp,candidate,mid,index))});
    }
  };
}
async function roster(client,target){
  for(let i=0;i<8;i++){
    const seen=await client.next('mesh-peers',15000);
    if(seen.ids.includes(target))return seen;
  }
  throw Error('Remote peer missing from signed federation roster');
}
test('three independently hosted rendezvous nodes bootstrap signed Android peer overlay',async()=>{
  const dir=fs.mkdtempSync(path.join(os.tmpdir(),'xyool-federated-phones-'));
  let a,b,c,left,right;
  try{
    a=await node(dir,'overlay-A');
    b=await node(dir,'overlay-B',['ws://127.0.0.1:'+a.port+'/v1/mesh']);
    c=await node(dir,'overlay-C',['ws://127.0.0.1:'+b.port+'/v1/mesh']);
    left=await client(a.port);right=await client(c.port);
    await reg(left,A,'a');await reg(right,C,'c');
    const leftKey=meshIdentity(A),rightKey=meshIdentity(C);
    leftKey.enable(left);rightKey.enable(right);
    await until(()=>a.inst.stats().remoteMesh===1&&c.inst.stats().remoteMesh===1,15000);
    const lr=await roster(left,C);
    const rl=await roster(right,A);
    assert.match(lr.pins[C],/^[a-f0-9]{64}$/);
    assert.match(rl.pins[A],/^[a-f0-9]{64}$/);
    const offer='v=0\r\n'+'d'.repeat(145);
    leftKey.signal(left,C,'offer',{sdp:offer});
    const delivered=await right.next('mesh-signal');
    assert.equal(delivered.from,A);
    assert.equal(delivered.sdp,offer);
    assert.equal(delivered.kind,'offer');
    left.send({type:'mesh-signal',to:C,kind:'offer',sdp:offer,
      authKey:'invalid',authTs:Date.now(),authSig:'invalid'});
    await sleep(170);
    // Unsigned attack did not arrive and cannot forge the relay.
    rightKey.signal(right,A,'answer',{sdp:'v=0\r\n'+'a'.repeat(145)});
    assert.equal((await left.next('mesh-signal')).kind,'answer');
    right.send({type:'mesh-disable'});
    await sleep(100);
    leftKey.signal(left,C,'offer',{sdp:offer});
    await sleep(150);
  }finally{
    left?.ws.terminate();right?.ws.terminate();
    await c?.inst.close();await b?.inst.close();await a?.inst.close();
    fs.rmSync(dir,{recursive:true,force:true});
  }
});
