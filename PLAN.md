# Running plan — nicholasg3.github.io

**This is the living project plan.** Update it at the end of every session that changes the site, the queue, or the process.

| Field | Value |
|-------|--------|
| **Last updated** | 2026-07-31 ~01:10 SGT |
| **Last commit focus** | Multi-vertical program: /fintech/ + /us-asean-china/ private hubs; yahoolovesyou harvest; enriched drafts (sources-first) |
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
| **Staging articles lack enrichment** | Built claim-first essays without systematic use of enriched/analyzed memos or primary sources. Skipped ground step of blog-review pipeline. | Re-ground before any promote-to-live |
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

1. Continue **sources-first** drafts for `/fintech/` and `/us-asean-china/` (target 30 seeds each; drafts only when enriched).
2. Grow canonical source lists from harvest original posters + doctrine-fit outlets.
3. Do **not** mass-produce unenriched essays.

### P0b — AI process integrity (deferred by Nick)

1. **Enrich staging drafts before more volume**  
   For each staged post (start with active seeds):  
   - Read enriched + analyzed memos when present  
   - Add inline attribution + **Source notes** with worthy primary links  
   - Mark retrieval gaps honestly  
   - Only then free-style Grok polish  

2. **Keep this `PLAN.md` current** after every session.

### P1 — active seeds (publish path)

| Pri | Idea | Live draft | Staging | Next |
|-----|------|------------|---------|------|
| 1 | Metric-authorship paradox | `blog/posts/metric-authorship-ai-coding.html` (Draft) | `blog/staging/posts/metric-authorship.html` | Reconcile dual copies; enrich with Anthropic/session study + Mollick sources; Nick sign-off |
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

| Tool | URL | Password (client-side only) | Data |
|------|-----|-----------------------------|------|
| Ideas queue | https://nicholasg3.github.io/blog/ideas-queue.html | `nick-blog-queue` | `blog/data/ideas-queue.json` |
| Article staging | https://nicholasg3.github.io/blog/staging/ | `nick-staging` | `blog/staging/posts/*`, `manifest.json` |

**Security note:** GitHub Pages has no server auth. These gates hide an internal backlog from casual visitors; they are not suitable for secrets.

**Rebuild ideas JSON (local):**
```bash
cd ~/code/nicholasg3.github.io
python3 scripts/build_ideas_queue.py
# optional: RETWEET_LIBRARY=/path/to/retweet-library python3 scripts/build_ideas_queue.py
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

### Enriched staging → live catalogue

- [ ] Nick sign-off  
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

### 2026-07-31 (later) — multi-vertical kickoff

**Decisions locked (Nick):**
- Pillars: AI (existing) + **Fintech** + **US–ASEAN–China entrepreneurship** (geo only when it hits that beat)
- Paths: `/fintech/`, `/us-asean-china/`
- Volume target: 30 seeds → enriched → drafts **per** new vertical
- Mini-sites **password-only** until Nick unlocks
- **Same password** for both vertical private pages: `nick-verticals`
- `@yahoolovesyou` = personal mixed feed, **not** vertical curator; use to discover original posters as canonical candidates; dedicated curator accounts later
- **No draft without Source notes + primary/canonical links**; research claims, thread context, theory, anecdotes; fewer than 30 OK; if thin facts, zoom out to patterns; sources may be news **or** papers/lit

**Done this block:**
- Captured 189 posts from `@yahoolovesyou` (`mode=all`, 10 pages) → `Projects-for-agents/retweet-library-fintech/raw/yahoolovesyou_mix.md`
- Scaffolded password hubs: `/fintech/`, `/us-asean-china/` (hub, seeds, sources, staging)
- Built 30 seed slots + proposed canonical sources per vertical
- Wrote **4 enriched staging drafts with Source notes** (2 fintech, 2 us-asean-china) — quality bar enforced; not 30 yet

**Not done:**
- Full 30 enriched drafts per vertical
- Dedicated curator accounts / continuous capture per vertical
- AI staging enrichment (explicitly deferred)
- Workflow file still may need workflow-scoped push

**Next agent:**
1. Enrich next fintech seeds (stablecoin privacy, PayPal distribution, SWIFT/sanctions rail) with primaries
2. Enrich next us-asean-china seeds (Forest City, NS enclave, tech controls) with primary reporting
3. Expand drafts only when Source notes are real
4. Keep updating this PLAN



### 2026-07-31

- Nick flagged staging articles lack sources; agent acknowledged skipping ground step.  
- Cross-ref fix shipped: titles + hyperlinks; Art. 50 + guidelines linked on disclosure posts.  
- **Created/updated this running plan** as the session source of truth for the site project.  
- **Next agent:** start P0 enrichment on metric-authorship (live draft + staging) with real Source notes, then remaining active seeds.  

### 2026-07-30

- Humanify skill retuned; sitewide Grok voice rewrite; title plain-English pass; ideas queue + staging scaffolding; metric draft on GH.  
