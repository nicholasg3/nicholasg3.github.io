#!/usr/bin/env python3
"""Write or update one staging article HTML file.

Usage:
  python3 scripts/write_staging_article.py --slug metric-authorship --title "..." --idea "..." ...
  Or import write_article() from a fleet runner.

Staging may include a "Seed tweet" line under the title for review.
When promoting to live, run scripts/promote_staging_article.py to strip that chrome.
"""
from __future__ import annotations

import argparse
import html
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGING_POSTS = ROOT / "blog" / "staging" / "posts"


def shell(title: str, idea: str, rank: int, slug: str, body_html: str, source: str = "", tweet: str = "") -> str:
    safe_title = html.escape(title)
    safe_idea = html.escape(idea)
    kicker = f"Staging draft · queue #{rank} · not live"
    tweet_line = ""
    if tweet:
        tweet_line = f'<p class="muted"><a href="{html.escape(tweet)}" rel="noopener noreferrer">Seed tweet</a> · source: {html.escape(source or "ideas queue")}</p>'
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="robots" content="noindex,nofollow,noarchive">
    <meta name="description" content="{safe_idea[:160]}">
    <title>{safe_title} | Staging</title>
    <link rel="stylesheet" href="../../styles.css">
  </head>
  <body>
    <header class="site-header">
      <a class="brand" href="../index.html" aria-label="Staging home">
        <span class="brand-mark">SP</span>
        <span>
          <strong>Staging</strong>
          <small>Private draft</small>
        </span>
      </a>
      <nav class="nav" aria-label="Primary">
        <a href="../index.html">Staging index</a>
        <a href="../../ideas-queue.html">Ideas queue</a>
      </nav>
    </header>

    <main class="article-main">
      <header class="article-header">
        <div class="issue-kicker">{html.escape(kicker)}</div>
        <h1>{safe_title}</h1>
        <p>{safe_idea}</p>
        {tweet_line}
      </header>

      <article class="article-body">
{body_html}
      </article>

      <aside class="article-side" aria-label="Staging notes">
        <section class="side-card">
          <span class="section-label">Staging</span>
          <strong>Not on the public catalogue.</strong>
          <p>Slug <code>{html.escape(slug)}</code>. Promote only after enrichment, free-style polish, and Nick sign-off.</p>
        </section>
      </aside>
    </main>

    <footer class="site-footer">
      <span>Staging draft</span>
      <a href="../index.html">Back to staging</a>
    </footer>
  </body>
</html>
"""


def write_article(slug: str, title: str, idea: str, rank: int, body_html: str, source: str = "", tweet: str = "") -> Path:
    STAGING_POSTS.mkdir(parents=True, exist_ok=True)
    path = STAGING_POSTS / f"{slug}.html"
    path.write_text(shell(title, idea, rank, slug, body_html, source, tweet))
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--idea", required=True)
    ap.add_argument("--rank", type=int, required=True)
    ap.add_argument("--body-file", required=True, help="HTML fragment for article body")
    ap.add_argument("--source", default="")
    ap.add_argument("--tweet", default="")
    args = ap.parse_args()
    body = Path(args.body_file).read_text()
    p = write_article(args.slug, args.title, args.idea, args.rank, body, args.source, args.tweet)
    print(p)


if __name__ == "__main__":
    main()
