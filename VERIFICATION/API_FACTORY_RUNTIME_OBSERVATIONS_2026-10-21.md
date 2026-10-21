# API Factory runtime observations — 2026-10-21

## Render preview
- Service: `salamou31-api-factory-preview`, URL: https://salamou31-api-factory-preview.onrender.com
- Render reports its latest deployment as `live`.
- Logs from 2026-10-20 20:00 UTC through 2026-10-21 20:45 UTC show the process starting with `node server.mjs` and listening on port 10000.
- A recorded `GET /health` returned HTTP 200 at 2026-10-20 20:00:30 UTC.
- A recorded `GET /` returned HTTP 404 at 2026-10-20 21:59:31 UTC. This is not necessarily an application failure because `/` is not a documented factory endpoint.
- No `/ready` request appears in the queried log window. Therefore current durable readiness is **not freshly verified** by this check.
- The free service logs include a process termination after idle time; this is consistent with a sleeping free service and means response latency/availability cannot be treated as always-on.

## Render main service
- Service: `salamou-31-api-factory`, URL: https://salamou-31-api-factory.onrender.com
- Render reports its latest deployment as `live`, but the queried time window returned no application logs.
- Existing documentation records a prior HTTP 503 `DURABLE_STORAGE_REQUIRED` response from this main endpoint. It remains blocked until an external `/ready` check passes after correct durable-storage configuration.

## Decision
- The preview is the best existing no-upfront-cost candidate, but do not advertise it as production-ready until `/ready` returns success with registry and artifact write/read verification and a harmless factory request succeeds.
- The current web/browser connectors could not perform that public HTTP request directly. TinyFish is available as an optional cloud-browser connection but is not connected yet.
- No service was redeployed or modified during these checks.
