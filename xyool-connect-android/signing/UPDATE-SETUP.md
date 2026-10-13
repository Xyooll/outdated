# Xyool Connect: Updates Without Uninstalling

## What changed

The app identity is now **frozen** to `org.xyool.connect.crossnetworkalpha` (the package used by v0.7). The first permanently signed update will be v0.8.0, Android `versionCode 9`. Every future update must use this *exact* package and the *same signing certificate* while increasing `versionCode` (10, 11, ...). That lets Android show **Update** instead of forcing Uninstall.

Every previous alpha APK was signed with disposable GitHub Actions debug keys and several versions changed package IDs, so those old signatures can **never** be updated in-place by a new stable-signed APK. **One final uninstall of the exact previous v0.7 app will be needed to install v0.8.** Uninstalling v0.7 erases its app-private Xyool ID/authentication secret; it cannot be recovered from a *public* ID alone. Keep the old app until the first signed build is available and note your old contact information.

## One-time setup (GitHub on Android)

1. Download the private `XYOOL_SIGNING_PASSPHRASE.txt` from your ChatGPT conversation and keep it safe. Treat it like an account recovery key. **Never put its value in a public GitHub file, issue, or chat.**
2. Sign into GitHub on your phone and open `https://github.com/Xyooll/outdated/settings/secrets/actions`. Choose **New repository secret**.
3. Secret name: `XYOOL_SIGNING_PASSPHRASE`. Value: paste the entire single-line value under **Secret value** in your downloaded private TXT. Save.
4. Open `https://github.com/Xyooll/outdated/actions/workflows/xyool-release-android.yml`, choose **Run workflow** from the **main** branch.
5. When the job succeeds, open its `xyool-stable-signed-release-apk` artifact, download the ZIP, extract `app-release.apk`, and install it. **The first time only** Android may require uninstalling the existing v0.7 because its old debug certificate differs.
6. After that, no deleting: every new signed APK produced by the release workflow upgrades this same application and preserves the private preferences/ID and contacts. Always install the **stable signed release** artifacts, not the debug/test APKs.

The repository contains an encrypted backup of the keystore at `xyool-connect-android/signing/xyool-stable.p12.enc.b64` and a public fingerprint at `xyool-connect-android/signing/CERTIFICATE_FINGERPRINT.txt`. Only the private Github Actions secret can decrypt the key. The build verifies the certificate fingerprint and fails if it changed.

## Automatic build pipeline

After the one-time secret is set, changes to Android app source on the main branch trigger `Build Xyool Stable Android Updates`. Manual runs are supported as well. Each app update must increment `versionCode` before building. Don't change applicationId, release keystore, key alias, or password. **If the signing secret is lost, the encrypted key in the repo becomes unrecoverable and future updates will break.** Keep a securely stored recovery copy of the secret.

There is not yet an in-app auto-download / automatic installation mechanism. You still need to **download and tap Install** on the next APK, but Android will say **Update**, not require deleting the existing app. Android may prompt before installs from outside the Play Store; the user must approve installation.

## Security

The unencrypted private key is never checked into GitHub. Encryption uses AES-256-CBC with PBKDF2 (300,000 iterations) and a high-entropy private passphrase. The Android certificate SHA-256 fingerprint is pinned in the release workflow. Restrict access to your GitHub repo secrets and workflow write permissions. Public-source repositories can expose any secrets that untrusted code obtains in an authorized workflow, so only run trusted main-branch code.

The v0.8 app remains an experimental network calling beta; permanent signing does not itself add verified E2EE, reliable background ringing, ID recovery, or guaranteed cross-network connectivity.
