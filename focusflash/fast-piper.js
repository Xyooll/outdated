// Lightweight, fully client-side Piper voice adapter. Uses browser-friendly JSDelivr build.
let modulePromise=null;
export async function generateFastPhrases(phrases,voice,onProgress){
 if(!modulePromise)modulePromise=import("https://cdn.jsdelivr.net/npm/@diffusionstudio/vits-web@1.0.3/+esm").catch(e=>{modulePromise=null;throw e;});
 onProgress("Loading mobile speech runtime…");
 const piper=await modulePromise;
 const Context=window.AudioContext||window.webkitAudioContext;
 const ac=new Context();
 try{
  const segments=[];
  let index=0;
  for(const phrase of phrases){
   index++;
   onProgress("Creating audio "+index+" of "+phrases.length+"…");
   const wav=await piper.predict({text:phrase,voiceId:voice},progress=>{
    const percent=progress?.total ? Math.round(progress.loaded*100/progress.total) : null;
    if(percent!=null && percent>=0 && percent<=100)
      onProgress("Downloading mobile voice: "+percent+"% · audio "+index+" of "+phrases.length);
   });
   const bytes=typeof wav.arrayBuffer==="function"?await wav.arrayBuffer():wav;
   const decoded=await ac.decodeAudioData(bytes);
   const copied=new Float32Array(decoded.length);
   if(decoded.numberOfChannels===1)copied.set(decoded.getChannelData(0));
   else{
    const a=decoded.getChannelData(0),b=decoded.getChannelData(1);
    for(let i=0;i<copied.length;i++)copied[i]=(a[i]+b[i])/2;
   }
   segments.push({samples:copied,sampleRate:decoded.sampleRate});
   await new Promise(resolve=>setTimeout(resolve,0));
  }
  return segments;
 }finally{await ac.close();}
}
