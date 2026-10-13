import test from 'node:test';
import assert from 'node:assert/strict';
import {chooseMeshPeers} from '../peer-sampler.mjs';

test('ring sampling fairly includes neighbors for a phone near the end',()=>{
  const suffixes='ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  const ids=[...suffixes].map(c=>'XY-'+c+'BCD-EFGH-JKLM');
  const options=ids.map(id=>({id,fp:'a'.repeat(64)}));
  const end=ids[ids.length-1];
  const chosen=chooseMeshPeers(end,options,6);
  assert.equal(chosen.length,6);
  assert(chosen.some(x=>x.id===ids[0]),'ring must wrap around');
  assert(chosen.some(x=>x.id===ids[ids.length-2]),'must include near predecessor');
  assert.equal(new Set(chosen.map(x=>x.id)).size,6);
});
test('malformed peer fingerprint is excluded',()=>{
  assert.deepEqual(chooseMeshPeers('XY-ABCD-EFGH-JKLM',[
    {id:'XY-MNPQ-RSTU-VWXY',fp:'not-a-hash'}
  ]),[]);
  assert.throws(()=>chooseMeshPeers('XY-ABCD-EFGH-JKLM',[],500));
});
