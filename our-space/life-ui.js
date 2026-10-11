
import {OBJECTS,ACTIONS,TASKS,NEEDS} from "./life-house.js?v=life-layout-2";
const $=id=>document.getElementById(id);
const numeric=n=>Math.max(0,Math.min(100,Number(n)||0));
const explain=e=>e?.message||"Connection issue — please try again.";
const today=()=>new Date().toISOString().slice(0,10);
export function createLifeUI({db,getUser,getAvatar,getAvatars,goTo,savePosition}){
 let needs=null,tasks=[],active=null,home=true,running=false,activityChannel=null,otherActivities=new Map();
 let tickTimer=null,finishing=false,completeAttempt=0,lastTasks=0;
 const actionBox=$("lifeActions"),progress=$("lifeProgress");
 const status=(s)=>{$("lifeStatus").textContent=s||"";};
 const onHome=()=>getAvatar()?.world_id==="home";
 function renderNeeds(){
  const host=$("lifeNeeds");host.replaceChildren();
  if(!needs){host.textContent="Loading household needs…";return;}
  for(const meta of NEEDS){
   const item=document.createElement("div");item.className="need";
   const top=document.createElement("div");top.className="need-heading";
   const label=document.createElement("span");label.textContent=meta.emoji+" "+meta.label;
   const percent=document.createElement("span");percent.textContent=Math.round(numeric(needs[meta.key]))+"%";
   top.append(label,percent);
   const outer=document.createElement("div");outer.className="need-track";
   const bar=document.createElement("div");bar.className="need-fill";
   const value=numeric(needs[meta.key]);
   bar.style.width=value+"%";
   bar.dataset.level=value<25?"low":value<48?"medium":"good";
   outer.append(bar);item.append(top,outer);host.append(item);
  }
  $("lifeMealCount").textContent="🍲 "+Number(needs.meals||0)+" prepared meal"+(Number(needs.meals||0)===1?"":"s");
 }
 function renderTasks(){
  const list=$("lifeTasks");list.replaceChildren();
  const map=new Map(tasks.filter(x=>x.day===today()).map(t=>[t.task_key,t]));
  const complete=[...map.values()].filter(t=>t.completed_at).length;
  $("lifeScore").textContent=(complete*25)+"/100 Home Care";
  for(const meta of TASKS){
   const entry=map.get(meta.key),done=!!entry?.completed_at;
   const row=document.createElement("div");row.className="duty-row"+(done?" duty-done":"");
   const summary=document.createElement("div");summary.className="duty-summary";
   const head=document.createElement("strong");head.textContent=meta.emoji+" "+meta.title;
   const sub=document.createElement("small");
   if(done)sub.textContent="✓ Completed today by "+(entry.completed_by===getUser()?.id?"you":"your person");
   else if(entry?.assigned_to)sub.textContent="Volunteered: "+(entry.assigned_to===getUser()?.id?"you":"your person");
   else sub.textContent="Available · resets at midnight UTC";
   summary.append(head,sub);row.append(summary);
   if(!done&&!entry?.assigned_to){
    const claim=document.createElement("button");claim.type="button";claim.className="duty-button";
    claim.textContent="I'll do it";
    claim.addEventListener("click",async()=>{
     claim.disabled=true;
     const res=await db.rpc("life_claim",{p_task:meta.key});
     if(res.error)status(explain(res.error));else status("Duty claimed. Use the matching furniture to finish it.");
     await refreshTasks();claim.disabled=false;
    });
    row.append(claim);
   }else if(done){const tick=document.createElement("span");tick.className="duty-tick";tick.textContent="✓";row.append(tick);}
   list.append(row);
  }
 }
 async function refreshTasks(){
  if(!getUser())return;
  const res=await db.from("life_daily_tasks").select("day,task_key,assigned_to,completed_by,completed_at").eq("day",today());
  if(res.error){status("Task sync: "+explain(res.error));return;}
  tasks=res.data||[];renderTasks();lastTasks=Date.now();
 }
 async function refreshNeeds(withTick=false){
  if(!getUser())return;
  let r;
  if(withTick&&document.visibilityState!=="hidden")r=await db.rpc("life_tick");
  else r=await db.from("life_needs").select("*").eq("user_id",getUser().id).single();
  if(r.error){status("Needs sync: "+explain(r.error));return;}
  needs=r.data;renderNeeds();
 }
 async function checkActivity(){
  if(!getUser())return;
  const res=await db.from("life_activities").select("*").eq("user_id",getUser().id).eq("status","active").limit(1).maybeSingle();
  if(res.error){status("Activity sync: "+explain(res.error));return;}
  active=res.data;renderProgress();
  if(active&&Date.now()>=new Date(active.started_at).getTime()+active.duration_seconds*1000)await finish();
 }
 async function refreshHouseholdActivities(){
  if(!running||!getUser())return;
  const result=await db.from("life_activities")
   .select("user_id,action_key,started_at,duration_seconds")
   .eq("status","active").limit(10);
  if(result.error)return;
  otherActivities=new Map((result.data||[]).map(a=>[a.user_id,a]));
 }
 function getActionFor(userId){
  if(userId===getUser()?.id)return active?.action_key||null;
  return otherActivities.get(userId)?.action_key||null;
 }
 async function start(){
  if(running)return;
  running=true;
  await Promise.all([refreshNeeds(true),refreshTasks(),checkActivity(),refreshHouseholdActivities()]);
  if(activityChannel)db.removeChannel(activityChannel);
  activityChannel=db.channel("our-space-life-activities")
   .on("postgres_changes",{event:"*",schema:"public",table:"life_activities"},()=>{
     refreshHouseholdActivities().catch(()=>{});
   }).subscribe();
  tickTimer=setInterval(()=>{
   if(!running||!getUser())return;
   refreshNeeds(true).catch(()=>{});
   if(Date.now()-lastTasks>20000)refreshTasks().catch(()=>{});
   refreshHouseholdActivities().catch(()=>{});
  },20000);
  renderProgress();
 }
 function stop(){
  running=false;clearInterval(tickTimer);tickTimer=null;
  active=null;needs=null;tasks=[];finishing=false;otherActivities=new Map();
  if(activityChannel)db.removeChannel(activityChannel);
  activityChannel=null;
  closeMenu();renderProgress();
 }
 function renderProgress(){
  if(!active){progress.classList.add("hidden");return;}
  progress.classList.remove("hidden");
  const meta=ACTIONS[active.action_key];
  $("lifeProgressName").textContent=(meta?.emoji||"⏳")+" "+(meta?.label||"Activity");
  const elapsed=Math.max(0,(Date.now()-new Date(active.started_at).getTime())/1000);
  const pct=Math.min(100,elapsed/active.duration_seconds*100);
  $("lifeProgressFill").style.width=pct+"%";
  $("lifeProgressTime").textContent=Math.max(0,Math.ceil(active.duration_seconds-elapsed))+"s";
 }
 function animate(){
  if(!running||!active)return;
  renderProgress();
  if(Date.now()>=new Date(active.started_at).getTime()+active.duration_seconds*1000
     &&!finishing&&Date.now()-completeAttempt>2500)finish().catch(()=>{});
 }
 async function finish(){
  if(!active||finishing)return;
  finishing=true;completeAttempt=Date.now();
  const a=active;
  try{
   const response=await db.rpc("life_finish",{p_id:a.id});
   if(response.error)throw response.error;
   active=null;renderProgress();
   const meta=ACTIONS[a.action_key];
   status("✓ "+(meta?.label||"Activity")+" complete!");
   await Promise.all([refreshNeeds(false),refreshTasks()]);
  }catch(e){status("Couldn't complete action: "+explain(e));}
  finally{finishing=false;}
 }
 async function cancel(){
  if(!active)return;
  $("lifeCancel").disabled=true;
  try{
   const res=await db.rpc("life_cancel",{p_id:active.id});
   if(res.error)throw res.error;
   active=null;renderProgress();status("Action cancelled.");
  }catch(e){status(explain(e));}
  finally{$("lifeCancel").disabled=false;}
 }
 function closeMenu(){actionBox.classList.add("hidden");$("lifeActionButtons").replaceChildren();}
 function menu(object,other=null){
  if(!running)return;
  closeMenu();
  const choices=Object.entries(ACTIONS).filter(([,a])=>a.object===object);
  if(!choices.length)return;
  $("lifeActionTitle").textContent=other?"Interact with "+String(other.display_name||"your person"):OBJECTS.find(o=>o.id===object)?.name||"Interact";
  for(const [key,meta] of choices){
   const button=document.createElement("button");button.type="button";button.className="action-choice";
   button.textContent=meta.emoji+" "+meta.label+" · "+meta.duration+"s";
   if(active)button.disabled=true;
   if(key==="eat"&&Number(needs?.meals||0)<1){button.disabled=true;button.title="Cook a meal at the stove first";}
   button.addEventListener("click",()=>perform(key,other));
   $("lifeActionButtons").append(button);
  }
  actionBox.classList.remove("hidden");
 }
 function perform(key,other){
  const meta=ACTIONS[key];if(!meta||active)return;
  closeMenu();if(!onHome()){status("Enter the cottage to perform life activities.");return;}
  let destination;
  if(meta.object==="partner"){
   if(!other){status("Your person is not nearby.");return;}
   // Approach within 110 pixels while remaining in a clear tile.
   destination=[Number(other.x)+50,Number(other.y)];
  }else destination=OBJECTS.find(o=>o.id===meta.object)?.stand;
  if(!destination){status("Couldn't find that furniture.");return;}
  status("Walking to "+(meta.object==="partner"?"your person":meta.label.toLowerCase())+"…");
  const success=goTo(destination[0],destination[1],async()=>{
   if(!running||active||!onHome())return;
   try{
    await savePosition();
    const result=await db.rpc("life_start",{p_action:key,p_object:meta.object});
    if(result.error)throw result.error;
    active=result.data;renderProgress();status("Doing: "+meta.label);
   }catch(e){status("Action could not start: "+explain(e));}
  });
  if(!success)status("No walkable route to that object.");
 }
 function interactAt(x,y){
  const obj=OBJECTS.find(o=>{const [rx,ry,w,h]=o.rect;return x>=rx-6&&x<=rx+w+6&&y>=ry-6&&y<=ry+h+6;});
  if(obj){menu(obj.id);return true;}
  const partner=getAvatars().find(a=>a.user_id!==getUser()?.id&&a.world_id==="home"&&Math.hypot(a.x-x,a.y-y)<60);
  if(partner){menu("partner",partner);return true;}
  closeMenu();return false;
 }
 function getSpeed(){
  const low=Math.min(...NEEDS.map(n=>numeric(needs?.[n.key]??80)));
  return low<20?.65:low<40?.82:1;
 }
 async function onChangeWorld(id){
  home=id==="home";
  $("lifeHud").classList.toggle("hidden",!home);
  $("lifeDutyPanel").classList.toggle("hidden",!home);
  if(!home)closeMenu();
  if(home&&running){await refreshNeeds(true);await refreshTasks();}
 }
 function onShowWardrobe(){closeMenu();}
 $("lifeCloseMenu").addEventListener("click",closeMenu);
 $("lifeCancel").addEventListener("click",cancel);
 document.addEventListener("visibilitychange",()=>{
  if(document.visibilityState==="visible"&&running){refreshNeeds(true).catch(()=>{});refreshTasks().catch(()=>{});checkActivity().catch(()=>{});}
 });
 return {start,stop,onChangeWorld,animate,interactAt,menu,closeMenu,onShowWardrobe,
   getSpeed,refreshNeeds,refreshTasks,getActionFor,get active(){return active;}};
}
