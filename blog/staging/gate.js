/* Staging gate — decrypts private drafts in the browser.
 *
 * GitHub Pages cannot authenticate anyone, so nothing here is a permission
 * check that could be bypassed by editing the DOM: the draft text is simply
 * not present until AES-GCM decrypts it. A wrong password fails the GCM auth
 * tag and produces nothing.
 *
 * The derived key lives in sessionStorage so unlocking the index also opens
 * the drafts for that tab session. It clears when the tab closes, or on Lock.
 */
window.stagingGate = (function () {
  "use strict";

  const SESSION_KEY = "sp-staging-key-v2";
  const IV_BYTES = 12;

  function b64ToBytes(b64) {
    const bin = atob(b64.replace(/\s+/g, ""));
    const out = new Uint8Array(bin.length);
    for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
    return out;
  }

  function bytesToB64(bytes) {
    let bin = "";
    for (const b of new Uint8Array(bytes)) bin += String.fromCharCode(b);
    return btoa(bin);
  }

  function requireSecureContext() {
    if (!window.isSecureContext || !window.crypto || !crypto.subtle) {
      throw new Error(
        "Encrypted staging needs a secure context. Use https:// or " +
        "http://localhost (python3 -m http.server), not file://."
      );
    }
  }

  async function fetchLock(lockUrl) {
    const res = await fetch(lockUrl + "?t=" + Date.now(), { cache: "no-store" });
    if (!res.ok) throw new Error("Could not load " + lockUrl);
    return res.json();
  }

  async function deriveKey(password, lock) {
    requireSecureContext();
    const kdf = lock.kdf;
    const base = await crypto.subtle.importKey(
      "raw", new TextEncoder().encode(password), "PBKDF2", false, ["deriveKey"]
    );
    return crypto.subtle.deriveKey(
      {
        name: "PBKDF2",
        salt: b64ToBytes(kdf.salt),
        iterations: kdf.iterations,
        hash: kdf.hash
      },
      base,
      { name: "AES-GCM", length: 256 },
      true,
      ["decrypt"]
    );
  }

  async function importSessionKey() {
    const stored = sessionStorage.getItem(SESSION_KEY);
    if (!stored) return null;
    try {
      return await crypto.subtle.importKey(
        "raw", b64ToBytes(stored), { name: "AES-GCM", length: 256 }, true, ["decrypt"]
      );
    } catch (_) {
      sessionStorage.removeItem(SESSION_KEY);
      return null;
    }
  }

  async function rememberKey(key) {
    const raw = await crypto.subtle.exportKey("raw", key);
    sessionStorage.setItem(SESSION_KEY, bytesToB64(raw));
  }

  function forgetKey() {
    sessionStorage.removeItem(SESSION_KEY);
  }

  /* Rejects on a wrong password: AES-GCM authentication fails. */
  async function decrypt(key, payloadB64) {
    const raw = b64ToBytes(payloadB64);
    const plain = await crypto.subtle.decrypt(
      { name: "AES-GCM", iv: raw.slice(0, IV_BYTES) }, key, raw.slice(IV_BYTES)
    );
    return new TextDecoder().decode(plain);
  }

  async function fetchAndDecrypt(key, url) {
    const res = await fetch(url + "?t=" + Date.now(), { cache: "no-store" });
    if (!res.ok) throw new Error("Could not load " + url);
    return decrypt(key, (await res.text()).trim());
  }

  /* Wires a password field to an unlock handler, with session reuse. */
  function wireGate({ lockUrl, onKey, onError }) {
    const input = document.getElementById("password");
    const button = document.getElementById("unlock-btn");
    const error = document.getElementById("gate-error");
    let lock = null;

    const fail = (message) => {
      if (error) error.textContent = message;
      if (onError) onError(message);
    };

    /* Resolves false only for a genuine decryption failure (wrong password).
     * Anything else — a missing file, bad JSON — is a real error worth showing,
     * so it propagates instead of being mislabelled as a bad password. */
    async function attempt(key) {
      try {
        await onKey(key);
        return true;
      } catch (e) {
        if (e && e.name === "OperationError") return false;
        throw e;
      }
    }

    async function unlock() {
      if (error) error.textContent = "";
      const password = input && input.value ? input.value : "";
      if (!password) return fail("Enter the staging password.");
      if (button) {
        button.disabled = true;
        button.textContent = "Unlocking…";
      }
      try {
        lock = lock || await fetchLock(lockUrl);
        const key = await deriveKey(password, lock);
        if (await attempt(key)) {
          await rememberKey(key);
        } else {
          fail("Wrong password.");
        }
      } catch (e) {
        fail(String((e && e.message) || e));
      } finally {
        if (button) {
          button.disabled = false;
          button.textContent = "Unlock";
        }
      }
    }

    if (button) button.addEventListener("click", unlock);
    if (input) {
      input.addEventListener("keydown", (e) => {
        if (e.key === "Enter") unlock();
      });
    }

    /* Try the key already derived earlier in this tab session. */
    (async () => {
      try {
        const key = await importSessionKey();
        if (key && !(await attempt(key))) forgetKey();
      } catch (_) {
        forgetKey();
      }
    })();
  }

  function whenLoaded() {
    if (document.readyState === "complete") return Promise.resolve();
    return new Promise((resolve) => window.addEventListener("load", resolve, { once: true }));
  }

  /* A single locked draft: decrypt the inline payload and become that page.
   *
   * The wait matters. Unlocking from a stored session key needs no PBKDF2, so
   * it can finish while the parser is still streaming this page — and
   * document.open() mid-parse interleaves with the markup still to come
   * instead of replacing it. Typing the password is slow enough to hide that;
   * arriving from the index is not. */
  function mountDraftPage({ lockUrl, payload }) {
    wireGate({
      lockUrl,
      onKey: async (key) => {
        const html = await decrypt(key, payload);
        await whenLoaded();
        document.open();
        document.write(html);
        document.close();
      }
    });
  }

  /* A page whose data lives in an encrypted JSON file next to it: the staging
   * index (manifest.enc) and the ideas queue (ideas-queue.enc). */
  function mountDataPage({ lockUrl, dataUrl, onData }) {
    wireGate({
      lockUrl,
      onKey: async (key) => onData(JSON.parse(await fetchAndDecrypt(key, dataUrl)))
    });
  }

  function mountIndexPage({ lockUrl, manifestUrl, onManifest }) {
    return mountDataPage({ lockUrl, dataUrl: manifestUrl, onData: onManifest });
  }

  return {
    mountDraftPage, mountDataPage, mountIndexPage,
    forgetKey, decrypt, deriveKey, fetchLock
  };
})();
