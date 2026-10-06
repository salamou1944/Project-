# Reticle reusable verification patterns

Source: https://github.com/reticlehq/reticle
Status: CANDIDATE_FOR_DEDUPE_AND_UPGRADE

## Skills/capabilities to extract

### 1. Runtime Proof Verdict
Contract: a completion claim is valid only when a real running target produced sufficient evidence for the asserted condition.
Verdicts: PASS, FAIL, UNKNOWN.
Rule: UNKNOWN is never treated as PASS.

### 2. Look-Act-Observe-Assert
Reusable agent execution pattern:
1. inspect current runtime state;
2. perform the smallest required action;
3. observe structured runtime events;
4. assert explicit predicates;
5. return verdict + evidence.

### 3. First-Divergence Diagnosis
When a verification predicate fails, identify the earliest contradictory event/state and attach the most actionable source location available.

### 4. Replayable Verification Flow
Convert a verified journey into a deterministic replay/regression guard that can run without an LLM in the verification loop.

### 5. Evidence Surface Contract
Prefer structured runtime evidence (network, state, console, DOM, routing and framework signals) over screenshots as proof of application behavior.

## Integration target

Compare these contracts against existing agent-skills, SOAT, Elite/ARMY-14 and AI Operating Memory. Create a new standalone skill only if semantic dedupe shows a genuinely missing contract; otherwise upgrade the existing skill.

## Non-goals

- Do not clone Reticle wholesale.
- Do not treat repository discovery or README claims as production proof.
- Do not replace existing SOAT/evidence infrastructure merely because Reticle implements a similar concept.
