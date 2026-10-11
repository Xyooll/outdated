/* FocusFlash local workspace profiles — two isolated, durable browser states.
 * Each profile owns scripts, reading position, blocks, voice, tone settings,
 * and a separate audio-file record in IndexedDB (managed by sound mixer).
 * This is NOT sign-in or cross-device sync. Clearing browser data erases it.
 */
(() => {
 "use strict";
 const CONFIG_KEY="focusflash-profiles-v1";
 const DEFAULT_NAMES=["User 1","User 2"];
 const OLD_KEYS=["focusflash-state-v1","focusflash-script-blocks-v1",
                 "focusflash-video-v1","focusflash-tones-v1"];
 let config={active:"1",names:[...DEFAULT_NAMES]};
 try{
   const existing=JSON.parse(localStorage.getItem(CONFIG_KEY)||"null");
   if(existing&&typeof existing==="object"){
     config.active=existing.active==="2"?"2":"1";
     if(Array.isArray(existing.names))
       config.names=DEFAULT_NAMES.map((d,i)=>typeof existing.names[i]==="string"?
         (existing.names[i].trim().slice(0,28)||d):d);
   }
 }catch{}
 const key=(base,id=config.active)=>"focusflash-profile-"+id+"-"+base;
 const save=()=>{try{localStorage.setItem(CONFIG_KEY,JSON.stringify(config));return true}catch{return false}};
 // Non-destructive migration: copy existing single-user data to User 1
 // without deleting old keys and without replacing newer profile data.
 for(const base of OLD_KEYS){
   try{
     const old=localStorage.getItem(base),scoped=localStorage.getItem(key(base,"1"));
     if(old!==null&&scoped===null)localStorage.setItem(key(base,"1"),old);
   }catch{}
 }
 save();

 function updateUI(){
   const $=id=>document.getElementById(id);
   const label=config.names[Number(config.active)-1];
   const select=$("profileSwitch");
   if(select){
     for(let i=0;i<2;i++)select.options[i].textContent=config.names[i];
     select.value=config.active;
   }
   for(let i=1;i<=2;i++){
     const n=$("profileName"+i),button=$("profileChoose"+i);
     if(n&&document.activeElement!==n)n.value=config.names[i-1];
     if(button){
       button.textContent=i===Number(config.active)?"✓ Using this workspace":"Switch to "+config.names[i-1];
       button.disabled=i===Number(config.active);
     }
     const card=$("profileCard"+i);
     card?.classList.toggle("selected",i===Number(config.active));
   }
   if($("profileAvatar"))$("profileAvatar").textContent=config.active;
   if($("profileBadge"))$("profileBadge").textContent=label+"’s studio";
   if($("profileSummary"))$("profileSummary").textContent=label+" · saved on this device";
 }
 function announce(message){
   const n=document.getElementById("profileStatus");
   if(n)n.textContent=message;
 }
 function setName(index,value){
   const id=Number(index);
   if(id!==1&&id!==2)return;
   config.names[id-1]=String(value||"").trim().slice(0,28)||DEFAULT_NAMES[id-1];
   const ok=save();
   updateUI();
   announce(ok?"Name updated and saved on this device.":"Cannot save profile names; check browser storage.");
 }
 function choose(id){
   const target=String(id);
   if(target!=="1"&&target!=="2")return false;
   if(target===config.active)return true;
   if(window.FocusFlashStudio?.isBusy?.()){
     announce("Finish or cancel video rendering before switching users.");
     updateUI();
     return false;
   }
   // Flush pending block edits and position BEFORE selecting the new owner.
   window.FocusFlashBlocks?.flush?.();
   window.FocusFlashReader?.persist?.();
   window.FocusFlashReader?.pause?.();
   window.FocusFlashTones?.stopReader?.();
   window.FocusFlashTones?.stopTest?.();
   const previous=config.active;
   config.active=target;
   if(!save()){
     config.active=previous;updateUI();
     announce("Unable to switch: local browser storage is blocked.");
     return false;
   }
   // Reload is deliberate: all modules initialize under the active namespace.
   // It also stops active microphones, TTS and Web Audio safely.
   window.location.reload();
   return true;
 }
 function mount(){
   const $=id=>document.getElementById(id);
   // New User 2 starts with an empty draft, not User 1's example text.
   if(config.active==="2"&&!localStorage.getItem(key("focusflash-state-v1"))){
     const field=$("sourceText");if(field)field.value="";
   }
   $("profileSwitch")?.addEventListener("change",e=>choose(e.target.value));
   for(let i=1;i<=2;i++){
     $("profileChoose"+i)?.addEventListener("click",()=>choose(i));
     $("profileName"+i)?.addEventListener("change",e=>setName(i,e.target.value));
   }
   $("profileEditBtn")?.addEventListener("click",()=>window.FocusFlashEditor?.selectTab?.("profiles",true));
   updateUI();
   announce("Each user has an independent saved workspace in this browser. No account or cloud sync is enabled.");
 }
 window.FocusFlashProfiles={
   key,id:()=>config.active,name:()=>config.names[Number(config.active)-1],
   mount,switchTo:choose,rename:setName
 };
})();