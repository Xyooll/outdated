
// Deterministic 960×540 top-down household. No outside game engine.
export const OBJECTS=[
 {id:"stove",name:"Stove",label:"🍳 Stove",area:"Kitchen",rect:[91,150,104,77],stand:[211,239]},
 {id:"table",name:"Dining table",label:"🍽️ Dining table",area:"Kitchen",rect:[320,168,104,76],stand:[365,263]},
 {id:"shower",name:"Shower",label:"🚿 Shower",area:"Bathroom",rect:[790,144,114,87],stand:[742,245]},
 {id:"sink",name:"Sink",label:"🫧 Sink",area:"Bathroom",rect:[539,165,102,67],stand:[653,241]},
 {id:"couch",name:"Sofa",label:"🛋️ Sofa",area:"Living room",rect:[88,356,150,77],stand:[277,407]},
 {id:"tv",name:"TV",label:"📺 TV",area:"Living room",rect:[328,349,107,70],stand:[326,435]},
 {id:"laundry",name:"Laundry basket",label:"🧺 Laundry",area:"Living room",rect:[85,446,79,53],stand:[199,455]},
 {id:"bed",name:"Bed",label:"🛏️ Bed",area:"Bedroom",rect:[744,355,152,106],stand:[694,418]}
];
export const ACTIONS={
 cook:{object:"stove",label:"Cook a meal",duration:9,task:"cook",emoji:"🍳",need:"Food"},
 eat:{object:"table",label:"Eat a meal",duration:6,emoji:"🍽️",need:"Hunger +32"},
 sleep:{object:"bed",label:"Sleep",duration:13,emoji:"💤",need:"Energy +45"},
 shower:{object:"shower",label:"Take a shower",duration:11,emoji:"🚿",need:"Hygiene +42"},
 relax:{object:"couch",label:"Sit and relax",duration:8,emoji:"🧸",need:"Fun +12 · Energy +8"},
 watch:{object:"tv",label:"Watch TV",duration:10,emoji:"📺",need:"Fun +34"},
 dishes:{object:"sink",label:"Wash dishes",duration:8,task:"dishes",emoji:"🫧",need:"Home Care"},
 laundry:{object:"laundry",label:"Do laundry",duration:9,task:"laundry",emoji:"🧺",need:"Home Care"},
 tidy:{object:"couch",label:"Tidy the living room",duration:10,task:"tidy",emoji:"🧹",need:"Home Care"},
 wave:{object:"partner",label:"Wave hello",duration:3,emoji:"👋",need:"Social +16"},
 hug:{object:"partner",label:"Give a hug",duration:4,emoji:"❤️",need:"Social +32"}
};
export const TASKS=[
 {key:"cook",title:"Prepare a meal",object:"stove",emoji:"🍲"},
 {key:"dishes",title:"Wash dishes",object:"sink",emoji:"🫧"},
 {key:"laundry",title:"Do the laundry",object:"laundry",emoji:"🧺"},
 {key:"tidy",title:"Tidy the home",object:"couch",emoji:"🧹"}
];
export const NEEDS=[
 {key:"hunger",label:"Hunger",emoji:"🍽️"},
 {key:"energy",label:"Energy",emoji:"⚡"},
 {key:"hygiene",label:"Hygiene",emoji:"🫧"},
 {key:"fun",label:"Fun",emoji:"🎮"},
 {key:"social",label:"Social",emoji:"❤️"}
];
const walls=[
 [14,104,932,16],[14,508,932,16],[14,104,16,420],[930,104,16,420],
 [469,120,20,74],[469,256,20,116],[469,428,20,80],
 [28,293,137,17],[248,293,406,17],[759,293,171,17]
];
const solids=[...walls,...OBJECTS.map(o=>o.rect)];
const inRect=(x,y,[rx,ry,w,h],margin=0)=>x>=rx-margin&&x<=rx+w+margin&&y>=ry-margin&&y<=ry+h+margin;
export function objectAt(x,y){return OBJECTS.find(o=>inRect(x,y,o.rect,7))||null;}
export function clearTile(x,y){
 if(x<35||x>924||y<124||y>495)return false;
 return !solids.some(r=>inRect(x,y,r,10));
}
export function clampHousePoint(x,y){
 return [Math.max(36,Math.min(923,x)),Math.max(125,Math.min(494,y))];
}
// Deterministic four-neighbor grid BFS. Collision map is shared with drawing.
export function findHousePath(fromX,fromY,toX,toY){
 const scale=20,cols=48,rows=27;
 const n=cols*rows;
 const xy=k=>[(k%cols)*scale+10,Math.floor(k/cols)*scale+10];
 const cell=(x,y)=>Math.max(0,Math.min(cols-1,Math.floor(x/scale)))+
 Math.max(0,Math.min(rows-1,Math.floor(y/scale)))*cols;
 function closest(k){
  const [x,y]=xy(k);
  if(clearTile(x,y))return k;
  const visited=new Uint8Array(n),queue=[k];visited[k]=1;
  for(let i=0;i<queue.length;i++){
   const v=queue[i],cx=v%cols,cy=(v/cols)|0;
   for(const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){
    const ax=cx+dx,ay=cy+dy;if(ax<0||ax>=cols||ay<0||ay>=rows)continue;
    const q=ay*cols+ax;if(visited[q])continue;visited[q]=1;
    const [px,py]=xy(q);if(clearTile(px,py))return q;
    queue.push(q);
   }
  }
  return -1;
 }
 const start=closest(cell(fromX,fromY)),dest=closest(cell(toX,toY));
 if(start<0||dest<0)return [];
 if(start===dest){const p=xy(dest);return [p];}
 const previous=new Int32Array(n).fill(-1),seen=new Uint8Array(n),queue=[start];
 seen[start]=1;
 for(let i=0;i<queue.length;i++){
  const v=queue[i];if(v===dest)break;
  const x=v%cols,y=(v/cols)|0;
  for(const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){
   const ax=x+dx,ay=y+dy;if(ax<0||ax>=cols||ay<0||ay>=rows)continue;
   const q=ay*cols+ax;if(seen[q])continue;
   const [px,py]=xy(q);if(!clearTile(px,py))continue;
   previous[q]=v;seen[q]=1;queue.push(q);
  }
 }
 if(!seen[dest])return [];
 const out=[];let cursor=dest;
 while(cursor!==start&&cursor!==-1){out.push(xy(cursor));cursor=previous[cursor];}
 out.reverse();
 // Remove runs in straight lines, retaining every corner.
 const compact=[];
 for(let i=0;i<out.length;i++){
  const prev=i===0?[fromX,fromY]:out[i-1],next=out[i+1];
  if(!next||Math.sign(out[i][0]-prev[0])!==Math.sign(next[0]-out[i][0])
      ||Math.sign(out[i][1]-prev[1])!==Math.sign(next[1]-out[i][1]))compact.push(out[i]);
 }
 return compact;
}
const box=(c,color,x,y,w,h)=>{c.fillStyle=color;c.fillRect(x,y,w,h);};
const rounded=(c,color,x,y,w,h,r=9)=>{c.fillStyle=color;c.beginPath();c.roundRect(x,y,w,h,r);c.fill();};
const oval=(c,color,x,y,a,b)=>{c.fillStyle=color;c.beginPath();c.ellipse(x,y,a,b,0,0,Math.PI*2);c.fill();};
export function drawHouse(c,t){
 // Solid interior scene with four visibly differentiated, walkable rooms.
 box(c,"#35324f",0,0,960,540);
 rounded(c,"#cab79d",24,110,916,398,12);
 box(c,"#c6c2a9",30,120,439,172);     // Kitchen tiles
 box(c,"#a6c6c9",489,120,441,172);     // Bathroom tile
 box(c,"#b99186",30,310,439,195);     // Living floor
 box(c,"#9b8ea7",489,310,441,195);    // Bedroom floor
 for(let y=126;y<291;y+=28){box(c,"#fff7df35",30,y,439,2);box(c,"#e4f7f63d",489,y,441,2);}
 for(let x=32;x<468;x+=37)box(c,"#fcf4e428",x,120,2,173);
 for(let x=495;x<930;x+=37)box(c,"#f7fefe24",x,120,2,173);
 for(let y=332;y<505;y+=35){box(c,"#edb2a233",30,y,439,2);box(c,"#e4d5ec33",489,y,441,2);}
 // Four room title plaques.
 c.textAlign="left";c.font="bold 17px system-ui";
 for(const [s,x,y,col] of [["KITCHEN",45,143,"#654d51"],["BATHROOM",507,143,"#4a6970"],
 ["LIVING ROOM",42,336,"#69464f"],["BEDROOM",505,336,"#5a4c6c"]]){
  c.fillStyle=col;c.fillText(s,x,y);
 }
 // Decorative rugs and small house plants.
 oval(c,"#efe0c270",280,433,96,43);
 oval(c,"#e7d6e68a",635,444,100,39);
 oval(c,"#637b6190",444,476,18,10);rounded(c,"#97755d",434,461,21,16,4);
 oval(c,"#699b72",444,451,23,19);
 // Interactive furniture uses hitboxes that match pathfinder obstacles.
 for(const o of OBJECTS){
  const [x,y,w,h]=o.rect;
  if(o.id==="stove"){
   rounded(c,"#eeeeec",x,y,w,h,10);rounded(c,"#5e646b",x+12,y+9,w-24,h-33,5);
   for(const [dx,dy] of [[27,24],[75,24],[27,51],[75,51]]){
    oval(c,"#141e30",x+dx,y+dy,12,9);oval(c,"#8b919a",x+dx,y+dy,7,5);}
   rounded(c,"#d8b6a5",x+14,y+h-18,w-28,11,4);
  }else if(o.id==="table"){
   oval(c,"#69556a",x+w/2,y+h/2+9,w/2+4,h/2);
   rounded(c,"#dbb694",x+5,y+2,w-10,h-18,10);
   for(const i of [24,73]){oval(c,"#fff5ec",x+i,y+24,15,12);oval(c,"#e6c5aa",x+i,y+24,9,6);}
  }else if(o.id==="shower"){
   rounded(c,"#edf3f4",x,y,w,h,8);rounded(c,"#79b8c5",x+8,y+7,w-16,h-14,7);
   box(c,"#e8ffff8c",x+13,y+10,6,h-20);box(c,"#e8ffff8c",x+w-19,y+10,6,h-20);
   oval(c,"#dff5f6",x+w/2,y+h/2,20,16);
  }else if(o.id==="sink"){
   rounded(c,"#f5e9db",x,y,w,h,10);oval(c,"#8ea7ad",x+w/2,y+h/2,31,20);
   oval(c,"#eaf6f7",x+w/2,y+h/2,23,15);box(c,"#747c83",x+w/2-4,y+4,8,17);
  }else if(o.id==="couch"){
   rounded(c,"#755575",x,y,w,h,16);rounded(c,"#c18b9f",x+9,y+11,w-18,h-22,13);
   rounded(c,"#e8b2bc",x+24,y+25,44,32,8);rounded(c,"#bfb0d4",x+76,y+25,48,32,8);
  }else if(o.id==="tv"){
   rounded(c,"#393d59",x,y,w,h,8);rounded(c,"#2c4965",x+10,y+8,w-20,h-22,5);
   box(c,"#85a7a6",x+15,y+25,35,4);box(c,"#c7b8d5",x+19,y+38,65,4);
   box(c,"#e3d7cf",x+25,y+h-10,w-50,5);
  }else if(o.id==="laundry"){
   rounded(c,"#92776c",x,y,w,h,10);rounded(c,"#e0ba9f",x+8,y+3,w-16,h-9,8);
   for(let i=0;i<4;i++)oval(c,["#fff3e9","#b6a6c6","#9cbec1","#d9a3a5"][i],x+18+i*13,y+19,9,12);
  }else if(o.id==="bed"){
   rounded(c,"#715976",x,y,w,h,15);rounded(c,"#e9b7ba",x+10,y+8,w-20,h-16,10);
   rounded(c,"#efdece",x+16,y+13,w-32,30,9);
   rounded(c,"#a99fc3",x+15,y+48,w-30,h-60,6);
   rounded(c,"#fff0e3",x+27,y+16,42,23,7);rounded(c,"#fff0e3",x+83,y+16,42,23,7);
  }
 }
 // Wall segments above all objects.
 for(const [x,y,w,h] of walls){rounded(c,"#67556d",x,y,w,h,5);box(c,"#b1a5b4",x,y,w,4);}
 // Little door thresholds visually mark entrances.
 for(const [x,y,w,h] of [[171,293,70,6],[661,293,90,6],[469,204,7,43],[469,383,7,36]]){
  rounded(c,"#e4c9a3",x,y,w,h,2);
 }
 c.fillStyle="#f6e6d1";c.font="bold 12px system-ui";c.textAlign="center";
 for(const o of OBJECTS){
  const [x,y,w,h]=o.rect;
  rounded(c,"#22243cbb",x+w/2-35,y+h+4,70,20,10);
  c.fillStyle="#fff4e9";c.fillText(o.name,x+w/2,y+h+18,65);
 }
 c.textAlign="left";
}
