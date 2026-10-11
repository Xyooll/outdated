# Our Space — Mini Life Simulator for Two

Live app: https://xyooll.github.io/outdated/our-space/

The primary **Cozy Cottage** world now contains a four-room household life simulator with movement, grid obstacle avoidance, interactive furniture, timed activities, needs, four voluntary daily duties, appearance customization, private chat, and persistent profiles.

## House and gameplay
- Four rooms: kitchen, bathroom, living room, bedroom. Click/tap furniture, then choose an action. The avatar walks to the furniture before the server starts a timed activity.
- Eight interactable furniture objects: stove, dining table, shower, sink, couch, TV, laundry basket, bed. The sofa has an extra **tidy** action.
- Five needs: hunger, energy, hygiene, fun, social; values 0–100. Needs drop *only during active use* and by at most ~20 seconds worth on returning from a pause.
- Meals: cook at stove to prepare food, then eat at table. Cooking sets one of four household chores to completed. Relax, shower, TV, sleep and interactions restore different needs.
- Four UTC-daily duties: prepare meal, wash dishes, do laundry, tidy home. Either member can volunteer. The first eligible completion counts toward the shared 0–100 Home Care score; repeat actions don't double-count.
- Tap the other player's avatar in the Cottage to wave or hug while they're online and nearby.
- Outfit and avatar position continue to save automatically. Real-time messaging and other worlds (Moon Garden, Sunset Shore) remain available.
- No new passphrase; Supabase login session persists between visits.

## Architecture
Static GitHub Pages PWA with modules:
- `world.js`: login, chat, avatars, movement, real-time subscriptions.
- `world-art.js`: avatar and optional garden/shore scenes.
- `life-house.js`: original top-down house drawing, fixed furniture map, shared collision and BFS pathfinding, action and task catalog.
- `life-ui.js`: needs, duty panel, contextual actions, progress bars, server RPC integration.
- `world.css`: mobile-first user interface.

Supabase tables `life_needs`, `life_activities`, `life_daily_tasks` hold persistent data. Critical activities are started/finished by checked server-side RPC functions so another client cannot forge action durations or award duplicate daily chores. Only the two authorized `couple_members` can use the APIs. All new public tables have row-level security; no browser service-role key is used.

**Privacy:** Chatrooms are authenticated and private to the two accounts but are NOT end-to-end encrypted. Existing room messages remain. Three older encrypted messages are available through [legacy.html](./legacy.html) with the original shared phrase. Neither set of messages was deleted.

## How to play on Android
Open the live app in Chrome and refresh (or restart installed app). Sign in if needed. The Cottage defaults to the playable house. Touch furniture to choose actions, or tap the floor to walk. Use arrow buttons to move. Tap **Dress up** to change hair, outfit, and accessories. Expand **Household duties** to volunteer for a task. Send text messages in the same private chat.

## Limits / deliberate scope
This is a compact 2D life simulation, **not The Sims 4**. No careers, pregnancy, building editor, inventories beyond prepared meal count, additional households, physics engine, or real-world responsibility tracking. It uses rapid example action durations (seconds) for an approachable playable prototype, not simulated multi-hour real time. Browser gameplay with two real phones must still be verified end to end after deployment.

## Visual action feedback

Walking animates alternating legs; eating/relaxing/watching shift the character toward a seated pose; sleeping leans the character and displays a sleep activity label. The household task list opens by default. Older avatar locations trapped in the new furniture map are safely moved to the center of the living room on first load.

Partner activities are now visible on both phones through a read-only, two-member RLS-protected Realtime stream. Furniture activity labels and simple movement/sitting/resting poses appear on the corresponding character.


## Life Sim 2.1: Old overlay removed

The life simulator is now the main screen. The previous stacked world navigator and always-visible chat overlay are removed. **Outfit**, **Duties**, **Places**, and **Chat** are toolbar controls. Chat and duties open as separate drawers; Places opens a small destination selector. The mobile movement controls are outside the canvas, below the household map, rather than covering the scene.

The app footer shows **Life Sim 2.1**. To force-refresh a phone that still displays the old overlay, open https://xyooll.github.io/outdated/our-space/?v=life-layout-2 in Chrome. The service worker uses cache `our-space-v8-sim-first`, and local JavaScript/CSS modules use revisioned URLs. This UI change does not alter authentication, conversations, room data, avatars, or household progress.
