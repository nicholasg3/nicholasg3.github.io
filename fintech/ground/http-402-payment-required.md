# Ground brief — http-402-payment-required

**Status:** grounded (2026-07-31)  
**Vertical:** fintech  
**Rank:** 4  
**Claim (particular):** HTTP status code 402 “Payment Required” has been reserved in the web standards stack for decades and is still not a working internet money primitive. Payments therefore still clear through wallets, processors, and app layers outside the core protocol.

## Who is arguing what

| Actor | Position | Source |
|-------|----------|--------|
| RFC 9110 (HTTP Semantics, 2022) | 402 is “reserved for future use” | rfc-editor.org/rfc/rfc9110 |
| Historical HTTP (RFC 1945 / early web culture) | Code slot existed early in HTTP design | rfc1945 context |
| Processors / wallets (structural) | Industry filled the gap with redirects, tokens, and hosted checkout | (industry structure; cite via implication + RFC void) |

## Facts that must appear

1. **RFC 9110 §15.5.3:** “The 402 (Payment Required) status code is reserved for future use.”
2. **Neighboring codes (401, 403, 404) are fully specified and operational** — the contrast shows path dependence.
3. **Implication:** without a protocol-level payment handshake, intermediaries mediate checkout.

## Theory hook

Protocol design and path dependence: a reserved status code is not a product. Network effects locked payments into browser + merchant + processor stacks.

## Real case

None invented. The “case” is the standard itself remaining unused as money rail.

## Retrieval gaps

- Early 1990s W3C/HTTP mailing-list lore is secondary; prefer RFC 9110 normative text.
- Do not claim a specific year “402 was invented” without the exact historic RFC cite in body if used.

## Source test

Remove RFC 9110 → the entire claim that 402 remains reserved fails.
