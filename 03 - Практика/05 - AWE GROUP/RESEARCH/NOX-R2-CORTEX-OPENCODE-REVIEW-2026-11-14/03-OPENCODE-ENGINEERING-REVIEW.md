# NOX R2 — независимое инженерное ревью OpenCode

Дата: 2026-11-14. Статус: **REVIEW_ONLY; NOT_R2_ACCEPTANCE; NOT_IMPLEMENTATION**.
Прочитаны целиком соседние 01 и 02. Оригиналы не изменены.

## 1. Executive verdict

1. **R2 не принято и не реализовано этим документом.** Реалистичный минимум — последовательность end-to-end доказательств поверх Nox. Open-world competence — более широкая исследовательская программа, не одна настройка Mastra.
2. Финальный web-продукт получил 13/13 PASS для дерева `a71660c6…`, но миссия остаётся `paused`: `600111/600000 ms`, две repair iterations и unresolved intent `eb2f2fcc-a5b9-47f2-ab2e-0e2f971a0dfc`.
3. **Root-duplicate имеет конкретную причину:** `file_write` после nested write регистрирует `path.basename(safePath)` (`src/tools/index.ts:365–419`, строка 407). Путь `product/app.js` сопровождается регистрацией `app.js` в корне.
4. QA получает не более 6 артефактов по 12 000 символов и 6 000 execution output. Binding fail-closed coverage правилен; простое увеличение окна не создаёт полный evidence protocol.
5. Пять завершённых model calls сообщают subtotal 337 014 tokens; шестой UNKNOWN сообщает ещё 104 613. Полные tokens and dollars **UNKNOWN**. Нет controlled evidence против конкретной модели или за concurrency as universal fix.
6. Уже есть approved spec binding, grants, Linux isolation, checkpoints, lifecycle fences, artifact manifests, host model routing и finite deterministic oracles. Это не universal qualification.
7. Fast path: artifact/candidate/lifecycle correctness → grant-safe ToolSearch proof → pinned permission-safe adapter → source/skill transfer → strategy comparison → вся T01–T12. Новый orchestrator заранее не нужен.

## 2. Метод и признаваемые статусы

Прочитаны actual source files, manifest/lockfile, pinned Mastra typings/docs и retained summaries/logs/checkpoints/ledger/receipts. Nox clean at **68cc0ee20a25991ea275512e20ac521cc8f8234b** на initial и final readback; более новых commits в `r1/dev` не обнаружено. Это локальное readback, не утверждение о других hosts/remotes.

В этом review **NOT_RUN**: tests/build, missions/resume/repair, live models/browser/MCP, installs, deployment и publication. Все PASS — ранее сохранённая evidence. Полные hashes и paths: файл 05.

Исходные 4504 rows не читались как dataset этим review. Соотношение 1331+3173=4504 marked declared, independently reconciled UNKNOWN. Full inventory остаётся обязательным для Cortex, не подменяется этим forensic review.

**CODE_PRESENT / WIRED / OFFLINE_TESTED / LIVE_OBSERVED / ACCEPTED / RELEASED / UNKNOWN** не смешиваются. L1=found; L2=docs/code/license inspected; L3=isolated executable test; L4=independent equal-task uplift. Source/README reading not L3/L4.

## 3. Source-backed forensic table

Paths ниже — относительно `/home/nox/awe-group-cleanroom-20261112`.

| Область | Где / фактический статус | Пределы доказательства |
|---|---|---|
| Prompt Master/spec | `src/agents/prompt-master.ts:28–102` | WIRED/LIVE_OBSERVED typed model spec и immutable binding. Criteria не являются сами domain oracle; domain spec correctness не доказана. |
| Approval | `src/cli/index.ts:95–123`, `src/api/server.ts:287–359`, `src/utils/spec-binding.ts` | Explicit approve и change detection. Не blanket installation/deployment/external authority; production transport authentication не признаётся доказанной без отдельной проверки. |
| Head | `src/agents/head-agent.ts:10–155` | WIRED. Role/task/tool/parallel selection, no model-ID choice. Static prose/tool lists и environment paths не dynamic trusted registry. |
| Mission Manager | `src/agents/mission-manager.ts:2158–2725` | Stored plan, checkpoints, repair and real parallel batches через Promise.allSettled (`2256–2326`). **Неверно называть весь runtime serial**; web-trace содержал одну delegation. |
| Factory/specialists | `src/agents/specialists.ts:32–195,197–369` | Grant-filtered static allTools, delegated grants not widened. Tool/Skill processors не wired. Newly registered artifact+text required, но quality содержимого не доказывается. Default agent steps 15. |
| Recursion | `src/agents/recursion.ts:29–42,463–647` | WIRED/OFFLINE_TESTED: depth 3, total 12, max children/parallel 4, child steps 10. Конкретный web-run не использовал nested/parallel execution. Skill gain не доказан. |
| Browser/MCP | `src/config/mcp.ts:72–302`, `src/tools/browser.ts` | Lazy MCP discovery/wrappers/cancellation present. Model→MCP healthy live call не показан; trusted host QA использует отдельный Playwright test library. |
| Finite web QA | `src/agents/web-qa.ts`, `src/capabilities/web-product.ts` | Exact bytes, syntax sandbox, loopback/CSP/no-network и 13 checks. Не полный visual design/WCAG/security standard. |
| CSV/domain QA | `src/capabilities/csv-*`, `src/tools/csv-analytics.ts`, `src/agents/csv-qa.ts` | Separate bounded calculator/oracle. P1 equal-input lessons 7/7 both groups and no tool selection change; improvement zero, не negative proof for all learning. |
| Models | `src/config/models.ts`, `reports/r1-p1/evaluation.md` | Static role defaults + host allowlist/byRole/byAgent, nested route propagation. Task-sensitive quality/cost and actual supplier availability not proven. |
| Ledger | `src/utils/model-ledger.ts`, production call sites | Durable SDK invocation lifecycle; abort/missing leads UNKNOWN. Не полный transport retry/step invoice; same-role node attribution gap и dollars unreconciled. |
| Artifacts | `src/utils/storage.ts`, MM `540–763` | Hash/size/content integrity, scoped storage, provenance for same-name repair. Общий candidate all-files+registry epoch отсутствует. |
| Filesystem/tools | `src/security/workspace-fs.ts`, `src/tools/index.ts:365–439` | Linux descriptor nofollow, bounded IO, mission owner fence. Basename path loss — layout defect; trusted host relocation boundary remains. |
| Shell/resources | `src/security/shell-sandbox.ts`, `resource-limits.ts`, `src/utils/process-registry.ts` | Earlier real Linux bwrap/cgroup/prlimit evidence. Каждый новый runtime требует собственные negative/cancel/egress/resource tests. |
| Admission/qualification | `src/utils/qualification.ts`, `mission-admission.ts`, `src/config/mission-policy.ts`, `src/security/tool-context.ts` | Host policy, generation/revoke/effect fence, provisional qualification. Hash не authenticate issuer; store/policy trusted host boundary. |
| Recovery/budget | `src/agents/lifecycle.ts:145–459`, MM recovery/acceptance path | Cumulative elapsed, durable intent before effect, quiescence and explicit accept/retry. Timeout pause correct; unknown remote outcome not undone. |
| TI/Manus discovery | `src/tools/ti-search.ts`, `src/tools/manus-search.ts` | Bound read-only searches with grants. Current catalog health UNKNOWN, legacy 3415 != полные 4504; discovered metadata != executable/installed/granted. |
| Skills/competence | No native workspace/processor production wiring; thin lesson evidence | Role prompt ≠ Skill; наличие message history ≠ learned skill. General skill registry, live held-out transfer не доказаны. |
| Memory/PG | `src/memory/index.ts` | LibSQL message history 20 roles/50 mission; semanticRecall и workingMemory false. PG wiring/package не найден; working provenance/ACL knowledge base не показана. |
| API/observability | `src/api/server.ts`, logs/ledger/checkpoints/tree | Local management surfaces and durable evidence. Не hosted/product auth proof или complete billing statement. |
| Release | existing reports | R2/release/deploy not accepted, not executed here, known Nox remote push not claimed. |

Retained offline summary: **39/39 suites PASS**, 2026-11-14T00:11:52.954Z–00:19:22.735Z, isolated per-suite data (`reports/r1-local-web-followup/full-offline/summary.json`). P0 accepted ровно в пяти scope boundaries; не whole-R1 или professional readiness. R0 retained 252 files, manifest 55/55, tree `85b9030f8bcc8b91a438b8b65fa9bf1f7647887ac631537446e8ffc4ea72ee6b`. Historical failed/partial runs сохранены.

## 4. Фактическое объяснение PAUSED/PASS

| UTC | Действие | Evidence |
|---|---|---|
| 00:21:26.554–00:22:08.480 | Head | 6 748 reported tokens |
| 00:22:08.571–00:23:50.955 | coder, approved file tools | 121 529; four product artifacts |
| 00:23:54.216–00:24:10.353 | first QA | No verifier receipt, FAIL; 9 455 |
| 00:24:10.417–00:27:23.242 | repair 1 | 180 623; app rewrite, forbidden URL, root duplicate |
| 00:27:23.331–00:27:46.448 | second QA | stale receipt/tree, incomplete evidence; 18 659 |
| 00:27:46.511–00:31:17.489 | repair 2 aborted | outcome UNKNOWN, 104 613 reported |
| 00:31:17.508 | deadline | paused, checkpoint, repair in-flight |
| Later | trusted independent host verifier | exact new bytes 13/13 PASS, no mission state change |

In-mission FAIL относится к раннему tree `198243a173248fd3ca8e21ff5a2cea15bc14034bdbe908f2fd3ef25b46b223c5`, а post-timeout PASS к `a71660c6e6562f9542ed16013f4e24dedd3dcc179106ebc1bb9d72efe31ababe`. Это не противоречивые оценки одних байтов. Late pass не закрывает intent/current spec-bound review/terminalization.

Подтверждены: basename registration; дорогие serial generations; вызов LLM QA даже при deterministic blockers (`qa-agent.ts:135–190,211–227`); bounded coverage; отсутствие доказанного no-progress gate; correct timeout/unknown protocol. Они не означают, что отдельная модель «плоха». **441 627 = лишь observed arithmetic subtotal включая UNKNOWN call**, не полный usage и не счёт.

## 5. Integration tickets — только спецификация

### I-01: nested artifact identity

`src/tools/index.ts:402–409`: derive canonical workspace-relative artifact path после trusted assertSafePath, preserving `product/`; prove containment; atomic file+registration under existing withMissionWrite. `src/utils/storage.ts`: canonical ID/path/hash and old-record compatibility. `specialists.ts`: one unambiguous persistence instruction instead of duplicate save semantics.

NEXT_TEST: nested path once/no root copy, same basename в разных legal dirs, modification/provenance, traversal/symlink/cross-mission denial, readback. Оригинальные root duplicates не удалять. Rollback restores exact tool diff only; no history rewrite.

### I-02: candidate epoch and acceptance barrier

1. MM `1790,2341–2725` owns `{mission_id, specification_hash, plan_hash, epoch, complete_scoped_file_manifest, artifact id/revision/path/hash, lineage}`. Include reconciled/root artifacts явно; no hidden evidence.
2. `lifecycle.ts:145–170` gets versioned append-only candidate/review/recovery evidence. Model/thread id is not epoch; schema migration compatible.
3. Before QA: settle parallel writers; check lease/spec/admission; freeze exact bytes. Until review returns/stales, all mutation paths in tools/storage/tool-context deny production candidate writes. No single global boolean; preserve other tenants/read-only verifier.
4. `qa-agent.ts`: typed EvidenceBundle with every artifact name/hash and full coverage or bounded typed chunk/oracle coverage records. omissions and any evidence budget visible and binding. No blind prefix certification.
5. `web-product.ts:53–94` already freezes bytes for browser; additionally bind those bytes to approved mission epoch. `web-qa.ts` distinguishes ABORTED/BLOCKED from product defect and cannot accept late/stale result.
6. Recheck all current hashes+registry+unresolved intent+spec+admission+deadline immediately before fenced terminal write. Any changed snapshot invalidates review.

**ACCEPTED** требует current criteria PASS, exact same candidate, valid authority, settled/resolved lifecycle, complete review and durable terminal state in budget. New verifier PASS cannot override old failed lifecycle. **FAILED** allowable for definitive current defects with closed intent; **PAUSED/BLOCKED/UNKNOWN** for timeout, recovery or incomplete evidence. Hash proves binding, not issuer identity.

### I-03: deterministic preflight and scheduling

MM performs layout/declared path/integrity/dependency/current deterministic oracle checks before advisory model. `qa-agent.ts:138–166,211–227` may withhold unnecessary paid judgment when deterministic FAIL is already binding. Save reviews anyway for diagnostics optionally, не авторитарное override.

`lifecycle.ts:348–459` accounts remaining cumulative reservations for provider/tool/QA/recovery/terminal stages. Per-stage limits, quiescence and no-progress detection; no reset on resume and no covert deadline extension. If insufficient, honest pause/block. Repair bounded by meaningful expected correction, not unlimited retries. Existing parallel execution remains with global agent/cost budget and no parallel write race.

Tests cover >6 artifacts, >12k contents, root duplicates, changed bytes during review, old receipt, exhausted resume with zero model call, missing quota before terminal.


### I-04: native ToolSearchProcessor inside existing grants

Installed `@mastra/core@1.82.0` exports it from `@mastra/core/processors`. Local docs/typings confirm `tools`, `includeResolvedTools`, `search.topK/minScore/autoLoad`, `storage=in-memory|context`, `ttl`, filter arguments `toolName/tool/requestContext/phase` with search/load/active. Agent takes `inputProcessors`.

* `src/agents/specialists.ts:150–195`: fresh per-delegation processor, tools only `grants ∩ registered ∩ admitted actual toolSet`; `tools:agentTools`, `includeResolvedTools:true`, inputProcessors. All actual tool execute paths still run runWithToolContext, assertToolAllowed, withEffect and invocation ledger.
* Filter derives only trusted host RequestContext and applies in all three phases; model plan/skill/catalog content never becomes grants. Dynamic tool.id can differ from object key, so map actual resolved toolName. MCP/browser/memory implicit tools must not bypass with default unresolved=false behavior.
* Trial storage=context with real per-mission/node thread and retained messages. In-memory loses restart and anonymous default entries share state; context trimming deloads and requires rediscovery. On resume reconstruct authorized active tools, never reuse log as authority.
* AutoLoad may trade an extra turn for overloading matches; measure rather than assume savings. Native BM25 search is not 4504 normalization or install/vet pipeline. ti_search/manus_search remain only candidate discovery.

NEXT_TEST: correct known tool and schema/real invocation; distractors and ungranted candidate hidden/blocked at search, load and active; restart/trim/revoke/concurrent isolation; dynamic name mapping; equal-budget tokens/latency. **L1/L2 read only here; no Nox smoke.**

### I-05: one permission-safe external adapter

Thin adapter in `src/tools/`; stable id in `src/tools/index.ts`; proposed by Head but authorized by MM/tool-context. Record official release/source SHA/package integrity and independent artifacts digest, license, schema, runtime/network/accounts/secrets. Durable intent→invocation→artifact→independent oracle. Installation requires separate owner authority.

`src/config/mcp.ts:86–115,211–227` uses **unpinned `npx @playwright/mcp`**, not a direct dependency and absent from package-lock at this revision. Probe inherits full env (`96–100`); server environment is more restricted. Pin direct package exact version+lock integrity and record actual Chromium/MCP version compatibility; `@playwright/test` itself is 1.49.1. Review schemas and actual dynamic IDs before use. `npx` itself is neither safe installer nor sandbox.

Untrusted code runs in approved mission-limited files/process/network/secrets environment and tracked descendants. `disconnectPlaywrightMCP` swallows disconnect errors by design; telemetry should not overclaim remote/browser cleanup. Test missing/tampered package, wrong tool/schema, absent browser, unhealthy discovery, revoked grant/OAuth, malicious page/registry instructions, cancellation and unknown external effect reconciliation. No install/test was authorized/performed here.

### I-06: knowledge, Skills and transfer

* Keep existing LibSQL message memory. semanticRecall is off, so native retrieval is a separate experiment. Do not mandate PG/second memory. Embeddings/ingestion calls need own usage/privacy accounting.
* A KnowledgeRecord carries owner/version/edition/date/hash/license/trust/ACL/source anchors including page/figure/timestamp, contradiction, staleness, revoke. Enforce ACL before retrieval/content exposure. Fit actual ingestion candidate to formats instead of universal custom parser; Docling/Crawl4AI etc are Cortex comparison candidates, not preselected wins.
* Installed SkillSearchProcessor requires skill-enabled Workspace; supports topK/minScore/ttl/blockingRefresh and search/load instructions plus skill_read resources. It is not Nox sandbox or competence proof. Prefer pinned read-only LocalSkillSource. Scripts/assets undergo I-05. Skill allowed-tools is experimental requested syntax, not permission. Instructions remain untrusted prompt data.
* Versioned Capability Pack links sources, skill digest, adapter pins, role, when/when_not, grants requested (not self-issued), deliverable and oracle. version+hash+spec scope follows reuse/revocation. Skills do not upgrade provisional qualification.
* Compare baseline vs lesson/skill for changed inputs, then held-out variant with fresh agent/context, frozen criteria hidden from solver, equal budgets. Quality must come from independent executable/oracle/expert review, not text resemblance. Existing 7/7 lesson A/B gives no measured improvement and cannot be advertised as learning uplift.

### I-07: strategy/model selection

Extend host-only `src/config/models.ts` based on measured quality, not plan-provided arbitrary provider IDs. Keep selected-model consistency; augment per-node/transport retry ledger while preserved UNKNOWN costs.

Near approved spec→Head→MM add typed host-owned execution recipe: deterministic, program/new small script, CLI/API, workflow/service/bot, single LLM, multiagent, hybrid or blocked. Each versioned recipe binds input schema, allowed adapters, outputs, oracle, fail mode, cancellation and idempotence. Unsupported input returns BLOCKED not opportunistic broader authority.

Do not pay LLM for exact known deterministic repeat; do not claim all novel web generation can be deterministic. Existing finite CSV/web verifier is reusable. Measure single-agent/team/code/LLM hybrid under equal tasks/resources, with no-improvement as valid outcome. Parallelism may shorten wall time but increase cost/conflicts. Retain existing MM DAG until a concrete limitation justifies Mastra workflow or other integration.

## 6. Build–buy–reuse matrix (initial evidence only)

| Need | Verdict / evidence now | Shortest safe decision |
|---|---|---|
| Mission lifecycle/grants/leases | A bounded; retained 39/39, actual safe pause | I-01–I-03 hardening, not rebuild |
| CSV/web finite oracles | A only their specs, retained L3 | Reuse; add domain visual/accessibility/expert standards |
| Dynamic granted tool loading | B candidate L1/partial L2, no run | I-04 single pinned proof |
| 4504 normalized knowledge/index | D after true reconciliation | No head-only catalogue inference |
| New executable tool | C/D per candidate, UNKNOWN | I-05 thin adapter/vet/pin/sandbox |
| Playwright MCP lifecycle | D but unpinned, healthy live unknown | lock/compat/env/security tests |
| Native Skill loading | B/D L1–L2, no workspace smoke | Read-only pinned trial+transfer gate |
| Source/ACL knowledge system | E for first vertical slice | Existing evidence+chosen retrieval library |
| Competence registry and packs | E for first pack; narrow lesson only | Held-out independent domain trial |
| Models/strategy optimisation | E atop current calls | Typed sealed recipes + measured comparison |
| LibSQL chat memory | A code; broad use unknown | Reuse, no new DB by default |
| New scheduler/meta-framework/fine-tuning | G defer | Must prove current MM or model gap first |
| Managed integrations | H/G actual account/OAuth gap unknown | Research total API/secrets/TCO before choose |

## 7. Required NEXT_TEST matrix and R2 gates

NOT_RUN new checks:

1. Nested artifact identity/one record/provenance/legacy historical reads.
2. Full manifest/all artifacts/complete coverage including binary and budgets; no silent truncation.
3. Changes before/during/after review, released lock, stale snapshot and non-current verifier PASS.
4. Lease/admission/revoke/cancel before/during/after QA; all writes refuse at review candidate and terminal.
5. repair count/no-progress and aborted unknown recovery; explicit resolution/fresh review then only valid terminal status.
6. Exhausted cumulative resume invokes no head/specialist/route/tool; deterministic blocker avoids unnecessary paid review.
7. Dynamic tool search actual allowed invocation, negative unknown selection, identity/schema mismatch, thread isolation/revoke/restart/trimming.
8. Native adapters corrupted/missing dependencies, stale schema/OAuth revoked, network/no-secret, cancellation/cleanup, external effect unknown not duplicated.
9. Injection from sources/tools/skills/registry cannot escalate authority; secrets/source ACL/cross-mission memory filtered before exposure.
10. Ledger zero vs missing, retries/aggregation overlap and full cost unknown, acquisition/reuse per scoped pack evaluated in equal budgets.

**Gates P0→P6:** candidate/offline lifecycle tests; one deterministic+one safe tool-call proof; one new sandbox adapter; one knowledge/skill held-out pack; professional bounded web mission with real visual/accessibility acceptance; strategy+recovery+adversarial direct Nox; all T01–T12 complete. Each early gate is an integration proof, not whole R2 acceptance.

Any spec correction creates new version/new mission with failure retained. Exact product artifact PASS remains separate from mission acceptance.

## 8. Corrections to draft 01–22

| Draft section | What changes in standalone 04 |
|---|---|
| 0–3 | Finite R2 vs continued open-world research; correct Kortix→Cortex; no universal accreditation promise. |
| 1–2 | Fresh local HEAD/clean/pins/retained dates; separate old/current hashes and partial tokens; remote release not inferred. |
| 4 | WIRED/present/live separation; actual top-level parallel batching noted; concrete basename/QA/ledger root causes. |
| 5 | Full 4504 identities and source links mandatory; duplicate normalization loses never rows; counts to be freshly reconciled. |
| 6–7 | Unrestricted research breadth retained; exact installed Mastra contracts and unpinned MCP risk added. |
| 8 | Discovery, vetted adapter, installed version, health, grant, load, invoke, receipt, current QA, reuse/revoke are distinct. |
| 9–11 | Current LibSQL capabilities, source ACL before retrieval, versioned packs, held-out fresh agent and no authority from knowledge. |
| 12 | Existing DAG/parallel groups reused; typed recipes and total no-progress economics, no universal parallel/model claim. |
| 13 | Improvement experiment can show no gain; source/tool/skill strategy learning separated; expiry/revocation/fine-tuning not assumed. |
| 14–15 | Vendor research primary evidence/license/version/cost and actual compatible API; custom F only after proved native gap. |
| 16 | Exact code touchpoints+A–H/L1–L4; feasible increments under separate implementation auth. Calendar and cost UNKNOWN not invented. |
| 17 | T01–T12 retained; epoch/lock/accounting/adversarial negatives/direct Nox required. Product PASS != mission acceptance. |
| 18 | Cost per accepted result; research/build/run/maintenance distinct; UNKNOWN cannot become free. |
| 19 | No numerical research-agent/search/specialty ceiling, but execution/purchase/secrets/network/prod/git authority unchanged. |
| 20 | 18 output families with schema/reconciliation/provenance/failure preservation/readback; no arbitrary field constraints blocking rows. |
| 21–22 | Source→knowledge→practice→current QA closed-loop questions added. Research never automatically integration/deploy/release. |

## 9. Feasibility and owner-only decisions

OpenCode can start **without replacing the core** at I-01/I-03 then I-02/I-04/I-05 and one first competence pack. Seams are small but security-critical and each requires independent tests. Native API static reading reduces uncertainty, not integration risk. Calendar/cost **UNKNOWN** before adapter/provider smoke; do not fabricate estimates.

Critical risks: races between writes and QA; multi-domain criterion quality; untrusted supply-chain and web/skill content; unknown remote outcomes after abort; environment/resource isolation portability; prompt-tool selection costs; ledger not invoice; benchmark overfitting; professional domain review gap.

Owner decisions still needed for implementation phases, installs, external effects/releases, target domains and expert standards, provider budget within real limits, production authentication/tenancy and true release acceptance. Research freedom delegates none of these.

## 10. Readback boundary

Nox remained clean at `68cc0ee20a25991ea275512e20ac521cc8f8234b` after evidence reading. Docs checkout baseline `189851ff4195c5ad0003b60333f144c6d3ef8555`; remote main returned same SHA over HTTPS at review time. Original files remain. Manifest 05 records hashes and distinguishes local writing, Git commit and GitHub publication.

Standalone research brief: `04-CORTEX-R2-BRIEF-REVISED-BY-OPENCODE.md`. **No implementation, mission, new test, package installation, deployment, paid provider work or Nox Git mutation was performed by this review.**

