// FocusFlash Script Blocks v2 — refresh the edit/playback shell.
const CACHE="focusflash-script-blocks-v2";
const STATIC=[
 "./","./index.html","./styles.css?v=blocks-2","./editor.css?v=blocks-2",
 "./app.js?v=blocks-2","./editor.js?v=blocks-2",
 "./script-blocks.js?v=blocks-2","./video-studio.js?v=blocks-2",
 "./instant-tts.js?v=blocks-2","./pitch-preserve.js?v=blocks-2",
 "./fast-piper.js?v=blocks-2","./manifest.webmanifest","./icon.svg"
];
self.addEventListener("install",event=>{
 event.waitUntil(caches.open(CACHE).then(c=>c.addAll(STATIC)));
 self.skipWaiting();
});
self.addEventListener("activate",event=>{
 event.waitUntil(caches.keys().then(keys=>Promise.all(
  keys.filter(key=>key.startsWith("focusflash-")&&key!==CACHE).map(key=>caches.delete(key))
  )));
 self.clients.claim();
});
self.addEventListener("fetch",event=>{
 if(event.request.method!=="GET"||new URL(event.request.url).origin!==self.location.origin)return;
 event.respondWith(fetch(event.request).catch(()=>caches.match(event.request)));
});