// Four-window dock v2, network-first to keep updated UI and data separate.
const CACHE="focusflash-four-pane-dock-v4";
const STATIC=[
 "./","./index.html",
 "./styles.css?v=four-panes-4","./editor.css?v=four-panes-4",
 "./workspace.css?v=four-panes-4","./reference-layout.css?v=four-panes-4",
 "./layout-v3.css?v=four-panes-4","./dock-windows.css?v=four-panes-4",
 "./four-pane-mobile.css?v=four-panes-4",
 "./profiles.js?v=four-panes-4","./dock-windows.js?v=four-panes-4",
 "./app.js?v=four-panes-4","./editor.js?v=four-panes-4",
 "./transcript.js?v=four-panes-4","./script-blocks.js?v=four-panes-4",
 "./video-studio.js?v=four-panes-4","./tone-generator.js?v=four-panes-4",
 "./instant-tts.js?v=four-panes-4","./pitch-preserve.js?v=four-panes-4",
 "./fast-piper.js?v=four-panes-4",
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