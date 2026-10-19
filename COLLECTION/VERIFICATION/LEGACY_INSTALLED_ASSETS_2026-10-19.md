# Legacy installed asset — Hyperswitch — 2026-10-19

## Preserved state

- Repository: [juspay/hyperswitch](https://github.com/juspay/hyperswitch)
- Pinned revision: `1d71d94d2e2e1c72f3ede13abebc24132997685f`
- License: Apache-2.0
- Prior source record: [JUSPAY_HYPERSWITCH_2026-10-08.md](../SOURCES/JUSPAY_HYPERSWITCH_2026-10-08.md)
- Prior installation report recorded `ALREADY_INSTALLED` at `COLLECTION/INSTALLED/juspay__hyperswitch`.

## Boundary

- Preserve the existing source directory; do not delete or rebuild it as part of the install-policy hardening.
- The source install is **not** proof of a configured payment provider, working merchant account, billing integration, runtime health, or revenue.
- No runtime/callable promotion is granted. Hyperswitch must stay a source asset until an explicit integration approval, security gate, provider configuration, test transaction, and payout/settlement evidence exist.
- The new installer no longer auto-selects legacy source notes or deep-extraction packets. Any future installation must be present in the canonical value queue with `promotion_action=INSTALL_APPROVED`, `install_approval=APPROVED`, `integration_gate=PASS`, and `security_gate=PASS`.
- The historical installation report remains in Git history; the current Collection run may report `NO_APPROVED_CANDIDATES` without deleting this preserved directory.
