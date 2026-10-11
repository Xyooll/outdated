
// Pure Canvas asset and feedback layer for the compact two-player life simulator.
// Everything is procedural: no external artwork or copyrighted game assets.
import {OBJECTS,ACTIONS} from "./life-house.js?v=screen-3";
const PI=Math.PI;
const w=(t,s)=>Math.sin(t*s);
const color=(ctx,c)=>{ctx.fillStyle=c;};
function dot(ctx,x,y,r,fill){ctx.beginPath();ctx.arc(x,y,Math.max(.5,r),0,PI*2);color(ctx,fill);ctx.fill();}
function rect(ctx,x,y,w,h,c){color(ctx,c);ctx.fillRect(x,y,w,h);}
function rounded(ctx,x,y,w,h,r,c){ctx.beginPath();ctx.roundRect(x,y,w,h,r);color(ctx,c);ctx.fill();}
function stroke(ctx,x,y,w,h,r,c,width=2){ctx.beginPath();ctx.roundRect(x,y,w,h,r);ctx.strokeStyle=c;ctx.lineWidth=width;ctx.stroke();}
function sparkle(ctx,x,y,size,fill){
 ctx.save();ctx.translate(x,y);ctx.strokeStyle=fill;ctx.lineWidth=2;
 ctx.beginPath();ctx.moveTo(-size,0);ctx.lineTo(size,0);ctx.moveTo(0,-size);ctx.lineTo(0,size);ctx.stroke();ctx.restore();
}
function label(ctx,text,x,y,fill="#fff1f5"){
 ctx.font="bold 13px system-ui";ctx.textAlign="center";
 const width=Math.max(45,Math.min(150,ctx.measureText(text).width+18));
 rounded(ctx,x-width/2,y-23,width,29,10,"#24283eeb");
 stroke(ctx,x-width/2,y-23,width,29,10,"#f1d5e575",1);
 ctx.fillStyle=fill;ctx.fillText(text,x,y-4,width-14);
}
const find=id=>OBJECTS.find(o=>o.id===id);
const center=o=>({x:o.rect[0]+o.rect[2]/2,y:o.rect[1]+o.rect[3]/2});
export function paintHouseDetails(ctx,seconds){
 // Gentle environment-only embellishments that do not affect collision.
 ctx.save();
 // Warm kitchen overhead light; sunlight patch on the living-room floor.
 const sunlight=ctx.createRadialGradient(278,325,9,278,325,220);
 sunlight.addColorStop(0,"#fff0b52d");sunlight.addColorStop(1,"#fff0b500");
 ctx.fillStyle=sunlight;ctx.fillRect(45,285,410,205);
 // Clock
 dot(ctx,447,160,19,"#705e77");dot(ctx,447,160,16,"#f7eedc");
 ctx.strokeStyle="#7a6574";ctx.lineWidth=2;
 ctx.beginPath();ctx.moveTo(447,160);ctx.lineTo(447,147);ctx.moveTo(447,160);ctx.lineTo(456,165);ctx.stroke();
 // Kitchen backsplash decorations
 rounded(ctx,229,157,75,22,4,"#8e9b8a");
 for(let i=0;i<4;i++){rounded(ctx,236+i*17,152,12,23,4,["#e5b6a0","#d1d6cc","#99bab2","#e5c389"][i]);}
 // Small decorative house plant, not a collision object
 rounded(ctx,445,450,16,20,3,"#ab7d8c");
 for(let i=0;i<7;i++){dot(ctx,453+Math.sin(i*2.8)*12,444+Math.cos(i*2.9)*13,8,["#618c6f","#84ae82","#a4c695"][i%3]);}
 // Mirror & curtain in bathroom
 rounded(ctx,686,146,72,61,9,"#718e9e");
 rounded(ctx,695,155,54,43,6,"#c2dfe2");
 ctx.fillStyle="#ebf5ed70";ctx.fillRect(700,159,5,30);
 // Framed photo on bedroom wall
 rounded(ctx,879,262,38,29,3,"#e3b9a6");
 rounded(ctx,885,267,26,18,3,"#9983b3");
 dot(ctx,894,276,5,"#f2c6bc");dot(ctx,902,276,5,"#d8b09a");
 // Static contact sparkles on countertop, no flashing.
 for(let i=0;i<3;i++)sparkle(ctx,94+i*43,242+(i%2)*4,2.2,"#ffffff34");
 ctx.restore();
}
export function paintInteractiveHighlights(ctx,seconds,hoverId,selectedId,path){
 if(!hoverId&&!selectedId&&(!path||!path.length))return;
 ctx.save();
 if(path&&path.length){
  const dotCount=Math.min(path.length,18);
  for(let i=0;i<dotCount;i++){
   const [x,y]=path[i];dot(ctx,x,y,4+(w(seconds+i,2)+1)*.7,"#fff4c5a8");
  }
 }
 for(const [id,strong] of [[hoverId,false],[selectedId,true]]){
  if(!id)continue;const o=find(id);if(!o)continue;
  const [x,y,width,height]=o.rect,pulse=(w(seconds,4)+1)/2;
  rounded(ctx,x-6,y-6,width+12,height+12,12,strong?"#f6d6e127":"#fff5df19");
  stroke(ctx,x-5,y-5,width+10,height+10,12,strong?"#ffd69f":"#ffedd0",2.3+pulse*1.5);
  const mid=center(o);
  sparkle(ctx,mid.x,Math.max(139,y-18-pulse*6),5+pulse*3,"#fff2c5");
  if(strong)label(ctx,"Interact ✦",mid.x,Math.max(150,y-23));
 }
 ctx.restore();
}
function steam(ctx,o,t,col){
 const mid=center(o);
 for(let i=0;i<6;i++){
  const phase=(t*.43+i*.19)%1;
  const x=mid.x+Math.sin(i*2.5)*22+Math.sin(t*2+i)*6;
  const y=o.rect[1]+6-phase*42;
  dot(ctx,x,y,3.4+phase*2,col);
 }
}
function drops(ctx,o,t){
 const [x,y,ww,hh]=o.rect;
 for(let i=0;i<13;i++){
  const yy=((t*68+i*23)%hh);
  const px=x+19+(i*19)%(ww-36);
  rect(ctx,px,y+yy,2,7,"#effaffc2");
 }
}
function tvGlow(ctx,o,t){
 const [x,y,ww,hh]=o.rect;
 const cx=x+ww/2,cy=y+hh/2;
 const g=ctx.createRadialGradient(cx,cy,5,cx,cy,120);
 g.addColorStop(0,"#c4a8ff68");g.addColorStop(1,"#b1ccff00");
 ctx.fillStyle=g;ctx.fillRect(x-100,y-90,ww+200,hh+160);
 rounded(ctx,x+12,y+8,ww-24,hh-24,5,["#7dc2ce","#b2a0d4","#e6bbc4"][Math.floor(t*2)%3]);
 for(let i=0;i<4;i++)rect(ctx,x+19,y+19+i*8,ww-42,2,"#ffffff45");
}
function emotes(ctx,a,t){
 if(a.action_key==="sleep"){
  for(let i=0;i<3;i++){
   const phase=(t*.6+i*.37)%1;
   ctx.fillStyle="#fff4fa";ctx.font="bold "+Math.round(14+phase*12)+"px system-ui";
   ctx.textAlign="center";ctx.fillText("z",a.x+17+i*11,a.y-130-phase*43);
  }
 }else if(a.action_key==="hug"||a.action_key==="wave"){
  const ch=a.action_key==="hug"?"♥":"✦";
  for(let i=0;i<5;i++){
   const theta=i*PI*2/5+t*.8;
   const xx=a.x+Math.cos(theta)*26,yy=a.y-94+Math.sin(theta)*14;
   ctx.font="bold 17px system-ui";ctx.textAlign="center";ctx.fillStyle=a.action_key==="hug"?"#ffb7d9":"#fff0bd";ctx.fillText(ch,xx,yy);
  }
 }else if(a.action_key==="eat"){
  const phase=(t*2)%1;dot(ctx,a.x+14,a.y-81-phase*16,3,"#f5d99e");
 }
}
export function paintActivityEffects(ctx,seconds,activities,avatarProfiles,celebration){
 ctx.save();
 const users=new Map((avatarProfiles||[]).map(a=>[a.user_id,a]));
 for(const activity of activities||[]){
  const type=ACTIONS[activity.action_key],o=find(type?.object),a=users.get(activity.user_id);
  if(o){
   if(activity.action_key==="cook")steam(ctx,o,seconds,"#ffe0b6ab");
   if(activity.action_key==="shower")drops(ctx,o,seconds);
   if(activity.action_key==="dishes")steam(ctx,o,seconds,"#d9f8ffc4");
   if(activity.action_key==="watch")tvGlow(ctx,o,seconds);
   if(activity.action_key==="laundry"){
    const mid=center(o);
    for(let i=0;i<6;i++){const angle=seconds*2+i*PI/3;
     dot(ctx,mid.x+Math.cos(angle)*19,mid.y+Math.sin(angle)*13,3.5,["#fff6ee","#f2b5db"][i%2]);}
   }
   if(activity.action_key==="tidy"){
    const mid=center(o);
    for(let i=0;i<5;i++)sparkle(ctx,mid.x+Math.sin(seconds+i*2)*45,mid.y+Math.cos(seconds*2+i)*22,4,"#ffebbc");
   }
  }
  if(a)emotes(ctx,{...activity,x:a.x,y:a.y},seconds);
 }
 if(celebration && celebration.until>Date.now()){
  const life=Math.max(0,Math.min(1,(celebration.until-Date.now())/1700));
  const x=celebration.x??480,y=celebration.y??350;
  for(let i=0;i<18;i++){
   const phase=(i*2.39),radius=(1-life)*100;
   const px=x+Math.sin(phase)*radius,py=y-50+Math.cos(phase)*radius*.65;
   sparkle(ctx,px,py,2+life*3,["#fbd2e3","#fbe7ac","#b2e8d4"][i%3]);
  }
 }
 ctx.restore();
}
