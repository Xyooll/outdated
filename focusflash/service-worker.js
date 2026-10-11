// FocusFlash two-user Workspaces v2: network-first app-shell cache.
// Per-user documents and imported MP3s stay in browser LocalStorage / IDB.
const CACHE="focusflash-workspaces-v3";
const STATIC=[
 "./","./index.html","./styles.css?v=workspace-3",
 "./editor.css?v=workspace-3","./workspace.css?v=workspace-3",
 "./profiles.js?v=workspace-3","./app.js?v=workspace-3",
 "./editor.js?v=workspace-3","./script-blocks.js?v=workspace-3",
 "./video-studio.js?v=workspace-3","./tone-generator.js?v=workspace-3",
 "./instant-tts.js?v=workspace-3","./pitch-preserve.js?v=workspace-3",
 "./fast-piper.js?v=workspace-3","./manifest.webmanifest","./icon.svg"
];
self.addEventListener("install",event=>{
 event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(STATIC)));
 self.skipWaiting();
});
self.addEventListener("activate",event=>{
 event.waitUntil(caches.keys().then(keys=>Promise.all(
  keys.filter(k=>k.startsWith("focusflash-")&&k!==CACHE).map(k=>caches.delete(k))
  )));
 self.clients.claim();
});
self.addEventListener("fetch",event=>{
 if(event.request.method!=="GET"||new URL(event.request.url).origin!==self.location.origin)return;
 event.respondWith(fetch(event.request).catch(()=>caches.match(event.request)));
});