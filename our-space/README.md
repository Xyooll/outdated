# Our Space — private chat for two

A small, mobile-first progressive web app with realtime text messaging, Supabase email-link login, per-account row-level permissions, and browser-side AES-256-GCM message encryption.

## Setup before chatting

1. Create a NEW and DEDICATED Supabase project at https://supabase.com/dashboard. Do not reuse the Xyool Supabase project.
2. Open the NEW project SQL Editor and execute the contents of setup.sql.
3. In Authentication > Users, invite/create exactly two email users, one for each of you. Ensure both can sign in. Turn off public sign-ups.
4. Use the two commented INSERT statements at the end of setup.sql in SQL Editor to enroll those two email addresses by ID. Confirm SELECT * FROM public.couple_members returns exactly two rows. Never place actual emails in the GitHub repo.
5. In the new project's settings, find the Project URL and the PUBLISHABLE API key (legacy anon key also supported). Put these values in config.js. A publishable key is not a secret; NEVER expose a service_role or secret key.
6. Host this folder over HTTPS. On GitHub, go to Xyooll/outdated > Settings > Pages > Deploy from a branch > main > /(root), if Pages is not already enabled. The expected app URL is https://xyooll.github.io/outdated/our-space/ .
7. In Supabase Authentication > URL Configuration, set Site URL and add the EXACT final app URL as an allowed redirect URL.
8. On each phone open the app URL, request an email login link for the invited account, and follow the link on that phone.
9. Both people must independently enter the SAME strong shared phrase (at least 12 characters, ideally 6+ genuinely random words). Exchange it IN PERSON. It is never uploaded or stored, and is forgotten when the page locks/reloads.
10. Send a test message from each phone. Install on Android from Chrome menu > Add to Home screen / Install app.

## Security details

Only the two database-enrolled Supabase user IDs can read or write messages, enforced by database Row Level Security. Messages are encrypted locally with AES-256-GCM and a key derived from the shared phrase using PBKDF2-SHA256 with 600,000 iterations. The server can see sender identifiers, times, IVs, and ciphertext, but NOT the message plaintext. Anyone with the shared phrase and a copy of the ciphertext could decrypt it. The source code and login page may be public through GitHub Pages; the chat contents are not.

This is an early, unaudited personal app, not as secure as Signal: no forward secrecy or key rotation, and compromised devices or altered website code could expose the shared phrase. Do not put the phrase or any server secret keys in GitHub. If either person loses the phrase, existing messages cannot be recovered. A different phrase will make existing messages unreadable. Only the 250 latest messages are displayed initially; there is no push notification, media attachment, typing status, or read receipt yet.

## Verify database access

Run SELECT tablename, rowsecurity FROM pg_tables WHERE schemaname='public' AND tablename LIKE 'couple_%'; — all three must show true. Verify the enrolled membership list has exactly two IDs. Try accessing messages from a third account: it should receive zero rows and cannot insert. Test encrypted ciphertext by inspecting a database row; it must not contain plaintext. Run the Supabase database security advisor after setup.

GitHub stores the app code ONLY. Supabase stores the encrypted data. This app is not operational until the new project, two users, and Pages are configured.
