# Ground brief — insurance-for-smart-contract-oracle-failure

**Status:** grounded (2026-07-31)  
**Vertical:** fintech  
**Rank:** 27  
**Claim (particular):** Cover for smart-contract and **oracle failure** only works when the **trigger is explicit** in the cover wording. Most buyers treat “DeFi insurance” as a complete map of protocol risk; in practice, products are **imperfect maps** — discretionary mutuals define covered event classes (exploit, oracle manipulation/failure, governance attack) and exclude pure market moves unless the oracle path is defined.

## Who is arguing what

| Actor | Position | Source |
|-------|----------|--------|
| Nexus Mutual | Protocol Cover includes smart contract hacks/exploits, oracle manipulation or failure, liquidation failure, governance takeovers; mutual has paid claims historically | https://docs.nexusmutual.io/overview/cover-products/ ; nexusmutual.io product pages |
| Nexus Mutual / OpenCover risk taxonomy | Onchain risk map separates smart-contract, oracle, governance, depeg, custody, etc. | Nexus “State of Crypto Insurance” / product taxonomy |
| Traditional IAIS / insurance theory | Insurance needs insurable interest, trigger clarity, and basis-risk management | IAIS hub is weak as sole source — use as sector context only if a specific paper is cited |

## Facts that must appear in the essay (with support)

1. **Nexus Mutual Protocol Cover wording lists oracle failure/manipulation among covered loss-event classes (alongside smart-contract exploits, liquidation failure, governance takeovers).**  
   Supports: Nexus Mutual docs cover-products page; product listing language.

2. **Nexus Mutual reports cumulative claims paid (e.g. >$18.5 million cited on mutual materials) and large historical cover amounts — use as evidence the market exists and pays, not as a solvency rating.**  
   Supports: Nexus Mutual marketing/report pages with those figures (attribute to the mutual).

3. **Cover products explicitly separate market price movements from oracle-driven losses** (market moves generally excluded unless caused by oracle failure/manipulation as defined).**  
   Supports: OpenCover / Nexus product language on exclusions.

4. **Discretionary mutuals are not the same as regulated insurance carriers** — governance of claims assessment is part of the product.  
   Supports: Nexus “State of Crypto Insurance” distinction between regulated insurance and discretionary mutuals.

## Theory hook

- **Basis risk:** mismatch between economic loss and contractual trigger.
- **Operational risk of oracles** as external data dependency of automated markets.
- **Parametric vs indemnity-style cover** on-chain (claims assessment processes).

## Real case used in draft (not invented)

| Case | What it establishes | Source |
|------|---------------------|--------|
| Nexus Mutual Protocol Cover product definition | Oracle failure/manipulation is a named covered class | Nexus docs |
| Mutual claims-paid history (aggregate) | Cover market has paid real claims since 2019 | Nexus materials |

Do **not** invent a paid claim for a specific oracle event without a primary claim report URL. Prefer product wording + aggregate claims stats.

## Retrieval gaps

- Individual historical claim PDFs (e.g. specific exploit years) not all re-verified URL-stable in this session — avoid naming a claim amount for a specific protocol unless linked.
- IAIS has no DeFi oracle standard; do not fake a global insurance standard for smart contracts.
- Traditional specialty crypto policies from admitted carriers are heterogeneous and often non-public — say so.

## Source test (must pass)

Every Source note must answer: *which sentence fails if this URL is removed?*
