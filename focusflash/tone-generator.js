/* FocusFlash Sound Generator — pure sine tones / stereo binaural beats.
   Local Web Audio oscillators only. No prerecorded audio, model, network or API.
   A binaural setting sends f-d/2 to the left and f+d/2 to the right.
   Proper headphones and stereo playback are necessary for this effect.
*/
(() => {
 "use strict";
 const $=id=>document.getElementById(id);
 const KEY="focusflash-tones-v1";
 const clamp=(x,min,max)=>Math.max(min,Math.min(max,Number.isFinite(Number(x))?Number(x):min));
 const normalize=obj=>({
   mode:["off","pure","binaural"].includes(obj?.mode)?obj.mode:"off",
   carrier:clamp(obj?.carrier??220,60,1200),
   beat:clamp(obj?.beat??6,.5,40),
   volume:clamp(obj?.volume??8,0,25),
   exportAudio:obj?.exportAudio!==false
 });
 let settings=normalize({});
 try{settings=normalize(JSON.parse(localStorage.getItem(KEY)||"null"));}catch{}
 let sharedContext=null,live=null,preview=null;
 const store=()=>{try{localStorage.setItem(KEY,JSON.stringify(settings));}catch{}};
 const label=()=>settings.mode==="off"?"Sound off":
   settings.mode==="pure"?settings.carrier+" Hz pure tone":
   (settings.carrier-settings.beat/2).toFixed(2)+" Hz left · "+
   (settings.carrier+settings.beat/2).toFixed(2)+" Hz right";
 function describe(){
   const value=$("toneCurrent");
   if(value)value.textContent=label();
   const warning=$("toneHeadphones");
   if(warning)warning.hidden=settings.mode!=="binaural";
   const checkbox=$("toneExport");
   if(checkbox)checkbox.checked=settings.exportAudio;
   const carrier=$("toneCarrierValue");if(carrier)carrier.textContent=settings.carrier+" Hz";
   const beat=$("toneBeatValue");if(beat)beat.textContent=settings.beat.toFixed(1)+" Hz";
   const volume=$("toneVolumeValue");if(volume)volume.textContent=settings.volume+"%";
   const beats=$("toneBeatRow");if(beats)beats.hidden=settings.mode!=="binaural";
   const hint=$("toneStatus");
   if(hint){
     hint.textContent=(preview?"Preview playing · ":live?"Reading with sound · ":"Ready · ")+label();
   }
   const btn=$("tonePreview");
   if(btn)btn.textContent=preview?"■ Stop tone":"▶ Test tone";
   const timeline=$("timelineToneStatus");
   if(timeline)timeline.textContent=settings.mode==="off"?"Disabled":
     settings.mode==="pure"?"Pure · "+settings.carrier+" Hz":
     "Binaural · "+settings.beat.toFixed(1)+" Hz";
   const track=$("timelineTone");
   if(track)track.dataset.mode=settings.mode;
 }
 function stop(session){
   if(!session||session.stopped)return;
   session.stopped=true;
   const {ctx,gain,oscillators}=session;
   const now=ctx.currentTime;
   try{gain.gain.cancelScheduledValues(now);gain.gain.setTargetAtTime(0,now,.009);}catch{}
   for(const osc of oscillators){try{osc.stop(now+.075);}catch{}}
   // A stop callback owns node disconnection after the fade.
   let left=oscillators.length;
   for(const osc of oscillators){
     osc.onended=()=>{
       if(--left===0){
         for(const node of session.nodes){try{node.disconnect();}catch{}}
       }
     };
   }
 }
 function createSession(ctx,destination){
   if(settings.mode==="off")return null;
   const master=ctx.createGain();
   const now=ctx.currentTime;
   master.gain.setValueAtTime(0,now);
   master.gain.setTargetAtTime(settings.volume/100,now,.025);
   master.connect(destination);
   const nodes=[master],oscillators=[];
   const osc=hz=>{
     const o=ctx.createOscillator();
     o.type="sine";
     o.frequency.setValueAtTime(hz,now);
     nodes.push(o);oscillators.push(o);
     return o;
   };
   if(settings.mode==="pure"){
     const o=osc(settings.carrier);
     o.connect(master);o.start(now);
   }else{
     if(typeof ctx.createStereoPanner!=="function"){
       master.disconnect();
       throw Error("This browser cannot separate left and right audio. Update Chrome for binaural beats.");
     }
     const left=osc(settings.carrier-settings.beat/2),right=osc(settings.carrier+settings.beat/2);
     const leftPan=ctx.createStereoPanner(),rightPan=ctx.createStereoPanner();
     leftPan.pan.value=-1;rightPan.pan.value=1;
     nodes.push(leftPan,rightPan);
     left.connect(leftPan);leftPan.connect(master);
     right.connect(rightPan);rightPan.connect(master);
     left.start(now);right.start(now);
   }
   return {ctx,gain:master,nodes,oscillators,mode:settings.mode,stopped:false};
 }
 function updateSession(session){
   if(!session||session.stopped)return;
   if(session.mode!==settings.mode){
     if(session===live){stop(live);live=null;startReader();}
     else if(session===preview){stop(preview);preview=null;startTest();}
     return;
   }
   const now=session.ctx.currentTime;
   session.gain.gain.setTargetAtTime(settings.volume/100,now,.025);
   const freq=session.mode==="pure"?[settings.carrier]:
      [settings.carrier-settings.beat/2,settings.carrier+settings.beat/2];
   for(let i=0;i<session.oscillators.length;i++)
     session.oscillators[i].frequency.setTargetAtTime(freq[i],now,.035);
 }
 function update(){
   stopIfOff();
   updateSession(live);updateSession(preview);
   store();describe();
 }
 function stopIfOff(){
   if(settings.mode!=="off")return;
   stop(live);stop(preview);live=null;preview=null;
 }
 function ensureContext(){
   if(!sharedContext||sharedContext.state==="closed")
     sharedContext=new (window.AudioContext||window.webkitAudioContext)();
   if(sharedContext.state==="suspended")sharedContext.resume().catch(()=>{});
   return sharedContext;
 }
 function startReader(){
   if(settings.mode==="off")return;
   stop(preview);preview=null;
   stop(live);live=null;
   try{
     const ctx=ensureContext();
     live=createSession(ctx,ctx.destination);
     describe();
   }catch(error){setError(error)}
 }
 function stopReader(){
   stop(live);live=null;describe();
 }
 function startTest(){
   if(settings.mode==="off"){
     setError(Error("Choose Pure tone or Binaural beats first."));return;
   }
   stop(preview);preview=null;
   stop(live);live=null;
   try{
     const ctx=ensureContext();
     preview=createSession(ctx,ctx.destination);describe();
   }catch(error){setError(error)}
 }
 function toggleTest(){
   if(preview){stop(preview);preview=null;describe();}
   else startTest();
 }
 function stopTest(){stop(preview);preview=null;describe();}
 function setError(error){
   const status=$("toneStatus");if(status)status.textContent="Sound unavailable: "+error.message;
 }
 function createExport(ctx,destination){
   if(!settings.exportAudio||settings.mode==="off")return null;
   // No sound is sent to the phone speaker while rendering.
   return createSession(ctx,destination);
 }
 function mount(){
   $("toneMode").value=settings.mode;
   $("toneCarrier").value=String(settings.carrier);
   $("toneBeat").value=String(settings.beat);
   $("toneVolume").value=String(settings.volume);
   $("toneExport").checked=settings.exportAudio;
   $("toneMode").addEventListener("change",e=>{settings.mode=e.target.value;update();});
   for(const [id,key] of [["toneCarrier","carrier"],["toneBeat","beat"],["toneVolume","volume"]])
     $(id).addEventListener("input",e=>{
       const [low,high]=key==="carrier"?[60,1200]:key==="beat"?[.5,40]:[0,25];
       settings[key]=clamp(e.target.value,low,high);update();
     });
   $("toneExport").addEventListener("change",e=>{settings.exportAudio=e.target.checked;update();});
   $("tonePreview").addEventListener("click",toggleTest);
   describe();
 }
 window.FocusFlashTones={
   mount,startReader,stopReader,startTest,stopTest,
   createExport,stopSession:stop,getSettings:()=>({...settings}),
   activeForExport:()=>settings.exportAudio&&settings.mode!=="off"
 };
})();
