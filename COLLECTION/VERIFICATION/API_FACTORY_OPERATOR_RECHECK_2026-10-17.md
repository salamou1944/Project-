# API Factory Operator Recheck — 2026-10-17

Status: VERIFIED_BLOCKED_ON_EXTERNAL_CONFIGURATION_AND_VERCEL_SCOPE

## Scope and safety
- Read-only recheck of GitHub Actions, Vercel deployment inventory, Supabase project inventory, Railway projects, and the existing API Factory evidence.
- No deployment was triggered, no secrets were retrieved, no paid resources were created, and no EASY resource was modified.

## Confirmed GitHub state
- PR: https://github.com/salamou1944/Salamou-31/pull/45
- PR #45 remains open and unmerged; head SHA: `eb7ed406f0da6831d0893208cb0b0264a117ba4b`.
- API Factory Test run `38995133913` completed successfully.
- Free Resource Operator run `38995133912` completed successfully.
- API Factory Vercel Smoke run `38995133899` (run #44) failed at the readiness contract step; the health check passed.

## Exact live-smoke failure
The run log observed `GET /ready` returning HTTP 200 with:
- `ready: true`, `ok: true`, `degraded: true`
- `checks.registryPersistence: false`
- `checks.artifactPersistence: false`
- `storage.registryMode: ephemeral-file`
- `storage.artifactMode: ephemeral-file`
- `storage.durable: false`

The stricter smoke test correctly rejects this response. Do not weaken the assertion. The production alias is still serving an older/degraded readiness contract rather than the fail-closed `DURABLE_STORAGE_REQUIRED` response.

## Deployment inventory
- Vercel project inventory returns `salamou31-api-factory`.
- Latest listed READY production deployment: `dpl_4vmQMfn4hr5SahXSJxf1ruh8pbYs`, source commit `35b462ff3137605f00c98383a8598b49610cd963`.
- PR head `eb7ed406f0da6831d0893208cb0b0264a117ba4b` is newer/different from the source SHA reported for that deployment; this is not proof the latest fail-closed source is live.
- Vercel project detail, alias inventory, and authenticated deployment fetch were denied with HTTP 403 for scope `bleu5`. Do not retry the same calls unchanged or claim alias reassignment was verified.

## Storage and platform boundary
- Supabase inventory exposes only `easy-platform-db`; it belongs to EASY and is explicitly out of scope for API Factory.
- Railway inventory exposes only `EASY Runtime Production` and `EASY Developer Platform`; no separate API Factory project was found.
- Existing evidence records Railway trial unavailability and no dedicated durable store. No new service or paid plan was created.
- A separate approved Supabase project, its migration, and server-side sensitive variables are still required before durable registry/artifact persistence can be activated. Creating a project requires the user's explicit organization choice and a cost quote/confirmation.

## Next safe actions
1. Resolve Vercel authorization for the actual project/team scope, then deploy the reviewed fail-closed source and verify the stable alias.
2. After the user explicitly chooses the Supabase organization, obtain the project cost quote; create only if confirmed at $0 and clearly separate from EASY.
3. Apply the API Factory migration and set the service-role key only as a sensitive server-side variable; never paste or commit it.
4. Re-run the live smoke test and verify persistence across separate invocations before calling the service production-ready.
5. Keep PR #45 open until its review and deployment gates are resolved.

## Source evidence
- PR #45: https://github.com/salamou1944/Salamou-31/pull/45
- Live-smoke run #44: https://github.com/salamou1944/Salamou-31/actions/runs/38995133899
- API Factory Test run: https://github.com/salamou1944/Salamou-31/actions/runs/38995133913
- Free Resource Operator run: https://github.com/salamou1944/Salamou-31/actions/runs/38995133912
- Existing persistence evidence: https://github.com/salamou1944/Project-/blob/main/COLLECTION/VERIFICATION/API_FACTORY_PERSISTENCE_EXPORT_2026-10-17.md
