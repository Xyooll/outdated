# Our Space — private chat for two

## Current installation status

- [x] App is committed to GitHub and published by the successful GitHub Pages deployment.
- [x] Dedicated **Our Space** Supabase project created under **Xyool Org** (US East).
- [x] Project URL and browser-safe publishable key configured in `config.js`.
- [x] Encrypted-message tables created; Row Level Security enabled on all three chat tables.
- [x] Private member and message access policies verified.
- [x] Realtime database events enabled.
- [x] Encrypted first-phone phrase verifier added so subsequent unlocks reject the wrong phrase.
- [ ] Configure Authentication redirect URL (owner's Supabase dashboard).
- [ ] Invite exactly two email accounts (owner's Supabase dashboard).
- [x] Enrolled two confirmed accounts into `public.couple_members` (one account per role; no email addresses stored in GitHub).
- [ ] Verify actual messaging between both phones.

## Finish setup from your phone

**1. Open Authentication URL Configuration**

https://supabase.com/dashboard/project/vtlqpgmipfhdjiidssxg/auth/url-configuration

Set the **Site URL** to:

https://xyooll.github.io/outdated/our-space/

Add the exact same URL to the **Redirect URLs** list and save.

**2. Invite exactly two users**

https://supabase.com/dashboard/project/vtlqpgmipfhdjiidssxg/auth/users

Under **Authentication → Users**, use **Invite user** for each of your two real email addresses. Only invite those two people. Verify the users appear in the list. You can keep your email addresses private: there is no need to paste them in your public GitHub source code.

Disable public signups after the two are invited (Authentication sign-in settings). Do not confuse this with Row Level Security; RLS is already enabled and is enforced even if signups were open.

**3. Accounts enrolled**

Completed: the two confirmed accounts have been assigned `person_one` and `person_two`. No additional enrollment is needed.

For reference, enrollment is equivalent to:

```sql
INSERT INTO public.couple_members(user_id,role)
SELECT id,'person_one' FROM auth.users
WHERE lower(email)=lower('EMAIL_ONE');

INSERT INTO public.couple_members(user_id,role)
SELECT id,'person_two' FROM auth.users
WHERE lower(email)=lower('EMAIL_TWO');
```

**4. Open your app**

https://xyooll.github.io/outdated/our-space/

Each person signs in using the invited email and their account password (recommended), then enters the **same unique, strong encryption phrase**. A one-time email link remains available as an alternative. If an email link redirects back to login, do not reuse that link; it may be expired, consumed, or open in a separate browser session. Use password login in the same Chrome tab or installed PWA to avoid this loop. The first unlocked phone sets the encrypted phrase verifier, so the other phone must use the same phrase. Exchange the phrase in person.

On Android Chrome: menu (⋮) → **Add to Home screen** / **Install app**.

## Security and limitations

- Supabase Auth identifies each person using email-link login.
- Access to the private conversation is restricted by database Row Level Security to the **two manually enrolled auth user IDs**.
- The browser encrypts messages with AES-256-GCM before upload, using PBKDF2-SHA256 (600,000 iterations) on the shared phrase. The phrase and derived key remain in browser memory; they are not uploaded or saved in GitHub.
- The server sees message timestamps, sender IDs, IVs, and ciphertext, but not plaintext.
- A separate encrypted verifier helps detect wrong phrases; choose at least six randomly selected words and keep them private. **Losing the phrase makes old messages unrecoverable.**
- **This is an unaudited first version, not a Signal replacement.** It has no forward secrecy, no independent identity verification, no media attachments or push notifications, and no offline send. A compromised device, malicious browser code, or someone who learns the phrase can expose messages.
- The latest 250 messages are shown. Github Pages hosts public application code and login UI, not the contents of private messages.
- Service-role/secret Supabase API keys must NEVER appear in web client files.

**Data project:** https://supabase.com/dashboard/project/vtlqpgmipfhdjiidssxg

**Code:** https://github.com/Xyooll/outdated/tree/main/our-space

## Login-loop correction

On 2026-10-11, Supabase Auth logs showed invalid/consumed one-time verification links and temporary email rate limiting. The app now offers direct email + password sign-in, an optional email-link fallback, and visible redirect errors. Email-account passwords and the shared end-to-end encryption phrase are **different** secrets. No passwords should be added to GitHub, shared in chat, or placed in config.js.
