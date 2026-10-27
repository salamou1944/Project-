# Asset review: mnfst/modelparams.dev

Review target: `mnfst/modelparams.dev` at immutable commit `0d09d9a3fb642770430fb357e3c72f8e7d9f1f67`.

Proposed use: static, zero-runtime-dependency catalog and validator for provider-specific LLM request parameters. API Factory integration is opt-in via `provider.modelParamsId`; it validates parameter keys, ranges, enums, and applicability before provider network I/O. It does not make provider calls, provide credentials, or imply production provider availability.

## Preliminary source review

- Root license: MIT.
- Published package: `modelparams@0.0.72`, MIT, with no runtime dependencies.
- Scope: TypeScript catalog, parameter definitions, model resolution, and deterministic validation.
- Upstream repo has other website/build components; Collection installation is a pinned source archive, and its installer does not run source lifecycle scripts.
- The integration test on Salamou-31's API Factory PR passed, including rejection of unsupported parameter keys before network I/O. CI evidence: https://github.com/salamou1944/Salamou-31/actions/runs/40442961304
- The package is not considered approved for Collection installation until the pinned-source review workflow passes all tests, build, dependency audit, and source-boundary checks. A passing review still does not imply a live provider works.

## Gate status

- Integration: PASS — [API Factory test on merged commit e3981dd](https://github.com/salamou1944/Salamou-31/actions/runs/40443294502) and [external smoke](https://github.com/salamou1944/Salamou-31/actions/runs/40443294594) succeeded.
- Security: PASS — [pinned-source review workflow](https://github.com/salamou1944/Project-/actions/runs/40443521733) verified the exact SHA, MIT/version/dependency boundary, package tests/build, production dependency audit, and runtime-source boundary scan.
- Install approval: proposed for the exact revision in [PR #56](https://github.com/salamou1944/Project-/pull/56). The source remains uninstalled until the approval merges and the Collection cycle verifies the current manifest row matches the exact revision.
