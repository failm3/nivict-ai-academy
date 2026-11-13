# OpenCode — R1 market reuse / runtime inventory (DRAFT; NOT SENT)

**Status:** prepared handoff for owner review **after successful R0 acceptance**. This is NOT authorization to send/execute, install tools, expand budget, modify keys, launch paid trials, push changes, or overwrite R0. It is a **read-only inventory and comparative design** task, not an order to implement the R1 Gateway.

## Role
Chief integration engineer and independent investigator of existing market-ready components for Nox/AWE GROUP. Avoid automatic agreement with previous decisions. Goal: maximum reuse, minimum additional code, no rewrite of Nox runtime/control plane.

## Inputs and immutable context

- [Market reuse audit](../RESEARCH/MARKET-REUSE-AUDIT-2026-11-13.md)
- [R1 architecture and statuses](../README.md)
- [R1-01 Tool Gateway contract](../01-TOOL-GATEWAY/SPEC.md)
- [R1-01 candidates](../01-TOOL-GATEWAY/CANDIDATES.md)
- [R1-01 independent acceptance](../01-TOOL-GATEWAY/ACCEPTANCE.md)
- Original R0 final engineering report and exact accepted source HEAD **must exist and be provided**. If they do not exist, mark BLOCKED, do NOT infer successful R0.

## Task (read-only, no network credential changes)

1. Establish exact local R0 source sha, branch, checkout cleanliness, Node/npm, `@mastra/core` / `@mastra/mcp` versions, `package.json` and lockfiles; do not modify any.
2. Create inventory of existing Head/Mission Manager/Agent Factory/Tool Intelligence, file/shell/browser/search tools, internal grants/permissions, capabilities, observed real calls, persistent state, traces, QA. Identify VERIFIED vs partially implemented vs NOT_IMPLEMENTED based on code and test evidence.
3. Compare actual installed package APIs to official Mastra built-in `ToolSearchProcessor`, `SkillSearchProcessor`, MCPClient, tool approvals, supervisor propagation, durable runs, storage. Document compatibility/version gaps without performing unauthorized upgrades.
4. Compare Composio (`@composio/mastra`), Pipedream Connect, Arcade, ToolHive, Activepieces for 3 specified tasks: business SaaS read-only, browser screenshot, internal file/test worker. Include concrete protocol, credentials, data egress, user separation, license, deployment, estimated billing plan, version, source. **No vendor logins or paid calls**.
5. Compare Docling, Crawl4AI, existing project memory/PG/Supermemory candidate, Mastra Knowledge (alpha warning), and RAGFlow as fallback. Choose smallest feasible knowledge ingestion/retrieval path.
6. Compare Agent Skills + Mastra skill search; Promptfoo, Playwright, optional Langfuse / Inspect AI for evals.
7. Deliver a **Build-vs-Buy gap map**: for every desired R1 capability, note `EXISTING`, `READY_TO_CONFIGURE`, `REQUIRES_ADAPTER`, `MINIMAL_NEW_CODE`, `BLOCKED`. Each claim with repo file/function or public official documentation link and evidence.
8. Recommend only **one** default integration architecture and at most 2 comparative alternatives. Identify first 5–10 approved capability candidates, required human approvals, exact acceptance tests, rollback and bounded risk. No migration to another Head/Model Router/Mission Manager unless independently justified by evidence.
9. Send result for owner's decision, do not automatically start R1 implementation.

## Required final artefacts

- `R1-READONLY-CAPABILITY-INVENTORY.md`
- `R1-BUILD-VS-BUY-MATRIX.md`
- `R1-ISOLATED-INTEGRATION-BENCHMARK-PLAN.md`
- status `RECOMMENDATION_ONLY / BLOCKED / NEEDS_OWNER_APPROVAL`, not PASS for any unexecuted integration.

**Hard fail** if an uninstalled catalog entry is called working, if model-visible tool descriptions are treated as authorization, if QA evidence is claimed but not run, if cost=0 is inferred from recorder metadata, if protected operations execute without owner approval, or if the task itself changes source state beyond an approved designated notes location.
