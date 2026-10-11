// Network-first FocusFlash shell; no old HTML/JS cached across releases.
const CACHE="focusflash-video-v2";
const STATIC=[
 "./index.html","./styles.css?v=video-1",
 "./app.js?v=video-1","./video-studio.js?v=video-1",
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
 // No caching third-party model requests here: the runtime handles model cache.
 event.respondWith(fetch(event.request).catch(()=>caches.match(event.request)));
});
