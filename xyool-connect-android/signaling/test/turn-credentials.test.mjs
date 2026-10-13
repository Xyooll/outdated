import test from 'node:test';
import assert from 'node:assert/strict';
import {createHmac} from 'node:crypto';
import {temporaryTurnCredentials} from '../turn/turn-credentials.mjs';

test('generates coturn-compatible expiring HMAC-SHA1 TURN REST credentials',()=>{
  const secret='xyool-test-not-production-shared-secret-0000001';
  const id='XY-ABCD-EFGH-JKLM';
  const r=temporaryTurnCredentials({secret,id,ttlSeconds:1800,now:1000000000000});
  assert.equal(r.expiresAt,1000001800);
  assert.equal(r.username,'1000001800:'+id);
  assert.equal(r.password,
    createHmac('sha1',secret).update(r.username).digest('base64'));
  assert.equal(r.password.length,28);
});
test('rejects invalid users, weak secrets, absurd expiries and times',()=>{
  const secret='xyool-test-not-production-shared-secret-0000001';
  assert.throws(()=>temporaryTurnCredentials({secret:'weak',id:'XY-ABCD-EFGH-JKLM'}));
  assert.throws(()=>temporaryTurnCredentials({secret,id:'bad'}));
  assert.throws(()=>temporaryTurnCredentials({secret,id:'XY-ABCD-EFGH-JKLM',ttlSeconds:999999}));
  assert.throws(()=>temporaryTurnCredentials({secret,id:'XY-ABCD-EFGH-JKLM',now:NaN}));
});
