# GLOBAL OPPORTUNITY + PAYMENT STACK — 2026-10-08

## Decision
Expand COLLECTION from AI/project discovery into a global opportunity miner. The objective is to find the shortest legitimate path from an existing internet asset/platform/opportunity to cash, client, credit, commission, reusable capability, or project closure.

## User payment constraint
The user has an active RedotPay account. RedotPay documents support for USDT and USDC and stablecoin-based virtual/physical cards; Algeria is not in its current unsupported-country registration list. However, feature availability can vary by account/region, and RedotPay Trade is currently restricted in Algeria. Never assume a fiat receiving account exists in the user's RedotPay account; verify the exact payment rail required by each opportunity.

## Opportunity classes
1. CASH_NOW — paid tasks, bounties, testing, research, data work, freelance jobs.
2. CLIENT — marketplaces/directories where an existing service can be sold.
3. COMMISSION — affiliate, referral, partner and revenue-share programs.
4. CREDIT — free API/cloud/tool credits that reduce operating cost.
5. READY_BUSINESS — existing SaaS/marketplace/platform that can be deployed or operated.
6. ASSET — useful open-source code, templates, datasets, integrations.
7. CAPABILITY — reusable functionality to extract as a Skill.
8. LEVERAGE — infrastructure that removes a paid dependency.
9. FUTURE — valuable but not immediately actionable.
10. IGNORE — low expected value, inaccessible, unsafe, or unverifiable.

## Payment compatibility fields
For every opportunity record:
- Country eligibility
- KYC requirements
- Payout currency
- USDT / USDC support
- Bank transfer support
- Card payout/support
- Minimum payout
- Fees
- Payout speed
- Client-side payment friction
- Whether RedotPay can actually receive/use the payout
- Whether the opportunity permits AI-assisted work
- Commercial/ToS restrictions
- Expected time to first revenue
- Capital required before revenue

## Initial validated candidates
### Workton
USDT-oriented freelance marketplace with Telegram workflow. Treat as a candidate only; verify current activity, Algeria eligibility, escrow/payout mechanics, and actual job volume before investing time.

### PayrollFlow
Cross-border invoicing/payout product advertising USDT TRC20/ERC20/BEP20 and local-bank withdrawals. Candidate for receiving international client payments. Verify jurisdiction, KYC, fees, custody, and whether an Algerian user can onboard.

### InstaDo
Freelance marketplace advertising USDT Safe Deal escrow. Candidate for direct service sales. Verify current marketplace liquidity, Algeria eligibility, payout wallet/network, and legal/compliance requirements.

## GitHub asset leads
- getcoherence/openpartner — affiliate/partner attribution and payout infrastructure; potentially relevant to MONY.
- agent-bounties — investigate as a possible bounty/agent-work opportunity or reusable board.
- Developer-Bounty-GitHub-Marketplace — investigate for developer bounty discovery.
- polar-marketplace — large marketplace codebase; inspect maturity/license/use case before collection.
- open-marketplace-protocol — potentially useful marketplace protocol; inspect before promotion.
- TriplEight/jobs-marketplace — jobs marketplace implementation; inspect only if architecture is reusable.

## Search rule
Do not start with a technology name. Start with a desired outcome/capability:
"get paid", "receive international payment", "sell service", "affiliate payout", "bounty", "testing", "AI evaluation", "ready marketplace", "ready SaaS", "unused platform", "open-source replacement", then identify the implementation/platform.

## Safety/compliance rule
Do not bypass KYC, country restrictions, payment-provider controls, or platform ToS. Do not classify a payout path as usable until its eligibility and payment rail are verified.

## Priority
P0: opportunities requiring no build and capable of first revenue.
P1: ready platforms with existing demand.
P2: existing projects that close a current portfolio gap.
P3: capabilities to extract into Skills.
P4: speculative/future assets.
