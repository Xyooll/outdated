// Our Space 3.0: network-only UI, no stale cached overlays.
// This worker intentionally does not intercept fetches. Existing offline
// game shell caches are removed on activation. Supabase gameplay needs network.
const REVISION="our-space-layout-3-network-only";
self.addEventListener("install",event=>{
 event.waitUntil(Promise.resolve().then(()=>self.skipWaiting()));
});
self.addEventListener("activate",event=>{
 event.waitUntil((async()=>{
  const keys=await caches.keys();
  await Promise.all(keys.filter(key=>key.startsWith("our-space-")).map(key=>caches.delete(key)));
  await self.clients.claim();
 })());
});
