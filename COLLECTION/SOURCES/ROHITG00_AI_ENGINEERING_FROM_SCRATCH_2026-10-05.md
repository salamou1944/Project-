# rohitg00/ai-engineering-from-scratch — Collection Record

- Source: https://github.com/rohitg00/ai-engineering-from-scratch
- Captured: 2026-10-05
- Provenance: user-supplied GitHub source; verified directly through GitHub
- Repository: rohitg00/ai-engineering-from-scratch
- Default branch: main
- License: MIT
- Archived: No
- Primary language: Python
- Stars at capture: 63,975
- Forks at capture: 10,948
- Open issues: 69
- Latest repository activity: updated 2026-10-05; pushed 2026-10-04

## What it contains

A large free/open-source AI-engineering curriculum organized into 20 phases and 523 lessons, spanning Python, TypeScript, Rust, and Julia. It covers mathematics and ML foundations, neural networks, backpropagation, tokenization, attention, LLM engineering, agents, MCP, Agent Skills, evaluation, production engineering, autonomous/swarm systems, and reusable prompts, skills, agents and MCP servers.

The repository explicitly follows a read → build → run → preserve evidence → modify workflow rather than a copy/paste tutorial model.

## High-value reusable assets / patterns

1. Learning skills for AI coding hosts:
   npx skills add rohitg00/ai-engineering-from-scratch
   Provides start-learning, learn, course-guide, learn-mcp, and learn-agent-skills routes.
2. Agent Skills learning path: five-lesson route covering contract, discovery, invocation, sandbox boundaries, release evaluations and host portability.
3. MCP learning path: 17-lesson route covering stateless requests, transports, bidirectional work, security, reliability, registry governance and conformance evidence.
4. Evidence-first engineering pattern: each lesson keeps command, working directory, exit code, meaningful output and produced/changed artifact.
5. Production engineering material: relevant to API Factory, AI Operating, Elite, agent control-plane and deployment hardening.
6. Scaffold/audit tooling: scripts/scaffold-lesson.sh and scripts/audit_lessons.py plus contributor templates and invariant checks.
7. Free/self-hosted learning: core curriculum is designed to run locally without a mandatory paid SaaS dependency.

## Operational / dependency notes

- Core repository is MIT licensed.
- Learning-host installation uses Node.js / npx and a compatible skill-capable coding agent.
- Runnable Python lessons require Python 3.
- Some focused labs require a selected host and writable skill scope.
- Website access is an alternative to cloning, but local clone is required for copied repository commands and executable MCP/Agent Skills labs.
- This is a curriculum rather than a SaaS runtime; do not treat it as a deployable production application without validating the relevant lesson/project artifact.
- External model/API dependencies may appear in individual lessons; inspect each lesson before classifying anything as zero-cost or production-ready.

## Maintenance / health

- Repository is active and not archived.
- GitHub metadata shows substantial recent activity.
- Release v2026.09 (d18b8fe) brought the curriculum to 523 lessons across 20 phases.
- Active Actions workflows include build-book, curriculum, translate and Copilot code review.
- Open issues and pull requests demonstrate ongoing maintenance; stars are discovery signal only, not quality proof.

## Value to our collection

High value.

Primary leverage categories:
- AI engineering learning paths
- Agent Skills
- MCP
- evidence-driven verification
- agent development
- production AI engineering
- repository automation/auditing
- free/local development resources

Potential direct reuse targets:
- Salamou-31 / AI Operating / Elite
- API Factory / AI-API Hub
- SOAT verification methodology
- reusable agent-skill architecture
- MCP conformance and security verification
- reduction of paid learning/development dependencies

## Verification status

DISCOVERY_CAPTURED — NOT_PRODUCTION_VERIFIED

This record does not claim that every lesson, skill, MCP lab, API integration or external dependency is production-ready. Any component selected for implementation must be separately inspected, license/dependency checked, and executed where practical.

## Follow-up collection rule

Keep this repository as a permanent distinct source even if it appears in future collection jobs. Future snapshots should track:
- star/fork movement
- release changes
- new phases/lessons
- new skills
- MCP/Agent Skills changes
- dependency/runtime changes
- security/operational limitations
- maintenance/archive status
- reusable artifacts with direct value to our projects
