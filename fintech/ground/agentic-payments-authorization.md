# Ground brief — agentic-payments-authorization

**Status:** grounded (2026-07-31)  
**Vertical:** fintech  
**Claim (particular):** Agentic commerce fails first on **authorization design** — scope, merchant category, spend caps, real-time approval, token lifecycle, and revocation — not on model intelligence. Networks that ship agent payments are packaging those controls as the product.

## Who is arguing what

| Actor | Position | Source |
|-------|----------|--------|
| Visa Intelligent Commerce (VIC) | Embed payment credentials, controls, authentication, and protections so AI agents can buy under user-set instructions | https://www.visa.com/en-us/solutions/intelligent-commerce |
| Visa investor/PR (Dec 2025 pilots) | Partners completing secure AI transactions; sandbox and closed-beta end-to-end purchases | https://investor.visa.com/news/news-details/2025/Visa-and-Partners-Complete-Secure-AI-Transactions-Setting-the-Stage-for-Mainstream-Adoption-in-2026/default.aspx |
| Visa–AWS (Dec 2025) | Marketplace listing / blueprints for agentic workflows with auth, tokenization, intent capture | https://press.aboutamazon.com/aws/2025/12/visa-and-aws-enable-next-generation-agentic-commerce-capabilities |
| Mastercard Agent Pay (ecosystem) | Parallel network approach to agent-initiated payments (secondary contrast only) | secondary press |

## Facts that must appear

1. **Visa launched Intelligent Commerce** as a portfolio for AI-agent-initiated transactions with controls and authentication.  
2. **User/agent instruction model:** dollar limits, merchant categories, approval prompts load into network rails.  
3. **Tokenization / one-time credentials** remain part of the authorization path (Visa materials).  
4. **Pilots and partner sandboxes** show the product is authorization plumbing, not a chatbot demo.  
5. **Principal–agent problem:** the human is principal; the software agent is agent; the merchant and network need proof of authority and a revoke path.

## Theory hook

- Principal–agent problem; least privilege; payment authorization as capability design.
- Network-effects path dependence: agents will route through rails that settle liability cleanly.

## Real case

Visa Intelligent Commerce + documented partner pilots (no invented agent startups).

## Retrieval gaps

- Live merchant dispute volume for agent-initiated payments is immature.  
- Do not claim national legal standard for “AI agent liability” as settled.

## Source test (must pass)

Every Source note must answer: *which sentence fails if this URL is removed?*
