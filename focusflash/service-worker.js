// Four-window dock v2, network-first to keep updated UI and data separate.
const CACHE="focusflash-spatial-v1";
const STATIC=[
 "./","./index.html",
 "./styles.css?v=spatial-v1","./editor.css?v=spatial-v1",
 "./workspace.css?v=spatial-v1","./reference-layout.css?v=spatial-v1",
 "./layout-v3.css?v=spatial-v1","./dock-windows.css?v=spatial-v1",
 "./four-pane-mobile.css?v=spatial-v1","./entrainment.css?v=spatial-v1",
 "./profiles.js?v=spatial-v1","./dock-windows.js?v=spatial-v1",
 "./app.js?v=spatial-v1","./editor.js?v=spatial-v1",
 "./transcript.js?v=spatial-v1","./script-blocks.js?v=spatial-v1",
 "./video-studio.js?v=spatial-v1","./tone-generator.js?v=spatial-v1",
 "./spatial-audio.js?v=spatial-v1",
 "./instant-tts.js?v=spatial-v1","./pitch-preserve.js?v=spatial-v1",
 "./fast-piper.js?v=spatial-v1",
 "./manifest.webmanifest","./icon.svg"
];
self.addEventListener("install",event=>{
 event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(STATIC)));
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