# Railway runtime triage — 2026-10-21

This is a log-backed diagnosis of the five services in the two existing Railway projects. The environment status query currently reports all five services offline, no active deployments, and no attached volumes. The failure messages below are from the latest deployment records exposed by the connector (dated October 4–6); they explain the last recorded failures, but do not prove they are the sole cause of today's offline state.

## EASY Runtime Production

- **salamou31-api-factory** — latest recorded deployment `5236f680-fe02-472e-a813-45a5374445ea` failed at `BUILD_IMAGE`. Railpack reported that it could not determine how to build the app and that `start.sh` was not found. Recorded service configuration uses the `AI-API-HUB/api-factory` root and `npm start`, while the builder is Railpack. This is a builder/configuration mismatch candidate, not a successful deploy. Service is in the EASY production project, so do not change it or redeploy there without an isolated plan.
- **easy-runtime-current** — deployment `e944fa9a-4e08-4d76-9548-56c4e49433e6` failed at `BUILD_IMAGE`: Railway could not find `Dockerfile.easy-runtime` in the code archive. Recorded source is `salamou1944/Easy-`, branch `main`. The source root / Dockerfile path must be reconciled before any future deploy.
- **easy-runtime** — deployment `a0027e31-b5d6-4660-949f-8d42c855b9ae` failed at `HEALTHCHECK`; `/health` returned service unavailable until the replica was marked unhealthy. This is a runtime/startup or health-contract failure, not a build success.

## EASY Developer Platform

- **easy-platform-runtime-v3** — deployment `d835e386-1fea-49e8-8dfd-a966cc07cee2` failed at `BUILD_IMAGE`. The current log slice exposes only the build start, so the exact compiler/build error is not proven. Recorded configuration uses `Dockerfile.easy-runtime` and `node apps/easy-developer-platform/runtime.mjs`; inspect the complete build log before changing anything.
- **soat-production-runtime** — deployment `d7349dc9-3162-4aec-a8a3-c369af29e9d5` failed at `HEALTHCHECK`: `/health` stayed unavailable for the five-minute retry window and the replica never became healthy.

## Decision

1. Treat Railway as **unavailable** for production use until a current deployment is built, running, and passes its service health contract.
2. Do not attempt quick fixes on the existing EASY production services. The API Factory Railway service has no attached volume and the production environment has no shared variables; the developer environment exposes one shared-variable name, but no value was read.
3. Use the existing Render Free preview plus dedicated Supabase gateway as the leading zero-upfront-cost API Factory candidate, pending a fresh external `/ready` smoke.
4. For a future Railway target, first choose an isolated project/environment, configure the correct Docker builder/root path, confirm required variables are present without exposing values, and prove health + durable readiness before routing traffic.
5. Preserve logs and failed deployments as evidence; do not treat a green GitHub token-access smoke as proof that Railway has deployed or is serving the app.
