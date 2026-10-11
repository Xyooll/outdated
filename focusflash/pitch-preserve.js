// Pitch-preserving speech transport. Entirely local, no model or CDN.
// Browser HTMLMediaElement.preservesPitch handles normal tempo changes.
// Beyond 3.5x, a small overlap/add pre-compressor keeps the HTML audio
// playback inside the range of reliably supported pitch correction.
// Very large compression will sound choppy, but not squeaky.
const MAX_NATIVE_RATE = 3.5;
const MAX_FACTOR = 24;
let cachedSource=null, cachedRatio=0, cachedSamples=null;

export function supportedPitchPreservation(){
  return typeof Audio !== "undefined" && "preservesPitch" in new Audio();
}

function encodeWav(samples, sampleRate){
  const bytes=new ArrayBuffer(44+samples.length*2),v=new DataView(bytes);
  const put=(at,str)=>{for(let i=0;i<str.length;i++)v.setUint8(at+i,str.charCodeAt(i));};
  put(0,"RIFF");v.setUint32(4,36+samples.length*2,true);put(8,"WAVE");
  put(12,"fmt ");v.setUint32(16,16,true);v.setUint16(20,1,true);
  v.setUint16(22,1,true);v.setUint32(24,sampleRate,true);
  v.setUint32(28,sampleRate*2,true);v.setUint16(32,2,true);
  v.setUint16(34,16,true);put(36,"data");v.setUint32(40,samples.length*2,true);
  for(let i=0;i<samples.length;i++){
    const x=Math.max(-1,Math.min(1,samples[i]));
    v.setInt16(44+i*2,Math.round(x<0?x*32768:x*32767),true);
  }
  return new Blob([bytes],{type:"audio/wav"});
}
function clamp(value,min,max){return Math.max(min,Math.min(max,value));}
function tick(){return new Promise(resolve=>setTimeout(resolve,0));}

// Offline WSOLA-like overlap/add: skip speech segments but preserve their
// original sample rate. A best-match search reduces clicks at joins.
// The result preserves pitch approximately, not every syllable.
async function compressPreservingPitch(source, factor, onProgress){
  const input=source.getChannelData(0);
  const n=input.length;
  const length=Math.max(1024,Math.ceil(n/factor));
  const result=new Float32Array(length);
  const weight=new Float32Array(length);
  const window=1024,hop=256,search=128,correlation=256;
  const hann=new Float32Array(window);
  for(let j=0;j<window;j++)hann[j]=.5-.5*Math.cos(2*Math.PI*(j+.5)/window);
  let frames=0;
  for(let dest=0;dest<length;dest+=hop){
    const guess=Math.round(dest*factor);
    if(guess>=n-8)break;
    let src=clamp(guess,0,Math.max(0,n-window));
    if(dest>0){
      let best=-Infinity,bestSrc=src;
      const min=Math.max(0,src-search),max=Math.min(n-window,src+search);
      for(let candidate=min;candidate<=max;candidate+=8){
        let dot=0,aEnergy=1e-8,bEnergy=1e-8;
        for(let j=0;j<correlation;j+=4){
          const y=dest+j;if(y>=length)break;
          const a=result[y]/Math.max(.00001,weight[y]),b=input[candidate+j];
          dot+=a*b;aEnergy+=a*a;bEnergy+=b*b;
        }
        const sim=dot/Math.sqrt(aEnergy*bEnergy);
        if(sim>best){best=sim;bestSrc=candidate;}
      }
      src=bestSrc;
    }
    const take=Math.min(window,length-dest,n-src);
    for(let j=0;j<take;j++){
      const windowValue=hann[j];
      result[dest+j]+=input[src+j]*windowValue;
      weight[dest+j]+=windowValue;
    }
    frames++;
    if(frames%240===0){
      onProgress?.("Preserving the natural voice tone: "+Math.min(99,Math.round(dest/length*100))+"%");
      await tick();
    }
  }
  for(let j=0;j<length;j++)result[j]=weight[j]>.00001?result[j]/weight[j]:0;
  return result;
}

export async function makePitchPreservedVoice({context,buffer,rate,volume,destination,onProgress}){
  if(!supportedPitchPreservation())
    throw new Error("Pitch preservation is unavailable. Update Chrome; audio will not be pitch-shifted.");
  if(!buffer||!Number.isFinite(rate)||rate<=0)
    throw new Error("Invalid narration or playback speed.");
  if(rate>MAX_FACTOR)
    throw new Error("This WPM would require more than 24x speech compression. Lower WPM to retain a human-sounding undertone.");
  const compressedFactor=rate>MAX_NATIVE_RATE?rate/MAX_NATIVE_RATE:1;
  const playbackRate=rate/compressedFactor;
  let samples;
  if(compressedFactor>1){
    if(cachedSource===buffer && Math.abs(cachedRatio-compressedFactor)<.0001)
      samples=cachedSamples;
    else{
      onProgress?.("Preparing natural-pitch speech without raising its tone…");
      samples=await compressPreservingPitch(buffer,compressedFactor,onProgress);
      cachedSource=buffer;cachedRatio=compressedFactor;cachedSamples=samples;
    }
  }else samples=buffer.getChannelData(0);
  const url=URL.createObjectURL(encodeWav(samples,buffer.sampleRate));
  const element=new Audio();
  element.preload="auto";
  element.preservesPitch=true;
  element.mozPreservesPitch=true;
  element.src=url;
  const source=context.createMediaElementSource(element);
  const gain=context.createGain();
  gain.gain.value=clamp(volume,0,1);
  source.connect(gain);
  gain.connect(destination);
  let disposed=false;
  let endedCallback=null;
  element.onended=()=>endedCallback?.();
  const dispose=()=>{
    if(disposed)return;
    disposed=true;
    endedCallback=null;
    element.pause();
    element.removeAttribute("src");
    element.load();
    source.disconnect();gain.disconnect();
    URL.revokeObjectURL(url);
  };
  const start=async (originalOffset=0)=>{
    if(disposed)throw Error("Audio source has been closed.");
    const offset=clamp(originalOffset/compressedFactor,0,Math.max(0,samples.length/buffer.sampleRate-.02));
    if(element.readyState<1)await new Promise((resolve,reject)=>{
      const timer=setTimeout(()=>{cleanup();reject(Error("The browser took too long to decode the voice."));},12000);
      const cleanup=()=>{clearTimeout(timer);element.removeEventListener("loadedmetadata",loaded);element.removeEventListener("error",error);};
      const loaded=()=>{cleanup();resolve();};
      const error=()=>{cleanup();reject(Error("The phone couldn't play generated WAV audio."));};
      element.addEventListener("loadedmetadata",loaded,{once:true});
      element.addEventListener("error",error,{once:true});
      element.load();
    });
    element.currentTime=offset;
    element.playbackRate=playbackRate;
    element.preservesPitch=true;
    await element.play();
  };
  return {
    element,gain,playbackRate,compressedFactor,
    start,dispose,
    setVolume(value){gain.gain.setTargetAtTime(clamp(value,0,1),context.currentTime,.03);},
    onEnded(fn){endedCallback=fn;}
  };
}
