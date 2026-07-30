#!/usr/bin/env python3
"""Promote a staging draft to a professional live blog post.

Strips staging-only chrome that is useful in private review but wrong in public:
  - "Seed tweet" lines under the title
  - Staging kickers ("Staging draft · queue #N · not live")
  - Staging side-cards / "not on public catalogue" asides
  - "reposted by @yahoolovesyou" lab notes in Source notes labels
  - noindex robots meta (optional: keep if --keep-noindex)

Does NOT delete legitimate primary sources in Source notes that happen to be
tweet URLs if they are real evidence — but rewrites "Seed tweet (...)" labels
to professional labels (e.g. "Discourse source (X post by @handle)").

Usage:
  python3 scripts/promote_staging_article.py \\
    --from blog/staging/posts/metric-authorship.html \\
    --to blog/posts/metric-authorship-ai-coding.html \\
    --kicker "Public memo" \\
    --dry-run
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path


def promote(html: str, *, kicker: str, keep_noindex: bool) -> str:
    # Remove seed-tweet subtitle lines in header
    html = re.sub(
        r'\s*<p[^>]*>\s*<a[^>]*>\s*Seed tweet\s*</a>[^<]*</p>\s*',
        "\n",
        html,
        flags=re.I,
    )
    html = re.sub(
        r'\s*<p class="muted"[^>]*>\s*<a[^>]*>\s*Seed tweet\s*</a>[^<]*</p>\s*',
        "\n",
        html,
        flags=re.I,
    )

    # Professional kicker
    html = re.sub(
        r'(<div class="issue-kicker">)(.*?)(</div>)',
        rf"\1{kicker}\3",
        html,
        count=1,
        flags=re.S,
    )

    # robots
    if not keep_noindex:
        html = re.sub(
            r'\s*<meta name="robots" content="noindex[^"]*"\s*/?>\s*',
            "\n    ",
            html,
            flags=re.I,
        )

    # staging footers / side cards
    html = re.sub(
        r'<span>Staging draft</span>',
        "<span>Strategy Publisher</span>",
        html,
        flags=re.I,
    )
    html = re.sub(
        r'<span>Private staging</span>',
        "<span>Strategy Publisher</span>",
        html,
        flags=re.I,
    )
    html = re.sub(
        r'<span>Staging</span>\s*<strong>Not on the public catalogue\.</strong>[\s\S]*?</section>',
        "",
        html,
        count=1,
    )
    # softer: rewrite staging side card content if present
    html = re.sub(
        r'(<span class="section-label">)Staging(</span>\s*<strong>)[^<]*(</strong>\s*<p>)[^<]*(</p>)',
        r"\1Note\2Public memo.\3\4",
        html,
        count=1,
    )

    # Source notes: rewrite "Seed tweet (...)" list labels
    def fix_seed_li(m: re.Match) -> str:
        inner = m.group(0)
        inner = re.sub(
            r">Seed tweet\s*\(([^)]+)\)(?:,\s*reposted by @[^<]+)?<",
            r">Discourse source (\1)<",
            inner,
            flags=re.I,
        )
        inner = re.sub(
            r">Seed tweet<",
            r">Discourse source (X)<",
            inner,
            flags=re.I,
        )
        # drop yahoolovesyou lab parentheticals
        inner = re.sub(r",\s*reposted by @yahoolovesyou", "", inner, flags=re.I)
        return inner

    html = re.sub(r"<li>[\s\S]*?</li>", fix_seed_li, html)

    # brand links that point to staging hub -> blog
    html = html.replace('href="../index.html"', 'href="../index.html"')  # ok if already blog
    html = re.sub(
        r'<a href="\.\./">Hub</a>',
        '<a href="../index.html">Blog</a>',
        html,
    )
    html = re.sub(
        r'<strong>Staging</strong>\s*<small>Private draft</small>',
        "<strong>Blog</strong><small>AI Strategy briefing</small>",
        html,
        flags=re.S,
    )
    html = re.sub(
        r'<title>(.*?) \| Staging</title>',
        r"<title>\1 | Blog</title>",
        html,
    )
    html = re.sub(
        r'<title>(.*?) \| [^<]*staging</title>',
        r"<title>\1 | Blog</title>",
        html,
        flags=re.I,
    )

    # styles path: staging posts often use ../../styles.css or ../styles.css
    # leave as-is if already correct for destination; caller may fix

    # nav / brand leftovers
    html = re.sub(
        r'aria-label="Staging home"',
        'aria-label="Blog home"',
        html,
        flags=re.I,
    )
    html = re.sub(
        r'<a href="[^"]*">Staging index</a>',
        '<a href="../index.html">Blog</a>',
        html,
        flags=re.I,
    )
    html = re.sub(
        r'<a href="[^"]*ideas-queue\.html">Ideas queue</a>\s*',
        '',
        html,
        flags=re.I,
    )
    html = re.sub(
        r'<a href="[^"]*">Back to staging</a>',
        '<a href="../index.html">Back to index</a>',
        html,
        flags=re.I,
    )
    html = re.sub(
        r'Private draft|private staging|Staging draft',
        'Strategy Publisher',
        html,
        flags=re.I,
    )

    html = re.sub(r"\n{3,}", "\n\n", html)
    return html


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="src", required=True)
    ap.add_argument("--to", dest="dst", required=True)
    ap.add_argument("--kicker", default="Public memo")
    ap.add_argument("--keep-noindex", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--styles", default="../styles.css", help="stylesheet href for live post")
    args = ap.parse_args()

    src = Path(args.src)
    raw = src.read_text()
    out = promote(raw, kicker=args.kicker, keep_noindex=args.keep_noindex)
    out = re.sub(
        r'href="[^"]*styles\.css"',
        f'href="{args.styles}"',
        out,
        count=1,
    )

    # sanity checks
    problems = []
    if re.search(r"Seed tweet", out, re.I):
        problems.append("still contains 'Seed tweet'")
    if re.search(r"queue #\d+", out, re.I):
        problems.append("still contains queue #")
    if re.search(r"not live|not public|not on the public catalogue", out, re.I):
        problems.append("still contains staging privacy wording")
    if problems and not args.dry_run:
        print("WARN:", "; ".join(problems))

    if args.dry_run:
        print(out[:1500])
        print("...")
        print("problems:", problems or "none")
        return

    dst = Path(args.dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(out)
    print(f"wrote {dst}")
    if problems:
        print("WARN after write:", "; ".join(problems))


if __name__ == "__main__":
    main()
