# AWE GROUP / NOX — START HERE (актуальная передача)

**Дата:** 2026-11-13. **Событие:** R0 получен OpenCode в 01:56 UTC (04:56 МСК), первые tool calls зафиксированы в 01:57 UTC. Итог **ещё неизвестен**, передача Nox в эксплуатацию ещё NO-GO.

**Дополнение 02:11 UTC (05:11 МСК):** R0 продолжает исполняться; три реальных LLM-субагента подтверждены, базовые offline suite PASS, новая security-проверка пока 3 PASS / 1 FAIL; P0 release acceptance и final report не подтверждены. Проверенная текущая точка: [NOX-R0-LIVE-STATUS-2026-11-13-0211UTC.md](../REPORTS/NOX-R0-LIVE-STATUS-2026-11-13-0211UTC.md). Не запускать R0 повторно.\n
**Дополнение 02:23 UTC (05:23 МСК):** Security 4/4 PASS, 7/7 общих offline suite PASS, независимый QA исходной версии 14 PASS / 12 FAIL / 5 BLOCKED, основные Security+QA файлы интегрированы; Runtime patch ещё не принят, в 02:22 выявлены ошибки typecheck, в 02:23 запущены повторные проверки без подтверждённого результата. [Новый проверенный статус](../REPORTS/NOX-R0-LIVE-STATUS-2026-11-13-0223UTC.md). **R0 остаётся IN PROGRESS / NO-GO.**

**Новая исследовательская концепция (2026-11-13, без разрешения на реализацию):** [NOX-R1-CAPABILITY-LIBRARIAN-AND-KNOWLEDGE-SYSTEM-2026-11-13.md](../IDEAS/NOX-R1-CAPABILITY-LIBRARIAN-AND-KNOWLEDGE-SYSTEM-2026-11-13.md) — роль «библиотекаря» (Capability Broker), фундаментальные KnowledgeCards, versioned Skills/Recipes, mandatory conditional quality contracts, тестовая школа перед R2. **R0 не менять, R1 не запускать до owner approval.**

**R1 — новая рабочая программа по блокам (2026-11-13):** создан [единый реестр R1 Capability & Knowledge](../R1-CAPABILITY-PROGRAM/README.md), [правила статусов](../R1-CAPABILITY-PROGRAM/00-GOVERNANCE.md) и пакет **R1-01 Tool Gateway** ([спецификация](../R1-CAPABILITY-PROGRAM/01-TOOL-GATEWAY/SPEC.md), [ToolCard schema](../R1-CAPABILITY-PROGRAM/01-TOOL-GATEWAY/tool-card.schema.json), [кандидаты](../R1-CAPABILITY-PROGRAM/01-TOOL-GATEWAY/CANDIDATES.md), [QA контракт](../R1-CAPABILITY-PROGRAM/01-TOOL-GATEWAY/ACCEPTANCE.md)). Только проектные документы, **ничего не внедрено**; R0 не изменён. Следующая предметная работа — инвентаризация уже подключённых инструментов и окончательный выбор минимальных adapters в R1-01; блоки R1-02–R1-08 из реестра обсуждать и фиксировать последовательно.

**Market reuse research R1 (2026-11-13):** [проверенный по официальным источникам обзор Build vs Buy для всех восьми блоков](../R1-CAPABILITY-PROGRAM/RESEARCH/MARKET-REUSE-AUDIT-2026-11-13.md). Ключевой вывод: Mastra уже имеет ToolSearchProcessor, SkillSearchProcessor, MCPClient, HITL; Composio/Pipedream — готовые пользовательские API/OAuth; ToolHive — опциональный MCP sandbox; Docling/Crawl4AI — knowledge ingestion; Agent Skills + Promptfoo — процедуры/QA. Использовать готовое, писать минимальные адаптеры, не переписывать Nox. [OpenCode read-only inventory — только DRAFT, НЕ отправлен](../R1-CAPABILITY-PROGRAM/PROMPTS/OPENCODE-R1-READONLY-REUSE-INVENTORY-DRAFT.md). **R0 продолжается независимо, ничего не установлено, R1 не разрешён к исполнению.**

## Восстановление

1. **Полный master handoff:** [NOX-MASTER-HANDOFF-2026-11-13-R0-LIVE.md](./NOX-MASTER-HANDOFF-2026-11-13-R0-LIVE.md).
2. **Хронология нашего ChatGPT разговора:** [NOX-CURRENT-CHAT-CONTINUITY-2026-11-13.md](../CHAT-LOGS/NOX-CURRENT-CHAT-CONTINUITY-2026-11-13.md).
3. **Точно отправленное в OpenCode задание R0:** [NOX-R0-EXACT-SENT-TO-OPENCODE-2026-11-13-0156UTC.md](../PROMPTS/NOX-R0-EXACT-SENT-TO-OPENCODE-2026-11-13-0156UTC.md).
4. **Аудит пяти P0 / NO-GO:** [NOX-OWNER-READINESS-REVIEW-01-2026-11-13.md](../REPORTS/NOX-OWNER-READINESS-REVIEW-01-2026-11-13.md).
5. **Исходный frozen acceptance draft:** [AWE-ARCHITECTURE-ACCEPTANCE-PLAN-2026-11-12.md](../TESTS/AWE-ARCHITECTURE-ACCEPTANCE-PLAN-2026-11-12.md).
6. **Идея владельца — обязательные профессиональные плагины/Unslop:** [NOX-MANDATORY-PROFESSIONAL-CAPABILITY-PACKS-CONCEPT-2026-11-13.md](../IDEAS/NOX-MANDATORY-PROFESSIONAL-CAPABILITY-PACKS-CONCEPT-2026-11-13.md).

## Ссылки на внешние инженерные следы

- [OpenCode Session Recorder — latest](https://github.com/failm3/awe-opencode-recordings/blob/main/LATEST.md)
- [Observer — latest](https://github.com/failm3/awe-group-observer/blob/main/LATEST.md)
- [Issue #14: NOX-R0](https://github.com/failm3/awe-group-runtime/issues/14)

## Следующая работа

При запросе «проверь OpenCode» сначала посмотреть новые minute logs после **01:58 UTC** и фактическую работу дочерних агентов, diffs, тесты, лимиты и статус R0; не повторно запускать задание. Потом принимать решение о R1 Tool Gateway. R1, большой платный стресс и внедрение Unslop **ещё не разрешены в рамках R0**.

**Принцип:** только проверенные tool calls, artifacts, hashes и независимый QA являются evidence. Запись в GitHub и запуск сессии сами по себе не доказывают готовность.
