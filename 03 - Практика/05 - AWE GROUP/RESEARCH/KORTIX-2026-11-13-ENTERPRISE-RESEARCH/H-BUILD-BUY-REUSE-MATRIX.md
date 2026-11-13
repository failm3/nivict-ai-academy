<a id="section-h"></a>

## H. BUILD–BUY–REUSE: рынок и минимальный прирост Nox

Дата проверки/отсечения: **2026-11-13**. Режим RESEARCH ONLY. Рекомендации — исследовательские, не разрешение запуска R1. Автор — отдельная lane market-build-buy-reuse; делегации не было.

### Вывод

**Сохранять Nox/Mastra, Head, Prompt Master, Factory, Mission Manager, Tool Intelligence (TI), Memory и QA. Покупать не «агентную платформу», а только недостающий конкретный внешний action/управляемое подключение.** Большинство рассматриваемых платформ заменяют уже существующий control plane и поэтому не являются разумным default. Сначала проверить native конфигурацию на фактическом accepted SHA; затем один ограниченный adapter. Даже готовые OAuth, checkpoints и guardrails не заменяют Nox authority при side effect.

Практическая последовательность после независимой приёмки R0: granted-tool discovery → один внешний action с receipt → provenance ingestion в существующую память → versioned skills/packs → независимые artifact evals. Temporal, альтернативные frameworks и enterprise suites — отдельный research backlog, не блокер.

### 1. Доказательный baseline и ограничения

Прочитаны `out/baseline.md`, DOC-04, DOC-05, DOC-17. Их pinned revision **9b58aab1e09d8627bc006736c21b3d4790720ed7**, 2026-11-13 11:34:38Z; точные URL и hashes — `out/source-manifest.json`. Baseline повторно сверял main в 12:53 UTC. Новая попытка публичного GitHub API в этой lane в 13:34 UTC дала 403; свежесть после baseline НЕ подтверждена. Не обходили отказ и не запрашивали доступ.

DOC-04 сообщает Mastra core **1.82.0**, MCP **2.8.0**, memory **1.41.0**, libsql **1.29.0**, Playwright test **1.49.1**, Head/Factory/TI/Memory/QA и MCP wiring. Это **reported-in-docs**, не непосредственное чтение active cleanroom. Actual runtime `/home/nox/awe-group-cleanroom-20261112` и его final SHA **unknown**. Recorder/Observer ранее возвращали 404; это не отсутствие реализации. Старый public runtime **d5e9d857dbdeb8f31f9a798b10b5af4af639dbda** не равен текущему.

Последний опубликованный engineering update DOC-26: reported **22/22** offline suites, затем independent audit IN PROGRESS / NO FINAL GO SEEN; security 4/5 и process-probe nonzero требуют контекста. Исторический FAIL 04:24 нельзя выдавать за неизменный текущий статус, а 22/22 — за release acceptance. Никаких тестов здесь не запускали.

Непосредственно статически прочитанный historical code: [runtime-adapter.mjs L1–11](https://github.com/failm3/awe-group-runtime/blob/d5e9d857dbdeb8f31f9a798b10b5af4af639dbda/awe/tool_registry/runtime-adapter.mjs#L1-L11) — `prepareRuntimeReview`, dispatch_supported:false; это review envelope, не executable connector. [qa/authority.mjs L3–36](https://github.com/failm3/awe-group-runtime/blob/d5e9d857dbdeb8f31f9a798b10b5af4af639dbda/awe/qa/authority.mjs#L3-L36) — fixture issuer с independent subject и scope/revoke checks, не production identity. Эти два наблюдения **verified-in-code только historical**.

#### Evidence и verdict — разные оси

- `reported-in-docs` — Nox документы; `vendor-claim` — официальные docs/SDK descriptions, включая registry metadata; `verified-in-code` — статически прочитанный pinned code, не runtime; `inference` — наша рекомендация; `unknown` — нет достаточных данных.
- Семь decision verdict: **ALREADY_EXISTS, CONFIGURE_NATIVE, CONNECT_READY_MADE, SMALL_ADAPTER, NECESSARY_NEW_CODE, REJECT, UNKNOWN**. Verdict не означает QA_ACCEPTED.
- Реальный Nox live call сторонних кандидатов: **unknown**, кроме вторичного сообщения о прежнем browser screenshot. Независимые сопоставимые benchmark tests кандидатов в этой lane **не получены**. Customer stories поставщика не повышены до independent evidence.

### 2. Матрица реально нужных capabilities

Все действия ниже — inference. Существование src компонентов — DOC-04 reported; точные ссылки собраны в приложении. «Gap» означает непроверенную гарантию, а не установленное отсутствие кода. P/N — предлагаемые будущие positive/negative tests, НЕ выполненные тесты.

| Capability / Nox anchor | Что сохранить, gap | Путь и конкретный delta | Verdict | Evidence / будущий P/N |
|---|---|---|---|---|
| Mission planning: Prompt Master + Head | createSpecification/planMission уже сообщены | reuse; никаких второго planner или SaaS supervisor; сверить immutable acceptance criteria | ALREADY_EXISTS | DOC-04 L25–26; P criteria доходят до QA; N CLI не обходит approval |
| Factory/recursion | createSpecialist/runDelegateCall уже сообщены | reuse/extend role pack injection и durable child budget только при final-source gap | ALREADY_EXISTS | DOC-04 L27–28; P scoped child; N пустой grant не наследует allTools |
| Tool selection: TI + specialists | catalog ≠ executable adapter ≠ grant | configure native ToolSearchProcessor, только granted objects; не новая TI база | CONFIGURE_NATIVE | Mastra processors, DOC-04 L32–37; P нужный инструмент; N найденный без grant не вызывается |
| Skills loading: specialists + workspace | SkillSearch wiring неизвестен | configure native после API audit; pin skill digest, provenance, lifecycle QA | CONFIGURE_NATIVE | Mastra skills docs; P load by task; N unreviewed skill не повышает permissions |
| MCP execution: config/mcp.ts + browser.ts | MCPClient/Playwright уже сообщены | reuse; health/reconnect/receipt/abort добавить лишь при gap | ALREADY_EXISTS | DOC-04 L31; P receipt; N revoked account/timeout не продолжает effect |
| External SaaS auth: tool-context + TI | аккаунты, tenant scopes и revoke не приняты | integrate один Composio ИЛИ Pipedream ИЛИ Arcade adapter; не три middleware | SMALL_ADAPTER | Composio Mastra docs; P action+provider receipt; N чужой tenant и повторный replay |
| Self-hosted MCP management | не заменять MCPClient и TI | integrate ToolHive только при необходимости isolation/managed MCP fleet; bind server identity к grant | CONNECT_READY_MADE | ToolHive docs; P approved server; N unsigned/untrusted server deny |
| Durable mission recovery | Mission Manager уже hardened, final guarantees unknown | reuse/extend существующий state machine; Temporal defer до evidence архитектурного gap | UNKNOWN | DOC-26; Temporal workflow docs; P crash-resume; N effect-before-checkpoint не дублирует действие |
| Effect fencing / cancellation | tool-context, mission-manager, tools уже существуют | extend текущие authority/envelope проверки непосредственно перед effect, только если нет на final SHA | NECESSARY_NEW_CODE | условный verdict, не новый security stack; P current lease; N stale owner/abort denies effect |
| Knowledge ingestion | createAgentMemory/libsql сохранить | integrate Docling для документов, Crawl4AI для разрешённых страниц; тонкий provenance/ACL adapter | SMALL_ADAPTER | Docling/Crawl4AI docs; P citation page/fragment; N cross-project result/robots-denied URL |
| Memory/retrieval | память уже существует, trust/ACL unknown | extend existing schema: source version/hash/license, project ACL до retrieval; RAGFlow/new memory defer | SMALL_ADAPTER | DOC-04 L34, DOC-05; P correct citation; N poisoned source не становится authority |
| Professional packs | Factory + QA + skills | extend manifest conditions/artifacts/oracles, не агент на каждую программу | SMALL_ADAPTER | DOC-05; P transfer на новую задачу; N чтение SKILL не считается mastery |
| Regression/red-team | qa-agent + qa-gate сохранить | integrate Promptfoo как дополнительный runner; независимые deterministic artifact checks остаются | CONNECT_READY_MADE | Promptfoo docs; P регрессия обнаружена; N grader не принимает self-asserted success |
| Browser/visual QA | Playwright уже сообщён | reuse browser receipts/screenshots; независимый visual rubric и owner criteria | ALREADY_EXISTS | DOC-04 L31,35; P actual DOM/screenshot; N screenshot другой версии не проходит |
| Trace/cost visibility | native Mastra traces сначала | configure native; Langfuse/MLflow integrate только при доказанном gap retention/eval UX | CONFIGURE_NATIVE | Mastra, Langfuse/MLflow docs; P trace→artifact hash; N secret/PII не экспортируется |
| Rigorous external evaluation | QA независимость сохранить | defer Inspect/NeMo profiler как отдельные offline harnesses, не production control plane | CONNECT_READY_MADE | Inspect/NeMo docs; P holdout task; N train/eval leakage |
| Persistent agent budget | Mission Manager/recursion | extend единый durable budget ledger при gap; не считать telemetry billing enforcement | NECESSARY_NEW_CODE | DOC-26 + spec budget; P cap через resume; N restart не обнуляет lifetime count |
| Полная замена framework | Mastra/Head/Factory/Memory | defer/reject migration без воспроизводимого blocking defect и migration ADR | REJECT | DOC-04 + сравнение ниже; переход сам не исправляет effect semantics |

### 3. Дедуплицированный каталог frameworks и инфраструктуры

Ключ дедупликации: product + роль; SDK, cloud и бренд не считаются тремя независимыми решениями. Каталог не ограничен искусственным top-N; это просмотренные релевантные ветви, не заявление полного покрытия всего рынка. Rolling docs не гарантируют API в pinned package. Registry release timestamp проверен против cutoff; код пакетов не исполнялся. SDK license не распространяется автоматически на cloud/model weights/enterprise plugins.

| Продукт / версия на cutoff | Capability, hosting / license evidence | Nox mapping, действие/delta/verdict | Cost/privacy/lock-in |
|---|---|---|---|
| Mastra core 1.82.0, MCP 2.8.0 | TS self-host; Apache-2.0 по npm; native processors, MCP, memory | Head/TI/Factory reuse + configure; CONFIGURE_NATIVE | Node >=22.13; MCP требует Zod ^4.2 и core >=1.79 <2; установленный lockfile неизвестен; native не означает бесплатные модели |
| LangGraph JS 1.7.4 / LangChain core 1.4.0 | graph checkpoint/store; MIT npm; self-host + отдельный commercial LangSmith | Mission Manager defer; REJECT wholesale migration, переносить checkpoint design tests | TS совместим по языку, не по state model; второй checkpoint authority, эксплуатация БД, cloud traces |
| LlamaIndex core 0.14.25 | MIT PyPI, Python >=3.10; agents/retrieval; self-host, managed services отдельно | Memory integrate только специфический retriever/parser за existing interface; SMALL_ADAPTER | Python sidecar/serialization + двойной index; облачный parsing требует data approval |
| Haystack 3.5.0 | Apache-2.0 PyPI; Python >=3.11; composable agent/RAG pipelines | Memory defer full pipeline; специализированный retrieval adapter возможен; SMALL_ADAPTER | новый Python runtime; pipeline quality нужно измерять, framework не ACL |
| PydanticAI 2.68.0 | MIT PyPI, Python >=3.11; typed agents/durable backend docs | Factory defer; REJECT второй agent runtime; schema validation pattern переносим | typed output не authorisation; sidecar и несовместимая модель history |
| Microsoft Agent Framework 1.26.0 | Python >=3.11 registry; license metadata пусто, UNKNOWN до проверки текста; docs называют successor AutoGen/Semantic Kernel | Head defer; REJECT replacement, middleware/workflow patterns reuse | миграция не drop-in TS; Azure deployment и terms отдельно |
| AutoGen AgentChat 0.7.5 | MIT PyPI, Python >=3.10 | Factory defer legacy framework adoption; REJECT | новые investments сравнивать с successor; отсутствие latest версии не отсутствие maintenance |
| Temporal TS workflow 1.25.0 | MIT SDK npm; durable histories/replay; self-host service либо Cloud | Mission Manager defer backend только после gap; SMALL_ADAPTER условно | Node >=20.3; детерминизм/versioning, activity retry ≠ exactly-once effect; service licensing отдельно |
| Composio Mastra 0.10.6 | ISC adapter npm; SaaS connector/auth сервис отдельно | TI/tool-context integrate один adapter; SMALL_ADAPTER | peer core ^1.46 включает 1.82; Node >=22.22.3 строже Mastra; API/cloud lock-in и OAuth custody |
| Pipedream Connect | SaaS; конкретная версия/terms не подтверждены, pricing URL 404 | TI integrate альтернативу Composio при action gap; UNKNOWN | end-user connections/credits предполагают quote, не приписывать цену; code/component license не hosted SLA |
| Arcade | official tool/auth docs, rolling, commercial terms/version unknown | TI/tool-context integrate альтернативу, SMALL_ADAPTER условно | token custody/scopes/retention и pricing gate обязательны |
| ToolHive | self-host MCP management/runtime/registry/gateway; docs updated 2026-11-10, source pin/license здесь unknown (API 403) | MCPClient integrate management только при необходимости; CONNECT_READY_MADE | containers/Kubernetes ops, egress policy; MCP management ≠ Nox task authorization |
| Activepieces | кандидат из DOC-05; независимая primary feature/license pin проверка здесь не завершена | TI defer; UNKNOWN | не выбирать до version/license/cloud data review |
| n8n | self-host/cloud; Sustainable Use License, не permissive OSS | TI defer embedded customer workflows; REJECT default, коммерческое право UNKNOWN | internal business use отличается от hosting для клиентов, нужен иной договор для непокрытого use case |
| Docling 2.150.0 | MIT PyPI, Python >=3.10; self-host document conversion | Memory integrate parse→existing ingest; SMALL_ADAPTER | OCR/model compute и лицензии weights отдельно; парсинг не доверие к документу |
| Crawl4AI 0.9.5 | Apache-2.0 PyPI; self-host crawler | web tools/Memory integrate extracted content only; SMALL_ADAPTER | browser compute, site terms, SSRF, не обходить paywall/robots |
| Promptfoo 0.125.1 | MIT npm; local runner + paid platform отдельно | QA integrate; CONNECT_READY_MADE | Node >=22.22 строже core; модельные вызовы и CI оплачиваются; red-team targets только разрешённые |
| Playwright test 1.49.1 | Apache-2.0 npm; existing Nox version, MCP server version unknown | browser/QA reuse; ALREADY_EXISTS | browser sandbox/patching/CI cost; не называть test package MCP release |
| Langfuse | self-host/cloud; official MIT core, commercial /ee modules | QA/observability integrate при native gap; SMALL_ADAPTER | SCIM/audit/retention commercial; trace redaction до экспорта, свой ops cost |
| MLflow / Databricks evaluation | MLflow docs retrieved; конкретная SDK версия/license pin здесь unknown | QA integrate export evaluator evidence; SMALL_ADAPTER | judge не заменяет independent oracle; Databricks identity/data boundary нельзя перенести автоматически |
| NVIDIA NeMo Agent Toolkit 1.9.0 | Apache-2.0 PyPI; Python >=3.11 <3.14; profiler/evals | QA defer profiling sidecar; CONNECT_READY_MADE | не обязывает менять Mastra; model/NIM/AI Enterprise terms отдельно, performance claims не Nox benchmark |
| Inspect AI | official UK AISI + Meridian Labs evaluation docs; version/license pin unknown | QA defer rigorous harness; CONNECT_READY_MADE условно | isolated datasets/sandboxes и paid models; не второй production orchestrator |
| RAGFlow / Supermemory | DOC-05 candidates; primary version/terms здесь не проверены | existing Memory defer replacement; UNKNOWN | нет доказанного retrieval gap, migration/ACL/duplication риск |

### 4. Обязательный enterprise landscape: что переносить, а не покупать целиком

Все feature descriptions в этой таблице — **vendor-claim**. Нет подтверждённого использования этих продуктов в Nox и независимых сравнительных тестов. Primary URLs — раздел Sources/manifest. Версии SaaS rolling, contract/SLA/region должны быть согласованы отдельно; платных испытаний не было.

| Организация / продукт | Полезный подтверждённый docs pattern | Nox mapping и delta | Action / verdict, hosting / risks |
|---|---|---|---|
| OpenAI Agents SDK / API | guardrails и tracing; API data docs различают abuse logs и application state | existing Head/tools: guardrails применять дополнительно, tool-context остаётся effect boundary | reuse pattern / CONFIGURE_NATIVE; API SaaS, SDK self-host; default abuse retention до 30 дней, ZDR approval/endpoint limits; не предполагать ZDR |
| Anthropic Claude tool use | статья 2025-11-24: Tool Search, programmatic tool calling, examples | TI→granted tool loading; не загружать весь каталог в prompt | configure/integrate / SMALL_ADAPTER; provider-specific protocol, sandbox для generated code, API cost; токеновые claims не Nox benchmark |
| Google Vertex Agent Engine | managed agent deployment / runtime docs | Mission Manager сохраняется; managed hosting только при доказанном ops gap | defer buy / UNKNOWN; GCP regions, IAM, data processing и compute/model billing; не заменить Nox ACL облачным IAM |
| Microsoft Agent Framework | middleware/type safety/session state/workflows, successor AutoGen | Head/Factory: bounded workflow patterns, без переноса control plane | defer / REJECT replacement; Python/.NET ecosystem boundary, managed Azure отдельно |
| AWS Bedrock AgentCore | Runtime, Gateway, Identity, Memory как отдельные building blocks | MCP/grants: возможен gateway/identity adapter; Memory Nox не заменять | integrate/buy conditional / SMALL_ADAPTER; AWS IAM + OAuth/account mappings, usage billing; Runtime isolation — claim, не наш test |
| IBM watsonx Orchestrate | каталог tools, orchestration/governance; cloud/on-prem варианты | TI: подключить конкретный корпоративный action при уже выбранном IBM стеке | defer buy / UNKNOWN; полная suite дублирует Head; pricing противоречие search/direct ниже |
| Salesforce Agentforce | metered actions/conversations, CRM-centric actions | TI business pack: узкий Salesforce action, Nox policy + receipt | integrate/buy conditional / SMALL_ADAPTER; SaaS/CRM lock-in, record-level permissions и credit billing |
| ServiceNow AI Control Tower / agents | primary product URL не загрузился (timeout); community материал не принят как product guarantee | TI ITSM actions при existing Now account; не новый Nox orchestrator | defer / UNKNOWN; enterprise quote/tenant/security неизвестны, не выдумывать функции |
| GitHub Copilot cloud/coding agent | ephemeral cloud engineering environment; docs предупреждают о flawed/insecure output | engineering QA plane, не runtime capability Nox автоматически | defer buy / REJECT как замена Head; code disclosure, PR/review authority; в этом исследовании не запускать |
| Cloudflare Agents | agent runtime/capabilities, MCP, workflows docs | Mission Manager/tools: edge adapter только при deployment need | defer / SMALL_ADAPTER conditional; Workers/Durable Objects runtime не drop-in Node, state egress/region/usage costs |
| Databricks / MLflow | MLflow GenAI docs доступны; Agent Framework URL 404; code cookbook найден отдельно | QA/Memory: evaluator traces/retrieval interface, не перенос lakehouse | integrate/defer / UNKNOWN до platform need; judge bias, Unity Catalog identity не Nox grant |
| NVIDIA NeMo Agent Toolkit | existing-agent profiling, evaluators/telemetry | QA export traces to isolated profiler | integrate/defer / CONNECT_READY_MADE conditional; Python boundary, metrics privacy, NIM terms отдельно |

### 5. Стоимость, лицензии, совместимость и purchase gate

Не определены workload, accepted-task rate, регионы, ставки команды, договоры и текущий billing. Поэтому **нет честного общего $/месяц и рейтинга «дешевле на X%»**. Цены ниже — наблюдение rolling официальной страницы в дату проверки, не quote и не frozen historical contract. Поздние версии не использованы; дата first publication части страниц неизвестна.

- Salesforce primary page: **$500 / 100k Flex Credits**, стандартный action **20 credits**; пример 1,000 таких actions → 20,000 credits → **$100** consumption. Это арифметический сценарий, не прогноз: не включает underlying CRM/прочие продукты/налоги/другие rates и retries. Conversation SKU отдельно **$2/conversation**; не складывать одновременно без выбранной модели billing.
- Temporal primary pricing: старт **$50/million actions**, active storage **$0.042/GB-hour**, retained **$0.00105/GB-hour**, developer support **10% usage**. Billable action ≠ business mission. Без activity/timer/retry history и retention общий TCO не считаем. Более позднюю change history не проверили, поэтому цену использовать только как observed quote input.
- IBM: search snippet давал **$530/month**, прямой HTML в этой проверке **$578/month Essentials**, Standard **$6,360/month**. **Противоречие зафиксировано; не использовать $530 или $578 как подтверждённый договорный бюджет.** Quote/locale/дата тарифа неизвестны.
- OpenAI API pricing URL вернул **403**; Pipedream Connect pricing **404**; цены не восстановлены по памяти. Anthropic/AWS/Google/Cloudflare pricing pages сохранены, но модель, регион и tier не выбраны — total unknown. Бесплатный trial не запускали.
- OSS licence fee может быть нулевым по выбранному core license, но infrastructure/model usage/maintenance/security review/patching/migration не нулевые. Langfuse enterprise модули и n8n embedding — отдельные лицензии. Для Docling OCR/VLM/ASR weights и исходного контента нужны отдельные права.

Метод будущего сравнения:

`TCO = engineering_hours × loaded_rate + migration + fixed_subscription + model_input/output/cache + connector_actions + workflow_actions + compute/storage/egress + support + security/QA_ops`.

`cost_per_accepted_outcome = TCO / independently_accepted_tasks`; denominator — принятые результаты, не запуски. Сравнить одинаковые task strata и acceptance oracle, cold/warm cache, retries, denied calls, region, data retention, output length. При неполученном accepted результате denominator ноль, cost/result не определён, не «бесплатно». Break-even buy/reuse: сэкономленные engineering+ops должны превышать marginal provider fees и lock-in migration cost при соблюдении одинаковых security gates. Часы здесь не оценены: нет final code diff/командной ставки.

#### Native compatibility findings

npm registry подтверждает core 1.82.0 (2026-11-04) и MCP 2.8.0 (2026-11-03). MCP peer core `>=1.79.0-0 <2.0.0-0` включает reported Nox core; Zod `^4.2.0`, Node `>=22.13.0`. Это **metadata compatibility**, не executed integration. Composio adapter 0.10.6 требует Node >=22.22.3 и core ^1.46.0; Promptfoo 0.125.1 — Node >=22.22.0. Нельзя слепо включить их в среду, лишь удовлетворяющую минимуму Mastra. Полная проверка lockfile/transitive dependencies/SDK import API остаётся UNKNOWN.

Для любого buy: существующий компонент + exact unmet action + product version/terms + tenant/account scope + revoke + egress/retention/DPA + idempotency/receipt + independent QA + rollback/export. Если любое обязательное поле unknown — не закупать сейчас. Никаких новых доступов в этой lane не запрашивалось.

### 6. Что отвергнуто, что осталось research-only

1. Переписать Mastra на LangGraph/AutoGen/Agent Framework ради популярности — REJECT: baseline уже имеет управление и memory; не доказан уникальный blocking gap.
2. Одновременно добавить Composio/Pipedream/Arcade/AgentCore — REJECT: четыре auth/data boundaries без workload justification. Выбрать один на конкретный action; собственный adapter иногда дешевле посредника.
3. Tool search как security boundary — REJECT: discovery не является authority; deny/revoke нужен перед effect.
4. Новая память или enterprise platform до provenance/ACL tests — defer; недоступность current source не доказывает missing implementation.
5. Temporal как «исправление exactly-once» — REJECT тезис; replay решает durable orchestration, внешний action требует idempotency/reconciliation/fence.
6. Guardrail/LLM judge как independent QA — REJECT: нужны независимый principal, immutable evidence и deterministic oracle, визуальный продуктовый rubric отдельно.
7. Framework maturity не равна Nox readiness. Official SDK и package metadata дают переносимый implementation path, не reliability benchmark.

Research options, не задерживающие practical native wiring: Temporal durability backend, Langfuse vs MLflow trace UX, Inspect holdout benchmarks, NVIDIA profiling, managed cloud runtimes. Stop-rule применён к native selection и parsing/evals: найдены primary docs, path и P/N tests; глубина остальных ветвей ограничена явно указанными unknown, а не искусственным числом кандидатов.

### 7. Sources и локальная проверяемость

- `../source-manifest.json`, `../baseline.md`: pinned DOC-04/05/17/26 и source access history.
- `web-evidence.json`: primary URLs, HTTP results, checked_at, redirects; `sources/<id>.html/.txt` — сохранённые ответы. Получение страницы не равно полному построчному review всей HTML: анализировались релевантные capability/license/pricing sections.
- `package-evidence.json`, `pypi-evidence.json`: version, publication date, engine/peer/license metadata. Latest stable выбиралась среди releases timestamp <= 2026-11-13, без установки. Registry assertions — publisher metadata, не code verification.
- `repo-evidence.json`, `sources/*-commit.json`: GitHub API 403 для попыток pin; **не обходили отказ**. Отсутствие SHA сторонних продуктов помечено, не заменено выдуманным hash.
- `sources/framework-0.md` … `framework-4.md`: extract официальных LangGraph, PydanticAI, Temporal, Haystack, LlamaIndex docs. Это rolling docs, не обещание наличия всех описанных APIs в конкретной версии.

Основные primary ссылки:

[Mastra processors](https://mastra.ai/docs/agents/processors) · [Skills](https://mastra.ai/reference/processors/skills-processor) · [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/durable-execution) · [LlamaIndex agents](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/) · [Haystack agents](https://docs.haystack.deepset.ai/docs/agents) · [PydanticAI durability](https://ai.pydantic.dev/durable_execution/overview/) · [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/) · [Temporal workflow](https://docs.temporal.io/workflow-execution) · [Temporal pricing](https://temporal.io/pricing).

[OpenAI guardrails](https://openai.github.io/openai-agents-python/guardrails/) · [OpenAI data](https://platform.openai.com/docs/guides/your-data) · [Anthropic advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use) · [Google Agent Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview) · [AWS AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) · [IBM Orchestrate](https://www.ibm.com/products/watsonx-orchestrate) · [Salesforce pricing](https://www.salesforce.com/agentforce/pricing/) · [ServiceNow attempted source](https://www.servicenow.com/products/ai-control-tower.html) · [GitHub agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent) · [Cloudflare Agents](https://developers.cloudflare.com/agents/) · [MLflow](https://mlflow.org/docs/latest/genai/index.html) · [NeMo Toolkit](https://docs.nvidia.com/nemo/agent-toolkit/latest/index.html).

[Composio Mastra](https://docs.composio.dev/docs/providers/mastra) · [Arcade](https://docs.arcade.dev/en/home) · [ToolHive](https://docs.stacklok.com/toolhive/) · [n8n license](https://docs.n8n.io/sustainable-use-license/) · [Docling](https://docling-project.github.io/docling/) · [Crawl4AI](https://docs.crawl4ai.com/) · [Promptfoo](https://www.promptfoo.dev/docs/intro/) · [Langfuse license](https://langfuse.com/docs/open-source) · [Inspect](https://inspect.aisi.org.uk/).

#### Coverage и оставшиеся ограничения

OUT-H, GOV-05/08, S03-01/02/09, S10-01/02/03/04/07/08/10: covered with explicit unknowns. S12-05/07/09/10 и REF-06: supported через ecosystem comparison, native-first, tradeoffs, cost/license gates и evidence appendix; эта lane не сертифицирует полный общий deliverable. Не закрыты: actual accepted runtime SHA; current native processor wiring; official frozen license/source text для части кандидатов; ServiceNow product page; Databricks Agent Framework URL; independent adoption/benchmark evidence; реальные negotiated prices. Это уменьшает силу решения до conditional candidate selection, не основание менять архитектуру или начинать trial.

#### Pinned Nox источники

- [DOC-04, L1–62](https://github.com/failm3/nivict-ai-academy/blob/9b58aab1e09d8627bc006736c21b3d4790720ed7/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/R1-CAPABILITY-PROGRAM/RESEARCH/NOX-IMPLEMENTED-CAPABILITIES-SOURCE-AUDIT-2026-11-13.md#L1-L62); SHA 9b58aab1e09d8627bc006736c21b3d4790720ed7; local out/sources/docs/R1-CAPABILITY-PROGRAM/RESEARCH/NOX-IMPLEMENTED-CAPABILITIES-SOURCE-AUDIT-2026-11-13.md.
- [DOC-05, L1–154](https://github.com/failm3/nivict-ai-academy/blob/9b58aab1e09d8627bc006736c21b3d4790720ed7/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/R1-CAPABILITY-PROGRAM/RESEARCH/MARKET-REUSE-AUDIT-2026-11-13.md#L1-L154); SHA 9b58aab1e09d8627bc006736c21b3d4790720ed7; local out/sources/docs/R1-CAPABILITY-PROGRAM/RESEARCH/MARKET-REUSE-AUDIT-2026-11-13.md.
- [DOC-17, L1–104](https://github.com/failm3/nivict-ai-academy/blob/9b58aab1e09d8627bc006736c21b3d4790720ed7/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/02%20-%20%D0%90%D1%83%D0%B4%D0%B8%D1%82%204504%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2.md#L1-L104); SHA 9b58aab1e09d8627bc006736c21b3d4790720ed7; local out/sources/docs/02 - Аудит 4504 инструментов.md.
- [DOC-26, L1–16](https://github.com/failm3/nivict-ai-academy/blob/9b58aab1e09d8627bc006736c21b3d4790720ed7/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/REPORTS/NOX-R0-STATUS-2026-11-13-1430-MSK.md#L1-L16); SHA 9b58aab1e09d8627bc006736c21b3d4790720ed7; local out/sources/docs/REPORTS/NOX-R0-STATUS-2026-11-13-1430-MSK.md.


