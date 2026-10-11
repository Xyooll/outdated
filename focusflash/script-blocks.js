/* FocusFlash Script Blocks: loop bounded passages, then move to next block.
   Local-only editing. The expanded playback text remains compatible with the
   original reader, all TTS engines, and WebM export. */
(() => {
 "use strict";
 const $=id=>document.getElementById(id);
 const STORAGE="focusflash-script-blocks-v1",MAX_REPEAT=100,MAX_WORDS=100000;
 const wordsOf=text=>String(text||"").trim().split(/\s+/).filter(Boolean);
 const id=()=>String(Date.now())+"-"+String(Math.random()).slice(2,8);
 const block=(text="",name="",repeats=1)=>({id:id(),name,text,repeats});
 const clamp=(value,min,max)=>Math.min(max,Math.max(min,Math.round(Number(value)||min)));
 let state={enabled:false,singleText:"",blocks:[]},sections=[],compiled="",timer=null,ready=false;
 try{
   const data=JSON.parse(localStorage.getItem(STORAGE)||"null");
   if(data&&typeof data==="object"){
     state.enabled=data.enabled===true;
     state.singleText=typeof data.singleText==="string"?data.singleText:"";
     state.blocks=Array.isArray(data.blocks)?data.blocks.slice(0,60).map(b=>({
       id:typeof b.id==="string"?b.id:id(),
       name:String(b.name||"").slice(0,100),
       text:String(b.text||"").slice(0,250000),
       repeats:clamp(b.repeats,1,MAX_REPEAT)
     })):[];
   }
 }catch{}
 const persist=()=>{try{localStorage.setItem(STORAGE,JSON.stringify(state));}catch{}};
 function build(){
   const output=[],steps=[];let total=0;
   for(let i=0;i<state.blocks.length;i++){
     const item=state.blocks[i],text=item.text.trim(),num=wordsOf(text).length;
     if(!num)continue;
     for(let repeat=0;repeat<item.repeats;repeat++){
       if(total+num>MAX_WORDS)throw Error("Sequence exceeds "+MAX_WORDS.toLocaleString()+" words. Reduce repetitions.");
       steps.push({
         blockId:item.id,name:item.name.trim()||"Block "+(i+1),
         blockIndex:i,iteration:repeat+1,repeats:item.repeats,
         startWord:total,endWord:total+num,words:num
       });
       output.push(text);
       total+=num;
     }
   }
   return {text:output.join("\n\n"),sections:steps,total};
 }
 function notify(message,problem=false){
   const status=$("blocksStatus");
   status.textContent=message;
   status.dataset.error=problem?"true":"false";
 }
 function saveAndApply(){
   if(!ready||!state.enabled)return;
   persist();
   try{
     const seq=build();
     compiled=seq.text;sections=seq.sections;
     if($("sourceText").value!==compiled){
       $("sourceText").value=compiled;
       $("sourceText").dispatchEvent(new Event("input",{bubbles:true}));
     }
     $("loadBtn").click();
     const duration=seq.total;
     notify(seq.sections.length+" segment"+(seq.sections.length===1?"":"s")+
       " · "+duration.toLocaleString()+" words · plays blocks in order");
     document.dispatchEvent(new CustomEvent("focusflash:blocks-changed",{detail:{sections:sections.slice()}}));
   }catch(error){notify(error.message,true);}
 }
 function queueApply(){
   persist();
   if(timer)clearTimeout(timer);
   timer=setTimeout(()=>{timer=null;saveAndApply();},350);
 }
 function makeButton(text,label,onClick,disabled=false){
   const b=document.createElement("button");
   b.type="button";b.textContent=text;b.title=label;b.setAttribute("aria-label",label);
   b.disabled=disabled;b.addEventListener("click",onClick);return b;
 }
 function render(){
   const root=$("scriptBlockList");
   const fragment=document.createDocumentFragment();
   for(let i=0;i<state.blocks.length;i++){
     const item=state.blocks[i],card=document.createElement("article");
     card.className="script-block";card.dataset.blockId=item.id;
     const top=document.createElement("div");top.className="script-block-head";
     const num=document.createElement("span");num.className="script-block-index";
     num.textContent="BLOCK "+String(i+1).padStart(2,"0");
     const tools=document.createElement("div");tools.className="script-block-tools";
     tools.append(
       makeButton("↑","Move block up",()=>move(i,-1),i===0),
       makeButton("↓","Move block down",()=>move(i,1),i===state.blocks.length-1),
       makeButton("⧉","Duplicate block",()=>duplicate(i)),
       makeButton("×","Delete block",()=>remove(i),state.blocks.length===1)
     );
     top.append(num,tools);
     const nameLabel=document.createElement("label");nameLabel.textContent="Block title";
     const name=document.createElement("input");name.type="text";name.maxLength=100;name.value=item.name;
     name.placeholder="e.g. Confidence";
     name.addEventListener("input",()=>{item.name=name.value;queueApply();});
     nameLabel.append(name);
     const textLabel=document.createElement("label");textLabel.textContent="Text to flash";
     const field=document.createElement("textarea");field.rows=4;field.spellcheck=true;
     field.placeholder="Write the words for this block…";field.value=item.text;
     field.addEventListener("input",()=>{item.text=field.value;queueApply();});
     textLabel.append(field);
     const bottom=document.createElement("div");bottom.className="script-block-bottom";
     const repeatLabel=document.createElement("label");repeatLabel.className="repeat-label";
     repeatLabel.textContent="Repeat this block";
     const repeats=document.createElement("input");
     repeats.type="number";repeats.min="1";repeats.max=String(MAX_REPEAT);
     repeats.step="1";repeats.inputMode="numeric";repeats.value=String(item.repeats);
     const suffix=document.createElement("span");suffix.textContent="times";
     repeats.addEventListener("change",()=>{
       item.repeats=clamp(repeats.value,1,MAX_REPEAT);
       repeats.value=String(item.repeats);saveAndApply();
     });
     repeatLabel.append(repeats,suffix);
     const summary=document.createElement("span");summary.className="script-block-count";
     summary.textContent=wordsOf(item.text).length+" words × "+item.repeats;
     bottom.append(repeatLabel,summary);
     card.append(top,nameLabel,textLabel,bottom);
     fragment.append(card);
   }
   root.replaceChildren(fragment);
 }
 function move(i,step){
   const j=i+step;if(j<0||j>=state.blocks.length)return;
   [state.blocks[i],state.blocks[j]]=[state.blocks[j],state.blocks[i]];
   render();saveAndApply();
 }
 function duplicate(i){
   if(state.blocks.length>=60){notify("Maximum 60 blocks.",true);return;}
   const value=state.blocks[i];
   state.blocks.splice(i+1,0,block(value.text,value.name+" copy",value.repeats));
   render();saveAndApply();
 }
 function remove(i){
   if(state.blocks.length<=1)return;
   state.blocks.splice(i,1);render();saveAndApply();
 }
 function enable(next){
   if(timer){clearTimeout(timer);timer=null;}
   if(next===state.enabled&&ready)return;
   if(next){
     state.singleText=$("sourceText").value;
     if(!state.blocks.length)state.blocks.push(block(state.singleText,"Opening",1));
   }else{
     $("sourceText").value=state.singleText;
     $("sourceText").dispatchEvent(new Event("input",{bubbles:true}));
     $("loadBtn").click();
     sections=[];compiled="";
     document.dispatchEvent(new Event("focusflash:blocks-changed"));
   }
   state.enabled=next;
   $("singleScriptEditor").hidden=next;
   $("blockScriptEditor").hidden=!next;
   $("scriptModeSingle").classList.toggle("active",!next);
   $("scriptModeBlocks").classList.toggle("active",next);
   $("scriptModeSingle").setAttribute("aria-pressed",String(!next));
   $("scriptModeBlocks").setAttribute("aria-pressed",String(next));
   if(next){render();saveAndApply();}
   persist();
 }
 function useSingleScript(text){
   // Used by import so a text file never silently overwrites block composition.
   if(state.enabled)enable(false);
   state.singleText=String(text||"");
   $("sourceText").value=state.singleText;
   $("sourceText").dispatchEvent(new Event("input",{bubbles:true}));
   $("loadBtn").click();
   persist();
 }
 function onNewBlock(){
   if(state.blocks.length>=60){notify("Maximum 60 blocks.",true);return;}
   state.blocks.push(block("","Block "+(state.blocks.length+1),1));
   render();saveAndApply();
   const area=$("scriptBlockList").lastElementChild?.querySelector("textarea");
   area?.focus();
 }
 function mount(){
   ready=true;
   $("scriptModeSingle").addEventListener("click",()=>enable(false));
   $("scriptModeBlocks").addEventListener("click",()=>enable(true));
   $("addScriptBlock").addEventListener("click",onNewBlock);
   $("applyScriptBlocks").addEventListener("click",()=>{if(timer)clearTimeout(timer);timer=null;saveAndApply();});
   $("sourceText").addEventListener("input",()=>{
     if(!state.enabled){state.singleText=$("sourceText").value;persist();}
   });
   // Restore the user's original editor mode after the main reader initializes.
   const wanted=state.enabled;state.enabled=!wanted;
   enable(wanted);
   if(!wanted)state.singleText=$("sourceText").value;
 }
 window.FocusFlashBlocks={
   mount,useSingleScript,
   isEnabled:()=>state.enabled,
   getSequence:()=>state.enabled?sections.slice():[],
   getBlocks:()=>state.blocks.map(b=>({...b})),
   flush:()=>{if(timer){clearTimeout(timer);timer=null;saveAndApply();}},
   compiledText:()=>state.enabled?compiled:$("sourceText").value
 };
})();
