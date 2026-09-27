#!/usr/bin/env python3
"""Rewrite one published blog post's prose with Opus 5.5 (via OpenRouter).

Nick's ruling (2026-09-27): past pipeline posts read as AI-written; Opus 5.5
rewrites them, and edits to old posts need no human approval. This tool does
ONE post at a time and refuses to emit output that fails the mechanical checks.

What it rewrites: the header dek (the <p> under the <h1>) and the prose inside
<article class="article-body">. What it never touches: the HTML shell (head,
meta, nav, byline, side cards, footer), tables, and the Source Notes section.
Tables and Source Notes are swapped for [[KEEP_n]] placeholders before the
model sees the body and restored verbatim afterwards. The title changes only
if the model says the current one breaks the Titles rule in CLAUDE.md.

Two model calls: a rewrite under BRIEF, then an editor pass (POLISH) that fixes
only residual tells; the polish result is used only if it also passes checks.

Checks (any failure = exit 1, nothing written unless --write-failed):
  - every href in the original article body/dek is still present
  - every number in the original prose is still present; no new numbers
  - no new URLs
  - word count within +/-25% of the original prose
  - all [[KEEP_n]] placeholders restored exactly once; basic tag balance
Then the offline AI-style detector (skill-library blog-review) scores the
prose before and after; both scores go into the report.

Usage:
  python3 scripts/rewrite_post.py ai-strategy/posts/ai-token-budget.html --out ~/rewrite-pilot
  python3 scripts/rewrite_post.py <post> --in-place          # overwrite the post (batch mode)
  python3 scripts/rewrite_post.py <post> --out DIR --brief-file brief.txt
Env: OPENROUTER_API_KEY (falls back to the last entry in ~/.hermes/.env).
"""
from __future__ import annotations

import argparse
import html as htmllib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

MODEL = "anthropic/claude-opus-5.5"
API = "https://openrouter.ai/api/v1/chat/completions"
DETECTOR = Path.home() / "code/skill-library/creative/blog-review/scripts/ai_style_detector.py"
ALLOWED_DIRS = ("ai-strategy/posts/", "fintech/posts/", "us-asean-china/posts/")

BRIEF = """You are editing an essay by Nicholas Garcia (Lecturer, NUS School of Computing; Deputy Director, NUS FinTech Lab) for his public blog. The current draft was machine-written and reads that way. Rewrite it so it reads like a careful practitioner wrote it by hand: someone who has sat in the procurement meeting, read the regulation, and has a view.

KEEP, exactly:
- The thesis and the order of the argument. You may merge or split paragraphs, but do not add or drop sections, and keep every <h2> (you may reword a heading that is a gimmick).
- Every fact, name, date, figure and number. Copy each number exactly as written (S$3 million stays S$3 million; 24-fold stays 24-fold; 2030 stays 2030). Do not introduce any number that is not in the draft.
- Every link: each <a href="..."> must appear in your output with the same href, attached to the same claim. Add no links.
- Every [[KEEP_n]] placeholder, on its own line, in the same place. They stand for tables and the source list.
- Length between 80% and 110% of the draft. Shorter is fine when you cut rhetoric; do not pad.

ADD nothing: no new facts, examples, firms, statistics, quotes, anecdotes or first-person experiences. If a sentence needs a fact the draft does not have, cut the sentence. No invented scene colour either: no rooms, calls, meetings, desks or people reacting ("nobody in the room", "on the call", "around the table").

YOU MAY CUT AND COMPRESS:
- Compress long enumerations ("plan, call tools, search files, write drafts, check its work...") to the two or three items that carry the point, provided no item holds a fact, number, name or link.
- Delete sentences that are pure rhetoric (a slogan, a restatement of the previous point, a summary line) when they carry no fact, number or link. Every fact, number, name and link must still appear somewhere.

CUT these machine tells wherever they appear:
- Reversal templates: "X, not Y", "it's not X, it's Y", "not just X but Y", "X does not do Y. It does Z." Say the positive claim once. At most one deliberate contrast in the whole piece.
- "X is where Y meets Z" and "X is where Y has to meet Z" sentences, in any form. Say what happens instead.
- Lists of three (and four) used for rhythm. Keep a list only when the items are the actual content; otherwise name the one that matters.
- Runs of short declarative sentences with the same opening ("Users see... Budgets see...", "Regional X still... Regional Y still..."). Staccato drumbeats.
- Aphorism closers and quotable one-liners at the end of paragraphs or the piece ("The goal is...", "That is the real test.", "Winners will..."). End on the last concrete point.
- Throat-clearing and signposting: "Here's the thing", "It is worth noting", "The lesson is", "This matters because", "That shift is useful", "Management sits where these signals meet".
- Gimmick framing where it is forced: ledger, receipt, test, packet, boundary, map, doctrine, theatre, operating object, artifact used as metaphors.
- Em dashes. Use at most two in the whole piece.
- Management uplift vocabulary: leverage, landscape, ecosystem, robust, navigate, unlock, material (as an adjective), legible, discipline (as a slogan).
- Unexplained acronyms: spell out on first use if the draft does.
- Explanatory clinchers: "That is why...", "This is why...", "which is exactly why...", "What X is really doing is...", "X is the wrong response", "the point is". State the reason inside the sentence that needs it.
- Paragraphs that end by restating what the paragraph just said, and paragraphs that summarize a table or list the reader has just read. Delete the restatement.
- A tidy last line. The piece and each section end on a concrete fact, instruction or consequence, never on a balanced, quotable sentence or a list of three adverbs.
- Repeated openings across a sentence or paragraph ("Regional customers still..., regional banks still..., regulators still...") and a first sentence that repeats its heading.
- Headings built on the "The [Adjective] [Noun]" formula. Headings should say what the section claims or covers, in plain words.

WRITE like this:
- Plain, concrete sentences. Prefer the specific noun to the abstract one.
- Vary sentence length on purpose: some long sentences that carry a chain of reasoning with a subordinate clause, some short ones. Avoid a steady medium beat.
- Connect ideas with the logic itself (because, so, which means, by then) rather than with rhythm.
- A practitioner's voice: direct, slightly dry, willing to say "usually" or "in my experience of these decks" only if the draft supports it (it usually does not, so mostly just state things).
- Keep the blockquote if there is one and keep its claim; rephrase it only if it is a slogan. It must repeat a point the body makes, not a new one.
- You may state the author's own judgment in the first person at most once, and not in the last paragraph. Do not use the phrase "my read is". Never invent experiences, clients, meetings or anecdotes.
- Keep the draft's spelling conventions (if it writes "optimize" and "licence", keep both as they are). Do not switch between British and American spelling.
- Test each sentence: would a good Financial Times columnist write it? If it sounds like a slide, a LinkedIn post or a consultant's summary, rewrite it.
- Numbered lists that are real checklists may stay as lists; tighten each item.

FORMAT: return exactly three sections and nothing else:
===TITLE===
KEEP   (or a new title, only if the current title is vague-but-grand: a stranger could not guess the post's content from it)
===DEK===
<the one-paragraph standfirst, plain text, no tags>
===BODY===
<the body HTML using only <p>, <h2>, <h3>, <blockquote>, <ol>, <ul>, <li>, <a href>, <strong>, <em>, and the [[KEEP_n]] lines>
"""

POLISH = """

SECOND PASS. You are now the line editor, not the writer. You receive the ORIGINAL (the source of truth for facts, numbers and links) and a REWRITE. Read the REWRITE as a sceptical magazine editor would. Find the sentences that still sound machine-made: tidy closers, balanced pairs, three-part lists kept for rhythm, sentences that restate a heading or the previous sentence, repeated sentence openings ("X still..., Y still..., Z still..."), "X is where Y meets Z" sentences, invented scene colour ("in the room", "on the call"), stock first-person tics ("My read is"), and any sentence that sounds like a slide. Rewrite only those sentences; leave good sentences alone. Keep every fact, number, link and [[KEEP_n]] placeholder from the ORIGINAL. Return the full piece in the same FORMAT, and nothing else.
"""

# ---------------------------------------------------------------- helpers

def api_key() -> str:
    k = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if k:
        return k
    env = Path.home() / ".hermes/.env"
    last = ""
    if env.exists():
        for line in env.read_text().splitlines():
            if line.startswith("OPENROUTER_API_KEY="):
                last = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not last:
        sys.exit("no OPENROUTER_API_KEY")
    return last


def call_model(system: str, user: str, max_tokens: int = 12000) -> tuple[str, dict]:
    payload = {"model": MODEL, "max_tokens": max_tokens, "temperature": 0.7,
               "messages": [{"role": "system", "content": system},
                            {"role": "user", "content": user}]}
    req = urllib.request.Request(API, data=json.dumps(payload).encode(), method="POST",
                                 headers={"Authorization": f"Bearer {api_key()}",
                                          "Content-Type": "application/json"})
    last_err = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                data = json.loads(r.read())
            msg = data["choices"][0]["message"]["content"]
            if data["choices"][0].get("finish_reason") not in ("stop", "end_turn", None):
                raise RuntimeError(f"finish_reason={data['choices'][0].get('finish_reason')}")
            return msg, data.get("usage", {})
        except (urllib.error.URLError, RuntimeError, KeyError, json.JSONDecodeError) as e:
            last_err = e
            time.sleep(5 * (attempt + 1))
    raise SystemExit(f"model call failed: {last_err}")


def plain(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = htmllib.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def words(s: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][\w'’.-]*", plain(s)))


NUM_RE = re.compile(r"\d+(?:[.,]\d+)*")


def numbers(s: str) -> list[str]:
    return NUM_RE.findall(plain(s))


def hrefs(s: str) -> list[str]:
    return re.findall(r'href="([^"]+)"', s)


def urls(s: str) -> set[str]:
    return set(re.findall(r"https?://[^\s\"'<>)]+", s)) | set(hrefs(s))


def detector(prose_html: str) -> dict:
    if not DETECTOR.exists():
        return {"error": f"detector not found at {DETECTOR}"}
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(prose_html)
        p = f.name
    try:
        out = subprocess.run([sys.executable, str(DETECTOR), p, "--detect-only", "--json"],
                             capture_output=True, text=True, timeout=60)
        rep = json.loads(out.stdout)
        return {"ai_likeness": rep["ai_likeness"], "readability": rep["readability"],
                "tell_count": rep["tell_count"],
                "tells": [f"{t['category']}: {t['match']}" for t in rep["tells"]]}
    except Exception as e:  # noqa: BLE001
        return {"error": str(e)}
    finally:
        os.unlink(p)

# ---------------------------------------------------------------- parse

def split_post(doc: str) -> dict:
    m = re.search(r'<article class="article-body">', doc)
    if not m:
        raise SystemExit("no <article class=\"article-body\">")
    start = m.end()
    end = doc.index("</article>", start)
    body = doc[start:end]

    keeps: list[str] = []

    def stash(mm):
        keeps.append(mm.group(0))
        return f"\n[[KEEP_{len(keeps)}]]\n"

    work = re.sub(r'<div class="article-table-wrap".*?</table>\s*</div>', stash, body, flags=re.S)
    work = re.sub(r"<table.*?</table>", stash, work, flags=re.S)
    work = re.sub(r'<section class="source-notes".*?</section>', stash, work, flags=re.S)
    work = re.sub(r"<(?:figure|pre|script|iframe|svg).*?</(?:figure|pre|script|iframe|svg)>",
                  stash, work, flags=re.S)

    hm = re.search(r"(<h1>)(.*?)(</h1>\s*<p>)(.*?)(</p>)", doc, re.S)
    if not hm:
        raise SystemExit("no <h1> + dek <p>")
    return {"start": start, "end": end, "body": body, "work": work, "keeps": keeps,
            "title": plain(hm.group(2)), "title_html": hm.group(2),
            "dek": hm.group(4), "hm": hm}


def parse_reply(txt: str) -> tuple[str, str, str]:
    m = re.search(r"===TITLE===\s*(.*?)\s*===DEK===\s*(.*?)\s*===BODY===\s*(.*)", txt, re.S)
    if not m:
        raise ValueError("reply missing ===TITLE===/===DEK===/===BODY=== sections")
    body = m.group(3).strip()
    body = re.sub(r"^```(?:html)?\s*|\s*```$", "", body)
    return m.group(1).strip(), m.group(2).strip(), body


def indent_body(body: str, pad: str) -> str:
    out = []
    for line in body.strip().splitlines():
        line = line.strip()
        if line:
            out.append(pad + line)
    return "\n" + "\n\n".join(out) + "\n" + pad[:-2] if out else body

# ---------------------------------------------------------------- checks

def run_checks(orig_prose: str, new_prose: str, orig_all: str, new_all: str,
               n_keeps: int, new_work: str) -> dict:
    res = {"ok": True, "failures": [], "warnings": []}

    def fail(msg):
        res["ok"] = False
        res["failures"].append(msg)

    oh, nh = hrefs(orig_all), hrefs(new_all)
    missing_h = sorted(set(oh) - set(nh))
    if missing_h:
        fail(f"hrefs missing: {missing_h}")
    new_u = sorted(urls(new_all) - urls(orig_all))
    if new_u:
        fail(f"new URLs: {new_u}")

    on, nn = numbers(orig_prose), numbers(new_prose)
    missing_n = sorted(set(on) - set(nn))
    added_n = sorted(set(nn) - set(on))
    if missing_n:
        fail(f"numbers missing: {missing_n}")
    if added_n:
        fail(f"numbers added: {added_n}")

    wo, wn = words(orig_prose), words(new_prose)
    ratio = wn / max(1, wo)
    res["words"] = {"before": wo, "after": wn, "ratio": round(ratio, 3)}
    if not 0.75 <= ratio <= 1.25:
        fail(f"word count {wo} -> {wn} ({ratio:.0%}) outside +/-25%")
    elif not 0.8 <= ratio <= 1.2:
        res["warnings"].append(f"word count ratio {ratio:.0%} outside the +/-20% target")

    for i in range(1, n_keeps + 1):
        c = new_work.count(f"[[KEEP_{i}]]")
        if c != 1:
            fail(f"placeholder [[KEEP_{i}]] appears {c} times")
    for tag in ("p", "h2", "h3", "blockquote", "ol", "ul", "li", "a", "strong", "em"):
        o = len(re.findall(rf"<{tag}[\s>]", new_work))
        c = len(re.findall(rf"</{tag}>", new_work))
        if o != c:
            fail(f"unbalanced <{tag}>: {o} open / {c} close")
    bad = sorted(set(re.findall(r"</?([a-zA-Z0-9]+)", new_work)) -
                 {"p", "h2", "h3", "blockquote", "ol", "ul", "li", "a", "strong", "em", "code", "br"})
    if bad:
        fail(f"disallowed tags in model body: {bad}")
    oh2 = len(re.findall(r"<h2", orig_prose))
    nh2 = len(re.findall(r"<h2", new_prose))
    if oh2 != nh2:
        res["warnings"].append(f"h2 count {oh2} -> {nh2}")
    return res

# ---------------------------------------------------------------- main

def rewrite(path: Path, brief: str, repair_rounds: int = 1, polish: bool = True) -> dict:
    doc = path.read_text(encoding="utf-8")
    sp = split_post(doc)
    orig_prose = sp["dek"] + "\n" + re.sub(r"\[\[KEEP_\d+\]\]", "", sp["work"])
    orig_all = sp["dek"] + sp["body"]

    user = (f"Current title: {sp['title']}\n\n===DEK===\n{plain(sp['dek'])}\n\n"
            f"===BODY===\n{sp['work'].strip()}\n")
    usage_total = {"prompt_tokens": 0, "completion_tokens": 0, "cost": 0.0}
    messages_user = user
    checks = None
    new_prose, new_body, title, dek = "", sp["body"], "KEEP", sp["dek"]
    for rnd in range(repair_rounds + 1):
        reply, usage = call_model(brief, messages_user)
        for k in usage_total:
            usage_total[k] += usage.get(k, 0) or 0
        try:
            title, dek, new_work = parse_reply(reply)
        except ValueError as e:
            checks = {"ok": False, "failures": [str(e)], "warnings": []}
            messages_user = user + f"\n\nYour previous reply was unusable: {e}. Follow FORMAT exactly."
            continue
        new_body = new_work
        for i, block in enumerate(sp["keeps"], 1):
            new_body = new_body.replace(f"[[KEEP_{i}]]", block)
        new_prose = htmllib.escape(dek, quote=False) + "\n" + re.sub(r"\[\[KEEP_\d+\]\]", "", new_work)
        new_all = dek + new_body
        checks = run_checks(orig_prose, new_prose, orig_all, new_all, len(sp["keeps"]), new_work)
        checks["round"] = rnd
        if checks["ok"]:
            break
        messages_user = (user + "\n\nA previous attempt failed these mechanical checks; fix them "
                         "while keeping the style brief:\n- " + "\n- ".join(checks["failures"]))

    # polish pass: an editor's second read that targets the residual tells only.
    checks = checks or {"ok": False, "failures": ["no reply"], "warnings": []}
    checks["polish"] = "skipped"
    if polish and checks["ok"]:
        draft = f"===TITLE===\n{title}\n===DEK===\n{dek}\n===BODY===\n{new_work}\n"
        p_reply, usage = call_model(brief + POLISH, "ORIGINAL (for facts, numbers, links):\n" + user +
                                    "\n\nREWRITE TO POLISH:\n" + draft)
        for k in usage_total:
            usage_total[k] += usage.get(k, 0) or 0
        try:
            p_title, p_dek, p_work = parse_reply(p_reply)
            p_body = p_work
            for i, block in enumerate(sp["keeps"], 1):
                p_body = p_body.replace(f"[[KEEP_{i}]]", block)
            p_prose = htmllib.escape(p_dek, quote=False) + "\n" + re.sub(r"\[\[KEEP_\d+\]\]", "", p_work)
            p_checks = run_checks(orig_prose, p_prose, orig_all, p_dek + p_body, len(sp["keeps"]), p_work)
            if p_checks["ok"]:
                p_checks["round"] = checks["round"]
                checks = p_checks
                checks["polish"] = "applied"
                title, dek, new_work, new_body, new_prose = p_title, p_dek, p_work, p_body, p_prose
            else:
                checks["polish"] = "rejected (kept pass-1): " + "; ".join(p_checks["failures"])
        except ValueError as e:
            checks["polish"] = f"rejected (kept pass-1): {e}"

    # assemble
    pad_m = re.search(r"\n([ \t]*)<", sp["body"])
    pad = pad_m.group(1) if pad_m else "        "
    new_doc = doc[:sp["start"]] + indent_body(new_body, pad) + doc[sp["end"]:]
    hm = re.search(r"(<h1>)(.*?)(</h1>\s*<p>)(.*?)(</p>)", new_doc, re.S)
    new_doc = new_doc[:hm.start(4)] + htmllib.escape(dek, quote=False) + new_doc[hm.end(4):]
    title_changed = title and title.upper() != "KEEP" and title != sp["title"]
    if title_changed:
        esc = htmllib.escape(title, quote=False)
        new_doc = new_doc.replace(f"<h1>{sp['title_html']}</h1>", f"<h1>{esc}</h1>", 1)
        new_doc = re.sub(r"<title>.*?(\s\|[^<]*)?</title>",
                         lambda m: f"<title>{esc}{m.group(1) or ''}</title>", new_doc, count=1)
        new_doc = re.sub(r'(<meta property="og:title" content=")[^"]*(")',
                         lambda m: m.group(1) + htmllib.escape(title) + m.group(2), new_doc)

    return {"doc": new_doc, "orig_doc": doc, "checks": checks, "usage": usage_total,
            "title_before": sp["title"], "title_after": title if title_changed else sp["title"],
            "orig_prose": orig_prose, "new_prose": new_prose,
            "detector_before": detector(orig_prose),
            "detector_after": detector(new_prose) if checks and checks.get("words") else None}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("post", help="post path relative to repo root (or absolute)")
    ap.add_argument("--out", help="directory for <slug>.before.html / .after.html / .report.json")
    ap.add_argument("--in-place", action="store_true", help="overwrite the post (only if checks pass)")
    ap.add_argument("--brief-file", help="override the built-in rewrite brief")
    ap.add_argument("--repair-rounds", type=int, default=1)
    ap.add_argument("--src-root", help="treat this dir as the repo root (for copies outside the repo)")
    ap.add_argument("--no-polish", action="store_true", help="skip the second (editor) pass")
    ap.add_argument("--write-failed", action="store_true", help="write output even if checks fail")
    a = ap.parse_args()

    root = Path(a.src_root).expanduser().resolve() if a.src_root else Path(__file__).resolve().parents[1]
    path = Path(a.post)
    if not path.is_absolute():
        path = root / path
    rel = str(path.resolve().relative_to(root)) if str(path.resolve()).startswith(str(root)) else str(path)
    if not rel.startswith(ALLOWED_DIRS):
        sys.exit(f"refusing: {rel} is not in {ALLOWED_DIRS}")
    if not (a.out or a.in_place):
        sys.exit("give --out DIR or --in-place")

    brief = Path(a.brief_file).read_text() if a.brief_file else BRIEF
    r = rewrite(path, brief, a.repair_rounds, not a.no_polish)
    slug = path.stem
    report = {"post": rel, "model": MODEL, "checks": r["checks"], "usage": r["usage"],
              "title_before": r["title_before"], "title_after": r["title_after"],
              "detector_before": r["detector_before"], "detector_after": r["detector_after"]}
    ok = bool(r["checks"] and r["checks"]["ok"])
    if a.out:
        out = Path(a.out).expanduser()
        out.mkdir(parents=True, exist_ok=True)
        (out / f"{slug}.report.json").write_text(json.dumps(report, indent=2))
        (out / f"{slug}.before.html").write_text(r["orig_doc"])
        if ok or a.write_failed:
            (out / f"{slug}.after.html").write_text(r["doc"])
    if a.in_place and ok:
        path.write_text(r["doc"], encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not ok:
        print("CHECKS FAILED: " + "; ".join(r["checks"]["failures"] if r["checks"] else ["no reply"]),
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
