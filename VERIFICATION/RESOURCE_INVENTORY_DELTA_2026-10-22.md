# Resource inventory delta — 2026-10-22

This addendum records fresh read-only checks after the main inventory was created. No secrets were read, no messages sent, no paid resources activated, and no deployments or Collection harvest cycles were triggered.

## Newly checked account resources

- **GitHub:** authenticated login `salamou1944`; owner-scoped repository query returned 10 repositories (9 public, 1 private). The separate known organization repository `Sssssssddddd/.github` is not included in that owner-only count.
- **GitLab:** one private project, `salamou1944-group/Salamou1944-project`, with `empty_repo: true`. It has no source code to reuse yet.
- **Shopify:** `My Store`, Algeria, DZD, CET, plan `trial`. Exact warning from the connected account: **Plan: trial — you'll need to upgrade before you can start selling and unlock full features**. No upgrade was made.
- **Figma:** Starter plan, View seat; Code Layers and Specs disabled.
- **Higgsfield:** authenticated profile resolves. Project inventory was not completed because the list operation requires an explicit workspace ID. Existing inventory reports Free plan, 10 credits, and a pending eligible trial; no trial was started and no credits were spent.
- **BetterMenu:** saved-recipe query returned zero recipes.
- **Metricool:** one brand linked to a YouTube channel ID; this does not prove published content or revenue.
- **AgentMail:** one selected organization and three inboxes. Earlier thread review found delivery-failure/bounce notifications in both outreach inboxes and no customer reply evidence.
- **Apollo:** current profile shows 80 lead credits, 5,000 AI credits, and zero export credits. One profile endpoint reports 160 direct-dial credits remaining while a separate usage endpoint previously reported 80. Direct-dial balance remains conflicted and should not be relied on until reconciled.
- **Upwork:** one Freelancer/Talent account; previous profile check showed zero Connects and private visibility.
- **Wix:** current site listing returned zero sites.
- **Automations:** five jobs. `Revenue + leverage sweep` is enabled, but `next_run_time` is null; next execution is not proven. Four other jobs are disabled. No schedules were changed.
- **Vercel runtime check:** attempts to fetch `/health` and `/ready` from recent READY deployment URLs were blocked by the connector safety layer before any request was sent. This is not an HTTP failure and does not establish endpoint health.

## Current gates

### COLLECTION

Cycle 28 remains the latest verified successful harvest: 68 refreshed, 32 blocked attempts preserved, 5,746 extracted artifacts / 5,778 source rows, 17,834 deferred. JSON audit: 13,738 files, zero parse failures, 1,011,256,549 bytes. Install gate remains `NO_APPROVED_CANDIDATES`.

Do **not** trigger cycle 29 yet. `READY.json` is 89,789,053 bytes against a 95,000,000-byte guard. The isolated JSON shard round-trip/hash/baseline test passed on [run 39678755963](https://github.com/salamou1944/Project-/actions/runs/39678755963), but the helper is on `feat/collection-json-shards-2026-10-22`, not `main`, and production readers/writers have not been migrated end-to-end.

### API Factory

- Supabase project `salamou-31-api-factory` reports ACTIVE_HEALTHY; `public.api_factory_registry` exists with RLS enabled and one row; Edge Function `api-factory-storage` v3 is ACTIVE.
- Vercel has READY production and staging deployment objects, but external `/ready` is unverified; the direct checks were blocked before request.
- Railway has five services across two projects; latest recorded deployments are FAILED and no volumes are attached. API Factory is inside EASY Runtime Production; do not redeploy there.
- Railway token smoke failed with Unauthorized on [run 39679784463](https://github.com/salamou1944/Salamou-31/actions/runs/39679784463). Secure owner-controlled rotation is required.
- API Factory test passed on [run 39679784439](https://github.com/salamou1944/Salamou-31/actions/runs/39679784439); SOAT integration smoke passed on [run 39679784500](https://github.com/salamou1944/Salamou-31/actions/runs/39679784500); provider contract passed on [run 39679784660](https://github.com/salamou1944/Salamou-31/actions/runs/39679784660). These are CI evidence, not production inference proof.

### Free inference / local execution

- ChatGPT/Codex plan access is not a general OpenAI API key or unrestricted production inference quota.
- OmniRoute + Codex App-Server remains a source-verified candidate only. Termalin reports zero reachable hosts and the local bridge inventory workflow [39519079143](https://github.com/salamou1944/local-bridge./actions/runs/39519079143) remains queued; no private persistent execution host is proven.
- Pollinations Classic remains source-reviewed but not live-verified. Do not send sensitive data or enable automatic routing.
- Google AI Studio, Groq, OpenRouter and other provider probes remain fail-closed until the exact account/model free tier is confirmed; no paid fallback.

## Next execution order

1. Keep Collection paused.
2. Integrate shard read/write support into every producer, validator, installer, and reader; prove semantic equality, stable ordering, counts, hashes, recovery behavior, and size limits against current state before merge.
3. Verify the API Factory Supabase gateway auth and real storage read/write-back, then external readiness on an isolated runtime. Keep Railway unchanged until secure token rotation and an isolated target are available.
4. Resolve AgentMail delivery failures and Apollo direct-dial discrepancy before further outreach or credit use.
5. Repair/verify the enabled automation's null next-run after its scheduling mechanism is understood.
