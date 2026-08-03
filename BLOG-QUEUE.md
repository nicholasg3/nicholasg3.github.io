# Blog queue — detail tables

**Running plan (session source of truth):** [`PLAN.md`](PLAN.md)  

Update `PLAN.md` every session. Keep this file for queue tables and tool pointers; do not let it drift ahead of `PLAN.md`.

Last aligned with PLAN: **2026-07-31**

---

## Private tools

| Tool | URL | Data |
|------|-----|------|
| Ideas queue | https://nicholasg3.github.io/blog/ideas-queue.html | `blog/data/ideas-queue.enc` |
| Article staging | https://nicholasg3.github.io/blog/staging/ | `blog/staging/posts/*`, `manifest.enc` |

One password for both, kept in Nick's password manager — never in this repo.
Drafts are AES-256-GCM ciphertext on disk and decrypt in the browser, so a
guessed URL discloses nothing. See the PLAN security note.

Plaintext drafts live in the private repo at `ai-agents-workspace/blog-staging/`.
Edit there, then republish:
```bash
export STAGING_SRC=~/code/ai-agents-workspace/blog-staging
python3 scripts/build_ideas_queue.py
STAGING_PASSWORD='…' python3 scripts/lock_staging.py --src "$STAGING_SRC"
python3 scripts/check_staging_locked.py
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
| 1 | **#4** Metric-authorship | Completion metrics reward who defines done | Staging only; **needs enrichment** (unpublished from the public blog 2026-08-03) | `blog-staging/src/metric-authorship.html` (private) |
| 2 | **#1** Expertise → environment | Performance → harness/folder | Staging only; unenriched | `blog-staging/src/expertise-to-environment.html` (private) |
| 3 | **#6** Sovereignty without self-sufficiency | State-as-VC | Staging only; unenriched | `blog-staging/src/sovereignty-without-self-sufficiency.html` (private) |
| 4 | **#8** AI unit economics | Load-bearing vs propped | Staging only; unenriched | `blog-staging/src/ai-unit-economics.html` (private) |
| 5 | **#9** Discovered bias | Opacity vs reform | Staging only; unenriched | `blog-staging/src/discovered-bias.html` (private) |

Full top-10 shortlist + ranks 11–30: `blog-staging/ideas-queue.json` (private) and PLAN queue map.

---

## Staging (30 posts)

Plaintext under `ai-agents-workspace/blog-staging/src/` (private); encrypted copies under `blog/staging/posts/`. **Status as of 2026-07-31: claim-first drafts without systematic Source notes.**  

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
