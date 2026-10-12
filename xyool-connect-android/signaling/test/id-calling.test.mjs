import {test} from 'node:test';
import assert from 'node:assert/strict';
import {once} from 'node:events';
import {mkdtempSync,rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {randomBytes} from 'node:crypto';
import {WebSocket} from 'ws';
import {createIdServer} from '../server-id.mjs';

const base=()=> 'XY-'+['ABCD','EFGH','JKLM'].join('-');
const second=()=> 'XY-'+['NPQR','STUV','WXYZ'].join('-');
const secret=()=>randomBytes(32).toString('hex');
function waitType(ws,type) {
 return new Promise((resolve,reject)=>{
  const timeout=setTimeout(()=>{ws.off('message',handle);reject(new Error('Timeout '+type));},3500);
  function handle(raw){
    const msg=JSON.parse(String(raw));
    if(msg.type!==type)return;
    clearTimeout(timeout);ws.off('message',handle);resolve(msg);
  }
  ws.on('message',handle);
 });
}
function send(ws,msg){ws.send(JSON.stringify(msg));}
async function connection(url){
 const s=new WebSocket(url);
 await once(s,'open');return s;
}
async function setup(fn) {
 const directory=mkdtempSync(join(tmpdir(),'xyool-id-test-'));
 const registryPath=join(directory,'registry.json');
 const server=createIdServer({host:'127.0.0.1',port:0,registryPath});
 await server.listen();
 const url='ws://127.0.0.1:'+server.address().port+'/v1/id';
 try{await fn({url,registryPath,server});}
 finally {await server.close();rmSync(directory,{recursive:true,force:true});}
}
async function register(url,id,token){
 const ws=await connection(url);
 const ready=waitType(ws,'registered');
 send(ws,{type:'register',id,token});
 assert.equal((await ready).id,id);
 return ws;
}

test('an ID registers, calls, accepts, and relays WebRTC negotiation',async()=>{
 await setup(async({url,server})=>{
  const a=await register(url,base(),secret()), b=await register(url,second(),secret());
  assert.equal(server.online(),2);
  const incoming=waitType(b,'incoming'),ringing=waitType(a,'ringing');
  send(a,{type:'call',to:second()});
  assert.equal((await incoming).from,base());
  await ringing;
  const aAccepted=waitType(a,'accepted'),bAccepted=waitType(b,'accepted');
  send(b,{type:'accept'}); await Promise.all([aAccepted,bAccepted]);
  const offer=waitType(b,'signal');
  const fakeSdp='v=0\r\n'+'s='.repeat(45);
  send(a,{type:'signal',kind:'offer',sdp:fakeSdp});
  assert.equal((await offer).sdp,fakeSdp);
  const answer=waitType(a,'signal');
  send(b,{type:'signal',kind:'answer',sdp:fakeSdp});
  assert.equal((await answer).kind,'answer');
  const candidate=waitType(b,'signal');
  send(a,{type:'signal',kind:'candidate',candidate:'candidate:1 1 udp 123 1.2.3.4 456 typ host',mid:'0',index:0});
  assert.equal((await candidate).kind,'candidate');
  const ended=waitType(a,'ended');
  send(b,{type:'hangup'}); await ended;
  a.close();b.close();
 });
});

test('IDs cannot be re-registered by a different token, even after reconnect',async()=>{
 await setup(async({url})=>{
  const id=base(),original=secret();
  const first=await register(url,id,original);
  await new Promise(res=>{first.once('close',res);first.close();});
  const attacker=await connection(url);
  const invalid=waitType(attacker,'error');
  send(attacker,{type:'register',id,token:secret()});
  assert.equal((await invalid).message,'This ID is already registered');
  await once(attacker,'close');
  const restored=await register(url,id,original);
  restored.close();
 });
});

test('offline, busy targets and nonmembers cannot force a call signal',async()=>{
 await setup(async({url})=>{
  const a=await register(url,base(),secret());
  const absent=waitType(a,'unavailable');
  send(a,{type:'call',to:second()});await absent;
  const b=await register(url,second(),secret());
  const incoming=waitType(b,'incoming');
  send(a,{type:'call',to:second()});await incoming;
  const busy=waitType(a,'error');
  send(a,{type:'call',to:second()});
  assert.equal((await busy).message,'Already in call');
  const rejected=waitType(a,'ended');
  send(b,{type:'reject'});assert.equal((await rejected).reason,'declined');
  a.close();b.close();
 });
});


test('registry survives a server restart and rejects a different owner',async()=>{
 const dir=mkdtempSync(join(tmpdir(),'xyool-id-restart-'));
 const db=join(dir,'registry.json');
 let service=createIdServer({host:'127.0.0.1',port:0,registryPath:db});
 try {
  await service.listen();
  const firstUrl='ws://127.0.0.1:'+service.address().port+'/v1/id';
  const owner=secret();
  const a=await register(firstUrl,base(),owner);
  await new Promise(resolve=>{a.once('close',resolve);a.close();});
  await service.close();
  service=createIdServer({host:'127.0.0.1',port:0,registryPath:db});
  await service.listen();
  const secondUrl='ws://127.0.0.1:'+service.address().port+'/v1/id';
  const fake=await connection(secondUrl);
  const err=waitType(fake,'error');
  send(fake,{type:'register',id:base(),token:secret()});
  assert.equal((await err).message,'This ID is already registered');
  await once(fake,'close');
  const restored=await register(secondUrl,base(),owner);
  restored.close();
 } finally {
  await service.close();
  rmSync(dir,{recursive:true,force:true});
 }
});

test('missing persistence directory rejects startup rather than losing IDs',()=>{
 const dir=join(tmpdir(),'xyool-missing-storage-'+randomBytes(8).toString('hex'));
 assert.throws(
   ()=>createIdServer({port:0,registryPath:join(dir,'registry.json')}),
   /Missing identity registry directory/
 );
});

test('health endpoint responds while server is running',async()=>{
 await setup(async({url})=>{
  const address=url.replace('ws://','http://').replace('/v1/id','/health');
  const response=await fetch(address);
  assert.equal(response.status,200);
  assert.deepEqual(await response.json(),{ok:true});
 });
});
