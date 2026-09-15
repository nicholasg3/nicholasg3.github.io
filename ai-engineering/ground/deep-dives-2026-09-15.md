# Ground brief — AI Engineering deep dives (4 pieces, 2026-09-15)

**Status:** grounded (2026-09-15)
**Vertical:** ai-engineering
**Parent piece:** `automations-that-run-without-me.md` (same ground rules apply)
**Source type:** Nick's own specifications and roadmaps, read directly this session.
No external claims are made, so no external sourcing is required.

## 1. the-mechanical-check-test

Source: `Projects-for-agents/frontier-orchestrator/SPEC.md` and `lane.json`.

| Claim | Evidence |
|---|---|
| Loop: observe → score → propose → act → receipt | SPEC "Loop" section |
| Six observe sources (gate exit status, citations file, labelled issue counts, another daemon's state file, third job's log recency, decisions-log staleness) | SPEC "Observe sources" |
| Tier A auto-run on mechanical witness; Tier B issue + phone ping; Tier C never | SPEC "Tiers" table |
| Tier C implemented as absence of a template in `lane.json`, not a runtime deny-list | `lane.json` `templates[]` contains no publish/mail/delete template; SPEC "Tier C — not in lane.json" |
| Template parts: trigger, tier, base priority, run command, witness | `lane.json` template `memory_slug_gate` (trigger/tier/priority_base/run/witness) |
| Witness kinds: exit code | `lane.json` `"witness": {"kind": "exit_code", "expect": 0}` |
| Caps: max 3 active managed issues, max 1 Tier-A run per cycle, separate A/B score thresholds (A higher) | `lane.json` `max_active_frontier_issues: 3`, `max_tier_a_runs_per_cycle: 1`, `min_score_tier_a: 0.55`, `min_score_tier_b: 0.4` |
| Done rule: witness exit 0 AND issue closed; create+close on first green run; Tier B = Nick is verifier; never assert done without a receipt in the state file | SPEC "Done rule" |
| Runs early morning after the other jobs | SPEC "Deployment" (~07:30 SGT, after pa-self-improve + skill-radar) |

Worked-example table (reformat a config, rename a variable, renew a token, summarise messages, choose a supplier, reply to a client) is illustrative reasoning applied to the published rule, not a claim about deployed templates. Written as generic examples, not as inventory.

## 2. review-what-actually-runs

Source: `Projects-for-agents/auto-qa/SPEC.md`.

| Claim | Evidence |
|---|---|
| Census from crontab + systemd user units + shebang files, following one level of source/exec references | SPEC `census.py` |
| Ledger records last-reviewed commit per file; due = commits newer than last review, or never reviewed | SPEC `ledger.py` |
| Priority = usage rank × staleness | SPEC `ledger.py` (verbatim formula) |
| Top 3 files/night, one model call each, fixed six-item rubric (correctness, unhandled failure paths, quoting/parsing, state × signal, concurrency with other daemons, missing tests) | SPEC `review.py` |
| Structured JSON findings (file, line, severity, evidence); per-run cost cap $1.50; stop when projected over cap | SPEC `review.py` |
| Tier-A auto-fix: mechanical verifier (py_compile / bash -n plus nearby selftest or dry-run), minimal fix by coding-tier model, applied to backup-protected copy, verified; pass → commit + close; fail → revert + report tagged "attempted"; cap 5 fixes/run; never touches the engine while its unit is failing | SPEC `fix.py` |
| Never file style-only findings; a finding needs a failure scenario; never review outside the census; skip a file after two unparseable responses | SPEC "Hard rules beyond doctrine" |
| Failure-mode table rows (engine running, gh down → report only + exit 0, cap hit → carry over with ledger untouched, duplicate → skip + note, STOPPED → exit 0) | SPEC "Failure modes" |
| Selftest contents incl. revert-on-fail restoring the original and keeping a .bak, and the per-run fix cap | SPEC "Selftest (minimum)" |

The anecdote about the census surfacing an unreferenced file and a four-job helper is Nick's own recollection of the first census run; presented as experience, not as a logged metric.

## 3. security-check-with-no-model

Source: `Projects-for-agents/auto-security/SPEC.md`.

| Claim | Evidence |
|---|---|
| Monthly, 1st of month; low frequency deliberate because issue fatigue is the real risk | SPEC "Cadence" (verbatim reasoning) |
| Zero-LLM; stdlib + already-installed system tools | SPEC header and "Checks" |
| Six checks: credential file permissions; repo leak scan over last month of commits + working tree; listening-socket allowlist; auth still required on the web surface; pending security updates + reboot flag; remote-access posture read from effective config | SPEC checks 1-6 |
| Report file+line only, never the matched value, never partially, anywhere | SPEC check 2 and "Hard rules" |
| Read-only always: never chmod, edit configs, install packages, restart services | SPEC "Hard rules beyond doctrine" |
| Telegram one-liner only on a FLAG; issues for new public listeners / world-readable secrets / leak hits, max 5, deduped | SPEC "Output" |
| Failure modes: missing tool → SKIPPED with reason; no sudo → degrade + note; STOPPED → exit 0 | SPEC "Failure modes" |
| Selftest fixtures incl. the assertion that the report does not contain the token | SPEC "Selftest (minimum)" |

Deliberately genericised for publication: no credential file paths, no port numbers, no site or host names. The SPEC's specific paths and allowlist entries are NOT reproduced.

## 4. ship-the-read-only-report-first

Source: `relationship-os/README.md` and `docs/design/relationship-os/ROADMAP.md`.

| Claim | Evidence |
|---|---|
| First slice = one read-only command reporting channel coverage and gaps; reads local DB only, no network | README "The Phase 1 first slice" |
| Each phase ships alone, is useful alone, has acceptance tests; phases touching the system of record need their own go-ahead | ROADMAP preamble |
| Coverage 2.5% → 30.3% after the deterministic pass → 51.3% after Nick's link review | ROADMAP Phase 1 and Phase 2 |
| 80 approvals, 38 rejections out of partial matches (118 reviewed) | ROADMAP Phase 2 ("80 approvals, 38 rejections") |
| Approval upgrades stored method to human_confirmed at confidence 1.0 | ROADMAP Phase 1 |
| Zero fuzzy auto-links; every link deterministic or from an explicit field | ROADMAP Phase 1 acceptance test |
| Notion sync verified zero writes against that system's own audit log | ROADMAP Phase 1 acceptance test |
| Double-ingest idempotency tested | ROADMAP Phase 1 and Phase 4 |
| No needs_reply where Nick's message was last; closings never classed as ghost-risk; no second draft without new inbound | ROADMAP Phase 2 acceptance tests |
| Committed memo contains no message or draft bodies; git history purged of memo bodies and verified clean on a fresh clone | ROADMAP Phase 2 |
| No suggestion for opted-out / snoozed / archived rows; missing date reports "unknown", never "overdue" | ROADMAP Phase 3 acceptance tests |
| Pause kill switch stops the next run before any adapter starts | ROADMAP Phase 3 acceptance test |
| DB permissions 0600, lives outside any git repo | README "Safety"; ROADMAP Phase 1 acceptance test |
| Daily schedule 08:45 via launchd | README |

No contact names, no directory contents, and no message content appear in the published piece. The ROADMAP names one merged duplicate person; that name is NOT reproduced.

## Editorial history (added 2026-09-16)

These five pieces are the published set. Three later revisions were made and
then reverted at Nick's instruction:

- **Revision 2 (Willison register).** All pieces rewritten first person; the
  four deep dives were deleted and replaced by three others (org chart,
  self-improving assistant, two memory stores). Nick: "a step backwards."
- **Revision 3 (AP mechanics).** The same revision-2 material re-cast in
  Associated Press style. Nick: "a tiny step forward but just rewrote stuff
  that already existed."
- **Revision 4 (AP commissioning).** Scrapped entirely; two new pieces with the
  angle chosen journalistically. Nick then asked to restore the pre-revision-2
  state, which is what is now live.

The restored text is byte-identical to commit 5ea793a with one exception: every
dollar figure was removed per Nick's separate standing instruction, which
postdates the original drafting. Two edits were required — the server's monthly
cost in the parent piece and the reviewer's per-run spend cap in
`review-what-actually-runs`. Both now describe the mechanism without the
number.

## Promotion checklist

1. Ground brief — DONE 2026-09-15 (this file).
2. Particular thesis per piece; named mechanisms; no restatement of the parent piece — DONE 2026-09-15.
3. Default-voice rewrite pass — NOT RUN 2026-09-15 (droplet unreachable by SSH all session; the OpenRouter key lives there).
4. AI-style detector pass — NOT RUN 2026-09-15 (same blocker).

**Promotion basis:** Nick's explicit instruction on 2026-09-15 to write these deeper pages and push them to the blog. Steps 3-4 remain outstanding for all five AI-Engineering pieces; run them together when the droplet is reachable.
