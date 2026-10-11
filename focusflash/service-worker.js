// Four-window dock v2, network-first to keep updated UI and data separate.
const CACHE="focusflash-four-pane-dock-v2";
const STATIC=[
 "./","./index.html",
 "./styles.css?v=four-panes-2","./editor.css?v=four-panes-2",
 "./workspace.css?v=four-panes-2","./reference-layout.css?v=four-panes-2",
 "./layout-v3.css?v=four-panes-2","./dock-windows.css?v=four-panes-2",
 "./profiles.js?v=four-panes-2","./dock-windows.js?v=four-panes-2",
 "./app.js?v=four-panes-2","./editor.js?v=four-panes-2",
 "./transcript.js?v=four-panes-2","./script-blocks.js?v=four-panes-2",
 "./video-studio.js?v=four-panes-2","./tone-generator.js?v=four-panes-2",
 "./instant-tts.js?v=four-panes-2","./pitch-preserve.js?v=four-panes-2",
 "./fast-piper.js?v=four-panes-2",
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