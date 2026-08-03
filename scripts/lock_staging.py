#!/usr/bin/env python3
"""Encrypt plaintext staging drafts into password-locked pages for GitHub Pages.

GitHub Pages has no server-side auth, so a gate that merely hides markup is
decorative: anyone who guesses the URL reads the draft. This script instead
encrypts each draft, so the bytes served by Pages are useless without the
password.

  plaintext source (private repo)  ->  AES-256-GCM  ->  locked page (this repo)

Crypto:
  key         PBKDF2-HMAC-SHA256, 310,000 iterations, 32 bytes
  salt        one per site build, published in blog/staging/lock.json
  cipher      AES-256-GCM, fresh 12-byte IV per file, 16-byte tag
  payload     base64(iv || ciphertext || tag)

The salt is shared across the build on purpose: the browser derives the key
once at unlock and reuses it for every draft in the session. A per-file salt
would force a 310k-iteration derivation on every page open. Salt is not a
secret; it defeats precomputed tables, which one site-wide value already does.

The IV is per file and random. Reusing an IV under one key breaks GCM, so
every run re-encrypts everything with fresh IVs.

No password hash is published. Verification is the GCM auth tag: a wrong
password fails to decrypt. That leaves nothing cheaper to attack offline than
the ciphertext itself.

The source root is a directory in the private repo:

  blog-staging/
    src/<slug>.html      drafts, one per staged article
    ideas-queue.json     the idea backlog behind blog/ideas-queue.html

Both are encrypted with the same key, so one unlock opens the whole private
side of the site for that browser session.

Usage:
  export STAGING_PASSWORD='...'          # or omit to be prompted
  python3 scripts/lock_staging.py --src ../ai-agents-workspace/blog-staging
  python3 scripts/lock_staging.py --src <dir> --check    # verify, write nothing
"""
from __future__ import annotations

import argparse
import base64
import getpass
import hashlib
import json
import os
import secrets
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
except ImportError:  # pragma: no cover - dependency hint
    sys.exit("Missing dependency: pip install cryptography")

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / "blog" / "staging"
LOCKED_POSTS = STAGING / "posts"
LOCK_META = STAGING / "lock.json"
MANIFEST_ENC = STAGING / "manifest.enc"
IDEAS_ENC = ROOT / "blog" / "data" / "ideas-queue.enc"
IDEAS_PLAIN = ROOT / "blog" / "data" / "ideas-queue.json"

PBKDF2_ITERATIONS = 310_000
KEY_BYTES = 32
SALT_BYTES = 16
IV_BYTES = 12

LOCKED_PAGE = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="robots" content="noindex,nofollow,noarchive">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Locked draft | Staging</title>
    <link rel="stylesheet" href="../../styles.css">
    <link rel="stylesheet" href="../gate.css">
  </head>
  <body>
    <main class="gate-main">
      <section class="gate-card">
        <h1>Locked draft</h1>
        <p class="muted">This is an unfinished draft. It is encrypted; the
          password decrypts it in your browser.</p>
        <label for="password">Password</label>
        <input id="password" type="password" autocomplete="current-password" autofocus>
        <button type="button" id="unlock-btn">Unlock</button>
        <p class="gate-error" id="gate-error" role="alert"></p>
        <p class="muted"><a href="../index.html">Back to staging index</a></p>
      </section>
    </main>
    <script id="payload" type="application/octet-stream">__PAYLOAD__</script>
    <script src="../gate.js"></script>
    <script>
      stagingGate.mountDraftPage({
        lockUrl: "../lock.json",
        payload: document.getElementById("payload").textContent.trim()
      });
    </script>
  </body>
</html>
"""


def b64(raw: bytes) -> str:
    return base64.b64encode(raw).decode("ascii")


def derive_key(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt,
                               PBKDF2_ITERATIONS, dklen=KEY_BYTES)


def encrypt(key: bytes, plaintext: bytes) -> str:
    iv = secrets.token_bytes(IV_BYTES)
    return b64(iv + AESGCM(key).encrypt(iv, plaintext, None))


def decrypt(key: bytes, payload: str) -> bytes:
    raw = base64.b64decode(payload)
    return AESGCM(key).decrypt(raw[:IV_BYTES], raw[IV_BYTES:], None)


def read_password() -> str:
    password = os.environ.get("STAGING_PASSWORD") or getpass.getpass("Staging password: ")
    if len(password) < 12:
        sys.exit(
            "Refusing to build: staging password is under 12 characters.\n"
            "The ciphertext is public, so a short password is guessable offline.\n"
            "Use a long random passphrase and store it in your password manager."
        )
    return password


def build_manifest(sources: list[Path]) -> dict:
    """Carry forward per-slug metadata from the previous manifest where possible."""
    previous = {}
    old = STAGING / "manifest.json"
    if old.exists():
        for article in json.loads(old.read_text()).get("articles", []):
            previous[article.get("slug")] = article

    articles = []
    for index, path in enumerate(sorted(sources), start=1):
        slug = path.stem
        entry = dict(previous.get(slug, {}))
        entry.setdefault("rank", index)
        entry.setdefault("slug", slug)
        entry.setdefault("id", slug)
        entry.setdefault("title", slug.replace("-", " ").capitalize())
        entry.setdefault("idea", "")
        entry.setdefault("source", "")
        entry.setdefault("status", "draft")
        entry["path"] = f"posts/{slug}.html"
        articles.append(entry)

    articles.sort(key=lambda a: a.get("rank") or 9_999)
    return {
        "version": 2,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "count": len(articles),
        "articles": articles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--src", required=True,
                        help="private staging root: <src>/src/*.html drafts and <src>/ideas-queue.json")
    parser.add_argument("--check", action="store_true",
                        help="decrypt what is already published and verify it round-trips; write nothing")
    args = parser.parse_args()

    root = Path(args.src).expanduser().resolve()
    if not root.is_dir():
        sys.exit(f"Source directory not found: {root}")

    src = root / "src"
    if not src.is_dir():
        sys.exit(f"Expected draft sources in {src}")

    sources = sorted(src.glob("*.html"))
    if not sources:
        sys.exit(f"No .html drafts in {src}")

    ideas = root / "ideas-queue.json"

    password = read_password()

    if args.check:
        if not LOCK_META.exists():
            sys.exit("Nothing published yet: blog/staging/lock.json is missing.")
        meta = json.loads(LOCK_META.read_text())
        key = derive_key(password, base64.b64decode(meta["kdf"]["salt"]))
        try:
            decrypt(key, MANIFEST_ENC.read_text().strip())
        except Exception:
            sys.exit("Wrong password: the manifest did not decrypt.")
        failures = []
        if IDEAS_PLAIN.exists():
            failures.append("blog/data/ideas-queue.json is published in plaintext")
        if IDEAS_ENC.exists():
            try:
                decrypt(key, IDEAS_ENC.read_text().strip())
            except Exception:
                failures.append("blog/data/ideas-queue.enc did not decrypt")
        for path in sorted(LOCKED_POSTS.glob("*.html")):
            html = path.read_text()
            start = html.find('type="application/octet-stream">')
            if start == -1:
                failures.append(f"{path.name}: no payload (is it still plaintext?)")
                continue
            start += len('type="application/octet-stream">')
            payload = html[start:html.find("</script>", start)].strip()
            try:
                decrypt(key, payload)
            except Exception:
                failures.append(f"{path.name}: payload did not decrypt")
        for line in failures:
            print("FAIL", line)
        print(f"checked {len(list(LOCKED_POSTS.glob('*.html')))} locked pages, {len(failures)} failure(s)")
        return 1 if failures else 0

    salt = secrets.token_bytes(SALT_BYTES)
    key = derive_key(password, salt)

    LOCKED_POSTS.mkdir(parents=True, exist_ok=True)
    for stale in LOCKED_POSTS.glob("*.html"):
        stale.unlink()

    for path in sources:
        payload = encrypt(key, path.read_bytes())
        (LOCKED_POSTS / f"{path.stem}.html").write_text(
            LOCKED_PAGE.replace("__PAYLOAD__", payload)
        )

    manifest = build_manifest(sources)
    MANIFEST_ENC.write_text(encrypt(key, json.dumps(manifest).encode("utf-8")) + "\n")

    # The plaintext manifest listed every unfinished slug to anyone who asked.
    stale_manifest = STAGING / "manifest.json"
    if stale_manifest.exists():
        stale_manifest.unlink()

    # Same leak, different file: the idea backlog names every unwritten piece.
    if ideas.exists():
        IDEAS_ENC.write_text(encrypt(key, ideas.read_bytes()) + "\n")
        if IDEAS_PLAIN.exists():
            IDEAS_PLAIN.unlink()
    elif IDEAS_PLAIN.exists():
        sys.exit(
            f"Refusing to leave {IDEAS_PLAIN.relative_to(ROOT)} published in plaintext.\n"
            f"Move it to {ideas} first."
        )

    LOCK_META.write_text(json.dumps({
        "version": 2,
        "generated_at": manifest["generated_at"],
        "count": manifest["count"],
        "kdf": {
            "name": "PBKDF2",
            "hash": "SHA-256",
            "iterations": PBKDF2_ITERATIONS,
            "salt": b64(salt),
        },
        "cipher": "AES-GCM-256",
    }, indent=2) + "\n")

    print(f"locked {len(sources)} drafts from {src}")
    print(f"  -> {LOCKED_POSTS.relative_to(ROOT)}/*.html")
    print(f"  -> {MANIFEST_ENC.relative_to(ROOT)}")
    if ideas.exists():
        print(f"  -> {IDEAS_ENC.relative_to(ROOT)}")
    print(f"  -> {LOCK_META.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
