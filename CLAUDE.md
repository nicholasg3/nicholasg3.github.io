# nicholasg3.github.io — agent rules

## The one hard rule
**Everything pushed to this repo is LIVE immediately.** GitHub Pages has no
server-side staging. There is no such thing as an "on-repo draft", a
"noindex draft", or a "draft catalogue card" in `blog/posts/` — a visitor
with the URL sees it, and the catalogue links make the URL public.
(This rule exists because exactly that happened on 2026-07-30 with
metric-authorship; Nick had to order an emergency takedown.)

- Drafts go to `blog/staging/posts/` ONLY (client-side password gate,
  unlisted, noindex). Register them in `blog/staging/manifest.json`.
- Promotion to `blog/posts/` + catalogue happens ONLY after Nick's explicit
  sign-off, via `scripts/promote_staging_article.py`.
- CI (`.github/workflows/draft-guard.yml`) fails any push that puts a
  noindex file in `blog/posts/` or a Draft card in `blog/index.html`.
  Do not weaken the guard; fix the content location instead.

## Titles
No vague-but-grand titles ("If success means X, the score may track Y").
A title states its concrete claim in plain words. Test: could a stranger
guess the post's content from the title alone?

## Process
See `PLAN.md` (session source of truth) and `BLOG-QUEUE.md` (queue tables).
Skills: `blog-review` (grounding + AI-style detector gate), `humanify`.
