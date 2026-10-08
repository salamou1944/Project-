# MiroFish Scenario Simulation Skill

Status: ADAPTABLE / REFERENCE
Source: https://github.com/oneseanlee/MiroFish
License boundary: AGPL-3.0; source reuse requires license review.

## Purpose
Use multi-agent scenario simulation to rehearse decisions before committing scarce money, credentials, paid APIs or customer-facing changes.

## Contract
INPUT
- scenario_seed: verified source material/context
- decision_question: exact decision to rehearse
- actors: relevant stakeholder/persona classes
- constraints: budget, time, channel, operational limits
- horizon: simulation period
- success_metrics: measurable outcomes

PROCESS
1. Build a scenario graph from the seed.
2. Define distinct actor personas and incentives.
3. Run multiple interaction rounds.
4. Compare recurring outcomes and divergence.
5. Separate simulation observations from factual evidence.
6. Convert robust patterns into a testable real-world experiment.

OUTPUT
- scenario assumptions
- actor set
- simulated outcomes
- recurring patterns
- divergent outcomes
- risks/failure modes
- experiment recommendations
- confidence limited to simulation evidence

## Non-negotiable gates
- Never present simulation output as guaranteed prediction.
- Never replace production smoke/E2E evidence with simulation.
- Never spend money solely because a simulation looks favorable.
- Preserve source provenance and license boundary.
- Dedupe against existing SOAT/ASTRA/agent-skills capabilities before implementing a new runtime.

## Immediate operating use
Prioritize revenue experiments, prospect outreach, pricing/offer design, PASTEL customer/operations scenarios, and EASY market-response scenarios where simulation can reduce wasted execution cycles.
