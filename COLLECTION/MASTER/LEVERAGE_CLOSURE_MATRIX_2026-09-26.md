# LEVERAGE CLOSURE MATRIX — 2026-09-26

Status: EXECUTION_QUEUE
Purpose: identify existing/open-source/ready-made components that can shorten EASY, MONY, Salamou-31, Elite/ARMY-14 and revenue delivery without inventing readiness.

## 1. Highest-leverage ready-made foundations

### EASY / commerce
- Medusa — headless commerce backend; candidate for replacing custom catalog/cart/order foundations.
- Saleor — headless commerce/API; candidate where GraphQL/Python fit and license boundaries are acceptable.
- Vendure — TypeScript/NestJS/GraphQL, plugin-first commerce; candidate for marketplace/omnichannel foundations.
- PrestaShop — turnkey traditional commerce; candidate when speed matters more than headless architecture.
- WooCommerce — mature turnkey WordPress commerce; candidate for client delivery/integration rather than rebuilding commerce primitives.
- Lago / Kill Bill — billing/subscription primitives for Salamou-31 or future SaaS.

### EASY support / customer operations
- Chatwoot — support/inbox foundation.
- Twenty / EspoCRM — CRM/customer pipeline foundation.
- Mautic / Listmonk — marketing and mailing foundations.
- Cal.com — scheduling foundation.

### EASY creative
- rembg — local background removal.
- Upscayl — local upscaling.
- ComfyUI — composable local image-generation/editing workflows.
- FFmpeg — media processing.
- whisper.cpp / Piper — local speech/voice components.
- Krita/GIMP/Inkscape/Penpot — editing/design foundations.

### Salamou-31 / AI API
- LiteLLM/Ollama/llama.cpp/vLLM/LocalAI/Open WebUI — provider/local-model abstraction and local inference.
- Apache APISIX / STOA / Ferro Labs AI Gateway / Preloop — API/AI gateway, policy, routing, audit and MCP control-plane candidates.
- SOAT / OGAC / Atlas — candidate integrated AI control-plane/reference architectures.
- Docling/OCRmyPDF/Tesseract — document/OCR pipeline foundations.

### Elite / ARMY-14
- Cloudflare security-audit-skill — coding-agent security-audit pattern.
- Alibaba open-code-review — AI code-review engine.
- ECC — agent operating-system pattern: skills, hooks, rules, MCP, memory, adapters.
- Railway agent-skill + hosted MCP — deployment/control-plane integration pattern.
- OpenTelemetry/SigNoz/Prometheus/Grafana/Uptime Kuma/Trivy/OSV-Scanner/Semgrep — observability/security verification stack.

### Research/browser/data collection
- Writ — browser workflow recorder/replayer + MCP.
- WebOperator/WebNav/AgentBrowser — local/service browser automation candidates.
- SearXNG + Crawl4AI + Scrapy + Playwright — research/collection stack.
- FreshRSS/Miniflux — persistent research/RSS intake.

## 2. Subscription-elimination map already captured

- Shopify/WooCommerce custom commerce -> Medusa/Saleor/Vendure/PrestaShop.
- Intercom/Zendesk -> Chatwoot/Zammad.
- HubSpot/Salesforce -> Twenty/EspoCRM/SuiteCRM.
- Mailchimp -> Mautic/Listmonk.
- Calendly -> Cal.com.
- Notion/Confluence -> AppFlowy/AFFiNE/Outline/Wiki.js/BookStack.
- Airtable -> NocoDB/Baserow.
- Postman -> Hoppscotch/Bruno/Yaak/HTTPie/Restfox.
- GitHub/GitLab hosted workflows -> Gitea/Forgejo/GitLab CE where appropriate.
- PaaS -> Coolify/Dokku/CapRover.
- Datadog/APM -> OpenTelemetry/SigNoz and related OSS.
- Snyk/dependency security -> Trivy/OSV-Scanner/Grype/Syft/Semgrep.
- Sentry -> GlitchTip or self-hosted Sentry where licensing/edition permits.
- Cloud AI -> local Ollama/llama.cpp/vLLM/LocalAI where capability and hardware permit.
- Buffer/Hootsuite/Sprout -> Postmill/Mixpost/Postiz/Socioboard candidates.
- OCR/document APIs -> OCRmyPDF/Docling/Tesseract.
- Browser cloud automation -> Writ/WebOperator/WebNav/AgentBrowser candidates.

## 3. What can shorten projects immediately

1. Stop rebuilding generic commerce primitives; evaluate Medusa/Vendure/PrestaShop against EASY's exact requirements.
2. Stop rebuilding support inbox/CRM primitives; evaluate Chatwoot + Twenty/EspoCRM.
3. Move EASY Creative Engine's non-LLM image operations local first: rembg + Upscayl + ComfyUI only where tests prove the gap.
4. Use n8n templates as delivery accelerators instead of designing common workflows from zero.
5. Use local model gateways/inference where they actually replace the current OpenAI dependency; EASY's current OpenAI 429 remains BLOCKED_EXTERNAL_DEPENDENCY until an alternative is verified.
6. Use OCRmyPDF/Docling/Tesseract as the base for document-automation client pilots.
7. Use API gateways/control planes rather than rebuilding routing/auth/quotas/audit from zero.
8. Use ECC/security-audit/open-code-review patterns to strengthen Elite/ARMY-14 instead of inventing equivalent scaffolding.

## 4. Current revenue routes

- Automation repair sprint.
- AI/API integration pilot.
- n8n/AI automation implementation.
- CRM/WhatsApp/API integrations.
- Document extraction/automation.
- E-commerce integration/diagnostics.
- Support Resolution Engine pilot.
- Product-content API as a paid API or done-for-you integration.
- Productized security/automation audit.
- Long-term agency implementation partnership.

Current public demand confirms active n8n/AI work, including ongoing agency collaboration and larger automation engagements. These are opportunities, not revenue until acceptance/payment evidence exists.

## 5. Top-5 weekly collection — 2026-09-26

1. cloudflare/security-audit-skill — deep verification pending/continuation.
2. alibaba/open-code-review — identity/license/function captured; integration proof pending.
3. affaan-m/ECC — identity/license/function captured; integration proof pending.
4. stablyai/orca — deep extraction pending.
5. Tencent/WeKnora — deep extraction pending.

Do not merge this weekly Top Five with the separate total-star Top-10 queue.

## 6. Not yet safe to call "ready"

Discovery is not adoption. Every candidate must pass:
license -> source/release -> deployment -> dependency/cost -> auth/security -> tests/health -> actual integration proof -> project-specific acceptance.

No platform should be forked/deployed merely because it appears in a catalog.

## 7. Execution priority

P0:
- revenue deliverables using existing code + n8n templates;
- EASY commerce/support foundation evaluation;
- EASY local creative replacement proof;
- Salamou-31 API gateway/provider abstraction;
- ARMY-14 evidence/security leverage.

P1:
- document pipeline;
- CRM/marketing/social stack;
- browser/research collection stack.

P2:
- broader self-hosted replacements and platform consolidation.

Evidence rule:
DISCOVERY -> VERIFIED -> INTEGRATED -> TESTED -> HUMAN_READY.
Never mark a candidate as integrated or production-ready from documentation alone.
