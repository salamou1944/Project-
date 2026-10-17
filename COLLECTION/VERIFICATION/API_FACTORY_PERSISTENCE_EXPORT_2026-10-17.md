# API Factory Persistence and Export Hardening — 2026-10-17

Status: IMPLEMENTED_IN_SOURCE; CI_RECHECK_PENDING; DURABLE_BACKEND_NOT_CONFIGURED
Source repository: https://github.com/salamou1944/Salamou-31
Branch: `feat/api-factory-railway-deployable-2026-10-16`
Current source commit at record creation: `95ede6c3074f7fcfd23c38866e793c1b11be0f36`
Vercel project: `salamou31-api-factory`
Production deployment created from this source: `dpl_GYsFPaaL2PjQiARhnakjRDfYjkeS` (state was BUILDING when recorded)
Previous stable alias target at record time: `dpl_H4MVfPEXNmAzaeXAbbeGYf2XuGh3`; do not assume the new build has taken over until alias and live smoke are checked.

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
- A subsequent CI run failed because a test file contained a literal escaped newline. The test was corrected and its storage assertions were aligned with the new response shape. A new CI run is pending; do not mark the full suite green until the latest run completes successfully.
- Vercel health/readiness had passed earlier. The latest deployment must still be checked after build completion and alias reassignment.
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
