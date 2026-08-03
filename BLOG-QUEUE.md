# Blog queue — detail tables

**Running plan (session source of truth):** [`PLAN.md`](PLAN.md)  

Update `PLAN.md` every session. Keep this file for queue tables and tool pointers; do not let it drift ahead of `PLAN.md`.

Last aligned with PLAN: **2026-08-03**

---

## Private tools

| Tool | URL | Password | Data |
|------|-----|----------|------|
| Ideas queue | https://nicholasg3.github.io/blog/ideas-queue.html | `nick-blog-queue` | `blog/data/ideas-queue.json` |
| Article staging | https://nicholasg3.github.io/blog/staging/ | `nick-staging` | `blog/staging/posts/*` |
| Fintech staging (moved from `fintech/index.html`) | https://nicholasg3.github.io/fintech/staging/ | `nick-verticals` | `fintech/staging/posts/*`; public landing now `fintech/index.html` (0 verified) |
| US–ASEAN–China staging (moved from `us-asean-china/index.html`) | https://nicholasg3.github.io/us-asean-china/staging/ | `nick-verticals` | `us-asean-china/staging/posts/*`; public landing now `us-asean-china/index.html` (1 verified: `english-language-founder-media-vs-local-language-c`) |

Client-side password only (GitHub Pages). See PLAN security note.

Rebuild ideas JSON:
```bash
python3 scripts/build_ideas_queue.py
```

---

## Process (per post)

1. Pick seed  
2. **Ground** (sources first — do not skip)  
3. Particular thesis  
4. Grok default-voice draft → **staging**  
5. Detector (diagnostic)  
6. Optional adversary panel  
7. Nick sign-off  
8. Promote to live catalogue  

Skills: `blog-review`, `humanify` (detect with flags; rewrite in default Grok voice).

---

## Active seeds

| Pri | Shortlist # | Focus | Status | Paths |
|-----|-------------|-------|--------|-------|
| 1 | **#4** Metric-authorship | Completion metrics reward who defines done | Staging only; **needs enrichment** (live copy removed 2026-08-03 — drafts must never enter `blog/posts/`) | `blog/staging/posts/metric-authorship.html` |
| 2 | **#1** Expertise → environment | Performance → harness/folder | Staging only; unenriched | `blog/staging/posts/expertise-to-environment.html` |
| 3 | **#6** Sovereignty without self-sufficiency | State-as-VC | Staging only; unenriched | `blog/staging/posts/sovereignty-without-self-sufficiency.html` |
| 4 | **#8** AI unit economics | Load-bearing vs propped | Staging only; unenriched | `blog/staging/posts/ai-unit-economics.html` |
| 5 | **#9** Discovered bias | Opacity vs reform | Staging only; unenriched | `blog/staging/posts/discovered-bias.html` |

Full top-10 shortlist + ranks 11–30: `blog/data/ideas-queue.json` and PLAN queue map.

---

## Staging (30 posts)

All under `blog/staging/posts/`. **Status as of 2026-07-31: claim-first drafts without systematic Source notes.**  

Do not promote until PLAN “enriched staging” checklist passes.

---

## Other open site work (ai-agents-workspace issues)

- **#127** Cron: retweet → humanified draft (human-gated)  
- **#128** Photos / Projects page  
- **#138** Shorts pipeline  
- Workflow primer Part 2+ when teaching outlines exist  
- Ideas-queue GitHub Action: local workflow file may need workflow-scoped push  

---

## Definition of done

See **PLAN.md** (enriched staging + live catalogue checklists).
