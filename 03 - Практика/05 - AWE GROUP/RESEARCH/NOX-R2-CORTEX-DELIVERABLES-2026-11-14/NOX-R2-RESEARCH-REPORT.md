# Nox R2 — финальный исследовательский отчёт

**Дата синтеза:** 2026-11-14 UTC. **Вердикт:** исследовательский пакет консолидирован и машинно проверен; **R2_NOT_ACCEPTED**, `CURRENT_NOX_UNKNOWN`, все G0–G5/T01–T12 `NOT_RUN`. Публикация в GitHub возможна только как **research/design snapshot с ограничениями**, не как доказательство работающего R2. Это не новый review OpenCode.

## 1. Решение и минимальный путь

Не создавать новую платформу. Соблюдать **REUSE EXISTING → CONFIGURE NATIVE → CONNECT READY-MADE → THIN ADAPTER → CUSTOM ONLY AFTER PROVEN GAP**. Порядок: fresh read-only Nox → G0 artifact/candidate/lifecycle correctness → G1 native granted ToolSearch на подтверждённом `@mastra/core=1.82.0` → G2 один owner-approved pinned read-only adapter → G3 один source/skill pack с held-out transfer → G4 typed route+complete ledger → G5 direct Nox T01–T12 с независимой приёмкой.

Консолидированный shortlist: **G0 без зависимости** (1), **native ToolSearch** (2), **один внешний proof по реальному gap**: MCP Inspector для локальной MCP-схемы, Docling для документа или Playwright MCP для browser mission — не все сразу; затем один Skill, Promptfoo/OSV/axe только как узкие QA helpers. Registry = metadata, не grant. Langfuse/ToolHive/LightRAG/Composio/Arcade/Inspect и оба Unslop не первый шаг. Полный ranked evidence: `RANKED-ACTIONABLE-SHORTLIST.md`, `solutions-shortlist.md`, `05-READY-MADE-INTEGRATION-ATLAS.md`, `13-BUILD-BUY-REUSE-MATRIX.csv`. Fastest path: `FASTEST-SAFE-INTEGRATION-PATH.md`, `16-FASTEST-SAFE-PATH-TO-R2.md`.

## 2. Четыре контура

- **A Tool/Capability:** NEED→DISCOVER→COMPARE/VET→EXPLICIT AUTHORITY→PIN/INSTALL sandbox→REGISTER/GRANT→DISCOVER ACTIVE→INVOKE→RECEIPT→independent QA→REUSE/REVOKE. Search/registry не permission; ToolCard хранит exact schema/digest/grants/egress/effects.
- **B Knowledge/Competence:** immutable KnowledgeRecord, SkillRecord, CapabilityPack и ActualExperience разделены; rights/ACL до index/prompt/cache; source anchors/freshness/retraction; transfer требует fresh-agent held-out evidence.
- **C Execution Strategy:** deterministic/program/API/bot/single/team/hybrid/BLOCKED на mission и step; model route отдельно; paired equal-budget comparisons, no forced winner.
- **D Controlled Improvement:** lesson не меняет runtime; knowledge/tool/skill/strategy/runtime имеют отдельные gates, expiry, rollback, no-benefit evidence.

Контракты и enterprise refs: `four-contours.md`, `09-AUTONOMOUS-TOOL-ACQUISITION.md`, `08-CONTINUOUS-KNOWLEDGE-SYSTEM.md`, `10-EXECUTION-STRATEGY-INTELLIGENCE.md`, `11-LEARNING-META-INTELLIGENCE.md`.

## 3. Минимальный R2 / R2.x / R3

**R2** — finite owner-approved полезный loop в названных низкорисковых профилях: immutable spec→bounded strategy→reuse/один vetted adapter→authorized action→полный CandidateEpoch/EvidenceBundle→independent QA→durable terminal→scoped reusable experience. Один vertical slice не принимает весь R2: все обязательные T01–T12 остаются в G5.

**R2.x** — повторяемые packs/домены, tenant transfer, Windows/new runtimes, более широкие visual/accessibility standards и route learning после отдельных proofs. **R3** — generalized profession graph, regulated authority, broad continuous learning/self-modification/fine-tuning. Их не удаляют из цели, но доказательно откладывают до accepted vertical loop; никаких новых orchestrator/vector DB/fine-tuning по умолчанию.

## 4. 4504 и расширенный поиск

Все **4504 исходные строки** сохранены в `03-COMPLETE-4504-REGISTRY.jsonl`: 1331+3173, raw JSON round-trip, IDs, pointers, aliases/groups, statuses, NEXT_TEST. Структурный validator PASS; duplicates не удалены. Это L1/H для каждой строки, **не полный per-row L2/L3/L4**. `SOURCE_HASH_MISMATCH` и archive bytes остаются UNKNOWN. Отдельно 32 значимых expanded candidate records в `04-EXPANDED-TOOLS-AND-SKILLS-REGISTRY.jsonl` (19 solutions + 7 knowledge + 6 evals), все L2/NOT_RUN. Подробности: `INVENTORY-AUDIT.md`, `inventory-validation-report.json`, `knowledge-report.md`, `evals-report.md`, `solutions-research.zip`.

## 5. Enterprise и Build–Buy–Reuse

42 evidence rows в `enterprise-evidence.csv` поддерживают contracts, host-enforced authority, discovery/execution separation, durable lifecycle, source-bound knowledge, simplest route и controlled eval. Vendor metrics не переносятся как Nox uplift. Сравнение: `06-ENTERPRISE-AGENT-COMPARATIVE-RESEARCH.md`, `enterprise-practices.md`. A–H/L1–L4 для 32 кандидатов: `13-BUILD-BUY-REUSE-MATRIX.csv`. `A` допустим только для scoped historical existing evidence; current compatibility остаётся UNKNOWN.

## 6. Испытания, независимая приёмка и rollback

`14-R2-ACCEPTANCE-AND-BENCHMARKS.md`, `validation-program.md`, `test-matrix.csv` задают frozen TR01–TR09, T01–T12, G0–G5, negatives, independent oracles, budgets и terminal semantics. Ни один тест здесь не выполнен. Каждый verdict привязан к current sealed epoch; product PASS ≠ mission ACCEPTED; late/stale receipt не принимает PAUSED mission; UNKNOWN effect не retry blindly.

12 небольших будущих tickets: `15-OPENCODE-EXECUTION-PACK/`, исходный `opencode-tickets.md`. Rollback: отключить/revoke новый adapter/pack/route, quiesce processes, удалить только derived index/config после reconciliation, сохранить immutable failures/evidence; external effects не считаются автоматически отменёнными. Все cost/calendar/uplift UNKNOWN до full ledger+invoice и paired independent measurement.

## 7. Фактические блокеры и GitHub readiness

Главные blockers: нет current Nox HEAD/status/hash/lock/call graph/receipts; owner не выбрал domain/oracles/experts/budgets/accounts; все runtime/security/transfer tests NOT_RUN; per-row upstream L2 для 4504 не завершён; full TCO UNKNOWN. Точные CQ01–CQ18: `CRITICAL-QUESTIONS.md`; разделы 0–22: `SECTIONS-0-22-AUDIT.md`; owner-only choices: `18-OWNER-DECISIONS-ONLY.md`.

**RESEARCH_PACKAGE_READY_WITH_EXPLICIT_LIMITATIONS** для GitHub как отдельный research snapshot; **NOT_READY_TO_CLAIM_R2 / NOT_READY_FOR_PRODUCTION_RELEASE**. Манифест с фактическими статусами, source, bytes и SHA-256: `DELIVERY-MANIFEST.md/.json`. Resume boundary: `resume.md`.
