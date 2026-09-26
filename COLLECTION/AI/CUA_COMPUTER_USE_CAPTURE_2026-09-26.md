# Cua Computer-Use Capture — 2026-09-26

Source: trycua/cua
License: MIT for core Cua; third-party/optional components have separate licenses.
Status: VERIFIED_SOURCE_CAPTURED; NOT YET OPERATIONALLY INTEGRATED.

## What Cua adds
- Cua Driver: native desktop/browser inspection and interaction through MCP, CLI, Python and TypeScript SDKs.
- Cua sandbox/fleet runtime for isolated environments.
- Lume for local macOS/Linux VM lifecycle on Apple Silicon.
- Cua Bench for simulated tasks, evaluators and trajectory export.
- CUA-S1 specialized computer-use decision models.
- contract-first native/runtime SDK architecture.
- bounded permission modes and capability manifests.
- optional local computer history with metadata-only hydration.

## Direct leverage for AI Operating Operator / Elite
1. Add GUI as a first-class capability surface alongside GitHub/API/shell/browser.
2. Keep the same task contract and evidence ledger: observation -> authorization -> action -> observation -> independent verification.
3. Require a reviewed capability manifest for desktop operations.
4. Default to bounded permission mode; never use unrestricted/bypass modes in Operator production.
5. Treat screenshots, accessibility trees, clipboard content, window titles, URLs and app data as potentially sensitive/untrusted input.
6. Preserve observation/capture provenance for coordinate/pixel actions.
7. Preserve exact runtime identity/platform and Cua release/commit in evidence.
8. Require cleanup/teardown evidence for ephemeral desktops.
9. Use Cua Bench-style simulated evaluators before real desktop authority.
10. Keep GUI automation separate from API automation; use APIs when available.

## Future adapter
Capability IDs: platform.cua.driver, platform.cua.sandbox, platform.cua.bench.
Safe initial operations: health, list_apps, screenshot, inspect, verify_visible_result, cleanup. Click/type/run_command require explicit authorization and scoped runtime.
Forbidden by default: credential extraction, secret/clipboard harvesting, MFA/CAPTCHA bypass, account takeover, arbitrary host filesystem access, unrestricted network pivoting, payment authorization, disabling endpoint security, persistence outside the declared sandbox, and GUI use to bypass permission/RBAC boundaries.

## Verification
Every execution should record taskId/idempotencyKey, exact Cua revision, runtime OS/sandbox identity, permission mode and manifest hash, redacted action transcript, observation/result references, independent verifier result and cleanup status.
GUI success must never be inferred from an action acknowledgement alone; verify resulting application state independently.

## Cua Bench leverage
Build hermetic regression fixtures for deterministic app interaction, visible-result verification, cancellation/retry, stale-observation rejection, permission denial and cleanup-after-failure. No paid Cua Cloud is required for this test layer.

## License boundary
Core Cua is MIT. Kasm portions are MIT. OmniParser repository content is CC-BY-4.0. Optional cua-som/Ultralytics and the reviewed cua-perception path have AGPL-related obligations. Do not introduce those optional components into a distributable production path without separate dependency/license review.

## Project mapping
- AI Operating Operator: primary future adapter/capability.
- Elite/ARMY-14: GUI execution and verification patterns while preserving soldier isolation.
- EASY: future customer-visible GUI/browser verification when API evidence is insufficient.
- MONY: customer-facing tracking/link verification only through authorized environments.
- Salamou-31: optional GUI test harness for generated API/admin surfaces.
- ASTRA: research-only GUI test harness if needed; no live-money authority.

## Promotion gate
Do not claim Cua is active from source inspection. First create a hermetic fixture contract, then a read-only adapter, local/simulated test, independent verifier and cleanup test. Only after those pass should real desktop actions be exposed.