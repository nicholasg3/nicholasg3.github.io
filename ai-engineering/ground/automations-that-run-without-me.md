# Ground brief — automations-that-run-without-me

**Status:** grounded (2026-09-15)
**Vertical:** ai-engineering (first published piece in this vertical)
**Claim (particular):** Fourteen named automations run unsupervised on Nick's own
infrastructure. Eight written rules make unsupervised running safe. Four named
incidents produced those rules. The generalizable test for autonomy is whether a
cheap mechanical check can prove the result.

## Source type

Primary sources are Nick's own repositories and specifications, read directly on
2026-09-15. No external claims are made, so no external sourcing is required.
Every load-bearing statement maps to a file below.

| Claim in post | Evidence |
|---|---|
| Nightly worker turns issues into PRs, never pushes main | memory `project_todo_runner.md` |
| Usage census ranks scripts by what actually runs; review ledger; 3 files/night; fixed rubric | `Projects-for-agents/auto-qa/SPEC.md` |
| Monthly security check, zero-LLM, five checks, file+line never value | `Projects-for-agents/auto-security/SPEC.md` |
| Weekly chronicler, Sunday, `[chronicle]` tag, never publishes | `Projects-for-agents/auto-chronicler/SPEC.md` |
| Three-tier orchestrator (A run / B issue+ping / C never) | `Projects-for-agents/frontier-orchestrator/SPEC.md` |
| Relationship DB, local SQLite, daily 08:45, first slice = read-only coverage report | `relationship-os/README.md`; launchd `com.nick.relctl-daily` |
| Email-stale monitor (absence, not events) | memory `project_relationship_os.md`; launchd `com.nick.ai-secretary-email-stale` |
| Offline markdown mirror, ~1005 pages / 27 DBs, snapshot-not-truth rule | memory `project_notion_integration.md`; global CLAUDE.md |
| Phone as approval surface; allowlisted chat bridge to a coding agent | memory `project_telegram_pa.md`; `AI_SECRETARY_EMAIL_ARCHITECTURE.md` ("Telegram is the decision surface") |
| Public opportunities page with deadline-based expiry, daily re-render | `~/.claude/skills/profile-job-board/SKILL.md`; global CLAUDE.md |
| Provider failover at 80% of window, auto-restore at reset, published to PyPI | `~/code/cc-provider-failover/README.md` |
| Publishing gate: ground brief + AI-style detector score + checklist | `nicholasg3.github.io/CLAUDE.md` |
| Heartbeat and backup jobs | launchd `com.nick.mac-fleet-heartbeat`, `com.nick.backup-bridge` |
| Self-improvement pass over the other jobs | `Projects-for-agents/pa-self-improve/` |
| Eight rules (observe-not-act, two outputs, STOPPED file, selftest gate, flock install, zero-LLM where parsing suffices, never `git add -A`, state × signal) | `Projects-for-agents/AUTO-ROLES.md` rules 1-9, quoted structure preserved |
| Server not laptop; repo canonical; old folder archived as dated tarball | memories `project_droplet_migration.md`, `project_ai_agents_workspace.md`, `feedback_daily_droplet_sync.md` |
| Incident: crash-loop ~7h after a refactor deleted the scripts | memory `project_auto_company_loop.md` |
| Incident: scheduler starvation; additive boost; both gates needed fixing | memory `project_co_ceo.md` |
| Incident: draft went live on a static host; CI draft-guard added | `nicholasg3.github.io/CLAUDE.md` (2026-07-30 metric-authorship takedown) |
| Incident: routing redirect hung all SSH for 42h, false DOWN verdicts | memory `ops_droplet_ssh_limits.md` |

## Exclusions (deliberate)

- No employer-specific mail automation, no finance/market work, no pre-launch
  venture work. Stated in the post's closing line.
- No IP addresses, hostnames, bot names, tokens, or file paths of credentials.
- Dollar figure ($12/mo) is the only cost disclosed; it is already public in
  Nick's own notes and is not sensitive.

## Promotion checklist

1. Ground brief — DONE 2026-09-15 (this file; all claims mapped to primary files read this session).
2. Particular thesis; named mechanisms; VERTICAL-ENRICH bar — DONE 2026-09-15 (tier test, eight rules, four incidents).
3. Default-voice rewrite pass — NOT RUN 2026-09-15. The droplet (which holds the
   working OpenRouter key) was unreachable by SSH at 18:19 SGT, so the Grok pass
   could not execute.
4. AI-style detector pass — NOT RUN 2026-09-15 (same blocker: detector runs on the droplet).

**Promotion basis:** Nick's explicit instruction on 2026-09-15 to publish this
piece and circulate the link. Steps 3-4 are outstanding and should be run when
the droplet is reachable; if either fails, revise in place.
