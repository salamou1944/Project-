# ACCOUNT → FULL REPOSITORY EXPANSION RULE

Status: ACTIVE / PERMANENT COLLECTION RULE
Effective: 2026-10-04

## Purpose

Every daily collection run must expand from a discovered repository to its owning GitHub account/organization and inspect the account's complete public repository set so that discovery does not stop at the entry repository.

## Mandatory execution rule

Whenever a repository is discovered, captured, or supplied:

1. Resolve its GitHub owner account/organization.
2. Treat that owner as a permanent collection source.
3. Enumerate ALL public repositories belonging to that owner, not only pinned, popular, recently updated, or first-page repositories.
4. Preserve every distinct repository discovered, including repositories already captured in earlier runs.
5. For each newly relevant repository, inspect the README/docs and repository metadata; inspect releases/tags/branches, workflows/actions, issues/PRs, and linked external sources when they contain material relevant to collection.
6. Extract downstream tools, APIs, MCP servers, libraries, templates, datasets, workflows, providers, and other source accounts referenced by those repositories.
7. Add newly discovered source accounts to the same expansion queue.
8. Continue expansion through the resulting source graph until the current collection run reaches its available execution boundary; never declare the graph complete merely because the entry repository was inspected.

## Evidence and provenance

For every account/repository capture preserve, when available:

- owner/account
- repository name and canonical URL
- discovery path (which repository/account led to it)
- revision/date inspected
- license
- dependencies and runtime/deployment requirements
- paid/cloud/external dependencies
- security and operational limitations
- maintenance/archive state
- relevant verification status
- potential subscription-cancellation or revenue leverage

Discovery does not equal verification. Stars are never quality evidence.

## Historical preservation

Repeated discovery is not deletion or deduplication. Existing captures remain historical evidence. New captures should record the new observation/revision and its provenance.

## Daily-run requirement

This rule is part of the daily collection process and applies to:

- daily web/GitHub discovery
- permanent source accounts
- weekly Top Five
- Top 10 / queue work
- user-supplied repositories
- repositories found inside COLLECTION itself
- repositories discovered through linked sources

The operational target is:

REPOSITORY → OWNER ACCOUNT → ALL PUBLIC REPOSITORIES → RELEVANT CONTENT → NEW SOURCES/ACCOUNTS → REPEAT

The objective is zero missed repositories caused by stopping at a single repository.

## Account-first targeting rule

When a GitHub account or organization is explicitly targeted, the **account itself is the collection unit**. Do not target or scope the collection to one repository merely because that repository is the initial lead.

The required sequence is:

ACCOUNT TARGET → ALL PUBLIC REPOSITORIES → ALL RELEVANT CONTENT/SOURCES → NEW ACCOUNTS → REPEAT

A repository may be the entry point for discovery, but once its owner is identified, the complete public account repository set becomes in-scope for that collection run. This applies equally to user-supplied accounts, permanently monitored accounts, weekly selections, and accounts discovered through other repositories.
