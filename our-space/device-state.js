// Optional trusted-device persistence. The shared phrase is never stored.
// Web Crypto non-extractable AES-GCM CryptoKeys can be cloned into IndexedDB.
// IMPORTANT: same-origin JavaScript can still USE the key. This is a convenience
// feature for personal, screen-locked phones, not hardware-bound protection.
const DB = "our-space-device-v1";
const STORE = "unlocks";

function run(mode, operation) {
  return new Promise((resolve, reject) => {
    if (!("indexedDB" in globalThis)) return reject(new Error("This browser has no device storage."));
    const open = indexedDB.open(DB, 1);
    open.onupgradeneeded = () => open.result.createObjectStore(STORE, { keyPath: "id" });
    open.onblocked = () => reject(new Error("Local device storage is busy."));
    open.onerror = () => reject(open.error || new Error("Could not open device storage."));
    open.onsuccess = () => {
      const db = open.result;
      let response;
      let value;
      try {
        const tx = db.transaction(STORE, mode);
        tx.oncomplete = () => { db.close(); resolve(value); };
        tx.onerror = () => { db.close(); reject(tx.error || new Error("Local storage failed.")); };
        tx.onabort = () => { db.close(); reject(tx.error || new Error("Local storage was canceled.")); };
        response = operation(tx.objectStore(STORE));
        response.onsuccess = () => { value = response.result; };
      } catch (error) { db.close(); reject(error); }
    };
  });
}

function id(project, user) { return project + "::" + user; }

export async function saveDeviceKey(project, user, salt, key) {
  if (!key || key.extractable !== false || key.algorithm?.name !== "AES-GCM")
    throw new Error("Cannot store an unsafe encryption key.");
  await run("readwrite", store => store.put({
    id: id(project, user), salt, cryptoKey: key, created: Date.now()
  }));
}

export async function getDeviceKey(project, user, salt) {
  const value = await run("readonly", store => store.get(id(project, user)));
  if (!value) return null;
  if (value.salt !== salt || value.cryptoKey?.type !== "secret" ||
      value.cryptoKey?.extractable !== false ||
      value.cryptoKey?.algorithm?.name !== "AES-GCM") {
    await forgetDeviceKey(project, user);
    return null;
  }
  return value.cryptoKey;
}

export async function forgetDeviceKey(project, user) {
  await run("readwrite", store => store.delete(id(project, user)));
}
