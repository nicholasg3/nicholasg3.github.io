# Strategy Publisher Publishing Handoff

## Recommended Public URL

Use Nick's existing GitHub Pages blog path:

`https://nicholasg3.github.io/blog/`

Nick rejected creating a dedicated `strategy-publisher` repo. Keep this package as the local source artifact, and publish only through an explicitly approved patch/push path into the external Pages source that serves `/blog/`.

## Source Package

Publish the contents of this `gh-pages/` directory as the website root:

- `index.html`
- `launch-bundle.html`
- `styles.css`
- `feed.xml`
- `.nojekyll`
- `README.md`
- `PUBLISHING_HANDOFF.md`
- `posts/ai-strategy-doctrine-before-tools.html`
- `posts/ai-workflow-investment-screen.html`
- `posts/ai-vendor-warning-label.html`
- `posts/ai-management-layer.html`
- `posts/ai-strategy-theatre-test.html`
- `posts/ai-data-center-veto.html`
- `posts/ai-quality-test.html`
- `posts/ai-herding-problem.html`
- `posts/ai-payback-ledger.html`
- `posts/ai-evidence-packet.html`
- `posts/stablecoin-distribution-test.html`
- `posts/asean-market-entry-test.html`
- `posts/founder-distribution-ledger.html`
- `posts/ai-productivity-receipt.html`
- `posts/ai-token-budget.html`
- `posts/ai-work-cadence.html`
- `posts/ai-agent-permission-ledger.html`
- `posts/ai-evaluation-gap.html`
- `posts/ai-disclosure-ledger.html`
- `posts/agent-identity-boundary.html`
- `posts/ai-distribution-boundary.html`
- `posts/ai-productivity-gap.html`
- `posts/ai-model-mix-ledger.html`
- `posts/ai-memory-ledger.html`
- `posts/ai-slop-audit.html`
- `posts/ai-audience-ledger.html`
- `posts/ai-control-gap-ledger.html`
- `posts/ai-source-rights-ledger.html`
- `posts/ai-browser-boundary.html`
- `posts/ai-coverage-gap.html`
- `posts/ai-disclosure-clock.html`
- `posts/agents-need-memory-architecture.html`

## Deployment Options

### Option A: Existing Pages Blog Path

Status: preferred path, but blocked until Nick explicitly approves a specific patch/push into the external Pages source.

1. Use the public Pages source that serves `https://nicholasg3.github.io/blog/`.
2. Copy every file from this `gh-pages/` directory into the approved blog source path.
3. Commit and push to `main`.
4. Confirm the site opens at `https://nicholasg3.github.io/blog/`.

Launch inventory note: Nick's current rule is at least five public articles before launch or partner sharing. This package now contains thirty local articles plus a curated launch-bundle index after Cycle 92. It is launch-inventory ready locally, but still requires explicit approval before any external Pages patch/push and must pass the live smoke test after publication.

### Option B: Local Review Only

If no external patch/push approval is granted, keep this as a local review artifact:

Open `index.html` locally and review the package without publication.

## Local Boundary Note

Auto Company did not push or configure GitHub Pages in this cycle. Nick has clarified that GitHub CLI auth on the droplet is valid with repo scope, but also rejected creating `nicholasg3/strategy-publisher`. The remaining blocker is explicit approval for the exact external Pages source/path that serves `/blog/`.

Required approval request:

Approve Auto Company to copy the verified patch tree into `/home/nicholas/ai-agents-workspace/docs/blog/`, commit only `docs/blog/` in that parent repo, push, and smoke-test `https://nicholasg3.github.io/blog/`.

Detailed approval brief:

`docs/operations/cycle-14-publication-approval-brief.md`

## Pre-Push Checklist

- From `projects/strategy-publisher/`, run `./release/check-publication-ready.sh` for the full local release gate. It verifies the package, rebuilds the `docs/blog/` patch tree, rejects unexpected files, and reports the latest archive.
- From `projects/strategy-publisher/`, run `./release/verify-gh-pages-package.sh`.
- If Nick needs a ready-to-apply local patch kit, run `./release/build-docs-blog-patch.sh`; it writes `/tmp/strategy-publisher-docs-blog-patch/docs/blog/` and a timestamped archive under `release/`.
- Open `index.html` locally and read the homepage.
- Open `launch-bundle.html` locally and confirm the eight-article reading path is the correct first-share page after launch.
- Open all article pages.
- Confirm the homepage and RSS include Issue 028, `The AI Source Rights Ledger`, with Issue 027 preserved in the archive.
- Check `feed.xml` uses the intended final public URL.
- Confirm the `$19/mo` CTA is acceptable as a manual reply path before adding Substack or checkout plumbing.
- Keep the full Issue 002 article public; sell the worksheet/pilot pack as the paid layer.

## Approved Apply Sequence

Only run this after the approval above is granted.

1. From `projects/strategy-publisher/`, run `./release/check-publication-ready.sh`.
2. Copy the generated `/tmp/strategy-publisher-docs-blog-patch/docs/blog/` tree to `/home/nicholas/ai-agents-workspace/docs/blog/`.
3. In `/home/nicholas/ai-agents-workspace`, inspect `git status --short`.
4. Stage only `docs/blog/`.
5. Commit with a message equivalent to `Publish Strategy Publisher blog`.
6. Push the parent repo.
7. Smoke-test the homepage, launch-bundle page, Issue 002 page, Issue 003 page, Issue 004 page, Issue 005 page, Issue 006 page, Issue 007 page, Issue 008 page, Issue 009 page, Issue 010 page, Issue 011 page, Issue 012 page, Issue 013 page, Issue 014 page, Issue 015 page, Issue 016 page, Issue 017 page, Issue 018 page, Issue 019 page, Issue 020 page, Issue 021 page, Issue 022 page, Issue 023 page, Issue 024 page, Issue 025 page, Issue 026 page, Issue 027 page, Issue 028 page, feed, and CSS after Pages propagation.

Do not stage unrelated parent-repo changes.

## Rollback

If the live smoke test fails after push, revert only the parent-repo commit that touched `docs/blog/`, push the revert, and record the failed archive plus smoke-test result in Auto Company consensus before attempting another publish.

## Post-Live Conversion Path

- Official first channel after the site is live: Substack.
- Interim fallback, only if Substack setup is delayed and explicitly desired: stablecoin-gated access to the paid pack.
- Do not add live payment or mailing-list plumbing inside this static package before the public site is smoke-tested.
