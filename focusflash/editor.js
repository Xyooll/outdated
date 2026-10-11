/* FocusFlash Studio editor controls. No canvas overlay and no rendering framework.
   Timeline is a lightweight UI for the existing reader's authoritative state. */
(() => {
 "use strict";
 const $=id=>document.getElementById(id);
 const tabs=[...document.querySelectorAll("[data-editor-tab]")];
 const panels=[...document.querySelectorAll("[data-editor-panel]")];
 const TOOL_KEY=window.FocusFlashProfiles?.key("focusflash-open-tool-v1")||"focusflash-open-tool-v1";
 const maxClips=48;
 let zoom=1,lastClipWindow="",cachedText=null,cachedSettings="",timelineVersion=0,lastState=null,timeline=null,refreshPending=false,scriptTimer=null;
 let lastBlockLayout="";

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
   try{localStorage.setItem(TOOL_KEY,name);}catch{}
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
   lastClipWindow="";lastBlockLayout="";
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
 function drawBlockTrack(index){
   const api=window.FocusFlashBlocks;
   const segments=api?.getSequence()||[];
   const wrapper=$("blockTimelineTrack");
   wrapper.classList.toggle("hidden",!api?.isEnabled()||!segments.length);
   if(!segments.length)return;
   const key=segments.map(v=>v.blockId+":"+v.startWord+":"+v.endWord).join("|");
   const strip=$("timelineBlocks");
   if(key!==lastBlockLayout){
     lastBlockLayout=key;
     const groups=[];
     for(const seg of segments){
       const last=groups[groups.length-1];
       if(last&&last.blockId===seg.blockId){
         last.endWord=seg.endWord;last.words+=seg.words;
       }else groups.push({...seg});
     }
     const fragment=document.createDocumentFragment();
     for(let i=0;i<groups.length;i++){
       const group=groups[i];
       const button=document.createElement("button");
       button.type="button";button.className="timeline-block-chip";
       button.dataset.start=String(group.startWord);
       button.dataset.end=String(group.endWord);
       button.title=group.name+" · "+group.repeats+" play(s)";
       button.textContent=group.name+" ×"+group.repeats;
       button.style.flex=Math.max(1,group.words)+" 1 0";
       button.addEventListener("click",()=>{
         const scrub=$("progressRange");scrub.value=String(group.startWord);
         scrub.dispatchEvent(new Event("input",{bubbles:true}));
       });
       fragment.append(button);
     }
     strip.replaceChildren(fragment);
   }
   let current=segments.find(v=>index>=v.startWord&&index<v.endWord) || segments[segments.length-1];
   $("timelineBlockCount").textContent=current.name+" · "+current.iteration+"/"+current.repeats;
   for(const button of strip.querySelectorAll(".timeline-block-chip")){
     const a=Number(button.dataset.start),b=Number(button.dataset.end);
     button.classList.toggle("active",index>=a&&index<b);
   }
 }
 function updatePlayhead(state){
   const t=makeTimeline(),index=Math.min(Math.max(0,state?.index??playheadIndex()),Math.max(t.words.length-1,0));
   const seconds=t.starts[index]||0;
   $("timelineCurrent").textContent=readableTime(seconds);
   drawClips(index);
   drawBlockTrack(index);
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
 function adjustWordSize(raw,source="other"){
   const value=Number(raw);
   if(!Number.isFinite(value))return;
   const size=Math.min(120,Math.max(16,Math.round(value/2)*2));
   const reader=$("fontSize"),exportSize=$("studioScale"),number=$("wordSizeNumber");
   reader.value=String(size);exportSize.value=String(size);number.value=String(size);
   $("studioScaleValue").textContent=size+" px";
   $("fontQuickLabel").textContent=size+" px";
   // app.js owns the actual reader rendering and persists this size.
   // Avoid recursive input dispatches when the source is already the reader.
   if(source!=="reader")
     reader.dispatchEvent(new Event("input",{bubbles:true}));
   if(source==="button"||source==="number")
     exportSize.dispatchEvent(new Event("change",{bubbles:true}));
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
     if(scriptTimer)clearTimeout(scriptTimer);
     scriptTimer=null;
     if(window.FocusFlashBlocks)
       window.FocusFlashBlocks.useSingleScript(String(reader.result||""));
     else{
       $("sourceText").value=String(reader.result||"");
       $("sourceText").dispatchEvent(new Event("input",{bubbles:true}));
       $("loadBtn").click();
     }
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
   $("studioRatio").addEventListener("change",()=>{
     selectRatio();
     // Responsive focus-letter alignment can change with aspect ratio.
     adjustWordSize($("fontSize").value);
   });
   $("studioScale").addEventListener("input",e=>adjustWordSize(e.target.value,"export"));
   $("fontSize").addEventListener("input",e=>adjustWordSize(e.target.value,"reader"));
   $("wordSizeNumber").addEventListener("change",e=>adjustWordSize(e.target.value,"number"));
   for(const id of ["wordSizeMinus","fontQuickMinus"])
     $(id).addEventListener("click",()=>adjustWordSize(Number($("fontSize").value)-2,"button"));
   for(const id of ["wordSizePlus","fontQuickPlus"])
     $(id).addEventListener("click",()=>adjustWordSize(Number($("fontSize").value)+2,"button"));
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
   document.addEventListener("focusflash:blocks-changed",()=>{
     cachedText=null;lastBlockLayout="";renderSoon();
   });
   document.addEventListener("focusflash:render",e=>{
     lastState=e.detail||null;
     renderSoon();
   });
   window.FocusFlashBlocks?.mount?.();
   let lastTool="script";
   try{lastTool=localStorage.getItem(TOOL_KEY)||"script";}catch{}
   selectTab(tabs.some(t=>t.dataset.editorTab===lastTool)?lastTool:"script");
   selectRatio();
   // app.js loads its saved reader size before editor.mount() executes.
   // Use that saved size as the single source of truth for both preview and video.
   adjustWordSize($("fontSize").value);
   makeTimeline();
   updatePlayhead({index:playheadIndex()});
 }
 window.FocusFlashEditor={mount:attach,selectTab,refresh:renderSoon};
})();
