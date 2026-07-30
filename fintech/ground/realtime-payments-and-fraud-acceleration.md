# Ground brief — realtime-payments-and-fraud-acceleration

**Status:** grounded (2026-07-31)  
**Vertical:** fintech  
**Claim (particular):** Instant, often irrevocable push rails remove the delay that once functioned as a silent fraud brake; authorized push payment (APP) scams become the design problem, as UK reimbursement rules and US Fed research on fast-payment APP risk both document.

## Who is arguing what

| Actor | Position | Source |
|-------|----------|--------|
| UK Payment Systems Regulator | From 7 Oct 2024, FPS APP scam victims reimbursed up to £85,000; ~50/50 send/receive PSP split; covers nearly all claims by volume | PSR PS24/7 |
| Federal Reserve Bank of Kansas City | APP scams exploit speed + irrevocability; US consumer protection often does not cover authorized scams the way unauthorized does | KC Fed Payments System Research Briefing (Nov 2024) |
| FedNow / FRFS | Instant interbank settlement service; network exploring payee name verification and fraud tools | FRB Services FedNow materials |
| US Senate PSI (via KC Fed cite) | 2023: three largest Zelle banks — >$206M disputed as scams; victims bore >80% of losses | KC Fed citing U.S. Senate 2024 |

## Facts that must appear

1. **APP scam definition: victim authorizes a push to fraudster-controlled account.**  
   Supports: KC Fed briefing.

2. **UK mandatory reimbursement from 7 Oct 2024; max £85,000 per FPS APP claim; PSR says 99.8% by volume / 90% by value fully covered at that cap.**  
   Supports: PSR PS24/7.

3. **US: many APP losses fall on victims because payment was “authorized.”**  
   Supports: KC Fed briefing.

4. **Zelle 2023 figure: >$206M disputed as scams at three largest banks; victims >80% of losses (Senate PSI via KC Fed).**  
   Supports: KC Fed briefing + Senate report URL if cited.

5. **FedNow designed for 24x7x365 RTGS-style instant settlement — finality is a feature.**  
   Supports: Federal Reserve FedNow about / FRFS pages.

## Theory hook

- **Payment finality vs dispute rights:** card chargeback model is not the A2A template.
- **Authorized push payment fraud:** social engineering + irrevocability.
- **Liability design as market structure:** UK shifts loss to PSPs to force controls.

## Real case

UK Faster Payments APP reimbursement regime (policy, not a single company failure) + US Zelle scam-loss data as documented by Senate PSI / KC Fed.

## Retrieval gaps

- FedNow-specific aggregate APP loss statistics still thin in public Fed releases; use system-design + UK/Zelle evidence carefully.
- Confirmation of Payee is UK/HK overlay — do not claim it is live nationwide on FedNow without a primary.

## Source test

Every Source note must answer: *which sentence fails if this URL is removed?*
