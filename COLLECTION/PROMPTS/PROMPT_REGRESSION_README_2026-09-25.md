# Prompt Regression — 2026-09-25

Status: CORPUS_READY_NOT_MODEL_BENCHMARKED

## What was executed

A regression corpus was built from observed repair/verification evidence only. It contains eight real failure/fix cases spanning Astra-, EASY, agent-skills, AI_operating_memory, and Project-.

## Safety boundary

This corpus does not invent successful model outputs. It distinguishes source/code evidence from runtime evidence and records where runtime verification was still pending.

## Deterministic contract

The runner checks whether an execution prompt explicitly carries the operational contract:
- OBJECTIVE
- SCOPE
- DO-NOT-MIX
- AVAILABLE EVIDENCE
- EXECUTION
- FAILURE SEMANTICS
- VERIFICATION
- PERSISTENCE
- STOP / CONTINUE

It also checks evidence preservation, project isolation, failure handling, duplicate avoidance, tool routing, and continuation semantics.

## Baseline vs candidate

A deterministic contract check is now available, but a genuine baseline-vs-candidate model benchmark is not yet claimed. The next measured step is to run the same corpus with:
1. the current baseline prompt;
2. a candidate optimized prompt;
3. identical task inputs;
4. local/free model execution where available;
5. preserved outputs and per-case metrics.

A candidate must not replace the baseline merely because it is shorter.

## Source boundary

Primary source evidence is stored in the collection repository. Project runtime/implementation evidence remains in its owning project repository and is referenced, not copied as project state.
