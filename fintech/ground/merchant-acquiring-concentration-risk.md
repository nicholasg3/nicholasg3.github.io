# Ground brief — merchant-acquiring-concentration-risk

**Status:** grounded (2026-07-31)  
**Vertical:** fintech  
**Claim (particular):** Digital commerce depends on a thin set of acquirers, card networks, and cloud hosts; merchant-acquiring concentration is operational risk, not only pricing power — rankings and infrastructure outages show correlated checkout failure when one path breaks.

## Who is arguing what

| Actor | Position | Source |
|-------|----------|--------|
| Nilson Report / Fiserv IR | Fiserv ranked No. 1 US merchant acquirer by purchase volume and transactions (2025 data cycle) | Fiserv 13 May 2026 news release citing Nilson |
| Nilson industry tables | Small set of firms (Fiserv, J.P. Morgan Payments, Worldpay, Global Payments, Elavon, BofA) dominate US acquiring | Nilson merchant acquiring coverage / summarized in industry IR |
| Stripe (merchant guidance) | Single gateway/acquirer path is a single point of failure; failover is operational design | Stripe payment failover resource |
| CPMI-IOSCO PFMI tradition | Concentration and operational risk are first-class for payment infrastructures | BIS CPMI materials (use carefully as framework, not fake statistic) |

## Facts that must appear

1. **US merchant acquiring is highly ranked/concentrated among a few large processors** — Fiserv cited as #1 by Nilson on volume and transactions.  
   Supports: Fiserv investor news release 13 May 2026.

2. **Industry lists put a handful of names (Fiserv, JPM Payments, Worldpay, Global Payments, etc.) at the top of US acquiring.**  
   Supports: Nilson-derived public summaries; attribute as ranking landscape, not invent shares.

3. **Merchants and PSPs document single-provider risk and recommend multi-path failover.**  
   Supports: Stripe “Payment failover” guidance.

4. **Cloud dependency compounds processor concentration** — major cloud outages have interrupted payment flows for merchants relying on single stacks (use dated secondary carefully; prefer Stripe’s own SPOF framing if outage primary is weak).  
   Supports: Stripe failover language + optional dated outage report if verified.

## Theory hook

- **Network effects + switching costs** in acceptance.
- **Operational concentration risk** (correlated downtime) vs market-power antitrust framing.
- **Two-sided payment platforms.**

## Real case

Prefer documented ranking concentration + Stripe’s own single-path failure framing over inventing a merchant bankruptcy. Optional: Global Payments / Worldpay scale M&A as further concentration if primary deal docs are clean.

## Retrieval gaps

- Exact Nilson percentage shares are paywalled; do not invent market-share % — use ordinal rankings from IR quotes.
- Avoid claiming a specific 2025 AWS outage percentage of global GMV without a primary.

## Source test

Every Source note must answer: *which sentence fails if this URL is removed?*
