/* FocusFlash Sound Studio — local sine tones, synthesized ambience and MP3 mix.
   Sound runs in Web Audio, so voice, tone, ambient FX and imported audio can
   share the same browser MediaStreamDestination for WebM video export.
*/
(() => {
 "use strict";
 const $=id=>document.getElementById(id);
 const KEY=window.FocusFlashProfiles?.key("focusflash-tones-v1")||"focusflash-tones-v1",
       DB_NAME="focusflash-soundtrack-v1",
       FILE_ID="active-"+(window.FocusFlashProfiles?.id?.()||"1");
 const LIMIT=50*1024*1024;
 const MODES=["off","pure","binaural"];
 const FX=["off","white","pink","brown","rain","waves","wind","stream","fire","forest","fan","night"];
 const FX_LABELS={off:"Off",white:"White noise",pink:"Pink noise",brown:"Brown noise",
   rain:"Rain",waves:"Ocean waves",wind:"Wind",stream:"Flowing stream",
   fire:"Fireplace",forest:"Forest birds",fan:"Electric fan",night:"Night crickets"};
 const clamp=(x,min,max)=>Math.max(min,Math.min(max,Number.isFinite(Number(x))?Number(x):min));
 const normalize=s=>({
   mode:MODES.includes(s?.mode)?s.mode:"off",
   carrier:clamp(s?.carrier??220,60,1200),
   beat:clamp(s?.beat??6,.5,40),
   volume:clamp(s?.volume??8,0,25),
   exportAudio:s?.exportAudio!==false,
   fx:FX.includes(s?.fx)?s.fx:"off",
   fxVolume:clamp(s?.fxVolume??18,0,40),
   fxExport:s?.fxExport!==false,
   mp3Volume:clamp(s?.mp3Volume??25,0,100),
   mp3Loop:s?.mp3Loop!==false,
   mp3Export:s?.mp3Export!==false
 });
 let settings=normalize({});
 try{settings=normalize(JSON.parse(localStorage.getItem(KEY)||"null"));}catch{}
 let sharedContext=null,readerSession=null,testSession=null;
 let fileUrl=null,fileName="",fileDuration=0,fileToken=0,importBusy=false;
 const generatedCache=new Map();
 const fmt=n=>Number(n.toFixed(2)).toString();
 const save=()=>{try{localStorage.setItem(KEY,JSON.stringify(settings));}catch{}};
 function fileLabel(){return fileName?fileName+" · "+Math.ceil(fileDuration)+" sec":"No MP3 imported";}
 function activeMix(forExport=false){
   const t=settings.mode!=="off"&&(!forExport||settings.exportAudio);
   const fx=settings.fx!=="off"&&(!forExport||settings.fxExport);
   const file=!!fileUrl&&(!forExport||settings.mp3Export);
   return {tone:t,fx,file,any:t||fx||file};
 }
 function summary(forExport=false){
   const mix=activeMix(forExport),parts=[];
   if(mix.tone)parts.push(settings.mode==="pure"?"Pure "+settings.carrier+" Hz":"Binaural "+fmt(settings.beat)+" Hz");
   if(mix.fx)parts.push(FX_LABELS[settings.fx]);
   if(mix.file)parts.push("MP3: "+fileName);
   return parts.join(" + ")||"Sound off";
 }
 function refresh(){
   $("toneCurrent").textContent=summary();
   $("toneHeadphones").hidden=settings.mode!=="binaural";
   $("toneBeatRow").hidden=settings.mode!=="binaural";
   $("toneCarrierValue").textContent=settings.carrier+" Hz";
   $("toneBeatValue").textContent=fmt(settings.beat)+" Hz";
   $("toneVolumeValue").textContent=settings.volume+"%";
   $("fxVolumeValue").textContent=settings.fxVolume+"%";
   $("mp3VolumeValue").textContent=settings.mp3Volume+"%";
   $("tonePreview").textContent=testSession?"■ Stop sound preview":"▶ Preview sound mix";
   $("toneStatus").textContent=(testSession?"Mix playing · ":readerSession?"Reading with mix · ":"Ready · ")+summary();
   $("mp3FileStatus").textContent=importBusy?"Checking audio file…":fileLabel();
   $("mp3Clear").disabled=!fileUrl;
   $("mp3Loop").checked=settings.mp3Loop;
   $("toneExport").checked=settings.exportAudio;
   $("ambienceExport").checked=settings.fxExport;
   $("mp3Export").checked=settings.mp3Export;
   $("timelineToneStatus").textContent=summary().slice(0,58);
   $("timelineTone").dataset.mode=activeMix().any?(settings.fx!=="off"?"ambient":settings.mode!=="off"?settings.mode:"file"):"off";
   if(document.activeElement!==$("toneCarrierNumber"))$("toneCarrierNumber").value=String(settings.carrier);
   if(document.activeElement!==$("toneBeatNumber"))$("toneBeatNumber").value=fmt(settings.beat);
 }
 function audioContext(){
   if(!sharedContext||sharedContext.state==="closed"){
     const Context=window.AudioContext||window.webkitAudioContext;
     if(!Context)throw Error("This browser does not support Web Audio.");
     sharedContext=new Context();
   }
   if(sharedContext.state==="suspended")sharedContext.resume().catch(()=>{});
   return sharedContext;
 }
 // Reusable, smoothly looped procedural environmental effects. These are
 // sound designs synthesized in the browser, not outdoor field recordings.
 function makeFX(ctx,type){
   if(generatedCache.has(type))return generatedCache.get(type);
   const sr=22050,seconds=type==="waves"?14:10,count=sr*seconds;
   const buf=ctx.createBuffer(2,count,sr);
   for(let channel=0;channel<2;channel++){
     const out=buf.getChannelData(channel);
     let seed=(0x9e3779b9 ^ ((channel+1)*0x1f123bb5) ^ (type.length*7919))>>>0;
     const random=()=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return (seed>>>0)/4294967296};
     let low=0,medium=0,brown=0,p0=0,p1=0,p2=0,p3=0,p4=0,p5=0,drop=0,dropPhase=0,chirp=0,chirpPhase=0;
     const period=type==="waves"?6:4;
     for(let i=0;i<count;i++){
       const t=i/sr,white=random()*2-1;
       low+=.002*(white-low);
       medium+=.055*(white-medium);
       brown=(brown+.02*white)/1.02;
       p0=.99886*p0+white*.0555179;
       p1=.99332*p1+white*.0750759;
       p2=.96900*p2+white*.1538520;
       p3=.86650*p3+white*.3104856;
       p4=.55000*p4+white*.5329522;
       p5=-.7616*p5-white*.0168980;
       const pink=(p0+p1+p2+p3+p4+p5+white*.5362)*.12;
       const surge=.10+.9*(.5-.5*Math.cos(2*Math.PI*t/period));
       let v=0;
       if(type==="white")v=white*.28;
       else if(type==="pink")v=pink*.55;
       else if(type==="brown")v=brown*2.1;
       else if(type==="rain"){
         if(random()<.00075) {drop=.3+random()*.35;dropPhase=0;}
         drop*=.992;dropPhase+=2*Math.PI*(650+channel*120)/sr;
         v=.28*pink+.12*white+.42*drop*Math.sin(dropPhase);
       }else if(type==="waves"){
         v=(pink*.72+white*.06)*surge +low*.7;
       }else if(type==="wind"){
         const gust=.48+.27*Math.sin(2*Math.PI*t/6+channel*.4)+.12*Math.sin(t*5);
         v=(pink*.28+medium*.48+low*1.7)*gust;
       }else if(type==="stream"){
         if(random()<.0003){drop=.15+random()*.2;dropPhase=0;}
         drop*=.995;dropPhase+=2*Math.PI*(1100+channel*80)/sr;
         v=pink*.38+white*.045+drop*Math.sin(dropPhase)*.16;
       }else if(type==="fire"){
         if(random()<.0009)drop=.45+random()*.6;
         drop*=.965;
         v=low*1.15+pink*.13+white*drop*.6;
       }else if(type==="forest"){
         if(random()<.000045){chirp=1;chirpPhase=0;}
         chirp*=.99915;chirpPhase+=2*Math.PI*(1400+800*chirp)/sr;
         v=(pink*.14+low*.45)+chirp*Math.sin(chirpPhase)*.14;
       }else if(type==="fan"){
         v=.06*Math.sin(2*Math.PI*118*t)+pink*.17+medium*.29;
       }else if(type==="night"){
         const pulse=Math.pow(Math.max(0,Math.sin(2*Math.PI*11*t+channel*.27)),7);
         v=.018*white+.075*Math.sin(2*Math.PI*2650*t)*pulse+low*.32;
       }
       // Tiny seam fade makes a seamless repeated bed without audible clicks.
       const fade=Math.min(1,i/(sr*.15),(count-1-i)/(sr*.15));
       out[i]=Math.max(-.9,Math.min(.9,v*.85*fade));
     }
   }
   generatedCache.set(type,buf);
   return buf;
 }
 function build(ctx,destination,forExport=false){
   const mix=activeMix(forExport);
   if(!mix.any)return null;
   const session={ctx,nodes:[],sources:[],media:[],tone:null,fx:null,file:null,
     signature:settings.mode+"|"+settings.fx+"|"+(fileUrl||""),stopped:false};
   const gain=(level)=>{
     const node=ctx.createGain();
     node.gain.setValueAtTime(0,ctx.currentTime);
     node.gain.setTargetAtTime(level,ctx.currentTime,.025);
     node.connect(destination);session.nodes.push(node);
     return node;
   };
   const osc=hz=>{
     const node=ctx.createOscillator();node.type="sine";
     node.frequency.setValueAtTime(hz,ctx.currentTime);
     session.sources.push(node);session.nodes.push(node);return node;
   };
   if(mix.tone){
     const g=gain(settings.volume/100);session.tone={gain:g,oscillators:[]};
     if(settings.mode==="pure"){
       const o=osc(settings.carrier);o.connect(g);o.start();
       session.tone.oscillators.push(o);
     }else{
       if(!ctx.createStereoPanner)throw Error("Binaural beats require a stereo-capable browser.");
       for(const [hz,pan] of [[settings.carrier-settings.beat/2,-1],[settings.carrier+settings.beat/2,1]]){
         const o=osc(hz),p=ctx.createStereoPanner();p.pan.value=pan;
         session.nodes.push(p);o.connect(p);p.connect(g);o.start();
         session.tone.oscillators.push(o);
       }
     }
   }
   if(mix.fx){
     const g=gain(settings.fxVolume/100);
     const node=ctx.createBufferSource();
     node.buffer=makeFX(ctx,settings.fx);
     node.loop=true;node.connect(g);node.start();
     session.nodes.push(node);session.sources.push(node);session.fx={gain:g};
   }
   if(mix.file){
     const g=gain(settings.mp3Volume/100);
     const element=new Audio();
     element.preload="auto";element.src=fileUrl;
     element.loop=settings.mp3Loop;
     const node=ctx.createMediaElementSource(element);node.connect(g);
     session.nodes.push(node);session.media.push(element);
     session.file={gain:g,element};
   }
   return session;
 }
 async function startMedia(session){
   if(!session||session.stopped)return;
   await Promise.all(session.media.map(el=>el.play()));
 }
 function stop(session){
   if(!session||session.stopped)return;
   session.stopped=true;
   for(const element of session.media){
     try{element.pause();element.removeAttribute("src");element.load();}catch{}
   }
   const now=session.ctx.currentTime;
   for(const layer of [session.tone,session.fx,session.file]){
     try{layer?.gain.gain.setTargetAtTime(0,now,.008);}catch{}
   }
   for(const source of session.sources){try{source.stop(now+.055);}catch{}}
   setTimeout(()=>{for(const node of session.nodes){try{node.disconnect();}catch{}}},100);
 }
 function updateSession(session){
   if(!session||session.stopped)return;
   const signature=settings.mode+"|"+settings.fx+"|"+(fileUrl||"");
   if(session.signature!==signature)return false;
   const now=session.ctx.currentTime;
   if(session.tone){
     session.tone.gain.gain.setTargetAtTime(settings.volume/100,now,.025);
     const frequencies=settings.mode==="pure"?[settings.carrier]:
       [settings.carrier-settings.beat/2,settings.carrier+settings.beat/2];
     session.tone.oscillators.forEach((o,i)=>o.frequency.setTargetAtTime(frequencies[i],now,.035));
   }
   if(session.fx)session.fx.gain.gain.setTargetAtTime(settings.fxVolume/100,now,.025);
   if(session.file){
     session.file.gain.gain.setTargetAtTime(settings.mp3Volume/100,now,.025);
     session.file.element.loop=settings.mp3Loop;
   }
   return true;
 }
 function update(rebuild=false){
   save();
   if(readerSession){
     if(rebuild||!updateSession(readerSession)){stop(readerSession);readerSession=null;startReader();}
   }
   if(testSession){
     if(rebuild||!updateSession(testSession)){stop(testSession);testSession=null;startTest();}
   }
   refresh();
 }
 function startReader(){
   stop(testSession);testSession=null;
   stop(readerSession);readerSession=null;
   if(!activeMix().any){refresh();return;}
   try{
     const ctx=audioContext();
     readerSession=build(ctx,ctx.destination);
     startMedia(readerSession).catch(err=>setError(err));
     refresh();
   }catch(err){setError(err);}
 }
 function stopReader(){stop(readerSession);readerSession=null;refresh();}
 function startTest(){
   stop(readerSession);readerSession=null;
   stop(testSession);testSession=null;
   if(!activeMix().any){setError(Error("Choose a tone, an ambience preset, or import an MP3 first."));return;}
   try{
     const ctx=audioContext();
     testSession=build(ctx,ctx.destination);
     startMedia(testSession).catch(err=>setError(err));
     refresh();
   }catch(err){setError(err);}
 }
 function stopTest(){stop(testSession);testSession=null;refresh();}
 function setError(err){$("toneStatus").textContent="Audio issue: "+(err?.message||err);}
 function createExport(ctx,destination){
   if(!activeMix(true).any)return null;
   // Export destination receives audio; nothing is routed to device speakers.
   return build(ctx,destination,true);
 }
 const activeForExport=()=>activeMix(true).any;
 // The imported local audio file is retained in IndexedDB when browser quota
 // permits, so the user normally doesn't have to import it on every visit.
 async function database(){
   if(!window.indexedDB)return null;
   return await new Promise((resolve,reject)=>{
     const req=indexedDB.open(DB_NAME,1);
     req.onupgradeneeded=()=>req.result.createObjectStore("files");
     req.onsuccess=()=>resolve(req.result);
     req.onerror=()=>reject(req.error);
   });
 }
 async function getSavedFile(){
   const db=await database();if(!db)return null;
   const get=key=>new Promise((resolve,reject)=>{
     const req=db.transaction("files").objectStore("files").get(key);
     req.onsuccess=()=>resolve(req.result||null);
     req.onerror=()=>reject(req.error);
   });
   try{
     const saved=await get(FILE_ID);
     if(saved)return saved;
     // Migrate existing legacy single-user audio into User 1 non-destructively.
     // Never copy this record into User 2.
     if(FILE_ID==="active-1"){
       const original=await get("active");
       if(original){
         await new Promise((resolve,reject)=>{
           const tx=db.transaction("files","readwrite");
           tx.objectStore("files").put(original,FILE_ID);
           tx.oncomplete=resolve;tx.onerror=()=>reject(tx.error);
         });
         return original;
       }
     }
     return null;
   }finally{db.close();}
 }
 async function storeFile(record){
   const db=await database();if(!db)return;
   try{await new Promise((resolve,reject)=>{
     const tx=db.transaction("files","readwrite");
     if(record)tx.objectStore("files").put(record,FILE_ID);
     else tx.objectStore("files").delete(FILE_ID);
     tx.oncomplete=resolve;tx.onerror=()=>reject(tx.error);
     tx.onabort=()=>reject(tx.error);
   });}finally{db.close();}
 }
 async function checkFile(blob,url){
   return await new Promise((resolve,reject)=>{
     const a=new Audio();a.preload="metadata";
     const timer=setTimeout(()=>{cleanup();reject(Error("Could not read audio metadata in this browser."));},13000);
     const cleanup=()=>{
       clearTimeout(timer);a.onloadedmetadata=null;a.onerror=null;
       a.pause();a.removeAttribute("src");a.load();
     };
     a.onloadedmetadata=()=>{
       const duration=a.duration;
       cleanup();
       if(!Number.isFinite(duration)||duration<=0)reject(Error("The imported audio duration is invalid."));
       else resolve(duration);
     };
     a.onerror=()=>{cleanup();reject(Error("This audio format cannot play on your phone."));};
     a.src=url;a.load();
   });
 }
 async function importFile(file,restoring=false){
   if(!file)return;
   if(!restoring){
     if(file.size>LIMIT)throw Error("Audio must be smaller than 50 MB.");
     if(!(/\.(mp3|m4a|wav|ogg|aac|webm)$/i.test(file.name)||/^audio\//i.test(file.type||"")))
       throw Error("Choose an MP3 or another supported audio file.");
   }
   const token=++fileToken;
   importBusy=true;refresh();
   const url=URL.createObjectURL(file);
   try{
     const duration=await checkFile(file,url);
     if(token!==fileToken){URL.revokeObjectURL(url);return;}
     stop(readerSession);readerSession=null;stop(testSession);testSession=null;
     if(fileUrl)URL.revokeObjectURL(fileUrl);
     fileUrl=url;fileName=file.name||"Imported audio";fileDuration=duration;
     importBusy=false;refresh();
     if(!restoring){
       try{await storeFile({blob:file,name:fileName,type:file.type||"audio/mpeg"});}
       catch(err){$("mp3FileStatus").textContent=fileLabel()+" · session only (storage unavailable)";}
     }
   }catch(err){
     URL.revokeObjectURL(url);
     if(token===fileToken){importBusy=false;refresh();}
     throw err;
   }
 }
 async function removeFile(){
   ++fileToken;
   stop(readerSession);readerSession=null;stop(testSession);testSession=null;
   if(fileUrl)URL.revokeObjectURL(fileUrl);
   fileUrl=null;fileName="";fileDuration=0;importBusy=false;refresh();
   $("mp3Import").value="";
   try{await storeFile(null);}catch{}
 }
 function mount(){
   $("toneMode").value=settings.mode;
   $("toneCarrier").value=String(settings.carrier);
   $("toneCarrierNumber").value=String(settings.carrier);
   $("toneBeat").value=String(settings.beat);
   $("toneBeatNumber").value=fmt(settings.beat);
   $("toneVolume").value=String(settings.volume);
   $("ambienceMode").value=settings.fx;
   $("ambienceVolume").value=String(settings.fxVolume);
   $("mp3Volume").value=String(settings.mp3Volume);
   $("mp3Loop").checked=settings.mp3Loop;
   $("toneExport").checked=settings.exportAudio;
   $("ambienceExport").checked=settings.fxExport;
   $("mp3Export").checked=settings.mp3Export;
   $("toneMode").addEventListener("change",e=>{settings.mode=e.target.value;update();});
   $("ambienceMode").addEventListener("change",e=>{settings.fx=e.target.value;update();});
   for(const [id,key,low,high] of [
     ["toneCarrier","carrier",60,1200],["toneBeat","beat",.5,40],
     ["toneVolume","volume",0,25],["ambienceVolume","fxVolume",0,40],
     ["mp3Volume","mp3Volume",0,100]
   ])$(id).addEventListener("input",e=>{settings[key]=clamp(e.target.value,low,high);update();});
   for(const [id,key,range,low,high,digits] of [
     ["toneCarrierNumber","carrier","toneCarrier",60,1200,0],
     ["toneBeatNumber","beat","toneBeat",.5,40,2]
   ])$(id).addEventListener("change",e=>{
     settings[key]=Number(clamp(e.target.value,low,high).toFixed(digits));
     e.target.value=String(settings[key]);
     $(range).value=e.target.value;update();
   });
   for(const [id,key] of [
     ["toneExport","exportAudio"],["ambienceExport","fxExport"],
     ["mp3Export","mp3Export"],["mp3Loop","mp3Loop"]
   ])$(id).addEventListener("change",e=>{settings[key]=e.target.checked;update();});
   $("tonePreview").addEventListener("click",()=>testSession?stopTest():startTest());
   $("mp3Clear").addEventListener("click",()=>removeFile().catch(setError));
   $("mp3Import").addEventListener("change",e=>{
     const file=e.target.files?.[0];
     importFile(file).catch(setError);
     e.target.value="";
   });
   refresh();
   getSavedFile().then(r=>{
     if(r?.blob&&!fileUrl&&fileToken===0)return importFile(
       new File([r.blob],r.name||"Saved audio.mp3",{type:r.type||"audio/mpeg"}),true
     );
   }).catch(()=>{});
 }
 window.FocusFlashTones={
   mount,startReader,stopReader,startTest,stopTest,
   createExport,startSession:startMedia,stopSession:stop,
   getSettings:()=>({...settings}),activeForExport,
   getImportedFile:()=>({name:fileName,duration:fileDuration,loaded:!!fileUrl}),
   getMixLabel:()=>summary()
 };
})();