import test from 'node:test';
import assert from 'node:assert/strict';
import {createHmac} from 'node:crypto';
import {makeTurnIssuer,normalizeIceServers,validIceUrl} from '../turn-lease.mjs';

test('disabled by default, never silently use public relay',()=>{
  assert.equal(makeTurnIssuer({}),null);
  assert.throws(()=>makeTurnIssuer({XYOOL_TURN_PROVIDER:'not-a-provider'}));
});
test('coturn shared secret signs an expiring username without disclosing secret',async()=>{
  const secret='s'.repeat(48);
  const issuer=makeTurnIssuer({XYOOL_TURN_PROVIDER:'coturn',
    XYOOL_TURN_SHARED_SECRET:secret,
    XYOOL_TURN_URLS:'turn:relay.example.com:3478?transport=udp,turn:relay.example.com:3478?transport=tcp'},
    {now:()=>1_800_000_000_000});
  const a=await issuer(),b=await issuer();
  assert.equal(a.type,'turn-credentials');
  assert.equal(a.ttlSec,7200);
  assert.notEqual(a.iceServers[0].username,b.iceServers[0].username);
  assert.equal(a.iceServers[0].credential,
    createHmac('sha1',secret).update(a.iceServers[0].username).digest('base64'));
  assert.ok(a.iceServers[0].username.startsWith('1800007200:'));
  assert.ok(!JSON.stringify(a).includes(secret));
});
test('invalid secret and illegal transport/addresses rejected',()=>{
  assert.throws(()=>makeTurnIssuer({XYOOL_TURN_PROVIDER:'coturn',
    XYOOL_TURN_SHARED_SECRET:'short',XYOOL_TURN_URLS:'turn:relay.example.com:3478'}));
  assert.equal(validIceUrl('turn:relay.example.com:3478?transport=tcp'),true);
  assert.equal(validIceUrl('turn:https://evil.example.com:3478'),false);
  assert.equal(validIceUrl('turn:relay.example.com:99999'),false);
  assert.equal(validIceUrl('http://example.com'),false);
  assert.throws(()=>normalizeIceServers([{urls:['http://example.com'],username:'x',credential:'y'}]));
  assert.throws(()=>normalizeIceServers([{urls:['turn:relay.example.com:3478']}]));
});
test('Cloudflare uses server-only bearer token and validates returned ICE servers',async()=>{
  const token='t'.repeat(48),keyId='a'.repeat(32);
  let requests=0;
  const fetchImpl=async(url,opts)=>{
    requests++;
    assert.ok(url.endsWith(keyId+'/credentials/generate-ice-servers'));
    assert.equal(opts.headers.Authorization,'Bearer '+token);
    assert.deepEqual(JSON.parse(opts.body),{ttl:7200});
    return {ok:true,json:async()=>({iceServers:[
      {urls:['stun:stun.cloudflare.com:3478']},
      {urls:['turn:turn.cloudflare.com:3478?transport=udp',
        'turns:turn.cloudflare.com:5349?transport=tcp'],
       username:'ephemeral-user',credential:'ephemeral-password'}
    ]})};
  };
  const issuer=makeTurnIssuer({XYOOL_TURN_PROVIDER:'cloudflare',
    XYOOL_CF_TURN_KEY_ID:keyId,XYOOL_CF_TURN_API_TOKEN:token},{fetchImpl});
  const lease=await issuer();
  assert.equal(requests,1);
  assert.equal(lease.iceServers.length,2);
  assert.ok(lease.iceServers.some(item=>item.username==='ephemeral-user'));
  assert.ok(!JSON.stringify(lease).includes(token));
});
test('Cloudflare provider errors fail closed',async()=>{
  const env={XYOOL_TURN_PROVIDER:'cloudflare',
    XYOOL_CF_TURN_KEY_ID:'a'.repeat(32),XYOOL_CF_TURN_API_TOKEN:'z'.repeat(48)};
  await assert.rejects(makeTurnIssuer(env,
    {fetchImpl:async()=>({ok:false,status:403})})());
  await assert.rejects(makeTurnIssuer(env,
    {fetchImpl:async()=>({ok:true,json:async()=>({iceServers:[]})})})());
});
