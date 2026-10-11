/* FocusFlash Video Studio 1.0
   In-browser Kokoro voice generation + synchronized WebM exporter.
   Text and audio are not uploaded to any service. Initial JS/model/voice assets
   are fetched from their public distribution hosts, then cached by the browser.
*/
(() => {
 "use strict";
 const $ = id => document.getElementById(id);
 const focusIndex = word => {
   const n=[...word].length;
   if(n<=1)return 0;
   if(n<=5)return Math.max(0,Math.floor((n-1)*.40));
   if(n<=9)return Math.max(0,Math.floor((n-1)*.38));
   return Math.max(0,Math.floor((n-1)*.35));
 };
 const MODEL="onnx-community/Kokoro-82M-v1.0-ONNX";
 const voices={
   af_heart:"Heart · female",af_bella:"Bella · female",
   af_nicole:"Nicole · female",af_sky:"Sky · female",
   am_michael:"Michael · male",am_liam:"Liam · male",
   bf_emma:"Emma · British",bm_george:"George · British"
 };
 let tts=null,modelLoading=null,voiceBuffer=null,voiceSignature="",busy=false;
 const fastVoices={"en_US-ryan-medium":"Ryan · American male","en_US-hfc_female-medium":"American female","en_US-lessac-low":"Lessac · American"};
 let micRecorder=null,micStream=null,micChunks=[],videoBlob=null,videoFilename="focusflash-video.webm";
 let audioContext=null,previewSource=null,previewGain=null,previewAnimation=0,renderAbort=false;
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
   sel("studioSpeedHint").textContent=rate==null?
     "Narration will match "+wpm+" WPM; volume "+volume+"%.":
     "Narration synced to "+wpm+" WPM at "+rate.toFixed(2)+"× playback and "+volume+"% volume."+
       (rate>3.5?" At this speed, the speech will be heavily pitch-shifted.":"");
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
   const scale=Number(sel("studioScale").value)||100;
   const centerY=cy;const parts=[...item];
   const fi=Math.min(focusIndex(item),Math.max(0,parts.length-1));
   const left=parts.slice(0,fi).join("");
   const main=parts[fi]||" ";
   const right=parts.slice(fi+1).join("");
   let size=Math.round(Math.min(W*.15,H*.095)*scale/100);
   const margin=W*.09;
   const weight="700";
   ctx.textBaseline="middle";
   for(;size>=18;size-=2){
     ctx.font=weight+" "+size+"px ui-monospace, Menlo, monospace";
     const w=ctx.measureText(item).width;
     if(w<W-2*margin)break;
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
   const text=sel("sourceText").value.trim();
   const intendedSignature=signature();
   if(!text){report("Paste some text before generating a narrator.");return;}
   if(words().length>800){
     report("For reliable phone performance, generate narration from 800 words or fewer at a time.");
     return;
   }
   busy=true;sel("studioGenerate").disabled=true;sel("studioExport").disabled=true;
   stopPreview();voiceBuffer=null;voiceSignature="";report("Initializing narrator...");
   try{
     const mode=sel("studioMode").value;
     const engine=mode==="quality"?await loadModel():null;
     const phrases=splitIntoPhrases(text);
     if(!phrases.length)throw Error("No readable text found.");
     const segments=[];let total=0;
     const gap=.11;
     if(mode==="fast"){
       report("Loading faster mobile voice, then generating audio...");
       const adapter=await import("./fast-piper.js?v=undertone-1");
       const results=await adapter.generateFastPhrases(phrases,sel("studioVoice").value,report);
       for(const raw of results){
         segments.push(raw);
         total+=raw.samples.length/raw.sampleRate+gap;
       }
     }else{
       for(let i=0;i<phrases.length;i++){
         report("Generating natural narration: "+(i+1)+" / "+phrases.length);
         const raw=rawAudio(await engine.generate(phrases[i],{voice:sel("studioVoice").value}));
         if(!raw.samples.length)throw Error("Voice generator returned an empty phrase.");
         segments.push(raw);
         total+=raw.samples.length/raw.sampleRate+gap;
         await wait(0);
       }
     }
     const rate=24000;
     const count=Math.ceil(total*rate);
     if(count>rate*780)throw Error("Narration is too long for one video (limit 13 minutes).");
     const context=await getContext();
     voiceBuffer=context.createBuffer(1,count,rate);
     const merged=voiceBuffer.getChannelData(0);
     let offset=0;
     for(const part of segments){
       // Kokoro returns 24 kHz. Guard future sample rate changes.
       const ratio=part.sampleRate/rate;
       const len=Math.ceil(part.samples.length/ratio);
       for(let j=0;j<len;j++)merged[offset+j]=part.samples[Math.min(part.samples.length-1,Math.floor(j*ratio))];
       offset+=len+Math.round(gap*rate);
     }
     voiceSignature=intendedSignature;
     sel("studioExport").disabled=false;
     sel("studioListen").disabled=false;sel("studioWav").disabled=false;
     if(voiceSignature!==signature())
       report("Narration generated, but the text or speaker changed. Regenerate to match.");
     else report("Voice ready ("+Math.ceil(voiceBuffer.duration)+" sec). Preview it or export video with audio.");
   }catch(error){
     voiceBuffer=null;
     report("Voice generation failed: "+error.message+
      ". You can still export a silent video. Try desktop Chrome if this phone lacks memory.");
   }finally{
     busy=false;sel("studioGenerate").disabled=false;
     sel("studioExport").disabled=false;
   }
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
   stopPreview();voiceBuffer=null;voiceSignature="";
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
 function stopPreview(){
   cancelAnimationFrame(previewAnimation);
   previewAnimation=0;
   try{previewSource?.stop();}catch{}
   try{previewSource?.disconnect();}catch{}
   try{previewGain?.disconnect();}catch{}
   previewSource=null;previewGain=null;
   sel("studioListen").textContent="▶ Preview synced undertone";
 }
 async function listen(){
   if(previewSource){stopPreview();return;}
   if(!voiceBuffer||voiceSignature!==signature()){
     report("Generate or record a voice for the current text first.");return;
   }
   const passage=words();
   if(!passage.length)return;
   const timeline=makeTimeline(passage),rate=narrationRate(timeline);
   const ctx=await getContext(),src=ctx.createBufferSource();
   const gain=ctx.createGain();
   src.buffer=voiceBuffer;
   src.playbackRate.value=rate;
   gain.gain.value=undertoneVolume();
   src.connect(gain);gain.connect(ctx.destination);
   const canvas=sel("studioSyncCanvas");
   const frameContext=canvas.getContext("2d",{alpha:false});
   const startAt=ctx.currentTime+.12;
   sel("studioListen").textContent="■ Stop synced preview";
   sel("studioSyncCanvas").classList.remove("hidden");
   previewSource=src;previewGain=gain;
   src.onended=()=>{if(previewSource===src)stopPreview();};
   const paint=()=>{
     if(previewSource!==src)return;
     const elapsed=Math.max(0,ctx.currentTime-startAt);
     const i=currentWordAt(timeline,Math.min(elapsed,timeline.total));
     drawVideoFrame(canvas,frameContext,passage[i],i,passage.length,elapsed,timeline.total);
     if(elapsed<timeline.total+.1)previewAnimation=requestAnimationFrame(paint);
   };
   drawVideoFrame(canvas,frameContext,passage[0],0,passage.length,0,timeline.total);
   src.start(startAt);
   previewAnimation=requestAnimationFrame(paint);
   report("Preview: "+timing().wpm+" WPM · speech "+rate.toFixed(2)+"× · "+Math.round(undertoneVolume()*100)+"% volume.");
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
   if(typeof MediaRecorder==="undefined"||!HTMLCanvasElement.prototype.captureStream){
     report("This browser cannot create video files. Please use recent Chrome on Android or desktop.");return;
   }
   const text=words();
   if(text.length===0){report("Paste text first.");return;}
   stopPreview();
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
   let stream=null,recorder=null,src=null,ctx=null,raf=0,finished=false;
   let audioDestination=null,narrationGain=null;
   const chunks=[];
   try{
     stream=canvas.captureStream(30);
     if(useVoice){
       ctx=await getContext();audioDestination=ctx.createMediaStreamDestination();
       src=ctx.createBufferSource();src.buffer=voiceBuffer;
       // Compress the generated speech to the EXACT same length as the WPM
       // timeline, at the user's quiet undertone volume.
       src.playbackRate.value=narrationRate(timeline);
       narrationGain=ctx.createGain();narrationGain.gain.value=undertoneVolume();
       src.connect(narrationGain);narrationGain.connect(audioDestination);
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
     const startAt=useVoice?ctx.currentTime+.25:performance.now()/1000+.25;
     if(useVoice)src.start(startAt);
     const paint=()=>{
       if(finished||renderAbort)return;
       const now=useVoice?ctx.currentTime:performance.now()/1000;
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
     if(src){try{src.stop();}catch{}}
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
       (useVoice?" with "+Math.round(undertoneVolume()*100)+"% undertone voice.":" without narration.")+
       " Watch it below or tap Save video. Nothing was uploaded.");
   }catch(error){
     report("Export could not finish: "+error.message);
     if(recorder?.state==="recording"){try{recorder.stop();}catch{}}
   }finally{
     finished=true;cancelAnimationFrame(raf);
     try{src?.stop();}catch{}
     for(const track of stream?.getTracks()||[])track.stop();
     busy=false;
     sel("studioExport").disabled=false;sel("studioGenerate").disabled=false;
     sel("studioListen").disabled=!voiceBuffer;
   }
 }
 function setVoiceStatus(){
   if(voiceBuffer&&signature()!==voiceSignature){
     stopPreview();voiceBuffer=null;voiceSignature="";
     sel("studioListen").disabled=true;sel("studioWav").disabled=true;
     report("Text or speaker changed. Generate narration again for the new version.");
   }
 }
 function mount(){
   const choice=sel("studioVoice"),mode=sel("studioMode");
   let saved={};
   try{saved=JSON.parse(localStorage.getItem("focusflash-video-v1")||"{}");}catch{}
   const populate=(preferred)=>{
     const list=mode.value==="fast"?fastVoices:voices;
     choice.replaceChildren();
     for(const [key,label] of Object.entries(list)){
       const option=document.createElement("option");
       option.value=key;option.textContent=label;choice.append(option);
     }
     choice.value=preferred&&list[preferred]?preferred:Object.keys(list)[0];
   };
   mode.value=saved.mode==="quality"?"quality":"fast";
   populate(saved.voice);
   if(["portrait","wide","square"].includes(saved.ratio))sel("studioRatio").value=saved.ratio;
   if(Number.isFinite(saved.size))sel("studioScale").value=String(saved.size);
   const save=()=>{try{localStorage.setItem("focusflash-video-v1",JSON.stringify({
     mode:mode.value,voice:choice.value,ratio:sel("studioRatio").value,
     size:Number(sel("studioScale").value)
   }));}catch{}};
   mode.addEventListener("change",()=>{
     populate();setVoiceStatus();save();
     report(mode.value==="fast"?"Fast mobile voice selected. Generate narration for the video.":"Natural high-quality voice selected. Slower on phones.");
   });
   for(const element of [sel("sourceText"),choice])
     element.addEventListener("input",setVoiceStatus);
   for(const id of ["studioVoice","studioRatio","studioScale"])
     sel(id).addEventListener("change",save);
   sel("studioGenerate").addEventListener("click",synthesize);
   sel("studioMic").addEventListener("click",toggleMic);
   sel("studioShare").addEventListener("click",shareVideo);
   sel("studioListen").addEventListener("click",()=>listen().catch(error=>report(error.message)));
   sel("studioWav").addEventListener("click",downloadWav);
   sel("studioExport").addEventListener("click",()=>exportVideo().catch(error=>report(error.message)));
   report("Fast mobile narration ready to start. First use downloads a voice model.");
 }
 window.FocusFlashStudio={mount};
})();