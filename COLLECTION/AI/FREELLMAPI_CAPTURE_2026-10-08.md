# FreeLLMAPI Capture — 2026-10-08

Source repositories:
- https://github.com/rodrigoangeloni/free-llm-api
- https://github.com/CP102-BOT/freellmapi

Category: AI / LLM / API / ROUTING

Status: High-value reusable architecture reference.

Observed:
- OpenAI-compatible single endpoint.
- Multi-provider aggregation.
- Automatic failover.
- Quota/usage tracking.
- Encrypted API-key storage.
- Custom OpenAI-compatible provider support.
- Provider adapters spanning major US/global providers plus Z.ai, Cloudflare, Hugging Face, OpenCode Zen, Kilo and other free/anonymous paths.
- Some variants include Chinese ModelScope coverage and coding-agent setup integrations.

Important constraint:
The project describes aggregate free-token capacity, but provider quotas, eligibility, rate limits and terms are dynamic. Treat totals as estimates, not guaranteed production capacity.

Reuse:
- Provider registry
- quota ledger
- cooldown/circuit-breaker logic
- free-only routing guard
- OpenAI-compatible compatibility layer
- local/self-hosted endpoint integration

Safety/legal:
Use only legitimate provider access. Do not bypass authentication, quotas, paid restrictions or provider controls. Review each provider's current ToS before commercial routing.

License/maintenance:
Must be verified per selected upstream/fork before code reuse; forks may differ.

Assessment: HIGH.
