# Ground brief — tokenized-bank-money-correspondent-banking

**Status:** grounded (2026-08-03)
**Vertical:** fintech
**Context:** publishes ahead of Nick's 6 Aug 2026 NUS FinTech Lab podcast with Hassan Ahmed (Coinbase); analytical, not adversarial.
**Claim (particular):** Tokenization does not solve payments interoperability, because money stays an issuer-specific liability. Moving value between issuers still needs one of: a bilateral acceptance arrangement (nostro/vostro by another name), an exchange/market-maker spread, or redemption through the legacy banking layer. Settlement gets faster; the topology of who trusts whom does not change. The three live architectural answers — consortium coin, dominant single coin, bridging/interoperability layer — each implicitly concede this. A bank-consortium stablecoin (OUSD) solves fragmentation by merging trust among issuers, not by protocol innovation.

## Who is arguing what

| Actor | Position | Source |
|---|---|---|
| BIS (Annual Economic Report 2025, Ch. III) | Tokenization keeps the two-tier structure (central bank reserves / commercial bank money); singleness of money still depends on all issuers meeting the same regulatory standard, not on the token format | bis.org/publ/arpdf/ar2025e3.htm |
| BIS Innovation Hub / Project Agorá (with IIF and 7-8 central banks) | Tested whether a unified ledger can compress correspondent-banking messaging, compliance and settlement into one step; real-value test (Jul 2026) still ran through participating commercial banks acting as intermediaries, alongside central banks | bis.org/press/p260527.htm; coindesk.com Jul 30 2026 report |
| IMF (Fintech Note 26/01, "Tokenized Finance," Apr 2026) | Tokenization is a structural shift, not a marginal efficiency gain, but its success depends on anchoring in public trust, safe settlement assets and legal certainty across jurisdictions — i.e., trust design, not code | imf.org/en/publications/imf-notes/issues/2026/04/01/tokenized-finance-574921 |
| MAS (BLOOM initiative, launched Oct 2025) | Frames its own initiative around distribution/clearing of settlement assets plus programmable compliance controls — i.e., who is allowed to move value and under what checks — rather than a single token replacing bank money | mas.gov.sg/news/media-releases/2025/mas-launches-bloom-initiative-to-extend-settlement-capabilities |
| Christian Catalini (Forbes, 30 Jun 2026) | Argues OUSD wins not because of better cryptography but because 140+ competing firms agreed to back the same issuer and governance structure — an explicit merger of trust, marketed as an "open standard" | forbes.com/sites/christiancatalini/2026/06/30/why-an-open-standard-will-win-the-stablecoin-race |
| US Congress (GENIUS Act, S.1582, §12) | Interoperability is not automatic even inside a single regulatory regime: regulators must first assess, then may prescribe, compatibility standards between competing stablecoin issuers | congress.gov/bill/119th-congress/senate-bill/1582; house financial services section-by-section (2025-07-10); Gibson Dunn summary |
| Gorton & Zhang, "Taming Wildcat Stablecoins" (Univ. Chicago L. Rev. 90(3), 2023) | Stablecoins recreate free-banking-era private money: acceptance at par is not automatic across issuers absent a common backstop, historically resolved by note-clearing arrangements or a central bank, not by technology | chicagounbound.uchicago.edu/uclrev/vol90/iss3/3 |

## Facts that must appear (with support)

1. **Project Agorá completed real-value testing on 30 July 2026: roughly CHF 800,000 (~USD 1 million) moved across six currencies (USD, EUR, GBP, JPY, CHF, KRW) by 28 commercial banks and 5 central banks, settling roughly 30 transactions in about 80 seconds on average.**
   Supports: coindesk.com report dated 30 Jul 2026, confirmed via direct fetch. Also cross-referenced by financefeeds.com and blockhead.co ("Twenty-Eight Banks Move Real Tokenized Money Across Borders"). The coindesk fetch confirms the CHF figure, currency list, bank count and average settlement time directly; used as the primary real-case number rather than the earlier May 2026 prototype figures (7-8 central banks, "more than 40" institutions, no dollar figure), which describe an earlier phase of the same project.

2. **BIS's own worked example (Annual Economic Report 2025, Chapter III, Graph 5) uses a $100 US-to-Korea payment to show that even tokenized commercial bank money keeps settlement inside each jurisdiction's central bank reserves; no money literally crosses the border, and coordinating the two domestic settlement legs still requires message exchange between the intermediating institutions.**
   Supports: direct fetch of bis.org/publ/arpdf/ar2025e3.htm, which returned the $100 US manufacturer / Korean supplier example and the line "No money moves across borders; settlement in central bank reserves occurs entirely within the United States." Chapter title confirmed as "III. The next-generation monetary and financial system."

3. **BIS states that singleness between private tokenized money and cash "is supported in the same way it is now for commercial bank deposits" and "requires that all private tokenised money issuers comply with the same regulatory standards" — i.e., trust in tokenized money is inherited from bank regulation, not created by the ledger.**
   Supports: same bis.org/publ/arpdf/ar2025e3.htm fetch, direct quote.

4. **OUSD ("Open USD"), announced 30 June 2026 through a new entity called Open Standard, is backed by more than 140 competing companies — including Visa, Mastercard, American Express, Stripe, BlackRock, Coinbase, Google and BNY — and is explicitly framed by economist Christian Catalini (a Libra alumnus) as solving fragmentation through shared governance among issuers, not new cryptography.**
   Supports: Forbes piece by Catalini (30 Jun 2026), fetched directly; corroborated in search snippets by Fortune, PYMNTS and Yahoo Finance coverage of the same launch. Catalini's own framing: OUSD "revives Libra's vision for a unified, open protocol" and wins because competitors "agree to a standard" rather than because of a technical breakthrough. Zach Abrams (Bridge co-founder) named as interim CEO of Open Standard.

5. **GENIUS Act §12 does not assume interoperability between competing US-regulated stablecoin issuers; it requires federal regulators to first assess whether technical compatibility standards are even necessary, in consultation with NIST, before they may prescribe them.**
   Supports: WebSearch synthesis of congress.gov S.1582 text and a Gibson Dunn summary, cross-checked against two independent secondary summaries (search results converged on identical language: regulators "may... prescribe technical standards... to promote compatibility and interoperability," conditioned on an assessment). Direct WebFetch of congress.gov and the House Financial Services section-by-section PDF both returned 403 (bot-blocked); claim rests on converged secondary sourcing rather than a single primary-text quote — flagged as a retrieval gap. Section 12 title and substance were corroborated independently by two separate WebSearch passes returning consistent section numbering, which is treated as sufficient given the convergence.

6. **MAS's BLOOM initiative (launched October 2025) structures its own multi-currency settlement effort around "distribution and clearing of settlement assets" and "programmable controls," with named participants (Circle, Coinbase, DBS, OCBC, UOB, Partior, Stripe, Ant International, StraitsX) split across those workstreams — i.e., even a regulator-convened initiative treats "who clears for whom, under what compliance check" as the open design question, not the token format.**
   Supports: MAS press release (mas.gov.sg/news/media-releases/2025/mas-launches-bloom-initiative-to-extend-settlement-capabilities), corroborated by fintechnews.sg and technode.global summaries.

7. **Gorton and Zhang's "Taming Wildcat Stablecoins" argues stablecoins structurally resemble pre-Civil-War US banknotes: privately issued money that did not trade at par across issuers absent a common clearing or backstop mechanism, historically resolved through note-clearing associations or eventually a central bank — not through better paper.**
   Supports: SSRN abstract (papers.ssrn.com/sol3/papers.cfm?abstract_id=3888752) and University of Chicago Law Review publication record (chicagounbound.uchicago.edu/uclrev/vol90/iss3/3), both confirmed via WebSearch; used as the load-bearing historical/theory analogy for why fragmentation among issuers is a trust problem, resolved historically by institutional consolidation (clearinghouses, then a central bank), not by a superior settlement rail.

## Theory anchors used (3)

- **Gorton & Zhang, "Taming Wildcat Stablecoins," University of Chicago Law Review 90(3), 909 (2023).** Load-bearing anchor. Stablecoin fragmentation mirrors free-banking-era private money; par acceptance across issuers was never automatic and was historically resolved by clearing arrangements or a central backstop, not by the notes themselves getting better.
- **Gorton & Pennacchi, "Financial Intermediaries and Liquidity Creation," Journal of Finance 45(1), 49-71 (1990).** Explains why "informationally insensitive" debt (bank deposits, and by extension a tokenized deposit) is valuable specifically because uninformed counterparties do not have to investigate the issuer before accepting it at par — the trust, not the settlement medium, is the scarce asset being reproduced across every issuer that wants its liabilities accepted elsewhere.
- **Kahn & Roberds, "Why Pay? An Introduction to Payments Economics," Journal of Financial Intermediation 18(1), 1-23 (2009).** Survey framing for why payment arrangements are a joint economic design problem (credit risk, finality, information) and not a pure engineering problem — used to support the claim that faster settlement rails do not by themselves resolve the underlying credit-risk allocation between issuers.

## Real case

Project Agorá, BIS-led with the Institute of International Finance: prototype phase (May 2026, 7-8 central banks + "more than 40" private institutions) followed by a real-value test on 30 July 2026 (28 commercial banks, 5 central banks, ~CHF 800,000 across six currencies, ~80 second average settlement). Used as the concrete example that faster, single-ledger settlement still runs through named intermediating commercial banks, not around them.

## What this brief does not establish

- No specific dollar loss, fee, or delay figure for the BIS $100 example beyond the qualitative description BIS itself gives (multiple message exchanges, in-jurisdiction settlement legs); BIS's public chapter does not quote an exact fee or day-count for that example, so none is invented in the draft.
- No claim that OUSD has launched publicly or settled live volume; as of the sourced coverage (late June/July 2026) it is an announced consortium with named backers, going live "later in 2026" across Solana, Stellar, Base and Polygon — the draft treats it as an announced architecture, not a live settlement system.
- No claim about which of the three architectures (consortium coin, dominant single coin, bridging layer) will "win" — the brief and draft treat them as three coexisting live answers, not a forecast.
- Carstens/Shin individually authored BIS speeches on tokenization and the "finternet" were searched for but not independently fetched and verified this session; dropped rather than cited unverified. The BIS Annual Economic Report 2025 Chapter III (a BIS institutional publication) is used instead, since it was directly fetched and quoted.
- Star & Ruhleder (1996) "Steps Toward an Ecology of Infrastructure" and Bech & Garratt (BIS "money flower" taxonomy) were considered as additional theory anchors per the task brief but not verified via fetch or search this session; dropped per source policy rather than cited unverified. Three verified anchors (Gorton & Zhang; Gorton & Pennacchi; Kahn & Roberds) are used instead.

## Retrieval gaps

- congress.gov (S.1582 bill page) and financialservices.house.gov (section-by-section PDF) both returned HTTP 403 on direct WebFetch (bot-blocked). GENIUS Act §12 language rests on two independent WebSearch-synthesized passes that converged on identical section numbering and near-identical language, plus a DLA Piper explainer confirming the interoperability provision's substance (title of section not confirmed in that fetch). Flagged for re-verification against a primary congress.gov text mirror if available.
- BIS press release (bis.org/press/p260527.htm, 27 May 2026 prototype) did not disclose a real-value dollar figure or currency list; those numbers come from the 30 July 2026 real-value test instead, reported by coindesk.com and corroborated by financefeeds.com/blockhead.co. The two BIS-related events (May prototype vs. July real-value test) are kept distinct in the draft rather than merged.
- IMF Fintech Note 26/01 was confirmed by title, number and date via WebSearch and the imf.org publication-page URL, but the full PDF text was not directly fetched (not attempted after 403 pattern on adjacent primary-document fetches); only the note's title, number, date and general thesis (tokenization as structural shift dependent on trust anchoring) are used, not any specific figure from inside it.

## Source test (must pass)

Every Source Note in the draft must answer: *which sentence fails if this URL is removed?* Applied in the HTML draft's Source Notes section below.
