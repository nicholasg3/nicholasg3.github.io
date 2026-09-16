/* Client-side deterrence gate. NOT cryptography.
   Page bodies are base64, not encrypted: anyone can decode them from the page
   source without the password. Keep sensitive material out of this site. */
(function () {
  var SALT = "6f8a2420041b6e50";
  var HASH = "e0a0b8660d4dd7487d95327931805eefa154cc245f8ccfb91e36f2f1b52dff27";
  var KEY = "portal-unlocked";

  function hex(buf) {
    return Array.prototype.map.call(new Uint8Array(buf), function (b) {
      return ("0" + b.toString(16)).slice(-2);
    }).join("");
  }

  function digest(pw) {
    if (!window.crypto || !window.crypto.subtle) {
      return Promise.reject(new Error("This browser needs HTTPS for the gate."));
    }
    var data = new TextEncoder().encode(SALT + ":" + pw);
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
    var t = host.getAttribute("data-title");
    if (t) { document.title = t; }
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
      '<p>Briefs, dashboards, decisions. Enter the password.</p>' +
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
          try { sessionStorage.setItem(KEY, "1"); } catch (e) {}
          reveal();
        } else {
          err.textContent = "Wrong password.";
        }
      }).catch(function (e) { err.textContent = e.message; });
    });
  }

  function start() {
    var unlocked = false;
    try { unlocked = sessionStorage.getItem(KEY) === "1"; } catch (e) {}
    if (unlocked) { reveal(); } else { mountGate(); }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else { start(); }
})();
