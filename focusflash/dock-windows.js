/* FocusFlash four-window dock.
 * Resizable, keyboard-accessible splitters on desktop.
 * The active profile owns its own window sizes in localStorage.
 * On phones the windows adapt to the player + lower Tools/Timeline switcher.
 */
(() => {
 "use strict";
 const $=id=>document.getElementById(id);
 const KEY=window.FocusFlashProfiles?.key("focusflash-dock-layout-v1")||"focusflash-dock-layout-v1";
 const DEFAULT={left:176,right:356,bottom:272};
 const valid=x=>Number.isFinite(Number(x))?Number(x):0;
 let size={...DEFAULT},drag=null,mounted=false;
 try{
   const old=JSON.parse(localStorage.getItem(KEY)||"null");
   if(old&&typeof old==="object")size={
     left:valid(old.left)||DEFAULT.left,
     right:valid(old.right)||DEFAULT.right,
     bottom:valid(old.bottom)||DEFAULT.bottom
   };
 }catch{}
 const desktop=()=>window.matchMedia("(min-width:951px)").matches;
 const clamp=(v,min,max)=>Math.max(min,Math.min(max,v));
 const shell=()=>$("editorWorkspace");
 function bounds(){
   const el=shell();
   const rect=el.getBoundingClientRect();
   const w=Math.max(600,rect.width),h=Math.max(420,rect.height);
   // Reserve at least 285px for the center video canvas.
   const middleMin=Math.min(350,Math.max(285,w*.3));
   const leftMax=Math.min(315,Math.max(120,w-280-middleMin));
   const rightMax=Math.min(510,Math.max(275,w-120-middleMin));
   return {rect,w,h,middleMin,leftMax,rightMax,
     bottomMax:Math.max(185,Math.min(465,h-290))};
 }
 function normalize(data){
   const b=bounds();
   const left=clamp(valid(data.left)||DEFAULT.left,120,b.leftMax);
   const right=clamp(valid(data.right)||DEFAULT.right,275,Math.min(b.rightMax,b.w-left-b.middleMin));
   const safeLeft=clamp(left,120,Math.max(120,b.w-right-b.middleMin));
   const bottom=clamp(valid(data.bottom)||DEFAULT.bottom,185,b.bottomMax);
   return {left:Math.round(safeLeft),right:Math.round(right),bottom:Math.round(bottom)};
 }
 function paint(data){
   size=normalize(data);
   const el=shell();
   el.style.setProperty("--dock-left-w",size.left+"px");
   el.style.setProperty("--dock-right-w",size.right+"px");
   el.style.setProperty("--dock-bottom-h",size.bottom+"px");
   for(const [id,value,low,high] of [
     ["dockResizeLeft",size.left,120,bounds().leftMax],
     ["dockResizeRight",size.right,275,bounds().rightMax],
     ["dockResizeBottom",size.bottom,185,bounds().bottomMax]
   ]){
     const node=$(id);
     node.setAttribute("aria-valuenow",String(value));
     node.setAttribute("aria-valuemin",String(Math.round(low)));
     node.setAttribute("aria-valuemax",String(Math.round(high)));
     node.setAttribute("aria-valuetext",value+" pixels");
   }
 }
 function save(){try{localStorage.setItem(KEY,JSON.stringify(size));}catch{}}
 function reset(){paint(DEFAULT);save();}
 function dragValue(kind,e){
   const b=bounds();
   if(kind==="left")return e.clientX-b.rect.left;
   if(kind==="right")return b.rect.right-e.clientX;
   return b.rect.bottom-e.clientY;
 }
 function onMove(e){
   if(!drag)return;
   const next={...size,[drag.kind]:dragValue(drag.kind,e)};
   paint(next);
   e.preventDefault();
 }
 function finish(e){
   if(!drag)return;
   try{drag.node.releasePointerCapture?.(e.pointerId);}catch{}
   drag=null;
   document.body.classList.remove("dock-resizing");
   save();
 }
 function bind(id,kind){
   const node=$(id);
   node.addEventListener("pointerdown",e=>{
     if(!desktop()||e.button!==0)return;
     e.preventDefault();
     drag={node,kind};
     document.body.classList.add("dock-resizing");
     try{node.setPointerCapture(e.pointerId);}catch{}
   });
   node.addEventListener("pointermove",onMove);
   node.addEventListener("pointerup",finish);
   node.addEventListener("pointercancel",finish);
   node.addEventListener("lostpointercapture",()=>{if(drag){drag=null;save();document.body.classList.remove("dock-resizing");}});
   node.addEventListener("keydown",e=>{
     if(!desktop())return;
     let delta=0;
     if(kind==="bottom"){
       if(e.key==="ArrowUp")delta=12;
       else if(e.key==="ArrowDown")delta=-12;
     }else{
       if(e.key==="ArrowRight")delta=kind==="right"?-12:12;
       else if(e.key==="ArrowLeft")delta=kind==="right"?12:-12;
     }
     if(e.shiftKey)delta*=3;
     if(e.key==="Home"){e.preventDefault();reset();return;}
     if(!delta)return;
     e.preventDefault();
     paint({...size,[kind]:size[kind]+delta});
     save();
   });
   node.addEventListener("dblclick",reset);
 }
 function mount(){
   if(mounted)return;
   mounted=true;
   bind("dockResizeLeft","left");
   bind("dockResizeRight","right");
   bind("dockResizeBottom","bottom");
   $("resetDockBtn").addEventListener("click",reset);
   $("dockInspectorEdit").addEventListener("click",()=>
     window.FocusFlashEditor?.selectTab?.("script",true));
   window.addEventListener("resize",()=>{if(desktop())paint(size);});
   paint(size);
 }
 window.FocusFlashDock={mount,reset,getLayout:()=>({...size}),storageKey:KEY};
})();