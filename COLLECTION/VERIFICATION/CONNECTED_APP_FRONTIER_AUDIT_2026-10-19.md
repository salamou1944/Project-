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

## Current frontier run

- Collection extraction workflow: [run 39180002514](https://github.com/salamou1944/Project-/actions/runs/39180002514), started by the updated owner-frontier commit `857010f226ccd7efdde94a22297d19ed32237053`; it was `pending` at the last observation.
- API Factory SOAT integration: [run 39179590053](https://github.com/salamou1944/Salamou-31/actions/runs/39179590053); real AI completion through the intended local Ollama provider passed its dedicated step, while the official SOAT smoke and downstream evidence persistence steps remained in progress/pending. No overall workflow success is claimed yet.


## Additional high-priority supply-chain finding
The monitored source `mnfst/awesome-free-llm-apis` had a historical malicious workflow in commit `48fcbe86582e16b7b746fee52e5512a891a8db76`: it searched repository/history for credential patterns and POSTed findings to `193.32.204.199:8080`. It was removed in `cf97c32fec1b2e96e9936746e2731a81bd5ea33f`. No “Security Audit” run appeared in the latest 30 visible Actions runs, but execution remains unverified. Treat the catalogue as untrusted discovery input; do not run its scripts/workflows or pass it secrets. No secrets were searched for or transmitted.


## Extended workspace inventory — 2026-10-19

- Notion private sidebar pages/databases: 0 returned; favorites: 0; recent pages: 0. The earlier targeted search also returned no matches. This means the connected workspace exposed no pages through these read operations, not that the workspace is necessarily empty or that all access paths were exhausted.
- Canva design search for `EASY` and `API Factory`: 0 matching designs returned.
- AgentMail account list: 0 signed-in app accounts. This is separate from the three AgentMail inboxes, which exist and were inspected above.
- The enabled `Revenue + leverage sweep` automation was requested for an immediate run (automation ID `6ab730fda9948191a73f262cdb30fa92`). The request was accepted; execution is asynchronous, so no completed sweep result is claimed here.


## Recipient-level bounce handling
The following addresses were observed in failed delivery threads and should not be retried without independent re-verification: `contact@deevdigital.com`, `contact@goldway-dz.com`, `support@ecomproassociates.com`, `hello@gmsolutions.com`, `hallo@gtpmedia.nl`, `info@channelboosters.io`, `sales@flexshopltd.com`, `contact@scaleverse.media`, `michael@nuworld.agency`, `hello@teroinlabs.com`, and `hello@agencemerlin.com`. These are bounces, not leads; no outbound messages were sent in this sweep.
