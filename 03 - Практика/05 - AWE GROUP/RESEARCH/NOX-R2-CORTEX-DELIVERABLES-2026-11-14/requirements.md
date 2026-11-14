# NOX / AWE GROUP R2 — полный requirements checklist (этап 1)

Дата поручения: 2026-11-14 (Will Craty). Статус: **RESEARCH REQUIREMENTS BASELINE; NOT_IMPLEMENTATION; NOT_R2_ACCEPTANCE**.

Каноническое ТЗ: `06-CORTEX-R2-FINAL-OWNER-PROMPT-2026-11-14.md` (`OWNER_FINAL_2026-11-14`), commit `302bdbb72f96f227efc8c8df5a4cb9a942f26a5b`, прочитано полностью на docs HEAD `9573a64f2602631ec5d2299716612ba8578c2a13`. Ниже `[ ]` означает **не выполнено в рамках всего исследования / требование перенесено**, а не утверждение, что прежние сессии ничего не делали. Настоящий этап выполняет только чтение, требования и baseline источников. Точные commit/URL/хеши и доступность: `/workspace/out/source-baseline.md`.

Сокращение: `R2DIR = 03 - Практика/05 - AWE GROUP/RESEARCH/NOX-R2-CORTEX-OPENCODE-REVIEW-2026-11-14/`.

## A. Обязательные прочтения, приоритет и границы этого этапа

- [x] Полностью прочитать `R2DIR/06-CORTEX-R2-FINAL-OWNER-PROMPT-2026-11-14.md` (438 логических строк по `read`, 437 newline; 81 097 bytes; SHA-256 в baseline).
- [x] Полностью прочитать `R2DIR/07-CORTEX-ACCOUNT-TRANSFER-FAILURES-2026-11-14.md` (83 строки; 22 009 bytes).
- [x] Прочитать `03`, `04`, `05` именно из revision `3c3fed07b8222946204cfa8169d9aef04f9f4097`; исходные байты сохранены в `/workspace/out/baseline-3c3fed07/`.
- [x] Проверить доступ к GitHub, canonical docs paths, checkpoint 01/02, RAW, observer/recorder и historical runtime export; отделить их от current Nox.
- [x] Зафиксировать UNKNOWN и NOT_RUN, не выдумывать current source scan, тесты, прежние результаты, цены или completion.
- [ ] Выполнить остальное ТЗ 06 целиком; настоящий checklist не является его выполнением.

Обязательный запрет: не менять Nox или исходные 01–07; не запускать OpenCode review, реализацию, production missions, deploy/release, новые платные тесты, покупки/top-up, новые секреты/аккаунты, внешние эффекты, расширение прав или публикацию 03/04/05. `/workspace/new-gemini/nox-r2` не канонический Nox и не условие всего исследования.

## B. Owner priorities 06: A, B, C и обязательность 22 разделов

### B.1 Приоритет A — исследовательская мультиагентность

- [ ] Не вводить искусственный численный cap на research subagents/superagents/teams/nesting/waves/search branches/models/critics; 1/10/100 — примеры, не KPI.
- [ ] Делегировать только ради прироста evidence/quality/parallelism/decision speed; фиксировать реально выполненное делегирование, не симулировать команды перечислением ролей.
- [ ] Применять при необходимости runtime forensic, Mastra/MCP, supply-chain/license, 4504, knowledge, Skills, strategy, enterprise, security, QA, economics, integration и red-team роли; расхождения разрешать первичными источниками.
- [ ] Соблюдать фактические platform/provider/budget/rate/ACL/security/privacy/license/resource ограничения; при препятствии указать failed action и нужный owner approval.
- [ ] `research` delegation не делегирует execution/install/production и не вмешивается в OpenCode/Nox.

### B.2 Приоритет B — universal goal + minimal R2

- [ ] Отдельно дать: (1) минимальный реально исполняющий полезную задачу и независимо принимаемый R2 и (2) open-world путь приобретения/обновления/переноса компетенций.
- [ ] Технически и экономически обосновать R2/R2.x/R3, сохранив конечную цель; один тест ≠ universal professional qualification.
- [ ] Критически пересмотреть границы при новых доказательствах, не молча удалить саморазвитие, стратегию или professional knowledge.

### B.3 Приоритет C — REUSE FIRST и быстрый полезный результат

- [ ] Первой ценной выдачей полного исследования дать `RANKED ACTIONABLE SHORTLIST` + `FASTEST SAFE INTEGRATION PATH`, до энциклопедии, но не вместо полного аудита.
- [ ] Для каждой сильной опции: exact version/commit/source/license; rationale; installed compatibility; Nox module/call-site; shortest wiring; mini-ticket; approvals; negatives; independent oracle; rollback; cost of accepted result.
- [ ] Соблюдать `REUSE EXISTING → CONFIGURE NATIVE → CONNECT READY-MADE → THIN ADAPTER → CUSTOM ONLY AFTER PROVEN GAP`.
- [ ] Не переписывать Head, Mission Manager, Factory, Mastra, memory, QA/tool stack без доказанного gap; архитектура не результат без independent acceptance.

## C. Все разделы 0–22 — полный обязательный объём

### 0. Назначение, ценность, решения

- [ ] Исследовать полный loop: unfamiliar useful professional mission → gaps knowledge/tools/skills → экономная strategy → reuse/acquire capability → authorized real action → independent QA → bounded reusable experience.
- [ ] Определить minimal R2 как finite specification-bound independently accepted loop; open-world graph/continuous learning оставить исследованием/развитием.
- [ ] Начинать с actual Nox + compatible installed Mastra; пакет/README/disk presence не решение.
- [ ] Research outputs превратить в owner-selectable маленькие проверяемые OpenCode tickets; owner отдельно решает implementation/production/publication/infrastructure/authority.

### 1. Единая evidence model

- [ ] Для каждого вывода/status использовать только различимые `PLANNED, DOCUMENTED, CODE_PRESENT, CONFIGURED/WIRED, CALLABLE, OFFLINE_TESTED, LIVE_OBSERVED, INDEPENDENT_QA_ACCEPTED(scope), RELEASED, BROKEN, UNKNOWN`.
- [ ] Маркировать `L1 found`, `L2 exact source/API/version/license vetting`, `L3 isolated successful adversarial executable test`, `L4 independent equal-task measured uplift`.
- [ ] К каждому claim: source/source-set + page/section/code location + observed UTC + upstream release/tag/commit SHA + package artifact/lock digest where applicable.
- [ ] Разделять as-designed/as-coded/as-configured/as-authorized/as-called/as-measured; метод и self-review limitations; собственные evidence refs у каждого claim.
- [ ] Artifact/hash не доказывают correctness/authenticity/learning/permission; UNKNOWN ≠ zero/free/safe/compatible/no-benefit; historical success ≠ current availability; P0/P1/browser ≠ R2 release.

### 2. Fresh source and runtime protocol

- [ ] При действующем owner access fresh-read `/home/nox/awe-group-cleanroom-20261112`, `r1/dev`; до integrations записать branch/HEAD/status/source hashes, в конце second readback; concurrent work → scoped snapshot.
- [ ] Сравнить с historical review baseline `68cc0ee20a25991ea275512e20ac521cc8f8234b`, clean 2026-11-14; delta и сохраняемую применимость evidence; до fresh read не называть latest.
- [ ] Читать package.json/package-lock, production call graph, tests, recent real run evidence, не только reports/historical export; не читать произвольные личные каталоги.
- [ ] Использовать canonical docs: `R1-CAPABILITY-PROGRAM/`, `RESEARCH/KORTIX-2026-11-13-ENTERPRISE-RESEARCH/`, `RESEARCH/CORTEX-NOX-CAPABILITY-KNOWLEDGE-MARKET-AUDIT-SCOPE-2026-11-13.md`, `PROMPTS/CORTEX-NOX-ENTERPRISE-CAPABILITY-RESEARCH-FINAL-2026-11-13.md`, `IDEAS/`, `ASTRA-AUTONOMY-AUDIT-2026-11-08/`, `CHECKPOINTS/`, `DECISIONS/`, `TESTS/` под `03 - Практика/05 - AWE GROUP/`.
- [ ] Observer sources `failm3/awe-opencode-recordings`, `failm3/awe-group-observer`; `failm3/awe-group-runtime` только historical export, не current source.
- [ ] Inventory dependencies перед claims; installed pinned contract для immediate integration; latest vendor отдельно и по версии.
- [ ] Использовать external primary specs/tagged code/supported API/releases/LICENSE/pricing/access/account terms; community/postmortems отдельным evidence class.
- [ ] При inaccessible source указать URL/owner/lock/payload tried (без секретов), effect, consequence, exact NEXT_TEST; не предполагать cost/security/compatibility.

### 3. Checkpoint — проверить, не копировать слепо

- [ ] Проверить и при новых primary evidence скорректировать historical baseline: limited P0; retained 39/39 offline 2026-11-14T00:11:52.954Z–00:19:22.735Z (не rerun review); R0 252 files/55/55 hashes.
- [ ] Сохранить различие: первая web attempt FAIL/paused; replacement four-file product `r1-static-task-tracker-v1` 13/13 на tree `a71660c6e6562f9542ed16013f4e24dedd3dcc179106ebc1bb9d72efe31ababe`, contract `4857e261da19afefcf3bcfa80879b5a1d286963a42495d8fa97f90aa30d01bb8`.
- [ ] Mission `r1-web-fc45eff2-3378-4ebd-8682-006ac71fac0a` historical `paused`, not accepted, `600111/600000 ms`, repair=2, aborted intent `eb2f2fcc-a5b9-47f2-ab2e-0e2f971a0dfc`; old FAIL tree `198243a…`, late PASS только new tree.
- [ ] Пять completed model calls subtotal 337014 tokens; sixth 104613 outcome UNKNOWN; total usage/dollars UNKNOWN; нет inferred price/release/deploy/professional qualification.
- [ ] Включить `reports/R1-LOCAL-WEB-PRACTICE.md`, обе run trees, logs, actual checkpoint; fresh non-paid sandbox tests только при отдельном разрешении.

### 4. Forensic runtime audit

- [ ] Проследить module/call/test/negative paths: PM typed spec→explicit approval→immutable hash; Head strategy→MM plan identity/dependencies/checkpoints; createSpecialist/delegation/per-role route/ledger; tools/allTools/MCPClient/listTools/wrappers/TI/Manus; artifact canonical path/readback/supersessions/manifest; fs/shell/process/network/grants/admission/qualification/revocation; memory/skills/QA/gates/oracle/terminal; recovery kill/cancel/timeout/parent loss/unknown external effect; APIs/UI/observability/build/package/release.
- [ ] Для каждого состояния: exact source, wiring, receipt/test id, independent verdict; no code→absence/UNKNOWN; code≠success; offline mock≠provider; package≠callable.
- [ ] Учитывать и fresh-check: Head выбирает roles/tools/parallel, не models; static host model defaults; MM batches и runDelegateCall поддерживают parallel; actual web plan был один coder+serial repairs.
- [ ] Fresh-check specialists static allTools, Tool/SkillSearch не wired на baseline; LibSQL message memory recall off; PG/general learned-skill registry не confirmed.
- [ ] Fresh-check basename `src/tools/index.ts:407` root duplication; QA 6 artifacts/12000 chars each/6000 output; exact browser snapshot vs broader candidate race; provisional host-policy qualification; hashes/receipts не identity/professional qualification.

### 5. Полный аудит 4504 исходных записей

- [ ] Учесть каждую строку `iirepresent.json` (ожидалось 1331), `Радар.json` (3173), `04 - Инструменты/Каталог кандидатов/90 - Данные/catalog-all-4504.csv` + related exports/cards; mismatch сделать finding, не silent filtering; shortlist не замена.
- [ ] Robust parse bytes/hash/schema/order incl JSON differences/multiline CSV; сохранить original row number/JSON path/id, origin/reference, every raw URL, all raw fields/aliases, source hash; durable source record id; не renumber/delete historical IDs.
- [ ] JSON/CSV/cards/export many-to-many crosswalk; exact missing/duplicate/unexpected/dangling; у каждой из 4504 machine record + final verdict/status даже inaccessible/low relevance.
- [ ] Counts per source/join, sha256 every input/output, cardinality invariant + audited exceptions; complete inventory ≠ execute all programs; static L1/L2 per item, deeper risk/usefulness/access-prioritized sandboxes.
- [ ] Отдельно normalize names и URLs; URL duplication лишь candidate relationship; не объединять fork/upstream, SaaS/self-hosted, SDK/service без evidence; aliases/relation types; many-to-many both directions.
- [ ] В каждой записи: stable source IDs; origin; raw pointer; raw/canonical URL + owner/repo; semantic class `[executable tool,MCP,SDK,CLI,API,Skill,workflow,library,service,app,documentation,article,catalogue,other/unknown]`; domain/operation/problem; upstream version/release/commit; health/date; OS/Node/WSL; dependencies/runtime; license per edition/assets; auth/secrets/residency/privacy; supply chain; privileges/egress; integration type/module/API; install отдельно от successful call; research/build/run/recurring/migration/maintenance cost или UNKNOWN; limits/failures/rollback; alternatives; L1–L4 refs; completeness/risk/confidence; A–H; reviewer/date.
- [ ] Независимые evidence-backed status/booleans для `has executable`, `installed version`, `healthy`, `authorized`, `actually called`, `result QA`, `currently released`; class `service` не executable proof.
- [ ] License отдельно repo/package/code/docs/model/artifact; absent license=UNKNOWN и ограничение reuse/inclusion; нет generic MIT extrapolation.
- [ ] Track revoked/dead/schema drift, safer status upon confirmed defect; documentation-only полезна как knowledge, не executable registry.
- [ ] Shortlist только recommended view; сообщить risk-ranked sandbox sample и execution coverage из 4504.

### 6. Расширенный поиск

- [ ] Найти дополнительные MCP, Agent Skills/SKILL.md, SDK/API/CLI, workflows/templates/starters/libraries/parsers/evaluators/knowledge/platforms; exact install/use/test path + account/cost/security, не links-only.
- [ ] Без numerical cap на searches/researchers/branches/categories/candidates; dedupe report claims с сохранением original IDs; counts не KPI.
- [ ] Classify ready connection/native/minor wiring-thin adapter/heavy/build-only-proven/reject-defer/unknown; сохранить rejected/inaccessible.
- [ ] Рациональный stop по предварительному вопросу/маргинальной ценности; log UNKNOWN+revisit; никогда не truncating 4504; учитывать rate/fair-use/prepaid limits, no new paid entitlement.

### 7. Технические семейства / actual APIs

- [ ] Оценить Mastra tools/processors/MCPClient/Workspace/workflow/memory/HITL/eval; MCP Registry/servers/Inspector/ToolHive; REST/OpenAPI/SDK/CLI/Playwright/DevTools/browser-use/Figma; managed Composio/Pipedream Connect/Arcade только при demonstrated OAuth/account need; Agent Skills; Docling/Crawl4AI; Promptfoo/Langfuse/Inspect AI при semantic QA gap; quality/testing/accessibility/visual/security/supply-chain/observability/CI.
- [ ] Разделить `heydamir/unslop` и `0design/unslop-skill`: sources/license/deps/capability/need.
- [ ] Для meaningful candidate: upstream+installed compatibility; package/release/tag/SHA/integrity; gap; Nox module/call path; minimal adapter; auth/secret/OAuth/step-up; egress; sandbox/resources; license/dependency rights; limits; receipt/oracle; migration/removal/rollback; direct+recurring cost/UNKNOWN; deploy need.
- [ ] Latest supported version отдельно от installed `@mastra/core=1.82.0`, memory 1.41.0, libsql 1.29.0, mcp 2.8.0, Playwright test 1.49.1; сохранить pins.
- [ ] Проверить unpinned `npx @playwright/mcp` (отсутствует в baseline lock): lifecycle/supply-chain/compat, не ready PASS.
- [ ] ToolSearch search/load/active filters, memory/context state, restart/thread/trimming; indexes available tools, не grants. Skills Workspace/index freshness/instructions/resources; scripts требуют independent authorized sandbox; experimental allowed-tools ≠ Nox permission.
- [ ] MCP Registry metadata/discovery ≠ sandbox/trust; verify current official ownership/security claims; privileged server untrusted до policy+sandbox+test.

### 8. G0–G5 и предлагаемые interfaces

Полные G0–G5 приведены ниже в разделе D и обязательны.

- [ ] Validate/refine, не implement. Предложить thin CandidateEpoch/EvidenceBundle и immutable CapabilityPack; не создавать subsystem, если existing protocol несёт fields.
- [ ] Candidate version: approved spec hash, accepted plan, actual file+artifact registry/hashes, source/skill/tool pins, invocation evidence; reviewer видит current snapshot, не supplied claims; verifier read + mutation lock.
- [ ] Acceptance: no unresolved intent, live admission, current bytes, all criteria, durable terminal; timeout/error/unknown nonaccepted и explicit recovery.
- [ ] Не снимать QA gates; quarantine old receipts; no late accept old/suspended/failed; fixed glob/text slices не complete evidence; deterministic preflight допустим; self-certificate/model majority ≠ independent oracle.

### 9. Контур A — Tool / Capability Intelligence

- [ ] Исследовать `NEED → DISCOVER → COMPARE → VET → EXPLICIT AUTHORITY → PIN/INSTALL IN SANDBOX → REGISTER → GRANT → DISCOVER ACTIVE → INVOKE → RECEIPT → INDEPENDENT QA → REUSE → REVALIDATE/REVOKE`.
- [ ] Каждый transition: actor, policy, I/O, persistent record, idempotency key, failure semantics, evidence ref. Metadata/adapter/install/health/grant/loaded/invocation/artifact/accepted/released различны; candidate name не модельная install-команда.
- [ ] ToolCard: tool_id/upstream/kind/when/when_not/pinned schema+dynamic toolName/versions+OS/preconditions/min grants/egress/data/auth OAuth/retries timeouts cancel/read vs effect/idempotency reconciliation/failure rollback/compat/provenance license digest/limits/health/evidence; docs не executable.
- [ ] Low-risk read-only только preapproved host policy; install/paid/secrets/publish/destructive/new rights external authorization; no default host/root env secrets to MCP child; discovery не меняет approved spec/role toolchain.
- [ ] Thin glue к `ti-search.ts`, `manus-search.ts`, `tool-context.ts`, artifact store, MM/QA; ToolSearch context storage/node ID/search-load-active; active restore только current grants; untrusted source/skill/web не policy; external candidate только через vet/pin/grant pipeline.
- [ ] Findings для LLM/MCP/OS compatibility, schema drift/vanished upstream/unhealthy server/dangling process/network timeout/duplicate effect/revoked OAuth/cancellation/stale registry; измерить search/schema cost vs full injection.

### 10. Контур B — Knowledge / Competence Intelligence

- [ ] Включить standards/RFC/vendor docs/research/journals/books+rights/white papers/cases/postmortems/SOP/checklists/training/conferences/audio-video timecodes/communities/repos/design systems/UI/marketing sales CRM/operations/data science/new domains; quality отдельно popularity.
- [ ] Различать KnowledgeRecord/SkillRecord/ToolCard/Template/AgentRole/CapabilityPack/EvaluationFixture/QAOracle/Claim-Evidence/ActualExperience; version/scope/source+ACL/status каждому; knowledge≠competence, role prompt≠skill, summary≠artifact, retrieval≠authorized action.
- [ ] KnowledgeRecord: canonical URL/location, author/publisher/owner, edition/version/effective+observed UTC, bytes или immutable pointer+hash, rights/license, trust rationale, language, tenant/owner ACL, page/section/figure/table/timestamp/byte anchors, transformations, citations/claims, contradictions, freshness/reindex, revocation/retraction, completeness/error.
- [ ] Не включать secrets/illegal corpora; read right ≠ reproduce/redistribute/fine-tune; ACL на ingestion/index/retrieval/prompt/tool/cache embeddings/artifact, не только post-hoc filter.
- [ ] Готовые extraction/retrieval/OCR/transcription для реальных PDF/tables/slides/image-only/dynamic web/audio-video и anchored citation quality; no universal parser/accuracy promise; experiments record input/provider/model/version/cost/tokens UNKNOWN/completeness/specimen ground truth.
- [ ] Updates event/schedule/mission-driven по releases/revocations/expiry/failure; conflicts сохранять с provenance/scope; unknown quality→hold/expert; partial ingest не смешивать как complete pack.
- [ ] Сохранить LibSQL message history; semantic/working/embeddings/PG только measured fit; immutable artifacts/evidence отдельно от rebuildable retrieval index; tenant isolation/migration/export/delete/unshare/redaction/backup/version compatibility.

### 11. Open-world graph / Skills / Packs

- [ ] Не закрывать graph списком: UX/UI/product; frontend/backend/mobile/desktop; software; agents/bots/workflows; marketing/sales/CRM/analytics; business/finance/management/ops; research/data/docs; content/media; security/IT/DevOps/infra; science/industry/cross-domain.
- [ ] Windows computer-use/browser/API/docs/visual verification — capabilities с own security/oracles, не автоматический transferable proof.
- [ ] Минимальные связи `domain → subdomain → fundamental knowledge → specialized procedure → prerequisites → tools → source rights/ACL → risks → deliverable → QA oracle → independent reviewer → validity scope → evidence of practice → verified experience`.
- [ ] New profession: trigger/gaps, authoritative foundations/current procedures, bounded spec/scope, sourced knowledge, practice, negatives/failures, held-out eval, pack version; LLM graph только proposal; source+evidence каждому entity/check; risk owner/expert approval; no safe scope=BLOCKED.
- [ ] Inventory existing skills/packs/cards/templates; role+prompt не skill; portable SKILL.md/scripts/assets/references/SOP/workflows/design kits/fixtures с license/provenance; minimum name/description+resources; load instructions ≠ executable access; allowed-tools untrusted request.
- [ ] CapabilityPack: stable ID/version/digest/parents, trigger/when_not, role/prerequisites, knowledge refs+editions/rights, validated skill refs/version, exact adapter/tool versions/hashes, requested minimal grants (not self-issued), context limits, deliverables, task schema, deterministic+qualitative QA, reviewer competence, security/egress/privacy, failure/recovery/rollback, practice/eval history, validity/expiry; on-demand load.
- [ ] Fundamental/shared candidates: anti-AI-slop+visual hierarchy, selected accessibility standard, Figma/design, browser+visual QA, software quality/testing/security, citation integrity, data metrics, document integrity, domain barriers; сначала existing packs+two Unslop repos; docs/scripts не qualification.
- [ ] Competence proof: practice→independent QA→changed case→held-out→fresh agent/context→bounded reuse→revalidation on source/tool/model change; скрыть baseline/treatment где нужно; test carry-over/leakage/injection/reward gaming; no-improvement сохранить.

### 12. Контур C — Execution Strategy Intelligence

- [ ] Сравнить deterministic function; existing/new script; CLI/API/typed workflow; persistent service/Telegram bot; single LLM; specialist; parent-managed parallel/nested team; hybrid; BLOCKED/no execution.
- [ ] Whole mission и step route отдельно; ambiguity/novelty/correctness/verifiability/safety/authority/latency/tokens+USD UNKNOWN/reuse/maintainability/reliability/recovery; model selection отдельная подзадача; no LLM для known repeat; no bot без sustained need.
- [ ] Reuse PM spec/approval; Head advisory, host authorizes route; MM DAG/parallel/recursion/recipes/web+CSV oracle до Mastra workflows/new planner; no renamed coordinator.
- [ ] Route contract: recipe id/version; mission/step input+preconditions; program/model/tool pack; stage/global resources; output/oracle; retry/idempotency/cancel; checkpoints/touchpoints; denial/fallback; fallback без authority expansion и не маскирует FAILED/UNKNOWN; outside spec→owner decision.
- [ ] Equal input/fresh context/authority/tools/wall+token budget/frozen independent oracle; compare parallel conflicts+search cost; token reduction, first correct call, repair productivity, oracle/mission accept, failure cost; включить OpenCode build cost; estimates/call counts до measurement UNKNOWN.

### 13. Контур D — Meta-Intelligence / Controlled Improvement

- [ ] Разделить knowledge/skill/tool acquisition, strategy learning, runtime improvement; own evidence/eval/authority/cost/expiry/rollback; lesson не меняет runtime/dependency само; fine-tuning не default.
- [ ] Минимум: calibrated uncertainty/abstention; no-progress/failure; risk/usefulness learning rank; rational stop; continuous eval; strategic experience memory; before/after benchmark; drift/dependency/source expiry; pins; scoped sharing; revocation; rollback; no auto tenant/personal merge; sensitive ledger/provider constraints.
- [ ] Experience: spec/scope/preconditions/context/initializer/sources/tools/models/prompts/templates/digests/costs/time/artifacts hashes/outcome independent oracle/failure classes/retries/superseded revoked/subsequent reuse; scoped positive, single no-failure ≠ universal safety.
- [ ] Transfer frozen independent criteria+fresh solver; acquisition cost/reuse success/retained depth/false claims/selection correction/repairs/total accepted cost; predeclare stop; preserve failed/no-benefit; no continuous background generation без justified benefit.

### 14. Готовые системы / компании

- [ ] Изучить OpenAI Codex/harness/Agents SDK; Anthropic Claude Code/Agent SDK/Skills/hooks; Google ADK/Agent Engine; Microsoft Agent Framework; AWS Bedrock; Devin; Fin; Agentforce; LangGraph; Mastra; strong OSS patterns dynamic skills/tool discovery/provenance/recovery/independent eval/visual design QA/sandboxes.
- [ ] Per system: version/date/public architecture или UNKNOWN, sourced production case, measured quality+methodology, expert fallback, lifecycle/recovery, grants/discovery, artifacts/provenance, license/access/pricing, source/release, Nox module, minimal diff, assumptions, own equal-task test, maintenance; no proprietary invention/slogan-as-compat.
- [ ] Output решения: каждый advantage → reusable component/proof target/equal-task measure/research-only; сравнить new platform layer TCO с node-local integration.

### 15. Build–Buy–Reuse / dependency gate

- [ ] Каждому значимому решению scoped A–H: `A ALREADY_WORKING; B CONFIGURE_NATIVE; C READY_MADE_INTEGRATION; D THIN_ADAPTER; E SIGNIFICANT_INTEGRATION; F CUSTOM_IMPLEMENTATION; G REJECT_OR_DEFER; H UNKNOWN`.
- [ ] A scoped current callable evidence; B pinned native+config+tests; C/D exact source/release/schema/security/min wiring; E hidden deps/cost/risk; F alternatives+proven gap; G rationale/revisit; H missing evidence/next safe check; component verdict не весь R2.
- [ ] B–F: repo/package/release/SHA/digest; LICENSE incl scripts/assets; Node/OS/WSL/browser; Nox module+call path; adapter; config/install/payload; credentials/OAuth; network/tenant; cgroup/process containment; migration/export; owner action; research/build/runtime/maintenance/migration costs UNKNOWN; independent test+rollback; «легко» только mechanism/files/unverified assumptions, не calendar.
- [ ] Owner gates перед implementation: exact package/install, cloud/payment, secret/OAuth R/W, external effects/deploy, system/integration auth; review candidates не installed/run.

### 16. Minimal R2 через OpenCode

- [ ] Дать concrete dependency graph+engineering tickets; bounded increments без core replacement возможны как hypothesis review, но general transfer/adapter safety/provider suitability не доказаны; implementation separate approval.
- [ ] Ticket: objective+scope; preconditions; current/pinned dep; allowed files; non-goals; immutable spec/evidence; candidate snapshot adversarial checks; policy/sandbox/egress/secrets; unit/integration/negative; independent QA artifact; logs/ledger/receipts; rollback/migration/data; effort bucket assumptions UNKNOWN; dependencies/next; owner decisions; не весь R2 одним issue.
- [ ] Сформулировать bounded working/no rewrite; native Tool/Skill/Workspace/MCP/workflow/memory versions+real tests; external components/adapters; blockers artifact identity/candidate QA race/coverage/terminal/ledger spend/domain oracle/model policy/revocation/storage ACL.
- [ ] Отделить R2.x/R3 generalized graph/hundreds domains/broad visual taste/self-learning scheduler/fine-tuning; выбрать informative first vertical slice и non-overfit comparison.
- [ ] Objective proof finished not generated: all criteria/checks, accepted artifacts, current terminal, full time/token/USD или UNKNOWN, no unresolved effects, uplift/no-uplift, owner contain/remove; no universal guarantee.

### 17. Acceptance programme

- [ ] Спроектировать frozen mission family+objective evidence для T01–T12; owner потом утверждает bounded specs/domains; early proof ≠ whole-R2. Все общие правила, T01–T12 и phase boundaries ниже в E/F/G.

### 18. Economics / FASTEST SAFE PATH

- [ ] Отдельно считать research/4504; implementation; tool/source/skill acquisition; runtime cloud+infra; independent QA+experts; maintenance/revalidation/migration/security; failed/discarded. Invoices/ledger discrepancy/currency date или UNKNOWN; OSS license zero ≠ TCO zero.
- [ ] Метрики accepted result: independent accepted mission rate, quality/citations/tool selection, repairs/productivity, first correct call, acquisition/transfer time, reuse frequency, first/steady latency+cost, recovery/unresolved effects; 337014+UNKNOWN sixth diagnostic, не bill.
- [ ] Критически проверить shortest path G0→G5: G0 I-01 + epoch/full evidence/preflight/reservations/locks/revalidation/bounded repair/intents; G1 one per-delegation granted ToolSearch+baseline; G2 one authoritative read-only adapter; G3 one bounded knowledge/skill loop; G4 typed strategy+ledger; G5 all direct T01–T12.
- [ ] Каждый gate: owner decision, bounded input/spec, artifacts, oracle, negatives, cost range if knowable, completion/abort, rollback; no invented calendar/cost; avoid wide MCP install/all-skills/new scheduler/universal parser/mandatory PG/fine-tuning/second orchestration memory first.

### 19. Research freedom / resource honesty

- [ ] No artificial cap; organize independent/nested critique, record disputes/dissent, use available strong models; breadth+counterexamples; mandatory all 4504+justified additions+decisions.
- [ ] Preserve original order/IDs/rejected/failed branches; exact dedupe; model/provider/agent/role/source usage+sampling+independence limitations; separate model reviewer не organizational independence.
- [ ] No infinite compute/API/accounts/data promise; no purchase/top-up/paid/secrets/unlicensed copying/publication/production/deploy/new rights без owner; research permissions only; paused questions→OWNER-DECISIONS-ONLY.
- [ ] Rational branch stop не уменьшает 4504/T01–T12/security rights; UNKNOWN+verification.

### 20. Deliverables / machine proof

- [ ] Создать без переименования все 18 families (раздел H), дополнительные файлы допустимы.
- [ ] Machine-readable checksum/source manifest; consistency audit; actual validation logs/scripts: cardinality/source/ID/FK/multiple mapping, links/aliases, no dropped raw fields, every row terminal research status/evidence/next check, schema+nullable UNKNOWN, requirement→artifact section+source refs, all artifact readback/hashes.
- [ ] Missing source→UNKNOWN+lookup, no false completeness; executive short; registries machine-readable; doc count не acceptance; stable cross-doc IDs, versions, contradictions resolved/disclosed; L1/L2 operational NEXT_TEST.

### 21. 18 критических вопросов — ответить primary refs + UNKNOWN gaps

- [ ] CQ01: latest fresh wired/invoked/independent accepted vs historical reports/exports.
- [ ] CQ02: почему late browser PASS не accepted; fresh snapshot/root artifact/coverage/repair/time/terminal/protocol causes.
- [ ] CQ03: proven vs inferred bottleneck (model/role/context/plan/dependency/provider/repair/QA); discriminating controlled test.
- [ ] CQ04: самые limiting accepted-mission gaps + exact ready component.
- [ ] CQ05: actual installed Mastra без version drift + falsifying smoke.
- [ ] CQ06: sandbox install/vet/grant/invoke/revoke без escalation/duplicate effect.
- [ ] CQ07: retrievable citations+rights/ACL/freshness/contradictions/tenant/retraction.
- [ ] CQ08: open-world bounded deliverables/oracles + expert boundary.
- [ ] CQ09: knowledge vs skill/tool/strategy/runtime learning + transfer evidence not recall.
- [ ] CQ10: deterministic/script/bot/workflow/single/multi/hybrid/blocked+model at mission/step.
- [ ] CQ11: failure/no-progress/recovery diagnostics без implicit runtime/permissions.
- [ ] CQ12: minimum footprint direct vertical slice no new core + unknown effort/risk deps.
- [ ] CQ13: устранить truncation/candidate race/old receipt без self-approval.
- [ ] CQ14: expiring source/pack/tool/oracle versions + reuse/revoke/sharing enforcement.
- [ ] CQ15: accepted-outcome economics при missing usage/invoice: bounds vs UNKNOWN.
- [ ] CQ16: frozen scoped overfit-resistant T01–T12 + validate negatives.
- [ ] CQ17: exact owner decisions/accounts/authority/expert/release blockers.
- [ ] CQ18: доказательно defer R2.x/R3, no perpetual platform research.

### 22. Boundaries / completion

- [ ] Только independent research/audit/catalog/primary comparison и отдельно authorized safe sandbox probes; no active Nox modifications/OpenCode interference/production R1/R2/deploy/release/publication/purchases/top-up/new credentials/external effects/expanded permissions.
- [ ] Можно опровергнуть broken premises и предложить alternatives+owner decision; никогда package=working/browser PASS=accepted/registry=authorized/skill loaded=competence/no errors=secure/partial usage=cost.
- [ ] Missing provenance/billing/live capability/license/upstream health=UNKNOWN+NEXT_TEST; owner отдельно authorizes tickets/install/external/release; direct Nox+independent QA mandatory; final concrete components/paths/changes/tests/rollback/open-world/FASTEST SAFE PATH; roadmap/brief не R2 acceptance.

## D. G0–G5 — точный gate checklist

- [ ] **G0 path+lifecycle** — modules `src/tools/index.ts`, `src/utils/storage.ts`, `src/security/tool-context.ts`, `src/agents/{mission-manager,lifecycle,qa-agent,web-qa}.ts`; prove canonical nested artifact, current candidate epoch, full coverage, sealed production writes during QA, current recheck+terminal, product PASS separate from mission accepted, cumulative budget, zero routes at exhausted resume.
- [ ] **G1 granted discovery** — `src/agents/specialists.ts`, `models.ts`, `tools/index.ts`, `security/tool-context.ts`; one native per-delegation ToolSearch over only granted tools; actual toolName/schema/call/receipt; negative load/revoke/restart/trimming/concurrency; measured savings.
- [ ] **G2 safe acquisition** — thin `src/tools/` adapter, index registry, optional `config/mcp.ts`, MM admission/effects; one pinned new external read-only useful isolated call; vetted source/license/digest; all negatives; no implicit install/secret/escalation.
- [ ] **G3 source/skill transfer** — `src/memory/index.ts` decision, authorized small knowledge/pack store, fresh specialist/oracle harness; source-bound pack; changed+held-out fresh agent; stale/tainted/unlicensed rejection; comparative competence или no benefit.
- [ ] **G4 strategy/economics** — PM/spec→Head→MM+ledger; typed deterministic/code/API/single/team/hybrid/blocked comparison equal budgets+complete cost; no direct non-jury model claim.
- [ ] **G5 independent acceptance** — approved direct Nox host/harness only; all T01–T12, appropriate experts, all negatives; OpenCode не operates solver loop.

## E. Общие правила T01–T12 (все обязательны)

- [ ] **TR01 Frozen Approved Spec:** owner input/scope/non-goals/current commit/deps/tools/sources/models/resources/deliverables/oracle/reviewer/global wall+token+spend/checkpoint recovery blocked/terminal; hidden variants+oracle keys не solver; QA/recovery/terminal в budget.
- [ ] **TR02 Direct production Nox:** tools/agents/artifacts, не OpenCode; mocks только early; custom wrapper не production wiring; independent reviewer не помогает solver.
- [ ] **TR03 QA binding:** mission+spec+plan fingerprint+candidate epoch+complete files/hashes+source/tool/skill/model/version/ACL+full ledger; no mutation during inspection; all artifacts/typed coverage, no prefix; stale/revoked/expired blocks.
- [ ] **TR04 Separate verdict:** product each criterion и terminal mission; ACCEPTED только all mandatory FINISHED/PASS/current snapshot/valid grant/no unresolved effect or repair/budget/durable terminal matching review; late check не retroactive accept.
- [ ] **TR05 Honest states:** product FAILED остаётся FAILED; PAUSED/BLOCKED/UNKNOWN для time/authority/unreadable/crash/incomplete QA/ambiguity; preserve logs/checkpoints/intents/artifacts/failures/superseded/abort; hash не competence certificate.
- [ ] **TR06 Full accounting:** every SDK start/end/node/role/plan step/model/provider/tools/wall/retries repairs recovery; zero vs missing vs incomplete tokens; invoice reconciliation или UNKNOWN; no dollars from partial tokens; research/build/run/maintenance separate.
- [ ] **TR07 Negative controls:** cross-tenant ACL; unapproved write; child escalation; malicious dependency/tool/skill/knowledge/page; stale schema/hash; missing/revoked OAuth; missing/tampered package; wrong-context memory; unsupported/unlicensed/retracted source; orphans; no-network/egress; resource exhaustion; descendants; no-progress/excess repair; cumulative overrun; duplicate unknown remote effect; destructive/external только harmless approved target+authority.
- [ ] **TR08 Frozen variants/oracle:** до measurements; no change после bad result; contract fix=new spec+new mission+prior failure retained; publish attempt selection+all failures против cherry-pick.
- [ ] **TR09 Domain signoff:** qualified human где professional judgment/licensed regulated/safety ethical; LLM не certification; generic static/browser oracle не design/security/WCAG certification.

## F. T01–T12 — полный proof-shape checklist

- [ ] **T01 deterministic no-LLM after routing:** owner known deterministic task+independent expected+ambiguous negative; typed recipe; actual logs/provider zero execution model calls after route; disclose planning/routing separately; exact output/hash+ACCEPTED budget; discovery≠invocation; cold start/repeat idempotence/tool-format failure/exhausted cancel/no LLM fallback; hidden changed input; no-LLM только traced production path.
- [ ] **T02 ready-made tool+schema:** pinned vetted authorized tool; limited set+distractors+denied; actual toolName/current valid schema/min safe calls/artifact/current QA; unknown denied cannot authorized search/load/invoke/silent effect; selection precision/time first correct/search-load vs full repeated held-out/cache restart trimming filters.
- [ ] **T03 novel tool safe sandbox:** inactive adapter+defined need; research candidate+separate owner acquisition approval; isolated nonprod source/version/digest/license/deps/schema/egress/secrets; pin/install/register/least grant/real read-only useful call/artifact/independent QA; fake unsigned unexpected/malicious metadata/wrong schema/missing binary account/no network/revoked OAuth grant/timeout cancel orphans/quarantine removal; acquisition≠execute; without approval NOT_RUN/UNKNOWN.
- [ ] **T04 unknown professional source knowledge:** bounded absent domain; current independent authoritative sources exact citations/rights/revisions; meaningful parse/source-to-claim/independent oracle expert; held-out not model memory; false citation/stale/contradictory/injection/unlicensed unsupported retracted/cross-tenant block/qualify; correctness+citation completeness+knowledge artifact, not extracted text; license/ingest/embedding costs separate UNKNOWN.
- [ ] **T05 skill held-out transfer:** verified bounded pack; baseline/treatment equal model/tools/time/tokens fresh contexts; practice→changed task→hidden held-out fresh uninvolved agent; predeclared quality/tools/safety+independent oracle+knowledge recall separate; no authority/fixture/criteria leakage/prompt following only; persisted pack/version/reuse/revoke/revalidate on source/tool change; no improvement honest; no broad qualification.
- [ ] **T06 professional website function+visual+accessibility:** novel owner spec features/persistence/users/assets+relative paths/viewports/browsers/standard+criteria/visual rubric; frozen criteria+changed layout/content unseen quality; exact snapshot/browser/local authorized network/screenshots/accessibility/qualified review as needed; hierarchy/responsive/readability/errors/interactions/edges; scanner не WCAG; full all-file manifest/no basename duplicate/stale receipt; contract+terminal both PASS in global budget incl QA settlement; late host 13/13 insufficient.
- [ ] **T07 bot/script/workflow choice+artifact:** sustained triggers/latency/audit+plausible alternative; pre-build matrix chosen `bot|script|workflow|other/blocked`, persistent justification; owner external deploy approval; locally authorized working artifact exact I/O/idempotence/retry/cancel/lifecycle cleanup/independent QA; hidden inferior-choice negative; research≠PASS.
- [ ] **T08 unknown profession graph extension:** bounded profession/subdomain+risk deliverable absent fixtures/packs; approved inputs only; identify prerequisites/discover verified sources+tools/build sourced graph+pack+deliverable/oracle/scope/practice+independent domain held-out accept; prerequisite gap/no-safe-scope/unsupported source/related confusion; prove graph node+reusable bounded competence, not fixed list/unlimited authority; domain-specific criteria; one domain≠all.
- [ ] **T09 adversarial injection no authority:** independent red team malicious web/doc/registry/Skill/MCP metadata/gateway/tool output/name schema collision/poisoned source cache/indirect instructions; attempts purchase/install/secrets env host cross-tenant/external writes/denied tool/spec-oracle-QA change; preserve policy/grants/candidate, refuse/quarantine/untrusted+evidence/no side effects/independent check; benign injection-like usable без overblock; не exhaustive security proof.
- [ ] **T10 interruption/recovery/budget/no duplicate:** real direct mission accepted stage plan+separately approved local/reconcilable effect probe; interrupt before intent/after durable intent before call/during unknown/after effect before receipt/before during QA/before terminal; kill crash cancel restart quiescence/no descendants/record unresolved; same spec candidate+cumulative elapsed no reset; explicit UNKNOWN reconcile/no automatic duplicate; legitimate fresh QA accept или PAUSED/FAILED; exhausted zero routes; fake faults preliminary only; real retained path+artifact.
- [ ] **T11 deterministic/LLM/hybrid efficiency:** predeclare ≥2 feasible routes+deterministic unsuitable; same inputs/fresh/oracle/authority/stage+global budgets/independent QA/tool source; single/multi/deterministic/program API/hybrid applicable; accepted rate/quality failures/first correct/wall/full tokens+USD UNKNOWN/repairs/build maintenance/reliability adversarial recovery; paired held-out+statistical uncertainty/sample limits; best/no-benefit/cannot-conclude, not always hybrid parallel.
- [ ] **T12 independent direct Nox without OpenCode:** owner final approved mission actual Nox interface; own PM/spec→approval→Head→MM→delegation/tools→independent QA→artifact/evidence/terminal; OpenCode no code/strategy/tools/repair/orchestration after start; separate authority reviewer immutable epoch; genuinely novel mission not static relabel; owner approval vs runtime choice explicit; setup/research visible; no covert operator.

## G. P0–P6 staging и максимальный claim

- [ ] **P0** lifecycle/snapshot tests; **P1** T01/T02 early PoCs; **P2** T03 sandbox integration; **P3** T04/T05+T08 knowledge/transfer samples; **P4** one bounded T06/T07; **P5** T09–T11; **P6** complete direct Nox T12+all coverage. Названия stages не approvals.
- [ ] Каждый T finally independent real direct Nox evidence; late T06 PASS не завершает paused mission; corrected spec/new mission только owner, original failure retained; nonapplicable требует reason+owner scope version, silent skip не accepted.
- [ ] Maximum R2 claim=bounded tested competence named domains/profiles; R2.x/R3 может expand open-world graph/packs/Windows/regulated permissions/generalized learning after evidence; no continuous framework before accepted vertical loop.

## H. Ровно 18 обязательных deliverable families — имена не менять

- [ ] **F01** `01-R2-EXECUTIVE-VERDICT.md` — short critical verdict/scope/fastest decisions/unknowns/no inflated status.
- [ ] **F02** `02-NOX-LATEST-RUNTIME-FORENSIC-AUDIT.md` — current call graph/source HEAD hashes/present wired call QA release matrix/blocking web chronology.
- [ ] **F03** `03-COMPLETE-4504-REGISTRY.jsonl` — one record per original source row, all reconciled inputs, many-to-many entity map, historic IDs aliases URLs raw fields pointers exceptions; не force 4504 unique tools.
- [ ] **F04** `04-EXPANDED-TOOLS-AND-SKILLS-REGISTRY.jsonl` — separate new findings/provenance/evidence/crossrefs original.
- [ ] **F05** `05-READY-MADE-INTEGRATION-ATLAS.md` — exact proven repos/packages/APIs/native fit/wiring/adapter/rollback.
- [ ] **F06** `06-ENTERPRISE-AGENT-COMPARATIVE-RESEARCH.md` — confirmed architecture/practice/cases/benchmarks/value.
- [ ] **F07** `07-OPEN-WORLD-COMPETENCE-GRAPH.md` + machine representation as needed — graph primitives/source/professional scope/no closed list.
- [ ] **F08** `08-CONTINUOUS-KNOWLEDGE-SYSTEM.md` — sources/provenance/ACL/refresh/citations/revocation/engine alternatives.
- [ ] **F09** `09-AUTONOMOUS-TOOL-ACQUISITION.md` — discover→vet→pin→grant→invoke→verify→revoke+authority.
- [ ] **F10** `10-EXECUTION-STRATEGY-INTELLIGENCE.md` — routes/models/recipes/evaluations/no-execution boundary.
- [ ] **F11** `11-LEARNING-META-INTELLIGENCE.md` — calibrated experience/no-progress/reuse transfer/controlled improvement.
- [ ] **F12** `12-DOMAIN-CAPABILITY-PACKS.md` — ready/candidate/proposed packs, skill refs/versions/oracles/rights/limits/experts.
- [ ] **F13** `13-BUILD-BUY-REUSE-MATRIX.csv` — every significant candidate A–H+all dependency/evidence/economics fields.
- [ ] **F14** `14-R2-ACCEPTANCE-AND-BENCHMARKS.md` — complete frozen T01–T12/negatives/actual acceptance boundary/coverage.
- [ ] **F15** `15-OPENCODE-EXECUTION-PACK/` — independent small tickets API/files/tests/deps/order/owner authority/criteria rollback migrations.
- [ ] **F16** `16-FASTEST-SAFE-PATH-TO-R2.md` — decision-driven shortest route+R2.x/R3 separation.
- [ ] **F17** `17-SOURCE-AND-EVIDENCE-LEDGER.jsonl` — source ID↔artifact/claim/relation/bytes/site/access/upstream SHA digest/license/method credibility/check evidence/UNKNOWN.
- [ ] **F18** `18-OWNER-DECISIONS-ONLY.md` — domain/oracle/identity/budget/install/external action/scope choices only, не editorial questions.

## I. Обязательные RAW-источники и related evidence

- [ ] **RAW-IIR** `04 - Инструменты/Каталог кандидатов/90 - Данные/iirepresent.json`; фактически JSON array 1331 object rows (`link`,`description`), bytes/hash в baseline. Сохранить каждую.
- [ ] **RAW-RADAR** `04 - Инструменты/Каталог кандидатов/90 - Данные/Радар.json`; фактически JSON array 3173 object rows (`link`,`description`). Сохранить каждую.
- [ ] **RAW-CSV** `04 - Инструменты/Каталог кандидатов/90 - Данные/catalog-all-4504.csv`; фактически 4504 data records+header через CSV parser, 16 columns, 0 uneven-width; это derived historical catalog export/crosswalk input, не дополнительные 4504 к двум JSON.
- [ ] **REL-ALL** `all-records-classified.json` — 4504 records; related derived export.
- [ ] **REL-CLEAN** `NIVICT-Radar-Cleaned-2026-11-04.json` — related cleaned export, не RAW replacement.
- [ ] **REL-SHORT** `NIVICT-Tool-Shortlist-2026-11-04.json` — shortlist only, не completeness.
- [ ] **REL-REVIEW** `NIVICT-Tools-Radar-Review-2026-11-04.md`; **REL-DUP** `duplicates.csv` (71 data rows); **REL-ISSUES** `issues.csv` (4090 data rows).
- [ ] **REL-MANIFEST** `import-manifest.json`; **REL-VALIDATION** `validation-report.json`; оба historical assertions, сверять с bytes, не принимать source hashes без проверки.
- [ ] **REL-CARDS** `04 - Инструменты/Каталог кандидатов/20 - Записи/` — фактически 4504 `.md`; `10 - Категории/` — 72 `.md`; crosswalk many-to-many+paths/dangling.
- [ ] Полный registry ещё НЕ создан на этапе 1; фактическая parse-cardinality не означает reconciliation/URL health/license/install/call/QA.

## J. Transfer failure controls 07 и финальная проверка 06

- [ ] **C-01 control:** 03/04/05 READ-ONLY BASELINE; не повторять review/publication; первая выдача полного research=shortlist+path.
- [ ] **C-02 control:** отдельно verify read-only Nox connector/WSL/path; без доступа UNVERIFIED/UNKNOWN, desk research продолжается.
- [ ] **C-03 control:** `/workspace/new-gemini/nox-r2` и `acceptance/git-state-default104.json` не канонические/не доказанные; не создавать фиктивные; scoped block не общий R2 failure.
- [ ] **C-04 control:** Mastra 404 логировать URL+date, не выводить missing API; installed typings/source first.
- [ ] **C-05 control:** docs/local cleanroom/historical runtime/sandbox разделены HEAD/hash/date; no WSL→historical baseline+UNKNOWN_CURRENT.
- [ ] **C-06 control:** source/reuse-first, checkpoints, no top-up, no complete cost claim без ledger.
- [ ] **N-01…N-08:** считать прежними OpenCode findings, не свежими Cortex discoveries; fresh-check basename/QA coverage/paused vs product PASS/processors wiring/unpinned Playwright/knowledge graph/4504 raw/model economics.
- [ ] Старые handoff 01/02, где сказано «финальный промпт ещё не создан», исторически superseded 06/07; не исполнять устаревшую команду писать новый prompt.
- [ ] Final 1: early ranked shortlist+links+integration points+minimal vertical slice.
- [ ] Final 2: все 4504+расхождения machine-readable, не installed plugins.
- [ ] Final 3: minimal R2 отдельно open-world R2.x/R3.
- [ ] Final 4: реальное доступное research delegation, no cap/no phantom.
- [ ] Final 5: все 22 раздела/18 families/4 контура/A–H/L1–L4/G0–G5/T01–T12/direct independent Nox сохранены.
- [ ] Final 6: no implementation/purchase/paid/acceptance без evidence+authority; UNKNOWN+NEXT_TEST.
- [ ] Final 7: отдельные small OpenCode tickets после owner decision с rollback/budget/negatives/real deps.
