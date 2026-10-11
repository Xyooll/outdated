// Only app shell, never API responses or decrypted messages.
const name="our-space-v2";const shell=["./","./index.html","./config.js","./icon.svg","./manifest.webmanifest"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(name).then(c=>c.addAll(shell)));self.skipWaiting();});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==name).map(k=>caches.delete(k)))));self.clients.claim();});
self.addEventListener("fetch",e=>{if(e.request.method!=="GET"||new URL(e.request.url).origin!==self.location.origin)return;e.respondWith(fetch(e.request).catch(()=>caches.match(e.request)));});
