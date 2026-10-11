
// All art is drawn on Canvas; no downloaded sprites or art assets required.
export const WORLD_META = {
 home: {title:"Cozy Cottage",eyebrow:"A LITTLE PLACE CALLED HOME",subtitle:"A cozy room for unwinding together.",chat:"Cottage Chat",dbRoom:"Just Us"},
 garden: {title:"Moon Garden",eyebrow:"UNDER A VERY KIND MOON",subtitle:"Stroll under the stars. The flowers never sleep.",chat:"Garden Chat",dbRoom:"Moon Garden"},
 shore: {title:"Sunset Shore",eyebrow:"OUR LITTLE ENDLESS SUMMER",subtitle:"Golden skies, soft waves, and time for us.",chat:"Shore Chat",dbRoom:"Sunset Shore"}
};
const SKIN={warm:"#bf825e",light:"#f5c5a4",deep:"#7c4a3e",olive:"#bb9876",gold:"#ddb078"};
const HAIR={chocolate:"#543a3b",black:"#292b3d",blonde:"#e4bb71",rose:"#d889a7",silver:"#c6c7d9",violet:"#8971be"};
const TOP={pink:"#efaac7",blue:"#76bae3",green:"#8fcbb7",purple:"#b7a5f2",orange:"#f2a87d",black:"#45475d"};
const PANTS={denim:"#657fa6",plum:"#8f6a9b",cream:"#d9c9b7",charcoal:"#4c556b"};
const clamp=(v,a,b)=>Math.min(b,Math.max(a,v));
function fill(c,color,x,y,w,h){c.fillStyle=color;c.fillRect(Math.round(x),Math.round(y),Math.round(w),Math.round(h));}
function ellipse(c,color,x,y,rx,ry){c.fillStyle=color;c.beginPath();c.ellipse(x,y,rx,ry,0,0,Math.PI*2);c.fill();}
function line(c,color,x1,y1,x2,y2,width){c.strokeStyle=color;c.lineWidth=width;c.beginPath();c.moveTo(x1,y1);c.lineTo(x2,y2);c.stroke();}
function rounded(c,color,x,y,w,h,r=10){c.fillStyle=color;c.beginPath();c.roundRect(x,y,w,h,r);c.fill();}
function hash(i){const x=Math.sin(i*96.367)*43758.5453;return x-Math.floor(x);}
function star(c,x,y,rad=3,col="#f6dfc5"){fill(c,col,x-rad/2,y-rad/2,rad,rad);if(rad>=3){fill(c,col,x+1,y-rad*1.4,2,rad*2.8);fill(c,col,x-rad*1.4,y+1,rad*2.8,2);}}
function plant(c,x,y,scale=1){
 c.save();c.translate(x,y);c.scale(scale,scale);
 ellipse(c,"#263c40",0,0,22,7);
 line(c,"#466b61",0,-5,-3,-44,5);
 ellipse(c,"#4e9675",-18,-29,15,7);
 ellipse(c,"#6bac7d",15,-37,14,6);
 ellipse(c,"#7fbf8e",-7,-50,12,6);
 rounded(c,"#bb7879",-14,-13,28,19,5);
 fill(c,"#d9958f",-11,-12,22,5);
 c.restore();
}
function flowers(c,x,y,t=0){
 for(let i=0;i<5;i++){
  const ox=(i%3)*15-16,oy=Math.floor(i/3)*15,shift=Math.sin(t*1.2+i)*2;
  line(c,"#557d58",x+ox,y+oy,x+ox+shift,y+oy-16,2);
  ellipse(c,i%2?"#f6adc9":"#e3b8f2",x+ox+shift,y+oy-18,5,5);
  ellipse(c,"#ffe2a2",x+ox+shift,y+oy-18,2,2);
 }
}
function drawHome(c,t){
 let grad=c.createLinearGradient(0,0,0,540);grad.addColorStop(0,"#79668a");grad.addColorStop(.39,"#86728b");grad.addColorStop(.4,"#b99c8e");grad.addColorStop(1,"#b48176");c.fillStyle=grad;c.fillRect(0,0,960,540);
 // paneling
 for(let x=0;x<960;x+=80)fill(c,"#fff4fa10",x,0,3,216);
 fill(c,"#665574",0,210,960,18);fill(c,"#e0b4a0",0,226,960,5);
 for(let y=248;y<540;y+=55){fill(c,"#835e6277",0,y,960,3);for(let x=(y%110);x<960;x+=125)fill(c,"#8b6768bb",x,y,3,56);}
 // windows and stars
 rounded(c,"#f2d8bd",92,38,246,165,11);rounded(c,"#414861",103,49,224,143,5);
 rounded(c,"#242e52",113,56,204,128,4);
 for(let i=0;i<26;i++){star(c,120+hash(i+7)*187,68+hash(i+43)*103,2,"#f2d6d7");}
 ellipse(c,"#f9e1bd",270,93,24,24);
 fill(c,"#dcc2be",211,54,8,136);fill(c,"#dcc2be",111,111,210,7);
 // left book shelf
 rounded(c,"#553b51",390,40,140,172,9);rounded(c,"#73556a",402,48,116,156,4);
 for(let row=0;row<3;row++){fill(c,"#412d46",404,92+row*50,113,9);for(let i=0;i<8;i++){const x=408+i*13+hash(i*3+row)*3;fill(c,["#f6b2b5","#8bbeb9","#eac48b","#a6aadf"][i%4],x,60+row*50,8,31);}}
 // sofa
 ellipse(c,"#463f56a9",730,299,180,32);
 rounded(c,"#644f65",564,173,332,118,23);rounded(c,"#9c7a87",572,167,317,83,20);
 rounded(c,"#b88e94",595,203,273,73,17);rounded(c,"#e4b4a6",624,190,66,51,12);rounded(c,"#b4a4d4",757,191,66,50,12);
 fill(c,"#533d51",582,274,25,29);fill(c,"#533d51",853,274,25,29);
 // rug
 ellipse(c,"#61465b55",490,421,290,83);ellipse(c,"#e1b3a7",484,415,268,67);ellipse(c,"#d18f9a",484,416,212,40);
 // coffee table
 ellipse(c,"#5a435559",482,389,97,29);
 rounded(c,"#865b65",380,350,205,27,13);fill(c,"#664754",400,377,13,36);fill(c,"#664754",551,377,13,36);
 // steam and mug
 rounded(c,"#eee0c9",474,334,27,19,3);fill(c,"#b4a5b7",496,340,6,9);
 for(let i=0;i<3;i++){ellipse(c,"#fff7fa99",478+i*8,324-Math.sin(t*2+i)*3,2,4);}
 plant(c,879,395,1.45);plant(c,80,408,1.15);
 // lamp
 fill(c,"#50435d",69,168,7,146);ellipse(c,"#4d3e59",72,317,26,7);
 rounded(c,"#f9d49c",38,109,68,64,8);ellipse(c,"#f9dab544",72,187,90,32);
}
function drawGarden(c,t){
 const grad=c.createLinearGradient(0,0,0,540);grad.addColorStop(0,"#242e58");grad.addColorStop(.44,"#37466a");grad.addColorStop(.45,"#3f675e");grad.addColorStop(1,"#335f56");c.fillStyle=grad;c.fillRect(0,0,960,540);
 for(let i=0;i<85;i++)star(c,hash(i+8)*950,hash(i+333)*198,2+Math.floor(hash(i+9)*3),"#e5daf0");
 ellipse(c,"#f3dec6",787,84,42,42);ellipse(c,"#ffecca36",787,84,72,72);
 // mountains
 c.fillStyle="#40536e";c.beginPath();c.moveTo(0,260);for(let x=0;x<=960;x+=75)c.lineTo(x,203+hash(x)*80);c.lineTo(960,311);c.lineTo(0,311);c.fill();
 // grass
 for(let i=0;i<170;i++){let x=hash(i+130)*960,y=270+hash(i+42)*266;fill(c,hash(i+5)>.6?"#478274":"#39695e",x,y,4,2);}
 // stream and stone bridge
 ellipse(c,"#34566c",481,338,260,125);ellipse(c,"#6c99a5",482,336,225,93);ellipse(c,"#81b2b6",480,335,204,73);
 for(let i=0;i<13;i++){const x=290+i*31;line(c,"#c6d2c2bb",x,315+Math.sin(t+i)*3,x+13,313,2);}
 // garden paths
 ellipse(c,"#a4a18d",194,440,171,46);ellipse(c,"#a4a18d",761,451,205,40);
 for(let i=0;i<10;i++){ellipse(c,"#b6aea0",270+i*42,464+Math.sin(i)*10,17,7);}
 // luminous trees
 for(let a=0;a<3;a++){
 const x=[80,900,636][a],y=[260,271,240][a];fill(c,"#605468",x-11,y-110,22,139);
 for(let j=0;j<8;j++)ellipse(c,j%2?"#5b8b85":"#53827f",x+Math.sin(j*2)*40,y-114+Math.cos(j)*31,35,28);
 for(let j=0;j<8;j++)star(c,x+Math.sin(j*3+a)*49,y-115+Math.cos(j*4)*37,3,j%2?"#dba7e9":"#efd2a4");
 }
 // pergola for two
 rounded(c,"#c3a0a2",307,211,8,105,2);rounded(c,"#c3a0a2",651,211,8,105,2);
 rounded(c,"#d8b9b2",302,202,360,12,3);
 for(let i=0;i<15;i++)ellipse(c,i%2?"#f4b9d9":"#a3a8df",310+i*23,208+Math.sin(i)*11,9,8);
 flowers(c,155,374,t);flowers(c,799,360,t);flowers(c,699,483,t);
 rounded(c,"#745a61",25,365,170,15,4);fill(c,"#654c55",45,378,7,23);fill(c,"#654c55",170,378,7,23);
 rounded(c,"#745a61",772,387,160,15,4);fill(c,"#654c55",789,400,7,22);fill(c,"#654c55",906,400,7,22);
}
function drawShore(c,t){
 const grad=c.createLinearGradient(0,0,0,540);
 grad.addColorStop(0,"#7c6a9e");grad.addColorStop(.23,"#cb8f9b");grad.addColorStop(.48,"#f5bb9f");grad.addColorStop(.49,"#8cacae");grad.addColorStop(.64,"#679dad");grad.addColorStop(.65,"#eac39b");grad.addColorStop(1,"#cda480");c.fillStyle=grad;c.fillRect(0,0,960,540);
 ellipse(c,"#ffe0b2",672,160,69,69);ellipse(c,"#ffe7c73f",672,160,106,106);
 // layered sea bands
 for(let j=0;j<11;j++){
 const yy=249+j*8;line(c,j%2?"#c2c4b6":"#a6c2ba",0,yy,960,yy,2);
 }
 for(let i=0;i<20;i++){const x=hash(i+19)*930;line(c,"#eddfcf99",x,287+hash(i)*43,x+17,287+hash(i)*43,2);}
 // sand shell tessellation
 for(let i=0;i<90;i++){const x=hash(i+67)*960,y=342+hash(i+183)*186;fill(c,i%3?"#e8c6a3":"#c99886",x,y,6,3);}
 // shoreline wave moving
 c.strokeStyle="#fdf0d6aa";c.lineWidth=7;c.beginPath();
 for(let x=0;x<965;x+=12){const y=340+Math.sin(x/68+t*.8)*8;if(x===0)c.moveTo(x,y);else c.lineTo(x,y);}c.stroke();
 // umbrellas and lounge chairs
 ellipse(c,"#98796780",204,380,83,18);fill(c,"#675c65",203,221,7,166);ellipse(c,"#f4ab9e",206,227,100,45);ellipse(c,"#d880a0",206,227,74,32);
 rounded(c,"#c78f85",265,345,130,16,4);fill(c,"#815a5c",282,361,7,29);fill(c,"#815a5c",361,361,7,29);
 // palms
 for(let j=0;j<2;j++){
 const x=j?886:74,y=j?353:317;
 line(c,"#865c53",x,y,x+8,y-172,20);
 for(let i=0;i<7;i++){
  const a=-Math.PI+i*(Math.PI/6),rootx=x+8,rooty=y-177;
  c.strokeStyle=i%2?"#427e70":"#356962";c.lineWidth=14;c.beginPath();c.moveTo(rootx,rooty);c.quadraticCurveTo(rootx+Math.cos(a)*61,rooty+Math.sin(a)*52,rootx+Math.cos(a)*91,rooty+Math.sin(a)*86);c.stroke();
 }
 }
 for(let i=0;i<7;i++){const x=320+i*68,y=432+Math.sin(i*4)*47;ellipse(c,["#fac2aa","#d7a6bb","#f5daa3"][i%3],x,y,7,5);}
}
export function drawWorld(ctx,id,time=0){
 ctx.clearRect(0,0,960,540);
 if(id==="garden")drawGarden(ctx,time);
 else if(id==="shore")drawShore(ctx,time);
 else drawHome(ctx,time);
 // Subtle vignette to keep attention on characters.
 const v=ctx.createRadialGradient(480,280,180,480,270,650);
 v.addColorStop(0,"#00000000");v.addColorStop(1,"#1416284a");
 ctx.fillStyle=v;ctx.fillRect(0,0,960,540);
}
export function drawAvatar(ctx,a,x,y,opts={}){
 if(!a)return;
 const scale=opts.scale||1;
 ctx.save();ctx.translate(x,y);ctx.scale(scale,scale);
 if(opts.offline)ctx.globalAlpha=.53;
 ellipse(ctx,"#12182758",0,-2,26,8);
 // footwear
 fill(ctx,"#2b3545",-18,-14,16,10);fill(ctx,"#2b3545",3,-14,16,10);
 // legs/pants
 const pant=PANTS[a.bottoms]||PANTS.denim;
 fill(ctx,"#343347",-16,-27,16,18);fill(ctx,"#343347",1,-27,16,18);
 fill(ctx,pant,-14,-28,12,16);fill(ctx,pant,3,-28,12,16);
 // shirt and shoulders
 const top=TOP[a.shirt]||TOP.pink;
 fill(ctx,"#343347",-20,-51,40,27);
 fill(ctx,top,-18,-49,36,24);
 fill(ctx,"#f9e9d74d",-11,-46,7,3);
 const skin=SKIN[a.skin]||SKIN.warm, hair=HAIR[a.hair_color]||HAIR.chocolate;
 fill(ctx,"#343347",-25,-47,8,22);fill(ctx,skin,-23,-45,6,17);
 fill(ctx,"#343347",17,-47,8,22);fill(ctx,skin,19,-45,6,17);
 fill(ctx,skin,-7,-60,14,13); // neck
 // ears and face
 fill(ctx,"#323347",-17,-82,34,26);fill(ctx,skin,-14,-79,28,25);
 fill(ctx,skin,-19,-70,5,9);fill(ctx,skin,14,-70,5,9);
 // hair variations
 const hairStyle=a.hair_style||"short";
 if(hairStyle==="long"||hairStyle==="bob"){
  fill(ctx,hair,-19,-82,38,hairStyle==="long"?48:35);
  fill(ctx,skin,-13,-73,26,19);
 }else if(hairStyle==="curly"){
  for(const [ox,oy] of [[-18,-80],[-11,-88],[-2,-89],[8,-87],[15,-81],[-19,-72],[16,-72]])
   fill(ctx,hair,ox,oy,10,10);
 }else if(hairStyle==="spiky"){
  fill(ctx,hair,-17,-84,34,14);
  for(let i=0;i<4;i++)fill(ctx,hair,-15+i*10,-95+(i%2)*5,8,16);
 }else {
  fill(ctx,hair,-17,-83,34,12);
  fill(ctx,hair,-17,-79,7,15);
 }
 // fringe
 fill(ctx,hair,-12,-79,22,5);
 // eyes, smiling mouth, blush
 fill(ctx,"#24283a",-8,-68,3,4);fill(ctx,"#24283a",6,-68,3,4);
 fill(ctx,"#eaa1a4",-13,-63,5,2);fill(ctx,"#eaa1a4",9,-63,5,2);
 fill(ctx,"#7b4b50",-3,-59,7,2);
 switch(a.accessory){
 case "crown":
  fill(ctx,"#f9d681",-15,-99,30,8);
  for(let i=0;i<3;i++)fill(ctx,"#f9d681",-14+i*11,-105+(i===1?-5:0),8,13);
  fill(ctx,"#cb7894",-2,-96,4,4);break;
 case "flower":
  for(let i=0;i<5;i++){const theta=i*Math.PI*2/5;ellipse(ctx,"#f2b6d6",13+Math.cos(theta)*7,-82+Math.sin(theta)*7,5,5);}
  ellipse(ctx,"#f7dd97",13,-82,4,4);break;
 case "glasses":
  ctx.strokeStyle="#f6d8e8";ctx.lineWidth=2;
  ctx.strokeRect(-12,-72,12,10);ctx.strokeRect(3,-72,12,10);
  line(ctx,"#f6d8e8",0,-68,3,-68,2);break;
 case "halo":
  ctx.strokeStyle="#f6da96";ctx.lineWidth=4;ctx.beginPath();ctx.ellipse(0,-101,21,6,0,0,Math.PI*2);ctx.stroke();break;
 }
 if(opts.emote && !opts.offline){
  const text=String(opts.emote).slice(0,30);
  ctx.font="700 12px system-ui";
  const w=Math.min(250,ctx.measureText(text).width+22);
  rounded(ctx,"#24273df5",-w/2,-151,w,27,9);
  ctx.fillStyle="#fff0f9";ctx.textAlign="center";ctx.fillText(text,0,-134,w-12);
 }
 if(opts.label!==false){
  const label=String(a.display_name||"Friend").slice(0,24);
  ctx.font="700 12px system-ui";ctx.textAlign="center";
  const w=clamp(ctx.measureText(label).width+22,55,190);
  rounded(ctx,"#242841dd",-w/2,-120,w,23,10);
  ctx.fillStyle="#fff5f9";ctx.fillText(label,0,-104,w-10);
  if(opts.online)ellipse(ctx,"#83df9c",w/2-6,-108,3.5,3.5);
 }
 ctx.restore();
}
