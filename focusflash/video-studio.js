/* FocusFlash Video Studio 1.0
   In-browser Kokoro voice generation + synchronized WebM exporter.
   Text and audio are not uploaded to any service. Initial JS/model/voice assets
   are fetched from their public distribution hosts, then cached by the browser.
*/
(() => {
 "use strict";
 const $ = id => document.getElementById(id);
 // Focus on the exact middle letter; for even-length words, take the
 // left middle. Ignore punctuation so the red focal point is a letter.
 const focusIndex = word => {
   const chars=[...word];
   const letters=[];
   for(let i=0;i<chars.length;i++)
     if(/[\p{L}\p{N}]/u.test(chars[i]))letters.push(i);
   return letters.length ? letters[Math.floor((letters.length-1)/2)] :
     Math.max(0,Math.floor((chars.length-1)/2));
 };
 const MODEL="onnx-community/Kokoro-82M-v1.0-ONNX";
 const voices={
   af_heart:"Heart · female",af_bella:"Bella · female",
   af_nicole:"Nicole · female",af_sky:"Sky · female",
   am_michael:"Michael · male",am_liam:"Liam · male",
   bf_emma:"Emma · British",bm_george:"George · British"
 };
 let tts=null,modelLoading=null,voiceBuffer=null,voiceSignature="",busy=false;
 const instantVoices={system:"Phone's voice · instant reading / compact voice in video"};
 const fastVoices={"en_US-ryan-medium":"Ryan · American male","en_US-hfc_female-medium":"American female","en_US-lessac-low":"Lessac · American"};
 let micRecorder=null,micStream=null,micChunks=[],videoBlob=null,videoFilename="focusflash-video.webm";
 let audioContext=null,previewSource=null,previewGain=null,previewAnimation=0,renderAbort=false;
 let readerSource=null,readerGain=null,readerGeneration=0;
 let readerVoice=null,previewVoice=null,nativeSpeaking=false;
 const pitchEngine=()=>import("./pitch-preserve.js?v=blocks-2");
 let mediaUrl=null;
 const sel=id=>$(id);
 const report=(message)=>{sel("studioStatus").textContent=message;};
 const words=()=>sel("sourceText").value.trim().split(/\s+/).filter(Boolean);
 const signature=()=>sel("sourceText").value.trim()+"\n@@"+sel("studioMode").value+"\n@@"+sel("studioVoice").value;
 const timing=()=>({
   wpm:Math.max(60,Math.min(2000,Number(sel("wpm").value)||300)),
   punct:sel("punctuationPause").checked,long:sel("longWordPause").checked
 });
 function wait(ms){return new Promise(r=>setTimeout(r,ms));}
 function durationFor(word,settings){
   let ms=60000/settings.wpm;
   if(settings.punct){
     if(/[.!?][”’"'()\]]*$/.test(word))ms*=1.8;
     else if(/[,;:][”’"'()\]]*$/.test(word))ms*=1.35;
   }
   if(settings.long && [...word].length>=12)ms*=1.2;
   return Math.max(30,ms);
 }
 function makeTimeline(items){
   // Visual WPM is authoritative whether or not the video has speech.
   // The voice is played faster/slower to match the total timeline.
   const settings=timing(),times=items.map(w=>durationFor(w,settings)/1000);
   const starts=[];let elapsed=0;
   for(const seconds of times){starts.push(elapsed);elapsed+=seconds;}
   return {starts,times,total:Math.max(.4,elapsed)};
 }
 const undertoneVolume=()=>Math.max(0,Math.min(1,(Number(sel("studioVolume").value)||0)/100));
 const narrationRate=(timeline)=>{
   if(!voiceBuffer||!timeline.total)return 1;
   return voiceBuffer.duration/timeline.total;
 };
 function updateSpeedHint(){
   const totalWords=words(),rate=totalWords.length&&voiceBuffer?narrationRate(makeTimeline(totalWords)):null;
   const wpm=timing().wpm,volume=Math.round(undertoneVolume()*100);
   sel("studioVolumeValue").textContent=volume+"%";
   sel("studioSpeedHint").textContent=sel("studioMode").value==="instant"?
     "Instant speech starts with Play. Your phone controls its maximum speaking speed; the red-letter words keep the chosen WPM. Voice level "+volume+"%.":rate==null?
     "Narration will match "+wpm+" WPM; volume "+volume+"%.":
     "Narration synced to "+wpm+" WPM at "+rate.toFixed(2)+"× playback and "+volume+"% volume."+
       (rate>3.5?" At this speed, speech may sound choppy, but its pitch is preserved.":"");
 }
 function currentWordAt(timeline,seconds){
   let lo=0,hi=timeline.starts.length-1;
   while(lo<hi){const mid=Math.ceil((lo+hi)/2);if(timeline.starts[mid]<=seconds)lo=mid;else hi=mid-1;}
   return lo;
 }
 function dimensions(value){
   if(value==="wide")return {width:1280,height:720};
   if(value==="square")return {width:960,height:960};
   return {width:720,height:1280};
 }
 function drawVideoFrame(canvas,ctx,item,position,count,elapsed,total){
   const {width:W,height:H}=canvas;const cx=W/2,cy=H/2;
   const bg=ctx.createLinearGradient(0,0,W,H);
   bg.addColorStop(0,"#0d0e16");bg.addColorStop(1,"#14101b");
   ctx.fillStyle=bg;ctx.fillRect(0,0,W,H);
   const shine=ctx.createRadialGradient(cx,cy,20,cx,cy,Math.max(W,H)*.55);
   shine.addColorStop(0,"#28202e");shine.addColorStop(1,"#11101900");
   ctx.fillStyle=shine;ctx.fillRect(0,0,W,H);
   const chosenPx=Math.max(16,Math.min(120,Number(sel("studioScale").value)||48));
   const ratio=sel("studioRatio").value;
   // Exported pixels scale to match the 270/600/330px-wide editing preview.
   const designWidth=ratio==="wide"?600:ratio==="square"?330:270;
   const centerY=cy;const parts=[...item];
   const fi=Math.min(focusIndex(item),Math.max(0,parts.length-1));
   const left=parts.slice(0,fi).join("");
   const main=parts[fi]||" ";
   const right=parts.slice(fi+1).join("");
   let size=Math.round(chosenPx*W/designWidth);
   const margin=W*.09;
   const weight="700";
   ctx.textBaseline="middle";
   for(;size>=12;size-=2){
     ctx.font=weight+" "+size+"px ui-monospace, Menlo, monospace";
     // The red focus character is at W/2. Both word halves must fit
     // individually, even when the chosen focus is left of text center.
     const half=Math.max(ctx.measureText(left).width,ctx.measureText(right).width);
     const focusWidth=ctx.measureText(main).width;
     if(2*half+focusWidth<=W-2*margin)break;
   }
   ctx.font=weight+" "+size+"px ui-monospace, Menlo, monospace";
   const m=ctx.measureText(main).width;
   const leftWidth=ctx.measureText(left).width;
   const rightWidth=ctx.measureText(right).width;
   const startX=Math.round(cx-m/2),endX=Math.round(cx+m/2);
   ctx.textAlign="right";ctx.fillStyle="#f7f3f6";ctx.fillText(left,startX,centerY);
   ctx.textAlign="center";ctx.fillStyle="#f04d56";ctx.fillText(main,cx,centerY);
   ctx.textAlign="left";ctx.fillStyle="#f7f3f6";ctx.fillText(right,endX,centerY);
   const guideY=size*.9;
   ctx.fillStyle="#da536080";
   ctx.fillRect(cx-1,centerY-guideY-22,2,15);
   ctx.fillRect(cx-1,centerY+guideY+7,2,15);
   ctx.font=Math.max(14,Math.round(W*.022))+"px system-ui";
   ctx.textAlign="center";ctx.fillStyle="#9995a5";
   ctx.fillText("FOCUSFLASH",cx,H*.07);
   const barW=W*.75,barY=H*.92;
   ctx.fillStyle="#484552";ctx.fillRect((W-barW)/2,barY,barW,4);
   ctx.fillStyle="#e65869";ctx.fillRect((W-barW)/2,barY,barW*Math.min(1,elapsed/total),4);
   ctx.fillStyle="#b3adb9";ctx.font=Math.max(14,Math.round(W*.022))+"px system-ui";
   ctx.fillText((position+1)+" / "+count,cx,barY+30);
 }
 async function getContext(){
   if(!audioContext||audioContext.state==="closed")
      audioContext=new (window.AudioContext||window.webkitAudioContext)();
   if(audioContext.state!=="running")await audioContext.resume();
   return audioContext;
 }
 async function loadModel(){
   if(tts)return tts;
   if(modelLoading)return modelLoading;
   modelLoading=(async()=>{
     report("Loading on-device narrator (first time may download ~90 MB)...");
     // Lazy import. This is the app's only optional runtime model dependency.
     const {KokoroTTS}=await import("https://esm.sh/kokoro-js@1.2.1?target=es2022");
     tts=await KokoroTTS.from_pretrained(MODEL,{
       dtype:"q8",device:"wasm",
       progress_callback:p=>{
         if(p?.status==="progress"&&Number.isFinite(p.progress))
           report("Downloading local voice model: "+Math.round(p.progress)+"%");
         else if(p?.status==="initiate")report("Loading voice assets: "+(p.file||"model")+"...");
       }
     });
     report("Narrator ready. Voice generation stays on your device.");
     return tts;
   })();
   try{return await modelLoading;}
   catch(error){tts=null;throw error;}
   finally{modelLoading=null;}
 }
 function splitIntoPhrases(text){
   const chunks=[];
   const sentences=(text.match(/[^.!?\n]+[.!?]*|\n+/g)||[text]).filter(x=>x.trim());
   for(const sentence of sentences){
     const seq=sentence.trim().split(/\s+/);
     let piece="";
     for(const token of seq){
       if((piece+" "+token).length>175&&piece){
         chunks.push(piece);piece=token;
       }else piece+=(piece?" ":"")+token;
     }
     if(piece)chunks.push(piece);
   }
   return chunks;
 }
 function rawAudio(sound){
   const samples=sound.audio||sound.data;
   const sampleRate=sound.sampling_rate||sound.sample_rate||24000;
   if(!(samples instanceof Float32Array)&&!ArrayBuffer.isView(samples))
      throw Error("The speech engine did not return playable audio.");
   return {samples:Float32Array.from(samples),sampleRate};
 }
 async function synthesize(){
   if(busy)return;
   // In Script Blocks mode, repeat audio clips instead of synthesizing each
   // repeated phrase again. This is especially important for neural voices.
   const blocksAPI=window.FocusFlashBlocks;
   blocksAPI?.flush?.();
   const script=sel("sourceText").value.trim();
   const signatureAtStart=signature();
   if(!script){report("Add some words before preparing narration.");return;}
   const mode=sel("studioMode").value,voice=sel("studioVoice").value;
   const units=blocksAPI?.isEnabled()?
     blocksAPI.getBlocks().filter(b=>b.text.trim()).map(b=>({
       text:b.text.trim(),repeats:Math.max(1,Math.min(100,Number(b.repeats)||1))
     })):
     [{text:script,repeats:1}];
   const uniqueWordCount=units.reduce((sum,u)=>sum+wordsIn(u.text),0);
   const cap=mode==="instant"?1800:800;
   if(uniqueWordCount>cap){
     report("This voice can synthesize up to "+cap+" unique words. Divide long blocks into chapters.");
     return;
   }
   const visualTimeline=makeTimeline(words());
   if(visualTimeline.total>480){
     report("The selected blocks would create more than 8 minutes of video. Reduce repetitions or increase WPM.");
     return;
   }
   busy=true;sel("studioGenerate").disabled=true;sel("studioExport").disabled=true;
   stopPreview();stopReaderUndertone();voiceBuffer=null;voiceSignature="";
   sel("studioListen").disabled=true;sel("studioWav").disabled=true;
   report("Preparing speech; repeated blocks will reuse audio…");
   try{
     await getContext();
     const model=mode==="quality"?await loadModel():null;
     const cache=new Map(),allSegments=[];
     for(let i=0;i<units.length;i++){
       const unit=units[i],cacheKey=mode+"|"+voice+"|"+unit.text;
       let generated=cache.get(cacheKey);
       if(!generated){
         const phrases=splitIntoPhrases(unit.text);
         if(!phrases.length)continue;
         if(mode==="instant"){
           const {generateInstantExportSpeech}=await import("./instant-tts.js?v=blocks-2");
           generated=await generateInstantExportSpeech(unit.text,msg=>report("Block "+(i+1)+": "+msg));
         }else if(mode==="fast"){
           const adapter=await import("./fast-piper.js?v=blocks-2");
           generated=await adapter.generateFastPhrases(phrases,voice,
             msg=>report("Block "+(i+1)+": "+msg));
         }else{
           generated=[];
           for(let j=0;j<phrases.length;j++){
             report("Narrating unique block "+(i+1)+"/"+units.length+
               ", phrase "+(j+1)+"/"+phrases.length);
             const raw=rawAudio(await model.generate(phrases[j],{voice}));
             generated.push(raw);
             await wait(0);
           }
         }
         for(const part of generated)
           if(!part.samples?.length||!Number.isFinite(part.sampleRate)||part.sampleRate<8000)
             throw Error("Voice engine returned an invalid audio segment.");
         cache.set(cacheKey,generated);
       }else report("Reusing previously generated voice for Block "+(i+1)+"…");
       for(let k=0;k<unit.repeats;k++)allSegments.push(...generated);
     }
     if(!allSegments.length)throw Error("No spoken audio could be generated.");
     const rate=24000,gap=Math.round(rate*.10);
     const lengths=allSegments.map(part=>Math.ceil(part.samples.length*rate/part.sampleRate));
     const totalSamples=lengths.reduce((a,b)=>a+b,0)+gap*(allSegments.length-1);
     if(totalSamples>rate*780)
       throw Error("The repeated narration is too long. Reduce block repetitions.");
     const context=await getContext();
     const assembled=context.createBuffer(1,totalSamples,rate);
     const output=assembled.getChannelData(0);
     let offset=0;
     for(let i=0;i<allSegments.length;i++){
       const part=allSegments[i],length=lengths[i],ratio=part.sampleRate/rate;
       for(let j=0;j<length;j++)
         output[offset+j]=part.samples[Math.min(part.samples.length-1,Math.floor(j*ratio))];
       offset+=length+(i<allSegments.length-1?gap:0);
     }
     if(signatureAtStart!==signature()){
       report("The script or voice changed while generating. Prepare the updated version.");
       return;
     }
     voiceBuffer=assembled;voiceSignature=signatureAtStart;
     sel("studioListen").disabled=false;sel("studioWav").disabled=false;
     updateSpeedHint();
     report("Voice ready ("+Math.ceil(assembled.duration)+" sec). "+
       "Generated "+cache.size+" unique passage"+(cache.size===1?"":"s")+
       "; repeated blocks reuse the same recording.");
   }catch(error){
     voiceBuffer=null;voiceSignature="";
     report("Narration couldn't finish: "+error.message+
       ". Try Instant mode, shorten the script, or export without sound.");
   }finally{
     busy=false;sel("studioGenerate").disabled=false;sel("studioExport").disabled=false;
   }
 }
 function wordsIn(text){
   return String(text||"").trim().split(/\s+/).filter(Boolean).length;
 }
 async function toggleMic(){
   if(micRecorder&&micRecorder.state==="recording"){
     micRecorder.stop();return;
   }
   if(busy){report("Wait for the current operation to finish.");return;}
   if(!navigator.mediaDevices?.getUserMedia||typeof MediaRecorder==="undefined"){
     report("Microphone recording is not supported in this browser.");return;
   }
   busy=true;
   stopPreview();stopReaderUndertone();voiceBuffer=null;voiceSignature="";
   sel("studioGenerate").disabled=true;sel("studioExport").disabled=true;
   sel("studioMic").textContent="■ Stop voice recording";
   try{
     micStream=await navigator.mediaDevices.getUserMedia({audio:{echoCancellation:true},video:false});
     const type=["audio/webm;codecs=opus","audio/webm","audio/mp4"]
       .find(t=>MediaRecorder.isTypeSupported(t))||"";
     micChunks=[];
     micRecorder=new MediaRecorder(micStream,type?{mimeType:type}:{});
     micRecorder.ondataavailable=event=>{if(event.data.size)micChunks.push(event.data);};
     micRecorder.onerror=event=>report("Microphone recording failed: "+(event.error?.message||"recording error"));
     micRecorder.onstop=async()=>{
       try{
         const blob=new Blob(micChunks,{type:micRecorder.mimeType||"audio/webm"});
         if(!blob.size)throw Error("No audio was recorded.");
         const ctx=await getContext();
         voiceBuffer=await ctx.decodeAudioData(await blob.arrayBuffer());
         voiceSignature=signature();
         updateSpeedHint();
         sel("studioListen").disabled=false;sel("studioWav").disabled=false;
         report("Voice recorded ("+Math.ceil(voiceBuffer.duration)+" sec). Export to include it in your video.");
       }catch(error){report("Couldn't process recording: "+error.message);}
       finally{
         micStream?.getTracks().forEach(track=>track.stop());micStream=null;micRecorder=null;
         sel("studioMic").textContent="● Record my voice";
         sel("studioGenerate").disabled=false;sel("studioExport").disabled=false;busy=false;
       }
     };
     micRecorder.start();
     report("Recording your voice. Read the passage aloud, then tap Stop voice recording.");
   }catch(error){
     micStream?.getTracks().forEach(track=>track.stop());
     micStream=null;micRecorder=null;busy=false;
     sel("studioMic").textContent="● Record my voice";
     sel("studioGenerate").disabled=false;sel("studioExport").disabled=false;
     report("Microphone unavailable: "+error.message);
   }
 }
 async function shareVideo(){
   if(!videoBlob){report("Export a video first.");return;}
   const file=new File([videoBlob],videoFilename,{type:videoBlob.type||"video/webm"});
   if(!navigator.canShare?.({files:[file]})){
     report("Sharing this video isn't supported by your browser. Use Save video below the preview.");return;
   }
   try{await navigator.share({files:[file],title:"FocusFlash Video"});}
   catch(error){if(error.name!=="AbortError")report("Share failed: "+error.message);}
 }
 function stopReaderUndertone(){
   if(nativeSpeaking){
     nativeSpeaking=false;
     try{window.speechSynthesis?.cancel();}catch{}
   }
   readerGeneration++;
   readerVoice?.dispose();
   readerVoice=null;readerSource=null;readerGain=null;
 }
 async function startReaderUndertone(wordIndex=0){
   stopReaderUndertone();
   if(!sel("studioReaderAudio").checked)return;
   if(sel("studioMode").value==="instant"){
     // This branch is synchronous before the first await so Android Chrome
     // can initiate native speech in the user's Play-button gesture.
     if(!window.speechSynthesis||!window.SpeechSynthesisUtterance){
       report("This browser has no built-in text-to-speech. Choose Quick video voice instead.");
       return;
     }
     const remaining=words().slice(wordIndex);
     if(!remaining.length)return;
     const pieces=[],MAX=200;
     let chunk="";
     for(const word of remaining){
       if(chunk&&chunk.length+word.length+1>MAX){pieces.push(chunk);chunk=word;}
       else chunk+=(chunk?" ":"")+word;
     }
     if(chunk)pieces.push(chunk);
     const voices=window.speechSynthesis.getVoices();
     const selected=voices.find(v=>v.localService&&/^en/i.test(v.lang))||
       voices.find(v=>/^en/i.test(v.lang))||null;
     const token=readerGeneration;
     const rate=Math.min(10,Math.max(.5,timing().wpm/180));
     nativeSpeaking=true;
     let p=0;
     const next=()=>{
       if(token!==readerGeneration||!nativeSpeaking||p>=pieces.length){
         if(p>=pieces.length)nativeSpeaking=false;
         return;
       }
       const u=new SpeechSynthesisUtterance(pieces[p++]);
       u.lang=selected?.lang||"en-US";
       if(selected)u.voice=selected;
       u.rate=rate;u.pitch=1;u.volume=undertoneVolume();
       u.onend=()=>{if(token===readerGeneration)next();};
       u.onerror=e=>{if(token===readerGeneration&&e.error!=="canceled"&&e.error!=="interrupted")next();};
       window.speechSynthesis.speak(u);
     };
     next();
     return;
   }
   if(!voiceBuffer||voiceSignature!==signature()){
     report("Generate or record a voice first for Fast/Natural AI mode, or select Instant.");
     return;
   }
   const token=readerGeneration,passage=words();
   if(!passage.length)return;
   const timeline=makeTimeline(passage),rate=narrationRate(timeline);
   let transport;
   try{
     const ctx=await getContext(),{makePitchPreservedVoice}=await pitchEngine();
     if(readerGeneration!==token)return;
     transport=await makePitchPreservedVoice({
       context:ctx,buffer:voiceBuffer,rate,volume:undertoneVolume(),
       destination:ctx.destination,onProgress:report
     });
     if(readerGeneration!==token){transport.dispose();return;}
     readerVoice=transport;
     readerGain=transport.gain;
     // The reader may have advanced while the voice was being prepared.
     // Pick the current word at the precise moment playback starts.
     const current=window.FocusFlashReader?.currentIndex?.()??wordIndex;
     const i=Math.max(0,Math.min(passage.length-1,current));
     const offset=voiceBuffer.duration*timeline.starts[i]/timeline.total;
     await transport.start(offset);
     if(readerGeneration!==token){transport.dispose();return;}
     transport.onEnded(()=>{if(readerVoice===transport)stopReaderUndertone();});
   }catch(error){
     if(readerVoice===transport)stopReaderUndertone();
     else transport?.dispose();
     report("Pitch-preserving reader voice unavailable: "+error.message);
   }
 }
 function stopPreview(){
   cancelAnimationFrame(previewAnimation);
   previewAnimation=0;
   previewVoice?.dispose();previewVoice=null;
   previewSource=null;previewGain=null;
   sel("studioListen").textContent="▶ Preview synced undertone";
 }
 async function listen(){
   if(previewVoice){stopPreview();return;}
   if(sel("studioMode").value==="instant"&&(!voiceBuffer||voiceSignature!==signature())){
     sel("playBtn")?.click();
     report("Native phone speech begins with the reader. No voice generation needed.");
     return;
   }
   window.FocusFlashReader?.pause?.();
   if(!voiceBuffer||voiceSignature!==signature()){
     report("Generate or record a voice for the current text first.");return;
   }
   const passage=words();if(!passage.length)return;
   const timeline=makeTimeline(passage),rate=narrationRate(timeline);
   const ctx=await getContext();
   const canvas=sel("studioSyncCanvas");
   const frameContext=canvas.getContext("2d",{alpha:false});
   sel("studioListen").disabled=true;
   let transport;
   try{
     const {makePitchPreservedVoice}=await pitchEngine();
     transport=await makePitchPreservedVoice({
       context:ctx,buffer:voiceBuffer,rate,volume:undertoneVolume(),
       destination:ctx.destination,onProgress:report
     });
     previewVoice=transport;previewGain=transport.gain;
     sel("studioSyncCanvas").classList.remove("hidden");
     drawVideoFrame(canvas,frameContext,passage[0],0,passage.length,0,timeline.total);
     await transport.start(0);
     const started=performance.now()/1000;
     transport.onEnded(()=>{if(previewVoice===transport)stopPreview();});
     const paint=()=>{
       if(previewVoice!==transport)return;
       const elapsed=Math.max(0,performance.now()/1000-started);
       const i=currentWordAt(timeline,Math.min(elapsed,timeline.total));
       drawVideoFrame(canvas,frameContext,passage[i],i,passage.length,elapsed,timeline.total);
       if(elapsed<timeline.total+.1)previewAnimation=requestAnimationFrame(paint);
     };
     sel("studioListen").textContent="■ Stop synced preview";
     sel("studioListen").disabled=false;
     previewAnimation=requestAnimationFrame(paint);
     report("Natural-pitch preview: "+timing().wpm+" WPM · "+rate.toFixed(2)+"× tempo · "+Math.round(undertoneVolume()*100)+"% volume.");
   }catch(error){
     transport?.dispose();
     if(previewVoice===transport)previewVoice=null;
     report("Preview unavailable: "+error.message);
     sel("studioListen").disabled=false;
   }
 }
 function wavFile(buffer){
   const samples=buffer.getChannelData(0),size=samples.length*2;
   const binary=new ArrayBuffer(44+size),v=new DataView(binary);
   const ascii=(offset,str)=>{for(let i=0;i<str.length;i++)v.setUint8(offset+i,str.charCodeAt(i));};
   ascii(0,"RIFF");v.setUint32(4,36+size,true);ascii(8,"WAVE");
   ascii(12,"fmt ");v.setUint32(16,16,true);v.setUint16(20,1,true);
   v.setUint16(22,1,true);v.setUint32(24,buffer.sampleRate,true);
   v.setUint32(28,buffer.sampleRate*2,true);v.setUint16(32,2,true);
   v.setUint16(34,16,true);ascii(36,"data");v.setUint32(40,size,true);
   for(let i=0;i<samples.length;i++){
     const x=Math.max(-1,Math.min(1,samples[i]));
     v.setInt16(44+i*2,x<0?x*32768:x*32767,true);
   }
   return new Blob([binary],{type:"audio/wav"});
 }
 function download(blob,name){
   const url=URL.createObjectURL(blob);
   const a=document.createElement("a");a.href=url;a.download=name;
   a.style.display="none";document.body.append(a);a.click();a.remove();
   setTimeout(()=>URL.revokeObjectURL(url),60000);
 }
 function nameSuffix(){return new Date().toISOString().replace(/[:.]/g,"-").slice(0,19);}
 function downloadWav(){
   if(!voiceBuffer||voiceSignature!==signature()){
     report("Generate narration first.");return;
   }
   download(wavFile(voiceBuffer),"focusflash-voice-"+nameSuffix()+".wav");
 }
 function mime(){
   for(const type of ["video/webm;codecs=vp9,opus","video/webm;codecs=vp8,opus",
      "video/webm;codecs=vp8","video/webm"])
      if(MediaRecorder.isTypeSupported(type))return type;
   return "";
 }
 async function exportVideo(){
   if(busy)return;
   // Instant mode creates a small exportable audio buffer on demand. The
   // ordinary reader already starts speaking without any preparation.
   if(sel("studioAudio").checked&&sel("studioMode").value==="instant"&&
      (!voiceBuffer||voiceSignature!==signature())){
     await synthesize();
     if(!voiceBuffer||voiceSignature!==signature())return;
   }
   if(typeof MediaRecorder==="undefined"||!HTMLCanvasElement.prototype.captureStream){
     report("This browser cannot create video files. Please use recent Chrome on Android or desktop.");return;
   }
   const text=words();
   if(text.length===0){report("Paste text first.");return;}
   stopPreview();window.FocusFlashReader?.pause?.();
   let narration=sel("studioAudio").checked;
   if(narration&&(!voiceBuffer||voiceSignature!==signature())){
     report("Generate narration for this text first, or uncheck 'Include generated voice'.");
     return;
   }
   const useVoice=narration&&!!voiceBuffer;
   const timeline=makeTimeline(text);
   if(timeline.total>480){report("Limit each exported video to 8 minutes; split longer text into chapters.");return;}
   busy=true;renderAbort=false;sel("studioExport").disabled=true;sel("studioGenerate").disabled=true;
   sel("studioListen").disabled=true;
   const {width,height}=dimensions(sel("studioRatio").value);
   const canvas=document.createElement("canvas");canvas.width=width;canvas.height=height;
   const context=canvas.getContext("2d",{alpha:false});
   drawVideoFrame(canvas,context,text[0],0,text.length,0,timeline.total);
   let stream=null,recorder=null,transport=null,ctx=null,raf=0,finished=false;
   let audioDestination=null;
   const chunks=[];
   try{
     stream=canvas.captureStream(30);
     if(useVoice){
       ctx=await getContext();audioDestination=ctx.createMediaStreamDestination();
       const {makePitchPreservedVoice}=await pitchEngine();
       transport=await makePitchPreservedVoice({
         context:ctx,buffer:voiceBuffer,rate:narrationRate(timeline),
         volume:undertoneVolume(),destination:audioDestination,onProgress:report
       });
       for(const track of audioDestination.stream.getAudioTracks())stream.addTrack(track);
     }
     const type=mime();
     if(!type)throw Error("No WebM video encoder is available in this browser.");
     recorder=new MediaRecorder(stream,{mimeType:type,videoBitsPerSecond:2100000});
     const complete=new Promise((resolve,reject)=>{
       recorder.ondataavailable=e=>{if(e.data.size>0)chunks.push(e.data);};
       recorder.onerror=e=>reject(e.error||Error("The video recorder failed."));
       recorder.onstop=()=>resolve();
     });
     recorder.start(1000);
     if(transport)await transport.start(0);
     const startAt=performance.now()/1000;
     const paint=()=>{
       if(finished||renderAbort)return;
       const now=performance.now()/1000;
       const elapsed=Math.max(0,now-startAt);
       const idx=currentWordAt(timeline,Math.min(elapsed,timeline.total));
       drawVideoFrame(canvas,context,text[idx],idx,text.length,elapsed,timeline.total);
       const pct=Math.min(100,Math.round(elapsed/timeline.total*100));
       report("Recording video in real time: "+pct+"% · Keep this tab open.");
       if(elapsed>=timeline.total+.4){finished=true;return;}
       raf=requestAnimationFrame(paint);
     };
     raf=requestAnimationFrame(paint);
     // Recorder operates in real time. The tab needs to stay visible.
     while(!finished&&!renderAbort){
       if(document.visibilityState==="hidden"){
         throw Error("Keep the app visible while recording. Export stopped when Chrome went to the background.");
       }
       await wait(200);
     }
     if(renderAbort)throw Error("Export canceled.");
     transport?.dispose();
     recorder.stop();
     await complete;
     if(!chunks.length)throw Error("No video data was recorded.");
     videoBlob=new Blob(chunks,{type:recorder.mimeType.split(";")[0]});
     videoFilename="focusflash-"+sel("studioRatio").value+"-"+nameSuffix()+".webm";
     if(mediaUrl)URL.revokeObjectURL(mediaUrl);
     mediaUrl=URL.createObjectURL(videoBlob);
     sel("studioPreview").src=mediaUrl;
     sel("studioDownload").href=mediaUrl;
     sel("studioDownload").download=videoFilename;
     sel("studioResult").classList.remove("hidden");
     // The visible Save link remains usable when auto-download is blocked.
     download(videoBlob,videoFilename);
     report("Video created at "+timing().wpm+" WPM"+
       (useVoice?" with pitch-preserved "+Math.round(undertoneVolume()*100)+"% undertone voice.":" without narration.")+
       " Watch it below or tap Save video. Nothing was uploaded.");
   }catch(error){
     report("Export could not finish: "+error.message);
     if(recorder?.state==="recording"){try{recorder.stop();}catch{}}
   }finally{
     finished=true;cancelAnimationFrame(raf);
     transport?.dispose();
     for(const track of stream?.getTracks()||[])track.stop();
     busy=false;
     sel("studioExport").disabled=false;sel("studioGenerate").disabled=false;
     sel("studioListen").disabled=!voiceBuffer;
   }
 }
 function setVoiceStatus(){
   if(voiceBuffer&&signature()!==voiceSignature){
     stopPreview();stopReaderUndertone();voiceBuffer=null;voiceSignature="";
     sel("studioListen").disabled=sel("studioMode").value!=="instant";
     sel("studioWav").disabled=true;
     report(sel("studioMode").value==="instant"?
       "Phone voice is available immediately. Reapply the script if it changed.":
       "Text or speaker changed. Generate narration again for video.");
   }
 }
 function mount(){
   const choice=sel("studioVoice"),mode=sel("studioMode");
   let saved={};
   try{saved=JSON.parse(localStorage.getItem("focusflash-video-v1")||"{}");}catch{}
   const populate=(preferred)=>{
     const list=mode.value==="instant"?instantVoices:mode.value==="fast"?fastVoices:voices;
     choice.replaceChildren();
     for(const [key,label] of Object.entries(list)){
       const option=document.createElement("option");
       option.value=key;option.textContent=label;choice.append(option);
     }
     choice.value=preferred&&list[preferred]?preferred:Object.keys(list)[0];
   };
   mode.value=["quality","fast","instant"].includes(saved.mode)?saved.mode:"instant";
   populate(saved.voice);
   if(["portrait","wide","square"].includes(saved.ratio))sel("studioRatio").value=saved.ratio;
   // The old control stored a 70–130% percentage, now size is in pixels.
   // Reader's own persisted font size is the canonical size across modes.
   const readerSize=Number(sel("fontSize")?.value)||48;
   sel("studioScale").value=String(Math.max(16,Math.min(120,readerSize)));
   if(Number.isFinite(saved.volume))
     sel("studioVolume").value=String(Math.max(0,Math.min(100,saved.volume)));
   if(typeof saved.readerAudio==="boolean")sel("studioReaderAudio").checked=saved.readerAudio;
   const save=()=>{try{localStorage.setItem("focusflash-video-v1",JSON.stringify({
     mode:mode.value,voice:choice.value,ratio:sel("studioRatio").value,
     size:Number(sel("studioScale").value),
     volume:Number(sel("studioVolume").value),
     readerAudio:sel("studioReaderAudio").checked
   }));}catch{}};
   const updateModeButtons=()=>{
     sel("studioGenerate").textContent=mode.value==="instant"?
       "⚡ Prepare compact video audio":"✦ Generate AI voice";
     sel("studioListen").disabled=mode.value!=="instant"&&(!voiceBuffer||voiceSignature!==signature());
     sel("studioListen").textContent=mode.value==="instant"?"▶ Hear phone voice now":"▶ Preview synced narration";
   };
   mode.addEventListener("change",()=>{
     stopReaderUndertone();populate();setVoiceStatus();save();
     updateModeButtons();
     report(mode.value==="instant"?
       "Instant phone speech ready. Press Play to hear it now. Video narration prepares automatically when exporting.":
       mode.value==="fast"?"Fast AI voice selected; generate it before reading with sound.":
       "Natural AI voice selected; generating it may take time.");
     updateSpeedHint();
   });
   for(const element of [sel("sourceText"),choice])
     element.addEventListener("input",()=>{
       setVoiceStatus();updateSpeedHint();
     });
   for(const id of ["wpm","punctuationPause","longWordPause"]){
     const element=sel(id);
     element.addEventListener("input",()=>{
       if(previewVoice)stopPreview();
       if((readerVoice||nativeSpeaking)&&window.FocusFlashReader?.isPlaying?.())
         startReaderUndertone(window.FocusFlashReader.currentIndex()).catch(()=>{});
       updateSpeedHint();
     });
   }
   sel("studioReaderAudio").addEventListener("change",()=>{
     if(!sel("studioReaderAudio").checked)stopReaderUndertone();
     else if(window.FocusFlashReader?.isPlaying?.())
       startReaderUndertone(window.FocusFlashReader.currentIndex()).catch(()=>{});
     save();
   });
   sel("studioVolume").addEventListener("input",()=>{
     const level=undertoneVolume();
     if(previewGain&&audioContext)
       previewGain.gain.setTargetAtTime(level,audioContext.currentTime,.025);
     if(readerGain&&audioContext)
       readerGain.gain.setTargetAtTime(level,audioContext.currentTime,.025);
     // Native SpeechSynthesisUtterance volume cannot change mid-utterance;
     // restart near the displayed word to use the new level.
     if(nativeSpeaking&&window.FocusFlashReader?.isPlaying?.())
       startReaderUndertone(window.FocusFlashReader.currentIndex()).catch(()=>{});
     updateSpeedHint();
     save();
   });
   for(const id of ["studioVoice","studioRatio","studioScale"])
     sel(id).addEventListener("change",save);
   sel("studioGenerate").addEventListener("click",synthesize);
   sel("studioMic").addEventListener("click",toggleMic);
   sel("studioShare").addEventListener("click",shareVideo);
   sel("studioListen").addEventListener("click",()=>listen().catch(error=>report(error.message)));
   sel("studioWav").addEventListener("click",downloadWav);
   sel("studioExport").addEventListener("click",()=>exportVideo().catch(error=>report(error.message)));
   updateSpeedHint();
   updateModeButtons();
   report(mode.value==="instant"?
     "Instant voice is ready. Press the reader's Play button; no AI voice generation is needed.":
     "AI voice selected. Generate it before hearing it in the reader.");
 }
 window.FocusFlashStudio={mount,startReaderUndertone,stopReaderUndertone};
})();