# Ground brief — stablecoin-reserves-attestation

**Status:** grounded (2026-07-31)  
**Vertical:** fintech  
**Claim (particular):** For fiat-backed payment stablecoins, the product is not the token. It is the reserve composition, segregation, redemption rights, and attestation regime — because markets reprice the liability when reserve quality or access fails, even when a marketing page says “fully backed.”

## Who is arguing what

| Actor | Position | Source |
|-------|----------|--------|
| NYDFS (Adrienne Harris guidance, 8 Jun 2022) | DFS-supervised USD stablecoins need redeemability, segregated reserves, monthly independent CPA attestations (AICPA standards) | https://www.dfs.ny.gov/industry_guidance/industry_letters/il20220608_issuance_stablecoins |
| Circle (USDC issuer) | Monthly third-party assurance that reserves ≥ circulation; weekly reserve disclosure; 1:1 redeemability claim | https://www.circle.com/transparency |
| Fed researchers (FEDS Note, SVB/USDC) | Circle disclosed ~$3.3B (~8%) of USDC reserves stuck at SVB; redemption pressure followed disclosure | https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html |
| CRS / academic post-mortems (Terra UST) | Algorithmic “stable” designs without liquid redeemable reserves failed in May 2022 | CRS IN11928; Richmond Fed Economic Brief |

## Facts that must appear in the essay (with support)

1. **NYDFS June 2022 guidance requires full backing, redeemability, and monthly independent CPA attestations** for DFS-supervised USD stablecoins.  
   Supports: NYDFS industry letter / press release 8 Jun 2022.

2. **Attestations are point-in-time examinations of management assertions under AICPA standards — not a full risk audit of the issuer.**  
   Supports: NYDFS guidance text; Circle transparency page (monthly assurance language).

3. **USDC secondary market depegged in March 2023 after Circle disclosed $3.3B of reserves at failed Silicon Valley Bank (~8% of then-reserves).**  
   Supports: Circle press room 13 Mar 2023; Fed FEDS Note; Reuters/CNBC contemporaneous coverage.

4. **TerraUSD (UST) collapsed in May 2022 as an algorithmic design without cash-equivalent redeemable reserves of the NYDFS type.**  
   Supports: CRS Algorithmic Stablecoins and the TerraUSD Crash (May 2022); Richmond Fed Economic Brief.

5. **Circle publishes monthly examination reports and describes reserves held separately for holders (cash / cash equivalents / Circle Reserve Fund).**  
   Supports: circle.com/transparency.

## Theory hook

- Bank-run / money-like liability theory: first-mover redemption when confidence in backing fails (Diamond–Dybvig style dynamics applied to private digital money).
- Disclosure as product quality: attestation cadence, scope, and lag are features users (and integrators) are buying.

## Real case used in draft (not invented)

| Case | What it establishes | Source |
|------|---------------------|--------|
| USDC–SVB March 2023 | Attested “backed” reserves can still face access risk at the deposit bank; market price reacted to reserve-path news | Circle primary + Fed note |
| Terra UST May 2022 | Without redeemable liquid reserves, “stable” branding failed under run | CRS / Richmond Fed |

## Retrieval gaps

- Exact secondary-market low print for USDC varies by venue (~$0.87–0.88 cited in press); use “below par / sub-90¢ range” with attributed press if needed.
- GENIUS Act federal stablecoin framework exists in parallel; this memo stays on attestation/reserve product design, not full federal comparison.
- Tether/USDT attestation cadence differs; do not over-claim symmetry without primary report.

## Source test (must pass)

Every Source note must answer: *which sentence fails if this URL is removed?*
