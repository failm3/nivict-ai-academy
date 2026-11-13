# NOX / AWE GROUP — MARKET REUSE AUDIT FOR R1

**13 ноября 2026. Тип:** независимый desk-research и предварительный инженерный выбор. **Не проверено локальным интеграционным тестом Nox; не утверждено владельцем к установке.** `R0` в OpenCode НЕ изменять и НЕ перезапускать, пока нет его самостоятельной приёмки. Отчёт относится ко всем восьми R1-блокам, но не является массовым аудитом 4504 исходников.

## ВАЖНАЯ ПОПРАВКА — проверка реально существующего Nox

В исходниках локального cleanroom из OpenCode Recorder подтверждены: **Mastra @mastra/core 1.82.0, @mastra/mcp 2.8.0, @mastra/memory 1.41.0, @mastra/libsql 1.29.0**, действующие кодовые интерфейсы `createSpecification` (Prompt Master), `headAgent`, `createSpecialist`, `runDelegateCall`, `MCPClient` Playwright, file/shell/web tools, `ti_search`, `manus_search`, `MissionManager`, QA. **Эти компоненты нельзя предлагать внедрить заново**. Дальнейший список Composio/Pipedream/ToolHive — только рынок кандидатов для **доказанных отсутствующих возможностей**, не готовая рекомендация к установке. Встроенные ToolSearchProcessor/SkillSearchProcessor существуют в документации Mastra, но их подключение в Nox пока **не подтверждено**; API/совместимость надо проверить в финальном R0 checkout.

[Подробный read-only source audit с версионными и файловыми доказательствами](./NOX-IMPLEMENTED-CAPABILITIES-SOURCE-AUDIT-2026-11-13.md). **При конфликте общего market scan и source audit — исходники Nox приоритетнее.**

## 0. Вывод для владельца

**Основное: большая часть «библиотекаря», профессиональных инструкций, удалённых интеграций, импорта документов, наблюдаемости и тестов уже реализована на рынке.** Рекомендуется стратегия **BUY/REUSE FIRST, THIN GLUE ONLY**:
1. Оставить существующий Nox/Mastra/Tool Intelligence, не менять оркестратор.
2. Для **известных разрешённых инструментов** использовать Mastra `ToolSearchProcessor` + `MCPClient` + `requireApproval` / `requireToolApproval` / `suspend`. Встроенный ToolSearchProcessor не умеет сам по себе устанавливать/одобрять любой кандидат из TI.
3. Для **SaaS/API OAuth интеграций** провести сравнительный пилот **Composio vs Pipedream Connect** (Arcade — запасной/специализированный кандидат), не подключать всех сразу. Для **self-hosted MCP** — оценить **ToolHive** только если текущий R0 sandbox/policy не покрывает требования.
4. Для **Knowledge**: Docling для PDF/Office/аудио; Crawl4AI для разрешённых сайтов/статей; имеющиеся PostgreSQL/память и source-citation retrieval прежде нового RAG сервера. RAGFlow — тяжёлая альтернатива, не default. Mastra Knowledge alpha не гарантирует межклиентскую изоляцию.
5. Для **профессиональных пакетов**: стандарт `SKILL.md`/Agent Skills + Mastra `SkillSearchProcessor` + проверяемые рецепты/тесты; дополнительные правила композиции минимальные, не отдельная Factory.
6. Для **QA и evals**: Promptfoo как репродуцируемый TS/CLI тестовый фреймворк; Playwright для браузерных артефактов. Langfuse при нехватке штатного observability; Inspect AI как независимая Python-система больших сравнительных экспериментов, не обязательная в MVP.
7. **Писать самим только доменную связку**: mapping `capability → approved connected tools` из существующего TI, task-scoped policy/identity/grant, неизменяемый receipt/QA артефакта, условия активации и QA контракты Capability Packs, ACL/provenance для корпоративной памяти. Встроенные продукты сократят код, но не снимают ответственность Nox за безопасность и верификацию.

### Что доказано, а что нет

`PRODUCT_DOCUMENTED`: конкретный API/feature описан в публичном руководстве и репозитории; `PUBLIC_ADOPTION`: публично описано использование людьми/организациями; `VENDOR_CASE_STUDY`: история от продавца, не независимый масштабный стресс-тест; `NOX_INTEGRATION_NOT_TESTED`: точная версия, скоуп, деньги, ключи, стабильность и совместимость локального Nox не проверены. **Все кандидаты пока NOX_INTEGRATION_NOT_TESTED**. Ни GitHub stars, ни «1000 apps», ни компания в списке клиентов не доказывают, что Nox сможет работать с конкретным инструментом.

## 1. Блок R1-01: поиск, подключение, подтверждение, исполнение

| Решение | Готовый функционал | Реальное рыночное свидетельство | Риск / пробел | Вердикт |
|---|---|---|---|---|
| **Mastra ToolSearchProcessor** | `search_tools`, `load_tool`, подгрузка зарегистрированных tools по запросу; нужен @mastra/core >=1.58.0 | Официальный функционал, сам Mastra используется компаниями (vendor cases: Salesforce, MongoDB, Sanity) | **Только заранее предоставленные toolsets**; сам не создаёт vendor connections и не выдает policy grants. Нельзя передавать unrestricted `allTools` | **DEFAULT REUSE** |
| **Mastra MCPClient** | MCP stdio/Streamable HTTP + проксирование tool schemas | Официальные docs | Auth, tenants, per-operation authz остаются обязанностью приложения, версия локально неизвестна | **DEFAULT REUSE** |
| **Mastra HITL & durable agents** | `requireApproval`, `requireToolApproval`, точный tool arguments fingerprint, suspend/resume, subagent approval propagation, persistent-suspended runs при storage | Официальные docs | approval ≠ durable identity-based policy; ещё проверить R0 cancellations and storage | **DEFAULT REUSE** |
| **Composio** | Поиск+вызов SaaS-toolkits, OAuth/управляемые credentials, per-user sessions, готовый пакет `@composio/mastra`; cloud/MCP | Публичные customer cases Glean/Browser Use; self-reported customers Amazon Quick/Zoom | Vendor cloud, тарифы, доступность из сети Nox, политика передачи данных, ограничения отдельных API | **TOP EXTERNAL SaaS CANDIDATE** |
| **Pipedream Connect** | Managed OAuth, множество APIs/actions/event triggers, REST/SDK/MCP, пользовательские подключения | Заявленные публичные reference customers, установленная integration platform | Hosted execution; terms/licence Pipedream source-available ≠ полная MIT-платформа; SaaS billing | **COMPOSIO COMPARISON A** |
| **Arcade** | Облачный actions/MCP gateway, OAuth, identity/policy governance | Продуктовая документация и примеры | Нет независимого Nox bake-off, прайсинг и опции хостинга уточнить | **COMPARISON B** |
| **ToolHive (Stacklok)** | Open-source self-hosted MCP server isolation, registry, identities, audit, OTel, Kubernetes/CLI | Официальный открытый репозиторий Apache 2.0 и documented deployment | Контейнеры, управление policy, ресурсы; только MCP, не произвольный API+CLI без адаптеров | **SECURITY OPTION IF NEEDED** |
| **Official MCP Registry** | Место нахождения опубликованных MCP servers | Функционирующий каталог | Никакой автоматической проверки безопасности, разрешений или фактического исполнения | **DISCOVERY ONLY** |
| **Activepieces** | Self-hostable TypeScript pieces, workflow templates, встроенный MCP, бизнес-автоматизация | Документация, открытые packages, community+commercial licensing | Дублирование собственного Mission Manager при включении в качестве оркестратора; проверять license boundaries | **LATER ACTION WORKER** |
| **n8n** | Зрелая workflow automation ecosystem | Массовое использование продукта, существующие docs | Sustainable Use License: если клиенты Nox смогут конфигурировать собственные workflows через AI, может потребоваться коммерческая лицензия | **NOT DEFAULT** |

**Правило архитектуры:** только один *основной* контур управления: Head/Mission Manager Nox; Mastra tool search — selection; TI — catalog; Composio/Pipedream/ToolHive — альтернативные способы *выполнения* и управления подключениями. Не делать три параллельных auth/cloud посредника.

**Важно:** `Mastra ToolSearchProcessor` подгружает *конкретный объект инструмента* в агента, но **не является независимым authorization boundary**. Policy middleware и адаптеры должны проверять user/tenant/task/scope при каждом `invoke`, даже если инструмент не был показан в списке. Mastra MCP auth guide отдельно предупреждает о REST routes и границах authn/authz.

**Источники:**
- Mastra tool search https://mastra.ai/blog/introducing-tool-search-processor ; official processors https://mastra.ai/docs/agents/processors
- Mastra approval/handoff https://mastra.ai/docs/agents/human-in-the-loop ; MCP auth https://mastra.ai/docs/guides/mcp-authentication-authorization
- Mastra production customers https://mastra.ai/customers ; 1.0 adoption https://mastra.ai/blog/announcing-mastra-1
- Composio repo https://github.com/ComposioHQ/composio ; Mastra adapter https://docs.composio.dev/docs/providers/mastra ; Glean case https://composio.dev/customers/glean ; Browser Use case https://composio.dev/built-with/browser-use
- Pipedream Connect https://pipedream.com/connect ; license https://github.com/PipedreamHQ/pipedream/blob/master/LICENSE
- Arcade https://docs.arcade.dev/en/home ; ToolHive https://github.com/stacklok/toolhive ; MCP Registry https://registry.modelcontextprotocol.io/
- Activepieces https://www.activepieces.com/docs/mcp/overview ; n8n licensing https://support.n8n.io/article/can-i-use-your-license-for-my-use-case

## 2. Блок R1-02: фундаментальные знания / книги / статьи / видео

| Решение | Уже умеет | Предлагаемое место | Ограничение |
|---|---|---|---|
| **Docling** (IBM-origin, MIT, CLI/API/MCP) | PDF, Office, EPUB, HTML, audio, OCR, таблицы → структурированные тексты | **Первый парсер документов и доступного аудио** | OCR/media могут быть тяжелыми, нужны тесты качества; лицензии самих документов |
| **Crawl4AI** (Apache 2.0) | Получение легально доступных веб-страниц, Markdown, структурированное извлечение, crawler | **Первый ingestion для статей и официальной документации** | Web safety, robots/terms, сложные сайты; не источник достоверности сам по себе |
| **RAGFlow** (Apache 2.0 core) | Полноценная база RAG, разбор сложных документов, цитаты, поиск | Запасной self-hosted RAG стек, если существующая память не справится | Документация рекомендует 4 CPU, 16 GB RAM, 50 GB disk; дублирование storage |
| **Mastra Knowledge alpha** | Публичный Knowledge graph, pages/notes и tools | **Only non-sensitive experimentation** | Документация прямо говорит, что гарантированной изоляции scopes ещё нет |
| **Existing PG / Supermemory candidate** | Исторические проектные решения о хранении / semantic search | Сначала проверить локальное состояние, reuse first | Новое разделение project ACL и quality gates требуется независимо от retrieval backend |
| **Video ingestion** | Docling поддерживает часть аудиоформатов, внешние транскрипты можно обрабатывать как документы | Для лицензированных/доступных видео: субтитры/транскрипт с timestamp и подтверждённый источник | Не заявлять полноценное понимание всех видео без анализа кадров и реального теста |

**Не писать собственный PDF parser, crawler или «видеотранскрибатор» до тестов готовых решений.** Писать, вероятно, придётся маленький **Knowledge Ingest Gate**: legal/access, provenance, scope, original URL, extracted fragments with timestamps, trust tier, verified flags, refresh policy, ACL applied **before** retrieval. LLM summary ≠ authoritative source.

**Источники:** Docling https://docling.ai/ ; repository https://github.com/docling-project/docling ; IBM production offering https://www.ibm.com/products/docling ; Crawl4AI https://docs.crawl4ai.com/ ; RAGFlow https://ragflow.io/docs ; Mastra Knowledge alpha https://mastra.ai/docs/knowledge/overview .

## 3. R1-03 / R1-04: Skills, Recipes и профессиональные пакеты

**Стандарт Agent Skills** `SKILL.md` в директории с `scripts/`, `references/`, `assets/`: переносимый versioned формат, progressive disclosure. **Mastra `SkillSearchProcessor`** ищет skills по запросу и загружает нужные; уже не надо писать собственный движок обнаружения skills.

**Писать самостоятельно только тонкий PackManifest:** conditions/task type → mandatory knowledge references + required *capabilities* + expected artifact schema + deterministic tests + approved experts. Профессиональные пакеты **не обязаны** автоматически устанавливать каждую программу в системе; обязателен quality contract, не конкретный vendor.

Предполагаемые три пакета первого пилота: `WEB-PRODUCTION`, `CODE-CHANGE`, `RESEARCH-REPORT`. Unslop — кандидат в `WEB-PRODUCTION` как независимый антислоп-аудит, а не гарантия художественного качества.

**Источники:** https://github.com/agentskills/agentskills ; https://mastra.ai/reference/processors/skills-processor ; https://mastra.ai/blog/introducing-skill-search-processor ; https://github.com/0design/unslop-skill .

## 4. R1-05 Agent Factory / Delegation

Mastra уже имеет инструменты для supervisor/subagent и распространения approval через иерархию; используем их если совместимы с текущим Head. Писать только собственные *ролевые шаблоны*, bounded scopes, parent→child delegation policy и тестируемые контракты handoff. **Не мигрировать на новый multiagent framework из-за его маркетинга.** Текущая реализация Nox имеет частичное делегирование, но real recursive execution R0 не был релизно подтверждён по предыдущему аудиту.

Источник: https://mastra.ai/docs/agents/human-in-the-loop .

## 5. R1-06 Independent QA / Evals / observability

| Готовое решение | Назначение | Уровень подтверждения | Решение |
|---|---|---|---|
| **Promptfoo** (MIT/CLI/TS) | Prompt+agent eval, негативные и red-team тесты, сравнительный CI | Open-source и публичный пример/официальная документация OpenAI | **PRIMARY MVP TEST RUNNER**; отдельно deterministic tests of actual artifacts |
| **Playwright/Chromium** | Действительно открыть сайты, проверить DOM и собрать desktop/mobile screenshots | Ранее реально использовалось в Nox NIVICT миссии | **REUSE** |
| **Langfuse** | Traces, costs, versions, datasets, experiments and LLM graders | Публичные case studies вендора для компаний, включая Canva/Ramp/Trade Republic, но это не Nox testing | **OPTIONAL**, если штатные Mastra traces/evals недостаточны |
| **Inspect AI** (UK AI Security Institute, open-source) | Надёжный независимый evaluation harness для agent tasks, sandboxing, arbitrary external agents, checkpoints | Государственный исследовательский проект, обширные тестовые наборы | **R2 / rigorous independent benchmark candidate**, не нужно тащить в R1 MVP |

**Внимание:** официальный OpenAI legacy Evals API имеет срок отключения 2026-11-30; **не начинать новую архитектуру на устаревающей платформе**, использовать актуальные Datasets/trace grading или open-source Promptfoo.

**Источники:** https://github.com/promptfoo/promptfoo ; https://developers.openai.com/api/docs/guides/promptfoo-codex ; https://langfuse.com/docs/evaluation/overview ; https://langfuse.com/handbook/chapters/customers ; https://inspect.aisi.org.uk/ ; https://developers.openai.com/api/docs/guides/evals .

## 6. R1-07 OpenCode Engineering Toolkit

**Строго отдельная плоскость разработки:** Git/GitHub, built-in OpenCode tools, MCP Inspector, Playwright, Context7, security CLI и Promptfoo могут помогать инженеру строить Nox. Это **не доказывает**, что Nox сам будет иметь эти инструменты. Не устанавливать во время R0. Контроль версий, ограниченная изолированная среда и read-only inventory до изменений.

## 7. R1-08 / R2 pilot stress — как выбрать, а не гадать

### Пилот 0 — compatibility (без live costs)
- Проверить фактические `@mastra/core`, `@mastra/mcp`, Node, список tools, существующие TI adapters/approval mechanisms именно из финального R0 checkout.
- Отделить already-implemented от docs-only, 5–10 approved tools, 0 new vendor credentials.
- Устроить negative tests selection/no grant, stale grant, changed tool digest, wrong-client memory, abort, double retry.
- **Fail if model can access tools without grant, or no real execution receipt.**

### Пилот 1 — external SaaS connector bake-off
- Сравнить **Composio и Pipedream** на одной *неопасной* задаче: OAuth test account → read one dummy record → invoke within scope → receipt → revoke → invocation rejected → audit, measured latency and fees. Arcade challenger only if both fail or require unwanted cloud permissions.
- Критерии: Mastra TypeScript compatibility, self-host/cloud policy, per-user separation, revocation, idempotency, API coverage for actual target app, privacy, costs.
- Не делать «сравнение» только по числу apps or flashy demos. Не подключать живую карьерную почту/HH без отдельной авторизации.

### Пилот 2 — open-source MCP isolation
- Если нужен локальный MCP execution, сравнить **existing R0 sandbox vs ToolHive** on same server with equivalent policy and four failure injections; не добавлять ToolHive, если новые функции не компенсируют complexity.

### Пилот 3 — knowledge and skill
- 10 источников MDN/другой первичной техдокументации + несколько разрешённых PDF/видео транскриптов → Docling/Crawl4AI → scope provenance and source citation → retrieval by relevant agent → `SKILL.md` recipe → actual work result.
- Оценить доступность, recall, точность цитат, устаревшую версию, prompt injection, cross-project isolation.

### Пилот 4 — end-to-end acceptance
- 3 независимые supervised задачи: статический сайт (не обязательно backend), code bugfix, research note with citations, no OpenCode assistance in execution.
- Immutable original requirements, real artifacts, independent human/professional evaluation when appropriate, bounded costs, crash/cancel and malicious-tool cases.
- Для каждого run: agent tasks, tool call ID, real adapter version, scope/grant, immutable receipt, artifacts+sha256, approval evidence, real costs, independent QA. Owner GO only after acceptance.

## 8. Финальная матрица Build vs Buy (предварительная)

| Результат | Готовое/используемое | Минимальная собственная доработка |
|---|---|---|
| Находить инструмент | Mastra ToolSearchProcessor; existing TI | adapter from verified TI candidates to **pre-approved** Mastra toolsets |
| Подключать инструменты | Mastra MCPClient; Composio/Pipedream; ToolHive optionally | selecting single integration route, secrets + tenant-scoped auth |
| Выдавать/забирать разрешения | Mastra HITL and vendor auth | durable policy/approval binding to mission+agent+args+version; revoke receipt |
| Работать с документами | Docling; Crawl4AI | ingestion ACL, provenance, freshness and source review |
| Выбирать навыки | Agent Skills; Mastra SkillSearchProcessor | versioned pack manifest + tasks applicability |
| Выполнять типовые задачи | Mastra workflow/agent, standard Skills, domain tools | 3 initial recipes and QA contracts |
| Динамические субагенты | existing Head/Factory, Mastra supervisor | bounded role/config composition and end-to-end tests |
| Проверять результат | Playwright, Promptfoo, optional Langfuse | immutable oracle, artifact validators and expert review |
| Crash recovery / cost / action safety | R0 lifecycle plus Mastra durable concepts | demonstrate single authoritative state, idempotent external effects, receipts |
| Профессиональное качество | expert sources + Unslop candidate | human rubric, reproducible visual comparison; no false synthetic score |

## 9. Принцип принятия решения

**Следующее задание OpenCode должно начинаться не словами «разработай Tool Gateway», а:**
> Сначала проведи read-only inventory финального R0 checkout. Сопоставь каждый недостающий capability с официальными возможностями текущей версии Mastra, готовыми TypeScript/MCP провайдерами, TI catalog и внешними решением. Проведи изолированные репродуцируемые bake-offs только после owner approval. Выбери минимум новых компонентов. Докажи невмешательство в действующее ядро, типы разрешений, фактические tool calls и QA. Предъяви code diff только для функций, которые готовые сервисы не покрывают.

**Сводка:** направление владельца подтверждается рынком. Но «готовый у вендора» ≠ «подключен в Nox», а «есть крупный клиент» ≠ «работает любая наша миссия». Выбирать по целевым сценариям и измеряемым gates; не по объёму маркетингового каталога.

## Исторические документы AWE

- [Текущая карта R1](../README.md) ; [R1-01](../01-TOOL-GATEWAY/SPEC.md)
- [Идея librarian+knowledge](../../IDEAS/NOX-R1-CAPABILITY-LIBRARIAN-AND-KNOWLEDGE-SYSTEM-2026-11-13.md)
- [Аудит 4504](../../02%20-%20%D0%90%D1%83%D0%B4%D0%B8%D1%82%204504%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2.md)
- [Актуальный приоритет reuse](../../%D0%90%D0%9A%D0%A2%D0%A3%D0%90%D0%9B%D0%AC%D0%9D%D0%9E%20%E2%80%94%202026-11-11%20%E2%80%94%20%D0%BF%D1%80%D0%B8%D0%BE%D1%80%D0%B8%D1%82%D0%B5%D1%82%20%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D1%8B%D1%85%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2%20%D0%B8%20%D1%80%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9%20%D0%BF%D0%BE%D1%80%D1%8F%D0%B4%D0%BE%D0%BA.md)
