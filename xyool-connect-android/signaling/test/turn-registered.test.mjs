import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {WebSocket} from 'ws';
import {createIdServer} from '../server-id.mjs';

test('only registered clients get a bounded TURN lease; no credential in /health',async()=>{
  const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'xyool-turn-'));
  let issued=0;
  const server=createIdServer({host:'127.0.0.1',port:0,
    registryPath:path.join(tmp,'registry.json'),
    turnIssuer:async()=>{
      issued++;
      return {type:'turn-credentials',ttlSec:7200,
        iceServers:[{urls:['turn:relay.example.com:3478?transport=udp'],
          username:'1800007200:mock',credential:'mock-value'}]};
    }});
  let ws;
  try{
    await server.listen();
    const {port}=server.address();
    const messages=[];
    ws=new WebSocket('ws://127.0.0.1:'+port+'/v1/id');
    await new Promise((resolve,reject)=>{
      ws.once('open',resolve);ws.once('error',reject);
    });
    ws.on('message',raw=>messages.push(JSON.parse(String(raw))));
    ws.send(JSON.stringify({type:'turn-refresh'})); // anonymous never gets TURN
    await new Promise(resolve=>setTimeout(resolve,50));
    assert.equal(issued,0);
    const id='XY-ABCD-EFGH-JKLM',token='a'.repeat(64);
    ws.send(JSON.stringify({type:'register',id,token}));
    await new Promise((resolve,reject)=>{
      let n=0;
      const tick=()=>{
        if(messages.some(x=>x.type==='turn-credentials'))resolve();
        else if(++n>100)reject(new Error('lease timeout'));
        else setTimeout(tick,10);
      };tick();
    });
    assert.equal(issued,1);
    assert.equal(messages.filter(x=>x.type==='turn-credentials').length,1);
    const lease=messages.find(x=>x.type==='turn-credentials');
    assert.deepEqual(lease.iceServers[0].urls,['turn:relay.example.com:3478?transport=udp']);
    ws.send(JSON.stringify({type:'turn-refresh'}));
    await new Promise(resolve=>setTimeout(resolve,75));
    assert.equal(issued,1); // five-minute per-socket cooldown
    const res=await fetch('http://127.0.0.1:'+port+'/health');
    assert.equal(res.status,200);
    assert.ok(!(await res.text()).includes('turn:'));
  }finally{
    if(ws)ws.terminate();
    await server.close();
    fs.rmSync(tmp,{recursive:true,force:true});
  }
});
