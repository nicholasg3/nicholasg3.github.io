#!/usr/bin/env python3
"""Build the ideas backlog for the password-gated ideas page.

Sources (in order):
1. Embedded shortlist + ranked seeds (always available)
2. Optional scan of RETWEET_LIBRARY paths for enriched/analyzed file links
3. Optional blog-shortlist markdown if present

Usage:
  python3 scripts/build_ideas_queue.py
  RETWEET_LIBRARY=/path/to/retweet-library python3 scripts/build_ideas_queue.py

Writes: $STAGING_SRC/ideas-queue.json (private repo).
Publish it with: python3 scripts/lock_staging.py --src $STAGING_SRC
"""
from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def staging_src() -> Path:
    """Private staging root — plaintext drafts never live in this public repo."""
    return Path(os.environ.get(
        "STAGING_SRC", ROOT.parent / "ai-agents-workspace" / "blog-staging"
    )).expanduser()


# Plaintext backlog: private repo only. lock_staging.py publishes the encrypted copy.
OUT = staging_src() / "ideas-queue.json"

# Ranked ideas — shortlist 1–10, then W26 skills / W30 high-signal.
# Update ranks/claims here; tweet/memo links can be refreshed by scan.
SEED_IDEAS = [
    {
        "rank": 1,
        "id": "expertise-to-environment",
        "idea": "Expertise migrates from the prompt to the environment (harness/folder config)",
        "source": "blog-shortlist #1 · active seed",
        "status": "queued",
        "tweet_urls": [],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
    },
    {
        "rank": 2,
        "id": "deleted-equals-valuable",
        "idea": "“Deleted = valuable”: scarcity theater over public knowledge",
        "source": "blog-shortlist #2",
        "status": "hold",
        "tweet_urls": [
            "https://x.com/cyrilXBT/status/2067146024452538498",
            "https://x.com/Raytar/status/2069884250132721840",
        ],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["cyrilXBT", "Raytar"],
    },
    {
        "rank": 3,
        "id": "prestige-curation",
        "idea": "Prestige-curation lubricates rather than filters",
        "source": "blog-shortlist #3",
        "status": "hold",
        "tweet_urls": [],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
    },
    {
        "rank": 4,
        "id": "metric-authorship",
        "idea": "Metric-authorship paradox: completion metrics score who defines done",
        "source": "blog-shortlist #4 · active seed #1",
        "status": "draft",
        "tweet_urls": ["https://x.com/emollick/status/2067839690158268923"],
        "enriched": [],
        "analyzed": [],
        "draft_post": "staging/posts/metric-authorship.html",
        "handles": ["emollick"],
    },
    {
        "rank": 5,
        "id": "multipersona-blind-spot",
        "idea": "Multi-persona “research” blind spot (STORM theater without retrieval)",
        "source": "blog-shortlist #5",
        "status": "hold",
        "tweet_urls": ["https://x.com/LinearUncle/status/2067550807311179783"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["LinearUncle"],
    },
    {
        "rank": 6,
        "id": "sovereignty-without-self-sufficiency",
        "idea": "Sovereignty without self-sufficiency (state-as-VC)",
        "source": "blog-shortlist #6 · active seed",
        "status": "queued",
        "tweet_urls": ["https://x.com/aeronlaffere/status/2070737708318642495"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["aeronlaffere"],
    },
    {
        "rank": 7,
        "id": "higher-order-sycophancy",
        "idea": "Higher-order sycophancy: weak pushback so the user “wins”",
        "source": "blog-shortlist #7",
        "status": "hold",
        "tweet_urls": ["https://x.com/voooooogel/status/2061345017432854716"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["voooooogel"],
    },
    {
        "rank": 8,
        "id": "ai-unit-economics",
        "idea": "AI unit economics: load-bearing or propped by subsidy?",
        "source": "blog-shortlist #8 · active seed",
        "status": "queued",
        "tweet_urls": ["https://x.com/burkov/status/2061523477765743090"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["burkov"],
    },
    {
        "rank": 9,
        "id": "discovered-bias",
        "idea": "Discovered bias: opacity vs reform when institutions admit bias",
        "source": "blog-shortlist #9 · active seed",
        "status": "queued",
        "tweet_urls": ["https://x.com/homocommunism/status/2067956915578044709"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["homocommunism"],
    },
    {
        "rank": 10,
        "id": "false-flag-astroturf",
        "idea": "False-flag / astroturf epistemics",
        "source": "blog-shortlist #10",
        "status": "hold",
        "tweet_urls": ["https://x.com/AISafetyMemes/status/2062254769402699922"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["AISafetyMemes"],
    },
    {
        "rank": 11,
        "id": "containment-attack-surface",
        "idea": "Containment as attack surface (eval object becomes attacker)",
        "source": "W30 lead R≈0.85",
        "status": "watch",
        "tweet_urls": [
            "https://x.com/AISafetyMemes/status/2079668520980562197",
            "https://x.com/lukeprog/status/2079664391469908423",
        ],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["AISafetyMemes", "lukeprog"],
    },
    {
        "rank": 12,
        "id": "openweights-agi-coherence",
        "idea": "Open-weights vs AGI-risk belief coherence",
        "source": "W26 deep analysis",
        "status": "watch",
        "tweet_urls": [
            "https://x.com/emollick/status/2081185596488241507",
            "https://x.com/tszzl/status/2081170506305433811",
        ],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["emollick", "tszzl"],
    },
    {
        "rank": 13,
        "id": "capabilities-slowdown-button",
        "idea": "Global capabilities slowdown as a coordination fantasy",
        "source": "W26 / alignment politics",
        "status": "watch",
        "tweet_urls": ["https://x.com/tszzl/status/2081122092096065771"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["tszzl"],
    },
    {
        "rank": 14,
        "id": "storm-research-skill",
        "idea": "STORM-style research skill (grounded multi-perspective)",
        "source": "W26 skill S=0.9",
        "status": "skill-seed",
        "tweet_urls": ["https://x.com/LinearUncle/status/2067550807311179783"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["LinearUncle"],
    },
    {
        "rank": 15,
        "id": "loop-engineering",
        "idea": "Loop engineering: design loops that prompt agents",
        "source": "W26 skill S=0.9",
        "status": "skill-seed",
        "tweet_urls": [
            "https://x.com/Hesamation/status/2063740195241906638",
            "https://x.com/steipete/status/2063697162748260627",
        ],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["Hesamation", "steipete"],
    },
    {
        "rank": 16,
        "id": "system-prompt-craft",
        "idea": "System-prompt craft (authoring practice, not leak cosplay)",
        "source": "W26 skill S=0.9",
        "status": "skill-seed",
        "tweet_urls": ["https://x.com/lefthanddraft/status/2064420135042224247"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["lefthanddraft"],
    },
    {
        "rank": 17,
        "id": "feedback-loop-dev",
        "idea": "Feedback-loop / iterative agent development workflow",
        "source": "W26 skill S=0.9",
        "status": "skill-seed",
        "tweet_urls": ["https://x.com/seangeng/status/2064513457584541849"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["seangeng"],
    },
    {
        "rank": 18,
        "id": "company-building-claude-code",
        "idea": "Company-building blueprint with Claude Code",
        "source": "W26 skill S=0.9",
        "status": "skill-seed",
        "tweet_urls": ["https://x.com/eng_khairallah1/status/2063958225234567417"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["eng_khairallah1"],
    },
    {
        "rank": 19,
        "id": "daily-driver-llm-workflow",
        "idea": "Expert daily-driver LLM workflow",
        "source": "W26 skill S=0.9",
        "status": "skill-seed",
        "tweet_urls": ["https://x.com/0xchromium/status/2063321324605280569"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["0xchromium"],
    },
    {
        "rank": 20,
        "id": "agentic-dev-best-practices",
        "idea": "Agentic-agent development best practices",
        "source": "W26 skill S=0.9",
        "status": "skill-seed",
        "tweet_urls": ["https://x.com/Av1dlive/status/2062833437980184989"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["Av1dlive"],
    },
    {
        "rank": 21,
        "id": "self-hosted-ai-workspace",
        "idea": "Self-hosted AI workspace (local models, RAG, councils)",
        "source": "W26 skill S=0.9",
        "status": "skill-seed",
        "tweet_urls": ["https://x.com/Hesamation/status/2061239803610341837"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["Hesamation"],
    },
    {
        "rank": 22,
        "id": "skillopt-auto-improve",
        "idea": "SkillOpt / auto-improving skill files",
        "source": "W26 skill S=0.9",
        "status": "skill-seed",
        "tweet_urls": ["https://x.com/garrytan/status/2061107022360391686"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["garrytan"],
    },
    {
        "rank": 23,
        "id": "token-reduction-wiki-layer",
        "idea": "Token-reduction / wiki-layer memory systems",
        "source": "W26 skill S=0.9",
        "status": "skill-seed",
        "tweet_urls": ["https://x.com/Asteri_eth/status/2060768042347372865"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["Asteri_eth"],
    },
    {
        "rank": 24,
        "id": "multi-agent-coding-workflow",
        "idea": "Multi-agent coding workflow (PR automation)",
        "source": "W26 skill S=0.9",
        "status": "skill-seed",
        "tweet_urls": ["https://x.com/suraj_sharma14/status/2067260985073959084"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["suraj_sharma14"],
    },
    {
        "rank": 25,
        "id": "forward-deployed-engineers",
        "idea": "Forward Deployed Engineers: service-embedded AI firms",
        "source": "W26 watchlist R=0.8",
        "status": "watch",
        "tweet_urls": ["https://x.com/AndrewYNg/status/2061477558693384395"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["AndrewYNg"],
    },
    {
        "rank": 26,
        "id": "analogy-as-authority",
        "idea": "Analogy-as-authority (LLMs “implement HNSW”)",
        "source": "W26 epistemics thread",
        "status": "watch",
        "tweet_urls": ["https://x.com/eric_alcaide/status/2070180569195901080"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["eric_alcaide"],
    },
    {
        "rank": 27,
        "id": "danger-prestige-marketing",
        "idea": "Danger/prestige labels as marketing (“most dangerous 37 pages”)",
        "source": "W26 research-method thread",
        "status": "watch",
        "tweet_urls": ["https://x.com/phosphenq/status/2070595499959492742"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["phosphenq"],
    },
    {
        "rank": 28,
        "id": "automation-vs-workforce",
        "idea": "Automation affordability vs workforce value",
        "source": "W26 watchlist",
        "status": "watch",
        "tweet_urls": ["https://x.com/GergelyOrosz/status/2061350086244725094"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["GergelyOrosz"],
    },
    {
        "rank": 29,
        "id": "agent-dynamic-memory-failure",
        "idea": "Agent failure on dynamic memory tasks",
        "source": "W26 watchlist (rohanpaul_ai)",
        "status": "watch",
        "tweet_urls": [],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["rohanpaul_ai"],
    },
    {
        "rank": 30,
        "id": "breakout-detection-protocols",
        "idea": "Breakout-detection / eval-environment hardening protocols",
        "source": "W30 skill seed S=0.40",
        "status": "skill-seed",
        "tweet_urls": ["https://x.com/AISafetyMemes/status/2079668520980562197"],
        "enriched": [],
        "analyzed": [],
        "draft_post": None,
        "handles": ["AISafetyMemes"],
    },
]


def library_roots() -> list[Path]:
    roots = []
    env = os.environ.get("RETWEET_LIBRARY")
    if env:
        roots.append(Path(env).expanduser())
    home = Path.home() / "code"
    candidates = [
        home / "ai-agents-workspace" / "Projects-for-agents" / "retweet-library",
        home / "ai-agents-workspace-yt69" / "Projects-for-agents" / "retweet-library",
        Path("/home/nicholas/ai-agents-workspace/Projects-for-agents/retweet-library"),
    ]
    for c in candidates:
        if c.is_dir() and c not in roots:
            roots.append(c)
    return roots


def index_memos(root: Path) -> dict[str, dict[str, list[str]]]:
    """Map handle lower -> {enriched: [paths], analyzed: [paths], tweets: [urls]}."""
    out: dict[str, dict[str, list[str]]] = {}
    for kind in ("enriched", "analyzed"):
        d = root / kind
        if not d.is_dir():
            continue
        for p in d.glob("*.md"):
            try:
                text = p.read_text(errors="replace")
            except OSError:
                continue
            urls = re.findall(r"https://x\.com/([A-Za-z0-9_]+)/status/\d+", text)
            handles = {u.lower() for u in urls}
            # also from title line
            m = re.search(r"\(([^)]+)\)\s*$", p.name)  # rare
            for h in re.findall(r"@([A-Za-z0-9_]+)", text[:400]):
                handles.add(h.lower())
            for h in handles:
                bucket = out.setdefault(h, {"enriched": [], "analyzed": [], "tweets": []})
                rel = str(p)
                if rel not in bucket[kind]:
                    bucket[kind].append(rel)
                for u in re.findall(r"https://x\.com/[A-Za-z0-9_]+/status/\d+", text):
                    if u not in bucket["tweets"]:
                        bucket["tweets"].append(u)
    return out


def attach_memos(ideas: list[dict], indexes: list[dict[str, dict]]) -> list[dict]:
    for idea in ideas:
        handles = [h.lower() for h in idea.get("handles", [])]
        enriched, analyzed = [], []
        for h in handles:
            for idx in indexes:
                if h not in idx:
                    continue
                for path in idx[h].get("enriched", []):
                    if path not in enriched:
                        enriched.append(path)
                for path in idx[h].get("analyzed", []):
                    if path not in analyzed:
                        analyzed.append(path)
                # fill missing tweets from index
                if not idea["tweet_urls"]:
                    idea["tweet_urls"] = idx[h].get("tweets", [])[:3]
        idea["enriched"] = enriched[:4]
        idea["analyzed"] = analyzed[:4]
        idea.pop("handles", None)
    return ideas


def main() -> None:
    ideas = [dict(x) for x in SEED_IDEAS]
    indexes = []
    scanned = []
    for root in library_roots():
        scanned.append(str(root))
        indexes.append(index_memos(root))
    ideas = attach_memos(ideas, indexes)

    payload = {
        "version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "title": "Publishing ideas queue (top 30)",
        "notes": [
            "Ranks 1–10 = blog-shortlist-2026-07-21 order.",
            "Ranks 11–30 = W26 skill/watchlist + W30 high-signal (not a formal re-score).",
            "Enriched/analyzed paths are absolute local paths when the builder can see a retweet-library clone.",
            "Password gate is client-side (GitHub Pages has no real server auth).",
        ],
        "scanned_libraries": scanned,
        "count": len(ideas),
        "ideas": ideas,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUT} ({len(ideas)} ideas, scanned {len(scanned)} libraries)")


if __name__ == "__main__":
    main()
