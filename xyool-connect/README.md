# Xyool Connect — Basics v0.1
Live URL (GitHub Pages): https://xyooll.github.io/outdated/xyool-connect/

A **standalone, phone-friendly prototype** alongside (not inside) the existing Our Space app. It is a static, dependency-free, Google-free-at-the-app-level browser UI. It does NOT replace Android, Android Telecom, or the underlying Motorola firmware.

## Works now
- 2D vector avatar; custom display name, skin, hair and shirt colors saved to local browser storage.
- Local contact list: add, remove, and open native Android call/SMS intents.
- Number-entry dialer: hands off `tel:` and `sms:` actions to the phone's installed calling/messaging apps.
- Mobile bottom navigation and privacy information.
- Local state persists in the same browser profile across visits, and can be deleted.

## Not built
- Native Android phone replacement, SMS inbox access, MMS, RCS, SIP, app-to-app calls, emergency call handling.
- Backend chat, accounts, chat rooms, file transfers, E2EE, NFTs, gamification, markets, wallet and custom firmware.
- Offline PWA install/secure sync; currently use a browser and optionally create a home-screen shortcut.

## Privacy and limitations
No external scripts, analytics, or SDKs are included in the hosted page. Local browser storage is not encrypted; anyone with access to the device/browser profile may see saved contacts. The GitHub Pages host sees normal web-server request metadata. A cellular plan is still needed for typical phone calls and SMS.

Existing 'Our Space' app and Supabase data are untouched. The earlier downloadable v0.1 archive additionally includes **optional** experimental Supabase chat scaffolding; that is not deployed or active in this hosted basics build, and is not end-to-end encrypted.

## Quick test on Android
1. Open the live URL in a browser.
2. Change avatar name/appearance and Save; refresh to check persistence.
3. Add a test contact; refresh; verify it remains.
4. Tap Call and SMS on a contact or enter a number in Phone; ensure Android offers the correct installed app. No actual call or SMS is sent until you confirm it.
5. Use Settings/Profile > Delete to clear local data.

This is an early prototype; real phone tests are still required.
