// FocusFlash Sound Mixer v2: app shell, soundscapes and local MP3 import.
const CACHE="focusflash-sound-mixer-v2";
const STATIC=[
 "./","./index.html","./styles.css?v=sound-mixer-2","./editor.css?v=sound-mixer-2",
 "./app.js?v=sound-mixer-2","./editor.js?v=sound-mixer-2",
 "./tone-generator.js?v=sound-mixer-2","./script-blocks.js?v=sound-mixer-2",
 "./video-studio.js?v=sound-mixer-2","./instant-tts.js?v=sound-mixer-2",
 "./pitch-preserve.js?v=sound-mixer-2","./fast-piper.js?v=sound-mixer-2",
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