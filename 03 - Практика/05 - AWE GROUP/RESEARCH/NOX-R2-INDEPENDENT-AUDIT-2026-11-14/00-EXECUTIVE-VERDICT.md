# Nox / Cortex — независимое инженерное заключение

Дата: 2026-11-14  
Статус: **READ_ONLY_AUDIT / STRATEGY_ONLY / NOT_IMPLEMENTATION / R2_NOT_ACCEPTED**

## Решение

**Nox нужно развивать, а не переписывать.** В нём уже реализован нетривиальный контур: структурированная спецификация и явное approval, Head, последовательные и параллельные делегации, рекурсивные специалисты, deny-by-default permissions, Linux isolation, checkpoints, durable intents, recovery, artifact integrity, независимый LLM QA плюс обязательный deterministic gate, bounded repair и durable model-call ledger.

Но сейчас Nox — **расширяемый bounded runtime, а не доказанный универсальный профессиональный агент**. Ни один из G0–G5 или T01–T12 не выполнен как программа R2; текущий runtime в этом аудите не перезапускался. Сохранённые 39/39 offline PASS, одна корректная CSV-миссия и отдельный web product PASS не равны общей приёмке.

**Cortex следует принять условно как research/design базу, но не выполнять OC-01…OC-12 механически.** Наиболее ценны его evidence discipline, negative controls, independent oracles, G0-first и reuse-first. Метаданные пакета местами противоречивы, а последовательность разработки нужно изменить: раньше измерить пользовательский outcome, не откладывая весь direct-Nox baseline до конца G4.

## Самые важные факты

1. **Artifact identity повреждена архитектурно:** `file_write` регистрирует basename вместо mission-relative path; одинаковые имена в разных каталогах не получают независимых canonical identities (`src/tools/index.ts:402-409`, `src/utils/storage.ts:445-469`).
2. **QA не связано с immutable reviewed candidate.** Есть сильные hash/size/final revalidation checks, но нет единого CandidateEpoch/EvidenceBundle и сравнения terminal candidate с тем, который видел reviewer (`src/agents/qa-agent.ts:87-112,146-166`; `src/agents/mission-manager.ts:2639-2651`).
3. **Ограничение evidence fail-closed, но неполно.** QA получает максимум 6 артефактов × 12 000 символов и 6 000 символов execution output. Это не silent PASS: неполнота становится critical defect. Однако полноценного пути проверки больших/binary deliverables нет.
4. **Деньги и полные tokens неизвестны.** Ledger честно сохраняет UNKNOWN, но `execution.totals` суммирует только top-level delegations и не включает Head, QA, repairs и descendants (`src/agents/mission-manager.ts:2653-2683`). SDK invocation ≠ HTTP retry ≠ invoice.
5. **Browser/MCP нельзя считать квалифицированным.** Используется unpinned `npx @playwright/mcp`, общий process singleton, нет эквивалентного shell containment/egress policy; wrappers части tools используют `selector`, тогда как проверенный pinned Playwright MCP 0.0.85 требует `target` (`src/config/mcp.ts:86-100,171-227`; `src/tools/browser.ts:328-380`).
6. **ToolSearch, общий MCP registry, Skills/plugins lifecycle, Windows computer-use и профессиональные packs отсутствуют.** Наличие зависимости или research metadata не означает working capability.
7. **Память не равна learning.** LibSQL подключён, semantic/working recall выключены; общий retrieval и ACL отсутствуют. CSV lesson fixture доказывает scoped reuse QA checks, а сохранённый paired result — нулевой correctness/tool-selection delta, не uplift.
8. **Реальная практическая ценность уже есть, но узкая.** CSV arithmetic одного run проверена независимо; web tree получил 13/13 product checks, но обе web missions остались `paused`, `accepted:false`. Product PASS не меняет mission verdict.

## Собственная стратегия

### Этап A — воспроизводимый baseline и ранний direct-Nox smoke

После отдельного разрешения на выполнение: typecheck/offline suites, затем одна новая low-risk bounded миссия через нормальный Nox loop с независимым collector/reviewer. Измерить accepted/paused/failed, wall time, repairs, unresolved intents, tokens/UNKNOWN и USD/UNKNOWN. Это diagnostic smoke, не R2 acceptance.

### Этап B — P0 correctness до расширения возможностей

1. Canonical nested paths и monotonic artifact revision; legacy records не переписывать.
2. Versioned immutable candidate manifest: spec/plan hash, все artifacts, revision/path/hash/size/provenance.
3. Typed EvidenceBundle: полный manifest и complete text chunks либо независимый binary/domain oracle; verdict содержит candidate hash.
4. Mutation/stale review/unresolved intent до terminalization → ноль ACCEPTED.
5. Deterministic FAIL до paid QA; no-progress fingerprint; отдельные завершающие reservations.
6. Ledger-derived whole-mission projection с per-node/delegation/retry identity; UNKNOWN не превращать в ноль или нулевую цену.

### Этап C — управляемость и минимальный routing

Добавить clarification/edit loop до approval, явный `PLANNING_FAILED/BLOCKED` вместо молчаливого generic fallback, простой host-owned route contract (deterministic/program/API/single/team/hybrid/BLOCKED) и минимальный operational trace view. Не создавать второй orchestrator.

### Этап D — два прикладных vertical slices

1. **Repository patch:** exact fixture commit → исправление → независимо применённый patch → failing test PASS и control PASS, без host `.git`/secrets.
2. **Documents:** authorized PDF/DOCX с таблицей → cited report и настоящий DOCX/PDF → независимый reader сверяет содержимое и anchors. Сравнить Docling/MarkItDown на gold fixture; не выбирать заранее.

Затем browser/multimodal hardening, ещё один формат analytics и один draft-only external API effect с host-held secret, idempotency/reconciliation.

### Этап E — расширение только по измеренному gap

- ToolSearch: paired equal-budget test против static granted subset; допустим результат `NO_BENEFIT`.
- Playwright: сначала pin, schemas, per-mission isolation, egress/process/cancel/cleanup; не добавлять второй browser stack без необходимости.
- Skills/knowledge: один immutable source-bound pack, ACL до retrieval, held-out fresh-agent evaluation.
- Langfuse: только optional exporter; Temporal/LangGraph/PostgreSQL/vector DB — только после доказанного непокрываемого требования.
- Windows computer-use: отдельный controlled broker/VM и threat model, не быстрый аналог Linux shell.

## Ожидаемый эффект — прогноз, не результат

- Меньше ложных или недоказанных terminal verdicts и однозначная связь результата с проверенными bytes.
- Полная атрибуция attempts/tokens и честная экономика без выдуманных USD.
- Меньше бесполезных paid QA/repair вызовов и ранняя видимость основных failure classes.
- Два проверяемых профессиональных workflow вместо утверждения универсальности по числу ролей/tools.
- Меньше supply-chain, cross-mission browser и learning/ACL рисков.

Численный uplift, сроки, стоимость и общая mission success rate остаются **UNKNOWN** до paired runs.

## Решения владельца, необходимые перед реализацией

1. Разрешение на baseline tests и первый diagnostic direct-Nox smoke; отдельно — на engineering changes.
2. Первая полезная mission, non-goals, independent oracle/reviewer и допустимые external effects.
3. Численные budgets: wall time, tokens/USD либо допустимый UNKNOWN, repairs/no-progress, agents/parallelism, resources.
4. Scope R2: обязательные T01–T12 и явные BLOCKED/OUT_OF_SCOPE; smoke не считать final acceptance.
5. Отдельные approvals на acquisitions/install/call/egress; никакого blanket install.
6. Model policy и invoice/USD reconciliation requirement.
7. Single-user trusted-host scope или требование multi-tenancy; последнее требует tenant isolation до exposure.
8. Evidence retention/redaction, publication/deployment authority.

## Итоговая формулировка состояния

> **SUBSTANTIVE_EXTENDABLE_RUNTIME / CURRENT_RUNTIME_NOT_FRESHLY_VERIFIED / PROFESSIONAL_SCOPE_NARROW / R2_NOT_ACCEPTED.**  
> **Cortex: RESEARCH_PACKAGE_INTEGRITY_PASS / RESEARCH_DEPTH_PARTIAL / EXECUTION_PACKAGE_REQUIRES_CORRECTION.**

Следующий допустимый шаг — не массовое внедрение каталога, а владельчески разрешённый baseline и малый P0 correctness slice. Данный аудит на этом останавливается; реализация не начата.
