// Network-first app shell for the installable 2D worlds; never cache Supabase API data.
const CACHE="our-space-v6-worlds";
const FILES=["./","./index.html","./config.js","./world.css","./world.js","./world-art.js","./icon.svg","./manifest.webmanifest"];
self.addEventListener("install",e=>{
 e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES)));
 self.skipWaiting();
});
self.addEventListener("activate",e=>{
 e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k)))));
 self.clients.claim();
});
self.addEventListener("fetch",e=>{
 if(e.request.method!=="GET"||new URL(e.request.url).origin!==self.location.origin)return;
 e.respondWith(fetch(e.request).catch(()=>caches.match(e.request)));
});
