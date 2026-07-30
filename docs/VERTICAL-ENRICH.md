# Vertical article enrichment (mandatory)

This is the quality bar for `/fintech/` and `/us-asean-china/` staging posts.
It is the same bar as AI blog staging. **Volume is not progress.**

Nick’s 2026-07-31 review: the first “30/30 enriched” batch was **wrong**. Those
files are **thin outlines** with ornamental hub links. They do **not** count as
enriched. Status on disk: `thin-outline`.

---

## What went wrong (do not repeat)

| Failure | Example |
|---------|---------|
| No Stage-2 retrieval | Skipped `retweet-library/*/pipeline/enrich.py` + `prompts/enrich.md` |
| No ground brief | Skipped blog-review step 1 (who argues, primary docs, theory, actors) |
| Hub links as “sources” | `asean.org` labeled “regional multilingual context” — supports no claim |
| Body never uses the source | Source notes list URLs the prose does not depend on |
| Too thin | ~200–400 words of coach outline vs ~900+ word grounded memo |
| False status | Labeled `enriched-draft` without enrichment |

---

## Pipeline (order is mandatory)

Copy the retweet + blog-review path. Do not invent a lighter vertical path.

### 0. Seed only

- Idea + thesis + optional seed tweet URL.
- Status: `queued` / `seed` / `queued-pattern`.
- **No HTML essay yet.**

### 1. Retrieve (when the seed comes from harvest / X)

Run or hand-produce an **enrich dossier** matching
`Projects-for-agents/retweet-library/pipeline/prompts/enrich.md`:

1. Full post (reconstructed) + `[VERIFIED]` / `[PARTIAL]` / `[NOT FOUND]`
2. Author & context
3. Linked content (summarize substance; URL)
4. Thread / replies / QTs (esp. disagreement)
5. Related factual background (cited)
6. **Retrieval gaps** (blunt list)

Store under:

- `Projects-for-agents/retweet-library-fintech/enriched/` or
- `Projects-for-agents/retweet-library-us-asean-china/enriched/` or
- `fintech/ground/<slug>.md` / `us-asean-china/ground/<slug>.md` for non-harvest seeds.

If the seed is **not** from a tweet, still write a ground brief (step 2). Skip only
the “full post” block.

### 2. Ground (blog-review step 1)

Before any essay HTML, write a **grounding brief** (`ground/<slug>.md`):

- Particular claim (one falsifiable-ish thesis)
- Who is arguing what (named actors + links)
- Primary documents that **support specific sentences you will write**
- Theory hook (named)
- Whose real-world concern (attributed)
- What you could **not** verify

**Rule for every candidate source:**  
> “Which sentence in the draft becomes false if this URL is removed?”  
If none, drop the source.

**Banned as sole sources:** institutional home pages, “hub” links, Statista
paywall stubs, ASEAN Secretariat with no cited instrument, “example national
stats” without a table/report title and year.

### 3. Connect

One claim. Cut ideas that do not serve it. If the seed is thin, write a **pattern
memo that says so** — or refuse to draft.

### 4. Draft (Grok voice; match live public memos)

**Model form:** live posts such as
[`asean-market-entry-test.html`](../blog/posts/asean-market-entry-test.html) and
[`stablecoin-distribution-test.html`](../blog/posts/stablecoin-distribution-test.html).

- Claim first; named institutions and numbers; optional blockquote test; useful-signal / false-positive table; close with procedure.
- Rough bar: **≥800 words** of body for a full memo.
- Integrate sources **in the body** (name + link + what they establish).
- Source notes: same documents, one line each on what they establish.
- Staging may keep seed-tweet chrome; live must strip it (`promote_staging_article.py`).

**Banned in body (Nick 2026-07-31):**

- Sections titled “What this is not claiming” / “What this is not”
- Stacked not-X-but-Y / “That is not a vibe complaint…” hedging
- Meta lines: “The particular claim is narrow,” “This draft intentionally…”
- Ornamental hub links that never appear as load-bearing evidence in the prose
- **Second-person coaching** (“you should,” “put this table in your growth review,” “operating rule:”) — report in **AP-like third person**: what the data show, how firms and customers behave
- **“Operators” / “operator” as generic subject** — AI-coded. Prefer concrete actors: banks, founders, firms, companies, regulators, customers, merchants, boards, teams
- Same ban class: “space,” “landscape,” “leverage” as verb fluff, “robust,” “seamless,” fake “most teams”

**Voice:** closer to an **AP feature** than a strategy memo barked at the reader. Attribute numbers. Prefer “according to / shows / ranks” over second-person coaching.

**Structure (balance — match live memos like `ai-coverage-gap.html`):**

- Continuous opening paragraphs (not a heading per idea)
- Optional **blockquote** thesis (one)
- **A few** H2s (about 3–5), each with real paragraphs under them — not one-sentence stubs
- Optional **table** when it forces a comparison
- Optional **real case** anecdote with primary/canonical links (no invented companies; if evidence is thin, skip the anecdote)
- **aside** with `Reader Decision` + `Market Signal` side-cards when it fits
- Source notes

**Writer routing:** public essay body → **Grok**. Research/brief → any agent.

### 4b. Prose rewrite pass (**mandatory — fixed step**)

Nick (2026-07-31): first-pass generation from research agents is usually stiff.
A **second pass that rewrites existing prose** (not regenerating from a seed)
is what lands in readable AP/Grok voice.

**Never mark a piece done after step 4 alone.** Always run 4b.

**How to rewrite (do not invent):**

1. Open the existing HTML. Keep every load-bearing fact, number, named institution, URL, table row, and real case.
2. Rewrite **paragraph prose only**: openings, H2 body text, blockquote if needed, close. Tighten sentences. Cut AI cadence (reversals, meta hedges, coach imperatives).
3. Prefer short active sentences, attributed numbers, continuous flow under few H2s.
4. Do **not** add invented companies or new uncited claims.
5. Do **not** strip Source notes or side cards; you may polish their wording.
6. Model voice: `us-asean-china/staging/posts/english-language-founder-media-vs-local-language-c.html` after its rewrite passes + live memos above.

**Label:** after 4b, status may stay `enriched-draft` but note `prose_rewrite: 2026-07-31` in ground brief or seed quality_note.

### 5. Status labels (honest)

| Status | Meaning |
|--------|---------|
| `queued` / `seed` / `queued-pattern` | Idea only |
| `grounded` | `ground/<slug>.md` exists with claim-linked primaries |
| `enriched-draft` | Full essay + body-integrated sources + Source notes that pass the “supports:” test **and** step 4b prose rewrite |
| `thin-outline` | **Debt.** Outline only. Do not promote. |
| `ready-for-nick` | Detector optional; Nick review next |

Never set `enriched-draft` without steps 2–4 **and 4b**.

### 6. Gate before promote

- Offline detector if shipping toward public.
- Nick sign-off.
- Promote script strips seed-tweet chrome.

---

## Source notes format (required)

```html
<li><a href="URL">Exact title, author/org, date if any</a>: Supports the claim that [specific sentence].</li>
```

Bad:

```html
<li><a href="https://asean.org/">ASEAN Secretariat</a>: Regional multilingual context.</li>
```

---

## Throughput rule

**One properly grounded memo beats thirty thin outlines.**

Agents hit session limits on quality, not on file count. If time is short: finish
one `grounded` + one `enriched-draft`, update PLAN, stop.
