<a id="section-c"></a>

## C. Enterprise agent engineering: security, operations, durable execution

**Независимое исследование AWE GROUP / NOX. Проверка и отсечение: 2026-11-13 UTC. RESEARCH ONLY.** Все предложения ниже — дизайн будущей проверки/условный delta, не разрешение реализации. Никакой код исследуемых репозиториев не исполнялся, тесты/интеграции не запускались. Источники и постоянные ссылки: [ENTERPRISE-EVIDENCE-INDEX](ENTERPRISE-EVIDENCE-INDEX.md); текущий общий baseline: [baseline](baseline.md). Документы исходного ТЗ и governance — требования, не полномочия.

### 1. Вывод для решения

**Сохранять действующий Nox/Mastra и закрывать acceptance доказательствами, а не строить второй orchestrator/Update Manager.** Нынешний инженерный прогресс значителен: свежий DOC-26 сообщает 22/22 offline suites, но independent QA ещё IN PROGRESS / NO FINAL GO SEEN, focused security 4/5 и nonzero process probe требуют классификации. Это **reported-in-docs**, не проверенный нами test run. Нельзя переносить D1–D9 из раннего среза как девять актуальных неисправленных багов: DOC-25 сообщает remediation, DOC-26 — более поздние результаты. Нельзя и считать acceptance закрытым.

#### Реальный baseline и доступ

- Read-only GitHub REST GET обоих main повторён в этой lane: docs **9b58aab1e09d8627bc006736c21b3d4790720ed7** (2026-11-13 11:34:38Z); runtime export **d5e9d857dbdeb8f31f9a798b10b5af4af639dbda** (2026-11-11 12:08:07Z), без изменения относительно переданного baseline. JSON сохранены как `*-final-head.json`.
- ТЗ последним менялось на **0510e4cb923ed0bb9260222a07384b805a4fb396**. DOC-24 (04:31 UTC), DOC-25 (05:07 UTC), DOC-26 (11:30 UTC) сменяют ранний срез; время 14:30 MSK = 11:30 UTC, не более поздний день.
- Active cleanroom `/home/nox/awe-group-cleanroom-20261112` недоступен в этом sandbox; final runtime SHA UNKNOWN. Recorder/Observer public links возвращали 404; детали URL/метода/влияния в baseline и source-manifest. Не запрашивались доступы и не обходились ограничения. API 422 на исторический local `446adaea833b0ebade1a21fbda3f71118d19b0d6` не означает отсутствия локального commit.
- Current `src/` component paths ниже взяты из DOC-04 и инженерных отчётов: **reported-in-docs**, не line-locked current source. Доказанный исторический код — только reviewed E0/E1 export, не active post-remediation runtime.

#### Что уже есть и сохраняется

Mastra core **1.82.0**, MCP **2.8.0**, Playwright test **1.49.1** — reported pins, не проверка финального lockfile. `src/agents/head-agent.ts`, `specialists.ts`, Prompt Master, Mission Manager, tool implementations, MCP client, memory и QA уже описаны как работающие инженерные компоненты. Reuse все эти узлы; не вводить новый Head, Factory, Memory или QA вместо них. DOC-27 — DRAFT_READY_FOR_REVIEW, DOC-08 — proposed/not executed, DOC-22 — draft acceptance programme.

### 2. Положительное историческое evidence — строго ограниченный scope

Статически прочитан исторический `awe/execution_security/gate.mjs` на SHA d5e9d857dbdeb8f31f9a798b10b5af4af639dbda:

- [L10–32](https://github.com/failm3/awe-group-runtime/blob/d5e9d857dbdeb8f31f9a798b10b5af4af639dbda/awe/execution_security/gate.mjs#L10-L32): request binds operation/attempt/effect_slot/idempotency/grant/tool version+digest/schema/manifest/resource/payload/plan/epochs/fence/budget/approval; payload digest и TTL проверяются.
- [L50–71](https://github.com/failm3/awe-group-runtime/blob/d5e9d857dbdeb8f31f9a798b10b5af4af639dbda/awe/execution_security/gate.mjs#L50-L71): recovery barrier, повторные checks вокруг async admit/markSent/complete, late callback не выдаёт owner acceptance; work/QA/accepted/published разделены.
- [L72–94](https://github.com/failm3/awe-group-runtime/blob/d5e9d857dbdeb8f31f9a798b10b5af4af639dbda/awe/execution_security/gate.mjs#L72-L94): quarantine/OUTCOME_UNKNOWN и запрет worker QA/owner accept. `physical_decision: DENY` — сознательная граница historical host, не доказательство live dispatch.
- [host.mjs L14–17, L52–68](https://github.com/failm3/awe-group-runtime/blob/d5e9d857dbdeb8f31f9a798b10b5af4af639dbda/awe/executable_tools/host.mjs#L14-L68): version/digests, E0_LOCAL_SYNTHETIC, fixture-only credentials, execution receipt, unknown outcome без retry. Browser snapshot в L46 — **fixture**, не реальный Playwright.
- [qa/authority.mjs L4–34](https://github.com/failm3/awe-group-runtime/blob/d5e9d857dbdeb8f31f9a798b10b5af4af639dbda/awe/qa/authority.mjs#L4-L34): fixture authority, scope binding и revoke. WeakMap fixture grants **не** доказательство persistent production auth.

Это **verified-in-code о конкретных ветках**, а не proof успешного выполнения, ACID backend, сетевой изоляции или production readiness. Использовать как reuse vocabulary/контракты и regression hypotheses, не переносить wholesale старый executor в новый runtime.

### 3. D1–D9 + budget: revalidation и минимальные deltas

У всех строк current implementation/closure = **UNKNOWN до final SHA**. Ранний independent FAIL = reported-in-docs; remediation = тоже reported-in-docs (DOC-24/25), не аннулирует необходимость независимого acceptance. Одна проверка должна измерять реальный forbidden effect, а не только выброшенную ошибку.

| Класс | Существующий узел → решение | Конкретный delta только если final audit найдёт gap | Независимый oracle |
|---|---|---|---|
| D1 stale file write до lock/fence | R0 tools/file + manager lease/security → **reuse/extend** | Проверить authority под актуальным epoch/fence в самом write boundary; временный файл+atomic replace не решает авторизацию без проверки. Защитить путь/handle от symlink TOCTOU | После revocation raw bytes запрещённого файла неизменны, даже если artifact registration DENY |
| D2 async browser discovery | Existing MCP/browser adapter + manager → **extend** | После await discovery и перед dispatch revalidate scope, epoch, grant, abort; держать один operation identity | Pause discovery → revoke → resume: внешний endpoint не получил action |
| D3 mutable artifact evidence | Existing QA/artifact store → **extend** | Обязательный content hash+size+source/run/version, immutable snapshot и повторный readback в normal/repair/resume/reconcile; ACL на evidence | Подмена одинакового размера, missing hash, путь на заменённый inode не дают PASS |
| D4 hardcoded .awe-data | Existing storage configuration/repair → **reuse/extend** | Единый validated AWE_DATA_DIR resolver во всех entrypoints; no fallback к shared default | Два data dirs + repair: второй tenant и default untouched |
| D5 web_search fallback after abort | Existing web tools → **extend** | Один parent signal на все fetch/hedged/retry/fallback, cleanup; после cancel нельзя стартовать новый fallback | Счётчик requests не растёт после barrier; late response не промотирует результат |
| D6 browser/MCP continues | Existing MCP transport + process supervisor → **extend** | Разделить cancel requested / transport notified / effect outcome / quiescent; таймаут shutdown и kill local child при наличии полномочия; remote reconcile | Нет локальных orphan children; remote uncertain outcome записан UNKNOWN, не CANCELLED_SUCCESS |
| D7 delegated signal absent | Factory/delegation/manager → **extend** | Явная parent-child cancellation linkage на каждом delegation path, включая top-level | Grandchild heartbeat прекращается и новые tools не запускаются |
| D8 effect → checkpoint crash gap | Manager storage+existing execution boundary → **extend** | Durable intent до dispatch; provider idempotency key, outbox worker только при существующем storage ownership, ambiguous-outcome reconciliation | Crash до/после send и ACK; один внешний эффект, либо UNKNOWN с запретом retry |
| D9 empty tools inherited | Factory/specialists → **extend** | `undefined` не равно `[]`; effective grants = intersection parent∩task∩child∩policy; empty остаётся empty | Child с [] получает DENY для любого tool, без fallback к parent |
| Persistent maxTotalAgents | Manager/Factory budget → **extend** | Транзакционный mission-lifetime reserve до регистрации child, top-level входит в тот же ledger; stable child id дедуплицирует retries, counters durable across restart | При лимите L L+1 child не зарегистрирован ни при race, ни после resume |

#### Критичные семантические детали

**Fencing-at-effect.** Lease на запись состояния не блокирует уже отправленный HTTP request. Где целевой ресурс умеет проверять monotonic fence — передавать fence в trusted storage/worker. Где не умеет — serialize dispatch через существующую доверенную границу, запрещать stale отправку, применять provider idempotency и reconcile. Между сетевым send и revoke существует физическая гонка: нельзя обещать отмену уже принятого внешнего эффекта. Approval должен быть связан с нормализованными args digest, resource, scope, version и expiry; изменённые args требуют нового approval.

**Abort/quiescence.** MCP 2025-06-18 cancellation notification [P19] — protocol request, не транзакционный rollback. Нельзя считать отправленный cancel подтверждённой остановкой. `cancel_requested`, `dispatch_blocked`, `local_quiescent`, `remote_outcome_unknown`, `reconciled` — разные наблюдения; не обязательно один DB enum. Источник raw effect и дочерние процессы проверяет независимый observer. Удалённую операцию без cancel/readback API нельзя сделать безопасной магией AbortSignal.

**Durable intent/outbox/replay.** [AWS outbox P4] устраняет DB write/message dual-write gap только при общей транзакции intent+state. Outbox часто доставляет повторно: consumer/provider должен дедуплицировать. [AWS P1] требует caller-provided identity и устойчивой семантики same request; один ключ с другим payload должен отклоняться. Предлагаемый key binds tenant+mission+logical operation+effect slot, НЕ новый attempt UUID на каждый retry. Без provider идемпотентности нельзя гарантировать exactly-once произвольного UI/payment action: UNKNOWN → reconcile → отдельное human decision, не автоматический retry. Temporal activity [P8] полезна как documented semantic comparison, **defer внедрение второго engine**.

**Evidence immutability.** Hash сам по себе не доказывает авторство/неизменяемость, если producer может одновременно заменить artifact и manifest. Extend существующий QA/storage: content-addressed snapshot, append-only event history с отдельными writer/reviewer правами, trusted timestamp/run identity, signed manifest при релизе, retention и readback. Human oracle/version хранятся отдельно от agent-generated report. Нельзя изменять критерии после неудачного теста без новой принятой версии.

**Budget.** Лимиты concurrency, lifetime total agents, tool calls, tokens, currency, wall time и retries — разные измерения. Reserve до эффекта/child registration; settle/reconcile фактическое потребление; pending reservation переживает crash. Возврат budget только по доказанному NOT_SENT, не при потерянном ACK. Валютные суммы — integer minor units; токены/внешний bill не всегда известны сразу, использовать bounded reservation и hard stop. Предлагаемые L/thresholds — переменные политики, численные бюджеты владельцем здесь не утверждены.

### 4. Enterprise patterns: первичные источники и применимость

Документированные паттерны ниже = **vendor-claim**, перенос в Nox = **inference/recommendation**, не vendor benchmark или доказательство нашего production. Версии SDK/licensing/pricing не подтверждены и не нужны для покупки: **buy ни для одного продукта не обоснован текущим доступом**. Документированный стандарт не означает совместимость установленной версии Nox. Все URL и сохранённые тела P1–P20 в evidence index.

| Организация / источник | Полезный паттерн и ограничение | Nox: reuse/extend/integrate/buy/defer и проверка |
|---|---|---|
| OpenAI P7 practical guide | Layered guardrails, tool risk, human intervention; guide не security proof | **extend** existing Head/QA approval policy: reversible low-risk и privileged effects разделены; negative: LLM self-approval не выпускает grant |
| Anthropic P2 evals | Task/trial/trajectory/outcome; code/model/human graders; end-state важнее рассказа агента | **reuse/extend** existing QA: frozen held-out scenarios, artifact readback, repeated trials; no circular same-agent PASS |
| Google ADK P9 safety | Identity, sandbox, callbacks, evaluation/tracing — defense in depth | **extend** existing adapters/Factory authority: tool callback проверяется и в delegate path; policy denial при injection; **defer** ADK runtime replacement |
| Microsoft P5/P20 WSL | Управляемость WSL, Windows/WSL policy и backup/export guidance | **integrate** существующий OS supervision после approval; WSL VM не tenant isolation для общих mounted files/credentials; backup restore drill обязателен |
| Amazon/AWS P1/P4 | Idempotent client intent; transactional outbox и duplicates | **extend** manager storage boundary, не отдельный cloud orchestrator; fault matrix send/ACK/crash |
| IBM P14 tutorial | User-delegated identity, token exchange, short-lived dynamic credentials | **extend** grants/credential broker: identity и OAuth audience scopes; **defer** IBM/Vault stack purchase. Tutorial deployment не выполнялся; конкретная совместимость UNKNOWN |
| Salesforce Testing API official search source | Asynchronous run ID + frozen test expectations/context/history | **extend** QA receipt schema с run id/expected/actual; COMPLETED job не равно каждый assertion PASS. P13 fetch содержательно слаб; факт ограничен official search snippet, не verified SDK |
| ServiceNow P15 official-domain community article | AI Control Tower governance, inventory и oversight | **reuse/extend** TI/governance inventory; community marketing ниже SDK по силе evidence. Не покупать второй control plane |
| GitHub P11/P16 | Обе запрошенные security pages оказались Page not found | **unknown**, не приписывать гарантии firewall/approval; **defer** product-specific adoption. Общие release practices ниже не выдаются за проверенные GitHub возможности |
| Cloudflare P6 incident postmortem | Глобальная проблема regex/WAF; staged rollout и performance failure containment важны и для configuration | **extend** existing release discipline: config/Skill не автоматически low-risk; canary с CPU/error/runtime и rollback. Это self-reported incident, не Nox test |
| Databricks P10 auth | App identity против user identity; on-behalf-of и resource authorization | **extend** existing gateway/knowledge ACL: ACL до retrieval и при tool effect; service credential не превращается в owner authority; **defer** lakehouse migration |
| NVIDIA P12 security guidelines | API owns validation/auth, model не получает secrets; guardrails не заменяют API security | **reuse/extend** existing security boundary: allowlisted structured args и redaction; **defer** NeMo как обязательный второй policy engine |
| Temporal P8 | Activity retries требуют идемпотентности, durable workflow не отменяет внешние эффекты | **reuse** семантику в manager design; **defer** Temporal engine до доказанного gap/operational need |

#### Tool overload, specialization и memory без дублирования

Reuse TI для metadata retrieval; возвращать bounded shortlist с schema/version/provenance, а не тысячи descriptions в prompt. Metadata relevance не authority: этапы discovery → adapter health/compatibility → grant → invoke → receipt разделены. Head выбирает capability, Factory получает только эффективные grants. Knowledge/Skills вставляются с source/ACL/version и instruction trust boundary, не заменяют tools. Положительный тест: разрешённый tool выбран с валидными args и receipt; отрицательный: релевантная карточка неconnected tool даёт BLOCKED, не invented call. Измерять catalog recall на frozen oracle, prompt tokens, wrong-tool calls и denied effects отдельно, без выдуманного процента экономии.

### 5. Tenant isolation, OAuth, secrets и HITL

**Reuse** R0 security, manager scope и текущую memory, **extend** только непокрытые инварианты:

1. Tenant/project/task/agent labels проходят от entrypoint до retrieval filters, grant, storage path, cache key, logs, artifact и delegated child. ACL проверяется **до** vector/keyword retrieval, включая cached summaries и citations; post-filter недостаточен. Тест tenant A/B с одинаковыми resource IDs и различными canary secrets.
2. Нормализованные scopes + explicit principal/subject/audience; OAuth token в trusted broker, не в tool description/LLM prompt. По MCP 2025-06-18 authorization P3 resource-bound audience и недопустимость чужих tokens должны проверяться; token passthrough не использовать как универсальный shortcut. Возможности revocation провайдера различаются: локально deny немедленно, внешнее revoke ack отдельно.
3. Secrets через handles; redact input/output/errors/trace/screenshots. Env vars и общий Windows profile могут раскрыть credentials дочернему процессу. Egress allowlist на фактическом network boundary; redirects/DNS changes/private IP/localhost/link-local проверяются после resolution, не только regex исходного URL.
4. Child scope не шире parent; `tools:[]` пуст; admission не принимает произвольные JS authority callbacks от worker. Sandbox и OAuth — независимые слои; UI computer-use может обходить API scope через залогиненный профиль, поэтому изолированный профиль и owner-controlled session boundary.
5. HITL request содержит exact normalized action, target, estimated cost/risk, evidence, expiry, version/digest и explicit approve/deny. Retry не расширяет утверждённую операцию. Owner GO на release не равен approval каждой внешней операции; прошлый approve не продлевается после изменившегося payload.

### 6. Safe improvement lifecycle для WSL2 и будущих workers

Основа: DOC-13/14/15/16 ASTRA, R0 cancellation/leases/QA, DOC-27 immutable acceptance; [SLSA v1.1 P17](https://slsa.dev/spec/v1.1/levels), [TUF 1.0.37 P18](https://theupdateframework.github.io/specification/latest/), Cloudflare P6. Эти стандарты не доказывают, что Nox уже SLSA-compliant. **Update Manager = defer**, пока inventory существующих releases/OS supervisor не выявит измеримый gap.

| Risk class (предлагаемая, не принятая policy) | Вид изменения | Gate / rollback |
|---|---|---|
| R-A: bounded content | Проверенный источник знаний без исполнения, без расширения ACL | provenance/license/hash, injection scan, retrieval regression, reversible index version; rollback указателя + purge poisoned cache |
| R-B: behaviour | Skill, prompt, template, уже разрешённый tool binding, model change | no new scopes; offline deterministic + quality/visual relevant eval; модель pin, latency/cost ceiling; active missions не меняют модель/Skill молча |
| R-C: execution surface | Новый MCP/API adapter, SDK/native executable, new network endpoint | isolated staging и pinned dependencies, SBOM/license/security review, TG matrix, revoke/kill/reconcile plan; отдельный owner approval |
| R-D: trust/data/control | Права/policy, core/Head/Manager/QA, database/schema, updater/signing keys | независимый review, frozen oracle, backup+restore evidence, compatible migration, dual-control release; запрещён self-approval |

Класс определяется **эффектом**, а не расширением файла: Skill с shell install не R-A; конфигурация глобального dispatch может быть R-D.

Предлагаемая последовательность (**не выполнялась**):

1. **Inventory/reuse:** записать final runtime SHA, lockfile digest, Node/package-manager/OS/WSL version, schema, model/provider pin (или фиксировать floating alias), tools/schema digests, policy/oracle versions. Документы DOC-04 pins — отправная точка, не окончательная ведомость.
2. **Isolated staging:** future branch/worktree и отдельный data dir/DB + Windows profile/secrets sandbox; не checkout поверх OpenCode session. Исследование не создаёт branch/commit. Frozen deterministic fixtures, then integration, then mission; положительные и отрицательные assertions.
3. **Provenance/signing:** reuse existing CI/release artifacts, при gap добавить digest manifest/signature, verify before install. SLSA provenance отдельно от signature; signature валидна лишь относительно trusted key/identity. TUF роли/expiry/rollback protection полезны для будущей distribution, но full TUF service сейчас **defer**.
4. **Version-pinned missions:** running mission сохраняет engine/adapter/model/schema/Skill/policy refs; новый release не переписывает историю. Security revoke немедленно блокирует опасные новые effects даже у старой pinned mission; pin не право обойти актуальную deny policy. Incompatible resume → blocked migration/reconciliation.
5. **Canary:** ограниченный isolated workload/worker, no broad scopes; compare invariant violations, failure count, p95 latency, memory/CPU, cost и artifact mismatch с заранее замороженным baseline. Порог задаётся владельцем до теста; текущих измерений нет. На одном WSL2 host canary не обеспечивает host-failure isolation — нужны отдельный instance/data root либо остановка и controlled handover.
6. **Quiesce/handover:** stop admission → drain/abort tracked tasks → preserve unknown intents → transfer ownership with new epoch. Два supervisors не должны активировать одного worker или общий DB writer без fence. Server workers: per-tenant identities/quotas, signed worker image, secret rotation, remote heartbeat, takeover barrier.
7. **Rollback/roll-forward:** rollback pointer недостаточен при schema migration или external effect. Backward-compatible expand/contract, snapshot restore rehearsal, explicit roll-forward path; stale worker credentials revoked. Rollback не переигрывает already-sent effects.
8. **Backups WSL2:** WSL export/import — image-level механизм, не автоматический consistent PostgreSQL backup. Согласованная DB backup/WAL стратегия по фактической DB, artifact manifest и external Windows-mounted folders отдельно; encryption/access/retention и восстановление в isolated target. RPO/RTO UNKNOWN до согласования/restore drill. Не копировать секреты в общедоступный release archive.

### 7. Приоритет и зависимости без выдуманных оценок

**P0 acceptance prerequisites:** получить из существующих доступных доказательств final SHA + lockfile/data-dir/OS scope; независимый verdict по security failure/process probe; revalidate D1–D9/budget на этом SHA; freeze oracle и owner decision. Это не запрос новых доступов и не обещание выполнить сейчас.

**P1 after acceptance:** reuse TI/adapter/grant/receipt boundaries и QA; добавить лишь выявленные недостающие контракты. Costs: нет численных vendor prices; оплачиваемые trials не проводились. Трудозатраты/SLA/production capacity UNKNOWN, оценка допускается только после final source inventory и воспроизводимого isolated test plan.

**P2 conditional backlog:** workers distribution/signing enhancements и TUF, внешние OAuth/secrets products, persistent outbox infrastructure — только если существующий storage/supervisor не покрывает требования. Migration на Temporal/ADK/новый control plane по нынешнему evidence не обоснована.

### Sources

- [Nox исходное ТЗ на file-change SHA](https://github.com/failm3/nivict-ai-academy/blob/0510e4cb923ed0bb9260222a07384b805a4fb396/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/PROMPTS/CORTEX-NOX-ENTERPRISE-CAPABILITY-RESEARCH-FINAL-2026-11-13.md#L24-L49)
- [AWS idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-apis/), [AWS outbox](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html)
- [Anthropic agent evals](https://www.anthropic.com/research/demystifying-evals-for-ai-agents), [MCP authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization), [MCP cancellation](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/cancellation)
- [Cloudflare postmortem](https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/), [Microsoft WSL enterprise](https://learn.microsoft.com/en-us/windows/wsl/enterprise)
- [Salesforce Testing API](https://developer.salesforce.com/docs/ai/agentforce/references/testing-api/testing-connect-reference.html) — официальный поисковый excerpt, weaker than full retrieval.
- Полный список URL, snapshots и ограничений: [ENTERPRISE-EVIDENCE-INDEX.md](ENTERPRISE-EVIDENCE-INDEX.md).


