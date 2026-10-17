# Account-wide source capture — varun29ankuS — 2026-10-17

Status: OWNER_ENUMERATION_COMPLETE; MEMORY/RAG SOURCES_TRIAGED; DEEP_SWEEP_OPEN
Owner: https://github.com/varun29ankuS
Enumeration method: GitHub owner-scoped repository search `user:varun29ankuS`, page 1 returned 27 public repositories and page 2 returned 0 on 2026-10-17.
Trigger: downstream upstream reference from `doobidoo/shodh-cloudflare` and `doobidoo/mcp-memory-service`.
Scope limit: README-level review of priority memory/RAG/database/catalog repositories, not a full source-tree audit of all 27 repositories.

## Enumerated public repositories

1. https://github.com/varun29ankuS/shodh-memory
2. https://github.com/varun29ankuS/shodhRAG
3. https://github.com/varun29ankuS/shodh-redb
4. https://github.com/varun29ankuS/Roshera-CAD
5. https://github.com/varun29ankuS/mif-spec
6. https://github.com/varun29ankuS/Vayu
7. https://github.com/varun29ankuS/navier-stokes-solution-search
8. https://github.com/varun29ankuS/bolt
9. https://github.com/varun29ankuS/Saryu-RNN
10. https://github.com/varun29ankuS/awesome-ai-memory
11. https://github.com/varun29ankuS/Complete-Python-3-Bootcamp
12. https://github.com/varun29ankuS/birdy
13. https://github.com/varun29ankuS/varun29ankuS
14. https://github.com/varun29ankuS/awesome-mcp-servers
15. https://github.com/varun29ankuS/homebrew-shodh-memory
16. https://github.com/varun29ankuS/skills
17. https://github.com/varun29ankuS/rasayan
18. https://github.com/varun29ankuS/rocksdb
19. https://github.com/varun29ankuS/ezpz
20. https://github.com/varun29ankuS/sentiment-dashboard
21. https://github.com/varun29ankuS/openai-agents-python
22. https://github.com/varun29ankuS/openai-cookbook
23. https://github.com/varun29ankuS/robo-news
24. https://github.com/varun29ankuS/shodh-website
25. https://github.com/varun29ankuS/modelcontextprotocol
26. https://github.com/varun29ankuS/ankita-pubsub
27. https://github.com/varun29ankuS/shodh-memory-website

## Priority findings

### P1 — shodh-memory

- Source: https://github.com/varun29ankuS/shodh-memory
- README advertises Apache-2.0, local-first persistent cognitive memory, MCP/HTTP interfaces, a single-binary deployment path, and no required LLM/API key/external database for core memory operations.
- Potential value: a local $0 memory backend for ASTRA/AI Operating Memory, avoiding a managed vector database and paid embedding calls.
- Before adoption, inspect current release/CI, default bind address, API authentication for remote use, backup/restore, memory deletion semantics, upgrade compatibility and performance evidence. README benchmark claims are maintainer claims, not independent measurements.
- The README points to a separate Cloudflare implementation, `doobidoo/shodh-cloudflare`; that version has different operational/storage assumptions.

### P1 — shodhRAG

- Source: https://github.com/varun29ankuS/shodhRAG
- README describes a local-first RAG/knowledge-base desktop application with hybrid dense-vector + BM25 retrieval, local ONNX embeddings, knowledge graph support, encrypted local DB and an audit log.
- User documents and query content sent to a configured cloud LLM are provider-dependent; local model mode is the privacy-preserving path.
- Potential value: reference implementation for document ingestion and evidence-grounded retrieval, not a direct replacement for API Factory or the memory server.
- Gate: README separates “what works today” from “in progress”; audit current tests and status before treating every listed capability as available.

### P2 — shodh-redb

- Source: https://github.com/varun29ankuS/shodh-redb
- README declares Apache-2.0 and describes an embedded Rust database with KV, vector search, blob storage, TTL, CDC and transactional file semantics.
- Best fit: a future embedded Rust/edge workload. It is not a hosted database or a drop-in Node.js persistence layer for current API Factory.
- No dependency added; benchmark only if a Rust service becomes a concrete requirement.

### P2 — awesome-ai-memory

- Source: https://github.com/varun29ankuS/awesome-ai-memory
- Curated index of memory tools and storage architectures. Useful for discovering canonical upstream owners and comparing graph/vector/hybrid approaches; it is not runtime infrastructure.
- Use as a discovery map and deduplicate entries against the existing COLLECTION account graph.

### P3 — skills / awesome-mcp-servers

- Sources: https://github.com/varun29ankuS/skills and https://github.com/varun29ankuS/awesome-mcp-servers
- The skills repo describes mixed licensing: many skills Apache-2.0, while some document-editing skills are source-available and explicitly not open source. Verify the license of each individual folder before reuse.
- awesome-mcp-servers is a discovery catalogue, not an assurance that every listed server is safe, maintained or production-ready.

## Other account notes

- `shodh-memory` references downstream `doobidoo/shodh-cloudflare`; this was the discovery path, not evidence that a Cloudflare deployment already exists.
- `shodhRAG` is a distinct application, not the same product as the core `shodh-memory` backend.
- `shodh-redb` is a distinct database library; do not confuse it with the memory server or assume API compatibility.
- The remaining enumerated repositories include CAD/engineering, CFD, RNN, OpenAI SDK/cookbook forks, and assorted examples; not yet deep-audited for this workstream.

## Reuse decision

- **First benchmark:** core `shodh-memory` against current ASTRA memory requirements using local-only mode and synthetic/non-sensitive test data.
- **Second benchmark:** SHODH on Cloudflare only if the existing Cloudflare account and free-tier limits are confirmed.
- **Do not replace API Factory storage with shodh-redb** unless a Rust embedded service is deliberately introduced.
- No code imported, no services deployed, and no secrets copied during this pass.

## Remaining work

1. Audit core `shodh-memory` authentication, backup/restore, deletion, and migration behavior from source and tests.
2. Compare its MCP/REST contract with existing AI Operating Memory and agent-skills patterns.
3. Continue recursive owner expansion from the catalog and all 27 repositories.
4. Keep deep sweep open until source-level review and downstream-owner capture are complete.
