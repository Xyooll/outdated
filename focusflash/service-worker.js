// FocusFlash Studio: cache the app shell, not heavy optional voice models.
const CACHE="focusflash-font-focus-v1";
const STATIC=[
 "./","./index.html","./styles.css?v=font-focus-1","./editor.css?v=font-focus-1",
 "./app.js?v=font-focus-1","./editor.js?v=font-focus-1",
 "./video-studio.js?v=font-focus-1","./instant-tts.js?v=font-focus-1",
 "./pitch-preserve.js?v=font-focus-1","./fast-piper.js?v=font-focus-1",
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