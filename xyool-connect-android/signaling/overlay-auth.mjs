import {createHash,createPublicKey,verify} from 'node:crypto';

export const canonicalFields=(...values)=>values.map(v=>{
  const text=String(v);
  return text.length+':'+text;
}).join('');
export const enableProof=(id,ts)=>
  'xyool-peer-enable-v1|'+canonicalFields(id,ts);
export const signalProof=(from,to,kind,ts,sdp='',candidate='',mid='',index=-1)=>
  'xyool-peer-signal-v1|'+canonicalFields(from,to,kind,ts,sdp,candidate,mid,index);

export function verifiedPublicKey(encoded,signature,data){
  try{
    if(typeof encoded!=='string'||encoded.length>300||encoded.length<90||
       typeof signature!=='string'||signature.length>220)return null;
    const der=Buffer.from(encoded,'base64');
    if(der.length<80||der.length>160||der.toString('base64')!==encoded)return null;
    const key=createPublicKey({key:der,format:'der',type:'spki'});
    if(key.asymmetricKeyType!=='ec'||key.asymmetricKeyDetails?.namedCurve!=='prime256v1')
      return null;
    const sig=Buffer.from(signature,'base64');
    if(!sig.length||sig.length>90||sig.toString('base64')!==signature)return null;
    if(!verify('sha256',Buffer.from(data,'utf8'),key,sig))return null;
    return {fingerprint:createHash('sha256').update(der).digest('hex')};
  }catch{return null;}
}
