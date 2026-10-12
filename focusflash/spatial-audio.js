/* FocusFlash Spatial Studio - moving 3D headphone sound via Web Audio HRTF.
   Audio-rate oscillator modulation avoids drifting JS pan timers.
   Never mixes the independent left/right binaural beat oscillators into HRTF.
*/
(() => {
 "use strict";
 const $=id=>document.getElementById(id);
 const KEY=window.FocusFlashProfiles?.key("focusflash-spatial-v1")||"focusflash-spatial-v1";
 const MOTIONS=["orbit","left-right","front-back","up-down","figure8","left","right","center"];
 const LABELS={
   orbit:"Orbit", "left-right":"Left / right", "front-back":"Front / back",
   "up-down":"Above / below",figure8:"Figure eight",
   left:"Fixed left",right:"Fixed right",center:"Centered"
 };
 const clamp=(n,low,high)=>Math.max(low,Math.min(high,Number.isFinite(Number(n))?Number(n):low));
 const normalize=s=>({
   enabled:s?.enabled===true,source:s?.source==="mp3"?"mp3":"probe",
   motion:MOTIONS.includes(s?.motion)?s.motion:"orbit",
   speed:clamp(s?.speed??12,3,45),
   width:clamp(s?.width??1.3,.25,2.5),
   volume:clamp(s?.volume??12,0,25),
   includeExport:s?.includeExport!==false
 });
 let settings=normalize({});
 try{settings=normalize(JSON.parse(localStorage.getItem(KEY)||"null"));}catch{}
 const sessions=new Set();
 const fmt=n=>Number(n.toFixed(2)).toString();
 const save=()=>{try{localStorage.setItem(KEY,JSON.stringify(settings));}catch{}};
 const loaded=()=>!!window.FocusFlashTones?.getImportedFile?.().loaded;
 function active(forExport=false,mp3Available=loaded()){
   const on=settings.enabled&&(!forExport||settings.includeExport);
   return {demo:on&&settings.source==="probe",
     mp3:on&&settings.source==="mp3"&&!!mp3Available};
 }
 function label(forExport=false,mp3Available=loaded()){
   const a=active(forExport,mp3Available);
   return a.demo?"Moving 3D shimmer · "+LABELS[settings.motion]:
     a.mp3?"3D moving MP3 · "+LABELS[settings.motion]:"";
 }
 function refresh(){
   $("spatialEnable").checked=settings.enabled;
   $("spatialSource").value=settings.source;
   $("spatialMotion").value=settings.motion;
   $("spatialSpeed").value=String(settings.speed);
   $("spatialWidth").value=String(settings.width);
   $("spatialVolume").value=String(settings.volume);
   $("spatialExport").checked=settings.includeExport;
   $("spatialSpeedValue").textContent=fmt(settings.speed)+" sec / cycle";
   $("spatialWidthValue").textContent=fmt(settings.width)+"×";
   $("spatialVolumeValue").textContent=settings.volume+"%";
   $("spatialDemoVolumeRow").hidden=settings.source!=="probe";
   $("spatialHelp").textContent=!settings.enabled?
     "Enable spatial audio, choose a source and listen with stereo headphones.":
     settings.source==="mp3"&&!loaded()?
     "Import your own MP3/audio file below first, then use Preview sound mix.":
     settings.source==="mp3"?
     "Moving 3D effect is applied to your imported audio. Use Imported audio volume to control loudness.":
     "The built-in shimmer moves around you; it can play alongside your other sound layers.";
 }
 function create(ctx,destination,forExport=false,mp3Available=loaded()){
   const a=active(forExport,mp3Available);
   if(!a.demo&&!a.mp3)return null;
   if(!ctx.createPanner||!ctx.createPeriodicWave)
     throw Error("3D headphone spatialization is unsupported in this browser.");
   const p=ctx.createPanner();
   p.panningModel="HRTF";p.distanceModel="inverse";
   p.refDistance=1;p.maxDistance=10;p.rolloffFactor=0;
   const now=ctx.currentTime;
   for(const axis of ["positionX","positionY","positionZ"]){
     if(!p[axis]?.setValueAtTime)
       throw Error("This browser does not support automated 3D sound positions.");
     p[axis].setValueAtTime(0,now);
   }
   const out=ctx.createGain();
   out.gain.setValueAtTime(a.demo?0:1,now);
   if(a.demo)out.gain.setTargetAtTime(settings.volume/100,now,.035);
   p.connect(out);out.connect(destination);
   const nodes=[p,out],sources=[],axes=[],freq=1/settings.speed,width=settings.width;
   const cosine=ctx.createPeriodicWave(
     new Float32Array([0,1]),new Float32Array([0,0]),{disableNormalization:true});
   function mod(axis,mult,scale,cos=false){
     const osc=ctx.createOscillator();
     if(cos)osc.setPeriodicWave(cosine);
     else osc.type="sine";
     osc.frequency.setValueAtTime(freq*mult,now);
     const g=ctx.createGain();
     g.gain.value=scale*width;
     osc.connect(g);g.connect(p[axis]);osc.start(now);
     nodes.push(osc,g);sources.push(osc);axes.push({osc,g,mult,scale});
   }
   const motion=settings.motion;
   if(motion==="orbit"){mod("positionX",1,1);mod("positionZ",1,1,true);}
   else if(motion==="left-right"){
     p.positionZ.setValueAtTime(-.8,now);mod("positionX",1,1);
   }else if(motion==="front-back"){
     p.positionX.setValueAtTime(.35,now);mod("positionZ",1,1,true);
   }else if(motion==="up-down"){
     p.positionZ.setValueAtTime(-.7,now);
     mod("positionY",1,.85);mod("positionX",1,.22,true);
   }else if(motion==="figure8"){
     mod("positionX",1,1);mod("positionZ",2,.68,true);
   }else{
     p.positionZ.setValueAtTime(-.75,now);
     p.positionX.setValueAtTime(motion==="left"?-width:motion==="right"?width:0,now);
   }
   if(a.demo){
     // Mix a soft broadband texture with pitched partials; high-frequency
     // texture provides pinna cues that are absent in a simple 220 Hz sine.
     const sampleRate=22050,len=sampleRate*3;
     const buffer=ctx.createBuffer(1,len,sampleRate);
     const data=buffer.getChannelData(0);
     let seed=0x7d25a31b,low=0,slow=0;
     for(let i=0;i<len;i++){
       seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;
       const w=(seed>>>0)/2147483648-1;
       low=.98*low+.02*w;slow=.998*slow+.002*w;
       data[i]=Math.max(-.8,Math.min(.8,(w*.10+low*.28+slow*.3)*
         Math.min(1,i/660,(len-1-i)/660)));
     }
     const source=ctx.createBufferSource();
     source.buffer=buffer;source.loop=true;
     source.connect(p);source.start(now);nodes.push(source);sources.push(source);
     for(const [hz,v] of [[330,.43],[495,.18]]){
       const o=ctx.createOscillator();o.type="sine";
       o.frequency.setValueAtTime(hz,now);
       const g=ctx.createGain();g.gain.value=v;
       o.connect(g);g.connect(p);o.start(now);
       nodes.push(o,g);sources.push(o);
     }
   }
   const session={
     input:p,fadeGain:a.demo?out:null,nodes,sources,axes,ctx,
     update(){
       if(a.demo)out.gain.setTargetAtTime(settings.volume/100,ctx.currentTime,.05);
       for(const item of axes){
         item.osc.frequency.setTargetAtTime(item.mult/settings.speed,ctx.currentTime,.1);
         item.g.gain.setTargetAtTime(item.scale*settings.width,ctx.currentTime,.1);
       }
       if(!axes.length){
         p.positionX.setTargetAtTime(
           settings.motion==="left"?-settings.width:settings.motion==="right"?settings.width:0,
           ctx.currentTime,.07);
       }
     },
     dispose(){sessions.delete(session);}
   };
   sessions.add(session);
   return session;
 }
 function change(rebuild=false){
   save();refresh();
   if(rebuild)window.FocusFlashTones?.restartMix?.();
   else{
     for(const session of sessions)session.update();
     window.FocusFlashTones?.refreshMix?.();
   }
 }
 function mount(){
   $("spatialEnable").addEventListener("change",e=>{
     settings.enabled=e.target.checked;change(true);
   });
   $("spatialSource").addEventListener("change",e=>{
     settings.source=e.target.value==="mp3"?"mp3":"probe";change(true);
   });
   $("spatialMotion").addEventListener("change",e=>{
     settings.motion=MOTIONS.includes(e.target.value)?e.target.value:"orbit";
     change(true);
   });
   for(const [id,key,lo,hi] of [
     ["spatialSpeed","speed",3,45],["spatialWidth","width",.25,2.5],
     ["spatialVolume","volume",0,25]
   ])$(id).addEventListener("input",e=>{
     settings[key]=clamp(e.target.value,lo,hi);change(false);
   });
   $("spatialExport").addEventListener("change",e=>{
     settings.includeExport=e.target.checked;change(false);
   });
   refresh();
 }
 window.FocusFlashSpatial={
   mount,active,label,create,refresh,
   getSettings:()=>({...settings}),
   getActiveCount:()=>sessions.size
 };
})();