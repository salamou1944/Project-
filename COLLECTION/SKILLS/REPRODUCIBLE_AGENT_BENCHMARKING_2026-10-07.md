# Reproducible Agent Benchmarking — 2026-10-07

Status: EXTRACTED / MERGE-UPGRADE CANDIDATE

Source:
- https://github.com/the-open-agent/agentbench
- Revision evidence: README inspected on 2026-10-07
- License: Apache-2.0

## Contract
Evaluate an agent/runtime through repeatable suites instead of a single success example.

### Benchmark dimensions
- baseline performance
- dialogue/output correctness
- long-horizon tasks
- tool invocation and evidence completeness
- startup/health latency
- memory/context stability
- concurrent throughput
- repeated-run reliability

### Run model
- fixed dataset
- explicit rounds
- bounded retries
- timeout
- deterministic validation rules
- machine-readable per-run records
- aggregated summary
- human-readable report

### Evidence quality
Record:
- success rate
- latency mean/std/worst
- token consumption where available
- top failure reasons
- tool-call/evidence completeness
- confidence interval for aggregate results
- exact dataset and runtime configuration

### Merge decision
Upgrade the existing SOAT/evaluation contract with statistical confidence, repeated-run reliability and load/throughput dimensions. Do not create a parallel evaluator.
