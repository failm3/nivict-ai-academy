<a id="section-d"></a>

## D — Инструменты и детерминированный библиотекарь NOX

**Рекомендация: reuse существующих Mastra Tools/MCPClient, TI и R0 policy/QA; extend только связь approved adapter → scoped grant → effect → receipt. Покупка посредника сейчас не обоснована.** ToolSearchProcessor действительно присутствует в точной версии upstream; это устраняет повод писать второй поисковый брокер, но не доказывает его wiring в Nox и не заменяет авторизацию. Исследование — не разрешение реализации R1.

Проверка: **2026-11-13 UTC**, cutoff 2026-11-13. Только GET и статическое чтение; установки, испытания, dispatch, изменение AWE, публикации не выполнялись. Сырые ответы и SHA256: `tools-connectors-librarian-sources.json`, `evidence/`. Статусы: **verified-in-code** — прочитанный конкретный код, не runtime; **reported-in-docs** — утверждение инженерного документа; **vendor-claim** — официальная документация поставщика; **inference** — проектный вывод; **unknown** — доказательств нет.

### 1. Реальный baseline и границы

Повторный GitHub GET commits/main: документация `9b58aab1e09d8627bc006736c21b3d4790720ed7`, committer 2026-11-13 11:34:38Z; runtime export `d5e9d857dbdeb8f31f9a798b10b5af4af639dbda`, 2026-11-11 12:08:07Z. **Это не SHA активного cleanroom.** DOC-26 сообщает 22/22 suites после remediation; independent final QA и owner GO этим не доказаны. R0 не объявляется завершённым.

DOC-04 сообщает существующие `src/tools/index.ts` (file/shell/http/search/save_artifact), `src/config/mcp.ts`/`src/tools/browser.ts` (Playwright MCP), `src/tools/ti-search.ts`, `src/tools/manus-search.ts`, `src/security/tool-context.ts`, `createSpecialist`, Head, Memory и QA. Здесь статус **reported-in-docs**, потому что первичный current filesystem/Recorder недоступен. Не пересоздавать их. `@playwright/test 1.49.1` не является версией `@playwright/mcp`; запуск через неприкреплённый npx в отчёте — повод проверить lock/digest, не запускать npx здесь.

Historical `awe/tool_registry/runtime-adapter.mjs:1–11` прямо требует `physical_decision: DENY`, `dispatch_supported:false`; metadata binding не runtime binary. Это **verified-in-code только historical export**; нельзя переносить вывод «нет dispatch» на нынешний cleanroom. [Код](https://github.com/failm3/awe-group-runtime/blob/d5e9d857dbdeb8f31f9a798b10b5af4af639dbda/awe/tool_registry/runtime-adapter.mjs#L1-L11).

Обязательные DOC-04,06–09,17–19 и DOC-26 сохранены полностью; baseline.md — полученный baseline оркестратора, а не заявление, что эта lane самостоятельно перечитала все 28 его источников. DOC-06 содержит **предложенные**, не существующие API `capability.search/explain/requestGrant/invoke/getReceipt/revokeGrant`. DOC-09 — draft metadata schema, не enforcement.

### 2. Version-pinned Mastra: что реально можно reuse

Оба annotated git tags `@mastra/core@1.82.0`, `@mastra/mcp@2.8.0` разрешились в **6e8dfcb83facb0861ebefa4fee384429a113acf4**, commit 2026-11-03 23:45:58Z. npm publish core: 2026-11-04 00:00:59.451Z; MCP: 2026-11-03 23:55:05.171Z — до cutoff. Метаданные npm: Apache-2.0, Node >=22.13.0; core Zod `^3.25.0 || ^4.0.0`, MCP Zod `^4.2.0`, core peer `>=1.79.0-0 <2.0.0-0`. Таким образом **1.82.0 удовлетворяет declared MCP peer range**; общий Zod должен удовлетворять ^4.2.0. Это manifest compatibility, не успешная сборка/исполнение. Фактический lockfile Nox неизвестен.

| API, точное доказательство upstream | Возможность | Delta к Nox и ограничение |
|---|---|---|
| [ToolSearchProcessor options L28–145](https://github.com/mastra-ai/mastra/blob/6e8dfcb83facb0861ebefa4fee384429a113acf4/packages/core/src/processors/processors/tool-search.ts#L28-L145), [implementation L241–265](https://github.com/mastra-ai/mastra/blob/6e8dfcb83facb0861ebefa4fee384429a113acf4/packages/core/src/processors/processors/tool-search.ts#L241-L265) | BM25 search, search_tools/load_tool, topK default 5, autoLoad default false; request-aware filter search/load/active | **reuse** для already registered tools, сохранить autoLoad=false в пилоте; разрешённые tools фильтровать на каждом шаге. Native BM25 не объявлять semantic embeddings/hybrid |
| [createTool/Tool requireApproval L243–280](https://github.com/mastra-ai/mastra/blob/6e8dfcb83facb0861ebefa4fee384429a113acf4/packages/core/src/tools/tool.ts#L243-L280), [constructor L417–441](https://github.com/mastra-ai/mastra/blob/6e8dfcb83facb0861ebefa4fee384429a113acf4/packages/core/src/tools/tool.ts#L417-L441) | Typed execute, схемы, approval flag/function | **reuse** существующих createTool; **extend** R0 effect check. Human approval option не durable tenant-scoped capability и не защита всех прямых вызовов |
| [MCPClient listTools L1186–1235](https://github.com/mastra-ai/mastra/blob/6e8dfcb83facb0861ebefa4fee384429a113acf4/packages/mcp/src/client/configuration.ts#L1186-L1235), [listToolsets L1275–1320](https://github.com/mastra-ai/mastra/blob/6e8dfcb83facb0861ebefa4fee384429a113acf4/packages/mcp/src/client/configuration.ts#L1275-L1320) | Native discovery, namespaced sets, variants returning errors | **reuse** MCPClient, не создавать второй клиент. Отдельно различать partial discovery failure и пустой успешный каталог |
| [StreamableHTTP + authProvider L642–705](https://github.com/mastra-ai/mastra/blob/6e8dfcb83facb0861ebefa4fee384429a113acf4/packages/mcp/src/client/client.ts#L642-L705) | Native HTTP transport/OAuth plumbing | **reuse**, но tenant token store, account binding, scopes и revocation сверять с R0; поддержка OAuth в библиотеке не готовая enterprise identity система |
| [callTool + timeout/signal L1760–1855](https://github.com/mastra-ai/mastra/blob/6e8dfcb83facb0861ebefa4fee384429a113acf4/packages/mcp/src/client/client.ts#L1760-L1855) | AbortSignal передаётся MCP SDK, timeout в callTool | **reuse → extend** receipt/reconciliation. Signal не доказывает остановку remote effect; disconnect не rollback |

Ссылки и код доказывают наличие API в upstream, не imports/config/mission reachable/actual calls в текущем Nox. Следующий разрешённый audit должен различать эти пять ступеней. Новую зависимость нельзя оправдывать только отсутствием найденного import в ограниченном source report.

### 3. Дедуплицированный атлас pathways

Ниже **16 семейств**, не число продуктов или подключённых инструментов. Разделение: **M** metadata, **A** исполнимый adapter, **G** grant, **I** invoke, **R** receipt. Один GitHub action через SDK/REST/MCP — одна semantic capability с несколькими bindings, а не три новых навыка. Все дельты условны до source audit final R0.

Общий профиль **P0** для каждой строки: tenant/owner/project/mission/task/agent/action/resource/TTL, adapter digest и account привязаны grant; секреты только vault refs, не ToolCard/prompt; revoke/expiry проверяется у effect, не только в search. Cancel требует подтверждения остановки либо `unclear` с reconciliation. Idempotency — provider key, а при отсутствии durable intent + readback; повтор неидемпотентного действия после timeout запрещён. Receipt включает args digest, effective scope, fence/revision, attempt и provider request ID, outcome/artifact hash, время/стоимость или unknown. Policy cost относится к вызову/поставщику, не протоколу.

| Pathway / primary reference | M → A → G → I → R | Reuse / минимальный delta к Nox; версия/license/cost и особенности |
|---|---|---|
| Native Mastra Tools | schema/createTool → existing handler → R0 grant → execute → typed result+artifact | **reuse** index.ts; **extend** binding P0. core 1.82.0 Apache-2.0; локальные compute/model costs не нулевые автоматически; cancel кооперативный |
| [MCP 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) | registry/listTools → pinned server + MCPClient → local P0 и OAuth → tools/call → result/isError + readback | **reuse** mcp.ts. MCP 2.8.0; протокол не лицензия server. Registry не trust/health approval. notifications/cancelled best effort; tool annotations не ACL и не гарантия идемпотентности |
| [REST/OpenAPI 3.1.1](https://spec.openapis.org/oas/v3.1.1.html) | operationId/spec digest → HTTP wrapper → method/path/account scope → request → status/body/provider ID | **reuse** web_fetch для public reads; **extend** write-specific adapter при доказанном gap. securitySchemes не выдают tokens; API/OAS license и тарифы отдельно. Timeout не undo; idempotency только documented endpoint |
| [GraphQL September 2025](https://spec.graphql.org/September2025/) | SDL/query hash → HTTP GraphQL adapter → operation/field/resource scopes → query/mutation → data+errors | **extend** HTTP boundary, не отдельный broker. Query depth/complexity limits; не объявлять read-only по HTTP POST; mutation retry dangerous. Server license/cost unknown |
| SDK | package/type schemas → pinned SDK wrapper → P0/provider token → method → normalized result/provider ID | **extend** createTool, когда SDK добавляет signing/pagination. Pin package/transitive digests/license. Retry defaults SDK проверить; несовместимость Node/Zod блокирует |
| CLI | help/version metadata → executable digest + argv allowlist → workspace/env grant → spawn no shell → exit/stdout/stderr/artifacts | **reuse** shell tool, **extend** per-command envelopes. Процесс group kill + join; нулевой exit не доказательство эффекта; лицензия каждого бинарника, compute cost |
| Browser automation | action schema → existing Playwright MCP wrapper → origin/profile/download scope → action → screenshot/DOM/readback | **reuse** browser.ts, не второй browser. @playwright/mcp фактическая версия unknown; Apache-2.0 upstream, third-party terms отдельно. Stop browser task не отменяет click/send; общий profile между tenants запрещён |
| [DevTools/CDP](https://chromedevtools.github.io/devtools-protocol/) | protocol domain/method → version-matched CDP adapter → target/session grant → CDP command → metrics/trace | **integrate только gap** browser debugging. Tip-of-tree нестабилен; pin browser protocol, не публичный debug port. CDP доступ широкий, isolate process/profile; no implicit rollback |
| Computer-use | screen/action metadata → OS session input adapter → machine/window/session grant → input → before/after image+audit | **defer**, пока browser/API достаточно; **extend** existing worker, не новый planner. Actual Nox adapter unknown. Lock screen, clipboard/file/credential boundaries; click not idempotent; commercial SDK terms unknown |
| [Git](https://git-scm.com/docs/git-rev-parse) | repo/ref/commit → existing CLI or provider read API → repo/path/read scope → show/diff → blob/commit digest | **reuse** shell/HTTP under P0. Pin Git version; GPLv2 Git не лицензия репозитория. Push/PR отдельные actions, никогда fallback. Content hash не attest current deployment |
| [SSH](https://man.openbsd.org/sshd_config) | host key/command contract → SSH executor → host/principal/forced-command → remote command → remote receipt+exit | **defer** при отсутствии доказанной remote потребности. Host key pin, no agent forwarding, no arbitrary shell; kill local SSH не доказывает remote stop. OpenSSH/license конкретной сборки проверить; host costs |
| [SQL/Postgres 17](https://www.postgresql.org/docs/17/sql-set-transaction.html) | schema/query template → DB driver → role/tenant/RLS/readonly → transaction → rows/commit ID | **reuse** TI DB API/libsql boundary, не новый DB. Read-only transaction + query whitelist, cancellation query и rollback/readback; lost commit ack = unclear. Postgres reference не доказывает TI version; driver/license unknown |
| [Webhooks](https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks) | event schema/subscription → receiver → issuer signature+tenant mapping → durable inbox → ack+processing receipt | **extend** existing API, не autonomous mission authority. Delivery ID replay dedup, signature raw bytes, secret rotation. 2xx ack не completed action; subscription cost/provider terms |
| [Queue/RabbitMQ](https://www.rabbitmq.com/docs/confirms) | topic/payload contract → consumer → tenant/topic grant → dequeue/process → ack + effect receipt | **extend** manager boundary только если нужна async delivery. Broker ack/publisher confirm не exactly-once business action. Inbox/outbox, dedup, poison messages, lease fence; конкретная версия/license/hosting unknown |
| [RPA/UiPath Orchestrator API](https://docs.uipath.com/orchestrator/automation-cloud/latest/api-guide/about-odata-and-references) | process/job schema → vendor API adapter → folder/robot scope → start job → terminal job + artifact | **defer/buy условно** для legacy UI без API, не второй Head. Cloud latest не pinned Nox-compatible; job stop не undo, license/robot costs требуют quote, trials не запускались |
| Specialized app | app operation/schema → REST/SDK/MCP binding → app account+resource grant → business action → provider object/readback | **integrate один binding** в existing createTool. CAD/design/CRM etc не новый transport. Pin app API version; UI-only fallback не получает больший scope; app subscription/terms отдельно |

Без complete input/output schemas, success/error examples с evidence и валидного grant pathway остаётся **candidate**, даже если metadata выглядит полноценной. Таблица — архитектурная классификация/inference, не 16 проверенных реализаций.

### 4. Посредники: только точечный missing link

Для всех: **никакой live compatibility Nox не проверено**. Дата чтения 2026-11-13; SaaS docs и цены — mutable vendor-claim, не immutable релиз/договор. Код лицензии фиксирован SHA (приложение Sources). Нельзя лицензией SDK обосновывать право self-host полного SaaS.

| Кандидат и официальные docs | Что добавляет сверх native | License/version/security/cost | Решение + delta / проверка |
|---|---|---|---|
| [Composio Mastra](https://docs.composio.dev/docs/providers/mastra) | provider превращает tools в Mastra format с input/output schemas; sessions/auth/tool routing | MIT репозитория на pinned SHA; hosted API отдельные условия. Docs не фиксируют совместимую версию @composio/mastra. [Pricing](https://composio.dev/pricing) сохранён, effective quote для Nox unknown | **integrate условно**, existing createTool/MCP/auth boundary; missing managed app auth, не search engine. Проверить tenant entity/session, scopes/revoke, wrapper peer deps, provider error→receipt; не давать vendor session authority на весь allTools |
| [Pipedream Connect](https://pipedream.com/docs/connect) | managed auth/refresh, API proxy, app actions/MCP | Pipedream Source Available License 1.0 для repo, не permissive OSS всего сервиса. [Pricing](https://pipedream.com/pricing); старый /docs/connect/pricing вернул 404. Account-specific tariff unknown | **integrate альтернатива Composio**, не вместе без gap. P0 поверх external user/account mapping, budget на proxy/action; vendor refresh не заменяет revoke локального grant |
| [Arcade](https://docs.arcade.dev/en/home) | actions runtime, OAuth/user tokens, policy — vendor-claim | arcade-mcp MIT, не облачная лицензия; [pricing](https://www.arcade.dev/pricing): Free 2000 calls/month, Team $25/month + $0.01/call, enterprise quote (snapshot, не итоговая цена Nox) | **defer**, сравнивать на той же action/scopes задаче при gap первых вариантов. Local R0 policy остаётся final gate, vendor tool result не QA |
| [ToolHive](https://docs.stacklok.com/toolhive/) | run/manage/isolate MCP servers, registry/operator | Apache-2.0 pinned core; infra/ops costs, enterprise quote unknown; docs не доказали deployment Nox/WSL2 | **integrate условно** под existing MCPClient только если isolation/process lifecycle gap не закрыт R0. Не второй TI и не новый mission orchestrator |
| [Activepieces](https://www.activepieces.com/docs) | flows/pieces/MCP, app automation | repo mixed: MIT вне указанных enterprise directories; EE separate. [Pricing](https://www.activepieces.com/pricing): Plus $20/month, Team $200, Embed from $36k/year; snapshot, credits/eligibility проверить | **defer/buy условно** как bounded external recipe endpoint, не замена Factory. Flow version, connection scopes, run cancellation и business readback обязательны |
| [n8n MCP](https://docs.n8n.io/advanced-ai/accessing-n8n-mcp-server/) | exposed workflow discovery/execution; current docs также describe create/edit — широкая поверхность | [Sustainable Use / Enterprise](https://docs.n8n.io/sustainable-use-license/), не unrestricted OSI OSS. [Pricing](https://n8n.io/pricing/): Starter €20/month billed annually, 2.5K executions; snapshot | **defer** при отсутствии существующего нужного workflow. Если reuse workflow — expose read/exact approved run only, не workflow authoring всем агентам. License embedding/resale отдельно review |

Ни один посредник не доказывает joined abort, exactly-once side effects, tenant isolation Nox или independent QA просто наличием в docs этих слов. Предпочтение native — не утверждение, что native решает managed OAuth для всех бизнес-приложений.

Формула сравнения без выдуманных workloads: `TCO = fixed plan + billable calls/credits/executions + upstream app/API/model costs + storage/egress/worker + auth/operations engineering`. Параметры тарифов, регион/налоги, retry, fanout, minimum commitment и latency неизвестны; числовой ROI/benchmark не рассчитывался. Free tier не отменяет security/license gates.

### 5. Tool Intelligence и детерминированный библиотекарь

**reported-in-docs:** DOC-17 исторически 4504 rows / 4466 unique full URLs / 38 duplicates; это URL-дедуп, не доказательство 4466 разных capabilities. DOC-18 handoff commit `58d3132c139b3e45ff7cd24289a2d618d87d373a`, 96 source files, 3415 candidates, approved_executable_records=0. Bundle недоступен; цифры не пересчитаны. 3415 и 4504 — разные datasets/stages, не measurement падения покрытия. DOC-19 предлагает incremental provenance/verification pipeline; его разрешения старому исполнителю не разрешают запуск collectors здесь.

**extend TI, не второй каталог:**
1. Сохранить raw source/capture hash и alias URL без перезаписи. Canonical product ID по official owner/repo/package namespace, release ID по version+digest, capability ID по action semantics, binding ID по adapter/API endpoint+version. Tracking params можно удалить только из display URL, не из evidence URL. Не объединять forks, облако/self-host, paid/free edition без explicit relationship.
2. Exact dedup по canonical ID/digest; fuzzy name/embedding только `possible_duplicate`, не автоматическое слияние scope/license. Один action с native/MCP/SDK bindings хранить один раз, варианты исполнения отдельно.
3. Taxonomy: domain × verb × resource × risk × transport; alias на русском/английском. Сначала ACL/trust/freshness/compatibility hard filters, затем native BM25. Семантическую/hybrid ветку добавить в существующий TI только при измеренном recall gap и frozen dataset; модель предлагает relevance, не grant.
4. Детерминированный выбор: eligible set → approved connected exact digest → resource fit → native preference при равном fit → measured health/cost (unknown не zero) → stable canonical ID tie-break. Сохранять query, policy/ranking revision и candidate snapshot, чтобы повторить объяснение. Не выдавать полнотекстовые credentials или чужие tenant metadata через search.
5. `explain`: source/version, why/when-not, schema digest, bounded successful example с receipt либо явно synthetic, common typed errors, compatible lock/environment, known limitations, last verification и expiry. Ни один пример документации не отмечать как успешный Nox call.
6. Состояния независимы: metadata verified, adapter built, security approved, account connected, grant active, invoked, receipted, QA accepted. Нельзя одним `status: approved` выразить всю матрицу.
7. Документы и ToolCard — untrusted data. Registry package command/download URL не исполнять; запрет auto-install. License/security advisory/schema digest drift переводит affected binding в review, не молчаливое обновление live mission.
8. Обучение применению: existing specialist/QA + memory сохраняют recipe version с exact tool/schema/environment и actual receipt. Practice → независимая QA → held-out новая задача → transfer evidence. Reading docs не mastery; recipe не увеличивает privilege.

### 6. Grant, invocation, receipts: минимальный недублирующий контракт

**extend существующих R0 tool-context/manager/store**, только после проверки незакрытого gap. Нужны две независимые оси: catalog approval и runtime authorization. LLM может предложить capability/args; grant issuer применяет deterministic policy и authoritative identity. OAuth scope обычно шире конкретного business resource, поэтому OAuth token никогда сам по себе не является Nox grant. OIDC authentication пользователя не заменяет OAuth resource authorization.

Перед effect: атомарно проверить current grant revision/expiry/revoke, mission lease/fence, adapter digest, normalized resource и reserved budget; удержать durable intent. Intent должен содержать idempotency key с семантикой provider endpoint. Retry после unknown outcome — reconcile first. Статус `cancelled` допустим после подтверждения quiescence; иначе `unclear`, не ложный успех. Сохранить attempted/started/completed и поздний provider result, даже после локального revoke; revoke не стирает аудит и не отменяет совершённый эффект.

MCP [authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) описывает HTTP OAuth discovery/resource binding; stdio credentials требуют отдельного режима. Token audience/resource, redirect allowlist, PKCE и storage review обязательны; не передавать токен произвольному downstream host. [Cancellation](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/cancellation) optional и race-prone: это не distributed transaction rollback. Для REST [Stripe idempotency](https://docs.stripe.com/api/idempotent_requests) — пример endpoint-defined guarantee, не универсальное свойство любого HTTP POST.

### 7. Draft и acceptance

`ToolCard-draft.json` — **не executable**, дополнительные research поля к DOC-09. Не выдаётся за backward-compatible валидный instance DOC-09. Разделяет schema/artifact digest, source evidence, compatible runtime, license/cost и binding state; grant/invocation отсутствуют по умолчанию. `TG-constraints.md` сохраняет все 6 positive + 12 negative исходного acceptance и уточняет oracle. Ничего не запускалось; ни одного PASS здесь нет.

Минимальный future pilot из DOC-06 сохраняется: existing workspace_read/write, test_runner, browser.screenshot, public_read; 5–10 allowlisted connected tools — **предложение документа**, не уже имеющийся live count. Первым безопасным кандидатом остаётся browser screenshot через existing Playwright/MCP, а не новая SaaS подписка. Условия: final R0 SHA+QA+owner GO, затем отдельная авторизация R1, version inventory и frozen tests.

### 8. Ограничения доступа, дат и полноты

| Источник/метод | Результат и влияние |
|---|---|
| current cleanroom `/home/nox/awe-group-cleanroom-20261112`, TI-v2 bundle | Нет доступной копии в этой lane; нет новых логинов/секретов. Actual lockfile, imports, active grants, adapters UNKNOWN |
| Recorder/Observer | Полученный baseline документирует public GET 404; повторный обход/новый доступ не предпринимался. DOC-04 остаётся reported, не самостоятельно verified current code |
| `https://docs.composio.dev/docs/auth-configuration` GET | 404; не трактуется как отсутствие auth. Альтернативный official docs путь зафиксирован в ledger |
| `https://pipedream.com/docs/connect/pricing` GET | 404; проверен официальный /pricing, quote не установлен |
| `https://www.activepieces.com/docs/about/overview` GET | 404; проверен /docs, detailed pinned runtime API compatibility unknown |
| Vendor current docs/pricing | Получены до cutoff, но не имеют гарантированного исторического version pin. Не переносить live claims на старые releases. Upstream код/licenses pinned commit, Mastra npm publish times сверены |
| Source collector filename collision | `code-types.ts` и `code-package.json` последовательно перезаписаны MCP версиями; core types отдельно сохранён `mastra-core-types.txt`, core npm manifests отдельно. Исходные superseded ledger rows помечены в финальном ledger; не использовать их как retained evidence |

### 9. Requirement traceability

| IDs | Покрытие |
|---|---|
| S04-01, S04-10 | §5: taxonomy/ranking/dedup, history vs v2, непроверенные counts |
| S04-02 | §3 M/A/G/I/R, §5 независимые состояния |
| S04-03 | §5 explain/schema/examples/errors, ToolCard |
| S04-04 | §2 exact versions, §4 vendors, §8 gaps; health live UNKNOWN |
| S04-05 | §2 ToolSearch native + filter, §5 dynamic allowed set |
| S04-06 | §3 P0, §6 scopes/OAuth/vault/revoke |
| S04-07 | §3 all pathways, §6 cancellation/idempotency/receipt, TG constraints |
| S04-08 | §5 recipe practice→QA→held-out transfer, не новый skill store |
| S04-09 | §5 registry/source quarantine, запрет automatic install |
| S04-11, OUT-D | §3 все 16 named pathways, §4 broker comparison |
| S04-12, REF-01, REF-03, REF-10 | native/version-pinned §2 и primary vendor/spec §4/6; полный source ledger. Coverage research, не runtime acceptance |

### Sources

Полный воспроизводимый реестр URL/GET status/timestamp/SHA256/pinned links — `tools-connectors-librarian-sources.json`. Сохранённые snapshots — `evidence/`; постоянные ссылки DOC и licenses ниже генерируются из реестра. Все product/API claims выше либо vendor-claim, либо явно tagged code/doc/inference. Отсутствие runtime tests не скрывается.

#### Обязательные документы (точные commits)

- [DOC-04](https://github.com/failm3/nivict-ai-academy/blob/9b58aab1e09d8627bc006736c21b3d4790720ed7/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/R1-CAPABILITY-PROGRAM/RESEARCH/NOX-IMPLEMENTED-CAPABILITIES-SOURCE-AUDIT-2026-11-13.md#L1-L63): 9b58aab1e09d8627bc006736c21b3d4790720ed7; snapshot `out/evidence/DOC-04.txt`.
- [DOC-06](https://github.com/failm3/nivict-ai-academy/blob/9b58aab1e09d8627bc006736c21b3d4790720ed7/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/R1-CAPABILITY-PROGRAM/01-TOOL-GATEWAY/SPEC.md#L1-L140): 9b58aab1e09d8627bc006736c21b3d4790720ed7; snapshot `out/evidence/DOC-06.txt`.
- [DOC-07](https://github.com/failm3/nivict-ai-academy/blob/9b58aab1e09d8627bc006736c21b3d4790720ed7/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/R1-CAPABILITY-PROGRAM/01-TOOL-GATEWAY/CANDIDATES.md#L1-L56): 9b58aab1e09d8627bc006736c21b3d4790720ed7; snapshot `out/evidence/DOC-07.txt`.
- [DOC-08](https://github.com/failm3/nivict-ai-academy/blob/9b58aab1e09d8627bc006736c21b3d4790720ed7/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/R1-CAPABILITY-PROGRAM/01-TOOL-GATEWAY/ACCEPTANCE.md#L1-L46): 9b58aab1e09d8627bc006736c21b3d4790720ed7; snapshot `out/evidence/DOC-08.txt`.
- [DOC-09](https://github.com/failm3/nivict-ai-academy/blob/9b58aab1e09d8627bc006736c21b3d4790720ed7/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/R1-CAPABILITY-PROGRAM/01-TOOL-GATEWAY/tool-card.schema.json#L1-L247): 9b58aab1e09d8627bc006736c21b3d4790720ed7; snapshot `out/evidence/DOC-09.txt`.
- [DOC-17](https://github.com/failm3/nivict-ai-academy/blob/9b58aab1e09d8627bc006736c21b3d4790720ed7/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/02%20-%20%D0%90%D1%83%D0%B4%D0%B8%D1%82%204504%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2.md#L1-L105): 9b58aab1e09d8627bc006736c21b3d4790720ed7; snapshot `out/evidence/DOC-17.txt`.
- [DOC-18](https://github.com/failm3/nivict-ai-academy/blob/9b58aab1e09d8627bc006736c21b3d4790720ed7/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/CHECKPOINTS/TOOL-INTELLIGENCE-V2-OPENCODE-SOURCE-HANDOFF-2026-11-12.md#L1-L17): 9b58aab1e09d8627bc006736c21b3d4790720ed7; snapshot `out/evidence/DOC-18.txt`.
- [DOC-19](https://github.com/failm3/nivict-ai-academy/blob/9b58aab1e09d8627bc006736c21b3d4790720ed7/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/DECISIONS/AWE-TOOL-INTELLIGENCE-CONTINUOUS-MONITORING-2026-11-12.md#L1-L31): 9b58aab1e09d8627bc006736c21b3d4790720ed7; snapshot `out/evidence/DOC-19.txt`.
- [DOC-26](https://github.com/failm3/nivict-ai-academy/blob/9b58aab1e09d8627bc006736c21b3d4790720ed7/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/REPORTS/NOX-R0-STATUS-2026-11-13-1430-MSK.md#L1-L17): 9b58aab1e09d8627bc006736c21b3d4790720ed7; snapshot `out/evidence/DOC-26.txt`.
- [HIST-04](https://github.com/failm3/awe-group-runtime/blob/d5e9d857dbdeb8f31f9a798b10b5af4af639dbda/awe/tool_registry/discovery.mjs#L1-L65): d5e9d857dbdeb8f31f9a798b10b5af4af639dbda; snapshot `out/evidence/HIST-04.txt`.
- [HIST-05](https://github.com/failm3/awe-group-runtime/blob/d5e9d857dbdeb8f31f9a798b10b5af4af639dbda/awe/tool_registry/runtime-adapter.mjs#L1-L12): d5e9d857dbdeb8f31f9a798b10b5af4af639dbda; snapshot `out/evidence/HIST-05.txt`.

#### Pinned license evidence

- [composio: MIT](https://github.com/ComposioHQ/composio/blob/5edfe135ac62517bf88efadb23222e51f792792f/LICENSE) — точный commit в URL, лицензия пакета/дерева, не облачного сервиса.
- [pipedream: NOASSERTION](https://github.com/PipedreamHQ/pipedream/blob/63e1c79655312cada2cf962f8a5dc11a1248c9b2/LICENSE) — точный commit в URL, лицензия пакета/дерева, не облачного сервиса.
- [arcade-mcp: MIT](https://github.com/ArcadeAI/arcade-mcp/blob/c623488f15096d49445f5f4390362434c640204b/LICENSE) — точный commit в URL, лицензия пакета/дерева, не облачного сервиса.
- [toolhive: Apache-2.0](https://github.com/stacklok/toolhive/blob/5f36b560c10ffdcdc6e177e5ec574a521b65915c/LICENSE) — точный commit в URL, лицензия пакета/дерева, не облачного сервиса.
- [activepieces: NOASSERTION](https://github.com/activepieces/activepieces/blob/ef02b406b5ee463ef79c81272f3160eee0ea0a5f/LICENSE) — точный commit в URL, лицензия пакета/дерева, не облачного сервиса.
- [n8n: NOASSERTION](https://github.com/n8n-io/n8n/blob/fb2cc9b80836337e4caab9b3f729823a3aa27861/LICENSE.md) — точный commit в URL, лицензия пакета/дерева, не облачного сервиса.
- [playwright-mcp: Apache-2.0](https://github.com/microsoft/playwright-mcp/blob/78eca85361efb545a4c0f59b6140aef0721c5412/LICENSE) — точный commit в URL, лицензия пакета/дерева, не облачного сервиса.
- [registry: NOASSERTION](https://github.com/modelcontextprotocol/registry/blob/115f85225c9fac5281d8a2dc8551cf49b004d2f9/LICENSE) — точный commit в URL, лицензия пакета/дерева, не облачного сервиса.


