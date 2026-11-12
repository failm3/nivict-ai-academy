# AWE GROUP — current actual runtime, tooling, UI and progression

2026-11-12. Verified against GitHub Academy approved architecture, runtime issue #11/#12, OpenCode Session Recorder up to 12:53 UTC, and official Mastra/OpenCode product documentation.

## Facts / identity
- Owner goal: mission → Prompt Master → Head → orchestrator/PM → dynamically created specialists → model/tool routing → parallel work → blind QA → persist/recover, with human approval for risky external actions.
- Current active prototype implementation: custom AWE runtime Node/TypeScript using Mastra tools/agents/workflows. Head is **AWE's own agent logic**, not OpenCode, Agno, Hermes or Agent Zero. OpenCode is the current engineering developer/harness; Hermes or Agent Zero are candidates for downstream capabilities or alternate framework only if justified. Do not stack four orchestrators.
- OpenCode Session Recorder 12:49 UTC proves separate TI API on localhost:8871 and response from Postgres; but it loaded **only 12 resources** from research files, not the canonical ~3415-resource Manus database backup. `ti_search` file created, wiring and type-check ongoing at 12:53 UTC, not yet Head invocation proven.
- Secrets: OpenCode printed service credentials and a pre-existing web-search API key to recorder outputs in 12:39–12:53 UTC; must rotate exposed values and prevent logging secrets. Avoid reproducing values in any report.
- Core missing proof: recursively generated agents, comprehensive dynamic model choice, immutable acceptance gates, scoped approval policy, production UI, crash-recovery, autonomous engineering.
- Tool registry is research metadata, not runnable automatic integrations. Distinguish DISCOVERED vs LIVE_TESTED vs APPROVED. Reusing existing libraries and tools may address a majority of functional capabilities, but no justified numeric probability of complete architecture closure.

## Interfaces
- Mastra Studio is documented to run locally at localhost:4111 for agents, workflows, tools, traces; **NOT yet verified started on this WSL or wired to current application**. A live Studio frontend is a reasonable first operator/developer UI rather than building custom full app. OpenCode Web UI is for OpenCode and not equivalent to AWE UI. Custom full UX is separate work and should follow real-use feedback.
- Confirm existing code/package.json/entrypoint, exact service startup command and local URL before claiming UI is live.
- User wants business-level operator console eventually: mission inbox, approvals, live agents, traces, artifacts, costs, projects, connector status. Build only missing pieces after using Studio/available Web UI.

## Integration priorities
Tier 0: verified local shell/git/files, reproducible browser desktop/mobile screenshot + visual QA, Tool Intelligence read-only catalog search, persisted project artifacts/traces.
Tier 1: company mail OAuth restricted read/draft (Gmail if hosted on Google, else email provider's APIs or IMAP/SMTP bridge), Figma MCP/API for design review/frames, GitHub, Drive, Calendar according to mission.
Tier 2: HH/Telegram/business services when needed. Company mailbox can be the operational identity for signups, but email credential does not automatically grant API/OAuth access and should never be a universal super-admin secret. Inbox content untrusted; sending/publishing/funds require explicit authorization. Avoid exposing passwords, MFA, OAuth tokens to chat/GitHub.
No suggestion to connect personal Gmail integration automatically to AWE; ChatGPT connector accounts do not transfer credentials to local WSL.

## Pragmatic next mission
**AWE-UI-CAPABILITY-01 (one bounded user-visible acceptance)**:
1. Finish only minimal TI `ti_search` integration or report concrete BLOCKED; rotate leaked tokens first, no full infra expansion.
2. Open an **existing** local AWE UI (prefer Mastra Studio if code compatible) and prove live Head and run trace, not OpenCode-only UI; give URL and screenshots.
3. Submit a short real mission through AWE Head: inspect ability to create **one professional Russian NIVICT product-design screen**, enumerate actual browser/design capabilities; actually run one read-only browser screenshot smoke-test of a controlled local page and return screenshot, evidence and model/tool names. Do NOT produce a fake complete portfolio or self-relax acceptance criteria.
4. Report measured gaps, owner approvals, cost, and only task-blocking needed changes; stop. No new custom dashboard, recursively autonomous updater or sweeping refactor.
5. Later: once UI and capabilities validated, hand off one real screen with truthful portfolio provenance and independent visual QA.

## Sources
- https://github.com/failm3/nivict-ai-academy/blob/main/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/AWE-GROUP-Architecture-v01.canvas
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/12-49/part0000.txt
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/12-53/part0000.txt
- https://github.com/failm3/awe-group-runtime/issues/11
- https://mastra.ai/docs/studio/overview
- https://opencode.ai/docs/cli/web
- https://developers.google.com/workspace/gmail/api/auth/scopes
