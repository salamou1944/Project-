# API Factory Deployment Recovery — 2026-10-17

## New actions performed
- Added a preview-only recovery workflow in Salamou-31 at `.github/workflows/api-factory-vercel-preview-recovery.yml`.
- Commit: `9717b6a9a999c59c2fd58614917b7a5e831918b3`.
- Workflow run: https://github.com/salamou1944/Salamou-31/actions/runs/38998183053
- The workflow ran safely and confirmed that the GitHub Actions secret `VERCEL_TOKEN` is absent. All deployment steps were skipped; no secret value was accessed or printed and no production deployment was attempted.
- This provides a repeatable, non-production deployment path once a valid token is stored in GitHub Actions secrets.

## Deepened Vercel diagnosis
- Project inventory and production deployment listing are readable.
- Project details, environment inventory, deployment inspection, access-bypass URL creation, and preview deployment creation all fail with HTTP 403 for Vercel scope `bleu5`.
- Vercel team inventory returns no teams for the currently authenticated connector, despite the existing project being associated with team ID `team_nVzQIdLrINspss25nTtCXR5r`.
- Repeating the calls with either team ID or slug does not resolve authorization. This is a connector/account-scope mismatch, not an application-code failure.
- Official Vercel documentation identifies team membership and project roles as the access boundary for project/deployment operations: https://vercel.com/docs/rbac/access-roles

## Confirmed live-runtime mismatch
- The current stable deployment is READY but sourced from commit `35b462ff3137605f00c98383a8598b49610cd963`, not the reviewed PR head.
- Live smoke run #44: https://github.com/salamou1944/Salamou-31/actions/runs/38995133899
- It fails because `/ready` returns HTTP 200 with `ready=true`, `degraded=true`, and `storage.durable=false`. The reviewed branch's readiness implementation returns a fail-closed 503 with `DURABLE_STORAGE_REQUIRED` when durable persistence is absent. Keep the strict assertion; do not make ephemeral storage look production-ready.

## Durable-storage options checked
- Supabase account inventory has one organization, `salamou1944@gmail.com's Org`, on the Free plan, and one project `easy-platform-db` owned by EASY. That project is strictly out of scope.
- Railway account inventory has only EASY services and the Railway trial is unavailable; no API Factory service was created.
- Render's service inventory requires an explicitly selected workspace before reading services. No workspace or service was created.
- Composio discovery found no active Cloudflare, Neon, or Turso connection. These are not presently usable without an external authorization flow.
- No new resource was created and no paid service was activated.

## Remaining external authorization required
1. A valid Vercel credential with access to the existing `bleu5` project scope must be authorized through the Vercel dashboard and stored as GitHub Actions secret `VERCEL_TOKEN`; never paste it into chat. The new workflow can then deploy a preview and verify readiness without changing production.
2. Durable persistence needs a separate Salamou-31 database. The only Supabase organization found is `salamou1944@gmail.com's Org`; its project creation quote must be checked and any nonzero cost approved before creation. Do not reuse EASY's database.

## Safety
No production alias was changed, no existing data was deleted, no secrets were printed, no paid resources were created, and no EASY resources were modified.
