#!/usr/bin/env python3
"""Selftest for the ISA wireframe set.

Checks:
1. Every wireframe page declared in the generator exists on disk.
2. Every link in index.html resolves to a file that exists.
3. Every wireframe page names at least one backing wave-2 module.
4. The portal ISA venture page links every wireframe, and those links resolve.

Exit 0 = pass. Exit 1 = fail, with one line per failure.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
VENTURE = os.path.join(ROOT, "content", "ventures", "isa.md")
MODULES = {"matching", "contracts", "ledger", "verification", "reporting"}

fails = []
checks = 0


def check(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)


# 1. declared pages exist
sys.path.insert(0, HERE)
import gen_wireframes as gen  # noqa: E402

declared = [p["slug"] + ".html" for p in gen.PAGES]
check(len(declared) > 0, "generator declares no pages")
for fn in declared:
    check(os.path.isfile(os.path.join(HERE, fn)), "missing wireframe: %s" % fn)
check(os.path.isfile(os.path.join(HERE, "index.html")), "missing index.html")

# 2. index links resolve, and cover every declared page
index = open(os.path.join(HERE, "index.html")).read()
linked = re.findall(r'href="([^"]+)"', index)
for href in linked:
    check(os.path.isfile(os.path.join(HERE, href)),
          "index link does not resolve: %s" % href)
for fn in declared:
    check(fn in linked, "index does not link: %s" % fn)

# 3. every page names a backing module in its footer
for fn in declared:
    body = open(os.path.join(HERE, fn)).read()
    foot = re.search(r"<footer>(.*?)</footer>", body, re.S)
    check(foot is not None, "%s has no footer" % fn)
    if not foot:
        continue
    text = foot.group(1)
    check("Backed by wave-2 module" in text,
          "%s footer does not name a backing module" % fn)
    named = {m for m in MODULES if re.search(r"<b>%s</b>" % m, text)}
    check(bool(named), "%s names no known wave-2 module" % fn)

# 4. the portal ISA venture page links every wireframe
check(os.path.isfile(VENTURE), "missing portal page: content/ventures/isa.md")
if os.path.isfile(VENTURE):
    md = open(VENTURE).read()
    check("ISA production wireframes" in md,
          "venture page lacks the 'ISA production wireframes' section")
    md_links = re.findall(r"\]\((\.\./\.\./wireframes/isa/[^)]+)\)", md)
    for rel in md_links:
        target = os.path.normpath(
            os.path.join(os.path.dirname(VENTURE), rel))
        check(os.path.isfile(target), "venture link does not resolve: %s" % rel)
    for fn in declared + ["index.html"]:
        check(any(l.endswith("/" + fn) for l in md_links),
              "venture page does not link: %s" % fn)

if fails:
    print("FAIL — %d of %d checks failed" % (len(fails), checks))
    for f in fails:
        print("  -", f)
    sys.exit(1)
print("PASS — %d checks, %d wireframe pages" % (checks, len(declared)))
