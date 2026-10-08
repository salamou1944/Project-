# Callable Capability Gate

## Purpose

Collection is not complete when a capability is merely discovered, preserved, or extracted.
A valuable capability becomes operationally complete only when it is represented in our repository
and has a deterministic on-demand invocation boundary.

## Lifecycle

DISCOVERED → PRESERVED → EXTRACTED → DEDUPED → ADAPTED → STORED → REGISTERED → CALLABLE_ON_DEMAND → PROVEN_CALLABLE

## Red-line rules

- Do not duplicate an existing capability, adapter, Skill, or runtime contract.
- Preserve source provenance, revision, license, dependencies, and limitations.
- Never store credential values in the registry.
- A registry entry is not callable merely because it has a source URL.
- A capability cannot be marked PROVEN_CALLABLE without execution evidence.
- External projects are not wholesale copied. Extract the narrow reusable contract into the appropriate existing repository.
- If the capability is already implemented elsewhere in our estate, upgrade/link the existing implementation instead of creating a parallel one.

## Required callable record

Each entry in `COLLECTION/MASTER/CALLABLE-REGISTRY.json` must contain:

- `capability_id`
- `name`
- `kind`
- `source` (repository, revision, license)
- `our_location` (repository and path)
- `entrypoint`
- `invocation`
- `dependencies`
- `secret_refs` (names only)
- `status`
- `evidence`

Allowed status values:

- `REGISTERED`
- `CALLABLE_ON_DEMAND`
- `PROVEN_CALLABLE`
- `BLOCKED`

## Fail-closed rule

Missing repository/path, entrypoint, invocation, or execution evidence prevents promotion to
`CALLABLE_ON_DEMAND` / `PROVEN_CALLABLE`.

The registry is an index and contract boundary; it does not replace the actual implementation.
