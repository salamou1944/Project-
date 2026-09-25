# LONG COLLECTION BATCH — 2026-09-25

Status: DISCOVERY_CAPTURED
Purpose: largest current discovery batch for reducing recurring SaaS/API subscriptions through self-hosted/open-source/local software. This file is a source-preservation layer, not a production-adoption verdict.

## Operating rule
- Discovery is not verification.
- Preserve upstream repository, license/edition caveats, deployment model, and external dependencies.
- Prefer software that can run locally/self-hosted.
- Separate true open source from source-available/fair-code and cloud-only offerings.
- Hosting, email delivery, model inference, payment rails, domain/DNS and third-party network APIs can still create external costs.

## High-value infrastructure / PaaS / deployment
- https://github.com/coollabsio/coolify — self-hosted deployment/PaaS candidate.
- https://github.com/Dokploy/dokploy — Docker/Compose-oriented deployment candidate.
- https://github.com/caprover/caprover — lightweight PaaS candidate.
- https://github.com/dokku/dokku — Heroku-like git-push deployment.
- https://github.com/railwayapp/railway — reference only; hosted dependency, not a self-hosted replacement.
- https://github.com/serversideup/docker-php — deployment/runtime reference.
- https://github.com/kubernetes/kubernetes — orchestration, higher operational cost.
- https://github.com/k3s-io/k3s — lightweight Kubernetes candidate.
- https://github.com/portainer/portainer — container management; verify edition boundary.
- https://github.com/ansible/ansible — infrastructure automation.
- https://github.com/opentofu/opentofu — infrastructure-as-code candidate.
- https://github.com/woodpecker-ci/woodpecker — self-hosted CI candidate.
- https://github.com/go-gitea/gitea — Git forge candidate.
- https://github.com/forgejo/forgejo — Git forge candidate.
- https://github.com/gitlabhq/gitlabhq — integrated forge/CI candidate; verify edition/resources.

## Identity / authentication / authorization / secrets
- https://github.com/keycloak/keycloak — IAM/SSO candidate.
- https://github.com/goauthentik/authentik — self-hosted identity candidate.
- https://github.com/zitadel/zitadel — identity platform candidate; verify licensing/cloud boundary.
- https://github.com/openbao/openbao — secrets-management candidate.
- https://github.com/Infisical/infisical — secrets/config candidate; verify license and enterprise boundaries.
- https://github.com/bitwarden/server — password/secrets ecosystem candidate; verify exact self-hosting/licensing boundaries.
- https://github.com/Authelia/authelia — authentication/2FA reverse-proxy candidate.
- https://github.com/ory/kratos — identity candidate.
- https://github.com/cerbos/cerbos — authorization policy engine candidate.
- https://github.com/spiffe/spire — workload identity candidate.
- https://github.com/juanfont/headscale — self-hosted Tailscale control-plane candidate.
- https://github.com/netbirdio/netbird — self-hosted mesh/zero-trust candidate.
- https://github.com/netmaker/netmaker — networking/control-plane candidate.

## Automation / durable execution / orchestration
- https://github.com/n8n-io/n8n — workflow automation; license/edition boundary must be checked.
- https://github.com/activepieces/activepieces — workflow automation candidate.
- https://github.com/windmill-labs/windmill — code-first workflow/job platform.
- https://github.com/kestra-io/kestra — orchestration candidate.
- https://github.com/temporalio/temporal — durable workflow engine.
- https://github.com/apache/airflow — data/workflow orchestration.
- https://github.com/dagster-io/dagster — data/asset orchestration.
- https://github.com/huginn/huginn — event/agent automation.
- https://github.com/triggerdotdev/trigger.dev — code-first background jobs; verify self-hosting/licensing.
- https://github.com/hatchet-dev/hatchet — durable task/workflow execution candidate.
- https://github.com/prefecthq/prefect — workflow orchestration candidate; verify OSS/cloud boundary.
- https://github.com/argoproj/argo-workflows — Kubernetes-native workflows.

## AI local inference / agent runtime / model gateway
- https://github.com/ollama/ollama — local model runtime.
- https://github.com/ggml-org/llama.cpp — local inference/runtime.
- https://github.com/vllm-project/vllm — high-throughput inference.
- https://github.com/mudler/LocalAI — OpenAI-compatible local AI server.
- https://github.com/BerriAI/litellm — model/provider gateway; verify license and hosted dependencies.
- https://github.com/open-webui/open-webui — local AI web interface.
- https://github.com/janhq/jan — local AI desktop/runtime candidate.
- https://github.com/nomic-ai/gpt4all — local model application/runtime.
- https://github.com/exo-explore/exo — distributed/local inference candidate.
- https://github.com/ggml-org/whisper.cpp — local speech recognition.
- https://github.com/OHF-Voice/piper1-gpl — local TTS candidate; verify current repo/license.
- https://github.com/sgl-project/sglang — inference serving candidate.
- https://github.com/huggingface/text-generation-inference — model serving candidate.
- https://github.com/unslothai/unsloth — local model fine-tuning/optimization candidate.
- https://github.com/langchain-ai/langgraph — agent/stateful orchestration candidate.
- https://github.com/openai/openai-agents-python — agent SDK reference; hosted model dependency may remain.
- https://github.com/pydantic/pydantic-ai — typed agent framework.
- https://github.com/joaomdmoura/crewAI — multi-agent orchestration candidate.
- https://github.com/microsoft/autogen — agent framework/reference; verify current project direction.
- https://github.com/google/adk-python — agent development kit.
- https://github.com/All-Hands-AI/OpenHands — coding agent candidate.
- https://github.com/Aider-AI/aider — coding agent candidate.
- https://github.com/continuedev/continue — local/remote coding assistant candidate.
- https://github.com/letta-ai/letta — stateful agent memory candidate.
- https://github.com/run-llama/llama_index — RAG/data framework.
- https://github.com/deepset-ai/haystack — RAG/agent pipeline framework.
- https://github.com/qdrant/qdrant — vector database.
- https://github.com/chroma-core/chroma — vector database.
- https://github.com/mem0ai/mem0 — memory layer candidate; verify self-hosting/licensing.

## Browser / web research / extraction
- https://github.com/microsoft/playwright — browser automation.
- https://github.com/browser-use/browser-use — browser agent framework.
- https://github.com/Panniantong/Agent-Reach — multi-channel web research/capability router.
- https://github.com/unclecode/crawl4ai — crawling/extraction candidate.
- https://github.com/firecrawl/firecrawl — crawl/extract platform; verify self-hosted/community limits.
- https://github.com/scrapy/scrapy — crawling framework.
- https://github.com/SearXNG/SearXNG — metasearch.
- https://github.com/benbusby/whoogle-search — private search proxy candidate.
- https://github.com/yacy/yacy_search_server — distributed search candidate.
- https://github.com/usewrit/writ — browser workflow recorder/replayer candidate.
- https://github.com/smouj/agent-browser — browser-control candidate.

## Search / databases / analytics
- https://github.com/meilisearch/meilisearch — search engine.
- https://github.com/typesense/typesense — search engine.
- https://github.com/opensearch-project/OpenSearch — search/analytics.
- https://github.com/apache/solr — search.
- https://github.com/manticoresoftware/manticoresearch — search.
- https://github.com/sist2app/sist2 — filesystem/web index candidate.
- https://github.com/postgres/postgres — relational database.
- https://github.com/duckdb/duckdb — analytical embedded DB.
- https://github.com/sqlite/sqlite — embedded DB.
- https://github.com/cockroachdb/cockroach — distributed SQL candidate; verify current licensing.
- https://github.com/ClickHouse/ClickHouse — analytical DB.
- https://github.com/valkey-io/valkey — Redis-compatible data store.
- https://github.com/dragonflydb/dragonfly — in-memory datastore candidate; verify license.
- https://github.com/neo4j/neo4j — graph database; verify edition.
- https://github.com/SurrealDB/surrealdb — multi-model DB candidate.
- https://github.com/matomo-org/matomo — web analytics.
- https://github.com/plausible/analytics — privacy analytics.
- https://github.com/umami-software/umami — lightweight analytics.
- https://github.com/PostHog/posthog — product analytics/flags; verify open-source/core boundaries.
- https://github.com/Openpanel-dev/openpanel — product analytics candidate.
- https://github.com/metabase/metabase — BI candidate; verify license/edition.
- https://github.com/apache/superset — BI candidate.
- https://github.com/grafana/grafana — dashboards/observability; verify edition.
- https://github.com/unleash/unleash — feature flags.
- https://github.com/Flagsmith/flagsmith — feature flags/config.

## Observability / monitoring / security
- https://github.com/SigNoz/signoz — OpenTelemetry observability.
- https://github.com/open-telemetry/opentelemetry-collector — telemetry pipeline.
- https://github.com/jaegertracing/jaeger — tracing.
- https://github.com/grafana/loki — logs.
- https://github.com/grafana/tempo — traces.
- https://github.com/prometheus/prometheus — metrics.
- https://github.com/louislam/uptime-kuma — uptime monitoring.
- https://github.com/TwiN/gatus — service health monitoring.
- https://github.com/glitchtip/glitchtip — error tracking.
- https://github.com/aquasecurity/trivy — vulnerability/container/license scanning.
- https://github.com/anchore/grype — vulnerability scanner.
- https://github.com/anchore/syft — SBOM generation.
- https://github.com/semgrep/semgrep — static analysis/security.
- https://github.com/google/osv-scanner — dependency vulnerability scanning.
- https://github.com/ossf/scorecard — supply-chain checks.
- https://github.com/securego/gosec — Go security scanning.
- https://github.com/gitleaks/gitleaks — secret detection; upstream currently signals maintenance/security focus, so verify transition.
- https://github.com/wazuh/wazuh — security monitoring/SIEM candidate.
- https://github.com/zeek/zeek — network security monitoring.
- https://github.com/OISF/suricata — IDS/IPS.

## Storage / backup / sync
- https://github.com/seaweedfs/seaweedfs — object/file storage.
- https://github.com/deuxfleurs-org/garage — S3-compatible distributed storage.
- https://github.com/restic/restic — encrypted backups.
- https://github.com/kopia/kopia — backup/snapshot system.
- https://github.com/borgbackup/borg — deduplicated encrypted backup.
- https://github.com/borgmatic-collective/borgmatic — Borg automation.
- https://github.com/duplicati/duplicati — backup candidate.
- https://github.com/uroni/urbackup — backup server.
- https://github.com/syncthing/syncthing — peer-to-peer file synchronization.
- https://github.com/rclone/rclone — cloud/object/file transfer and sync.
- https://github.com/minio/minio — S3 object storage candidate; current OSS/support posture must be re-verified before adoption.
- https://github.com/photoprism/photoprism — self-hosted photo management.
- https://github.com/immich-app/immich — self-hosted photo/video management.

## Documents / media / creative
- https://github.com/ocrmypdf/OCRmyPDF — OCR/PDF pipeline.
- https://github.com/docling-project/docling — document parsing.
- https://github.com/tesseract-ocr/tesseract — OCR.
- https://github.com/Stirling-Tools/Stirling-PDF — PDF toolkit candidate.
- https://github.com/danielgatis/rembg — local background removal.
- https://github.com/upscayl/upscayl — local image upscaling.
- https://github.com/comfyanonymous/ComfyUI — local image/video generation workflow.
- https://github.com/FFmpeg/FFmpeg — media processing.
- https://github.com/obsproject/obs-studio — recording/streaming.
- https://github.com/kdenlive/kdenlive — video editing.
- https://github.com/openshot/openshot-qt — video editing.
- https://github.com/audacity/audacity — audio editing.
- https://github.com/Automattic/harper — local writing/grammar candidate.
- https://github.com/penpot/penpot — design/prototyping candidate; verify current edition/license.

## Communication / email / collaboration
- https://github.com/mattermost/mattermost — team communication; verify current edition.
- https://github.com/RocketChat/Rocket.Chat — team communication; verify licensing/edition.
- https://github.com/jitsi/jitsi-meet — meetings.
- https://github.com/nextcloud/server — files/collaboration.
- https://github.com/haiwen/seafile — file sync/collaboration; verify edition.
- https://github.com/docker-mailserver/docker-mailserver — mail server.
- https://github.com/mailcow/mailcow-dockerized — mail stack.
- https://github.com/StalwartLabs/stalwart — mail server.
- https://github.com/roundcube/roundcubemail — webmail.
- https://github.com/the-djmaze/snappymail — webmail.
- https://github.com/atech/postal — transactional mail platform.
- https://github.com/mautic/mautic — marketing automation.
- https://github.com/knadh/listmonk — newsletters/transactional campaigns.
- https://github.com/keila-wings/keila — email marketing candidate.
- https://github.com/phpList/phplist3 — email marketing candidate.

## CRM / support / internal business tools
- https://github.com/twentyhq/twenty — CRM candidate.
- https://github.com/espocrm/espocrm — CRM.
- https://github.com/salesagility/SuiteCRM — CRM.
- https://github.com/frappe/crm — CRM candidate.
- https://github.com/chatwoot/chatwoot — customer support.
- https://github.com/zammad/zammad — helpdesk.
- https://github.com/odoo/odoo — ERP/CRM ecosystem; verify edition.
- https://github.com/frappe/erpnext — ERP/business suite.
- https://github.com/plane-software/plane — project management.
- https://github.com/openproject/openproject — project management.
- https://github.com/Vikunja/vikunja — task/project management.
- https://github.com/nocodb/nocodb — database-to-spreadsheet interface.
- https://github.com/bramw/baserow — database/spreadsheet workspace.
- https://github.com/appsmithorg/appsmith — internal tools/app builder.
- https://github.com/ToolJet/ToolJet — internal tools.
- https://github.com/illacloud/illa-builder — internal tool builder.
- https://github.com/usememos/memos — lightweight knowledge/notes.

## Forms / e-sign / scheduling
- https://github.com/formbricks/formbricks — forms/surveys.
- https://github.com/ohmyform/ohmyform — forms.
- https://github.com/documenso/documenso — e-sign.
- https://github.com/docusealco/docuseal — e-sign.
- https://github.com/OpenSignLabs/OpenSign — e-sign candidate.
- https://github.com/calcom/cal.com — scheduling.
- https://github.com/cal-diy/cal.diy — scheduling candidate.
- https://github.com/easyappointments/easyappointments — scheduling.
- Legal validity of e-signatures remains jurisdiction-dependent.

## Commerce / payments / billing
- https://github.com/medusajs/medusa — commerce backend.
- https://github.com/saleor/saleor — commerce platform.
- https://github.com/vendure-ecommerce/vendure — commerce framework.
- https://github.com/prestashop/prestashop — e-commerce.
- https://github.com/getlago/lago — usage-based billing/metering candidate.
- https://github.com/killbill/killbill — subscription/billing platform.
- https://github.com/actualbudget/actual — budgeting; not payment processing.
- https://github.com/firefly-iii/firefly-iii — finance management.
- Payment gateways, bank connectivity, card networks and regulatory/KYC requirements remain external dependencies.

## Data pipelines / ETL
- https://github.com/airbytehq/airbyte — data integration.
- https://github.com/meltano/meltano — ELT/data integration.
- https://github.com/dlt-hub/dlt — data loading pipelines.
- https://github.com/apache/nifi — dataflow.
- https://github.com/apache/kafka — event streaming.
- https://github.com/redpanda-data/redpanda — Kafka-compatible streaming candidate.
- https://github.com/debezium/debezium — CDC.
- https://github.com/apache/flink — stream/batch processing.
- https://github.com/apache/spark — distributed processing.
- https://github.com/duckdb/duckdb — local analytical engine.
- https://github.com/ClickHouse/ClickHouse — analytical warehouse.

## Research directories / discovery indexes
- https://github.com/SolvoHQ/awesome-self-host-saas-alternatives — 100 SaaS / 294 alternatives snapshot; discovery metadata, not adoption proof.
- https://github.com/open-saas-directory/awesome-saas-directory — open-source/self-hosted SaaS directory.
- https://selfhosttools.com/ — 225 curated tools, 17 categories, 2026 snapshot.
- https://selfhostindex.com/ — broad self-hostable catalog; directory snapshot.
- https://github.com/awesome-selfhosted/awesome-selfhosted — large self-hosted discovery index.
- https://www.openelse.dev/blog/ultimate-list-open-source-alternatives-developer-saas — developer SaaS discovery.
- https://ideaproof.io/open-source/self-hosted — maintained-project discovery index.
- https://ossfind.com/ — SaaS alternatives discovery.
- https://altfreestack.com/ — free/open-source stack discovery.

## Verification queue
1. Directly inspect repository LICENSE and edition boundaries.
2. Inspect deployment manifests and installation path.
3. Check release/activity and archived status.
4. Identify cloud-only features and external metered APIs.
5. Identify security/authentication model and secret handling.
6. Check backup/restore and data export.
7. Check commercial-use and redistribution terms.
8. Test the highest-value candidates locally where feasible.
9. Promote only evidence-backed candidates to VERIFIED/REUSABLE.


## README extraction batch — aw-junaid (2026-09-25)
The following repositories were directly fetched from their current default-branch README.md during the collection pass; each entry records the observed blob SHA and an excerpt for semantic indexing.

### Hacking-Tools
SHA: 05877acce00b2c9ea0989f3fd56958089016d2dd
Purpose: security research / malware analysis / education collection. README explicitly limits use to authorized research, malware analysis, and education.

### Kali-Linux
SHA: d3db045f5844a82fc2524e999e4ee643cb979c31
Purpose: Kali Linux tools documentation, including web penetration testing, ethical hacking and forensics.

### bug-bounty
SHA: e67128a5f0e4f61d5ebe38b1941c3d2c318bd8e1
Purpose: bug-bounty/security reference collection; README indicates MIT license.

### Black-Hat-Python
SHA: de1f97efeb682bb291b4f9522f734cb74dfe736f
Purpose: Black Hat Python reference/materials; README notes some code portions originate from other open sources.

### Computer-Science
SHA: 80f5e29ce1331b3650eec46ed8a3166c031c0451
Purpose: broad computer-science/programming resource index, including learning resources and project ideas.

### Python-System-Administration
SHA: efef9e4f15a54c8e7ccae56060c9fe29f7f66aca
Purpose: Python scripts, automation, DevOps utilities, system administration, infrastructure management, cloud automation and monitoring examples.

### cybersec-projects
SHA: a8ea48f3e73060343978fbbaf719385748d1b72e
Purpose: hands-on cybersecurity learning/research projects, offensive and defensive tools, automation and simulations.

### self-hostable-services
SHA: b1409a311b32c007eaa35a53db6116eb8e50e047
Purpose: free self-hostable network/web services, including email, file sharing, CMS, automation, backup, booking, communication and related categories; Docker support is highlighted.

### Security-and-Hacking
SHA: 32f1b99860e0399a41e0e08756ab7cf680bde0f5
Purpose: security/hacking reference spanning network, endpoint, web, reverse engineering, cryptography, CTF and bug-bounty categories.

### Password-Cracking
SHA: b55126b348a6942d1da1b18ec9f3bc3f79f16986
Purpose: password-cracking reference covering Hashcat, John the Ripper, wordlists, file formats, AI and research; treated as security-reference material, not an operational target list.


## README extraction batch — aw-junaid 02
- programming-books — SHA aad4eef31898376bd32e729667f52b9412a04639 — curated free programming books/resources.
- Neuroscience — SHA d30099d325658a8baba81fa05d7b4aa2dca2677d — computational neuroscience concepts, datasets, tools and research.
- golang-web-security — SHA 4d9c7e24750f95a29c95619d4f52592e5f21285b — secure Go web development: auth, authorization, validation, CSRF, headers.
- Machine-Learning-For-Security — SHA 6b6e83135c349518065fd5df46ebe73b6572fb8d — anomaly detection, malware classification, threat prediction.
- android-security — SHA 17fcc7d1b71239a142907bb89827b4c0f7663b6c — Android secure development, reverse engineering, vulnerability testing.
- PHP-Web-Security — SHA 3a5f960c415fc6784970f11d302a1a8259e172be — PHP web security reference.
- Web-Security — SHA be569f4f81d0c426cd3926d2195991997a680c3c — OWASP Top 10, XSS, SQLi, CSRF and secure coding.
- Malware-Analysis — SHA acbf8b40b8f66c249d28c9ae2596e115ee9ad80b — static/dynamic analysis, reverse engineering and sandboxing.
- awesome — README.md not found on default path during this fetch; tree metadata remains authoritative for existence.
- Docker — SHA 20cc7f2a055196449ed7c01221e54e243388e77d — Docker-oriented reference repository.
