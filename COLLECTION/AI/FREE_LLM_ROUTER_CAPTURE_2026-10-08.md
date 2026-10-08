# Free LLM Router Capture — 2026-10-08

Source:
https://github.com/Pr0fess0rOP/free-llm-router

Category: AI / LLM / API / ROUTING / CODING AGENTS

Status: High-value engineering reference.

Observed capabilities:
- Self-hosted OpenAI-compatible gateway.
- Multi-provider failover.
- OpenAI Chat Completions and Responses/Codex routing.
- Claude Code compatibility.
- Model aliases/virtual models.
- Circuit breakers.
- Request deduplication.
- Analytics.
- Rate-limit cooldowns.
- Cloud-provider keys plus local Ollama.

Why valuable:
This is close to the control-plane behavior we want for AI/API Factory: one contract above heterogeneous providers, with provider health and failure state handled centrally.

Extraction targets:
- provider registry
- retry/failover classification
- circuit breaker
- virtual model aliases
- quota/cooldown state
- Codex/Responses compatibility

Constraint:
Use as architecture/reference until license, current provider terms and production behavior are independently verified.
