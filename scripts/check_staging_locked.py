#!/usr/bin/env python3
"""Fail if anything private is about to be served in the clear.

Everything under blog/ is published by GitHub Pages the moment it is pushed,
with no way to take it back for anyone who already fetched it. This check is
the backstop for the one mistake that matters: committing an unfinished draft,
or the backlog that names them, as readable bytes.

It needs no password, so CI and a pre-commit hook can both run it:

    python3 scripts/check_staging_locked.py
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / "blog" / "staging"
LOCKED_POSTS = STAGING / "posts"

# Markup that only ever appears in a real draft, never in the locked shell.
PLAINTEXT_TELLS = (
    "article-body",
    "source-notes",
    "issue-kicker",
    "site-footer",
)

MUST_NOT_EXIST = (
    ROOT / "blog" / "data" / "ideas-queue.json",
    STAGING / "manifest.json",
)


def main() -> int:
    problems: list[str] = []

    for path in MUST_NOT_EXIST:
        if path.exists():
            problems.append(
                f"{path.relative_to(ROOT)} is plaintext in a published directory. "
                f"Move it to the private staging source and re-run lock_staging.py."
            )

    if not (STAGING / "lock.json").exists():
        problems.append("blog/staging/lock.json is missing — staging was never locked.")
    if not (STAGING / "manifest.enc").exists():
        problems.append("blog/staging/manifest.enc is missing — staging was never locked.")

    pages = sorted(LOCKED_POSTS.glob("*.html"))
    if not pages:
        problems.append("blog/staging/posts/ has no pages at all.")

    for page in pages:
        html = page.read_text(errors="replace")
        name = page.relative_to(ROOT)
        if 'id="payload"' not in html:
            problems.append(f"{name} has no encrypted payload — is it still a plaintext draft?")
        found = [tell for tell in PLAINTEXT_TELLS if tell in html]
        if found:
            problems.append(f"{name} contains draft markup in the clear: {', '.join(found)}")

    for problem in problems:
        print(f"FAIL  {problem}")

    if problems:
        print(f"\n{len(problems)} problem(s). Nothing unfinished may be published in the clear.")
        return 1

    print(f"ok — {len(pages)} staging pages locked, no plaintext drafts or backlog published")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
