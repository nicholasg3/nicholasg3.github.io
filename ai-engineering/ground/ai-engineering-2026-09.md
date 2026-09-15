# Ground brief — AI Engineering, September 2026 package

**Status:** grounded (2026-09-16)
**Vertical:** ai-engineering
**Pieces:** `automations-that-run-without-me.html` (main analysis),
`what-the-agents-cannot-do.html` (companion)

## Editorial history

Four earlier drafts were published and deleted on Nick's instruction over
2026-09-15/16:

1. An "operator memo" register — rejected on tone.
2. A first-person build-log register (Simon Willison's blog as reference) —
   rejected; Nick called it a step backwards.
3. An AP-mechanics rewrite of the same material — rejected as "just rewrote
   stuff that already existed."
4. Four process-hygiene deep dives (tier test, review ranking, security
   checklist, read-only-first) — rejected as low value add.

The current package was commissioned differently: Nick asked for an AP-style
writer to decide **what** to write, not only how. The selection is therefore
journalistic rather than inventory-driven. The story chosen is that the fleet's
costly failures were organizational, not technical, with the status-board
false alarm as the lede. The companion piece covers the permission
architecture, led by the merge agent that has never merged anything.

A planned fifth piece on real cost figures was dropped on Nick's instruction
("dont discuss the real money piece"), and every dollar figure was removed
from the package.

## Sources (all Nick's own repositories, read 2026-09-15/16)

| Claim | Evidence |
|---|---|
| Status board reported seven of the 10 then running as broken; none were | `co-ceo/org/README.md` — "`ok` and `degraded`" section |
| "A role that finds problems is a role doing its job"; "the health of the employee is not the health of what it watches" | same section, quoted verbatim as design notes |
| 11 agents + 1 human = 12 nodes; titles as listed | `co-ceo/org/org.json` |
| Charters quoted (managing editor, creative director) | `org.json` charter fields, verbatim |
| 7 of 11 agents use no LLM; LLM users carry per-run cost caps and log cost | `Projects-for-agents/AUTO-ROLES.md` rule 7; auto-sre / auto-controller / auto-security SPECs ("Zero-LLM") |
| Rule 1 observe-and-propose; max 5 issues per run; STOPPED kill switch; selftest before cron | `AUTO-ROLES.md` rules 1, 2, 3, 4 |
| Code reviewer examines 3 files nightly | `Projects-for-agents/auto-qa/SPEC.md` |
| Questions: one sentence / 400 chars, unknown node errors, 24h re-ask dedupe, default recipient is the manager | `co-ceo/org/README.md` — "Filing an ask" |
| Escalation: 48 hours, one level per sweep, twice daily, never past the top, one phone message, failure-tolerant | `org.json` `escalate_after_hours`; README "Escalation" |
| Three status states; completion marker wins; deferred push is not lost work | README, "Two rules keep red honest" |
| Digest defaults to routine ("being wrongly quiet beats being wrongly loud"); blank summary rather than a guessed one ("a wrong summary is worse than no summary") | README, digest rules |
| Security audit moved daily → monthly because of alert fatigue; messages only on a flagged check | `Projects-for-agents/auto-security/SPEC.md` "Cadence" and "Output" |
| Security auditor is read-only: never chmod, edit configs, install packages or restart services | auto-security SPEC "Hard rules beyond doctrine" |
| Scheduler starvation; additive not multiplicative boost; override needed in both gates; only one fixed first time | memory `project_co_ceo.md` |
| Seven-hour crash loop after a refactor deleted the scripts | memory `project_auto_company_loop.md` |
| Unlisted page on a static host is public; emergency takedown; CI draft-guard added | `nicholasg3.github.io/CLAUDE.md`; `.github/workflows/draft-guard.yml` |
| 42 hours of false DOWN verdicts from a routing redirect | memory `ops_droplet_ssh_limits.md` |
| Merge agent: dry-run default, live refused unless `LIVE-ENABLED` exists, created by Nick by hand, census row `enabled: false` | `Projects-for-agents/merge-warden/SPEC.md` "Modes" and "Cadence" |
| Three tiers and the mechanical-check admission test; Tier C is the absence of a template | `Projects-for-agents/frontier-orchestrator/SPEC.md`; `lane.json` templates |
| Episodic-memory read path cannot write (never calls mutating commands) | `optmem-bridge/README.md` `recall.py` |
| Self-modifying agent: 3 auto-applied categories, 4 escalated categories, split on reach; never restarts the live service | `Projects-for-agents/pa-self-improve/README.md` |

## Exclusions

No dollar figures. No arc names, employer mail automation, client finances or
unreleased ventures. No credential paths, ports, hostnames, IP addresses or bot
handles. The disclosure line at the top of each piece states that the systems
are the author's own.

## Accuracy note

The status-board incident occurred when the fleet numbered 10 agents; it now
numbers 11. The main piece says "seven of the 10 then running" to avoid
implying the current count.

## Promotion checklist

1. Ground brief — DONE 2026-09-16 (this file).
2. Particular thesis; named mechanisms; claims mapped to primary files — DONE 2026-09-16.
3. Default-voice rewrite pass — NOT RUN. The droplet has refused SSH on both
   addresses for the whole session; the OpenRouter key lives there.
4. AI-style detector pass — NOT RUN (same blocker).

**Promotion basis:** Nick's explicit instruction to scrap the earlier drafts and
publish a new package. Steps 3-4 outstanding; run both when the droplet is
reachable and revise in place if either fails.
