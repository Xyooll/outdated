// FocusFlash undertone v1: network-first PWA shell, versioned local assets.
const CACHE="focusflash-undertone-v2";
const STATIC=[
 "./index.html","./styles.css?v=undertone-2",
 "./app.js?v=undertone-2","./video-studio.js?v=undertone-2",
 "./fast-piper.js?v=undertone-2","./manifest.webmanifest","./icon.svg"
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
