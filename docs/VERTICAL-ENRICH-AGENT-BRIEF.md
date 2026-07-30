# Agent brief — full rewrite of vertical thin-outline stubs

Repo root: `/Users/nicholasgarcia/code/nicholasg3.github.io`

## Mandatory reading (in order)

1. `docs/VERTICAL-ENRICH.md` — quality bar, bans, structure
2. Model finished piece: `us-asean-china/staging/posts/english-language-founder-media-vs-local-language-c.html`
3. Model ground brief: `us-asean-china/ground/english-language-founder-media-vs-local-language-c.md`
4. Live form references: `blog/posts/asean-market-entry-test.html`, `blog/posts/stablecoin-distribution-test.html`, `blog/posts/ai-coverage-gap.html` (side cards)

## Your assigned slugs

(See task prompt.) For each slug:

### A. Research + ground brief

Write `{vertical}/ground/{slug}.md` with:

- Particular claim
- Named actors + links
- Primary docs that will support **specific body sentences**
- Theory hook
- Real case **only if documented** (no invented companies)
- Retrieval gaps

Source test: *Which sentence fails if this URL is removed?*

### B. Full HTML rewrite

Overwrite `{vertical}/staging/posts/{slug}.html`.

**Shell pattern** (match model piece):

- `noindex`, brand header for Fintech or US–ASEAN–China
- Kicker: `Staging · enriched draft · queue #{rank} · not public`
- H1 + deck
- Body: AP/Grok third-person feature voice
- Opening continuous paragraphs
- One blockquote thesis
- 3–5 H2s with real paragraphs (not one-line stubs)
- Optional comparison table
- Optional real case with links
- Source notes with exact titles; each line says what it establishes
- `aside` with Reader Decision + Market Signal side-cards
- Footer

**Word count:** body roughly 900–1400 words (excluding source notes).

**Banned:** inventing companies; hub-only sources; “What this is not claiming”; stacked not-X-but-Y; second-person coaching (“you should”); meta “particular claim is narrow”; ornamental ASEAN/Statista homes; **generic “operators” / “operator”** (name the real actor: bank, founder, firm, customer, regulator).

**Voice:** AP feature + default Grok. Attribute numbers (“according to DataReportal…”, “the Fed said…”).

### C. Do not touch

- Do not edit other agents’ slugs
- Do not rewrite `english-language-founder-media-vs-local-language-c` (already done)
- Do not commit/push (parent will)
- Do not mass-edit seeds.json if concurrent (parent rebuilds status after)

## HTML brand strings

| vertical | brand strong | kicker vertical label |
|----------|--------------|------------------------|
| fintech | Fintech | Fintech staging title suffix |
| us-asean-china | US–ASEAN–China | same |

Title tag: `{title} | {Fintech|US–ASEAN–China} staging`

## Seed metadata

Read claim/idea from `{vertical}/data/seeds.json` for your slug’s `idea`, `thesis`, `tweet_urls`, `primary_url`, `rank`.

If seed tweet exists, optional line under deck: `<p><a href="...">Seed tweet</a></p>` (staging chrome OK).

## Done criteria per slug

- [ ] `ground/{slug}.md` exists
- [ ] HTML full rewrite, sources body-integrated
- [ ] **Step 4b prose rewrite** applied (second pass on existing body — not first-gen only)
- [ ] No invented anecdote
- [ ] Side cards present
- [ ] ≥3 load-bearing primary/canonical links that appear in body

## Prose-rewrite-only mode (when parent assigns rewrite pass)

If the task is **rewrite existing prose only**:

1. Read current `{vertical}/staging/posts/{slug}.html`
2. Read model: `us-asean-china/staging/posts/english-language-founder-media-vs-local-language-c.html`
3. Rewrite body paragraphs for AP/Grok voice; **preserve all facts, numbers, links, cases, tables, source notes**
4. Do not research new claims unless fixing a broken sentence
5. Do not invent companies
6. Keep structure (H2s, blockquote, side cards) unless merging one-line stub headings into real sections

## Return to parent

List each slug: `DONE` or `BLOCKED (reason)`. Note strongest primary used per piece.
For rewrite-only: `REWRITTEN` per slug.
