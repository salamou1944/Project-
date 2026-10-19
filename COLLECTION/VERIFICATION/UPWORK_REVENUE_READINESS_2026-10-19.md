# Upwork and Apollo revenue readiness — 2026-10-19

## Upwork account state (read-only inspection)

- Connected account role: Freelancer/Talent; organization UID `2100415208992274981`.
- Profile: [open freelancer profile](https://www.upwork.com/freelancers/~014d65b8eb0c666d8c?utm_campaign=LLM_chatgpt_MCP_freelancerprofile&utm_content=freelancerprofile&utm_medium=LLM&utm_source=chatgpt).
- Profile visibility is **Private**; title is generic, description is placeholder-quality, the only listed skill is Customer Service, there are no certificates or portfolio projects, and profile aggregates show 0 completed jobs / 0 reviews. Current rate is $100/hour, which is not supported by any Upwork history yet. Treat this as a conversion/readiness blocker, not proof that applications are technically prohibited.
- Freelancer dashboard: 0 active contracts, 0 invitations, no submitted proposals, and **0 Connects** (free balance 0, paid balance 0). Identity verification says proposals can be submitted, but Connects are required per job.
- Plan: Freelancer Basic. A 50% off one-month Freelancer Plus promotion is visible through 2026-12-31; it was not activated. No subscription or Connects purchase was made.

## Current opportunity inspected

**A.i automation company** — [open job](https://www.upwork.com/jobs/~022111503420376780385?utm_campaign=LLM_chatgpt_MCP_jobpost&utm_content=jobpost&utm_medium=LLM&utm_source=chatgpt)

- Job ID: `2111503420376780385`; state ACTIVE at read time; posted 2026-10-17; part-time, less than one month, intermediate; hourly rate not stated.
- Scope: launch an AI automation agency site in Webflow/Framer; route forms through n8n/Make webhooks to Supabase/Airtable; configure social lead forms and tracking pixels; provide handover documentation.
- Application gate: **14 Connects required; balance 0; `can_apply=false`**. No application was attempted.
- Client risk: verified payment method, UAE, 5 jobs posted, 0 hires, 0 reviews, 0% hire rate, 2 invitations sent, 7 interview invitations, 0 offers and 0 hires on this posting. This is a live listing but a new/untested client.
- Client explicitly requests no AI-written replies or cover letters. Do not generate or submit a proposal for this posting; if reconsidered, the user must write it in their own words.
- Decision: preserve as a **low-confidence candidate**, not a recommended paid application. Do not buy Connects for it.

## Saved job with potentially better fit

**Marketing Ops / Automation Specialist** — [saved job link](https://www.upwork.com/jobs/~022108001189893574453?utm_campaign=LLM_chatgpt_MCP_jobpost&utm_content=jobpost&utm_medium=LLM&utm_source=chatgpt)

- The saved listing describes a paid test for website / WhatsApp / Instagram enquiries into one CRM, source tagging, acknowledgements, follow-up at days 3/7/14/30, and tracked proposals. It listed $15–$38/hour.
- The listing was last updated 2026-10-08. A live detail lookup returned a permission/status error saying the job could not be opened right now and may be private, invite-only, or temporarily unavailable. It was **not retried**; current liveness is unverified.
- Decision: keep saved, but do not count as an actionable lead until its open status and application cost are independently confirmed.

## Apollo credit state (read-only; no search/enrichment performed)

- Profile endpoint: 80 lead credits remaining; 0 used. AI credits: 5,000 effective; 0 used. Export credits: 0. Direct-dial profile endpoint reports 160 effective and 0 used.
- Team usage endpoint reports 80 lead credits remaining and 0 used; 150 conversation credits remaining; 50,000 broadcast credits remaining; 20 inbound-website-visitor credits remaining; 5,000 AI credits remaining; 0 export credits.
- Direct-dial balance is inconsistent across endpoints: profile reports 160 effective while usage stats report 80 remaining. The usage stats also report an anomalous `web_search_record_credit` value (limit 0, consumed -80, remaining 80). Do not treat either anomaly as usable credit.
- No Apollo people/company enrichment or email-reveal action was run. These balances are preserved; no lead credits were spent.

## Action boundary

- No proposal submitted, no message sent, no Connects purchased, no Freelancer Plus subscription activated, and no Apollo credit-consuming search/enrichment performed.
- The immediate blocker is profile readiness plus zero Upwork Connects. Before public profile changes or any paid Connects/subscription purchase, get explicit user approval. Keep the existing revenue rule: no upfront spend before revenue.
