# AI Engineering from Scratch — Collection Capture — 2026-09-26

Status: VERIFIED_SOURCE_CAPTURED
Source: https://github.com/rohitg00/ai-engineering-from-scratch
Revision basis: main; September 2026 release v2026.09 references commit d18b8fe.
License: MIT (LICENSE inspected directly).
Purpose: durable knowledge/pattern source for future engineering work. This file is a catalog and provenance record, not a claim that every lesson is integrated or operational.

## Source facts

- 20 phases; current README advertises 523 lessons.
- Curriculum spans Python, TypeScript, Rust and Julia.
- Reusable lesson artifacts include prompts, Agent Skills, agents and MCP servers.
- Core learning loop: problem -> concept/derivation -> build from scratch -> framework/use -> ship artifact -> test/evidence.
- The repository explicitly requires preserving command, working directory, exit code, meaningful output and changed/produced artifact as evidence.
- Repository contains runnable code, quizzes, outputs, focused learning paths, glossary, roadmap and book pipeline.
- MIT license permits reuse subject to the license notice/terms; still inspect third-party dependencies and referenced projects separately.

## Phase map

0. Setup & Tooling — environment, Git, APIs/keys, Docker, data, Linux, debugging.
1. Math Foundations — linear algebra, calculus, probability, optimization, information theory, numerical stability, graphs and stochastic processes.
2. ML Fundamentals — classical ML, evaluation, CV, pipelines, experiment tracking, anomaly/imbalance handling.
3. Deep Learning Core — backpropagation, losses, optimizers, regularization, stability, mini-framework, PyTorch/JAX, debugging.
4. Computer Vision — CNNs, detection/segmentation, generation, diffusion, ViT, OCR/document understanding, retrieval, tracking and VLMs.
5. NLP — tokenization, embeddings, retrieval/search, structured outputs, RAG chunking, entity/relation extraction, LLM evaluation and long-context evaluation.
6. Speech & Audio — ASR, Whisper, TTS, voice pipelines, streaming speech-to-speech, anti-spoofing/watermarking, audio evaluation.
7. Transformers — attention, positional encoding, BERT/GPT/T5, MoE, KV cache, FlashAttention, scaling and speculative decoding.
8. Generative AI — VAEs, GANs, diffusion, conditioning, editing, video/audio/3D generation, flow matching and evaluation.
9. Reinforcement Learning — MDPs, Q-learning, policy gradients, actor-critic, PPO, reward modeling/RLHF, multi-agent RL.
10. LLMs from Scratch — tokenizer/data pipeline, mini-GPT, distributed training, SFT, RLHF, DPO, evaluation, quantization and inference optimization.
11. LLM Engineering — production-oriented LLM application engineering; prompt engineering and practical model use.
12. Multimodal AI — vision-language and cross-modal reasoning/building.
13. Tools & Protocols — tool interfaces, function calling, MCP, Agent Skills, security, authorization, gateways/registries, reliability, conformance and governance.
14. Agent Engineering — agent loop, planning/plan-execute, coding-agent workflows, repository evidence, harnesses, isolation, verification, review and durable feedback.
15. Autonomous Systems — long-horizon execution and operational controls for unattended agents.
16. Multi-Agent & Swarms — orchestration, role specialization, handoffs, shared memory, consensus/BFT, production scaling, failure modes and evaluation.
17. Infrastructure & Production — inference economics, serving, caching, routing, observability, progressive deployment, load testing, SRE, security/compliance and FinOps.
18. Ethics, Safety & Alignment — reward hacking, red teaming, prompt injection, safety/control, provenance, governance, moderation and dual-use risk.
19. Capstone Projects — coding agents, cross-repo RAG, voice assistants, multimodal QA, research agents, DevOps agents, production RAG, code migration, multi-agent engineering, observability/evals, MCP governance, GitHub issue-to-PR agents, safety harnesses and low-level agent/LLM components.

## Highest-value material for our projects

### AI Operating Operator / Elite / ARMY-14
- Agent loop contract: explicit observe -> decide -> act -> observe -> stop cycle.
- Mandatory stop/turn budgets; no unbounded loops.
- Tool registry + schema validation before execution.
- Treat tool outputs and retrieved documents as untrusted input.
- Separate task framing, repository evidence, harness execution, isolation, verification, review and feedback.
- Plan/execute separation and explicit verification gates.
- Durable checkpoints, resumable runs and bounded retries.
- Independent evaluation/observability rather than trusting the agent's own success claim.
- Multi-agent role separation: planner, critic, executor, verifier; avoid shared authority by default.
- Failure-mode tracking: cascading failure, groupthink/monoculture, long-horizon reliability loss.
- Production controls: queues, checkpoints, admission/load control, SRE, progressive release, audit logs.
- Security focus: prompt injection, tool poisoning, secret/PII scrubbing, auditability, governance.

### MCP / protocol layer
The focused MCP route is explicitly ordered, not numeric:
06 fundamentals -> 07 server -> 08 client -> 09 transports -> 10 resources/prompts -> 11 sampling -> 12 roots/elicitation -> 13 async tasks -> 14 apps -> 15 tool-poisoning security -> 16 OAuth 2.1 -> 18 production auth -> 17 gateways/registries -> 28 tool contracts/content -> 29 reliability/cancellation/flow control -> 30 registry supply-chain/drift -> 31 conformance/versioning/operations.
Use this ordering when extending our MCP capabilities.

### Agent Skills
Focused five-lesson route:
22 portable contract/runtime boundary -> 24 discovery/progressive disclosure -> 25 invocation/routing -> 26 permissions/sandboxes/trust -> 27 evals/packaging/portability.
Important boundary: discovery is not authorization; skill metadata is untrusted input; real-host evidence is distinct from conceptual understanding.

### EASY
Potential leverage to investigate later:
- multimodal/document understanding
- OCR
- image retrieval/metric learning
- vision-language models
- local inference/edge inference
- production model routing and caching
- multimodal evaluation
- RAG evaluation and retrieval quality
Only promote a concrete implementation after a real EASY gap is demonstrated.

### Salamou-31
Potential leverage:
- structured outputs/constrained decoding
- embeddings and retrieval
- hybrid retrieval + reranking
- query rewriting
- LLM evaluation
- provider/model routing
- AI gateway patterns
- prompt/semantic caching
- unit economics/FinOps
- production API observability and load testing.

### ASTRA
Potential leverage:
- experiment tracking and reproducible evidence
- time-series/anomaly evaluation
- model calibration/perplexity where applicable
- hypothesis -> experiment -> evaluator -> critic -> iteration loop
- checkpoint/resume and failure containment.
No trading-performance claim is inferred from the curriculum.

## Capstone patterns worth mining into implementation/tests

- Terminal-native coding agent
- Cross-repository semantic RAG
- Autonomous research agent
- DevOps troubleshooting agent
- Code migration agent
- Multi-agent software engineering team
- LLM observability/eval dashboard
- Stateless MCP server with registry/governance
- GitHub issue-to-PR autonomous agent
- Agent harness loop contract
- Tool registry with schema validation
- JSON-RPC stdio transport
- Function-call dispatcher
- Plan-execute control flow
- Verification gates + observation budget
- Sandbox runner/path jail
- Fixture-based eval harness
- OpenTelemetry GenAI spans + Prometheus metrics
- End-to-end coding-agent harness
- RAG evaluation and end-to-end RAG
- Task-spec format and eval runner
- Safety gate and prompt-injection detector

## Evidence / provenance rules to carry forward

1. Source presence is not integration.
2. A README claim is not a runtime proof.
3. Every promoted capability needs source revision, license/dependency boundary, implementation inspection, adapter contract, test, health/reachability evidence and independent verification.
4. Preserve exact commands, working directory, exit code and meaningful output for executable checks.
5. Keep external-provider failures explicit; never convert them into fallback success.
6. Keep project/source boundaries separate: collection knowledge remains knowledge until promoted into a tested project capability.

## Collection policy

Retain the upstream repository as a permanent source. Prefer references and extracted patterns over blind bulk copying. Re-scan the upstream roadmap/changelog before major future upgrades because the curriculum is a living repository and lesson counts/content change over time.

## Directly relevant source files inspected

- LICENSE
- README.md
- ROADMAP.md
- phases/11-llm-engineering/README.md
- phases/12-multimodal-ai/README.md
- phases/13-tools-and-protocols/README.md
- phases/14-agent-engineering/README.md
- phases/15-autonomous-systems/README.md
- skills/course-guide/SKILL.md
- skills/learn-mcp/SKILL.md
- skills/learn-agent-skills/SKILL.md
- phases/14-agent-engineering/01-the-agent-loop/docs/en.md
- book/README.md
- CHANGELOG.md
- FORKING.md
- CONTRIBUTING.md

