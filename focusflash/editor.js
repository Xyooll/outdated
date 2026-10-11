/* FocusFlash Studio editor controls. No canvas overlay and no rendering framework.
   Timeline is a lightweight UI for the existing reader's authoritative state. */
(() => {
 "use strict";
 const $=id=>document.getElementById(id);
 const tabs=[...document.querySelectorAll("[data-editor-tab]")];
 const panels=[...document.querySelectorAll("[data-editor-panel]")];
 const maxClips=48;
 let zoom=1,lastClipWindow="",cachedText=null,cachedSettings="",timelineVersion=0,lastState=null,timeline=null,refreshPending=false,scriptTimer=null;

 function selectTab(name,scroll=false){
   const tab=tabs.find(t=>t.dataset.editorTab===name);
   if(!tab)return;
   for(const item of tabs){
     const selected=item===tab;
     item.classList.toggle("active",selected);
     if(selected)item.setAttribute("aria-current","page");
     else item.removeAttribute("aria-current");
   }
   for(const panel of panels)panel.hidden=panel.dataset.editorPanel!==name;
   if(scroll&&matchMedia("(max-width:710px)").matches)
     tab.scrollIntoView({block:"nearest",inline:"nearest",behavior:"smooth"});
 }
 function textWords(){
   return $("sourceText").value.trim().split(/\s+/).filter(Boolean);
 }
 function settings(){
   return {
     wpm:Math.max(60,Math.min(2000,Number($("wpm").value)||300)),
     punct:$("punctuationPause").checked,
     long:$("longWordPause").checked
   };
 }
 function wordTime(text,conf){
   let ms=60000/conf.wpm;
   if(conf.punct){
     if(/[.!?][”’"'()\]]*$/.test(text))ms*=1.8;
     else if(/[,;:][”’"'()\]]*$/.test(text))ms*=1.35;
   }
   if(conf.long && [...text].length>=12)ms*=1.2;
   return Math.max(30,ms)/1000;
 }
 function readableTime(seconds){
   const whole=Math.max(0,Math.round(seconds||0));
   return Math.floor(whole/60).toString().padStart(2,"0")+":"+(whole%60).toString().padStart(2,"0");
 }
 function buildTimeline(words){
   const conf=settings();
   const starts=new Float64Array(words.length+1);
   let seconds=0;
   for(let i=0;i<words.length;i++){
     starts[i]=seconds;seconds+=wordTime(words[i],conf);
   }
   starts[words.length]=seconds;
   return {words,starts,total:seconds};
 }
 function makeTimeline(){
   const text=$("sourceText").value,conf=settings();
   const settingsKey=conf.wpm+":"+conf.punct+":"+conf.long;
   // Avoid concatenating huge source texts into a cache key on every word.
   if(text===cachedText&&settingsKey===cachedSettings&&timeline)return timeline;
   cachedText=text;cachedSettings=settingsKey;timelineVersion++;
   const words=textWords();
   timeline=buildTimeline(words);
   lastTimelineKey=key;lastClipWindow="";
   $("timelineClipCount").textContent=words.length.toLocaleString()+" words";
   $("editorTextStats").textContent=words.length.toLocaleString()+" words · "+readableTime(timeline.total)+" estimated";
   $("timelineDuration").textContent=" · "+readableTime(timeline.total);
   $("timelineMid").textContent=readableTime(timeline.total*.5);
   $("timelineEnd").textContent=readableTime(timeline.total);
   return timeline;
 }
 function playheadIndex(){
   return Math.max(0,Number($("progressRange").value)||0);
 }
 function drawClips(index){
   const t=makeTimeline(),count=t.words.length,canvas=$("timelineWords");
   const range=Math.max(6,Math.floor(maxClips/zoom));
   let first=Math.max(0,index-Math.floor(range*.38));
   if(first+range>count)first=Math.max(0,count-range);
   const end=Math.min(count,first+range);
   const id=first+":"+end+":"+timelineVersion;
   if(id!==lastClipWindow){
     lastClipWindow=id;
     const fragment=document.createDocumentFragment();
     if(!count){
       const empty=document.createElement("span");empty.className="timeline-clip";
       empty.textContent="Add some text to begin";empty.style.flex="1";fragment.append(empty);
     }
     for(let i=first;i<end;i++){
       const clip=document.createElement("button");
       clip.type="button";
       clip.className="timeline-clip";
       clip.dataset.wordIndex=String(i);
       clip.textContent=t.words[i];
       clip.title="Jump to word "+(i+1)+": "+t.words[i];
       clip.setAttribute("aria-label","Go to word "+(i+1)+" "+t.words[i]);
       const duration=t.starts[i+1]-t.starts[i];
       clip.style.flex=Math.max(.4,duration).toFixed(2)+" 1 0";
       clip.addEventListener("click",()=>{
         const scrub=$("progressRange");
         scrub.value=String(i);
         scrub.dispatchEvent(new Event("input",{bubbles:true}));
         $("wordStage").focus({preventScroll:true});
       });
       fragment.append(clip);
     }
     canvas.replaceChildren(fragment);
   }
   for(const clip of canvas.children)
     clip.classList.toggle("active",Number(clip.dataset.wordIndex)===index);
 }
 function drawAudioStatus(){
   const mode=$("studioMode").value;
   $("timelineVoiceStatus").textContent=mode==="instant"?"Live TTS":mode==="fast"?"AI voice": "Neural voice";
   const root=$("timelineAudio");
   if(root.dataset.mode===mode)return;
   root.dataset.mode=mode;
   const wave=document.createElement("div");
   wave.className="voice-wave";
   // Deterministic decorative waveform, not a claim that rendered audio is present.
   for(let i=0;i<72;i++){
     const bar=document.createElement("i");
     const y=.35+.5*Math.abs(Math.sin(i*1.9)+Math.sin(i*.51)*.35);
     bar.style.height=Math.round(4+y*21)+"px";
     wave.append(bar);
   }
   root.replaceChildren(wave);
   root.title=mode==="instant"?
     "Live phone text-to-speech for reading. Video soundtrack is synthesized on export.":
     "AI voice can be generated, previewed, and included in exported video.";
 }
 function updatePlayhead(state){
   const t=makeTimeline(),index=Math.min(Math.max(0,state?.index??playheadIndex()),Math.max(t.words.length-1,0));
   const seconds=t.starts[index]||0;
   $("timelineCurrent").textContent=readableTime(seconds);
   drawClips(index);
   drawAudioStatus();
 }
 function renderSoon(){
   if(refreshPending)return;
   refreshPending=true;
   requestAnimationFrame(()=>{
     refreshPending=false;
     updatePlayhead(lastState);
   });
 }
 function selectRatio(){
   const ratio=$("studioRatio").value,info=$("editorPreviewFormat");
   const canvas=$("editorPreview");
   canvas.dataset.ratio=ratio;
   info.textContent=ratio==="wide"?"16:9 · Landscape":ratio==="square"?"1:1 · Square":"9:16 · Vertical";
 }
 function importFile(file){
   if(!file)return;
   if(file.size>3e6){alert("Please choose a text file under 3 MB.");return;}
   if(!/\.(txt|md)$/i.test(file.name)&&!/^text\//i.test(file.type)){
     alert("Choose a .txt or .md file.");return;
   }
   const reader=new FileReader();
   reader.onload=()=>{
     $("sourceText").value=String(reader.result||"");
     $("sourceText").dispatchEvent(new Event("input",{bubbles:true}));
     if(scriptTimer)clearTimeout(scriptTimer);
     scriptTimer=null;
     $("loadBtn").click();
     selectTab("script",true);
   };
   reader.onerror=()=>alert("Could not read this file.");
   reader.readAsText(file);
 }
 function attach(){
   for(const tab of tabs)tab.addEventListener("click",()=>selectTab(tab.dataset.editorTab,true));
   $("jumpExportBtn").addEventListener("click",()=>{
     selectTab("export",true);
     if(matchMedia("(max-width:710px)").matches)
       $("editorExport").scrollIntoView({behavior:"smooth",block:"start"});
   });
   $("topImportBtn").addEventListener("click",()=>{
     selectTab("script",true);$("importFile").click();
   });
   $("loadBtn").addEventListener("click",()=>{
     if(scriptTimer)clearTimeout(scriptTimer);
     scriptTimer=null;
   });
   $("importFile").addEventListener("change",e=>{
     importFile(e.target.files?.[0]);e.target.value="";
   });
   $("studioRatio").addEventListener("change",selectRatio);
   $("sourceText").addEventListener("input",()=>{
     renderSoon();
     if(scriptTimer)clearTimeout(scriptTimer);
     // Clipchamp-like immediate preview after typing/pasting, without
     // interrupting each keystroke or re-tokenizing large texts continuously.
     scriptTimer=setTimeout(()=>{
       scriptTimer=null;$("loadBtn").click();
     },460);
   });
   for(const id of ["wpm","punctuationPause","longWordPause"]){
     $(id).addEventListener("change",renderSoon);
     $(id).addEventListener("input",renderSoon);
   }
   $("studioMode").addEventListener("change",drawAudioStatus);
   $("timelineZoomIn").addEventListener("click",()=>{
     zoom=Math.min(5,zoom+1);lastClipWindow="";renderSoon();$("timelineZoomLabel").textContent=zoom+"×";
   });
   $("timelineZoomOut").addEventListener("click",()=>{
     zoom=Math.max(1,zoom-1);lastClipWindow="";renderSoon();$("timelineZoomLabel").textContent=zoom+"×";
   });
   // Keep export progress visible while the voice panel is not selected.
   const mirror=()=>{
     const output=$("editorExportStatus");
     if(output)output.textContent=$("studioStatus").textContent;
   };
   const observer=new MutationObserver(mirror);
   observer.observe($("studioStatus"),{childList:true,characterData:true,subtree:true});
   mirror();
   document.addEventListener("focusflash:render",e=>{
     lastState=e.detail||null;
     renderSoon();
   });
   selectTab("script");
   selectRatio();
   makeTimeline();
   updatePlayhead({index:playheadIndex()});
 }
 window.FocusFlashEditor={mount:attach,selectTab,refresh:renderSoon};
})();
