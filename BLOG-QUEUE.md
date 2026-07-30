# Blog queue & plan (nicholasg3.github.io)

Last updated: 2026-07-31

Tracking for open writing work. Site deploys from `master` (GitHub Pages).
Issues for this site live on `nicholasg3/ai-agents-workspace` (this repo has issues disabled).

## Private live ideas database

- **Page (password-gated):** https://nicholasg3.github.io/blog/ideas-queue.html
- **Default password:** `nick-blog-queue` (change hash in `blog/ideas-queue.html`)
- **Data:** `blog/data/ideas-queue.json` (rebuilt by `scripts/build_ideas_queue.py`)
- **Auto-update:** `.github/workflows/ideas-queue.yml` daily + on builder changes
- Optional secret `WORKSPACE_REPO_TOKEN` (read access to `ai-agents-workspace`) attaches enriched/analyzed paths from the retweet library

GitHub Pages has no real server auth. This is a client-side password gate for an internal backlog, not high-security secrets.


## Process (per post)

1. Pick seed from shortlist / active seeds
2. Ground (who argues it, primary sources, theory)
3. Particular thesis
4. **Grok default-voice** draft/rewrite (`humanify` skill = detect + free rewrite)
5. Offline detector (diagnostic)
6. Optional droplet adversary panel
7. Nick sign-off
8. Remove draft label → catalogue as final → push

Canonical skills: `skill-library/creative/humanify`, `blog-review`.

## Active drafts on this repo

| File | Title | Status | Next |
|------|-------|--------|------|
| `blog/posts/metric-authorship-ai-coding.html` | If success means task completion, the score may track who defines the task | **Draft on GH** (catalogue card marked Draft; `noindex`) | Enrich evidence; real study citation if public; free-style Grok pass; Nick sign-off |

## Seed queue (from shortlist 2026-07-21 / handoff 2026-07-22)

Priority order:

| Pri | Shortlist # | Focus | Status |
|-----|-------------|-------|--------|
| 1 | **#4** Metric-authorship paradox | Completion metrics reward who defines “done” | Draft HTML on GH; needs enrichment |
| 2 | **#1** Expertise → environment | Performance migrates into harness/folder config | Queued — no draft |
| 3 | **#6** Sovereignty without self-sufficiency | State “sovereignty” via VC amid interdependence | Queued |
| 4 | **#8** AI unit economics | Load-bearing vs propped usage | Queued |
| 5 | **#9** Discovered bias | Opacity vs reform when bias is admitted | Queued |

Source docs (workspace / strategic-publishing):

- `signals/retweet-library/digests/blog-shortlist-2026-07-21.md`
- `signals/retweet-library/digests/blog-seeds-active-2026-07-22.md`
- Handoffs: `ai-agents-workspace/HANDOFF-blog-humanify-and-seeds-2026-07-22.md`

## Other open site work (GH issues on ai-agents-workspace)

- **#127** Cron: retweet-library → humanified blog post (human-gated drafts) — blocked on seed quality practice
- **#128** Photos / Projects page
- **#138** Shorts pipeline from blog/teaching content
- Teaching series: workflow primer Part 2+ when outlines exist

## Recently done (2026-07-30)

- Sitewide default-Grok prose rewrite
- Plain-English titles (drop ledger/boundary costume)
- Table/section label cleanup
- `humanify` skill = detect + default Grok rewrite (no doctrine checklist)

## Definition of done (draft → final)

- [ ] Particular claim still clear after enrichment
- [ ] Sources are primary where possible (not only retweet dossier)
- [ ] Free-style Grok rewrite (not choppy checklist prose)
- [ ] Detector residual acceptable
- [ ] Nick sign-off
- [ ] Remove `noindex` + Draft catalogue label
- [ ] Live on Pages without “Draft” kicker
