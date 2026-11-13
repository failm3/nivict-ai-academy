# NOX / AWE GROUP — Internal architecture and proposed OpenCode integrations

**Date:** 2026-11-13. **Status:** DISCUSSION / PROPOSAL; NOT AN R0 CHANGE OR OWNER AUTHORIZATION. This document captures an architecture explanation and candidates to evaluate while R0 is being independently finalized. No installations, keys, permissions, commits in runtime or paid API tests performed.

## Two separated control planes

- **OpenCode development plane:** engineering agent + child engineering/QA sessions + controlled Git and development tools; builds, fixes and tests Nox.
- **Nox operating plane:** user-facing autonomous mission manager; not an OpenCode subagent and not dependent on OpenCode for ordinary tasks.

## Candidate integrations to prepare for OpenCode, without altering live R0

1. GitHub/Git: review, branch, PR, read-only baseline and approval-gated push/release.
2. TypeScript build/tests, lint and security/static analysis; reproducible combined release gate and non-mutating read-only baseline.
3. Playwright/Chromium: browser functional, screenshot, responsive and a11y acceptance in isolated workspace.
4. Context7: version-specific technical documentation, optional/read-only.
5. Figma official remote MCP: read design tokens, components and frames; keep write-to-canvas separately approved.
6. Existing Tool Intelligence/Manus registries: read-only discovery, explicit evidence of not-yet-executable tools. Gate a real Tool Gateway in R1; no mass connection of 4504 catalog entries.
7. Professional skills for architecture review, debugging, independent QA, design QA, reproducible release gates, pinned and verified.
All require version compatibility, bounded tokens/permissions, cost test, provider authentication approval, isolated rollout. OpenCode docs: https://opencode.ai/docs/mcp-servers ; https://opencode.ai/docs/skills ; https://opencode.ai/docs/plugins . Official Figma: https://developers.figma.com/docs/figma-mcp-server/ . Context7: https://context7.com/docs/overview .

## Target Nox runtime process — conceptual contract

1. User request enters mission API/UI. Mission ID, tenant/user, budget, risk class, nonfunctional acceptance and initial artifact context persisted.
2. Prompt Master converts natural language into versioned, auditable requirements; asks clarifications only for essential blockers; owner approval or explicit policies on ambiguous external actions. This component is architectural / implementation and acceptance still need verification.
3. Head chooses mission strategy and decomposition, identifies roles, dependency DAG, deliverables, acceptance, permissible recursion. Head does not bypass safety gates.
4. Mission Manager is deterministic control plane: scheduler, dependency gates, concurrency, budget and token caps, heartbeat/leases, cancellation and crash recovery; durable CAS prevents double-execution.
5. Agent Factory instantiates scoped **ephemeral agent workers from versioned role templates**, not newly trained LLM models. Instances receive mission/task IDs, model policy, selected skills/packs, memory view, typed input/output schema and permitted tools. Head may request agent creation; deterministic factory/policy gate actually provisions it. Agents can spawn bounded children only with authority delegated from parent.
6. Model Router chooses approved local/cloud LLM based on role, quality/latency/cost, security and remaining quota, records usage and handles bounded failover. Model calls are reasoning engines, not the control plane or memory database.
7. Tool Intelligence is registry/search with provenance and versions; Tool Gateway (R1 planned) turns only APPROVED known connectors into mission-scoped grants; launches isolated execution with abort, audit, idempotency and typed output. Registry entries alone are not available executable tools.
8. Bots are **deterministic action workers** / adapters / automations (shell, browser, API, parser, scraper, test runner), not inherently LLM agents. A coding specialist could propose new bot source in sandbox, but installing/publishing/enabling it requires tests, signature/review and user or delegated policy approval; no automatic production code injection.
9. QA independent of producing agent checks original immutable acceptance, real files/screenshots/tool receipts, security, accessibility, professional domain criteria, cost and missing artifacts; can reject and request bounded repair. Text claims of success are not proof.
10. Delivery packages actual artifacts, report, independent verdict, limitations and reproducible locations; update episodic, provenance-aware long-term memory only after successful verification, respecting workspace boundaries.

## Where things live (target and evidence-aware current split)

| Entity | Target persistence / lifetime | Current status caveat |
|---|---|---|
| Agent role templates, prompts, skills, packs, tool manifests | Versioned config in Git, pinned digest; immutable per mission | Some code and specialists exist; future factory contract still not acceptance-proven |
| Live agent workers | Ephemeral process/context; persistent task state and receipts only | True dynamic recursive delegation not release-accepted |
| Bots and tools | Versioned code packages/adapters, sandbox workers, registry metadata | File/shell/browser/ti_search/manus_search partially available; universal gateway not implemented |
| Mission state, checkpoints, approvals, budgets, leases | Transactional durable DB with CAS and ownership | Local .awe-data / JSON/LibSQL in audited local runtime; races are R0 P0 |
| Artifacts, screenshots, files, manifests | Durable artifact store with hashes and provenance, separate from LLM messages | Local .awe-data/artifacts used in NIVICT mission; missing required manifest caused QA FAIL |
| Short-term context | Bounded task-scoped message/context cache | Existing partial mechanisms; not persistent source of truth |
| Long-term knowledge/memory | Namespace-separated searchable store with links to source, revision, TTL/revocation | Supermemory/vector experience historical; production integration not independently verified |
| Tool Intelligence catalog | PostgreSQL/PG read API + provenance, approval state | Existing catalog ≠ real invocable tool |
| Secrets | Secure isolated vault/environment, never logs or untrusted prompts | Specific final production secret manager not verified |
| Immutable QA and audit ledger | Append-only events, reproducible release SHA, executed tests, token/cost telemetry | Recorder / Observer read-only instruments exist, but do not certify release |

## Example: design mission

User request → Prompt Master frozen brief → Head plans design + research + coding + QA → manager creates dependent tasks → factory provisions scoped ephemeral specialists → model router selects appropriate LLMs → gateway provides minimal browser/file/figma/tools → sandbox bots execute and register artifacts → independent visual/a11y/function QA (expert review separately) → bounded repair → final delivery → source-linked memory update. Stop on cancellation, exceeded limits, owner approval gates.

## Current boundary of evidence

Prior real NIVICT mission generated responsive site, but independent QA overall FAIL (13/14, missing README/manifest), owner aesthetic evaluation 2/10. Earlier independent audit required five P0 fixes; R0 is running in OpenCode as of prior 02:25 UTC snapshot. R1 gateway, professional quality packs, full stress test, autonomous Nox release NOT VERIFIED. Do not confuse planned flow with running end-to-end infrastructure.

**Owner decision pending**: choose integration priority and approval policy; do not silently install while R0 active.
