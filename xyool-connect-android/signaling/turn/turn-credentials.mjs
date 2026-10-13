import {createHmac} from 'node:crypto';

const ID=/^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$/;

/**
 * Coturn's TURN REST credential format (HMAC-SHA1, per TURN REST draft).
 * Execute ONLY on an operator-controlled machine. Never ship the secret in
 * an APK, a QR code, or public frontend; clients get only scoped credentials.
 */
export function temporaryTurnCredentials({
  secret,id,ttlSeconds=3600,now=Date.now()
}={}){
  if(typeof secret!=='string'||secret.length<32)
    throw new Error('Turn on TURN only with a strong 32+ character private secret');
  if(!ID.test(id||''))throw new Error('Expected a valid Xyool ID');
  if(!Number.isSafeInteger(ttlSeconds)||ttlSeconds<60||ttlSeconds>86400)
    throw new Error('TTL must be between 60 and 86400 seconds');
  if(!Number.isFinite(now)||now<0)throw new Error('Invalid clock');
  const expiresAt=Math.floor(now/1000)+ttlSeconds;
  const username=expiresAt+':'+id;
  const password=createHmac('sha1',secret).update(username).digest('base64');
  return {username,password,expiresAt};
}

if(import.meta.url===new URL('file://'+process.argv[1]).href){
  try{
    const id=process.argv[2];
    const ttlSeconds=process.argv[3]?Number(process.argv[3]):3600;
    const result=temporaryTurnCredentials({
      secret:process.env.XYOOL_TURN_SHARED_SECRET,id,ttlSeconds
    });
    console.log(JSON.stringify(result,null,2));
  }catch(err){
    console.error(err.message);
    process.exitCode=1;
  }
}
