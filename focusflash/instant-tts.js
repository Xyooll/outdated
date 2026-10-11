// FocusFlash instant speech: device voice for Play; compact local eSpeak for export.
// Native speechSynthesis begins without model downloads or prerecording.
// Browser speech output cannot be recorded into Canvas MediaRecorder, so
// export uses bundled GPLv3 eSpeakNG (~3 MB initial voice data, then cache).
let generation=0;
let activeUtterance=null;
let espeakPromise=null,espeak=null;

export function stopInstantSpeech(){
 generation++;
 try{window.speechSynthesis?.cancel();}catch{}
 activeUtterance=null;
}
function parts(text,maxLength=210){
 const tokens=String(text||"").split(/\s+/).filter(Boolean),pieces=[];
 let part="";
 for(const token of tokens){
  if(part && part.length+token.length+1>maxLength){
   pieces.push(part);part=token;
  }else part+=(part?" ":"")+token;
 }
 if(part)pieces.push(part);
 return pieces;
}
export function speakInstant(text,{rate=1,volume=.18}={}){
 stopInstantSpeech();
 if(!window.speechSynthesis||!window.SpeechSynthesisUtterance)
  throw Error("No built-in text-to-speech voice is installed or exposed by this browser.");
 if(!String(text).trim())return;
 const token=generation,fragments=parts(text);
 const voice=window.speechSynthesis.getVoices().find(v=>
  /^en[-_]/i.test(v.lang)&&v.localService)||
  window.speechSynthesis.getVoices().find(v=>/^en/i.test(v.lang))||null;
 let i=0;
 const next=()=>{
  if(token!==generation||i>=fragments.length)return;
  const sentence=new SpeechSynthesisUtterance(fragments[i++]);
  sentence.lang=voice?.lang||"en-US";
  if(voice)sentence.voice=voice;
  sentence.pitch=1; // keep natural voice pitch
  sentence.volume=Math.max(0,Math.min(1,volume));
  sentence.rate=Math.max(.5,Math.min(10,rate));
  sentence.onend=()=>{if(token===generation)next();};
  sentence.onerror=e=>{
   if(e.error==="canceled"||e.error==="interrupted")return;
   if(token===generation)next();
  };
  activeUtterance=sentence;
  window.speechSynthesis.speak(sentence);
 };
 next();
}
function loadScript(url){
 return new Promise((resolve,reject)=>{
  if(window.SimpleTTS){resolve();return;}
  const script=document.createElement("script");
  script.src=url;script.async=true;
  script.onload=()=>window.SimpleTTS?resolve():reject(Error("eSpeak script did not initialize."));
  script.onerror=()=>reject(Error("Could not load the compact local speech engine."));
  document.head.appendChild(script);
 });
}
export async function getFastExportEngine(onProgress){
 if(espeak)return espeak;
 if(!espeakPromise){
  espeakPromise=(async()=>{
   onProgress?.("Preparing small offline speech engine (about 3 MB once)...");
   await loadScript("./vendor/espeakng-simple.js");
   const synth=new window.SimpleTTS({
    workerPath:"./vendor/espeakng.worker.js",
    defaultVoice:"en",defaultRate:230,enhanceAudio:false
   });
   await new Promise((resolve,reject)=>{
    let settled=false;
    const timeout=setTimeout(()=>{
     if(settled)return;
     settled=true;try{synth.worker?.terminate();}catch{}
     reject(Error("Local speech engine startup timed out. Check internet on first use."));
    },30000);
    synth.onReady(error=>{
     if(settled)return;settled=true;clearTimeout(timeout);
     if(error)reject(Error(error.message||"Local speech engine failed to start."));
     else resolve();
    });
   });
   return synth;
  })();
 }
 try{espeak=await espeakPromise;return espeak;}
 catch(error){espeakPromise=null;throw error;}
}
export async function generateInstantExportSpeech(text,onProgress){
 const chunks=parts(text,145);
 if(!chunks.length)throw Error("Paste text first.");
 if(chunks.length>95)throw Error("This passage is too long for a single phone export. Split into chapters.");
 const synth=await getFastExportEngine(onProgress);
 const results=[];
 for(let i=0;i<chunks.length;i++){
  onProgress?.("Preparing video narration: "+(i+1)+" / "+chunks.length);
  const result=await new Promise((resolve,reject)=>{
   let ended=false;
   const timeout=setTimeout(()=>{if(ended)return;ended=true;reject(Error("Speech synthesis timed out."));},14000);
   synth.speak(chunks[i],{voice:"en",rate:240,pitch:50,volume:1},(samples,sampleRate)=>{
    if(ended)return;ended=true;clearTimeout(timeout);
    if(!samples?.length||!Number.isFinite(sampleRate)||sampleRate<8000)
     reject(Error("The synthesizer could not produce an audio segment."));
    else resolve({samples:samples instanceof Float32Array?samples:new Float32Array(samples),sampleRate});
   });
  });
  results.push(result);
  if(i%4===3)await new Promise(r=>setTimeout(r,0));
 }
 return results;
}
