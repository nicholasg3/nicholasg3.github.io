/* Client-side deterrence gate. NOT cryptography.
   Page bodies below are base64, not encrypted: anyone can decode them from
   the page source without the password. Keep sensitive material out. */
(function () {
  var SALT = "383cfbefa289eb1f";
  var HASH = "d763ee35fd1bb9c33be63ba5c66adbb702ff9a9f3a4369e910ffe664c7037c4a";
  var KEY = "portal-unlocked-2026-09-16";

  function hex(buf) {
    return Array.prototype.map.call(new Uint8Array(buf), function (b) {
      return ("0" + b.toString(16)).slice(-2);
    }).join("");
  }

  function digest(pw) {
    var data = new TextEncoder().encode(SALT + ":" + pw);
    if (!window.crypto || !window.crypto.subtle) {
      return Promise.reject(new Error("This browser needs HTTPS for the gate."));
    }
    return window.crypto.subtle.digest("SHA-256", data).then(hex);
  }

  function reveal() {
    var node = document.getElementById("payload");
    var host = document.getElementById("content");
    if (!node || !host) { return; }
    var bytes = Uint8Array.from(atob(node.textContent.trim()), function (c) {
      return c.charCodeAt(0);
    });
    host.innerHTML = new TextDecoder("utf-8").decode(bytes);
    node.remove();
    document.documentElement.classList.remove("locked");
    var gate = document.getElementById("gate");
    if (gate) { gate.remove(); }
    document.title = host.getAttribute("data-title") || document.title;
    if (location.hash) {
      var target = document.getElementById(location.hash.slice(1));
      if (target) { target.scrollIntoView(); }
    }
  }

  function mountGate() {
    var gate = document.createElement("div");
    gate.id = "gate";
    gate.innerHTML =
      '<h1>Internal portal</h1>' +
      '<p>Program memos, reports, and dashboards. Enter the password.</p>' +
      '<form><input type="password" id="pw" autocomplete="current-password" ' +
      'autofocus placeholder="Password" aria-label="Password">' +
      '<button type="submit">Open</button></form>' +
      '<div class="err" id="err" role="status"></div>' +
      '<p class="fine">Obfuscation, not encryption. This is a public host: ' +
      'treat everything here as disclosable.</p>';
    document.body.appendChild(gate);
    gate.querySelector("form").addEventListener("submit", function (ev) {
      ev.preventDefault();
      var err = document.getElementById("err");
      err.textContent = "";
      digest(document.getElementById("pw").value).then(function (got) {
        if (got === HASH) {
          try { sessionStorage.setItem(KEY, "1"); } catch (e) { /* private mode */ }
          reveal();
        } else {
          err.textContent = "Wrong password.";
          document.getElementById("pw").select();
        }
      }).catch(function (e) { err.textContent = e.message; });
    });
  }

  function start() {
    var ok = false;
    try { ok = sessionStorage.getItem(KEY) === "1"; } catch (e) { ok = false; }
    if (ok) { reveal(); } else { mountGate(); }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();
