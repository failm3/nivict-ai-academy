<a id="section-k"></a>

## K — Минимальные OpenCode-ready задания

**Не отправлены OpenCode и не разрешены к выполнению.** Сначала R0 acceptance prerequisites, затем условный R1. Все tests NOT_RUN; задачи — будущие контракты, не выполненные работы. Target paths условны до P0-01. В каждой задаче сначала найти существующую реализацию: при equivalence no-op с evidence, а не переписывание. Никакого повторного market scan: D/EFG/C и будущий H содержат конкретные варианты; только bounded compatibility/gap checks.

Общий gate R1: P0-03 + отдельный будущий разрешённый инженерный scope. Конфигурация/контент не автоматически безопасны: смена tool/policy/skill может расширить authority. Указанное config-only честно применимо только если механизм уже существует; отсутствие механизма не разрешает скрытую большую задачу. Ticket R1-09 выполняется отдельно для каждого pack; одна миссия/один oracle, не monolithic five-domain rollout.

### P0-01 — Зафиксировать финальный source SHA и imports/call paths; diff запрещён

- **phase**: R0 prerequisite
- **change_class**: read-only
- **prerequisites**: нет
- **existing_module**: final checkout/package/lock/entrypoints
- **decision**: reuse
- **diff_intent**: Зафиксировать финальный source SHA и imports/call paths; diff запрещён
- **api_schema**: Inventory: commit, lock digest, Node/Zod, module+symbol+line, state schema
- **permissions**: Лишь чтение имеющегося доступа
- **tests**: Сопоставить reachable call path; отрицательный: не выдавать DOCS_ONLY за CALL_VERIFIED
- **artifact**: r0-final-inventory.json
- **acceptance**: Каждый путь/версия подтверждён текущим snapshot либо UNKNOWN
- **blockers**: Финальный checkout недоступен; published export не замена
- **status**: BLOCKED_FOR_EXECUTION_RESEARCH_ONLY
- **test_status**: NOT_RUN
- **version**: Final R0 SHA/lock required; explicit upstream pins are evidence, not installed versions
- **rollback**: Не применимо: read-only/evidence gate, runtime не меняется
- **evidence_refs**: DOC-04; DOC-26; DOC-27; I; D/EFG/C as applicable

### P0-02 — Сверить D1–D9 и lifetime budget с финальными immutable evidence; не повторять ремонт на основании старого FAIL

- **phase**: R0 prerequisite
- **change_class**: evidence review
- **prerequisites**: P0-01
- **existing_module**: tools/security/manager/recursion/QA
- **decision**: reuse
- **diff_intent**: Сверить D1–D9 и lifetime budget с финальными immutable evidence; не повторять ремонт на основании старого FAIL
- **api_schema**: Matrix: defect→SHA→test→raw effect→independent verdict
- **permissions**: Не запускать тесты в этой research; будущая изолированная QA отдельно
- **tests**: D1 fence file write; D2 async discovery revoke; D3 immutable artifacts; D4 AWE_DATA_DIR repair isolation; D5 web_search fallback after abort; D6 browser/MCP quiescence; D7 child signal; D8 crash gap; D9 empty grants; lifetime budget restart
- **artifact**: r0-acceptance-evidence-index.json
- **acceptance**: Все критичные отрицательные сценарии имеют независимый verdict на одном release; unexplained 4/5 и probe nonzero разрешены доказательствами
- **blockers**: Нет final independent PASS; 22/22 engineering недостаточно
- **status**: BLOCKED_FOR_EXECUTION_RESEARCH_ONLY
- **test_status**: NOT_RUN
- **version**: Final R0 SHA/lock required; explicit upstream pins are evidence, not installed versions
- **rollback**: Не применимо: read-only/evidence gate, runtime не меняется
- **evidence_refs**: DOC-04; DOC-26; DOC-27; I; D/EFG/C as applicable

### P0-03 — Свести frozen R0 baseline и решение владельца; не инициировать approval

- **phase**: R0 prerequisite
- **change_class**: release gate
- **prerequisites**: P0-01,P0-02
- **existing_module**: release manifest/owner acceptance
- **decision**: reuse
- **diff_intent**: Свести frozen R0 baseline и решение владельца; не инициировать approval
- **api_schema**: ReleaseBinding + acceptance refs, scope offline/live/production отдельно
- **permissions**: Нет обращения к владельцу; фиксировать существующее решение либо UNKNOWN
- **tests**: PASS не другого SHA; отрицательный: owner GO без independent evidence не меняет technical verdict
- **artifact**: r0-release-gate.json
- **acceptance**: R0 принят в нужном scope; rollback evidence доступно; иначе BLOCKED
- **blockers**: Owner GO UNKNOWN
- **status**: BLOCKED_FOR_EXECUTION_RESEARCH_ONLY
- **test_status**: NOT_RUN
- **version**: Final R0 SHA/lock required; explicit upstream pins are evidence, not installed versions
- **rollback**: Не применимо: read-only/evidence gate, runtime не меняется
- **evidence_refs**: DOC-04; DOC-26; DOC-27; I; D/EFG/C as applicable

### R1-01 — Добавить только один approved native read-only binding в существующий каталог, не новый каталог

- **phase**: R1 conditional
- **change_class**: config-only если существующий validator
- **prerequisites**: P0-03
- **existing_module**: TI, DOC-09 ToolCard 0.1.0
- **decision**: reuse/extend
- **diff_intent**: Добавить только один approved native read-only binding в существующий каталог, не новый каталог
- **api_schema**: Exact DOC-09 schema; lifecycle/grant отдельно
- **permissions**: Metadata only; no secret/no execute authority
- **tests**: Валидная карточка читается; дополнительное поле/новый enum rejected; approved metadata без grant не вызывает tool
- **artifact**: toolcard-native-readonly.json + schema evidence
- **acceptance**: Совместимо с 0.1.0 и identity existing tool; duplicate binding не новая capability
- **blockers**: Final TI schema/validator UNKNOWN; если validator отсутствует выделить code ticket
- **status**: BLOCKED_FOR_EXECUTION_RESEARCH_ONLY
- **test_status**: NOT_RUN
- **version**: Final R0 SHA/lock required; explicit upstream pins are evidence, not installed versions
- **rollback**: Disable new binding/feature; revoke new grants; drain and reconcile; restore compatible pinned config/code/index; preserve receipts and unknown intents; no undo of external effects
- **evidence_refs**: DOC-04; DOC-26; DOC-27; I; D/EFG/C as applicable

### R1-02 — Wiring existing registered tools к native request-aware search/load/active filters; autoLoad=false

- **phase**: R1 conditional
- **change_class**: small code или no-op
- **prerequisites**: R1-01
- **existing_module**: Head/Factory + native ToolSearchProcessor core 1.82.0
- **decision**: reuse
- **diff_intent**: Wiring existing registered tools к native request-aware search/load/active filters; autoLoad=false
- **api_schema**: Existing processor API, trusted context, granted tool IDs
- **permissions**: Search result не permission; revoke проверяется при effect
- **tests**: Найден разрешённый tool; другой tenant, expired grant и load bypass rejected; [] остаётся пустым
- **artifact**: native-search-wiring.diff + tests + trace
- **acceptance**: Нет второго search service; текущие handlers неизменны; один sanctioned call trace
- **blockers**: Final imports/Node/Zod/lock; D pinned upstream, не local proof
- **status**: BLOCKED_FOR_EXECUTION_RESEARCH_ONLY
- **test_status**: NOT_RUN
- **version**: Final R0 SHA/lock required; explicit upstream pins are evidence, not installed versions
- **rollback**: Disable new binding/feature; revoke new grants; drain and reconcile; restore compatible pinned config/code/index; preserve receipts and unknown intents; no undo of external effects
- **evidence_refs**: DOC-04; DOC-26; DOC-27; I; D/EFG/C as applicable

### R1-03 — Только отсутствующий binding grant→adapter digest→args→effect; не переписывать R0 security

- **phase**: R1 conditional
- **change_class**: small code или no-op
- **prerequisites**: P0-03,R1-01
- **existing_module**: security/tool-context + createTool invoke boundary
- **decision**: extend
- **diff_intent**: Только отсутствующий binding grant→adapter digest→args→effect; не переписывать R0 security
- **api_schema**: GrantBinding/InvocationEnvelope → existing types adapter
- **permissions**: Trusted issuer; deny missing/expired/revoked/wrong account/scope/fence
- **tests**: Позитивный read; негатив wrong account, changed args, stale fence, ungranted direct invoke
- **artifact**: boundary-contract.diff + negative evidence
- **acceptance**: Каждая достижимая dispatch ветка проходит gate; zero unauthorized raw effects
- **blockers**: Не дублировать уже закрытые R0 contracts; нужен final call graph
- **status**: BLOCKED_FOR_EXECUTION_RESEARCH_ONLY
- **test_status**: NOT_RUN
- **version**: Final R0 SHA/lock required; explicit upstream pins are evidence, not installed versions
- **rollback**: Disable new binding/feature; revoke new grants; drain and reconcile; restore compatible pinned config/code/index; preserve receipts and unknown intents; no undo of external effects
- **evidence_refs**: DOC-04; DOC-26; DOC-27; I; D/EFG/C as applicable

### R1-04 — Нормализовать receipt и unresolved outcome на имеющийся intent journal; не новый outbox service

- **phase**: R1 conditional
- **change_class**: small code или no-op
- **prerequisites**: R1-03
- **existing_module**: manager storage + tools receipt/artifact
- **decision**: extend
- **diff_intent**: Нормализовать receipt и unresolved outcome на имеющийся intent journal; не новый outbox service
- **api_schema**: Receipt + stable operation/effect-slot key
- **permissions**: No blind retry non-idempotent action; evidence ACL
- **tests**: Successful readback; crash/send/ACK loss→unknown и reconcile, duplicate key diff args denied
- **artifact**: receipt-contract.diff + replay fixtures
- **acceptance**: Receipt привязан к spec/grant/artifact hash; timeout не success/cancelled
- **blockers**: Provider idempotency/readback неизвестны; только synthetic/offline до отдельного допуска
- **status**: BLOCKED_FOR_EXECUTION_RESEARCH_ONLY
- **test_status**: NOT_RUN
- **version**: Final R0 SHA/lock required; explicit upstream pins are evidence, not installed versions
- **rollback**: Disable new binding/feature; revoke new grants; drain and reconcile; restore compatible pinned config/code/index; preserve receipts and unknown intents; no undo of external effects
- **evidence_refs**: DOC-04; DOC-26; DOC-27; I; D/EFG/C as applicable

### R1-05 — Pin один уже используемый read-only server; health/discovery timeout/origin/scope config

- **phase**: R1 conditional
- **change_class**: config-only если текущий config поддерживает
- **prerequisites**: R1-03,R1-04
- **existing_module**: src/config/mcp.ts MCPClient 2.8.0
- **decision**: reuse
- **diff_intent**: Pin один уже используемый read-only server; health/discovery timeout/origin/scope config
- **api_schema**: Native listTools/listToolsets/authProvider/callTool signal
- **permissions**: Existing account only; no extra scopes; isolated profile/stdio env
- **tests**: List success vs partial error различаются; expired grant/timeout cannot claim remote stopped
- **artifact**: mcp-binding-manifest.json + trace
- **acceptance**: Exact server package/digest/license фиксированы; no new client; cancel evidence honest
- **blockers**: Actual @playwright/mcp version UNKNOWN; config API final audit; если кода нет отдельный wiring
- **status**: BLOCKED_FOR_EXECUTION_RESEARCH_ONLY
- **test_status**: NOT_RUN
- **version**: Final R0 SHA/lock required; explicit upstream pins are evidence, not installed versions
- **rollback**: Disable new binding/feature; revoke new grants; drain and reconcile; restore compatible pinned config/code/index; preserve receipts and unknown intents; no undo of external effects
- **evidence_refs**: DOC-04; DOC-26; DOC-27; I; D/EFG/C as applicable

### R1-06 — Добавить отсутствующий provenance+ACL-before-retrieval contract и citations, не вторую память

- **phase**: R1 conditional
- **change_class**: small code или no-op
- **prerequisites**: P0-03
- **existing_module**: Memory/ingest/retrieval/artifact store
- **decision**: extend
- **diff_intent**: Добавить отсутствующий provenance+ACL-before-retrieval contract и citations, не вторую память
- **api_schema**: KnowledgeRecord + tenant-scoped cache/index key
- **permissions**: Private docs не в cloud; untrusted instructions не исполняются
- **tests**: Разрешённый citation/page lookup; cross-tenant cache hit, poisoned source, expired source denied/marked stale
- **artifact**: knowledge-contract.diff + fixtures
- **acceptance**: Ссылки ведут к bytes/revision; revoke ACL закрывает cached retrieval; no secret in logs
- **blockers**: Actual memory schema/ACL/citation wiring UNKNOWN
- **status**: BLOCKED_FOR_EXECUTION_RESEARCH_ONLY
- **test_status**: NOT_RUN
- **version**: Final R0 SHA/lock required; explicit upstream pins are evidence, not installed versions
- **rollback**: Disable new binding/feature; revoke new grants; drain and reconcile; restore compatible pinned config/code/index; preserve receipts and unknown intents; no undo of external effects
- **evidence_refs**: DOC-04; DOC-26; DOC-27; I; D/EFG/C as applicable

### R1-07 — Один PDF/table fixture через ready-made parser adapter; не писать parser и не вводить отдельный orchestrator

- **phase**: R1 conditional
- **change_class**: bounded adapter code
- **prerequisites**: R1-06
- **existing_module**: existing ingest worker → Docling
- **decision**: integrate условно
- **diff_intent**: Один PDF/table fixture через ready-made parser adapter; не писать parser и не вводить отдельный orchestrator
- **api_schema**: Structured document + page/bbox/table provenance → KnowledgeRecord
- **permissions**: Local isolated parse, resource limits, no scripts/network by default
- **tests**: Сохранена структура таблицы/страницы; malformed PDF/zip bomb/timeout safe reject; no egress
- **artifact**: parser-binding manifest + structured artifact + comparison
- **acceptance**: Только если final inventory нет эквивалента и выигрывает текущий parser по заранее frozen fixture oracle
- **blockers**: Docling b9bf356f9763095ca9d51e7452a054a7db20f237 (2026-11-13T05:37:57Z), MIT; model weights/deps из EFG ledger; нет утверждённого install; local benchmark NOT_RUN
- **status**: BLOCKED_FOR_EXECUTION_RESEARCH_ONLY
- **test_status**: NOT_RUN
- **version**: Final R0 SHA/lock required; explicit upstream pins are evidence, not installed versions
- **rollback**: Disable new binding/feature; revoke new grants; drain and reconcile; restore compatible pinned config/code/index; preserve receipts and unknown intents; no undo of external effects
- **evidence_refs**: EFG E2; M; DOC-04 L34

### R1-08 — Wiring native search/load одного vetted SKILL.md; versioned competence receipt в existing memory

- **phase**: R1 conditional
- **change_class**: small code или no-op
- **prerequisites**: R1-06,R1-03
- **existing_module**: Factory/workspace native SkillSearch core 1.82.0
- **decision**: reuse/extend
- **diff_intent**: Wiring native search/load одного vetted SKILL.md; versioned competence receipt в existing memory
- **api_schema**: Agent Skills pinned spec + SkillRecord, native processor API
- **permissions**: allowed-tools metadata не grant; scripts не auto-run
- **tests**: Skill loaded authorized; injected instructions/unauthorized tool rejected; changed skill hash invalidates prior competence
- **artifact**: skill-binding.diff + practice/held-out/transfer evidence
- **acceptance**: Practice→independent QA→новая задача→transfer, ни search ни чтение не mastery
- **blockers**: Workspace skill loader/import/ACL final unknown; no claims обучения до eval
- **status**: BLOCKED_FOR_EXECUTION_RESEARCH_ONLY
- **test_status**: NOT_RUN
- **version**: Final R0 SHA/lock required; explicit upstream pins are evidence, not installed versions
- **rollback**: Disable new binding/feature; revoke new grants; drain and reconcile; restore compatible pinned config/code/index; preserve receipts and unknown intents; no undo of external effects
- **evidence_refs**: DOC-04; DOC-26; DOC-27; I; D/EFG/C as applicable

### R1-09 — Один conditional pack: data/research первым; затем отдельные UX, engineering, marketing, business

- **phase**: R1 conditional
- **change_class**: config/content-only если pack mechanism существует
- **prerequisites**: R1-08,R1-04
- **existing_module**: Factory role templates + existing QA
- **decision**: extend
- **diff_intent**: Один conditional pack: data/research первым; затем отдельные UX, engineering, marketing, business
- **api_schema**: PackBinding: trigger/tools/knowledge/skill/constraints/oracle/artifact checklist
- **permissions**: Нет полномочий рекламной публикации/CRM write/deploy; read-only artifacts
- **tests**: Relevant pack selected; irrelevant не loaded; hidden task/false citations rejected; UI technical PASS не visual PASS
- **artifact**: versioned pack + frozen domain oracle + QA report
- **acceptance**: Независимо принят owner-oriented artifact без OpenCode как оператора
- **blockers**: Точные девять полей каждого pack EFG G; если runtime pack selector отсутствует отдельный small-code ticket
- **status**: BLOCKED_FOR_EXECUTION_RESEARCH_ONLY
- **test_status**: NOT_RUN
- **version**: Final R0 SHA/lock required; explicit upstream pins are evidence, not installed versions
- **rollback**: Disable new binding/feature; revoke new grants; drain and reconcile; restore compatible pinned config/code/index; preserve receipts and unknown intents; no undo of external effects
- **evidence_refs**: DOC-04; DOC-26; DOC-27; I; D/EFG/C as applicable

### R1-10 — Зафиксировать ReleaseBinding для миссии и rollback совместимого config/skill/index

- **phase**: R1 conditional
- **change_class**: small code или no-op
- **prerequisites**: R1-04,R1-06,R1-08
- **existing_module**: existing release lifecycle/mission manager
- **decision**: extend
- **diff_intent**: Зафиксировать ReleaseBinding для миссии и rollback совместимого config/skill/index
- **api_schema**: Runtime/lock/policy/tool/skill/index/oracle version refs
- **permissions**: Revocation overrides pin; unknown state version fail-closed
- **tests**: Active mission не переключается; rollback с incompatible schema запрещён; unknown sent effects preserved
- **artifact**: compatibility matrix + canary/rollback rehearsal evidence
- **acceptance**: Drain/reconcile и restart сохраняют бюджеты/intent/evidence; нет двух owners
- **blockers**: Нет final schema migration/rollback inventory; будущие rehearsal NOT_RUN
- **status**: BLOCKED_FOR_EXECUTION_RESEARCH_ONLY
- **test_status**: NOT_RUN
- **version**: Final R0 SHA/lock required; explicit upstream pins are evidence, not installed versions
- **rollback**: Disable new binding/feature; revoke new grants; drain and reconcile; restore compatible pinned config/code/index; preserve receipts and unknown intents; no undo of external effects
- **evidence_refs**: DOC-04; DOC-26; DOC-27; I; D/EFG/C as applicable

### R1-11 — Если managed OAuth gap доказан, один Composio ИЛИ Pipedream binding; не оба и не замена TI

- **phase**: R1 conditional
- **change_class**: bounded adapter only after decision
- **prerequisites**: R1-03,R1-04,R1-10
- **existing_module**: existing createTool/MCP/account boundary
- **decision**: defer→integrate
- **diff_intent**: Если managed OAuth gap доказан, один Composio ИЛИ Pipedream binding; не оба и не замена TI
- **api_schema**: Provider pinned SDK peer+action schema+tenant/account mapping → existing envelope
- **permissions**: Отдельное реальное решение cloud/accounts/cost/scopes; revoke
- **tests**: Same isolated action; wrong tenant/account/revoked refresh denied; provider timeout→unknown
- **artifact**: vendor compatibility/licence/cost manifest + scoped receipt
- **acceptance**: Измеримый gap закрыт при меньшем полномочии и понятном TCO; иначе defer
- **blockers**: H final comparison; exact package compatibility, SaaS terms/quote/data residency unknown
- **status**: BLOCKED_FOR_EXECUTION_RESEARCH_ONLY
- **test_status**: NOT_RUN
- **version**: Final R0 SHA/lock required; explicit upstream pins are evidence, not installed versions
- **rollback**: Disable new binding/feature; revoke new grants; drain and reconcile; restore compatible pinned config/code/index; preserve receipts and unknown intents; no undo of external effects
- **evidence_refs**: DOC-04; DOC-26; DOC-27; I; D/EFG/C as applicable

### Порядок и критерий остановки

P0-01 → P0-02 → P0-03. Затем R1-01/06 → R1-02/03 → R1-04 → R1-05/08 → R1-09 → R1-10. R1-07 optional format gap; R1-11 optional managed OAuth gap, не блокируют первый native-only outcome. Зависимости tickets.json приоритетнее компактной иллюстрации порядка. Если source audit показывает закрытый gap, ticket закрывается доказанным no-op. Если primary evidence + integration path + positive/negative oracle готовы, не углублять vendor scan этого класса; переходить к незакрытым требованиям. Число tickets не оценка дней или бюджета.


