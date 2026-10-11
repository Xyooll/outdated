// FocusFlash: responsive app-like editor with split mobile tool/timeline views.
const CACHE="focusflash-mobile-workspace-v1";
const STATIC=[
 "./","./index.html",
 "./styles.css?v=mobile-workspace-1","./editor.css?v=mobile-workspace-1",
 "./workspace.css?v=mobile-workspace-1",
 "./reference-layout.css?v=mobile-workspace-1",
 "./layout-v3.css?v=mobile-workspace-1",
 "./profiles.js?v=mobile-workspace-1","./app.js?v=mobile-workspace-1",
 "./editor.js?v=mobile-workspace-1","./transcript.js?v=mobile-workspace-1",
 "./script-blocks.js?v=mobile-workspace-1",
 "./video-studio.js?v=mobile-workspace-1","./tone-generator.js?v=mobile-workspace-1",
 "./instant-tts.js?v=mobile-workspace-1",
 "./pitch-preserve.js?v=mobile-workspace-1",
 "./fast-piper.js?v=mobile-workspace-1",
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