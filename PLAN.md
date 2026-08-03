# Running plan — nicholasg3.github.io

**This is the living project plan.** Update it at the end of every session that changes the site, the queue, or the process.

| Field | Value |
|-------|--------|
| **Last updated** | 2026-08-03 ~16:40 SGT |
| **Last commit focus** | Unpublished the unfinished draft; encrypted staging at rest |
| **Owner** | Nick + agents |
| **Deploy** | Push to `master` → GitHub Pages |
| **Issues** | Repo has issues **disabled** — track durable work on `nicholasg3/ai-agents-workspace` |

---

## How to maintain this document

After any real work on this repo, an agent must:

1. Update **Last session** (what we did, what we skipped, what broke).
2. Update **Now / next** (ordered; one primary next action first).
3. Update **Open work tables** (status columns only — do not invent new queues without Nick).
4. Bump **Last updated**.
5. Commit `PLAN.md` with the related code/content change when possible.

Do **not** treat handoffs in `ai-agents-workspace` as fresher than this file when they conflict — **this file wins for site work**, then correct the handoff if needed.

---

## Last session (2026-07-30 → 2026-07-31)

### Done

| Item | Notes |
|------|--------|
| Live prose rewrite (default Grok voice) | Sitewide pass on public posts; tables left intact |
| Plain-English titles | Dropped costume words (ledger/boundary/packet/etc.); URLs kept stable |
| Cross-reference cleanup | Body cites other memos by **title + hyperlink**, not Issue NNN; fixed “Strategy Publisher Doctrine” framing on disclosure-clock; linked EU AI Act Art. 50 + Commission guidelines where cited |
| Ideas queue page | Password-gated DB UI: `/blog/ideas-queue.html` |
| Ideas queue data + builder | `blog/data/ideas-queue.json`, `scripts/build_ideas_queue.py` |
| Metric-authorship draft on GH | Live draft card + `noindex` post |
| Staging area | `/blog/staging/` + 30 draft HTML essays + `manifest.json` |
| Humanify skill policy (in skill-library) | Detect = rules; rewrite = default Grok voice (no doctrine checklist) |

### Done wrong / incomplete (debt)

| Debt | Why it matters | Owner next |
|------|----------------|------------|
| **Vertical “30/30 enriched” was fake** | Mass outlines (~200–400 words) with ornamental hub links (ASEAN home, Statista stub) that support no body sentence. Skipped retweet Stage-2 enrich + blog-review ground. | Status demoted to `thin-outline`. Re-ground one-by-one per `docs/VERTICAL-ENRICH.md` |
| **AI staging articles lack enrichment** | Same class of failure on `/blog/staging/` | Re-ground before any promote-to-live |
| **GH Actions workflow for ideas-queue not on remote** | Push rejected: OAuth token lacks `workflow` scope. File may exist only locally under `.github/workflows/ideas-queue.yml` | Nick: push workflow with workflow-scoped token, or paste in GH UI |
| **BLOG-QUEUE understated full funnel** | Only listed 5 seeds; retweet library has top-10 shortlist + large weekly R≥0.8 piles | Keep shortlist/top-30 in PLAN + ideas-queue.json |
| **Shortlist markdown not in this repo** | Lives in git history / strategic-publishing extract | Optional: restore copy under `blog/data/` or link stable path |

### Not done (explicitly)

- Primary-source enrichment of all 30 staging posts  
- Free-style rewrite *after* enrichment (sources first)  
- Adversary panel on staging pieces  
- Promote any staging post to public catalogue  
- Teaching series Part 2+  
- Photos/Projects page (#128)  
- Shorts pipeline (#138)  
- Auto cron retweet → draft (#127)

---

## Now / next (ordered)

### P0 — multi-vertical enrichment (current priority)

1. **Fleet rewrite done (2026-07-31):** fintech **30/30** + us-asean-china **30/30** `enriched-draft` with `ground/*.md`, side cards, body sources, ~900–1100 body words (mechanical bar).
2. **Nick review next:** spot-check quality; flag pieces that still feel thin or hub-linked; free-style polish only on flagged slugs.
3. Do **not** promote without Nick; seed-tweet chrome stays staging-only.
4. Grow curator accounts / continuous harvest after review.

### P0b — AI process integrity (deferred by Nick)

1. **Enrich AI staging drafts before more volume**  
   For each staged post under `/blog/staging/` (start with active seeds):  
   - Read enriched + analyzed memos when present  
   - Add inline attribution + **Source notes** with worthy primary links  
   - Mark retrieval gaps honestly  
   - Only then free-style Grok polish  

2. **Keep this `PLAN.md` current** after every session.

### P1 — active seeds (publish path)

| Pri | Idea | Live draft | Staging | Next |
|-----|------|------------|---------|------|
| 1 | Metric-authorship paradox | — (unpublished 2026-08-03) | `metric-authorship.html` | Enrich with Anthropic/session study + Mollick sources; free-style rewrite; Nick sign-off; then promote |
| 2 | Expertise → environment | — | `expertise-to-environment.html` | Find/fix seed tweet; ground; enrich staging |
| 3 | Sovereignty without self-sufficiency | — | `sovereignty-without-self-sufficiency.html` | Use enriched aeronlaffere memo; primary policy sources |
| 4 | AI unit economics | — | `ai-unit-economics.html` | Use burkov + related; no invented numbers |
| 5 | Discovered bias | — | `discovered-bias.html` | Ground beyond framing tweet |

### P2 — rest of top-30 staging

- 25 remaining staging posts: same enrich → polish → optional panel → promote gate  
- Do **not** mark “strong” or “ready” without Source notes

### P3 — site / automation

- Enable ideas-queue auto-refresh workflow on GitHub  
- Optional: restore `blog-shortlist-2026-07-21.md` into `blog/data/`  
- #127 human-gated retweet→draft cron (only after seed quality practice is real)  
- #128 Photos/Projects page  
- #138 Shorts  
- Workflow primer Part 2+ when teaching outlines exist  

---

## Private tools (this repo)

| Tool | URL | Protection | Data |
|------|-----|-----------|------|
| Ideas queue | https://nicholasg3.github.io/blog/ideas-queue.html | **encrypted** | `blog/data/ideas-queue.enc` |
| Article staging (AI) | https://nicholasg3.github.io/blog/staging/ | **encrypted** | `blog/staging/posts/*`, `manifest.enc` |
| Fintech vertical | https://nicholasg3.github.io/fintech/ | markup-hiding only — **readable** | `fintech/data/*`, `fintech/staging/` (**30 thin-outline**; not enriched), `fintech/ground/*` |
| US–ASEAN–China vertical | https://nicholasg3.github.io/us-asean-china/ | markup-hiding only — **readable** | `us-asean-china/data/*`, staging (**29 thin + 1 enriched**), `ground/` |
| Vertical enrich bar | [`docs/VERTICAL-ENRICH.md`](docs/VERTICAL-ENRICH.md) | — | Mandatory process |

Passwords live in Nick's password manager. Do not write one into this repo —
the repo is what gets published.

### Security model (2026-08-03)

GitHub Pages cannot authenticate anyone. The old gates compared a published
SHA-256 hash and then revealed markup that was already in the response, so a
guessed URL — `blog/staging/posts/<slug>.html` — returned the whole draft, and
`manifest.json` listed every slug worth asking for.

The blog now encrypts instead of hides. `scripts/lock_staging.py` writes
AES-256-GCM ciphertext (PBKDF2-SHA256, 310k iterations, site salt in
`blog/staging/lock.json`, fresh IV per file); `blog/staging/gate.js` decrypts in
the browser. No password hash is published, so a wrong password just fails the
GCM auth tag. Plaintext drafts live only in the private `ai-agents-workspace`
repo under `blog-staging/`.

What that buys and does not buy: anyone holding the password reads everything,
and the ciphertext is public, so the password must be long and random — the
script refuses anything under 12 characters. Still not a place for credentials.

**Open exposure — the two verticals.** They were not migrated. Their 60 drafts,
60 `ground/*.md` briefs, and `data/*.json` are served in the clear, and
`seeds.html` / `sources.html` have no gate at all. Fix is the same shape as the
blog: move plaintext to `blog-staging/`, extend `lock_staging.py` to those
sections, wire their pages to `gate.js`. Needs Nick's go-ahead.

**Rebuild and publish (local):**
```bash
export STAGING_SRC=~/code/ai-agents-workspace/blog-staging
cd ~/code/nicholasg3.github.io
python3 scripts/build_ideas_queue.py            # writes $STAGING_SRC/ideas-queue.json
# optional: RETWEET_LIBRARY=/path/to/retweet-library python3 scripts/build_ideas_queue.py
STAGING_PASSWORD='…' python3 scripts/lock_staging.py --src "$STAGING_SRC"
python3 scripts/check_staging_locked.py         # CI runs this on every push
```

---

## Definition of done

### Staging draft → “enriched staging”

- [ ] Particular claim still clear  
- [ ] Inline sources for non-obvious facts  
- [ ] Source notes with primary (or best canonical secondary) links  
- [ ] Links checked worthy (HTTP OK; not random blogs when primary exists)  
- [ ] Retrieval gaps stated when evidence thin  
- [ ] Free-style Grok polish **after** sources, not instead of them  


## Promote staging → live (hard rules)

Staging may show **lab chrome** that is useful for review:

- Kicker: `Staging draft · queue #N · not live`
- Subtitle line: `Seed tweet · source: blog-shortlist #…`
- Side card: “Not on the public catalogue”
- Source notes labeled “Seed tweet (…), reposted by @yahoolovesyou”

**When promoting to `blog/posts/` (or unlocking a vertical publicly), strip all of that.** Live pieces must look professional:

| Keep | Remove |
|------|--------|
| Real claims and argument | “Seed tweet” subtitle under the H1 |
| Worthy primary/canonical sources in Source notes | Queue numbers / “not live” kickers |
| Title-linked internal memos | “reposted by @yahoolovesyou” lab notes |
| Professional kicker (e.g. `Public memo`) | Staging asides / private branding |

**Tool:** `scripts/promote_staging_article.py`  
```bash
python3 scripts/promote_staging_article.py \
  --from "$STAGING_SRC/src/SLUG.html" \
  --to blog/posts/SLUG.html \
  --kicker "Public memo"
```
Promotion is the *only* way a draft reaches a public directory, and only after
Nick signs off. Everything else stays encrypted in `blog/staging/`.
Review the output before catalogue + push. If a tweet is truly evidence (not just the discovery seed), keep it in Source notes under a professional label (e.g. “Discourse source”), never as a title-deck “Seed tweet”.


### Enriched staging → live catalogue

- [ ] Nick sign-off  
- [ ] **Seed tweet chrome removed** (subtitle, queue kicker, yahoolovesyou lab notes)
- [ ] Remove staging-only framing; fit public chrome  
- [ ] No bare Issue NNN in body (title + href)  
- [ ] External legal/tech refs linked in main text where cited  
- [ ] Remove `noindex` only when intentionally public  
- [ ] Catalogue card + push `master`  

---

## Process (canonical)

1. Pick seed (shortlist / ideas-queue / staging)  
2. **Ground** (enriched memo + primary sources + theory)  
3. Particular thesis  
4. Grok default-voice draft into **staging**  
5. Offline detector (diagnostic)  
6. Optional adversary panel (droplet)  
7. Nick sign-off  
8. Promote to `blog/posts/` + catalogue; drop draft labels  

Skills: `skill-library/creative/blog-review`, `skill-library/creative/humanify`  
(Humanify = **detect** with flags; **rewrite** in default Grok voice — no doctrine checklist during rewrite.)

---

## Queue map (do not collapse these layers)

| Layer | What | Where |
|-------|------|--------|
| Raw retweet capture | Large ongoing funnel | `ai-agents-workspace` / yt69 `retweet-library/` |
| Weekly digests | Themes + R/S scores | `retweet-library/digests/` |
| Blog shortlist top 10 | Curated for Nick’s voice | git history / strategic-publishing; mirrored in ideas-queue ranks 1–10 |
| Active seeds (5) | Write-next priority | table above |
| Staging (30) | Draft essays | `blog/staging/` — **currently unenriched** |
| Live public posts | ~32 memos | `blog/posts/` + catalogue |

---

## Related links

- Live blog: https://nicholasg3.github.io/blog/  
- Queue doc (detail tables): [`BLOG-QUEUE.md`](BLOG-QUEUE.md)  
- Workspace handoff (may lag): `ai-agents-workspace/HANDOFF-blog-humanify-and-seeds-2026-07-22.md`  
- GH issues: https://github.com/nicholasg3/ai-agents-workspace/issues  

---

## Session log (append-only)

### 2026-08-03

- **Unfinished draft was live on the public blog.** `blog/posts/metric-authorship-ai-coding.html` was reachable and featured as "Latest Memo" on `blog/index.html` while labelled *needs enrichment · not final*. Deleted the page, removed the card, repointed `draft_post` at staging.
- **The staging gate did not protect anything.** It compared a published SHA-256 hash and then unhid markup that was already in the response; `blog/staging/posts/*.html` and `manifest.json` were readable by direct URL. Same for `blog/data/ideas-queue.json` behind the ideas-queue gate.
- **Drafts are now encrypted at rest** (AES-256-GCM, PBKDF2-SHA256 310k). New: `scripts/lock_staging.py`, `blog/staging/gate.js`, `gate.css`, `scripts/check_staging_locked.py` + CI workflow, `scripts/test_staging_gate.js` (14 browser checks, all passing).
- **Plaintext moved out of this repo** to `ai-agents-workspace/blog-staging/`. Authoring scripts now read/write there via `$STAGING_SRC`.
- **Rotate the password** — the old `nick-staging` / `nick-blog-queue` values were committed in this repo's docs and history.
- **Next agent:** decide on the two verticals (still readable in the clear), then resume metric-authorship enrichment in staging.

### 2026-07-31 (night+3) — mandatory prose rewrite pass

**Nick:** first-gen text is stiff; rewrite of existing prose is good. Fixed step **4b** in VERTICAL-ENRICH.

**Also ban:** generic “operators” as subject (AI-coded). Name banks, founders, firms, customers, regulators.

**Done:** fleet prose rewrite of all 60 staging posts; residual “operator” only as technical terms (port operator, PSE system operator, mobile-operator channel).

### 2026-07-31 (night+2) — fleet full rewrite (8 subagents)

**Done:** Parallel rewrite of all remaining thin-outline stubs under `docs/VERTICAL-ENRICH.md` + model piece (English founder media).

| Vertical | Ground briefs | HTML posts | Status |
|----------|---------------|------------|--------|
| Fintech | 30 | 30 | `enriched-draft` |
| US–ASEAN–China | 30 | 30 | `enriched-draft` |

**Process:** 8 Grok subagents × ~7–8 slugs; each wrote `ground/{slug}.md` + full HTML (AP/Grok third person, blockquote, H2s, table, Reader Decision + Market Signal, body-integrated primaries). No invented companies per brief.

**Mechanical bar (all pass):** body ≥700 words (actual ~900–1100), side cards, source notes, ground file.

**Still true:** Nick spot-check before any promote; some primaries may need browser verification (bot blocks); AI blog staging still deferred.

### 2026-07-31 (night+1) — quality correction (Nick review)

**Nick’s call (correct):** vertical “sources” were often BS hub links that did not support arguments; articles were too thin; agent skipped deep enrichment (retweet Stage-2 + blog-review ground) and mass-produced outlines.

**Corrective actions:**
- Demoted **59** seeds from `enriched-draft` → `thin-outline`; HTML kickers say “thin outline · needs ground”
- Added [`docs/VERTICAL-ENRICH.md`](docs/VERTICAL-ENRICH.md): mandatory pipeline + “supports which sentence?” source test
- Re-did **one** model piece properly: `english-language-founder-media-vs-local-language-c`
  - Ground brief: `us-asean-china/ground/english-language-founder-media-vs-local-language-c.md`
  - Body integrates Constitute Art. 36, DataReportal Digital 2024 Indonesia, EF EPI #80/471, Kirkpatrick ELF ASEAN, Tech in Asia as English media public
  - ~1300 words; Source notes each name the claim they support

**Still true / next:**
1. Do **not** treat the other 59 as enriched
2. Nick picks priority slugs → ground brief → full rewrite (throughput: quality, not 30/session)
3. Wire vertical harvest seeds through `retweet-library-*/pipeline/enrich.py` when tweet-backed
4. AI staging enrichment still deferred
5. No public unlock without Nick

### 2026-07-31 (night) — multi-vertical volume push (**SUPERSEDED — quality fail**)

**What shipped then:** 30 HTML files per vertical labeled enriched.  
**What they actually were:** thin outlines + ornamental sources.  
**Do not cite this session as done.** See night+1 correction above.

### 2026-07-31 (promote rule)

- Nick: seed-tweet under title is good for **staging**, must be removed for **live**.
- Documented in PLAN; added `scripts/promote_staging_article.py`.


### 2026-07-31 (later) — multi-vertical kickoff

**Decisions locked (Nick):**
- Pillars: AI (existing) + **Fintech** + **US–ASEAN–China entrepreneurship** (geo only when it hits that beat)
- Paths: `/fintech/`, `/us-asean-china/`
- Volume target: 30 seeds → enriched → drafts **per** new vertical
- Mini-sites **password-only** until Nick unlocks
- **Same password** for both vertical private pages: `nick-verticals`
- `@yahoolovesyou` = personal mixed feed, **not** vertical curator; use to discover original posters as canonical candidates; dedicated curator accounts later
- **No draft without Source notes + primary/canonical links**; research claims, thread context, theory, anecdotes; fewer than 30 OK; if thin facts, zoom out to patterns; sources may be news **or** papers/lit

**Done in kickoff block (earlier same day):**
- Captured 189 posts from `@yahoolovesyou` → raw harvest file under retweet-library-fintech
- Scaffolded password hubs; 30 seed slots each; first enriched drafts

**Later note:** night volume push was quality-failed; see night+1 correction.



### 2026-07-31

- Nick flagged staging articles lack sources; agent acknowledged skipping ground step.  
- Cross-ref fix shipped: titles + hyperlinks; Art. 50 + guidelines linked on disclosure posts.  
- **Created/updated this running plan** as the session source of truth for the site project.  
- **Next agent:** start P0 enrichment on metric-authorship (staging only since 2026-08-03) with real Source notes, then remaining active seeds.  

### 2026-07-30

- Humanify skill retuned; sitewide Grok voice rewrite; title plain-English pass; ideas queue + staging scaffolding; metric draft on GH.  
