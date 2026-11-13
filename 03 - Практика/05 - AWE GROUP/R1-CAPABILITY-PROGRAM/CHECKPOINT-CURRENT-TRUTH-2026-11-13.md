# AWE GROUP / NOX — ЕДИНАЯ КОНТРОЛЬНАЯ ТОЧКА: R0, R1, build-vs-buy

**Дата:** 2026-11-13. **Статус:** утверждение пользовательского приоритета и выверенная реконструкция беседы, **НЕ acceptance R0 и НЕ разрешение установить R1**.

## Главная цель
**Nox** — самостоятельный агент AWE GROUP, принимающий миссии прямо от владельца и сам организующий их выполнение: требования → Head → Mission Manager / специализация / подагенты → модели+инструменты+знания → независимый QA → реальные артефакты → память. **OpenCode — отдельная инженерная среда разработки Nox**, не его внутренний оркестратор и не будущий пользовательский посредник.

## Что исходники уже подтвердили — не строить повторно
Данные получены из фактических `read`-операций OpenCode Session Recorder в локальном `/home/nox/awe-group-cleanroom-20261112`, а не из старой `awe-group-runtime/main` (там другой исторический baseline).

- `@mastra/core: 1.82.0`, `@mastra/mcp: 2.8.0`, `@mastra/memory: 1.41.0`, `@mastra/libsql: 1.29.0`, `@playwright/test: 1.49.1`; также TypeScript, Zod, Express, etc. `package.json` прочитан 02:49 UTC.
- **Prompt Master** существует: `src/agents/prompt-master.ts` импортируется в `src/api/server.ts`, вызывается `createSpecification(request)` через `POST /specify`; CLI также вызывает функцию. Это **кодовый call path**, не доказательство полноценного интервью/QA Prompt Master.
- **Head Agent**: Mastra `Agent` в `src/agents/head-agent.ts` с планированием и JSON-планом делегирования.
- **Mission Manager**: `mission-manager.ts`; API approve/cancel, CLI run/resume; R0 активно исправляет race/cancel/артефакты.
- **Agent Factory частично**: `src/agents/specialists.ts` функция `createSpecialist()` действительно создаёт Mastra Agent с задачей, контекстом, выбранными моделью и разрешёнными инструментами. `recursion.ts` содержит `runDelegateCall`, лимиты глубины, подагентов, параллелизма. Полный end-to-end не принят.
- **Инструменты**: Mastra `createTool` для `shell`, `file_read`, `file_write`, `file_list`, `web_fetch`, `web_search`, `web_extract`, `save_artifact`, `ti_search`, `manus_search`, браузерные tools.
- **MCP уже используется**: `src/config/mcp.ts` lazy `MCPClient` для `@playwright/mcp` через stdio, discovery tools и браузерный адаптер; Playwright/browser использовался в NIVICT миссии. Нельзя «внедрять MCP с нуля».
- Memory и QA модули есть; достаточность cross-project ACL, долгосрочных знаний и независимого acceptance не доказана.
- `ToolSearchProcessor`, `SkillSearchProcessor`, полный approval/gateway могут быть доступны в текущем Mastra, **но их локальная конфигурация/применение в Nox ещё не подтверждены**.

Доказательная запись: [Source audit](./RESEARCH/NOX-IMPLEMENTED-CAPABILITIES-SOURCE-AUDIT-2026-11-13.md), с первичными записями Recorder 02:49, 02:51, 02:54, 03:03 UTC.

## R0 — существующий текущий инженерный этап
Закрывает P0: (1) cancellation/timeout, (2) durable state/CAS/leases, (3) deny-by-default tools/sandbox, (4) true deliverable and delegation, (5) reproducible independent QA. Реальные child-агенты OpenCode, кодовые правки, offline tests есть. **Последнее в данной беседе проверенное чтение рабочего интегратора — 03:15 UTC** (2026-11-13); финальное owner acceptance и единственный интегрированный GO **не подтверждены**. Не перезапускать и не выдавать R1 build task автоматически. На первом сайте NIVICT было 13/14 technical QA с overall FAIL и owner visual 2/10; это реальные недостатки качества, а не только нехватка книг.

## R1 — не новый оркестратор, а измеримые недостающие возможности
- **Tool Intelligence**: уже есть исследовательский каталог кандидатов (~4504 historical) и `ti_search`/`manus_search`, но catalogue entry != connected/granted/invoked tool.
- **Tool Gateway**: выбрать APPROVED, реально подключённый adapter, выдать task/agent scoped grant, выполнить реальный вызов, сохранить receipt+artifact, отозвать grant. «Библиотекарь» не обязательно новая AI-сущность — встроенные Mastra-функции имеют приоритет.
- **Knowledge System**: хранить версионированные достоверные документы, инструкции, книги/статьи/видео-транскрипты с правами/источниками, выполнять ACL-scoped retrieval; это не Tool Gateway и не автономное «переобучение модели».
- **Skills/Recipes/Capability Packs**: применять условно обязательные профессиональные процедуры, существующие стандарты и инструменты под конкретные deliverables; например WEB-PRODUCTION, CODE-CHANGE, RESEARCH-REPORT. Обязателен результат и Quality Contract, не произвольный конкретный продукт и не backend для каждого лендинга.
- **Independent QA**: проверять исходные критерии, реальные файлы, источники и безопасность, а не заявления LLM.

## Результат рыночного исследования — условные кандидаты, НЕ новые установки
- Mastra ToolSearch/SkillSearch, HITL, MCP — сначала проверить, какие API и конкретные вызовы уже реализованы в локальном Nox.
- Composio, Pipedream Connect, Arcade, ToolHive — только если фактически отсутствуют нужные SaaS/OAuth/MCP grant/connector capabilities.
- Docling/Crawl4AI — кандидаты ingest документов и веб-источников; не заменяют trusted provenance and ACL.
- Agent Skills — формат навыков; Promptfoo/Playwright/Langfuse/Inspect AI — eval/observability кандидаты; часть Playwright уже реально используется.
- `Market reuse audit` — desk research публичной документации и внедрений поставщиков, **не тест на совместимость с Nox**. Нельзя выдавать vendor adoption, GitHub stars или большой каталог за доказательство функциональности.

[Рыночный аудит](./RESEARCH/MARKET-REUSE-AUDIT-2026-11-13.md); [Программа и статусы](./README.md); [R1-01](./01-TOOL-GATEWAY/SPEC.md).

## Единый порядок действий (source-first)
1. Получить **интегрированный финальный R0 SHA + независимую приёмку**.
2. Провести **актуальный source & runtime inventory** именно этой версии: `EXISTS_AND_TESTED`, `EXISTS_NOT_WIRED`, `EXISTS_BUT_FAILS`, `MISSING`; тесты реальных инструментов/грантов/рецептов и ToolSearch/SkillSearch.
3. Составить **строгую gap matrix** — только доказанные пробелы.
4. По каждому пробелу сначала проверить **готовую совместимую функцию уже установленного стека**, затем 1–2 готовых рыночных решения в изолированном сравнительном тесте; писать только минимально необходимый связующий код.
5. После отдельного owner approval: R1 минимальный безопасный набор настоящих tools/knowledge/skills, реальные permission gates и независимые QA tests.
6. Первая миссия **напрямую через Nox без OpenCode**; затем оплаченные стресс-тесты только по отдельному бюджету, затем контролируемая эксплуатация.

## Исправленные ошибки консультанта
- Преждевременно предложил «внедрить Mastra» — **она уже стоит**.
- Предлагал новый Broker/Factory до точной оценки штатных компонентов — **так нельзя**.
- Смешивал «на рынке доступно», «в Nox установлено», «реально работает» и «прошло QA» — **это четыре разные категории**.
- Смешивал Tool Gateway и знания/навыки, хотя они независимы и должны взаимодействовать.
- Не считать R1 спецификацию, документы и массовый обзор 4504 доказательством выполненной инженерной работы.

**Правило для всех следующих решений: ПРОВЕРИТЬ СУЩЕСТВУЮЩИЙ NOX → ДОКАЗАТЬ ПРОБЕЛ → ПРОВЕРИТЬ ГОТОВОЕ → ИЗОЛИРОВАННЫЙ ТЕСТ → МИНИМАЛЬНАЯ ИНТЕГРАЦИЯ → НЕЗАВИСИМЫЙ QA.**

**Никаких установок, изменений live R0, платных тестов или новых permissions этим документом не разрешено.**
