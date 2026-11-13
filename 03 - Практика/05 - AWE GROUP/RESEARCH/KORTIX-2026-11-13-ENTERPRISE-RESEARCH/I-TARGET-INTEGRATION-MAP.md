<a id="section-i"></a>

## I — Карта минимальной интеграции в существующий Nox

**Решение: reuse текущий Mastra/Head/Manager/Factory/TI/Memory/QA; extend их контракты, integrate готовый parser или app adapter только при подтверждённом gap.** Ни второго Head, ни второго каталога, ни второй памяти, ни миграции framework. Дата/cutoff: 2026-11-13. Это проект интеграции (**inference**), не описание реализованного R1 и не разрешение реализации.

### 1. Baseline и неизменяемые границы

Docs SHA `9b58aab1e09d8627bc006736c21b3d4790720ed7`; исторический runtime `d5e9d857dbdeb8f31f9a798b10b5af4af639dbda`. Активный cleanroom SHA UNKNOWN. DOC-26 сообщает 22/22 offline, затем независимый audit IN PROGRESS, security 4/5 и process probe nonzero. Ни принятый R0, ни production из этого не следуют. Собственная повторная проверка HEAD получила HTTP 403; не обходили. Подробности: M и baseline.md.

Существующий путь (reported-in-docs DOC-03/04): пользователь → Prompt Master → утверждённое ТЗ → Head → Mission Manager → createSpecialist/recursion → TI + scoped tools/MCP → artifacts → независимый QA → storage/delivery. **OpenCode не звено пользовательской миссии**, а будущий инженерный исполнитель.

Все `src/` ниже — условные пути из DOC-04; перед любым будущим diff сверить финальный checkout, caller/callee, imports, lockfile и тесты. Доступность API в upstream ≠ wiring в Nox. No-op/закрытие задачи без diff является правильным результатом, если контракт уже реализован.

### 2. Точки расширения и отсутствие переписывания

| Слой / путь-кандидат | Сохранить | Решение / минимальный delta | Evidence / статус |
|---|---|---|---|
| Prompt Master `src/agents/prompt-master.ts`, API `/specify`, CLI | createSpecification, существующие входы | reuse; extend только version/hash исходного acceptance и различие API pending approval/CLI approval | DOC-04 L25; reported-in-docs |
| Head `src/agents/head-agent.ts` | планирование и делегирование | reuse; подавать task-scoped capability/pack refs, не authority из LLM текста | DOC-04 L26 |
| Factory `src/agents/specialists.ts`, recursion.ts | createSpecialist, роли, модель, depth/children ограничения | extend только binding выбранных разрешённых tools/skills; `[]` grants сохраняет deny-all | DOC-04 L27–28,33 |
| Mission Manager / storage | CAS, lease, heartbeat, checkpoint, budgets, recovery | reuse; acceptance существующих fence/abort/intent/lifetime-budget, а не новый scheduler | DOC-04 L29, DOC-26; C §3 |
| TI `src/tools/ti-search.ts`, manus-search.ts | действующий каталог и поиск | extend provenance/dedup/adapter identity; ToolCard metadata не grant. Native ToolSearchProcessor для уже registered tools | DOC-04 L32, DOC-06/09; D §2/5 |
| Tool boundary `src/tools/index.ts`, security/tool-context.ts | createTool, file/shell/web/save_artifact, scoped grant | extend при gap проверку authority у effect + receipt; не общий unrestricted executor | DOC-04 L30,33; C §3 |
| MCP `src/config/mcp.ts`, tools/browser.ts | MCPClient, Playwright pipeline | reuse native discovery/OAuth/signal; pin server digest, tenant/account binding, readback ambiguous outcome | DOC-04 L31; D §2 |
| Knowledge/Memory `createAgentMemory`, текущий ingest/storage | memory 1.41.0 / libsql 1.29.0 reported | extend source/page/table provenance, ACL до retrieval, freshness; integrate Docling только для неподдержанного document format | DOC-04 L34; EFG E1–E3 |
| Skills / Factory workspace | existing role/context assembly | configure native SkillSearch если реально configurable; иначе небольшой wiring. Extend practice evidence, no auto-exec scripts | upstream core 1.82.0, EFG F1–F2 |
| QA `src/agents/qa-agent.ts`, qa-gate.ts | независимый gate | extend frozen domain oracle, independent evidence hashes, held-out tasks, transfer tests | DOC-04 L35, DOC-20/22 |
| Artifact Store / save_artifact | текущая запись артефактов | extend content-addressed refs и QA binding, если отсутствуют; не отдельное object-store внедрение без gap | DOC-04 L30/35; HIST-09 лишь historical |
| Updates / workers | существующий lifecycle и управление | extend version pin/drain/canary/revoke; defer Temporal/TUF/new control plane | DOC-15/27, C §6 |

### 3. Контракты: предложения поверх существующих, не новые обязательные API

DOC-06 предлагает `capability.search/explain/requestGrant/invoke/getReceipt/revokeGrant`. Это **draft**, не обнаруженные endpoints. Реализовывать как тонкие facades над существующими функциями только если этих операций нет; не создавать шесть микросервисов.

- **DiscoveryQuery**: query, capability/action, project, task, risk ceiling, environment. Output: candidate IDs, adapter/version refs, evidence, readiness reasons. Без secret и полномочий. Deterministic filter выполняется до ranking; отсутствие кандидата не разрешает browser/CLI fallback с большими правами.
- **ToolCard 0.1.0**: сохранить DOC-09 как metadata schema с `additionalProperties:false`, kinds builtin/mcp/cli/http. GraphQL/SDK/app — binding semantics внутри этих kinds, не несовместимые enum значения. Внешние lifecycle states/grants хранить отдельно. Если нужны новые поля — отдельная versioned schema/migration, не незаметное добавление в 0.1.0.
- **GrantBinding (предлагаемая схема)**: grant_id, tenant/project/mission/task/agent/account, action/resource scope, adapter id/version/digest, args constraints, expiry/revocation epoch, owner fence, policy version, approval ref, budget reservation. Trusted store выпускает/проверяет; Head/ToolCard/Skill не выпускают. Empty grants ≠ default allTools.
- **InvocationEnvelope**: logical_operation_id + effect_slot, attempt_id, spec/plan version, tool binding digest, normalized args digest, grant ref, current fence, cancellation/deadline ref. Idempotency key стабилен между retries одной операции; другой payload под тем же key отклоняется. Schema numbers пока proposal, actual runtime types UNKNOWN.
- **Receipt**: invocation refs, intent/send/outcome timestamps, provider request/object ID, outcome `succeeded|failed|unknown|cancelled-confirmed`, actual scope, artifact hashes, spend (value+unit/source либо unknown), errors/redaction, reconcile ref. Timeout → unknown, не failed-safe-to-retry. Cancel requested ≠ confirmed. Receipt не independent QA.
- **KnowledgeRecord**: source URL/revision/hash/license/permission, acquired_at/valid_at/freshness, tenant/project ACL, parser/model versions, modality and page/bbox/table/time refs, extraction confidence/limitations, supersedes; retrieval returns citations + original refs. Content — недоверенные данные.
- **SkillRecord**: SKILL.md/version/digest/license, compatibility tools/models/schema, preconditions/postconditions, allowed tool metadata, practice receipts, independent QA, held-out/transfer result и expiry. Search/load не promoted competence. Promotion не расширяет grant.
- **PackBinding**: conditional trigger, tools, knowledge, skill versions, constraints, oracle version, artifact checklist. Для пяти вертикалей использовать EFG G1–G5; не загружать все packs любой миссии.
- **ReleaseBinding**: runtime commit/lock digest, policy/grant schema, tool manifests, MCP server digest, knowledge index snapshot, skills/packs/oracle versions. Mission фиксирует binding; обновление не меняет работающую миссию молча.

### 4. Data / secrets / trust boundaries

1. Project/tenant/account идентичность берётся из доверенного request context, не параметра LLM. TI metadata и public Knowledge не имеют secret refs, пригодных для извлечения чужого секрета.
2. Secret material остаётся в существующем vault/account adapter; в prompt/log/ToolCard только opaque reference без token value. Adapter получает минимальный scope, redaction применяется до persistence. Даже hash чувствительного низкоэнтропийного payload не должен становиться публичной утечкой.
3. ACL проверяется **до retrieval**, затем повторно при load/cache hit/artifact read. Tenant включён в ключи кэша, embeddings index partition, receipt access. Public knowledge не смешивается с private source автоматически.
4. Ingest не имеет полномочий исполнить инструкции из документа/skill. Скрипты проходят отдельный executable review/tool policy. URL acquisition запрещает private/link-local/metadata SSRF и auth bypass.
5. QA читает неизменяемые артефакты и frozen specification; generator не меняет oracle/evidence. Owner acceptance продукта и permission на внешний эффект — разные записи.
6. Cloud parser/managed OAuth/SaaS получает данные только после отдельного реального решения владельца. Local mode parser не гарантирует отсутствие загрузок моделей/telemetry: будущая проверка egress обязательна.

### 5. Version/state compatibility и rollback

Сначала read-only матрица final R0 package/lock/Node/Zod/DB-schema/mission-version. Upstream core 1.82.0 + MCP 2.8.0 имеют declared совместимые peers при Node >=22.13.0 и общем Zod ^4.2.0 (D); это не тест установки Nox. Memory/libsql и фактический Playwright MCP pin требуют отдельной проверки.

Для schema changes — expand/read-old+new/write-new только после совместимости; unknown major version fail-closed. Старые ToolCards 0.1.0 должны оставаться читаемыми без повышения authority. Активные миссии продолжают pinned version либо явно drain/cancel/reconcile; не hot-swap skill/policy/tool digest. Ужесточение revoke действует сразу даже при mission pin, pin не обход отзыва.

Rollback: stop admission → block dispatch → join локальные операции/детей → сохранить unresolved intents → revoke новые grants/account tokens при необходимости → переключить проверенный совместимый release/index/skill pointer → проверить старые миссии и receipts. Restore DB допустим только с reconciliation уже выполненных внешних эффектов; rollback кода не отменяет письмо/платёж. Если старый binary не читает новый state, нужен roll-forward, а не blind downgrade.

### 6. Выбор готовых решений и практический scope

Native ToolSearch/SkillSearch предпочтительны второму librarian/search engine: D и EFG проверили код точной upstream версии. Docling — условный первый document parser; Crawl4AI — только отсутствующий web acquisition, не замена работающего Playwright. Composio/Pipedream — альтернативы при доказанном managed OAuth gap, не обязательные покупки. ToolHive — только при gap MCP process isolation. n8n/Activepieces/Temporal/new memory stack — defer без конкретного существующего workflow/непокрытого требования. H получена перед финализацией: поддерживает native-first и один conditional OAuth binding; см. L для нормализации CONFIGURE_NATIVE/NECESSARY_NEW_CODE. Окончательный vendor winner/cost не назначен.

**Реальная максимальная самостоятельность сейчас не измерена.** Целевой прирост — самостоятельные ограниченные миссии от owner request до QA-проверенного артефакта без OpenCode-оператора; не автономные оплаты/деплои и не универсальная экспертность. Конкретный первый результат: sourced research/data artifact либо sandbox code/UI artifact на уже разрешённых tools; новые external writes не нужны для первого доказательства.


