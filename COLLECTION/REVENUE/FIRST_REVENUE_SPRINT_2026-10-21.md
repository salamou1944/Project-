# First-Revenue Sprint — 2026-10-21

## Decision

**Primary 7-day revenue experiment: a small, fixed-scope e-commerce catalog cleanup / product-data audit service.** Sell the deliverable before building a SaaS. Use existing spreadsheet/code/AI tools only; do not buy API credits, subscriptions, Connects, hosting upgrades, or ads. This is a revenue experiment, not a claim that demand or income is guaranteed.

Why this wins over the other existing assets for the first attempt:
- It can be delivered as a human-reviewed spreadsheet/CSV without requiring the API Factory to be production-ready.
- It reuses the user's e-commerce work and product-integrity experience from EASY without depending on the OpenAI image-generation credit that was previously exhausted.
- A live Upwork listing published 2026-10-21 asks for an automated competitor-price tracker for 2,500+ products and shows a $50 fixed budget and a verified-payment client. This is evidence of a buyer problem, not proof that the user will win that listing: https://www.upwork.com/jobs/~022112874893029610294
- A second live listing asks for CRM cleanup of 20 records with a $30 fixed budget and verified payment: https://www.upwork.com/jobs/~022112131935869040206
- The user's connected Upwork freelancer profile currently has no completed jobs/reviews and is private; its displayed overview/title are weakly specified. Connects balance was verified as **0** (free 0, paid 0), so submitting normal proposals is not a no-cost immediate path. Do not buy Connects.
- Previous outbound email threads in the AI API pilot inbox include multiple delivery failures. Do not repeat those bounced addresses/domains.

## Offer to test

### Offer A — Product catalog cleanup pilot
**Test scope:** up to 10–20 SKUs from a customer-provided CSV/XLSX or product URLs.
**Deliverables:**
1. Cleaned CSV/XLSX with consistent product titles, SKU/variant fields, price/availability columns, and clearly marked missing values.
2. Duplicate and inconsistency report; no product facts, prices, specs, or availability are invented.
3. A short prioritized list of the most important listing corrections.
4. Optional Arabic product-title/description rewrite only where source facts are supplied and can be verified.
5. Before/after sample for 2 products, approved by the client before processing the remainder.

**Price test:** quote a small fixed pilot (suggested experiment: USD $20–$30 equivalent, or a locally agreed amount); this is a test price, not a verified market rate. Confirm a usable payment rail and the exact scope with the client before starting. Prefer a funded milestone or advance for direct work. Never spend money to deliver the pilot.

**Acceptance criteria:** the client receives the agreed files, all changed fields are auditable, uncertain data is flagged rather than guessed, and the client explicitly confirms delivery. Do not promise sales lift or conversion improvement.

### Offer B — Competitor price snapshot (only when the customer supplies sources)
A one-time spreadsheet comparing up to 20–50 customer-selected products against customer-provided competitor URLs, with source URL, checked-at date, matching confidence, price, variant/pack-size notes, and unmatched rows. Do not promise a fully automated 2,500-SKU system until a separate paid discovery and technical feasibility check is funded.

## Target customer

Start with one narrow segment: small e-commerce sellers with an existing product list but incomplete, duplicated, inconsistent, or hard-to-compare listings. First approach sellers where the owner can approve a small paid pilot quickly. Prioritize warm contacts and relevant seller communities over paid ads or mass cold email.

## 7-day execution plan

### Day 1 — Make the offer tangible
- Create one fictional/demo CSV with 10 rows and a before/after report; label it clearly as a sample, not client work.
- Prepare a one-page scope, acceptance checklist, price-test range, and payment terms.
- Confirm which payment methods can actually receive the selected customer's payment; RedotPay account existence alone does not prove a particular payout rail works.

### Days 2–3 — Find buyers without spending
- Identify 20 relevant sellers or agencies from existing contacts and public business pages.
- Send individualized messages only to valid, relevant contacts; do not reuse bounced email addresses.
- Ask for a 10-SKU paid pilot, not a large system build. Do not send mass spam or claim a portfolio result that does not exist.
- Track prospect, source, contact channel, reply, next action, quote, payment status, and delivery status.

### Days 4–5 — Deliver one paid pilot
- Do not begin unpaid bulk work. Use a funded milestone or agreed advance where possible.
- Keep a copy of original customer data unchanged; return a separate cleaned copy.
- Verify every modified value against supplied source data and produce a short change log.

### Days 6–7 — Decide using evidence
- Continue only if at least one qualified buyer replies positively or pays for a pilot.
- If 20 relevant approaches produce no qualified replies, revise the segment/offer/message before building anything larger.
- If a pilot is paid and accepted, ask permission for an anonymized case study and offer a repeat monthly catalog maintenance package.
- Record actual cash received separately from proposals, verbal interest, invoices, or pending platform balances.

## Asset and blocker inventory relevant to revenue

| Asset | Evidence / current state | Revenue decision |
|---|---|---|
| COLLECTION / Project- | Recent collection-continuous runs succeeded; the queue is large and contains reusable research, but research counts are not revenue. Latest run: https://github.com/salamou1944/Project-/actions/runs/39533389021 | Use only to find specific buyers/opportunities; pause low-value expansion while executing the cash test. |
| API Factory / Salamou-31 | API Factory test, SOAT runtime integration smoke, provider contract, and Railway token-access CI runs passed on 2026-10-21. The Render preview is the currently documented zero-upfront-cost runtime with durable registry/artifact storage; free service can sleep. Deployment execution adapters are not implemented, and the main Render endpoint is documented as fail-closed with DURABLE_STORAGE_REQUIRED. Evidence: https://github.com/salamou1944/Salamou-31/blob/main/AI-API-HUB/api-factory/DEPLOYMENT.md | Keep as a later paid prototype/implementation service. Do not sell it as a production API hosting platform or promise provider-backed deployment today. |
| EASY | Product-creative flow exists, but OpenAI generation was previously blocked by exhausted provider credits. | Park paid image generation. Reuse product-data/creative knowledge only in work that does not require paid inference. |
| MONY | Affiliate/reward bridge needs a real qualifying partner reward before revenue exists. | Not the first-revenue bet; no commission forecast until a real approved conversion and payout occur. |
| Upwork | Connected profile has no completed jobs/reviews and is private; Connects balance is zero. Some verified-payment buyer listings exist, but several require dialect, language, or technical qualifications not yet proven. | Do not buy Connects. Use only organic invites/free opportunities if they appear; do not misrepresent qualifications. |
| AgentMail outreach | Inbox exists, but historical outbound threads include multiple bounces. | Audit addresses before future sends; no bulk sending and no repeated bounced targets. |
| Payment rail | User has reported a RedotPay account; a specific employer/client payout path has not been verified. | Verify the actual method, fees, minimum, and eligibility for each buyer before counting the opportunity as payable. |

## Revenue funnel and stop/go gates

1. **Lead found** — named business and source URL recorded.
2. **Qualified** — visible catalog/data problem and plausible buyer/decision-maker.
3. **Contacted** — valid channel, individualized message, timestamp recorded.
4. **Interested** — buyer replies; not revenue.
5. **Paid** — money or funded milestone confirmed; this is the first revenue event.
6. **Delivered** — files and change log delivered.
7. **Accepted** — buyer confirms acceptance.
8. **Repeatable** — second paid order or recurring maintenance commitment.

No stage may be inferred from the prior stage. Do not report revenue before stage 5.

## Explicitly not selected as the first bet

- **Hosted API Factory:** useful existing engineering asset, but deployment execution and production operational proof remain incomplete.
- **EASY Magic image generation:** requires provider credit or a verified zero-cost image provider; do not spend before revenue.
- **MONY affiliate bridge:** contingent on partner-approved conversions and payout.
- **YouTube monetization:** longer time-to-revenue and requires consistent content production/audience growth.
- **Large-scale Collection expansion:** useful research infrastructure but not itself a paying customer.

## Immediate next actions

1. Produce the fictional 10-row demo CSV and its change log.
2. Build a list of 20 qualified sellers from public, relevant sources; record sources and avoid duplicate/bounced contacts.
3. Draft two short outreach variants (Arabic-first; English only where suitable) and keep them as drafts until recipients and payment terms are checked.
4. Report the first real reply, funded pilot, delivery, and cash receipt separately.
