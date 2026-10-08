# LIVE HIGH-VALUE BOUNTIES — 2026-10-08

## Verified live candidates

### P0 — Tenstorrent #58986 — $1,000
FP32 ttnn.cumsum returns NaN after infinity/overflow. Open issue in official tt-metal repository. Acceptance criteria include regression tests and performance characterization on relevant architectures.
URL: https://github.com/tenstorrent/tt-metal/issues/58986
Why fit: Python/C++/tests/debugging; existing AI/engineering assets can assist analysis.
Risk: requires Tenstorrent environment/hardware validation and assignment before PR.

### P0 — Tenstorrent #51655 — $1,000
ttnn.typecast to uint16 rounds while other integer destinations and host path truncate. Official open issue with detailed reproduction and proposed root cause.
URL: https://github.com/tenstorrent/tt-metal/issues/51655
Why fit: deterministic bug, clear reproduction, focused kernel/test change.
Risk: low-level TTNN/SFPU knowledge and hardware validation required.

### P0 — Tenstorrent #59732 — $3,000
ttnn.sampling distribution bias from low-precision random threshold. Official open bounty; currently assigned to another contributor according to issue text. DO NOT pursue unless assignment becomes available.
URL: https://github.com/tenstorrent/tt-metal/issues/59732
Status: WATCH, not actionable now.

### P0 — Tenstorrent #56908 — $3,000
Distributed LayerNorm/RMSNorm 2D-core-grid row-stride corruption. Official open bounty. Engineering scope is substantial and hardware validation is required.
URL: https://github.com/tenstorrent/tt-metal/issues/56908
Status: WATCH/possible target after capability match.

### P1 — Tenstorrent #53787 — $5,000
ttnn.log_sigmoid fp32 error and missing branch. Official bounty. Scope is substantial and requires architecture/device validation.
URL: https://github.com/tenstorrent/tt-metal/issues/53787
Status: WATCH; high upside but higher technical barrier.

### P1 — Google OSS Patch Rewards
Official Google Patch Rewards program currently advertises $500, $2,000, $7,500 and $15,000 reward levels depending on security impact. This is a legitimate high-ticket route, but security expertise and strict scope are mandatory.
URL: https://bughunters.google.com/open-source-security/patch-rewards
Do not confuse this with Google's OSS VRP, which is paused for new product-vulnerability submissions as of Oct 1 2026.

## Important rejection
Do NOT use random aggregator-created bounty issues (for example bounty-plaza copies) as evidence of a payable opportunity. The source issue and official program terms must be verified.

## Tenstorrent payment gate
Official terms say:
- no fee/purchase required;
- contribution must address an open issue tagged bounty + difficulty;
- participant must be assigned on GitHub before submitting PR;
- payment follows an accepted/merged contribution;
- participant must independently satisfy legal eligibility and payment-information requirements;
- no delegation of payout to another person.
Reward chart: warmup $1–200, easy $201–500, medium $501–1,999, hard $2,000–3,000.

## Immediate strategy
1. Do not claim any bounty yet.
2. Rank only issues that are unassigned and technically compatible.
3. Prefer deterministic fixes (#51655 / #58986) over deep hardware/model bring-up.
4. Verify current assignment status immediately before any user action.
5. If a candidate requires a physical device unavailable to us, downgrade it.
6. User must personally perform identity/assignment/payment steps.
