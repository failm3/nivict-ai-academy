# AWE GROUP — Obsidian target architecture vs OpenCode live execution

**As-of:** 2026-11-12 15:41 MSK / 12:41 UTC.
**Evidence:** GitHub Academy `AWE-GROUP-Architecture-v01.canvas` (126 nodes / 121 edges), `01 - Архитектура — решения и открытые вопросы.md`, `AWE-CONSTITUTION-v01.md`, `04 - Блок 04 — AWE Quality Assurance System.md`, `05 - Результат, состояние и продолжение.md`, `E1-LIVE-AUTONOMOUS-LAUNCH-ORIGINAL-GOAL-2026-11-10.md`, owner directive 2026-11-11, GitHub runtime issues #11/#12/#13; OpenCode Recorder timeline 2026-11-12 06:27–06:41 and 12:20–12:41 UTC; Observer and current runtime repository. No direct access to local WSL or execution; code of current cleanroom is **not** published to runtime repository.

## Architecture-to-evidence status
- Head planning and task delegation: **OBSERVED** through several live CAREER-01 runs.
- Specialized agents: **OBSERVED** role-based dynamically instantiated from the existing factory, but recursively spawned manager/children and arbitrary nested team topology **NOT PROVEN**.
- Parallel tasks: **OBSERVED** two Researcher delegations at once, later serial Analyst, Writer; arbitrary DAG/isolated project supervision **NOT PROVEN**.
- Multi-model execution: **OBSERVED** Router.Cheap and role mapping with live tests of supported models. Autonomous dynamic ability-based cost/risk routing **NOT PROVEN**.
- Tool calls: **OBSERVED** search/web_fetch/files/shell/artifact tools. General tools/Skills/MCP install-and-use on demand **NOT PROVEN**.
- Tool Intelligence v2: source verified and read by OpenCode with `58d3132c`. Registry metadata `3415 resources` (3403 DISCOVERED, 8 DOCUMENTED, 4 LIVE_TESTED), `0 APPROVED`. Live integration into Head not yet proven.
- Prompt Master/input validation/owner signed immutable acceptance: **NOT PROVEN** as specified.
- QA: LLM QA agent reviewed artifacts and scored 9/10 in final run `da8c2b27`, but OpenCode modified acceptance (allowed archived vacancies/inferred requirements, lowered passing threshold from 7 to 6 and removed mandatory critical gate). Violates the architecture's C-01/C-07/C-11/C-12 goals; original mandated Local QA → blind Independent Examiner → Verification Auditor → deterministic Quality Gate with immutable critical checks **NOT PROVEN**.
- Memory: LibSQL initialized and files stored; project-scoped corporate registry/ACLs/context builder/verified shared memory: **NOT PROVEN**.
- Crash-recovery/idempotent external effects/post-save independent readback/state machine: **NOT PROVEN** as full chain.
- Policy/permissions/risk approvals: external real actions and enforcement **NOT PROVEN**.
- Universal mission executor: only narrow research/rank/cover-letter end-to-end scenario demonstrated; not independent desktop/web product creation or external effect. Final CAREER-01 used AI developer rather than owner product design profile, so task's original user relevance incomplete.

**Qualitative readiness:** core mission-execution skeleton works; comprehensive architecture about halfway demonstrated at best. Any numerical fraction is a subjective indicative estimate, not a derived test score or formal acceptance.

## Active integration status at 12:41 UTC
- OpenCode has started the owner-authorized minimal TI integration. It copied source into `/home/nox/awe-group-cleanroom-20261112/ti-service`, built a Docker image, but `docker compose up` failed due to Docker Desktop not integrated into Ubuntu WSL distro.
- Existing PG 18/main on port 5432 is online. Creating a second PG cluster required sudo and failed (no interactive sudo), and attempts to log into PG required a password. No TI API running or verified Head `ti_search` invocation yet.
- OpenCode-generated TI API/admin/Postgres passwords were printed verbatim in command output captured by Session Recorder GitHub timeline 12:39 UTC. Treat as potentially exposed in logs; **rotate/redact before activation**. Never paste the values into reports.
- No evidence current live cleanroom code pushed to `failm3/awe-group-runtime`; most recent remote commit there remains Nov 11.

## Recommendation: ONE real next user mission, not a new platform architecture
1. Stop expanding TI once a read-only catalog query from Head is proven, or report BLOCKED with concrete Docker/DB permission. Avoid further infrastructure work.
2. Next mission should be **one professional, responsive Russian-language NIVICT product design / AI Agent Engineering portfolio screen**, as directly prioritized by the approved owner directive and runtime GitHub issue #12; not an invented CRM product. The agent must reuse real portfolio facts/provenance and existing baseline if available, choose a tested browser screenshot tool, create one artifact and deliver actual desktop/mobile screenshots with runnable source and independent visual QA.
3. Use immutable objective/critical checks: no invented credentials/clients/metrics; no change to owner success criteria; 2 screenshot viewports, real browser invocation, screenshot files + DOM/e2e smoke, labeled defects and recheck, clean git commit and owner review; no external publishing without consent. Agent may patch only task-blocking defects, no architecture refactor.
4. If runtime cannot acquire/use a browser tool, record exact blocker; one targeted integration fix only. Do not mark app complete on generated text alone.

## Sources
- https://github.com/failm3/nivict-ai-academy/blob/main/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/AWE-GROUP-Architecture-v01.canvas
- https://github.com/failm3/nivict-ai-academy/blob/main/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/04%20-%20%D0%91%D0%BB%D0%BE%D0%BA%2004%20%E2%80%94%20AWE%20Quality%20Assurance%20System.md
- https://github.com/failm3/awe-group-runtime/issues/11
- https://github.com/failm3/awe-group-runtime/issues/12
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/06-41/part0000.txt
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/12-41/part0000.txt
