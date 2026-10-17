# API Factory — Vercel Runtime Smoke Evidence

Date: 2026-10-16
Status: VERIFIED_HEALTH_AND_READINESS_ONLY
Internal source: https://github.com/salamou1944/Salamou-31
Source branch: `feat/api-factory-railway-deployable-2026-10-16`
Source commit: `2052f524bda4d1ef73454baf8d0554fc61e31c99`
Vercel project: `salamou31-api-factory`
Deployment: `dpl_D6WQe46rwFPm7VKWQLHUA4fSMBt9`
Stable URL: https://salamou31-api-factory.vercel.app
Workflow evidence: https://github.com/salamou1944/Salamou-31/actions/runs/38942046871

## Verified

The GitHub Actions live-smoke job was rerun after the corrected deployment was assigned to the stable alias. Both requests returned HTTP success and the expected JSON contracts:

- `GET /health`: `{"ok":true,"service":"api-factory","version":"1.0.0","mode":"manifest-to-runnable-api"}`
- `GET /ready`: `{"ok":true,"ready":true,"checks":{"authentication":true}}`

Vercel reports the deployment as `READY`, with the stable alias assigned and no alias error. Readiness confirms that the `FACTORY_API_KEY` variable is configured; this record deliberately contains no secret value.

## Fixes applied

- `api/index.mjs` now exports an explicit Fastify serverless request handler and awaits `app.ready()`.
- Vercel defaults for generated artifacts and the API registry now use writable `/tmp` paths rather than the read-only deployment bundle.

## Important limits

- This is health/readiness proof, not full verification of every API Factory operation or a paid-provider completion.
- `/tmp` is ephemeral. Generated artifacts and registry data are not durable across cold starts or instance replacement. Do not treat the current deployment as production-complete for persistent API registrations.
- The Vercel GitHub integration is not connected to this project: a Git-source deployment attempt failed with `git_info_fail`. The working deployment was created from the exact source files in the recorded commit. Future code changes are not yet proven to auto-deploy.
- Railway remains unavailable for this service because the connected account's trial expired. No paid upgrade was made.
- Do not reuse the existing EASY Supabase database for API Factory state; keep project boundaries separate unless a dedicated, approved storage design is established.

## Next gates

1. Add a dedicated durable registry/artifact store without introducing a paid dependency or crossing EASY data boundaries.
2. Verify authenticated API Factory routes and generated-API execution end-to-end.
3. Establish a supported Git-linked deployment path or keep an explicit, repeatable manual deploy procedure.
4. Run the API Factory test suite against the current source commit; prior green test results predate these two deployment fixes.

## Follow-up correction — 2026-10-17

Source branch received an unmerged follow-up on 2026-10-17:

- Commit `e91bca60f50f8a200286247072e3c89f4e6d346d`: `/ready` now returns HTTP 503 with `DURABLE_STORAGE_REQUIRED` unless both registry and artifact stores report durable storage.
- Commit `97da17b5a39082826411e0803195359e8c3c3082`: integration test now asserts readiness fails closed when using local ephemeral storage.
- Commit `b0be17e29f35583b6f9c8b831fad36b52853459e`: README documents the required server-side storage configuration.

This is a source-level change only. It has **not** been deployed to the stable Vercel alias in this follow-up, and the current-source test suite has not yet been confirmed green. The older `GET /ready` success above is historical evidence for the earlier deployed revision, not proof that durable persistence exists. Render account inventory returned no existing web services, Postgres instances, or Key Value instances to reuse. No new resources were created, and the existing EASY database remains out of scope.

Next gate: configure an approved dedicated durable store, run the full current-source test suite, then deploy the exact reviewed commit and repeat authenticated build/register/export/inspect tests before calling the API Factory production-ready.
