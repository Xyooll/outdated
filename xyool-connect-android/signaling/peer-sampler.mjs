/**
 * Choose a bounded set of deterministic clockwise/counterclockwise Xyool
 * bootstrap neighbors, instead of always returning the first 16 registered
 * clients and starving the rest as the network grows.
 *
 * Discovery sampling is not identity verification; the separate signed
 * phone-key registry is responsible for that.
 */
export function chooseMeshPeers(own,candidates,max=16){
  if(!Number.isInteger(max)||max<1||max>32)throw Error('Invalid peer cap');
  const map=new Map();
  for(const p of candidates){
    if(p&&typeof p.id==='string'&&p.id!==own&&
       /^[a-f0-9]{64}$/.test(p.fp||''))map.set(p.id,p.fp);
  }
  const sorted=[...map].sort((a,b)=>a[0].localeCompare(b[0]));
  if(sorted.length<=max)return sorted.map(([id,fp])=>({id,fp}));
  // Insert own into the circle; spread sampling in both directions.
  const after=sorted.findIndex(([id])=>id.localeCompare(own)>0);
  const start=after<0?0:after;
  const out=[];
  const used=new Set();
  for(let distance=0;out.length<max&&distance<sorted.length;distance++){
    for(const index of [
      (start+distance)%sorted.length,
      (start-distance-1+sorted.length*2)%sorted.length
    ]){
      const [id,fp]=sorted[index];
      if(!used.has(id)){used.add(id);out.push({id,fp});}
      if(out.length===max)break;
    }
  }
  return out;
}
