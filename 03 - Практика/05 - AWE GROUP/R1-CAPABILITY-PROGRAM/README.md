# AWE GROUP / Nox — R1 Capability & Knowledge Program

**Единая точка входа.** Дата открытия: 2026-11-13.  
**Статус программы:** SPECIFICATION_IN_PROGRESS; **NOT R1 RUNTIME EXECUTION**.  
**Основная цель:** после закрытия P0 R0 научить Nox получать нужные знания, выбирать и безопасно выполнять действия подходящими инструментами, независимо проверять результат и передавать пользователю рабочий продукт.

> **Граница:** не перезапускать R0, не менять работающий OpenCode, не устанавливать плагины или MCP, не выдавать доступы, не запускать платные проверки и не модифицировать production runtime на основании этих документов. Владелец сейчас авторизовал **структурирование и подготовку блоков**, не внедрение R1. Не смешивать OpenCode build-plane и Nox runtime-plane.

## Сначала исходники Nox — приоритет над market scan

**Проверенный source audit (2026-11-13):** [что уже реализовано в локальном Nox](./RESEARCH/NOX-IMPLEMENTED-CAPABILITIES-SOURCE-AUDIT-2026-11-13.md). В `package.json` уже присутствуют Mastra 1.82.0 / MCP 2.8.0 / memory 1.41.0 / libsql 1.29.0 / Playwright. В коде есть Prompt Master (`createSpecification`), Head, `createSpecialist`, рекурсивное делегирование, MCPClient и браузерный adapter, файлы/shell/web/TI, Mission Manager и QA. **Запрет рекомендовать эти компоненты как новые установки**. Все market options ниже — только conditional gap candidates после проверки финального R0 SHA и реального missing capability.

## Проверка рынка — обязательная входная точка перед реализацией

[MARKET-REUSE-AUDIT-2026-11-13.md](./RESEARCH/MARKET-REUSE-AUDIT-2026-11-13.md) — проверенные по официальной документации готовые варианты для всех R1 блоков: Mastra built-ins, Composio/Pipedream/Arcade, ToolHive, Docling, Crawl4AI, Agent Skills, Promptfoo, Langfuse и др. **Текущая стратегия: сначала использовать готовое, затем писать только недостающий glue-код.** Реальных установок или проверки совместимости в Nox не было.

## Каноническая структура

| ID | Блок | Что производит | Статус разработки документа | Статус внедрения |
|---|---|---|---|---|
| R1-00 | [Правила, определения, статусы](./00-GOVERNANCE.md) | Правила, критерии, единый реестр | DRAFT_READY_FOR_REVIEW | NOT_APPLICABLE |
| **R1-01** | [Tool Gateway / Capability Broker](./01-TOOL-GATEWAY/SPEC.md) | ToolCard, scoped grants, adapters, invocation receipt | **DRAFT_READY_FOR_REVIEW** | **NOT_STARTED** |
| R1-02 | Knowledge System | KnowledgeCard, source ingestion, provenance, scoped retrieval | NOT_STARTED | NOT_STARTED |
| R1-03 | Skills & Recipes | Версионированные SOP, инструкции, примерные действия и ошибки | NOT_STARTED | NOT_STARTED |
| R1-04 | Professional Capability Packs | Task templates: знания, обязательные способности, проверки | NOT_STARTED | NOT_STARTED |
| R1-05 | Agent Factory Integration | Выдача ограниченных capabilities агентам, отзыв, рекурсия | NOT_STARTED | NOT_STARTED |
| R1-06 | Independent QA / Evals | Независимые тесты выбора/вызова/результата и антислоп QA | NOT_STARTED | NOT_STARTED |
| R1-07 | OpenCode Engineering Toolkit | Изолированные инструменты **разработчика** Nox, не Nox как пользователя | NOT_STARTED | NOT_STARTED |
| R1-08 | Pilot Missions / School | Реальные задания без OpenCode как оператора, R2 readiness | NOT_STARTED | NOT_STARTED |

**Важно:** названия R1-01…R1-08 — идентификаторы **новой программы интеграций**, они **не перенумеровывают** существующие архитектурные блоки 01–05 AWE GROUP.

## Рабочий порядок

1. Берём **один** блок, читаем его контракт и существующие источники; не начинаем большой рефакторинг.
2. Inventory: какие возможности уже реально присутствуют в Nox/OpenCode/Mastra/PG, а какие — только кандидаты или текст.
3. Конкретный выбор: готовый сервис/встроенный адаптер/минимальный glue-код; решение с аргументами и рисками.
4. Фиксируем схемы, права, типы событий, version pins, negative tests и критерии DONE.
5. После отдельного разрешения и завершения R0: изолированный smoke test реального подключения, воспроизводимая интеграция, independent QA, commit+readback.
6. Обновляем **одну таблицу статусов здесь**, связываем тесты и evidence по SHA; только затем открываем следующий блок.

**Статусы документов:** NOT_STARTED → DRAFT_READY_FOR_REVIEW → OWNER_APPROVED → IMPLEMENTATION_READY.  
**Статусы исполнения:** NOT_STARTED → IMPLEMENTING → CONNECTED_UNVERIFIED → INTEGRATION_PASS → INDEPENDENT_QA_PASS → RELEASED; также BLOCKED/FAIL/PARTIAL.  
**Вердикт R1:** пока ни один runtime-блок не имеет статуса PASS или RELEASED.

## Первый выбранный блок — R1-01

- [Спецификация Tool Gateway](./01-TOOL-GATEWAY/SPEC.md)
- [ToolCard JSON Schema v0.1 (draft)](./01-TOOL-GATEWAY/tool-card.schema.json)
- [Очередь реальных кандидатов и источники](./01-TOOL-GATEWAY/CANDIDATES.md)
- [Контракт независимой приёмки](./01-TOOL-GATEWAY/ACCEPTANCE.md)

Начальный pilot: 1 Head / 1 child → поиск capability в существующей TI → проверка утверждённого адаптера → ограниченный grant → реальный вызов → receipt → артефакт → независимый QA → отзыв. Все шаги должны быть реальными, не simulated tools.

## Первичные источники (история проекта)

- [Аудит 4504 кандидатов](../02%20-%20%D0%90%D1%83%D0%B4%D0%B8%D1%82%204504%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2.md) — screening, не подключённые tools.
- [Владелец: готовое прежде самописного](../%D0%90%D0%9A%D0%A2%D0%A3%D0%90%D0%9B%D0%AC%D0%9D%D0%9E%20%E2%80%94%202026-11-11%20%E2%80%94%20%D0%BF%D1%80%D0%B8%D0%BE%D1%80%D0%B8%D1%82%D0%B5%D1%82%20%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D1%8B%D1%85%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2%20%D0%B8%20%D1%80%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9%20%D0%BF%D0%BE%D1%80%D1%8F%D0%B4%D0%BE%D0%BA.md).
- [Уже разработанные правила памяти и scope](../%D0%9F%D0%B0%D0%BC%D1%8F%D1%82%D1%8C%20%E2%80%94%20%D1%81%D0%BA%D0%B2%D0%BE%D0%B7%D0%BD%D0%B0%D1%8F%20%D0%B0%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%B8%20%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0.md).
- [Обзор R1 с Knowledge / Professional Packs](../IDEAS/NOX-R1-CAPABILITY-LIBRARIAN-AND-KNOWLEDGE-SYSTEM-2026-11-13.md).
- [Независимый R0 аудит](../REPORTS/NOX-OWNER-READINESS-REVIEW-01-2026-11-13.md) и [последняя сохранённая проверка R0](../REPORTS/NOX-R0-LIVE-STATUS-2026-11-13-0223UTC.md).
- [Исходный acceptance-план субъектов архитектуры](../TESTS/AWE-ARCHITECTURE-ACCEPTANCE-PLAN-2026-11-12.md).

## Текущая граница решения владельца

Владелец просил перейти от обсуждения к **раскладке готовых сервисов по конкретным блокам с сохранением в GitHub**, чтобы исключить путаницу. Создание этих документов является выполнением задачи по организации. **Конкретные продукты, ключи, платные тарифы, разрешения на инсталляцию, изменения кода, бюджет R1 и запуск R1 пока не утверждены.**
