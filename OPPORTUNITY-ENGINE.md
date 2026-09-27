# Opportunity Engine — First-Dollar Mission

## Objective
Convert collected market signals into verified, actionable commercial opportunities without paid lead credits.

## Sources
- n8n Community Jobs
- Upwork marketplace (discovery only while Connects = 0)
- LinkedIn/direct company opportunities
- Workana/Freelancer and other public sources
- COLLECTION repositories: free, astra, project, files

## Sellable capability clusters
1. Lead-flow repair: forms/Meta/WhatsApp -> validation -> dedup -> CRM -> routing -> notifications -> retries/logging.
2. API/webhook repair: normalization -> idempotency -> retries -> alerts -> traceability.
3. Document-to-CRM: email/PDF/form -> extraction -> validation -> structured JSON -> CRM/webhook.
4. E-commerce/support automation: classify -> lookup -> draft response -> human handoff.

## Qualification gate
A signal is NOT a lead merely because it exists.
Track:
discovered -> verified -> contactable -> contacted -> replied -> qualified -> paid_pilot -> paid -> delivered

Only count revenue after payment evidence.

Reject/hold:
- paid Connects or lead credits required when balance is zero
- vague listings with no identifiable buyer/contact path
- claims requiring experience we cannot prove
- opportunities whose terms/data handling are not verified

## Current verified signals (2026-09-27)
- Upwork: n8n AI Automation Engineer — CRM, AI Agents & API Integration — $1,000 fixed, long-term (>6 months). Discovery only; current Connects balance is 0.
- Upwork: Lead Capture System — $800 fixed in 4 weekly $200 deliveries; strong fit, but requires production examples in application and currently requires Connects.
- n8n Community: NUBO — ongoing project-by-project n8n + AI + API/CRM/WhatsApp work; direct community opportunity.
- n8n Community: multiple current hiring threads for ongoing n8n/AI automation.

## Immediate operating rule
Prioritize opportunities with:
A) direct/public contact path,
B) no upfront spend,
C) small paid pilot possible,
D) recurring maintenance potential,
E) close match to our existing capabilities.

Use Upwork for market intelligence while Connects = 0, not as a reason to buy Connects.

## Evidence
External source URLs must be retained with every opportunity record. Never mark contacted/replied/paid without external evidence.
