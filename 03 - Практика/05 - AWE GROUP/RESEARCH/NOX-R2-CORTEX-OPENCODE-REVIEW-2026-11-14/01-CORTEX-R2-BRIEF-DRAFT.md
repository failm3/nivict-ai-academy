# NOX / AWE GROUP — R2 Capability & Competence Intelligence
## Предварительное финальное ТЗ Cortex для независимого инженерного ревью OpenCode

Дата: 2026-11-14.
Статус: DRAFT_FOR_OPENCODE_REVIEW — это не окончательный приказ Cortex, не разрешение на изменение Nox, не принятие R2.
Владелец: AWE GROUP / Nox.
Этап: независимое инженерное ревью OpenCode → обновление ТЗ → передача Cortex на полное исследование → отдельное решение владельца об интеграции.

### 0. Главное требование владельца

Цель — не новая архитектурная презентация и не очередная большая разработка фреймворка. Нужен реально работающий автономный Nox, который может принять профессиональную миссию в ранее неизвестной области; определить пробелы в знаниях, инструментах и навыках; выбрать рациональную стратегию исполнения; быстро получить готовые и проверенные возможности; выполнить реальные действия; пройти независимый QA; сохранить и переносить подтверждённый опыт.

Жёсткий инженерный принцип: REUSE FIRST → CONFIGURE NATIVE → CONNECT READY-MADE → THIN ADAPTER → CUSTOM IMPLEMENTATION ONLY WHEN NECESSARY AND PROVEN.

Преимущество имеют существующие компоненты Mastra, Agent Skills, MCP, готовые SDK, API, CLI, исполняемые программы, проверенные workflows, профессиональные библиотеки, готовые шаблоны, парсеры, evaluation-инструменты и интеграционные платформы. Нельзя переписывать зрелое решение ради предпочтений инженера. Но нельзя и слепо подключать зависимости, дублирующие ядро или нарушающие права/границы проекта.

Критерий успеха — независимо принятая полезная миссия, а не число файлов, плагинов, агентов, отчётов или строк кода. Обязателен кратчайший безопасный путь к R2 с точными решениями и исполнимыми задачами OpenCode.

### 1. Источники и требование к свежести

Канонические материалы: GitHub failm3/nivict-ai-academy, прежде всего:
- 03 - Практика/05 - AWE GROUP/R1-CAPABILITY-PROGRAM/
- 03 - Практика/05 - AWE GROUP/RESEARCH/KORTIX-2026-11-13-ENTERPRISE-RESEARCH/
- 03 - Практика/05 - AWE GROUP/RESEARCH/CORTEX-NOX-CAPABILITY-KNOWLEDGE-MARKET-AUDIT-SCOPE-2026-11-13.md
- 03 - Практика/05 - AWE GROUP/PROMPTS/CORTEX-NOX-ENTERPRISE-CAPABILITY-RESEARCH-FINAL-2026-11-13.md
- 03 - Практика/05 - AWE GROUP/IDEAS/
- 03 - Практика/05 - AWE GROUP/ASTRA-AUTONOMY-AUDIT-2026-11-08/
- 03 - Практика/05 - AWE GROUP/CHECKPOINTS/
- 03 - Практика/05 - AWE GROUP/DECISIONS/
- 03 - Практика/05 - AWE GROUP/TESTS/

Дополнительные репозитории: failm3/awe-opencode-recordings (журнал фактической работы), failm3/awe-group-runtime (исторический экспорт, НЕ текущий cleanroom), failm3/awe-group-observer.
Фактическая локальная рабочая копия Nox при разрешённом доступе: /home/nox/awe-group-cleanroom-20261112, ветка r1/dev.

Не принимать старый remote export за текущие исходники. Отчёты и схемы не равны фактически вызываемому runtime. При недоступном исходнике фиксировать UNKNOWN. Сверять актуальные commit SHA, lockfile, конфигурацию и evidence перед окончательным выводом.

### 2. Контрольная точка OpenCode на 14 ноября 2026, 00:34 UTC

Последний подтверждённый локальный R1 commit: 68cc0ee. Важные предшественники: d682c89, 04121c0, 4ef555f.

- Приняты исправления ограниченного P0, isolation и recovery; типизация и сборка PASS.
- Полный offline gate 39/39 suites PASS.
- Замороженный R0 неизменён: 252 файла, 55/55 проверок hash.
- Первая локальная веб-миссия завершилась FAIL / PAUSED, evidence сохранены.
- После исправления cumulative resume time запущена ровно одна отдельная разрешённая повторная миссия.
- Вторая миссия создала реальный четырёхфайловый статический task tracker.
- Финальный продукт прошёл 13/13 независимых браузерных проверок, включая адаптивность, keyboard, local resources, persistence, filtering, deletion.
- Но сама миссия NOT ACCEPTED: PAUSED после 600111 мс из 600000 мс; unresolved repair intent сохранён; нельзя подменять browser PASS терминальным SUCCESS.
- Пять завершённых модельных вызовов: неполная сумма 337014 токенов; полное использование и provider dollars UNKNOWN.
- Локальная ветка r1/dev чистая на момент последнего отчёта. Деплой, публикация, remote push новых коммитов НЕ подтверждены.

Источник: https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-14/00-34/part0000.txt
Evidence: reports/R1-LOCAL-WEB-PRACTICE.md и reports/r1-local-web-1794615675176-cad6b269/.
Это baseline, не гарантия, что с момента публикации ничего не изменилось: начать с fresh-read актуального состояния.

### 3. Предлагаемое целевое определение R2 — провести критическую проверку

Рабочее имя: R2 Autonomous Capability & Competence Runtime.

Nox должен уметь:
1. Получать произвольную допустимую профессиональную миссию на естественном языке.
2. Фиксировать задачу, требования, scope, критерии результата, риски, бюджет.
3. Определять имеющиеся и отсутствующие компетенции и инструменты.
4. Выбирать стратегию исполнения: программа, готовый скрипт, новый скрипт, CLI, API, workflow, бот, LLM, агент, коллектив агентов или гибрид.
5. Использовать собственный каталог; при дефиците обнаруживать внешние кандидаты.
6. Находить профессиональные знания и процедуры из проверенных источников.
7. Исследовать, сравнивать, проверять совместимость, безопасность, лицензии и стоимость решений.
8. Подключать разрешённые готовые решения, используя минимальное число изменений в runtime.
9. Выполнять миссию с наблюдаемым состоянием, ограниченными полномочиями и восстановлением.
10. Независимо проверять реальные артефакты, действия и качество.
11. Сохранять версионированные навыки, решения, ошибки и доказательства; переиспользовать при новой миссии.
12. Расширять карту профессий без закрытого заранее списка.
13. Работать самостоятельно, без OpenCode как обязательного пользовательского посредника.

Это гипотеза определения R2, а не уже утверждённый и реализованный стандарт. Kortix должен указать, что реалистично для минимально принятого R2, что нужно вынести в R2.x/R3, а что требует дополнительных разрешений/ресурсов. Не обещать профессиональную аккредитацию во всех областях.

### 4. Полный независимый forensic audit текущего Nox

Проверить по исходникам, runtime evidence и действительным инструментальным вызовам:
Prompt Master, Head, Mission Manager, Factory/createSpecialist, recursion/runDelegateCall, модельный router, Mastra tools, MCPClient, Tool Intelligence, Memory/libsql/PG, Artifact Store, grants/policy, QA, release/update lifecycle, observability, receipts, recovery.

Установить для каждой функции состояние: PLANNED / DOCUMENTED / CODE_PRESENT / CONFIGURED / CALLABLE / TESTED / INDEPENDENT_QA_ACCEPTED / RELEASED / BROKEN / UNKNOWN.
Обязательно показать разрывы между as-designed, as-coded, as-configured и as-run.

Исследовать конкретную причину несоответствия между финальным browser PASS и PAUSED миссии, а также дорогих/долгих генераций, чрезмерных repair-loop, контекста, выбора моделей, количества calls и strategy. Не предлагать увеличение лимитов как основной ответ. Не использовать неполные токенные суммы как полный cost ledger.

### 5. Полный аудит 4504 исходных записей

Исходники: iirepresent.json (1331), Радар.json (3173), каталог 04 - Инструменты/Каталог кандидатов/90 - Данные/catalog-all-4504.csv и связанные экспорты/карточки.

Обязательная полнота: учесть каждую исходную строку с неизменным historical ID, origin, raw URL, alias, normalized product/capability, дубли, ссылочную целостность и статус. Запрещено подменять каталог на шортлист из 20–50 продуктов.

Для каждой записи: реальный класс (исполняемый tool, MCP, SDK, CLI, API, Skill, workflow, library, service, app, документация, статья, каталог и т.д.), компетенции и операции, официальный owner/repo/release, актуальность, лицензия, безопасность, совместимость с Nox, зависимости, способ интеграции, стоимость, риски, ограничения доступа, альтернативы, степень доказательства и итоговый verdict. Дублирующиеся URL не объявлять независимыми capabilities; форки и SaaS/self-hosted editions не сливать без анализа.

Не требуется запускать все 4504 неизвестных программ. Полнота инвентаризации 4504 обязательна, глубокие исполняемые тесты приоритизировать по реальной полезности, риску и доступности sandbox. Факт статического чтения не выдавать за smoke PASS.

### 6. Расширенный поиск вне каталога

Найти дополнительные релевантные профессиональные инструменты, MCP, SKILL.md/Agent Skills, SDK, API, CLI, workflows, шаблоны, starter kits, библиотеки, парсеры, evaluation suites, источники знаний и платформы. Нет искусственного лимита находок, числа используемых поисковых источников, промежуточных агентов или исследовательских ветвей. Искать столько, сколько нужно для доказательного качественного результата, не превращая задачу в бесконечное коллекционирование ссылок.

Делить кандидатов на: реальное готовое подключение, доступная native-функция, minor wiring, heavy integration, build-only-if-proven, reject/defer, unknown.

### 7. Технические семейства и зрелые готовые интеграции

Обязательно оценить актуальные готовые варианты, НЕ объявляя их заранее обязательными:
- Mastra native Tools, ToolSearchProcessor, SkillSearchProcessor, MCPClient, memory/workflow/HITL;
- официальный MCP Registry, конкретные MCP servers, MCP Inspector, ToolHive;
- REST/OpenAPI, SDK, CLI, Playwright/DevTools, browser-use, Figma MCP/API;
- Composio, Pipedream Connect, Arcade и другие managed integrations — только при доказанном OAuth/account gap;
- Agent Skills стандарт и готовые vendor/community skills;
- Docling, Crawl4AI и другие профессиональные ingestion alternatives;
- Promptfoo, Langfuse, Inspect AI и другие evaluators — только при действительном QA gap;
- существующие безопасные инструменты code quality, тестирования, supply-chain безопасности, observability, CI/CD;
- Unslop как минимум два разных проекта: heydamir/unslop и 0design/unslop-skill; не смешивать лицензии, зависимости и capabilities.

Для кандидата: exact upstream version/sha/docs, actual functional need, module/path Nox for wiring, minimal adapter/config, compatibility with Node/WSL/runtime, account secrets/OAuth handling, test, security gate, rollback, recurring costs, need for deployment.

Не дублировать существующий Head, Factory, Memory, Mission Manager, router или QA без доказанной необходимости. Проверить version-specific native Mastra API перед предложением нового кода.

### 8. Система A — Tool / Capability Intelligence

Спроектировать практически исполнимый путь:
NEED → DISCOVER → COMPARE → VET → TEST IN SANDBOX → CONNECT/REGISTER → GRANT → INVOKE → RECEIPT → QA → REUSE → REVALIDATE/REVOKE.

Развести независимые понятия: tool metadata, executable adapter, installed version, healthy connection, authorization/grant, actual invocation, verified result. Model-suggested tool не может выдавать сам себе права. ToolCard может содержать when/when_not, schema, compatible versions, fail modes, confirmed examples and evidence.

Предложить native-first thin glue к уже существующему TI/tool-context. Допуск низкорисковых операций может быть автоматическим при заранее утверждённой политике; установка нового исполняемого кода, деньги, секреты, публикации, destructive writes и новые права требуют соответствующих внешних ограничений.

### 9. Система B — Continuous Knowledge & Competence Intelligence

Постоянно пополняемая проверяемая база: standards/RFC/vendor docs, исследования, журналы, книги/учебники при наличии прав, белые книги, кейсы, постмортемы, SOP, учебные материалы, конференции, видео/аудио с таймкодами, профессиональные сообщества, репозитории, design systems, UI libraries, маркетинг, операции, продажи, IT, data science и новые области.

Нужны source provenance: URL, author, edition/version/date/hash, rights, trust, citations to original page/section/figure/timestamp, ACL, trust freshness, contradictory evidence, staleness monitoring, reindex/revoke. Обновления по events/schedules/missions, а не загрузка всего интернета по минутному таймеру без пользы.

Различать KnowledgeRecord, SkillRecord, ToolCard, Template, Agent Role, Capability Pack, QA Oracle. Изучение источника не равно mastering skill. Использовать current memory and ready-made extraction/retrieval components, не писать собственный универсальный parser и отдельную память без gap.

### 10. Open-world professional competence graph

Не ограничивать Nox фиксированным перечнем профессий. Нужна модель domain → subdomain → fundamental knowledge → specialized procedures → tools → dependencies → deliverable → QA standard → validity scope → verified experience.

При новой профессии Nox строит новую карту из проверенных фундаментальных компонентов, обнаруживает недостающие знания, добывает источники, проводит practice/eval, формирует новую specialization pack и фиксирует границы квалификации. Для отраслей с критическими рисками корректно ограничивает недоказанную экспертизу.

Базовые области (не закрытый список): UX/UI и Product Design; frontend/backend/mobile/desktop; software engineering; AI agents/bots/workflows; marketing, sales, CRM, analytics; business, finance, management, operations; research, data, documents; content/media; security, IT, DevOps/infrastructure; cross-domain scientific/industry specializations.

### 11. Библиотека фундаментальных Skills и профессиональных Capability Packs

Провести реальную инвентаризацию уже существующих skills и packs. Не считать role prompt полноценным проверенным Skill, а specification-only pack — установленным.

Найти максимально готовые переносимые SKILL.md, scripts, assets, references, professional SOP, example workflows, design kits, test fixtures и templates; проверить лицензии и совместимость. Для каждого pack: triggers, roles, knowledge refs, tool dependencies, skill versions, acceptance oracle, outputs, failure modes, when_not.

Включить anti-AI-slop, UI hierarchy, accessibility, Figma, browser/visual QA, software quality/testing/security, research citation integrity, business metrics и domain-specific professional barriers. Пакеты загружать условно, а не все в каждый контекст.

Проверять компетентность: practice → independent QA → held-out variant → transfer by fresh agent/context. Новое знание само по себе не должно повышать permissions.

### 12. Система C — Execution Strategy Intelligence

Нужно доказуемое решение, когда использовать:
- готовый алгоритм/функцию/утилиту;
- существующий или новый маленький скрипт;
- CLI/API и детерминированный workflow;
- постоянный сервис или Telegram-бот;
- одиночный LLM call;
- специализированного агента;
- parallel multiagent team;
- hybrid strategy;
- no-execution/blocked when capability or authority absent.

Выбор по неоднозначности, вероятности успеха, качеству, безопасности, правам, времени, совокупной стоимости, устойчивости, повторному использованию и поддержке. Подбор LLM модели — подзадача общей стратегии, не замена ей.

Рассмотреть, насколько существующий Prompt Master/Head/Mission Manager уже делает этот выбор; готовые Mastra workflows и deterministic recipes vs custom planner. Разделять выбор стратегии для миссии и отдельного шага. Никакого LLM для простого повторения известного скрипта без причин. Никакого нового постоянного бота, если достаточно одноразового action.

### 13. Система D — Meta-Intelligence / Controlled Improvement

Нужны calibration of competence/uncertainty, failure/no-progress detection, continuous evaluation, learning priority, rational research stopping, cost of competence, strategic memory, benchmark-before-and-after, drift detection, expiry of knowledge, tool updates, version pinning, rollback, shared verified knowledge with appropriate scope.

Отличать: Knowledge acquisition / Skill acquisition / Tool acquisition / Strategy learning / Runtime improvement. У каждого разные проверки, стоимость и authority. Обучение должно быть по требованию и проактивно при доказанной пользе, не ради фоновой активности. Не считать fine-tuning обязательным.

### 14. Исследовать зрелые работающие агенты и компании

Сравнить публично подтверждённые практики:
OpenAI Codex / harness / Agents SDK; Anthropic Claude Code / Agent SDK / Skills / hooks; Google ADK / Agent Engine; Microsoft Agent Framework; AWS Bedrock; Cognition Devin; Intercom Fin; Salesforce Agentforce; LangGraph; Mastra и другие релевантные производственные системы.

Не только маркетинговые страницы: опубликованные production cases, архитектура, версии, измерения, бенчмарки, postmortems, API и исходники. Не приписывать компании непубличную архитектуру. Для каждого pattern: цель; фактические доказательства; как переводится в Nox; готовый компонент; минимальный integration diff; ограничения; независимый proof of value.

### 15. Строгая классификация Build–Buy–Reuse

Каждому значимому решению дать отдельный технический verdict:
A ALREADY_WORKING;
B CONFIGURE_NATIVE;
C READY_MADE_INTEGRATION;
D THIN_ADAPTER;
E SIGNIFICANT_INTEGRATION;
F CUSTOM_IMPLEMENTATION;
G REJECT_OR_DEFER;
H UNKNOWN.

Для каждого F: исследованные готовые аналоги, доказательство несовместимости/непригодности, проверенная причина собственного кода, оценка рисков и maintenance burden.

Для B–F: конкретное repo/package/release, лицензия, инструкция установки, runtime module path, схема API, места wiring, deps, auth, тесты, трудозатраты как диапазон с допущениями, runtime cost, risks, rollback. Никакой характеристики «легко» без указания точного механизма.

Уровни evidence независимы: L1 found; L2 code/docs/license vetted; L3 isolated executable tested; L4 independently measured uplift on equal tasks. Нельзя заявлять L3/L4 по README или только статическому чтению.

### 16. Критический вопрос — насколько легко OpenCode реализует R2?

Проверить фактический OpenCode developer capability на текущем исходном коде. Составить конкретную dependency graph:
- что уже работает и не нужно трогать;
- что включает настройка Mastra;
- какие Skill/MCP/SDK готовы к вставке;
- где нужен thin adapter;
- где необходим небольшой contract change;
- где блокер безопасности, памяти, QA, lease, model policy;
- что уже имеет независимую проверку, а что только proposed;
- какие части следует отложить после MVP R2.

Ответить: может ли OpenCode сделать это без изменения ядра и по какому минимальному маршруту; какие объективные доказательства необходимы; какие риски/конфликты с текущим R1. Отдельно оценить эффект повышения квалификации, сокращения ненужных LLM calls и улучшения успешности реальных миссий. Указать, что считать R2, R2.x, R3.

### 17. R2 acceptance: реальные, независимые, проверяемые миссии

Обязательные направления программы:
T01 deterministic no-LLM execution after routing;
T02 correct ready-made tool choice and schema args;
T03 novel tool acquisition and safe sandbox trial;
T04 unknown-source-backed professional knowledge acquisition;
T05 skill held-out transfer to new task/agent;
T06 professional website with functional + visual + accessibility QA and terminal ACCEPTED within bounded budget;
T07 choose bot vs script vs workflow and deliver working test artifact;
T08 unknown profession/competence graph extension;
T09 adversarial tool/knowledge and prompt injection cannot grant authority;
T10 interruption/recovery with correct cumulative budget and no duplicate effect;
T11 efficiency comparison deterministic/LLM/hybrid;
T12 independent direct Nox mission without OpenCode as operator.

Добавить privacy/ACL, rollback, resource exhaustion, unapproved external write, malicious dependency, stale schema, failed OAuth/revoked grant, wrong-context memory, unsupported or unlicensed source, expert domain sign-off where needed.

Criteria: actual accepted artifacts and receipts, frozen initial requirements, no self-certification, complete cost and latency (or UNKNOWN), preserved failure evidence, no false success. Product QA PASS != mission ACCEPTED. Avoid overfitting to fixed acceptance fixtures.

### 18. Integration economics и fast path

Нужна стоимость принятых результатов (not price per model call), token/latency/repair usage, mean time to first correct tool call, tool selection precision, time to acquire skill, ability to re-use it, quality score, bounded failure and recovery.

Отделять cost of research, cost of build, cost of running, cost of continued maintenance. Выбирать решение по максимальной полезности и минимальным совокупным затратам/рискам, без иллюзии что free OSS означает zero TCO.

OpenCode не должен получать инструкцию «разработай всю R2 платформу». Передать минимальные взаимонезависимые проверяемые integration tickets (exact files/APIs/tests/rollbacks), упорядоченные по shortest safe path. Сначала по возможности один проход сквозного флоу, затем обобщение.

### 19. Свобода исследования и супер-агенты Cortex

Владелец не накладывает искусственных ограничений на количество исследовательских агентов, супер-агентов, моделей, поисковых ветвей, глубину поиска, число найденных инструментов, типов источников и профессиональных категорий. Cortex вправе самостоятельно организовать параллельное независимое исследование, делегировать задачи, критически пересматривать гипотезы и собирать результаты по своему усмотрению, чтобы получить качественный итог максимально эффективно.

Это свобода исследовательского метода, НЕ утверждение о бесконечных физических ресурсах или право превысить фактические тарифы, договорные ограничения, authority boundaries и разрешения. Без отдельной санкции нельзя покупать платные ресурсы, использовать чужие секреты, изменять production, нарушать лицензии или разворачивать сервисы с внешними эффектами. Уже разрешённые пользователем и технически доступные ресурсы можно использовать в пределах их прав и лимитов.

Инструменты, суперагенты и делегации — средство повысить качество исследования, а не KPI. Независимая критика и параллельная верификация приветствуются. Обязательно показывать использованные модели/источники и уровень доказательств; не маскировать неизвестное.

### 20. Выходные артефакты

Ожидаемый пакет, без искусственных ограничений на дополнительные файлы:
01 R2-EXECUTIVE-VERDICT.md
02 NOX-LATEST-RUNTIME-FORENSIC-AUDIT.md
03 COMPLETE-4504-REGISTRY.jsonl (все оригинальные строки и IDs)
04 EXPANDED-TOOLS-AND-SKILLS-REGISTRY.jsonl
05 READY-MADE-INTEGRATION-ATLAS.md
06 ENTERPRISE-AGENT-COMPARATIVE-RESEARCH.md
07 OPEN-WORLD-COMPETENCE-GRAPH.md
08 CONTINUOUS-KNOWLEDGE-SYSTEM.md
09 AUTONOMOUS-TOOL-ACQUISITION.md
10 EXECUTION-STRATEGY-INTELLIGENCE.md
11 LEARNING-META-INTELLIGENCE.md
12 DOMAIN-CAPABILITY-PACKS.md
13 BUILD-BUY-REUSE-MATRIX.csv
14 R2-ACCEPTANCE-AND-BENCHMARKS.md
15 OPENCODE-EXECUTION-PACK/ (точные инженерные задачи, зависимости, criterion, rollback)
16 FASTEST-SAFE-PATH-TO-R2.md
17 SOURCE-AND-EVIDENCE-LEDGER.jsonl
18 OWNER-DECISIONS-ONLY.md

Глубина каталога должна быть машиночитаемой, а executive-документ — коротким и критическим. Предоставить checksum/source manifest и consistency audit. Не заменять итоги общими заверениями.

### 21. Критические вопросы для независимого результата Cortex

- Что фактически умеет Nox после последнего OpenCode commit?
- Почему live web mission получила продукт QA PASS, но не accepted mission?
- Где самые большие реальные gap/стоимость/неэффективность?
- Какие exact готовые компоненты устранят каждый gap?
- Как быстро и безопасно их подключить к текущему Mastra?
- Кто и как будет приобретать новые tools без privilege escalation?
- Как вести непрерывную проверяемую профессиональную базу?
- Как обеспечить open-world profession mapping и реальные transferable skills?
- Как выбирать между кодом, ботом, workflow, LLM и hybrid?
- Как измерять стратегическое и профессиональное самоулучшение?
- Может ли OpenCode реализовать R2 с минимальным кодом?
- Что невозможно сделать достоверно на данном этапе, что требуется от владельца?
- Какие exact тесты достаточны для R2 acceptance?

### 22. Ограничения, критерий успешности и порядок

Cortex выполняет независимое исследование, каталогизацию, сопоставление и при наличии отдельной sandbox-возможности безопасные проверочные испытания. Исследование само по себе не запускает R2-deploy и не санкционирует mutation активной системы Nox, вмешательство в сессию OpenCode, внешние публикации, платные закупки, новые права.

Cortex должен критически опровергать наши неверные предположения, в том числе R2 scope. Избегать ложных "PASS", "установлено", "система уже умеет". При недоступности доказательств — UNKNOWN и конкретный способ проверки.

Окончательный R2 будет принят только после реальных прямых Nox-миссий и независимого QA, а не после написания красивого roadmap.

**Требуемый итог: понятный список конкретных готовых решений, exact точек их подключения, минимальных инженерных изменений, независимых проверок и достижимый кратчайший путь для OpenCode к работающему R2.**

---

## Инженерное ревью OpenCode — НЕ часть окончательного промпта Cortex

Этот файл сейчас предназначен для прочтения OpenCode как INPUT, а НЕ как прямое разрешение выполнить инженерные работы. OpenCode должен независимо проверить актуальные исходники и дополнить/исправить спецификацию, сохранив первоначальную версию, и записать предложенный конечный вариант в отдельный файл.

Подробные инструкции находятся в соседнем файле 02-OPENCODE-ENGINEERING-REVIEW-TASK.md.
