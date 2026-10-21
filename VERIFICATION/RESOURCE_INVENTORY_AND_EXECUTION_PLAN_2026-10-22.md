# Resource Inventory and Execution Plan — 2026-10-21

## Purpose
Evidence-backed inventory for COLLECTION and API Factory. Repository code and workflow runs are the source of truth for code/CI; provider dashboards are the source of truth for service state. Never infer credentials, free quotas, production readiness, or access from a connector merely existing.

## Verified connected surfaces

### GitHub
- Connected account: `salamou1944` (GitHub App installation confirmed).
- Core repositories in scope: `salamou1944/Project-` (COLLECTION), `salamou1944/Salamou-31` (API Factory), `salamou1944/agent-skills` (automation/control-plane), and `salamou1944/local-bridge.` (bridge diagnostics).
- COLLECTION continuous run `39676042890` completed successfully on 2026-10-21: https://github.com/salamou1944/Project-/actions/runs/39676042890
- JSON-shard IO workflow initially failed at `39677250418` because partitioning reordered array items. Fix committed on `feat/collection-json-shards-2026-10-22`; runs `39678581571` and `39678601654` were in progress when this record was written. Do not merge until latest verification passes.
- Passing CI proves only the named workflow scope, not production readiness.

### ChatGPT app/plugin discovery
- Targeted marketplace searches marked GitHub, OpenAI Developers, Vercel, and Higgsfield as installed.
- Hugging Face and TinyFish appeared available but not installed in targeted searches.
- Search results are query-dependent and are not a full export of every app installed in the ChatGPT UI.
- Hugging Face may help discover models/Spaces; TinyFish may offer browser automation if installed and authorized. Neither listing itself provides inference credits or production deployment rights.

### Cloud/runtime connectors
- Railway exposes projects `EASY Runtime Production` and `EASY Developer Platform`. A previously inspected `salamou31-api-factory` service inside EASY Runtime Production had no service variables, no attached volume, and a failed build (`BUILD_IMAGE` / Railpack prepare-build error). Do not redeploy it into EASY production or copy secrets there.
- Supabase exposed `salamou-31-api-factory` and `easy-platform-db`, both reported `ACTIVE_HEALTHY` by project listing. This is control-plane status only; verify schema, Edge Functions, buckets, policies, and actual read/write probes before claiming persistence works.
- Vercel exposed project `salamou31-api-factory`; project presence does not prove a successful production deployment.
- Termalin currently returns no available hosts through this connector. That does not prove the Termalin account has no hosts.
- Notion searches for `COLLECTION` and `API Factory` returned no matching pages in the queried surface; this does not prove the workspace is empty.

## Zero-cost inference candidates and gates
1. Local inference (Ollama or equivalent): strongest no-provider-billing candidate if a machine with sufficient resources is reachable. No connected Termalin host was available in this audit; previous CI-local Ollama success is not production proof.
2. Pollinations: a possible public endpoint to evaluate, not a guaranteed free production dependency. Check current terms, uptime, privacy, rate limits, model availability, and commercial use.
3. Hugging Face: useful for model discovery and hosted Spaces; free inference is not guaranteed for arbitrary models. Check current quota and eligibility.
4. NVIDIA NIM, Cloudflare Workers AI, Mistral, Hugging Face: keep NOT VERIFIED until credentials and explicit billing/free-tier settings are configured and a real request succeeds. Never assume a blank tier means free.
5. GitHub Actions: use for tests, audits, and bounded extraction, not as a permanent inference server; monitor minutes, artifacts, and runner availability.

## Execution order
1. Finish JSON-shard IO verification; fix failures on the branch and merge only after all tests pass.
2. Continue COLLECTION with bounded incremental runs. Record actual refreshed/blocked/deferred counts and audit outcomes before scheduling the next cycle; preserve blocked attempts and source data.
3. Audit the API Factory Supabase project: tables, Edge Functions, storage buckets, policies, and safe write/read verification without touching EASY data.
4. Audit Vercel and Railway separately: live URL, commit, build/runtime status, environment-variable names only, volume/storage, health checks, and cost limits.
5. Verify API Factory's end-to-end deploy adapter, durable quota/usage/idempotency storage, and provider-independent smoke path.
6. Test free inference candidates with a deterministic prompt; record endpoint/model/status/latency/usage/terms. Integrate only repeatable, commercially acceptable candidates.
7. Reconcile this connector inventory with the user's visible ChatGPT Apps list and service dashboards before calling the overall inventory complete.

## Evidence and safety rules
- AVAILABLE is not INSTALLED; INSTALLED is not CONNECTED; CONNECTED is not WORKING; WORKING is not PRODUCTION READY.
- Never store secret values in this file.
- No paid service, subscription, destructive refresh, production deployment, or EASY production change without explicit approval.
- Every status update must include a source URL/run ID or identify missing evidence.
