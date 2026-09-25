# Verification Queue — Next Frontier

Discovery has reached sufficient breadth; the next leverage comes from proving the highest-value candidates.

## Priority A — agent control and evidence
1. Preloop: inspect architecture/policy enforcement, MCP interception, approval failure paths, persistence, tests, Docker/Helm.
2. RelayRoom: inspect coordination state, persistence, authentication and worktree isolation.
3. Superlog/OpenObserve/SigNoz: inspect OTLP ingestion, retention, local storage, licensing and alerting.
4. Agent Reach: inspect adapters and health checks; map each channel to zero-config/authenticated/external-paid dependency.

## Priority B — durable automation
1. Hatchet: persistence, retries, idempotency, durable recovery.
2. Activepieces: self-host deployment, CE boundary, secrets, queues, retries and webhooks.
3. Windmill: source-build vs binary/image boundary, workers, queues, permissions.
4. Dagu/Healthchecks: lightweight scheduled execution and monitoring.
5. Temporal: compare operational footprint against Hatchet/Windmill.

## Priority C — research intake
1. Hoarder / ArchiveBox / RSSHub / FreshRSS / Miniflux.
2. SearXNG.
3. Crawl4AI.
4. Playwright / Browser Use.
5. Persistent evidence schema: source URL -> timestamp/revision -> raw artifact -> extracted artifact -> verification -> reusable capability.

## Priority D — infrastructure cost elimination
1. Coolify / Dokploy / Dokku / OpenTofu.
2. OpenBao / Authentik / Keycloak.
3. Restic / Kopia / Plakar.
4. SeaweedFS / Garage.
5. Uptime Kuma / Gatus / GlitchTip / OpenTelemetry.

## Priority E — local AI
1. Ollama / llama.cpp / vLLM / LocalAI.
2. LiteLLM as provider gateway.
3. AnythingLLM / Khoj / Dify / Langflow / Flowise.
4. Qdrant / Chroma / pgvector.
5. whisper.cpp / Piper.

## Completion gate
Do not emit COLLECTION COMPLETE until discovery source graph is exhausted for major replacement families, high-value candidates have repository evidence, the collection index links the verification corpus, unresolved paid/cloud/external dependencies are explicit, and no candidate is marked VERIFIED solely from an awesome-list or marketing claim.
