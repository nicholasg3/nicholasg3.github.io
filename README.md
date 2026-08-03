# nicholasg3.github.io

Public site (GitHub Pages from `master`).

## Start here

**→ [`PLAN.md`](PLAN.md)** — running plan: last session, next actions, debt, queues.

Detail tables: [`BLOG-QUEUE.md`](BLOG-QUEUE.md).

## The one rule

Nothing unfinished goes in a public directory. Everything under this repo is
served by GitHub Pages the moment it is pushed, and a page that has been
fetched cannot be unpublished. Drafts live encrypted in `blog/staging/`; the
plaintext lives in the private `ai-agents-workspace` repo.

## Private (encrypted at rest)

| Page | Contents |
|------|----------|
| [Ideas queue](https://nicholasg3.github.io/blog/ideas-queue.html) | `blog/data/ideas-queue.enc` |
| [Article staging](https://nicholasg3.github.io/blog/staging/) | `blog/staging/posts/*.html`, `manifest.enc` |

One password for both, in Nick's password manager — never in this repo. The
served bytes are AES-256-GCM ciphertext, so a leaked URL discloses nothing.

Publish drafts after editing them in the private repo:

```bash
export STAGING_SRC=~/code/ai-agents-workspace/blog-staging
STAGING_PASSWORD='…' python3 scripts/lock_staging.py --src "$STAGING_SRC"
python3 scripts/check_staging_locked.py     # also runs in CI on every push
```

## Public

- Home: https://nicholasg3.github.io/  
- Blog: https://nicholasg3.github.io/blog/  

## Private verticals — NOT yet encrypted

| Vertical | Hub |
|----------|-----|
| Fintech | https://nicholasg3.github.io/fintech/ |
| US–ASEAN–China entrepreneurship | https://nicholasg3.github.io/us-asean-china/ |

**Known exposure.** These two still use the old gate, which only hides markup:
their 60 unenriched drafts, 60 `ground/*.md` briefs, and `data/*.json` are
readable by anyone who requests the URL, and `seeds.html` / `sources.html` have
no gate at all. Same fix as the blog — see `PLAN.md`.
