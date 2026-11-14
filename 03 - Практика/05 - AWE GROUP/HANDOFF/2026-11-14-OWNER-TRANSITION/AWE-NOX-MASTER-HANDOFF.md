# AWE GROUP / NOX — MASTER HANDOFF / 2026-11-14

**Owner-authorized cross-chat continuity checkpoint.**  
**As-of:** 2026-11-14, 16:56 UTC / 19:56 Moscow.  
**Canonical target repository:** `failm3/nivict-ai-academy`.  
**Purpose:** restore project architecture, owner decisions, current OpenCode execution, acceptance requirements, future product plan, and working style.  
**Evidence level:** this is a detailed human-readable reconstruction of the conversation and cited source state, **NOT a verbatim automatic export of every ChatGPT message**. Exact owner kickoff prompt is separately preserved in this handoff directory. Do not assert full byte-exact preservation of this chat. Preserve earlier authenticated GitHub recordings unchanged.

## 0. Owner's overriding priorities (ACTIVE, do not supersede)

1. **Finish a product, not infinite architecture.** The consultant must actively stop scope creep. Every proposed addition must answer: "Без этого Nox действительно не может пройти утверждённую приёмку и быть передан владельцу?" If NO → backlog for later version.
2. Main strategy **EXTEND NOX / GENERALITY BEFORE WORKFLOW COUNT**. Preserve and improve existing Nox; no rewrite unless a proven necessity. Do NOT build a bespoke workflow for each profession.
3. Objective: **usable, independently verified, autonomous digital teammate**. Nox should understand unknown task requirements, find and organize missing competencies/tools, execute real work, acquire useful experience and transfer it, coordinate teammates, safely recover, and not require constant owner supervision.
4. After actual acceptance → **STOP core feature growth → create product interface/shell → hand over to owner (R3)**. No extra architecture research, broad new stress campaign, new frameworks or catalog expansion as a default.
5. The OpenCode OWNER APPROVAL was already sent on Nov 14; engineering has started. **Do not resend, interrupt or change scope without a concrete blocker**. OpenCode is the development environment; Nox is the product.
6. Maintain factual rigor: source presence ≠ working integration; past PASS ≠ live success; recording of tool activity ≠ validated acceptance; report assertions ≠ independent evaluation; success of one unknown task ≠ proof of universal competence.
7. Owner wants important decisions, prompts, results, checkpoints, and chat continuity in GitHub. Publish with verified readback. NEVER commit credentials, tokens, PATs, personal secrets, or private data. Full message-by-message auto-archival needs an independent capture path; do not falsely claim this checkpoint is a complete byte-exact transcript.
8. Russian, direct technical style; constructive criticism welcome; no repetitive clarifying questions; consultant is chief architectural advisor and independent acceptance reviewer, not blind cheerleader.
9. OpenCode has broad delegated engineering authority, including subagents, tools, models and parallel work within existing budgets/permissions; no blanket permission for unlimited spend, irreversible effects, production operations or expanded secrets.
10. Nox is masculine grammatical gender, project label AWE GROUP; the main agent is called Nox. External development prompts may use AWE GROUP as project label.

## 1. Explicit six acceptance criteria (owner's final Definition of Done)

**Do not say “Nox готов” without evidence of all six.**
1. **Acquisition of new professional competency:** for a previously unknown work type, Nox can identify requirements, find and qualify necessary tools/skills, build a suitable agent team, without a programmer writing bespoke core code for that profession.
2. **Real work and actual deliverable:** Nox solves a substantive task, produces files/product/results with independent oracle/QA validation, not just narrates a plan.
3. **Useful reusable experience:** after success, Nox stores provenance-bound, applicable, correct experience; fresh follow-up task demonstrates real transfer or measurable benefit versus memory-off (not just that LibSQL can write/read).
4. **Operational autonomy:** plan, execute, diagnose, replan, recover within limits without constant owner prompts. User confirmation only for truly needed permissions, new spending or risk boundary.
5. **Coordinated teamwork:** can accept delegated tasks, form and manage specialists, produce result in a larger team with reproducible trace; do not assert a general productivity advantage without a controlled comparison.
6. **Dependability and truthful status:** does not falsely mark failed/partial work ACCEPTED, respects grants, data boundary and budgets, recovers/pauses safely, can be relied on within a measured scope.

**Exact desired verdict when AND ONLY when these pass:**
> «Nox готов. Останавливаем разработку ядра, переходим к оболочке и передаче тебе».

Readiness is bounded, measured readiness for initial controlled owner use, not zero-error, universal human-level ability, certified production security, or 24/7 availability.

**Small qualification:** the owner-approved kickoff prompt explicitly demands a successful unknown-task generality demonstration, but does NOT literally make passing all six criteria in one final suite mandatory. This is an acceptance gap, not a reason to interrupt OpenCode mid-development. At its first output verify all six; if evidence missing, require targeted validation/bugfix, not architectural expansion.

## 2. Owner-approved engineering prompt and engineering commitments

Owner approved on Nov 14 (the exact full text is in `OWNER-APPROVAL-EXACT.md`):
- "EXTEND NOX / GENERALITY BEFORE WORKFLOW COUNT."
- OpenCode as chief engineering executor, empowered to decide technical architecture, code modifications, tools, model selection, bounded autonomous subagents, parallel checks, sandbox installs, tests.
- "Прекрати рассматривать исследования и архитектурное планирование как основной результат работы." No building infra for its own sake, no installing everything in Cortex's catalog.
- A successful Nox should take unknown task → make plan → choose models/agents/tools → detect missing capability → find/check/acquire it → replan on failure → get real result → independent QA → finish with frozen core/no developer hints.
- Save changes and evidence to GitHub, check publication via readback, report honest incomplete states, no declaration that Nox is ready without tests.
- Execution begins after stable GitHub auth.

**Current intended finite engineering path** as OpenCode formulated:
A. **P0-min correctness** for trustworthy evidence (artifact identities/revisions, immutable review candidate, QA binding, failure gates, budgets).
B. **Generalization loop** `spec → plan → delegate → observe → diagnose/replan → verify → recover`.
C. **Host-owned Capability Plane** `requirement → discover → select → acquire → inspect → qualify → approve → admit → invoke → observe → competence/revoke`.
D. Frozen source, hidden task(s), independent oracle, failed-first-route, unseen tool, cross-domain result, fresh-agent transfer versus memory-off, controls.
E. If passes acceptance → shell/UX → owner handover. If fails → only bounded, evidence-driven corrections.

A full stress test of long-running 24/7 operation, 50–100 concurrent agents, heavy DB pressure etc **was not explicitly specified by the kickoff**. Functional tests, regression, actual autonomous test required; resilience/recovery tests are in strategy. Do not misrepresent broad stress as already authorized, launched or passed. A targeted reliability acceptance of concurrent missions, interruption/recovery and resource bounds is advisable without opening endless architecture research.

## 3. Frozen/reviewed original architecture: what's there vs. what's missing

Audit basis **`r1/dev@68cc0ee20a25991ea275512e20ac521cc8f8234b`** (historical snapshot; local OpenCode may have uncommitted changes after this).

| Layer | Confirmed source wiring on audited base | Gaps / caveats |
|---|---|---|
| Input/API | Authenticated CLI/REST, typed spec, explicit approval and spec hash binding | Product shell absent; full conversational clarification/edit before approval incomplete |
| Prompt Master | `src/agents/prompt-master.ts`, converts request to spec, hash binding | YES IMPLEMENTED, but NOT full dialogic prompt editing |
| Head | `src/agents/head-agent.ts`: dynamic roles/tasks/tool grants, planning | Silent generic fallback on parse errors; typed capability gap/replan being built; host-only model policy |
| Mission Manager | `src/agents/mission-manager.ts`, parallel delegations, stages, bounded repairs | Exact reviewed-candidate/terminal guarantee was incomplete |
| Specialists | `src/agents/specialists.ts`, recursive dynamic specialist instructions | Roles/prompts exist; new capability acquisition not equivalent to specialist naming |
| Tools | File/shell/web search/fetch/extract etc | General discovery/qualification and Skills lifecycle missing in reviewed base |
| Browser/MCP | Playwright MCP path existed | Unpinned versions, schema mismatch, isolation/egress concerns; not production-qualified |
| Model routing | `src/config/models.ts`, host `byAgent/byRole`, SDK ledger | Not measured adaptive auto-routing; whole mission economics incomplete |
| Persistence | LibSQL history, checkpoint and durable intents, recovery | Semantic/working recall off; fresh-agent transfer and gain not proved |
| QA | LLM review plus deterministic QA gate, evidence and hash checks | Complete typed EvidenceBundle + immutable candidate linking needed |
| Security | deny-by-default, scoped grants, Linux sandbox and safe web fetch | No general multi-tenant/Windows security guarantee |
| Product shell | CLI and REST only | Owner-facing UI after R2 |
| Update automation | No independent Evolution plane | Future post-handover enhancement |

**Fundamental decision:** Nox is a credible expandable *bounded execution kernel*, not a validated general-purpose autonomous employee yet. We must **extend**, not rewrite. The 4504 Cortex registry entries are all candidates/UNVETTED, not callable certified tools.

### Structural diagrams
```text
Owner (currently CLI/REST; UI later)
     ↓
Prompt Master [implemented; clarification loop incomplete]
     ↓
Approval / typed immutable task spec
     ↓
Head [dynamic plan/roles] ↔ Host-owned model policy
     ↓
Mission Manager [parallel/recursive agents + checkpoints]
     ├→ Specialist team → files/shell/web
     ├→ Capability Plane [IN PROGRESS] → MCP/Skills/APIs → qualify/grant/invoke
     ├→ LibSQL / reusable competence [partial; transfer unproven]
     ├→ QA + independently verified exact candidate [base + P0 in progress]
     └→ Recovery/leases/replan [recovery base; general replan IN PROGRESS]
     ↓
Real artifacts and honest terminal outcome

Post-R3 optional:
Cloud Nox Evolution (24/7 monitoring) → validated recommendations
Update Manager (controlled release/rollback) → Nox runtime
OpenCode adapter (optional coding executor, NOT the core).
```

### Mission lifecycle envisioned
Owner task → Prompt Master spec and clarification as needed → owner approval → Head plans/team/tools → if capability gap, discovery/qualification under grants → replan → Mission Manager delegates/executes → QA independent check → bounded repair/replan or safe BLOCKED → persist verified experience → deliver result with evidence. Not every arrow is a proven live runtime behavior yet.

## 4. Current OpenCode execution, verified observational facts Nov 14

**Stable Github authorization fixed at 16:19 UTC**:
- Previous repeat authorization caused by temporary OAuth device-flow publication script; Git helper had not persisted credentials inside isolated HOME.
- User created one fine-grained PAT for `failm3/nivict-ai-academy` with Contents Read/Write and metadata read. No token in ChatGPT or GitHub.
- OpenCode reported token moved to `.oc-isolated/home/.config/opencode/github/nivict-ai-academy.token` (file mode 0600, directory 0700, `.oc-isolated/` gitignored) and removed temporary `/tmp/opencode/github-pat`.
- Clean fresh process API and git ls-remote checks reported successful, no new commits just for token setup. Plain protected-file store, not OS keyring. NEVER reveal token contents.

**Kickoff for approved new engineering work: 16:20 UTC**:
> "Начинаю с P0-min как основы достоверных испытаний: canonical artifact identity/revisions и immutable reviewed candidate. Затем подключу capability-gap/replanning loop и проведу реальное испытание на новой задаче. Изменения будут проверяться тестами до любой публикации."

**~16:23 UTC:** review identified candidate freeze seam between artifact reconciliation and QA; repair should create separate candidate epoch.

**~16:25 UTC:** recognized QA might read mutated live files after snapshot; needs immutable exact QA input, not just artifact hash.

**~16:30 UTC:** regression showed receipt must bind terminalization; repair/recovery backward-compat checks.

**~16:32 UTC:** OpenCode reported implementation of P0 artifact identity/revisions:
- `src/utils/storage.ts`: normalized canonical mission-relative POSIX paths, both separator forms, traversal/absolute path checks, monotonic per-mission/path revision, deterministic selection, nested same-name independence, legacy dedup, reconciliation.
- `src/tools/index.ts` `file_write`: register proper nested path.
- New `src/tests/artifact-identity.test.ts`.
- Developer-reported tests: 5/5 + 10/10 + 12/12 + 75/75 + 13/13 = **115/115** selected checks, typecheck success. Evidence is OpenCode session report, not independently re-run. OpenCode explicitly said no commit yet at this point.

**~16:33 UTC:** selected minimal Head capability request + manager one bounded approved discovery/acquisition stage + replan. No automatic unvetted package install or scope expansion.

**~16:51 UTC:** corrected public typing contract:
> `planMission` returns `DelegationPlan | CapabilityDecision`; ordinary calls source-compatible. Test `ordinaryPlan` assumptions adapted.

**~16:53 UTC:** typecheck passed, started new offline end-to-end integration test sequence:
> `unknown capability → real artifact → replan → execution → QA`
plus denial of unapproved grants and duplicate acquisition controls. **This is NOT yet a passed live hidden-task transfer test.**

**~16:55 UTC:** resume test found a real defect:
> persisted capability attempt plus `acceptedPlan` before ordinary plan; resume incorrectly treated paused acquisition as existing accepted plan and skipped Head replan.
OpenCode fixing accepted-plan state rather than weakening test.

**~16:56 UTC:** 500ms timeout was flaky due to lease/startup latency; adjusted test to deterministic checkpoint: pause exactly after saved capability attempt, then independent manager resumes; tests recovery reproducibly.

**AWE Observer** as of ~16:55 UTC collection #1142: OpenCode `PROCESS_PRESENT`; launch and runtime working trees have many modifications, but HEAD of observed working copies still `29db82e7b00c25c96dbf035aef4b5e3a9ff3eff4`. Observer's event schema `DATABASE_SCHEMA_UNSUPPORTED`; process detection alone does NOT prove a particular task. Read OpenCode recording for actions, not just Observer status.

**Do not claim:** main Nox development finished, latest changes pushed, all tests passed, real hidden autonomous mission passed, 24/7 works, or six acceptance criteria passed.
**Do:** on subsequent verification pull latest recorder timeline AND observer and academic repo commits/readback.

## 5. Canonical sources, current repos and anchors

- **Main knowledge/owner decisions:** https://github.com/failm3/nivict-ai-academy
- **Independent generality strategy (owner APPROVED):**
  https://github.com/failm3/nivict-ai-academy/blob/b42d05dd44c05815b683784ad803c668bc3d6a20/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/RESEARCH/NOX-UNIVERSALITY-STRATEGY-2026-11-14/UNIVERSALITY-STRATEGY.md
- **Independent audit:** https://github.com/failm3/nivict-ai-academy/tree/main/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/RESEARCH/NOX-R2-INDEPENDENT-AUDIT-2026-11-14
- **OpenCode recording:** https://github.com/failm3/awe-opencode-recordings — `LATEST.md`, `timeline/2026-11-14/16-20/...` to `16-56/...` and later minutes as they are added.
- **Recorder specific examples:**
  - `timeline/2026-11-14/16-19/part0000.txt`: credential verification.
  - `timeline/2026-11-14/16-32/part0002.txt`: P0 identity implementation and test results.
  - `timeline/2026-11-14/16-33/part0001.txt`: planned minimal capability workflow.
  - `timeline/2026-11-14/16-51/part0000.txt`: typing `DelegationPlan | CapabilityDecision`.
  - `timeline/2026-11-14/16-53/part0000.txt`: integration test.
  - `timeline/2026-11-14/16-55/part0000.txt`: acceptedPlan resume defect.
  - `timeline/2026-11-14/16-56/part0000.txt`: deterministic checkpoint/recovery test.
- **Read-only Observer:** https://github.com/failm3/awe-group-observer — `LATEST.md`, `state.json`. Observer redacts code/branch names/secrets.
- **Local source working checkout:** WSL `/home/nox/awe-group-cleanroom-20261112` (cannot access directly from this ChatGPT session), separate from `awe-e1-launch-20261110` and other archived source trees.
- **OpenCode:** WSL, isolated config under `.oc-isolated`, Router.Cheap models. OpenCode and Nox are separate entities; the former engineers the latter.

## 6. Recent owner questions, decisions, and answers — PRESERVE

### A. Approving the owner kickoff
Owner transmitted the full approval (separate EXACT file) with explicit permission to begin engineering, independent model/tool/subagent selection, bounded safeguards, no artificial agent-count caps. Asked whether this means Nox will be ready; answer: **right direction but ready only on real final acceptance, not promise**.

### B. Start confirmed, good wishes
Owner asked verify OpenCode started and requested luck for owner and assistant. Checked recording: `session.execution.started` Nov 14 at 16:20 UTC and live tool calls; stable PAT configured 16:19 UTC. Shared good wishes for real autonomous launch.

### C. What after prompt?
Owner explicitly wants no profession enumeration or infinite architectural rewrites. Clarified target: own Nox product shell, interface, then R3 transfer; ChatGPT/OpenCode are no longer required intermediaries for ordinary owner missions.

### D. Are tests automatic; stress?
Owner asked what Nox will learn, what tasks OpenCode set and if stress testing already launched. Answer: kickoff includes functional/regression and novel autonomous mission, NOT a quantified full stress test. Strategy includes hidden tasks, failure recovery, unseen tools, fresh-agent learning transfer, negative controls, equal-budget baselines. Don't misrepresent stress as included.

### E. Six acceptance criteria & anti-scope-creep rule
User explicitly insisted:
> Nox knows how to find and organize a profession, do work, remember positive results and repeat them, function autonomously without constant supervision, be a team member and someone one can rely on.
Agreed to test the six criteria and say "ready for UI" if verified. System not expected to know all professions out of the box; it needs **general method to acquire capabilities**.

### F. OpenCode plan verified
We checked recent recording at 16:32/16:33: P0 canonical artifact identity/revisions, QA correctness, general capability loop and an independent unknown-task trial planned. Direct recent activity supports moving toward generality; cannot claim outcome yet.

### G. Is architecture closed? 24/7 monitoring and OpenCode
Owner wants Nox extensible over time and eventually a separate permanently online monitoring agent, even when home computer off:
- **Nox Evolution** (future): cloud scheduler/event watcher, technology/model/tool/MCP/Skills/security update radar, qualification/tests, verified recommendations.
- **Update Manager** (future): staged testing, permissioned release, rollback; don't let Nox both change its own QA and certify its own safety.
- Independent cloud host required for offline-PC 24/7; can be scheduled checks, not perpetual expensive LLM session.
- **OpenCode as optional Nox coding executor/adapter**, not required core. The system must still work when OpenCode unavailable.
- **DECISION:** document these as future post-R3 enhancements, do NOT interrupt current OpenCode engineering or postpone handover to build them.
- Important distinction: capability/plugin updates are narrower and can be authorized via Capability Plane; updating core requires separate independent release policy.

### H. Request for schematic architecture + Prompt Master status
Two diagrams discussed:
1. Owner / future UI → Prompt Master → Head → Mission Manager → specialized teams → tools and Capability Plane; model routing, memory, QA, recovery supporting; future Nox Evolution external.
2. Owner request → Prompt Master clarification/spec/approval → Head plan → assess tool gap → acquire/replan if needed → Mission Manager delegate/execute → QA → correction or persist experience → deliver.
**Prompt Master confirmed IMPLEMENTED in original code**, `src/agents/prompt-master.ts`, typed spec, approval/hash binding; interactive clarification/edit loop still incomplete.
Current activity at 16:51 UTC changes Head plan type to `DelegationPlan | CapabilityDecision`, integration test in progress.

### I. Handover request
Owner requested full preservation of conversation wishes, agreements, OpenCode state, links, and a copy-paste prompt to move into a new ChatGPT conversation. Treat this file plus exact kickoff plus transition prompt as continuity anchors. Existing separate original OpenCode recordings still hold verbatim tool-session data. This handoff does not claim automatic verbatim capture of ChatGPT entire current dialogue.

## 7. Broader project historical context (chronological)

- AWE GROUP overall goal: universal self-organizing multiagent system, Head, specialists, LLM routing, QA, long-term memory, budgets, tools. Team roles in historical planning: owner Nox product/design/front; Yuri backend; Sasha marketing (not current sprint dependencies).
- Primary future real-world mission **CAREER-01** (headhunter): job-market research and applications, autonomous agents/browser and evidence; not a required specialization to implement before first generality acceptance.
- Earlier **E0** integrated PostgreSQL and proof/evidence: OWNER_ACCEPTED complete; not evidence of E1/Nox user autonomy.
- Earlier **E1** control plane and tools but failed to prove autonomous dynamic multiagent task completion, prompting OpenCode/Nox cleanroom development.
- Past data: OpenCode 2.2.6, WSL2 Ubuntu, Node/Python, Router.Cheap, several available providers. Router key budget once noted ~$9.98; **do not treat historical amount as fresh spendable balance**. No secret values anywhere.
- Prior Cortex data research: 4504 candidate tools, all UNVETTED; selection G0→G4, tests alone don't qualify tool. Skills must be authenticated/qualified.
- Historical observational tests included E1 OFFLINE 442 PASS and newer R0 snapshots; **must not combine with current R2 success claim**.
- Various discussions about stable GitHub archival across sessions. GitHub recordings/observer repos and main academy repo are sources of truth only with current fetch/readback.
- Focus remains first real bounded generality acceptance then UI and R3.

## 8. Instructions to the NEXT CHAT assistant

1. Begin by fetching this file, the exact owner kickoff, and the **latest** OpenCode session index/last records and Observer. Do not hallucinate real-time machine access. Use connected GitHub rather than generic web for private repo.
2. On first reply, brief summary of state, precisely grounded in newest timestamps. No new plan/research unless user requests.
3. Enforce six readiness criteria and scope-creep guardrail; **do not generate additional professions/core features simply to make a larger system**. No single-run smoke should be mistaken for complete acceptance.
4. After verified acceptance, say clearly: "Nox готов. Переходим к оболочке и передаче в управление владельцу." Initiate product UI and direct owner operating flow, not another development phase.
5. Keep evolving Nox Evolution, OpenCode adapter, cloud 24/7 in **future roadmap only**, not P0/R2 release gating.
6. Never claim all ChatGPT messages have been archived automatically; only contents of GitHub files / recorder can be claimed by verified readback.
7. Continue in Russian; respectful directness, insist on evidence.
