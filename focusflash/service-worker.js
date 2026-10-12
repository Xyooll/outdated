// Four-window dock v2, network-first to keep updated UI and data separate.
const CACHE="focusflash-entrainment-v1";
const STATIC=[
 "./","./index.html",
 "./styles.css?v=entrainment-v1","./editor.css?v=entrainment-v1",
 "./workspace.css?v=entrainment-v1","./reference-layout.css?v=entrainment-v1",
 "./layout-v3.css?v=entrainment-v1","./dock-windows.css?v=entrainment-v1",
 "./four-pane-mobile.css?v=entrainment-v1","./entrainment.css?v=entrainment-v1",
 "./profiles.js?v=entrainment-v1","./dock-windows.js?v=entrainment-v1",
 "./app.js?v=entrainment-v1","./editor.js?v=entrainment-v1",
 "./transcript.js?v=entrainment-v1","./script-blocks.js?v=entrainment-v1",
 "./video-studio.js?v=entrainment-v1","./tone-generator.js?v=entrainment-v1",
 "./instant-tts.js?v=entrainment-v1","./pitch-preserve.js?v=entrainment-v1",
 "./fast-piper.js?v=entrainment-v1",
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