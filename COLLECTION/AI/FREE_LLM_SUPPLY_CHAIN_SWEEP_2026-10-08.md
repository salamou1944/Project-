# Free LLM Supply Chain Sweep — 2026-10-08

## Objective
Identify high-value free/low-cost LLM providers, OpenAI-compatible gateways, routers, and regional adapters that can materially strengthen the COLLECTION and future AI/API Factory.

## Decision
Prioritize infrastructure that can aggregate legitimate free tiers and open/compatible endpoints without bypassing authentication, quotas, paid restrictions, or provider controls.

## Verified high-value layers

### 1. FreeLLMAPI
Sources:
- https://github.com/rodrigoangeloni/free-llm-api
- https://github.com/CP102-BOT/freellmapi

Observed architecture:
- One OpenAI-compatible /v1 endpoint.
- Aggregates many provider free tiers.
- Automatic failover, quota tracking and encrypted key storage.
- Supports custom OpenAI-compatible endpoints including local/self-hosted runtimes.
- Provider set observed across Google, Groq, Cerebras, NVIDIA, Mistral, OpenRouter, Cloudflare, HuggingFace, Z.ai, Ollama, Kilo, Pollinations, LLM7, OVH AI Endpoints and OpenCode Zen.
- Some forks add ModelScope/Chinese provider coverage and coding-agent setup flows.

Assessment: HIGH VALUE REFERENCE. Study architecture; do not blindly depend on claimed aggregate token totals because provider quotas and eligibility change.

### 2. Free LLM Router
Source:
- https://github.com/Pr0fess0rOP/free-llm-router

Observed capabilities:
- Self-hosted OpenAI-compatible gateway.
- Multi-provider failover.
- Model aliases.
- Circuit breakers.
- Usage analytics.
- Secure key management.
- Supports OpenAI Responses/Codex and Claude Code paths.

Assessment: HIGH VALUE ENGINEERING REFERENCE for our routing/control plane.

### 3. LLM-Router
Source:
- https://github.com/neang-mengseang/LLM-Router

Observed capabilities:
- OpenAI-compatible single endpoint.
- 14 providers.
- Automatic failover.
- Circuit breaker.
- Virtual models.
- Direct provider testing.
- No external database/Redis dependency.

Assessment: HIGH VALUE lightweight implementation reference.

### 4. Russian provider bridge: ai-forever/gpt2giga
Source:
- https://github.com/ai-forever/gpt2giga

Purpose:
- Bridge OpenAI-style traffic to GigaChat.
- Useful regional provider adapter/reference.

Existing COLLECTION account inventory already contains ai-forever/gpt2giga; this sweep upgrades it from a repository mention to an explicit API-factory candidate.

Assessment: HIGH VALUE REGIONAL ADAPTER.

### 5. YandexGPT → OpenAI adapters
Sources:
- https://github.com/sazonovanton/YandexGPT_to_OpenAI
- related repository family discovered during GitHub search.

Purpose:
- Translate YandexGPT access into an OpenAI-shaped interface.

Assessment: MEDIUM/HIGH VALUE regional adapter; inspect license, maintenance and current API compatibility before production use.

## Provider layer

### United States / global
- Groq — official OpenAI-compatible endpoint; strong inference speed and open-weight model access.
- OpenRouter — free model variants and dynamic free router; free models have low limits and are not positioned as production capacity.
- Google AI Studio — free model quotas subject to current provider policy.
- Cloudflare Workers AI — edge inference/free-tier path where eligible.
- NVIDIA NIM — model/inference access with account/credit conditions.
- Mistral — Experiment/free-tier path where eligible.
- Hugging Face — inference provider/router layer.
- Z.ai / Zhipu — GLM provider.

### China
- Alibaba/Qwen — OpenAI-compatible model access and free quotas for eligible accounts/models.
- DeepSeek — OpenAI-compatible API, generally paid rather than permanently free.
- Kimi/Moonshot, GLM/Zhipu, MiniMax — preserve as provider candidates; verify current free quotas before classifying as free.
- ModelScope — important Chinese model distribution/inference ecosystem; verify endpoint and terms per model.

### Russia
- GigaChat / ai-forever
- YandexGPT
- Preserve regional adapters because they diversify provider geography and model supply.

## Routing policy for our future AI/API Factory

1. Free/legitimate quota first.
2. Never bypass auth, CAPTCHA, quotas, rate limits, paid-model restrictions or provider controls.
3. Never silently spend paid credits.
4. Track provider + account + model + quota + reset time + license/ToS evidence.
5. Fail over on 429/5xx/timeouts only where provider terms permit normal API retry.
6. Keep provider adapters behind one OpenAI-compatible contract.
7. Prefer self-hosted/open-weight inference when cloud free quotas become unstable.
8. Treat claimed aggregate token totals as estimates, not guaranteed capacity.
9. Production/customer workloads require explicit provider ToS/licensing review.

## Priority extraction
- Router/failover/quota accounting: extract as reusable Skills.
- Provider adapters: extract as provider-neutral capability contracts.
- Regional bridges: preserve as optional adapters.
- Model discovery: make runtime-driven rather than hard-coded.
- Cost guard: default FREE_ONLY and explicit opt-in for paid routing.

## Evidence status
Verified against current web/GitHub search on 2026-10-08. Free-tier availability is dynamic and must be revalidated before operational use.


## Second-region sweep — 2026-10-08

Additional current candidates found during regional sweep:

- **Nous Research / Nous Portal** — OpenAI-compatible inference endpoint with a $0 portal tier and free models. Treat as a provider candidate; verify current model/quota and commercial terms before routing production traffic.
- **UnoRouter** — OpenAI-compatible multi-model gateway advertising a large catalog of free routes. Treat as a discovery/fallback gateway, not as guaranteed production capacity.
- **ModelScope** — important China model/inference ecosystem. Preserve as a source for open-weight Chinese models and possible hosted inference; verify each model endpoint and license rather than treating the platform as universally free.
- **Z.ai / GLM** — Chinese provider with free Flash/Air options in current provider inventories; KYC/account eligibility must be tracked.
- **SambaNova** — US inference provider worth keeping as a performance/provider-diversity candidate; free/promotional terms are dynamic and must be verified before classifying as free.
- **TokenRouter** — emerging multi-provider/model gateway with promotional/free model routes; track as experimental.
- **Mistral** — European provider with a current free API tier in provider inventories; monthly credits and rate limits make it a useful secondary provider rather than a guaranteed unlimited source.
- **Cohere** — trial/evaluation API access; useful for multilingual/embedding-oriented workloads but not a permanent production-free tier.
- **Together AI** — selected $0 models/promotional access can be useful, but do not classify the entire platform as free.

### Regional conclusion

No strong evidence was found that a newly discovered India/Japan/Korea/Middle-East provider materially beats the existing core stack on **free + OpenAI-compatible + no-card + reusable infrastructure**. The strongest additions are therefore cross-regional gateways (Nous Portal, UnoRouter), Chinese model infrastructure (ModelScope), and provider-diversity candidates (Mistral, Cohere, SambaNova, TokenRouter).

### Selection rule

Do not add providers merely because a directory lists them. Promote a provider into the operational tier only after current verification of:
1. free quota,
2. card/KYC requirements,
3. OpenAI compatibility,
4. tool/vision/coding capability where needed,
5. commercial-use terms,
6. geographic eligibility,
7. rate limits and reset behavior.
