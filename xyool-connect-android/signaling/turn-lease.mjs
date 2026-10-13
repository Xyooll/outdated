import { createHmac, randomBytes } from 'node:crypto';

const host=/^[A-Za-z0-9.-]{1,253}$/;
const uri=/^(stun|stuns|turn|turns):([A-Za-z0-9.-]{1,253}):([0-9]{2,5})(?:\?transport=(udp|tcp))?$/;
const TTL_SEC=7200;
export const validIceUrl=url=>{
  if(typeof url!=='string'||url.length>320)return false;
  const m=uri.exec(url);return !!m&&host.test(m[2])&&Number(m[3])>=1&&
    Number(m[3])<=65535&&(!m[4]||m[1].startsWith('turn'));
};
export function normalizeIceServers(raw){
  if(!Array.isArray(raw)||raw.length>8)throw new Error('Invalid TURN response');
  const list=[];
  for(const input of raw){
    if(!input||typeof input!=='object')throw new Error('Invalid ICE entry');
    const urls=typeof input.urls==='string'?[input.urls]:input.urls;
    if(!Array.isArray(urls)||urls.length<1||urls.length>8||
       !urls.every(validIceUrl))throw new Error('Invalid ICE URLs');
    const relays=urls.filter(x=>x.startsWith('turn'));
    const stuns=urls.filter(x=>x.startsWith('stun'));
    if(relays.length){
      if(typeof input.username!=='string'||input.username.length<1||
         input.username.length>256||typeof input.credential!=='string'||
         input.credential.length<1||input.credential.length>512)
        throw new Error('Invalid TURN lease');
      list.push({urls:relays,username:input.username,credential:input.credential});
    }
    if(stuns.length)list.push({urls:stuns});
  }
  if(!list.some(x=>x.username))throw new Error('No TURN relay credentials available');
  return list;
}
/** Providers are optional. Nothing is issued unless explicitly configured. */
export function makeTurnIssuer(env=process.env,{fetchImpl=fetch,now=()=>Date.now()}={}){
  const provider=(env.XYOOL_TURN_PROVIDER||'').trim().toLowerCase();
  if(!provider)return null;
  if(provider==='coturn'){
    const secret=env.XYOOL_TURN_SHARED_SECRET||'';
    if(secret.length<32)throw new Error('TURN shared secret must be 32+ characters');
    const urls=(env.XYOOL_TURN_URLS||'').split(',').map(x=>x.trim()).filter(Boolean);
    if(!urls.length||urls.length>6||urls.some(x=>!validIceUrl(x)||!x.startsWith('turn')))
      throw new Error('Invalid TURN relay URLs');
    return async()=>{
      const username=Math.floor(now()/1000+TTL_SEC)+':'+randomBytes(12).toString('hex');
      const credential=createHmac('sha1',secret).update(username).digest('base64');
      return {type:'turn-credentials',ttlSec:TTL_SEC,
        iceServers:normalizeIceServers([{urls,username,credential}])};
    };
  }
  if(provider==='cloudflare'){
    const keyId=env.XYOOL_CF_TURN_KEY_ID||'';
    const apiToken=env.XYOOL_CF_TURN_API_TOKEN||'';
    if(!/^[a-f0-9]{32}$/i.test(keyId)||apiToken.length<16||
       apiToken.length>512)throw new Error('Cloudflare TURN configuration incomplete');
    return async()=>{
      const url='https://rtc.live.cloudflare.com/v1/turn/keys/'+keyId+
        '/credentials/generate-ice-servers';
      const response=await fetchImpl(url,{
        method:'POST',
        headers:{Authorization:'Bearer '+apiToken,'Content-Type':'application/json'},
        body:JSON.stringify({ttl:TTL_SEC}),
        signal:AbortSignal.timeout(6000)
      });
      if(!response.ok)throw new Error('TURN provider denied lease');
      const body=await response.json();
      return {type:'turn-credentials',ttlSec:TTL_SEC,
        iceServers:normalizeIceServers(body.iceServers)};
    };
  }
  throw new Error('Unsupported TURN provider');
}
