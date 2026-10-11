/* FocusFlash seekable transcript panel.
 * A lightweight view of the same script/playback index used by the reader.
 * Rebuilds only when the script/timing changes, not on every flashed word.
 * In Blocks mode, transcript passages respect each repeated block boundary.
 */
(() => {
 "use strict";
 const $=id=>document.getElementById(id);
 const LIMIT=24,WINDOW=72;
 let segments=[],starts=new Float64Array(),lastText=null,lastSettings=null;
 let dirty=true,activeIndex=0,activeSegment=-1,windowKey="",search="";
 let list=null,status=null;

 const time=sec=>{
   const s=Math.max(0,Math.floor(sec||0));
   return String(Math.floor(s/60)).padStart(2,"0")+":"+String(s%60).padStart(2,"0");
 };
 const settings=()=>({
   wpm:Math.max(60,Math.min(2000,Number($("wpm").value)||300)),
   punctuation:$("punctuationPause").checked,
   long:$("longWordPause").checked
 });
 const duration=(word,s)=>{
   let ms=60000/s.wpm;
   if(s.punctuation){
     if(/[.!?][”’"'()\]]*$/.test(word))ms*=1.8;
     else if(/[,;:][”’"'()\]]*$/.test(word))ms*=1.35;
   }
   if(s.long&&[...word].length>=12)ms*=1.2;
   return Math.max(30,ms)/1000;
 };
 function rebuild(){
   const input=$("sourceText").value,conf=settings();
   const settingsId=[conf.wpm,conf.punctuation,conf.long].join(":");
   if(!dirty&&input===lastText&&settingsId===lastSettings)return;
   lastText=input;lastSettings=settingsId;dirty=false;
   const words=input.trim().split(/\s+/).filter(Boolean).slice(0,100000);
   starts=new Float64Array(words.length+1);
   for(let i=0;i<words.length;i++)starts[i+1]=starts[i]+duration(words[i],conf);
   const sequence=window.FocusFlashBlocks?.getSequence?.()||[];
   const ranges=sequence.length?sequence.map((part,i)=>({
     from:Math.max(0,Math.min(words.length,part.startWord)),
     to:Math.max(0,Math.min(words.length,part.endWord)),
     label:part.name||"Block "+(part.blockIndex+1),
     repeat:(part.iteration||1)+"/"+(part.repeats||1)
   })).filter(part=>part.to>part.from):[
     {from:0,to:words.length,label:"Script",repeat:""}
   ];
   const next=[];
   for(const range of ranges){
     let at=range.from;
     while(at<range.to){
       let end=Math.min(range.to,at+LIMIT);
       // Prefer sentence boundaries while retaining short, readable cards.
       for(let i=Math.min(end,range.to)-1;i>=at+5;i--){
         if(/[.!?][”’"'()\]]*$/.test(words[i])){end=i+1;break;}
       }
       const phrase=words.slice(at,end).join(" ");
       next.push({
         start:at,end,time:starts[at],text:phrase,
         label:range.label,repeat:range.repeat
       });
       at=end;
     }
   }
   segments=next;windowKey="";
   const count=$("transcriptCount");
   if(count)count.textContent=segments.length.toLocaleString()+
     (segments.length===1?" passage":" passages");
 }
 function locate(wordIndex){
   if(!segments.length)return -1;
   let lo=0,hi=segments.length-1;
   while(lo<hi){
     const m=Math.floor((lo+hi)/2);
     if(segments[m].end<=wordIndex)lo=m+1;
     else hi=m;
   }
   return lo;
 }
 function selectedIndices(){
   if(search){
     const hits=[];
     for(let i=0;i<segments.length;i++){
       if((segments[i].text+" "+segments[i].label).toLowerCase().includes(search))hits.push(i);
       if(hits.length>=120)break;
     }
     return {ids:hits,key:"filter:"+search+":"+segments.length,found:hits.length};
   }
   const index=Math.max(0,locate(activeIndex));
   // Slide the rendered window only every 24 passages to avoid DOM churn.
   const first=Math.max(0,Math.min(segments.length-WINDOW,
     Math.floor(index/24)*24-24));
   const end=Math.min(segments.length,first+WINDOW);
   const ids=Array.from({length:end-first},(_,i)=>first+i);
   return {ids,key:"window:"+first+":"+end+":"+segments.length,found:segments.length};
 }
 function makeRow(info,i){
   const button=document.createElement("button");
   button.type="button";
   button.className="transcript-entry";
   button.dataset.segment=String(i);
   button.setAttribute("aria-label",time(info.time)+" "+info.text);
   const top=document.createElement("span");top.className="transcript-entry-top";
   const ts=document.createElement("span");ts.className="transcript-time";ts.textContent=time(info.time);
   const tag=document.createElement("span");tag.className="transcript-block-label";
   tag.textContent=info.repeat?info.label+" · "+info.repeat:info.label;
   top.append(ts,tag);
   const words=document.createElement("span");words.className="transcript-sentence";
   words.textContent=info.text;
   button.append(top,words);
   button.addEventListener("click",()=>{
     const slider=$("progressRange");
     slider.value=String(info.start);
     slider.dispatchEvent(new Event("input",{bubbles:true}));
     if(matchMedia("(max-width:800px)").matches)
       document.querySelector(".editor-preview-section")?.scrollIntoView({behavior:"smooth",block:"start"});
   });
   return button;
 }
 function draw(force=false){
   if(!list)return;
   rebuild();
   if(!segments.length){
     if(force||windowKey!=="empty"){
       windowKey="empty";
       const empty=document.createElement("div");
       empty.className="transcript-empty";
       empty.textContent="Your transcript will appear here when you add a script or blocks.";
       list.replaceChildren(empty);
     }
     return;
   }
   const view=selectedIndices();
   if(!force&&windowKey===view.key)return;
   windowKey=view.key;
   const fragment=document.createDocumentFragment();
   if(!view.ids.length){
     const p=document.createElement("p");p.className="transcript-empty";
     p.textContent="No matching passages. Try a different search.";
     fragment.append(p);
   }
   for(const i of view.ids)fragment.append(makeRow(segments[i],i));
   list.replaceChildren(fragment);
   if(search){
     $("transcriptHelp").textContent=
       view.ids.length+(view.ids.length===120?"+":"")+" matching passages";
   }else{
     $("transcriptHelp").textContent=
       "Select a passage to jump · "+segments.length.toLocaleString()+" total passages";
   }
 }
 function highlight(index){
   activeIndex=Math.max(0,index);
   if(!list)return;
   rebuild();
   const segment=locate(activeIndex);
   $("transcriptNow").textContent=time(starts[Math.min(activeIndex,starts.length-1)]||0);
   draw();
   if(segment===activeSegment&&list.querySelector('.transcript-entry.current'))return;
   activeSegment=segment;
   const old=list.querySelector(".transcript-entry.current");
   if(old){old.classList.remove("current");old.removeAttribute("aria-current");}
   const current=list.querySelector('[data-segment="'+segment+'"]');
   if(current){
     current.classList.add("current");
     current.setAttribute("aria-current","location");
     if(!search&&$("editorTranscript")&&!$("editorTranscript").hidden){
       const visibleTop=list.scrollTop,visibleBottom=visibleTop+list.clientHeight;
       const top=current.offsetTop-list.offsetTop;
       if(top<visibleTop+8||top+current.offsetHeight>visibleBottom-8)
         list.scrollTop=Math.max(0,top-list.clientHeight*.33);
     }
   }
 }
 function mount(){
   list=$("transcriptList");status=$("transcriptHelp");
   if(!list)return;
   $("transcriptSearch").addEventListener("input",event=>{
     search=event.target.value.trim().toLowerCase().slice(0,80);
     windowKey="";draw(true);highlight(activeIndex);
   });
   $("transcriptEditBtn").addEventListener("click",()=>
     window.FocusFlashEditor?.selectTab?.("script",true));
   $("sourceText").addEventListener("input",()=>{dirty=true;});
   for(const id of ["wpm","punctuationPause","longWordPause"]){
     $(id).addEventListener("input",()=>{dirty=true;});
     $(id).addEventListener("change",()=>{dirty=true;});
   }
   document.addEventListener("focusflash:blocks-changed",()=>{
     dirty=true;draw(true);highlight(Number($("progressRange").value)||0);
   });
   document.addEventListener("focusflash:render",event=>{
     highlight(Number(event.detail?.index)||0);
   });
   highlight(Number($("progressRange").value)||0);
 }
 window.FocusFlashTranscript={mount,update:highlight,refresh:()=>{dirty=true;draw(true);highlight(activeIndex)}};
})();
