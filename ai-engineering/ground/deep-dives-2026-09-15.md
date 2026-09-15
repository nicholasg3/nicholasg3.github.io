# Ground brief — AI Engineering deep dives (2026-09-15, revision 2)

**Status:** grounded (2026-09-15)
**Vertical:** ai-engineering
**Parent piece:** `automations-that-run-without-me.html` (now "Sixteen Automations")
**Source type:** Nick's own specifications, READMEs and config, read directly this session.
No external claims are made.

**Revision note.** Revision 1 published four process-hygiene pieces (tier test, review
ranking, security checklist, read-only-first). Nick judged them low value; all four were
deleted on 2026-09-15 and replaced by the three below. A fifth candidate — the fleet's
real cost figures — was dropped on Nick's instruction, and every dollar figure was
removed from the parent piece at the same time.

## 1. agents-with-an-org-chart

Source: `co-ceo/org/README.md`, `co-ceo/org/org.json`, `co-ceo/org/orgctl`, `co-ceo/inbox/README.md`.

| Claim | Evidence |
|---|---|
| 12 nodes: 1 human + 11 agents; titles CEO, Chief of Staff, Managing Editor, Creative Director, Chronicler, Knowledge Gardener, Staff QA Engineer, Fleet Health Officer, Security Auditor, Cost Controller, GTM Signal Watch, Release Gatekeeper | `org.json` nodes (enumerated) |
| Per node: reports_to, dir, log, reports_dir, reports_glob, cadence, expect_run_within_hours, charter | `org.json` node schema |
| Charters quoted (Managing Editor, Creative Director) | `org.json` charter fields, verbatim |
| `orgctl chart`, `validate` (non-zero on any problem) | `orgctl` subparsers; README |
| `ask` defaults `--to` to your manager; role files and keeps going, does not block | README "Filing an ask" |
| Unknown node exits 2; text one sentence, 400 char max; re-ask dedupe while open and <24h old | README "Rules that matter to a caller" |
| `list --open`, `list --for nick --json`, `answer`, `withdraw`, `status` | README "Reading and answering" |
| Ledger is append-only JSONL, never committed, never hand-appended; withdraw twice is a no-op; withdrawn asks never escalate | README "The ledger" / "Withdrawing" |
| Escalation: 48 hours (`escalate_after_hours`), one level per sweep, idempotent in window, never past nick (`at-root`), one Telegram line when it lands on nick, failure-tolerant exit 0 | README "Escalation"; `org.json` |
| `ok` means did the run fail, never what it found; "a role that finds problems is a role doing its job"; conflating told Nick 7 of 10 employees were broken | README "`ok` and `degraded`" (verbatim reasoning) |
| Three states green / amber(degraded) / red, with the listed examples; degraded null on red | README state table |
| "A completion marker wins"; "a deferred push is not a lost artifact" | README "Two rules keep red honest" |
| Digest rules: fold continuations, collapse repeats, classify kind (default plumbing, "being wrongly quiet beats being wrongly loud"), mine structured lines, cap 10 with the half-slots guard and the auto-sre example | README "`recent` — how a log becomes a digest" |
| "Dry runs never lead"; "a wrong summary is worse than no summary" | README, verbatim |

Genericised for publication: the ~1,500-line figure for orgctl is Nick's estimate of the
single-file CLI, stated as approximate. Arc names, the ten life arcs, and every client,
venture and employer reference are excluded.

## 2. bot-that-reads-its-own-transcripts

Source: `Projects-for-agents/pa-self-improve/README.md`.

| Claim | Evidence |
|---|---|
| Loop reflects on its own receipts rather than guessing; every change gated by a runnable witness (exits 0), reversible via git, risky surfaces escalate | README header |
| Interaction history = the coding agent's own session transcripts (JSONL); a state file maps chat → session id | README "Where the bot + its history live" |
| Four friction signals: corrections, tool errors, unfulfilled requests, re-asks; scored and deduped by theme | README `mine.py` row |
| Theme-miner fallback when transcript friction is empty | README `mine_themes.py` row |
| `improve.py` is the judgment seam: ONE concrete improvement + a runnable witness; deterministic stub for the selftest | README `improve.py` row |
| Gate: SAFE + reversible → auto-apply + git commit; RISKY → queue + Telegram ping | README `gate.py` row |
| Auto-applied set: instruction-file clarifications in a marked block, read-only tool proposals, skill/recurring-error notes; tool ideas land in a proposals dir, not live tools | README "Auto-apply vs escalate" |
| Escalated set: outbound email, calendar writes, allowlist, destructive ops | README "Auto-apply vs escalate" and "Safety (non-negotiable)" |
| Never restarts or redeploys the live bridge; instruction changes picked up on next message | README "Auto-apply vs escalate" |
| Ledger of {change, witness result, did friction drop next period}; finds peak, flags regressions, stop-on-decline after K cycles | README `reflect.py` row |
| "The loop declines by ADDING" — the reason stop-on-decline exists | README "Discipline" line (issue #68) |
| Hermetic end-to-end selftest exits 0, no side effects; daily droplet timer ~06:30 SGT with its own log; review ledger and escalations periodically | README "Run it" and "Droplet timer" |

The bot's public handle and the droplet hostname are NOT reproduced. Nick's ambivalence
about the theme-miner fallback is his own editorial position, flagged as such.

## 3. two-memory-stores

Source: `lessons/README.md`, `optmem-bridge/README.md`.

| Claim | Evidence |
|---|---|
| Rules store: one file per lesson, kebab-case id == filename, frontmatter then optional body | lessons README "Format" |
| Required fields id, tags, trigger, rule (max 2 sentences), evidence, created, last_applied; selector updates last_applied; body not read by selector | lessons README "Format" (example block reproduced with a real lesson id) |
| Library, not a daemon — no cron of its own; readers call select, writers call emit | lessons README "What it does" |
| Cap 50 active; promotion proposal must name what it retires (oldest last_applied default) | lessons README "Curation rules" |
| Writers never touch active/ — emit only writes inbox/; promotion is manual, human or main session, never a background daemon | lessons README "Curation rules" |
| Dedupe by slug; emit refuses an id already present in active/ or inbox/ | lessons README "Curation rules" |
| Contradiction check against MAP.md / DECISIONS.md before proposing promotion | lessons README "Curation rules" |
| Selector ranks by tag-match count then most-recently-applied, token-bounded, active only; `--cite` is a separate call | lessons README "Reading (selector)" |
| Three injection points: worker prompts, engine cycle context, interactive sessions | lessons README diagram |
| Episodic store = OptMem; bridge never writes the store directly, only through the real CLI | optmem README "What it does" |
| Read path cannot write (never calls note/forget/nap/import) | optmem README `recall.py` |
| Write gate: event-or-decision-with-a-reason, not trivial, not near-duplicate, not rule-shaped; rejection points at lessons/emit.py | optmem README `save.py` and diagram node X2 |
| Engine saves at end of every cycle on both paths, rate-limited to 3/day via a flock-serialised counter | optmem README "Wiring" |
| Turn-end Stop hook, because session-end capture does not fire when the lid closes; debounce file touched the instant it is due, before the block | optmem README `checkpoint-hook.sh` and diagram W4 |

Tool names, store paths and env var names are genericised in the published piece. The
example lesson id shown (`git-add-own-files-only`) is a real active lesson and is
harmless to publish — it restates the rule already published in the parent piece.

## Promotion checklist

1. Ground brief — DONE 2026-09-15 (this file).
2. Particular thesis per piece; named mechanisms; no restatement of the parent — DONE 2026-09-15.
3. Default-voice rewrite pass — NOT RUN 2026-09-15. Droplet unreachable by SSH all session.
4. AI-style detector pass — NOT RUN 2026-09-15 (same blocker).

**Voice note (revision 3, 2026-09-16).** Three registers were tried. The first draft used
an operator-memo register; Nick rejected the tone. The second used a first-person build-log
register (Simon Willison's blog as reference); Nick rejected that too. All four pieces are
now written to **Associated Press style**: news register, inverted pyramid, third person,
short paragraphs, no serial comma, AP numerals (spell out one through nine, figures for 10
and above), AP time forms (2 a.m.), % with figures, down-style headlines. Titles were
re-cast accordingly and the manifest, index cards and feed follow. Verified mechanically:
zero serial commas, zero first-person pronouns outside quoted command examples, zero
second-person address, zero dollar figures. No byline, name or branding other than Nick's
appears on any page.

**Promotion basis:** Nick's explicit instruction on 2026-09-15 to publish these and to
update the parent page. Steps 3-4 remain outstanding for all four pieces; run them
together when the droplet is reachable.
