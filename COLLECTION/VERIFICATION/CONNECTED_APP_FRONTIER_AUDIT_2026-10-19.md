# Connected Account and Application Frontier Audit — 2026-10-19

## Scope and evidence boundary

Read-only inventory of connected account surfaces relevant to Collection, API Factory, current projects, and revenue work. This is not a claim that every connector exposes all account data or that every available tool is authenticated to a usable workspace. No credentials or secret values were read or copied. No external messages were sent and no paid prospecting credits were spent.

## GitHub — authenticated account and visible repositories

- Authenticated GitHub account: `salamou1944`.
- Organization memberships returned: none.
- Accessible repository list: 10 repositories; the next page at offset 100 was empty.
- This is the authenticated user's visible repository scope, not the full external-account frontier in Collection.

| Repository | Current useful scope / preserved entry points |
|---|---|
| [Salamou-31](https://github.com/salamou1944/Salamou-31) | API Factory, service catalog, Collection links, revenue/service offers, workflows. |
| [agent-skills](https://github.com/salamou1944/agent-skills) | Canonical Skills, Elite, ARMY-14, MONY/revenue engine, workflows, registry and tests. |
| [Easy-](https://github.com/salamou1944/Easy-) | EASY commerce product, API lab/registry, commerce connector, platform/services/tests; keep MONY outside this boundary. |
| [AI_operating_memory](https://github.com/salamou1944/AI_operating_memory) | Canonical state/policy, project boundaries, known limitations, MONY state and evidence rules. |
| [Astra-](https://github.com/salamou1944/Astra-) | ASTRA executable/paper-trading boundary, readiness gates, tests and collection sources. |
| [Astra](https://github.com/salamou1944/Astra) | Research and real-data evidence. Its latest recorded gates explicitly fail profitability/alpha; live execution remains OFF. |
| [Files-](https://github.com/salamou1944/Files-) | README plus collection material; root is sparse, so deeper `collection/` inventory remains pending. |
| [Project-](https://github.com/salamou1944/Project-) | Canonical Collection and monetization ledger, frontier inventory, source preservation, verification reports. |
| [Pastel-](https://github.com/salamou1944/Pastel-) | QR concierge and Supabase-backed site; don't change QR destination until a real-phone test of the new live URL. |
| [local-bridge.](https://github.com/salamou1944/local-bridge.) | Safe Windows self-hosted runner plan. README says the laptop must register an idle runner; GitHub connection alone does not connect the laptop. |

### Additional source-level gates observed

- `Astra/VERIFICATION.md` records research gates failed and explicitly leaves profitability/alpha unverified, live execution OFF, and zero broker orders in the recorded risk/shadow evidence. Do not promote ASTRA to live trading.
- `Easy-/PROJECT-BOUNDARY.md` says prototype mode is non-production and production claims require a real provider, durable persistence, auth, request IDs, integrity validation, and deployed end-to-end tests.
- `AI_operating_memory/KNOWN-LIMITATIONS.md` requires actual write evidence, honors tool permissions, and forbids bypassing MFA/CAPTCHA.
- `local-bridge./README.md` defines a manual, read-only Windows runner setup. No reachable host was verified in Termalin, so this path remains unactivated.

## Connected deployment, database, and compute surfaces

### Railway

Two projects are visible:
- `EASY Runtime Production` — services `salamou31-api-factory`, `easy-runtime-current`, `easy-runtime`.
- `EASY Developer Platform` — services `soat-production-runtime`, `easy-platform-runtime-v3`.

Read-only service config inspection:
- `salamou31-api-factory` production config returned no direct service variable names. Its five latest listed deployment records were removed; no current live API Factory deployment is proven by this inventory.
- `easy-runtime-current` has configuration variable names for EASY, OpenAI, operator, product-content and Supabase integrations. Variable values were not read. No EASY variables or deployments were changed.
- The Railway SOAT production runtime's visible recent deployments include failures from 2026-10-06. The separate GitHub Actions SOAT integration run is a different runtime boundary and must be assessed on its own evidence.

### Supabase

- One project is visible: `easy-platform-db`, status `ACTIVE_HEALTHY`, region `eu-west-1`.
- It is EASY's database. Do not reuse it for API Factory; a separate approved durable store is still required.

### Vercel

- The connected Vercel deployment-context tool returned no teams. Prior Collection evidence also records a missing `VERCEL_TOKEN` GitHub secret and blocked connector scope. No production alias change or current Vercel deployment proof is claimed.

### Render

- One workspace is visible, named `Salamou's workspace`. Service enumeration was refused because no workspace was selected. No workspace was selected on the user's behalf; existing Collection notes say no reusable API Factory database/Key Value was found in the earlier reviewed scope.

### Termalin

- `hosts_list` returned zero reachable servers and explicitly says no servers are connected to the account yet. This contradicts any assumption that the laptop is reachable merely because the Termalin site/browser is open. The local Windows runner remains a separate setup path.

### GitLab

- One owned private project/group is visible: `salamou1944-group/Salamou1944-project`.
- The project reports `empty_repo: true`; it is not an additional source of code until initialized.

## Business, design, commerce, and knowledge apps

### AgentMail

Three inboxes are present:
- `api-pilot@agentmail.to`
- `easy@agentmail.to`
- `pastel-realtime-e2e@agentmail.to`

The current visible threads in API Pilot and EASY consist of delivery failures/bounces from September 12–27, 2026; no customer reply, acceptance, payment, or revenue evidence was found in those returned thread pages. The PASTEL test inbox had no threads. Do not count the previous outreach as leads or revenue. Verify a contact address and active opportunity before any new outbound action.

### HubSpot

- The connected owner lookup returned one active owner. No CRM records were queried or changed during this pass.

### Shopify

- One connected store: `My Store`, domain `2eih8n-pc.myshopify.com`, currency DZD, country Algeria, timezone CET.
- **Plan: trial — you'll need to upgrade before you can start selling and unlock full features**
- Read-only store checks returned **0 active products and 0 orders**. No product was created or imported and no store setting was changed.
- Treat it as an existing commerce asset on trial, not as a live revenue channel until the account is eligible and a real checkout/payment path is verified.

### Wix / Canva / Notion / Figma

- Wix: zero sites returned.
- Canva: project-name search returned no results.
- Notion: workspace `Salamou Salamou’s Space` is connected; the Collection/API Factory/EASY/ASTRA search returned no results. This is not proof the workspace is empty.
- Figma: account has a Starter plan seat marked `View`; Code Layers are disabled. Figma AI permission is present, but editable code-layer work is not established by this account state.

### AgentMail app catalog

- The catalog lists 41 apps, but `list_accounts` returned zero signed-in app accounts. Catalog availability is not a connected credential or entitlement; do not assume Firecrawl or other catalog services are activated.

### Task automations

- Five automations were returned. Enabled workflows include `Daily collection digest` and `Revenue + leverage sweep`; a separate account-collection automation is disabled. These automations are instructions/schedules, not evidence that a particular extraction, email, or revenue event completed. Their outputs must be checked.

## Execution priorities derived from this audit

1. Complete the newly triggered Collection deep extraction and verify the current-main JSON audit report before marking the frontier extracted.
2. Keep Layer B accounts incomplete until their repository inventories are actually persisted and paginated where result caps were reached.
3. Keep API Factory production-blocked until a stable deployment and durable registry/artifact storage are proven; don't reuse EASY's Supabase project.
4. Continue local-only SOAT evidence validation independently of the Railway production service. Do not weaken the zero-cost provider policy.
5. Fix outreach deliverability/address validation before another campaign; do not send duplicates or count bounces as leads.
6. Keep ASTRA paper/research-only and EASY creative generation paused behind its provider-credit boundary.
7. Treat local-bridge as unconnected until a safe Windows self-hosted runner or Termalin host is actually online.

## Current frontier run — verified 2026-10-19

- **Full safe-incremental Collection harvest passed:** [run 39186272221](https://github.com/salamou1944/Project-/actions/runs/39186272221), source marker commit `4393ae5fafce96694688a2b7bcaa1f9e9b1f8477`, generated-state commit `0cf9757`. All harvest, canonical-Skill reconciliation, state guard, promotion/readiness/callable policy, install gate, post-install validation, audit persistence and final install-outcome steps passed.
- **Current-main JSON audit passed:** 10,975 JSON/JSONC files, zero parse failures, 626,208,456 raw bytes. Report SHA `c96c794c2ee70143583ae91b71b83db5874d1702`. The source devcontainer remains unchanged; JSONC handling is limited to standard `devcontainer.json`.
- Harvest result: 199 account owners, 31,343 repository metadata rows, 100 repos selected in the bounded cycle, 99 refreshed, 1 blocked; 2,985 extracted source rows, 2,396 cached rows, 490 prior sources preserved as not selected, 20,048 deferred repos, and one source branch-not-found error. The run scanned 2,985 source files and produced 24,535 capability groups, 17,298 promotion-review items and 7,237 restricted/quarantined items.
- **No automatic promotion:** runtime-readiness claims = 0; explicit readiness declarations = 0; install outcome `NO_APPROVED_CANDIDATES`; installed/already-installed = 0. This is a successful preservation/reconciliation cycle, not evidence that any collected asset is production-ready.
- API Factory SOAT integration [run 39179590053](https://github.com/salamou1944/Salamou-31/actions/runs/39179590053) completed **success**. The pinned SOAT runtime authenticated, local Ollama returned a real deterministic completion (`"4"`), official smoke passed, execution/business-outcome gates passed, and the verification record was uploaded as artifact [12155088912](https://github.com/salamou1944/Salamou-31/actions/runs/39179590053/artifacts/12155088912) (ZIP SHA-256 `4b7a721294b6e53086e2e89a65c71231906029487383ceeb6ce3dd79b7f0faf5`). Durable production deployment remains **not proven**.

## Additional high-priority supply-chain finding
The monitored source `mnfst/awesome-free-llm-apis` had a historical malicious workflow in commit `48fcbe86582e16b7b746fee52e5512a891a8db76`: it searched repository/history for credential patterns and POSTed findings to `193.32.204.199:8080`. It was removed in `cf97c32fec1b2e96e9936746e2731a81bd5ea33f`. No “Security Audit” run appeared in the latest 30 visible Actions runs, but execution remains unverified. Treat the catalogue as untrusted discovery input; do not run its scripts/workflows or pass it secrets. No secrets were searched for or transmitted.


## Extended workspace inventory — 2026-10-19

- Notion private sidebar pages/databases: 0 returned; favorites: 0; recent pages: 0. The earlier targeted search also returned no matches. This means the connected workspace exposed no pages through these read operations, not that the workspace is necessarily empty or that all access paths were exhausted.
- Canva design search for `EASY` and `API Factory`: 0 matching designs returned.
- AgentMail account list: 0 signed-in app accounts. This is separate from the three AgentMail inboxes, which exist and were inspected above.
- The enabled `Revenue + leverage sweep` automation was requested for an immediate run (automation ID `6ab730fda9948191a73f262cdb30fa92`). The request was accepted; execution is asynchronous, so no completed sweep result is claimed here.


## Recipient-level bounce handling
The following addresses were observed in failed delivery threads and should not be retried without independent re-verification: `contact@deevdigital.com`, `contact@goldway-dz.com`, `support@ecomproassociates.com`, `hello@gmsolutions.com`, `hallo@gtpmedia.nl`, `info@channelboosters.io`, `sales@flexshopltd.com`, `contact@scaleverse.media`, `michael@nuworld.agency`, `hello@teroinlabs.com`, and `hello@agencemerlin.com`. These are bounces, not leads; no outbound messages were sent in this sweep.


## Upwork and Apollo readiness check
- Upwork account is Freelancer Basic, profile visibility Private, title/description need a verified rewrite, only Customer Service is listed as a skill, no portfolio/highlights, 0 completed jobs/reviews, 0 proposals, 0 active contracts, 0 invitations, and 0 Connects.
- The checked active AI automation job requires 14 Connects and has 0 hires/0 reviews; no application was attempted. The saved Marketing Ops/Automation Specialist job lists $15–$38/hour but could not be opened for current liveness; it was not retried.
- Apollo profile shows 80 lead credits and 5,000 AI credits remaining with zero used. Direct-dial counters disagree across endpoints; no search/enrichment was performed and no credits were spent. Details: [UPWORK_REVENUE_READINESS_2026-10-19.md](UPWORK_REVENUE_READINESS_2026-10-19.md).


## HubSpot CRM records — read-only audit

- CRM search returned **0 deals**, **2 contacts**, and **1 company**. No writes were performed.
- Contacts are explicitly sample records: [Brian Halligan (Sample Contact)](https://app.hubspot.com/contacts/149568666/record/0-1/894044249312?utm_source=app_12360546_mcp&utm_medium=ai_agent&utm_campaign=search) and [Maria Johnson (Sample Contact)](https://app.hubspot.com/contacts/149568666/record/0-1/894054999231?utm_source=app_12360546_mcp&utm_medium=ai_agent&utm_campaign=search).
- The sole company record is [HubSpot / hubspot.com](https://app.hubspot.com/contacts/149568666/record/0-2/453775516896?utm_source=app_12360546_mcp&utm_medium=ai_agent&utm_campaign=search), lifecycle stage `lead`. In context with the sample contacts and empty deals, treat it as seed/demo data unless independently verified otherwise.
- Result: HubSpot currently provides no evidenced customer pipeline; the two sample contacts and one company must not be counted as leads, customers, or revenue.


## Post-automation AgentMail recheck
- Re-read all three connected inbox thread lists after the revenue sweep run. API Pilot: 6 threads, latest 2026-09-27, all visible messages are delivery failures/bounces or older sent/bounced threads. EASY: 5 threads, latest 2026-09-22, all visible threads are delivery failures. PASTEL E2E: 0 threads.
- No new email thread or new outbound send appeared after the automation run. The 11 known bounced recipients remain suppressed.


## Explicit installation approval boundary
- Automatic installation now requires `promotion_action=INSTALL_APPROVED`, `install_approval=APPROVED`, `integration_gate=PASS`, and `security_gate=PASS`. The installer no longer auto-selects deep-extraction manifest rows or legacy source notes.
- With no approved queue candidates, the install outcome is explicitly `NO_APPROVED_CANDIDATES`; this is a safe no-op, not installation success.
- Existing Hyperswitch source remains preserved and not runtime-promoted: [legacy install boundary](LEGACY_INSTALLED_ASSETS_2026-10-19.md).


## Connected deployment, workspace, and owned-repository frontier — read-only sweep (2026-10-19)

### GitHub account and owned repositories
- The GitHub app exposes one installed account: `salamou1944`. The authenticated account lists **10 repositories**; page offset 10 is empty. This is a separate owned-repository frontier from the 199 external owners in the Collection sweep.
- Repositories inspected at root: `Salamou-31`, `agent-skills`, `Easy-`, `AI_operating_memory`, `Astra-`, `Astra`, `Files-`, `Project-`, `Pastel-`, and private `local-bridge.`.
- High-value preserved roles:
  - `agent-skills`: canonical Skills plus EASY runtime and MONY/Revenue Engine; current README is present.
  - `Salamou-31`: API Factory and its local-provider/zero-cost policy; root also contains two PDF artifacts (one named `*_pdf_temp`). Preserve them, but review whether they belong in a code repository before any deletion/move.
  - `AI_operating_memory`: canonical state/evidence rules and MONY state; keep as the canonical memory layer, not a duplicate business repository.
  - `Astra`: research-only quant lab with README evidence claiming 49/49 local regression and real-data inputs, but candidate gates are FAIL and live-money execution is disabled. Treat the readme claims as repository-recorded evidence, not independently rerun proof in this audit.
  - `Astra-`: separate executable bot boundary with live trading OFF by default, approval gates and no withdrawal capability; do not merge into the research repo.
  - `Easy-`: project boundary, API registry/lab, app, services and tests; keep separate from runtime evidence in Railway.
  - `Files-`: minimal root README and a `collection/` directory; inspect the subtree before judging it empty.
  - `Pastel-`: static QR concierge with a documented truth policy; public Pages deployment and real-phone QR migration remain explicitly gated.
  - `local-bridge.`: private Windows self-hosted runner control point. README limits initial workflow to read-only diagnostics; no runner dispatch was attempted.
  - `Project-`: collection and monetization control plane; current repository size reported by GitHub is about 317,504 KB, so JSON/audit and packet growth must be bounded.
- Own-repo extraction is not automatically included in the 199-owner external sweep. Continue treating these ten repositories as a separate first-party source frontier.

### Railway — deployment truth
- Workspace `salamou1944's Projects` contains two projects: `EASY Runtime Production` and `EASY Developer Platform`.
- Read-only production status shows **all five listed services have FAILED latest deployments**, with no pending staged work: `easy-runtime`, `easy-runtime-current`, `salamou31-api-factory`, `easy-platform-runtime-v3`, and `soat-production-runtime`. Some older deployments are removed/skipped; this is not current runtime proof.
- API Factory Railway source is `salamou1944/Salamou-31`, branch `feat/api-factory-railway-deployable-2026-10-16`, root `AI-API-HUB/api-factory`; its current Railway config lists no service variables. The latest failure is `BUILD_IMAGE`: Railpack failed to prepare the build, with no diagnostic attached. Fix the build/source configuration before redeploying; do not add secrets or weaken fail-closed auth.
- EASY runtime has a variable-name list including both `EASY_OPENAI_API_KEY` and misspelled `ESAY_OPENAI_API_KEY`; values were not read. Treat this as configuration drift to review, not permission to print or expose secrets.
- Railway service status and deployment IDs were checked read-only; no deploy/redeploy, environment mutation or secret access occurred.

### Supabase
- One project `easy-platform-db` is `ACTIVE_HEALTHY` in `eu-west-1`, Postgres 17.6.1.166. Its API URL is `https://rdcodzowehzmwdxhztxe.supabase.co`.
- This is the existing EASY database. Do not reuse it for API Factory/MONY storage; durable separate storage and cross-invocation persistence remain open.

### Vercel
- One team-scoped project was found: `salamou31-api-factory`. Project metadata says `live: false`, but the latest production-target deployment is `READY` at [salamou31-api-factory.vercel.app](https://salamou31-api-factory.vercel.app/).
- That READY deployment was built from feature branch `feat/api-factory-railway-deployable-2026-10-16`, commit `35b462ff3137605f00c98383a8598b49610cd963`, not current main. Several newer staging/preview deployments have ERROR state. This is a deployable artifact candidate, not proof of current production API health or correct environment variables.
- No environment variable values were requested or printed.

### Other connected platforms
- **GitLab:** one private project `salamou1944-group/Salamou1944-project` is visible, but its metadata says `empty_repo: true`; repository-tree lookups return 404. No code asset to extract yet.
- **Replit:** three editable apps were listed, all auto-generated titles and last updated between 2026-09-11 and 2026-10-02. Search by `EASY` and `API Factory` returned no matching apps; these names cannot currently be tied to the known prototypes.
- **Notion:** recent pages and the combined search for Collection/API Factory/EASY/MONY returned no results. No Notion source was added.
- **Canva:** connected design search returned no designs.
- **Wix:** no sites returned.
- **Render:** workspace list returned `Salamou's workspace`; service listing requires a workspace ID selected by the user under this connector's safety contract. No workspace was selected and no service list was read.
- **HubSpot:** previous read-only audit shows two sample contacts, one HubSpot company seed record and zero deals; not a real evidenced customer pipeline.
- **AgentMail:** previous recheck found only delivery failures/bounces or older sent/bounced threads; no fresh outbound message was sent. Suppressed bounced recipients remain suppressed.
- **Apollo:** 80 lead credits and 5,000 AI credits reported unused; direct-dial counters disagree, so do not treat that discrepancy as usable credit. No enrichment/search spend.
- **Upwork:** zero Connects, private/incomplete profile, no proposal/contracts/invitations; no paid application attempted.

### Prioritized fixes from this sweep
1. Identify and repair the single invalid JSON path in `CURRENT_MAIN_JSON_AUDIT.json`; keep the report and do not suppress the parse failure.
2. Stop using Railway deployment status as a proxy for successful runtime; rebuild the API Factory image/source setup, then run an authenticated health/smoke against the intended branch and evidence store.
3. Reconcile Vercel's READY production-target artifact on a feature branch with project `live: false` and failed newer previews; validate route behavior before claiming production.
4. Review the misspelled EASY environment-variable name without exposing any value.
5. Keep the 10 first-party GitHub repos as a separate extraction lane from the 199 external owners; inspect the useful `Files-/collection`, `AI_operating_memory`, `Astra` and `Astra-` evidence files before promotion.
6. Keep MONY paid-boundary blocked and do not spend Upwork Connects or Apollo credits until there is a validated zero-cost path to a real paid outcome.


## First-party asset triage — repositories opened beyond root (2026-10-19)

- `Files-/collection/mufeedvh/COLLECTION_MANIFEST.md` (SHA `8dafd2f3186f1b5b88204fde2245dadf3943a99a`) records 43 public repositories from `mufeedvh`; it explicitly says repository inventory is verified but file-content snapshots, full Git history/refs, and public Gists are incomplete/not included. Do not label this collection complete. Preserve `code2prompt`, `pdfrip`, `okjson`, `gofindapis`, and other small assets until a per-repo license/security/usefulness pass is done.
- `Astra-/collection/aw-junaid/COLLECTION_MANIFEST.md` (SHA `959afbe63f1f461466d8d10b9a6e062b3f14ec72`) records 33 repositories and public Gists with cross-repository Nmap scope; it explicitly requires source/destination refs, trees and content verification before completion. Existing destination content should remain preserved; do not merge this security-research collection into the trading-bot runtime.
- `Astra/collection` has separate `aw-junaid` and `nmap` trees; `Astra-/collection/aw-junaid` and `Files-/collection/mufeedvh` are distinct collection lanes. Their provenance should remain separate pending a content-level dedupe pass.
- `Easy-/api-registry/SOURCES.md` (SHA `55dc75dedbdf4ac3840326b6e7aeaeb75a7d3018`) records discovery catalogs for public APIs, model/vision/video, OCR, search and ecommerce. This is a candidate directory, not proof of free commercial access or production readiness. Preserve licensing, pricing, auth, rate-limit and data-retention gates.
- `Easy-/api-lab/PAID-OPPORTUNITY-MATRIX.md` (SHA `1c0127015666b54dc58e9b260b441f7fbafe6bef`) contains 10 B2B pilot concepts and KPI/pricing hypotheses. `CLIENT-HUNTING-STATUS.md` (SHA `3fa328312470c16662c44ddca0dfcebd68989aee`) explicitly records no verified paid conversion and some bounces; these are sales hypotheses/history, not customer or revenue evidence.
- `Project-/OPPORTUNITY-ENGINE.md` (SHA `2eadd334d0852f5bee4992ce4bd35b11083de6af`) and `REPUTATION-FIRST-SERVICE-PACK.md` (SHA `8f562c0054e57a06f00183435bd94b89ad4f3b86`) already define a zero-upfront-spend service path: lead-intake reliability, CRM/API sync, and AI intake with human review. Reuse this instead of creating a new offer taxonomy; re-verify old prospects and listings before outreach.
- `AI_operating_memory/CAPABILITY-MAP.md` (SHA `228f995dec6c91afc7bf8dbe401ee6f418997a2a`) points to existing canonical Skills in `agent-skills`. Its state policy says `PROJECT-STATE-MONY-CANONICAL.json` is the single machine-readable MONY state source; don't create competing state copies.
- `Astra/VERIFICATION.md` (SHA `a3d118aeb9293241c1efe48c1104e17ce5c8a303`) records 49/49 regression, real Kraken data and four assets, but the cross-asset/research gates fail, profitability remains unverified, and live execution is OFF. `Astra-/OPERATIONAL_READINESS.md` (SHA `9e7b20db69f01ec03c0ab8725d63af733b0ded1c`) keeps explicit human approval, reconciliation and kill-switch gates. Keep both research and bot boundaries separate.
- `Files-` has a minimal README, but its collection subtree is not empty. `Easy-` contains a provider-neutral knowledge bank, API registry, API lab, and explicit project boundary. These are valuable source inventories; no assets were installed or promoted during this read-only triage.

### First-party CI state observed
- `Salamou-31`: local SOAT runtime smoke and Railway-token access smoke succeeded on 2026-10-19; these are CI/runtime integration evidence, not production revenue or durable-storage proof.
- `Easy-`: latest Elite supervisor succeeded on 2026-10-18; recent ARMY-14 runs were cancelled. No new external creative-provider success was established here.
- `Astra`: prospective paper validation and handover workflows succeeded on 2026-10-18; research gates remain failed and live trading stays off.
- `Astra-`: last ASTRA BOT CI success observed on 2026-10-01; no newer run in the recent page.
- `Pastel-`: last Pages deployment success observed on 2026-10-09; QR migration remains gated on real-phone validation.
- `local-bridge.`: read-only diagnostics/listing workflows succeeded on 2026-10-13; no runner dispatch was triggered.
- `agent-skills`: latest runs visible in the first page are from 2026-10-09; the browser Skill update on 2026-10-19 has no observed post-change CI run.
- `Files-`: no GitHub Actions runs found.
