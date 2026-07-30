# Prose rewrite pass (fixed step 4b)

## Why

First-pass generation (research → draft) produces stiff, AI-sounding prose.
Rewriting **already-generated** copy into AP/Grok feature voice is what works.
This pass is **mandatory** after every draft and after every fleet generate.

## Instructions for rewrite agents

For each assigned HTML path:

1. Read the full file.
2. Read the voice model:
   `us-asean-china/staging/posts/english-language-founder-media-vs-local-language-c.html`
3. Rewrite the **article body prose** (deck under H1, paragraphs under H2s, blockquote if present, closing paragraphs).
4. **Preserve:** all facts, numbers, dates, institution names, hyperlinks, table content, real cases, Source notes URLs, side-card labels (may polish card text).
5. **Cut:** not-X-but-Y stacks, “what this is not,” meta hedges, second-person coaching, list camouflage, breathless clinchers.
6. **Ban “operators” / “operator”** as a generic subject (AI-coded). Name the actor: bank, founder, firm, company, regulator, customer, merchant, board, team.
7. **Aim for:** short active sentences, attributed numbers, continuous paragraphs under a few solid H2s, news lead where it fits.
7. Overwrite the same HTML path. No commit.

## Done

Return `REWRITTEN: slug` for each file, or `BLOCKED: slug — reason`.
