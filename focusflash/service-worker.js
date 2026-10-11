// FocusFlash transcript editor v2 — explicit refresh of all app-shell assets.
const CACHE="focusflash-transcript-editor-v2";
const STATIC=[
 "./","./index.html",
 "./styles.css?v=reference-ui-2","./editor.css?v=reference-ui-2",
 "./workspace.css?v=reference-ui-2","./reference-layout.css?v=reference-ui-2",
 "./profiles.js?v=reference-ui-2","./app.js?v=reference-ui-2",
 "./editor.js?v=reference-ui-2","./transcript.js?v=reference-ui-2",
 "./script-blocks.js?v=reference-ui-2",
 "./video-studio.js?v=reference-ui-2",
 "./tone-generator.js?v=reference-ui-2",
 "./instant-tts.js?v=reference-ui-2",
 "./pitch-preserve.js?v=reference-ui-2",
 "./fast-piper.js?v=reference-ui-2",
 "./manifest.webmanifest","./icon.svg"
];
self.addEventListener("install",event=>{
 event.waitUntil(caches.open(CACHE).then(c=>c.addAll(STATIC)));
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