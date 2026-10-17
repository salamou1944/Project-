# API Factory Persistence and Export Hardening — 2026-10-17

Status: IMPLEMENTED_IN_SOURCE; API_FACTORY_SUITE_PASSED_ON_CODE_COMMIT; LATEST_DOC_COMMIT_RECHECK_RUNNING; DURABLE_BACKEND_NOT_CONFIGURED
Source repository: https://github.com/salamou1944/Salamou-31
Branch: `feat/api-factory-railway-deployable-2026-10-16`
Current runtime source commit deployed: `95ede6c3074f7fcfd23c38866e793c1b11be0f36`; latest branch head after documentation boundary update: `7651b5b8413c89c1057c8e85c835ed9a0977cc41`
Vercel project: `salamou31-api-factory`
Production deployment: `dpl_4vmQMfn4hr5SahXSJxf1ruh8pbYs` — verified `READY`.
Stable alias `https://salamou31-api-factory.vercel.app` now resolves to `dpl_4vmQMfn4hr5SahXSJxf1ruh8pbYs`.

## Implemented

- `registry-store.mjs`: file-backed local registry plus Supabase REST singleton-row persistence, atomic local writes, request timeout, and fail-closed behavior if a partially configured or failed remote store is used.
- `artifact-store.mjs`: private Supabase Storage upload, inspection, and retrieval for generated API files; local/ephemeral mode is explicitly marked non-durable.
- `migrations/20261017_api_factory_storage.sql`: dedicated table with RLS and a private artifact bucket.
- `PERSISTENCE.md`: setup instructions and strict separation from EASY's Supabase project.
- `GET /v1/factory/export/:name`: authenticated export of generated files as a JSON bundle; file retrieval works from local storage or remote object storage.
- `/ready` now returns storage-mode checks and `degraded` when registry/artifact storage is not durable.
- New tests cover registry upsert/read behavior, private artifact persistence/retrieval, fail-closed remote failures, and authenticated bundle export.

## Evidence and current limits

- Existing API Factory tests had previously passed the compiler/generated-runtime/auth/idempotency/provider-fail-closed checks.
- A subsequent CI run failed because `test-server.mjs` contained literal escaped newlines. The test was corrected and its storage assertions were aligned with the response shape. API Factory Test run `38989110726` passed, including the strict provider-policy regression test, on code commit `6b67fbf4b80eccd38358dbc08b42a66a85b4b3bc`. API Factory Test run `38989207081` completed successfully, including the dynamic test-date update and direct zero-cost provider-policy tests.
- Vercel health/readiness had passed earlier. Live smoke run `38989207054` passed after the stable alias was assigned to the latest READY deployment; it verified health, readiness/degraded state, capabilities/export metadata, and unauthenticated export rejection.
- Durable storage is implemented in code but not active: no dedicated Supabase project has been created, and no storage credentials have been added. The only discovered Supabase project belongs to EASY and is intentionally excluded.
- No paid service was created or upgraded. Railway remains unavailable due expired trial.
- The Vercel project is not yet proven Git-linked; deployment remains a manually initiated source-file deployment.
- API Factory deployment adapters still deliberately report unimplemented for Railway/Vercel. The export bundle is a working output path, not proof of one-click deployment.

## Required next gates

1. Get the user's explicit organization choice before creating a separate Supabase project; only then create the dedicated free-tier project if the quote is $0.
2. Apply the migration, store `FACTORY_REGISTRY_URL` and `FACTORY_REGISTRY_SERVICE_ROLE_KEY` as sensitive Vercel variables, redeploy, and verify persistence across separate invocations.
3. Confirm latest CI green, new Vercel deployment READY, stable alias target, `/health`, `/ready`, and authenticated `/v1/factory/export/:name` behavior.
4. Implement and test a real deployment adapter only after credentials and provider contract are available; do not fake a deploy by returning a plan.
5. Keep PR #45 open until review; no merge was performed.

## Free-provider policy hardening — 2026-10-17

- API Factory zero-cost eligibility now requires `officialSourceVerified=true`, an HTTPS provider-owned source, supported access/status enums, `hardStop=true`, and a source audit date no older than 30 days. It rejects known community discovery domains as the authoritative source.
- The COLLECTION-derived fixture entries for Gemini, Pollinations and Ollama are explicitly marked `official_source_verified=false` because their current source URLs point to OmniRoute, a community catalogue rather than the provider's own terms.
- The Google Gemini real-probe now refuses to send a provider request unless `GOOGLE_AI_STUDIO_BILLING_TIER=free` is explicitly set, in addition to requiring `GEMINI_TOKEN`. This is a safety gate, not independent proof of the account's billing tier.
- Official Google documentation distinguishes the free tier from paid tiers requiring linked billing; verify the actual project/key billing status before running a live request: https://ai.google.dev/gemini-api/docs/billing and https://ai.google.dev/gemini-api/docs/pricing.
- New direct regression tests cover community-source rejection, missing official-source attestation, invalid access classes, one-time promotions, stale source dates, and malformed dates. Latest API Factory Test run `38989207081` completed successfully.
