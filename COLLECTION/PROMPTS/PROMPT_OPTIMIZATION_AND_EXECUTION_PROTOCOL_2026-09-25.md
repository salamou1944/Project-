# PROMPT OPTIMIZATION AND EXECUTION PROTOCOL — 2026-09-25

Status: ACTIVE / COLLECTION-INDEXED
Purpose: improve the prompts/instructions used in project execution and reduce unnecessary token, API, and reasoning overhead without weakening correctness.

## 1. Scope

Apply this protocol to:
- prompts/instructions used for EASY, MONY, ASTRA, Elite/ARMY-14, Salamou-31 and collection work;
- research prompts;
- coding/repair prompts;
- tool-routing prompts;
- verification/evidence prompts;
- user-facing execution instructions when a shorter, clearer formulation preserves the same intent.

Do not merge project-specific prompts across projects unless the reusable rule is explicitly proven to be generic.

## 2. Core optimization loop

CURRENT PROMPT
-> extract objective, constraints, evidence requirements, project boundary
-> remove duplication and non-operative prose
-> make execution order explicit
-> define failure states and stop conditions
-> define required evidence
-> run representative cases
-> compare against baseline
-> retain only changes with measured improvement
-> regression test
-> persist the winning prompt/version and evidence

A prompt is NOT considered improved merely because it is shorter or more sophisticated.

## 3. Evidence-first prompt contract

Important execution prompts should make these fields explicit when applicable:
- OBJECTIVE
- SCOPE
- DO-NOT-MIX boundaries
- AVAILABLE SOURCES
- EXECUTION REQUIRED (not report-only)
- FAILURE / BLOCKER semantics
- VERIFICATION requirements
- PERSISTENCE destination
- STOP/CONTINUE conditions
- FINAL RESPONSE contract

Required anti-false-success rule:
- never convert unavailable external capability into simulated success;
- distinguish code-complete, deployed, runtime-reachable, real-operation-success, and independently-verified states.

## 4. Optimization techniques captured

### GEPA / DSPy
GEPA performs reflective prompt optimization from examples plus a metric and can use textual feedback explaining failures. DSPy exposes GEPA and other optimizers including MIPROv2. This is a candidate for measured prompt optimization, not an automatic authority.

Sources:
- https://github.com/stanfordnlp/dspy
- https://github.com/gepa-ai/gepa

### Promptfoo
Promptfoo supports baseline evaluation, candidate generation from failures/scores, candidate evaluation, and validation splits through `promptfoo optimize`. Candidate for local prompt regression/optimization.

Source:
- https://github.com/promptfoo/promptfoo

### Meta Llama Prompt Ops
Prompt Ops is an open-source prompt optimization package focused on data-driven optimization for Llama models and supports local/provider configurations such as vLLM. Candidate for cost-reduced experimentation when its supported model path matches the task.

Source:
- https://github.com/meta-llama/prompt-ops

### Context/prompt compression
Collection already contains code2prompt evidence. code2prompt can generate structured codebase context, estimate token usage, and use templates/filters, which can reduce exploration round trips and unnecessary context transfer.

Source:
- https://github.com/mufeedvh/code2prompt

## 5. Project application

EASY:
- optimize Creative/repair instructions around Product DNA, Product Integrity, provider routing, and fail-closed behavior;
- reduce repeated context sent to providers.

MONY:
- keep business-state instructions deterministic and evidence-gated;
- do not optimize away required PartnerStack evidence.

ASTRA:
- keep trading/risk constraints explicit;
- prompt optimization must never weaken safety or verification boundaries.

Elite / ARMY-14:
- optimize stage-specific executor/verifier instructions;
- preserve state-machine evidence and independent verification.

Salamou-31:
- optimize provider-neutral API generation instructions;
- prefer structured outputs and reusable evaluation cases.

Collection:
- optimize research prompts for deduplication, source qualification, and project mapping.

## 6. $0 strategy

Prefer local/open-source optimization and evaluation first where practical.
Possible candidates:
- DSPy/GEPA
- Promptfoo
- Prompt Ops
- local/self-hosted inference through Ollama/LocalAI/vLLM
- GitHub Actions for repeatable regression where free quota/public-repository rules permit

Paid inference may be used only as an optional optimization/evaluation provider when no free/local route can establish the required evidence.

## 7. Operational rule for prompts sent during execution

Before issuing a substantial internal/project instruction:
1. Reuse already-known context instead of restating it.
2. Include only constraints that affect execution.
3. Specify what must actually be changed/tested.
4. Require evidence for completion.
5. Identify blockers precisely.
6. Search existing collection knowledge before new collection.
7. Search public GitHub when a capability gap remains.
8. Do not claim success from an unverified fallback.
9. Keep the final user-facing message concise and evidence-based.

## 8. Verification status

VERIFIED_EVIDENCE_CAPTURED:
- GEPA/DSPy reflective optimization documentation inspected.
- Promptfoo optimization documentation inspected.
- Meta Llama Prompt Ops repository inspected.
- Existing collection evidence for code2prompt inspected through Project- search.

NOT YET VERIFIED IN OUR PROJECTS:
- no optimizer has yet been integrated into a production project;
- no measured before/after benchmark exists for our project prompts;
- no claim is made that any candidate improves our actual workloads until a local regression set proves it.

## 9. Next implementation target

Build a small, local-first prompt regression corpus from real failure/success cases already present in project evidence. Use it to evaluate prompt changes before replacing active prompts. Keep the baseline and candidate outputs so regressions are detectable.

