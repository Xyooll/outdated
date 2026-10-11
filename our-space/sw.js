// Network-first game shell; versioned assets prevent stale overlay modules.
const CACHE="our-space-v9-living-assets";
const FILES=[
 "./","./index.html","./config.js?v=assets-v1",
 "./world.css?v=assets-v1","./world.js?v=assets-v1",
 "./world-art.js?v=assets-v1","./life-house.js?v=assets-v1",
 "./life-ui.js?v=assets-v1","./life-assets.js?v=assets-v1","./icon.svg","./manifest.webmanifest"
];
self.addEventListener("install",event=>{
 event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(FILES)));
 self.skipWaiting();
});
self.addEventListener("activate",event=>{
 event.waitUntil(caches.keys().then(keys=>Promise.all(
  keys.filter(key=>key.startsWith("our-space-")&&key!==CACHE).map(key=>caches.delete(key))
 )));
 self.clients.claim();
});
self.addEventListener("fetch",event=>{
 if(event.request.method!=="GET")return;
 const url=new URL(event.request.url);
 if(url.origin!==self.location.origin)return;
 event.respondWith(fetch(event.request).catch(()=>caches.match(event.request)));
});
