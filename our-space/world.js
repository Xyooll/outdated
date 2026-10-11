
import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.117.3/+esm";
import { URL as PROJECT_URL, KEY as PUBLISHABLE_KEY } from "./config.js?v=assets-v2";
import { drawWorld, drawAvatar, WORLD_META } from "./world-art.js?v=assets-v2";
import { drawHouse, findHousePath, clearTile, ACTIONS, objectAt } from "./life-house.js?v=assets-v2";
import {paintHouseDetails,paintInteractiveHighlights,paintActivityEffects} from "./life-assets.js?v=assets-v2";
import { createLifeUI } from "./life-ui.js?v=assets-v2";

const $ = id => document.getElementById(id);
const valid = /^https:\/\/[a-z0-9-]+\.supabase\.co\/?$/i.test(PROJECT_URL)
  && (PUBLISHABLE_KEY.startsWith("sb_publishable_") || PUBLISHABLE_KEY.length > 100);
const db = valid ? createClient(PROJECT_URL,PUBLISHABLE_KEY,{
  auth:{persistSession:true,autoRefreshToken:true,detectSessionInUrl:true}
}) : null;
const VIEW_IDS=["loadingView","loginView","recoverView","worldView"];
const FIELDS={avatarName:"display_name",skin:"skin",hairStyle:"hair_style",
 hairColor:"hair_color",shirt:"shirt",bottoms:"bottoms",accessory:"accessory"};
const ctx=$("worldCanvas").getContext("2d");
const preview=$("avatarCanvas").getContext("2d");
let me=null,myAvatar=null,avatars=[],rooms={},world="home";
let chatChannel=null,avatarChannel=null,loadStamp=0,messageStamp=0;
let lastFrame=0,lastWrite=0,writeBusy=false,dirty=false,positionTarget=null;
let inputDirection=new Set(),timer=null,appReady=false,recovery=false,starting=null,waypoints=[],arrival=null;
let emoted={},outfitPending=false,sessionGeneration=0,hoveredId=null;
function panelState(which,showIt){
 const panel=$(which+"Panel"),button=$(which+"Btn");
 if(!panel||!button)return;
 panel.classList.toggle("hidden",!showIt);
 button.setAttribute("aria-expanded",String(showIt));
 if(which==="chat"&&showIt){
  $("chatBadge").classList.add("hidden");
  $("chatMessages").scrollTop=$("chatMessages").scrollHeight;
 }
}
function closePanels(){
 for(const name of ["chat","tasks","places"])panelState(name,false);
}
function togglePanel(name){
 const showIt=$(name+"Panel").classList.contains("hidden");
 closePanels();
 if(showIt)panelState(name,true);
}
const life=createLifeUI({db,getUser:()=>me,getAvatar:()=>myAvatar,
 getAvatars:()=>avatars,goTo:walkTo,savePosition:ensureSavedPosition});
const NUM=v=>Number.isFinite(+v)?Number(v):0;
const clamp=(n,min,max)=>Math.max(min,Math.min(max,n));
function message(id,text){$(id).textContent=text||"";}
function show(id){
 if(id!=="worldView")closePanels();
 for(const view of VIEW_IDS)$(view).classList.toggle("hidden",view!==id);
 $("signoutBtn").classList.toggle("hidden",id!=="worldView");
}
function err(e){return e?.message||"Something went wrong. Please try again.";}
function setStatus(s){$("networkState").textContent=s||"Private worlds";}
function ensureAuthenticated(){if(!me||!myAvatar)throw Error("Please sign in again.");}
function avatarById(id){return avatars.find(a=>a.user_id===id);}
function worldRow(){return rooms[WORLD_META[world].dbRoom];}
function localizeTime(ts){return new Date(ts).toLocaleTimeString([],{hour:"numeric",minute:"2-digit"});}
function currentWorld(){return WORLD_META[world];}
function updateWorldHead(){
 const info=currentWorld();
 $("worldTitle").textContent=info.title;
 $("worldEyebrow").textContent=info.eyebrow;
 $("worldDescription").textContent=info.subtitle;
 $("chatHeading").textContent=info.chat;
 for(const tab of document.querySelectorAll("[data-world]"))tab.classList.toggle("active",tab.dataset.world===world);
}
function online(a){return Date.now()-new Date(a.updated_at).getTime()<85000;}
function updateWorldPeople(){
 const people=avatars.filter(a=>a.world_id===world&&online(a));
 const amount=people.length;
 $("worldPeople").textContent="● "+(amount===2?"Both here ♥":amount===1?"1 here":"Quiet for now");
}
function safeLook(obj){
 return {
 user_id:obj.user_id,
 display_name:String(obj.display_name||"Player").slice(0,24),
 skin:obj.skin||"warm",hair_style:obj.hair_style||"short",
 hair_color:obj.hair_color||"chocolate",shirt:obj.shirt||"pink",
 bottoms:obj.bottoms||"denim",accessory:obj.accessory||"none",
 world_id:obj.world_id||"home",x:clamp(NUM(obj.x)||450,25,935),
 y:clamp(NUM(obj.y)||345,125,485),updated_at:obj.updated_at||new Date().toISOString()
 };
}
async function enter(){
 if(starting)return starting;
 starting=doEnter();
 try{return await starting;}finally{starting=null;}
}
async function doEnter(){
 if(!db){show("loginView");message("loginStatus","Database setup is missing.");return;}
 const thisStart=++sessionGeneration;
 try{
  const response=await db.auth.getUser();
  if(response.error||!response.data.user){me=null;myAvatar=null;appReady=false;show("loginView");
   if(response.error&&response.error.name!=="AuthSessionMissingError")message("loginStatus","Could not restore sign-in: "+err(response.error));
   return;
  }
  if(recovery){show("recoverView");return;}
  if(appReady&&me?.id===response.data.user.id)return;
  me=response.data.user;
  const member=await db.from("couple_members").select("role").eq("user_id",me.id).maybeSingle();
  if(member.error)throw member.error;
  if(!member.data){show("loginView");message("loginStatus","This account is not one of the two approved members.");return;}
  const [roomRes,profileRes]=await Promise.all([
    db.from("chat_rooms").select("id,name").order("created_at",{ascending:true}),
    db.from("world_avatars").select("*")
  ]);
  if(roomRes.error)throw roomRes.error;
  if(profileRes.error)throw profileRes.error;
  rooms=Object.fromEntries(roomRes.data.map(x=>[x.name,x]));
  for(const meta of Object.values(WORLD_META)){
    if(!rooms[meta.dbRoom])throw Error("Missing chat room "+meta.dbRoom+". Check database setup.");
  }
  avatars=(profileRes.data||[]).map(safeLook);
  myAvatar=avatarById(me.id);
  if(!myAvatar){
    const newProfile={user_id:me.id,display_name:"Player",world_id:"home",x:450,y:345};
    const saved=await db.from("world_avatars").insert(newProfile).select().single();
    if(saved.error)throw saved.error;
    myAvatar=safeLook(saved.data);
    avatars.push(myAvatar);
  }
  if(thisStart!==sessionGeneration)return;
  world=WORLD_META[myAvatar.world_id]?myAvatar.world_id:"home";
  // Avatars from the old free-roaming Cottage might have been left inside new furniture.
  if(world==="home"&&!clearTile(myAvatar.x,myAvatar.y)){
    myAvatar.x=450;myAvatar.y=350;dirty=true;
  }
  appReady=true;
  setStatus("● Connected");
  updateWorldHead();
  show("worldView");
  connectAvatarChannel();
  if(dirty)await ensureSavedPosition();
  await changeRoomChat();
  await life.start();
  await life.onChangeWorld(world);
  updateWorldPeople();
  if(timer)clearInterval(timer);
  timer=setInterval(()=>{if(appReady&&me){
    // Heartbeat only: presence is inferred from recent authenticated profile updates.
    flushPosition(true).catch(e=>setStatus("Reconnecting…"));
    if(document.visibilityState==="visible")loadMessages(true).catch(()=>{});
  }},24000);
  if(!lastFrame)requestAnimationFrame(frame);
 }catch(e){
  appReady=false;show("loginView");
  message("loginStatus","Could not enter your world: "+err(e));
 }
}
async function refreshProfiles(){
 if(!appReady||!me)return;
 const res=await db.from("world_avatars").select("*");
 if(res.error){setStatus("Reconnecting…");return;}
 for(const remote of res.data){
  if(remote.user_id===me.id)continue; // never override local animation
  const a=safeLook(remote),idx=avatars.findIndex(x=>x.user_id===a.user_id);
  if(idx>=0)avatars[idx]=a;else avatars.push(a);
 }
 updateWorldPeople();
}
function connectAvatarChannel(){
 if(avatarChannel)db.removeChannel(avatarChannel);
 avatarChannel=db.channel("our-space-avatar-updates")
  .on("postgres_changes",{event:"*",schema:"public",table:"world_avatars"},payload=>{
   const updated=payload.new;
   if(!updated?.user_id || updated.user_id===me?.id)return;
   const a=safeLook(updated),idx=avatars.findIndex(x=>x.user_id===a.user_id);
   if(idx>=0)avatars[idx]=a;else avatars.push(a);
   updateWorldPeople();
  })
  .subscribe(state=>{if(state==="CHANNEL_ERROR"||state==="TIMED_OUT")setStatus("Reconnecting…");else if(state==="SUBSCRIBED")setStatus("● Connected");});
}
async function flushPosition(force=false){
 if(!db||!appReady||!myAvatar||writeBusy)return;
 if(!dirty&&!force)return;
 writeBusy=true;
 const snapshot={world_id:world,x:Math.round(myAvatar.x),y:Math.round(myAvatar.y),updated_at:new Date().toISOString()};
 dirty=false;
 try{
  const result=await db.from("world_avatars").update(snapshot).eq("user_id",me.id);
  if(result.error)throw result.error;
  lastWrite=performance.now();
  myAvatar.updated_at=snapshot.updated_at;
  updateWorldPeople();
 }catch(e){dirty=true;message("chatStatus","Position was not saved: "+err(e));}
 finally{writeBusy=false;}
}
async function changeWorld(next){
 if(!WORLD_META[next]||!me||next===world)return;
 closePanels();
 if(life.active){message("lifeStatus","Finish or cancel your activity before changing worlds.");return;}
 positionTarget=null;waypoints=[];arrival=null;hoveredId=null;inputDirection.clear();
 world=next;myAvatar.world_id=next;
 myAvatar.x=450;myAvatar.y=350;
 dirty=true;
 updateWorldHead();
 updateWorldPeople();
 message("chatStatus","");
 await flushPosition(true);
 await changeRoomChat();
 await life.onChangeWorld(world);
}
async function changeRoomChat(){
 if(chatChannel)await db.removeChannel(chatChannel);
 chatChannel=null;
 const room=worldRow();
 if(!room){message("chatStatus","The chat room is unavailable.");return;}
 await loadMessages();
 chatChannel=db.channel("our-space-messages-"+room.id)
 .on("postgres_changes",{event:"INSERT",schema:"public",table:"chat_room_messages",filter:"room_id=eq."+room.id},p=>{
  if(worldRow()?.id!==room.id)return;
  if($("chatPanel").classList.contains("hidden") && p.new?.sender_id!==me?.id)
   $("chatBadge").classList.remove("hidden");
  const id=p.new?.sender_id;
  if(id&&p.new?.body)emoted[id]={text:String(p.new.body).slice(0,30),until:Date.now()+4500};
  loadMessages().catch(()=>{});
 }).subscribe();
}
async function loadMessages(silent=false){
 if(!appReady||!me)return;
 const room=worldRow();
 if(!room)return;
 const stamp=++messageStamp;
 const result=await db.from("chat_room_messages")
  .select("id,room_id,sender_id,body,created_at")
  .eq("room_id",room.id).order("created_at",{ascending:false}).limit(120);
 if(result.error){if(!silent)message("chatStatus",err(result.error));return;}
 if(stamp!==messageStamp||room.id!==worldRow()?.id)return;
 const list=$("chatMessages");
 const atBottom=list.scrollHeight-list.scrollTop-list.clientHeight<80;
 const frag=document.createDocumentFragment();
 if(!result.data.length){
  const node=document.createElement("div");node.className="empty-chat";
  const heart=document.createElement("strong");heart.textContent="♥";
  const text=document.createElement("div");text.textContent="Your first message starts the story here.";
  node.append(heart,text);frag.append(node);
 }
 for(const entry of result.data.reverse()){
  const mine=entry.sender_id===me.id, avatar=avatarById(entry.sender_id);
  const el=document.createElement("article");el.className="msg"+(mine?" my":"");
  const icon=document.createElement("span");icon.className="tinyavatar";icon.textContent=avatar?.accessory==="crown"?"👑":"♥";
  const col=document.createElement("div");col.className="msg-content";
  const head=document.createElement("div");head.className="msg-head";
  const name=document.createElement("strong");name.textContent=mine?"You":avatar?.display_name||"Your person";
  const time=document.createElement("time");time.dateTime=entry.created_at;time.textContent=localizeTime(entry.created_at);
  const bubble=document.createElement("div");bubble.className="bubble";bubble.textContent=entry.body;
  head.append(name,time);col.append(head,bubble);el.append(icon,col);frag.append(el);
 }
 list.replaceChildren(frag);
 if(atBottom||!list.dataset.loaded)list.scrollTop=list.scrollHeight;
 list.dataset.loaded="yes";
}
async function sendMessage(e){
 e.preventDefault();
 if(!me||!appReady)return;
 const text=$("message").value.trim(), room=worldRow();
 if(!text||!room)return;
 const btn=$("sendBtn");btn.disabled=true;
 message("chatStatus","");
 try{
  const result=await db.from("chat_room_messages").insert({room_id:room.id,sender_id:me.id,body:text});
  if(result.error)throw result.error;
  $("message").value="";
  emoted[me.id]={text:text.slice(0,30),until:Date.now()+4500};
  await loadMessages();
  $("chatMessages").scrollTop=$("chatMessages").scrollHeight;
 }catch(error){message("chatStatus","Not sent: "+err(error));}
 finally{btn.disabled=false;}
}

function walkTo(x,y,callback=null){
 if(!appReady||!myAvatar)return false;
 if(life.active){
  message("lifeStatus","Finish or cancel the current action before moving.");
  return false;
 }
 if(world!=="home"){positionTarget={x:clamp(x,26,934),y:clamp(y,125,484)};return true;}
 const route=findHousePath(myAvatar.x,myAvatar.y,x,y);
 if(!route.length)return false;
 waypoints=route;arrival=callback;positionTarget=null;
 return true;
}
function moveTo(x,y){if(!appReady)return;life.closeMenu();walkTo(x,y);}
async function ensureSavedPosition(){
 for(let i=0;i<10;i++){
  if(writeBusy){await new Promise(r=>setTimeout(r,125));continue;}
  await flushPosition(true);
  if(!writeBusy&&!dirty)return;
 }
 throw Error("Position has not synchronized; retry the activity.");
}
function worldPoint(e){
 const rect=$("worldCanvas").getBoundingClientRect();
 return {x:(e.clientX-rect.left)*960/rect.width,y:(e.clientY-rect.top)*540/rect.height};
}
function moveAvatar(delta){
 if(!myAvatar||!appReady)return;
 if(life.active){
  waypoints=[];arrival=null;positionTarget=null;
  inputDirection.clear();
  return;
 }
 const d=Math.min(delta,0.06);
 let dx=0,dy=0;
 for(const dir of inputDirection){
  if(dir==="up")dy-=1;if(dir==="down")dy+=1;
  if(dir==="left")dx-=1;if(dir==="right")dx+=1;
 }
 const speed=185*d*(world==="home"?life.getSpeed():1);
 if(world==="home"){
  if(dx||dy){
   waypoints=[];arrival=null;positionTarget=null;
   const l=Math.hypot(dx,dy);
   const nx=clamp(myAvatar.x+dx/l*speed,26,934);
   const ny=clamp(myAvatar.y+dy/l*speed,125,485);
   if(clearTile(nx,myAvatar.y)){myAvatar.x=nx;dirty=true;}
   if(clearTile(myAvatar.x,ny)){myAvatar.y=ny;dirty=true;}
  }else if(waypoints.length){
   const target=waypoints[0],vx=target[0]-myAvatar.x,vy=target[1]-myAvatar.y;
   const dist=Math.hypot(vx,vy);
   if(dist<=speed+1){
    myAvatar.x=target[0];myAvatar.y=target[1];waypoints.shift();dirty=true;
    if(!waypoints.length && arrival){
     const callback=arrival;arrival=null;
     Promise.resolve().then(callback).catch(e=>message("lifeStatus",err(e)));
    }
   }else{
    const nx=myAvatar.x+vx/dist*speed,ny=myAvatar.y+vy/dist*speed;
    if(clearTile(nx,ny)){myAvatar.x=nx;myAvatar.y=ny;dirty=true;}
    else{waypoints=[];arrival=null;message("lifeStatus","Path blocked. Tap another spot.");}
   }
  }
 }else{
  if(dx||dy){
   const l=Math.hypot(dx,dy);
   myAvatar.x=clamp(myAvatar.x+dx/l*speed,26,934);
   myAvatar.y=clamp(myAvatar.y+dy/l*speed,125,484);
   positionTarget=null;dirty=true;
  }else if(positionTarget){
   const vx=positionTarget.x-myAvatar.x,vy=positionTarget.y-myAvatar.y;
   const dist=Math.hypot(vx,vy);
   if(dist<=speed){myAvatar.x=positionTarget.x;myAvatar.y=positionTarget.y;positionTarget=null;dirty=true;}
   else{myAvatar.x+=vx/dist*speed;myAvatar.y+=vy/dist*speed;dirty=true;}
  }
 }
 if(dirty&&performance.now()-lastWrite>1100)flushPosition().catch(()=>{});
}
function drawPreview(){
 if(!myAvatar)return;
 const look={...myAvatar};
 for(const [id,column] of Object.entries(FIELDS)){const el=$(id);if(el)look[column]=el.value||look[column];}
 preview.clearRect(0,0,200,240);
 preview.fillStyle="#ffffff0c";preview.fillRect(0,0,200,240);
 drawAvatar(preview,look,100,202,{label:false,scale:2.05});
}
function frame(ts){
 const dt=lastFrame?Math.min(.05,(ts-lastFrame)/1000):0;
 lastFrame=ts;
 if(appReady&&myAvatar){
  moveAvatar(dt);
  if(world==="home"){
    drawHouse(ctx,ts/1000);
    paintHouseDetails(ctx,ts/1000);
    const v=life.visual();
    paintInteractiveHighlights(ctx,ts/1000,hoveredId,v.selected,waypoints);
  }else drawWorld(ctx,world,ts/1000);
  const visible=avatars.filter(a=>a.world_id===world).sort((a,b)=>a.y-b.y);
  for(const a of visible){
   const you=a.user_id===me.id, active=you||online(a);
   const bubble=emoted[a.user_id]&&emoted[a.user_id].until>Date.now()?emoted[a.user_id].text:null;
   const activity=life.getActionFor(a.user_id);
   const actionText=activity?ACTIONS[activity]?.emoji+" "+ACTIONS[activity]?.label:null;
   const moving=you&&(waypoints.length>0||inputDirection.size>0||!!positionTarget);
   const y=a.y+(active?Math.sin(ts/550+a.x)*1.2:0);
   drawAvatar(ctx,a,a.x,y,{online:active,offline:!active,emote:bubble||actionText,
    scale:1.38,walking:moving,clock:ts/1000,activity});
  }
  if(world==="home"){
    const v=life.visual();
    paintActivityEffects(ctx,ts/1000,v.activities,avatars,v.celebration);
  }
  if(!$("closet").classList.contains("hidden"))drawPreview();
  life.animate();
 }
 requestAnimationFrame(frame);
}
function showCloset(){
 if(!myAvatar)return;
 closePanels();
 life.onShowWardrobe();
 for(const [id,col] of Object.entries(FIELDS))$(id).value=myAvatar[col]||"";
 $("closet").classList.remove("hidden");$("avatarName").focus();
 drawPreview();
}
function closeCloset(){$("closet").classList.add("hidden");}
async function saveOutfit(e){
 e.preventDefault();
 if(!me||!myAvatar||outfitPending)return;
 const values={};for(const [id,column] of Object.entries(FIELDS))values[column]=$(id).value.trim();
 if(!values.display_name){message("outfitStatus","Please choose a name.");return;}
 outfitPending=true;$("saveOutfit").disabled=true;
 message("outfitStatus","");
 try{
  const update={...values,updated_at:new Date().toISOString()};
  const result=await db.from("world_avatars").update(update).eq("user_id",me.id).select().single();
  if(result.error)throw result.error;
  Object.assign(myAvatar,safeLook({...myAvatar,...result.data}));
  message("outfitStatus","Saved! Your person can see your new look.");
  updateWorldPeople();
 }catch(error){message("outfitStatus","Could not save: "+err(error));}
 finally{outfitPending=false;$("saveOutfit").disabled=false;}
}
async function signOut(){
 sessionGeneration++;appReady=false;positionTarget=null;waypoints=[];arrival=null;inputDirection.clear();life.stop();
 if(timer)clearInterval(timer);timer=null;
 if(avatarChannel)await db.removeChannel(avatarChannel);
 if(chatChannel)await db.removeChannel(chatChannel);
 avatarChannel=null;chatChannel=null;
 await db.auth.signOut();
 me=null;myAvatar=null;avatars=[];rooms={};recovery=false;
 setStatus("Private worlds");show("loginView");
}
$("loginForm").addEventListener("submit",async e=>{
 e.preventDefault();if(!db)return;
 $("loginBtn").disabled=true;message("loginStatus","");
 try{
  const email=$("email").value.trim(),password=$("password").value;
  const res=await db.auth.signInWithPassword({email,password});
  if(res.error)throw res.error;
  $("password").value="";
  await enter();
 }catch(error){message("loginStatus",err(error));}
 finally{$("password").value="";$("loginBtn").disabled=false;}
});
$("forgotBtn").addEventListener("click",async()=>{
 if(!db)return;
 const email=$("email");
 if(!email.value.trim()||!email.checkValidity()){email.reportValidity();return;}
 $("forgotBtn").disabled=true;message("loginStatus","");
 try{
  const res=await db.auth.resetPasswordForEmail(email.value.trim(),{redirectTo:location.origin+location.pathname});
  if(res.error)throw res.error;
  message("loginStatus","Check your email. Open the newest recovery link once in Chrome. Email limits may apply.");
 }catch(e){message("loginStatus",err(e));}
 finally{$("forgotBtn").disabled=false;}
});
$("recoverForm").addEventListener("submit",async e=>{
 e.preventDefault();
 const pw=$("newPassword").value;
 if(pw.length<12||pw!==$("newPasswordAgain").value){
  message("recoverStatus","Enter the same password of at least 12 characters twice.");return;
 }
 $("recoverBtn").disabled=true;
 try{
  const res=await db.auth.updateUser({password:pw});
  if(res.error)throw res.error;
  recovery=false;history.replaceState(null,"",location.pathname);
  $("newPassword").value="";$("newPasswordAgain").value="";
  await enter();
 }catch(e){message("recoverStatus",err(e));}
 finally{$("recoverBtn").disabled=false;}
});
$("sendForm").addEventListener("submit",sendMessage);
$("signoutBtn").addEventListener("click",signOut);
$("closetBtn").addEventListener("click",showCloset);
$("closetClose").addEventListener("click",closeCloset);
$("closetShade").addEventListener("click",closeCloset);
$("outfitForm").addEventListener("submit",saveOutfit);
for(const name of ["chat","tasks","places"])
 $(name+"Btn").addEventListener("click",()=>togglePanel(name));
$("chatClose").addEventListener("click",()=>panelState("chat",false));
$("tasksClose").addEventListener("click",()=>panelState("tasks",false));
for(const shade of document.querySelectorAll("[data-panel-close]"))
 shade.addEventListener("click",()=>panelState(shade.dataset.panelClose,false));
for(const id of Object.keys(FIELDS))$(id).addEventListener("input",drawPreview);
for(const tab of document.querySelectorAll("[data-world]"))
 tab.addEventListener("click",()=>changeWorld(tab.dataset.world).catch(e=>message("chatStatus",err(e))));
$("worldCanvas").addEventListener("pointerdown",e=>{
 e.preventDefault();
 if(life.active){
  message("lifeStatus","Action in progress. Wait for it to finish or tap Cancel.");
  return;
 }
 const point=worldPoint(e);
 hoveredId=null;
 if(world!=="home"||!life.interactAt(point.x,point.y))moveTo(point.x,point.y);
 $("worldCanvas").focus();
});
$("worldCanvas").addEventListener("pointermove",e=>{
 if(e.pointerType!=="mouse"||!appReady||world!=="home"){hoveredId=null;return;}
 const pt=worldPoint(e);
 const furniture=objectAt(pt.x,pt.y);
 hoveredId=furniture?.id||null;
 $("worldCanvas").style.cursor=hoveredId?"pointer":"crosshair";
});
$("worldCanvas").addEventListener("pointerleave",()=>{hoveredId=null;});
for(const control of document.querySelectorAll("[data-move]")){
 const dir=control.dataset.move;
 control.addEventListener("pointerdown",e=>{e.preventDefault();control.setPointerCapture(e.pointerId);inputDirection.add(dir);});
 for(const type of ["pointerup","pointercancel","lostpointercapture"])
  control.addEventListener(type,()=>{inputDirection.delete(dir);if(dirty)flushPosition().catch(()=>{});});
}
document.addEventListener("keydown",e=>{
 if(e.target.closest("input,textarea,select"))return;
 const map={ArrowUp:"up",ArrowDown:"down",ArrowLeft:"left",ArrowRight:"right",
  w:"up",s:"down",a:"left",d:"right"};
 const direction=map[e.key]||map[e.key.toLowerCase()];
 if(direction&&appReady){e.preventDefault();inputDirection.add(direction);}
 if(e.key==="Escape"){closeCloset();closePanels();}
});
document.addEventListener("keyup",e=>{
 const map={ArrowUp:"up",ArrowDown:"down",ArrowLeft:"left",ArrowRight:"right",w:"up",s:"down",a:"left",d:"right"};
 const direction=map[e.key]||map[e.key.toLowerCase()];
 if(direction){inputDirection.delete(direction);if(dirty)flushPosition().catch(()=>{});}
});
window.addEventListener("blur",()=>{inputDirection.clear();if(dirty)flushPosition().catch(()=>{});});
window.addEventListener("online",()=>{if(appReady){refreshProfiles().catch(()=>{});loadMessages().catch(()=>{});flushPosition(true).catch(()=>{});}});
document.addEventListener("visibilitychange",()=>{
 if(document.visibilityState==="visible"&&appReady){refreshProfiles().catch(()=>{});loadMessages(true).catch(()=>{});flushPosition(true).catch(()=>{});}
});
const params=new URLSearchParams(location.search);
const hashParams=new URLSearchParams(location.hash.replace(/^#/,""));
const authError=params.get("error_description")||hashParams.get("error_description");
if(authError){
 message("loginStatus","Sign-in link could not be used: "+authError.replace(/\+/g," "));
 if(!location.hash.includes("access_token"))history.replaceState(null,"",location.pathname);
}
if(db){
 db.auth.onAuthStateChange((event)=>{
  if(event==="PASSWORD_RECOVERY"){recovery=true;setTimeout(()=>show("recoverView"),0);}
  else if(event==="SIGNED_OUT"){
   appReady=false;life.stop();avatars=[];me=null;myAvatar=null;
   setTimeout(()=>show("loginView"),0);
  }
  else if(event==="SIGNED_IN"&&!recovery){setTimeout(()=>enter(),0);}
 });
 enter();
}else{show("loginView");message("loginStatus","Our Space is not connected to its database yet.");}
if("serviceWorker"in navigator){
 navigator.serviceWorker.register("./sw.js")
  .then(reg=>reg.update())
  .catch(()=>{});
}
