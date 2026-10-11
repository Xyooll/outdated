# Our Space — Worlds for Two

**Live app:** https://xyooll.github.io/outdated/our-space/

A game-like private two-person chat. Each approved member signs in with their own Supabase email/password, moves a customizable pixel character through three shared scenes, and sends real-time messages in that scene.

## Worlds

- 🏡 **Cozy Cottage** — home lounge and the "Just Us" chat.
- 🌙 **Moon Garden** — moonlit garden and its own chat.
- 🌅 **Sunset Shore** — beach walk and its own chat.

Tap the 2D Canvas to walk toward a destination, use WASD/arrow keys on desktop, or touch the four directional controls on mobile. **Dress up** opens the character closet: name, five skin tones, five hair styles, six hair colors, six tops, four bottoms, five accessories. The changes save immediately when you tap **Save my look** and appear for both people.

## Persistence and privacy

- **Login session**: Supabase auth `persistSession` and `autoRefreshToken` keep each device logged in, unless the user signs out or clears browser storage.
- **Saved avatar**: `public.world_avatars` holds display name, cosmetics, world, and position for both authorized people. The app sends position updates at roughly one per second while walking and heartbeats during active sessions. Updates from the other person arrive over Supabase Realtime. The scene reflects whether your partner was recently connected; movement latency depends on network conditions.
- **Chat rooms**: `public.chat_rooms` and `public.chat_room_messages` hold independent room-specific messages. Row-Level Security restricts all room data to the exact two `public.couple_members` users. New chats are *not end-to-end encrypted*: the server can read message content. It is not a Signal substitute.
- **Old conversation**: The 3 older, passphrase-encrypted messages remain untouched in `public.couple_messages`, and the old client has been preserved at [legacy.html](./legacy.html), where the original shared phrase is still required to read them. Do not delete the old database objects without exporting what you need.

## Technical overview

Static GitHub Pages PWA: [index.html](./index.html) + [world.css](./world.css) + [world.js](./world.js) + [world-art.js](./world-art.js). Built using the Canvas 2D API (all art is original canvas geometry, no third-party sprites). Supabase JS manages login, database queries and Realtime changes. No secret/service-role API keys belong in the public source; only the browser-safe publishable key is in [config.js](./config.js).

A dedicated project named **Our Space** exists in the Supabase **Xyool Org**. [Dashboard](https://supabase.com/dashboard/project/vtlqpgmipfhdjiidssxg). The two accounts were already approved in `public.couple_members`. The old cryptographic chat and old project Xyool are unchanged.

## Using it on Android

Open the live app URL in Chrome. Tap the browser's ⋮ menu and choose **Install app** or **Add to Home screen**. Sign in on both phones with your two approved email/password pairs; **no shared encryption phrase** is required for the new world chats. Login sessions in Gmail's embedded browser and Chrome may be separate, so use the same browser or installed PWA consistently.

## Security model and limitations

- Database table grants plus RLS block unauthenticated clients and accounts outside the approved two users. The new server-readable chats are intentionally easier to access but **not end-to-end encrypted**. Both members can view each room's messages, including when the other is offline.
- Avatar locations only represent positions in the fictional 2D world, not physical device locations.
- No photos, push notifications, item shop, XP, inventory, collidable physics, or account-wide appearance moderation yet. Worlds are 2D scenes; all three have a fixed layout, and server coordinates are updated at a moderate interval rather than every animation frame.
- For the best privacy, lock both phones, use individual strong account passwords, and consider enabling multi-factor authentication.
