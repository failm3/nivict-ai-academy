# Фактическое состояние Nox: находки и границы доказательств

Объект: `r1/dev@68cc0ee20a25991ea275512e20ac521cc8f8234b`. Все пути ниже относительны этому checkout. Аудит read-only: тесты, миссии, provider calls и deployment не запускались.

## 1. Подтверждённая база, которую нужно сохранить

| Область | Источник | Ограничение |
|---|---|---|
| Specification/approval | `src/agents/prompt-master.ts:28-101`; `src/api/server.ts:287-359`; `src/utils/spec-binding.ts` | Typed spec и immutable binding есть; нет полноценного clarification/edit workflow |
| Head и grants | `src/agents/head-agent.ts:95-179`; `src/agents/specialists.ts:150-194,273-284` | Head выбирает roles/tasks/tools, не model IDs; grants ограничены approved spec |
| Parallel/recursive execution | `src/agents/mission-manager.ts:2230-2327`; `src/agents/recursion.ts:31-42,463-647` | Runtime не целиком serial; конкретные web runs не доказывают nested/parallel generality |
| Recovery/lifecycle | `src/agents/lifecycle.ts:197-333,383-460,873-959`; `src/agents/mission-manager.ts:2050-2155,2743-2807` | Durable intents, atomic checkpoints, leases, quiescence, operator accept/retry реально wired |
| QA/repair | `src/agents/qa-gate.ts:318-406`; `src/agents/qa-agent.ts:87-112,128-227`; `src/agents/mission-manager.ts:2395-2437` | LLM verdict advisory; deterministic gate binding; repair bounded двумя итерациями |
| File/shell security | `src/security/workspace-fs.ts:8-80`; `src/security/shell-sandbox.ts:22-64`; `src/tools/index.ts:258-355` | Значительный Linux containment; не universal security certification и не Windows support |
| Web fetch | `src/tools/index.ts:160-170,463-650` | SSRF/DNS pinning/redirect checks существуют; browser path их не наследует |
| Model routing/ledger | `src/config/models.ts:97-154`; `src/utils/model-ledger.ts:8-42,96-182` | Host byAgent/byRole уже есть; ledger UNKNOWN-safe, но не whole-mission economics |
| Domain verifiers | `src/agents/csv-qa.ts:32-66`; `src/agents/web-qa.ts:7-34`; `src/capabilities/web-product.ts:53-299` | Два полезных узких oracle, не профессиональный универсальный reviewer |

## 2. Приоритетные подтверждённые дефекты

Severity отражает риск design/code. Сценарии гонок и повреждений ниже — статические выводы, не воспроизведённые runtime incidents.

### N-01 P0 — nested artifact identity и версии

`file_write` пишет безопасный nested path, но вызывает `saveArtifactFile(..., path.basename(safePath), ...)` (`src/tools/index.ts:402-409`). Это создаёт root duplicate и теряет путь. `listArtifacts()` дедуплицирует по `name`, выбирая последний по `(created_at, id)` (`src/utils/storage.ts:445-469`).

Дополнительный пробел Cortex: timestamp имеет миллисекундную точность, а tie-breaker — случайный UUID (`src/utils/storage.ts:430-438,462-469`). Быстрые перезаписи одного имени могут быть упорядочены не по фактической записи. Нужны canonical relative path и monotonic per-mission revision, не только удаление root copies.

**Acceptance:** `a/result.txt` и `b/result.txt` остаются независимыми; ноль root duplicates; быстрые same-name writes выбирают последнюю revision; traversal/symlink/cross-mission denied; legacy records читаются без rewrite.

### N-02 P0 — reviewed candidate не immutable

Evidence читается до async QA, а финальная проверка видит текущие bytes (`src/agents/mission-manager.ts:2341-2367,2639-2651`). Нет общего candidate hash в QA verdict и обязательного сравнения reviewed/current manifest. Existing lease/spec/admission/seal/final hash controls ценны, но не доказывают, что именно terminal candidate прошёл review.

**Acceptance:** mutation до/во время/после QA, stale receipt, late descendant write и unresolved intent дают ноль ACCEPTED; terminal record содержит durable readback того же candidate hash.

### N-03 P0 — полный EvidenceBundle отсутствует

Лимиты: 6 artifacts, 12 000 chars/artifact, 6 000 execution output (`src/agents/qa-agent.ts:87-112,160-164`). Дополнительно Mission Manager читает файл до 15 000 chars, а image заменяет path placeholder (`src/agents/mission-manager.ts:801-809`). Truncation корректно блокирует PASS, но repair не может устранить жёсткий review limit изменением deliverable — возможны бесполезные платные repair/QA.

**Acceptance:** каждый scoped artifact присутствует в manifest; текст покрыт полными chunks; binary проверен независимым oracle; любые omissions/budgets binding; candidate hash входит в receipt.

### N-04 P1 — deterministic FAIL всё равно оплачивает model QA; no-progress не распознаётся

Coverage/CSV/web defects вычисляются до model call (`src/agents/qa-agent.ts:134-140`), но `withModelCall` выполняется безусловно (`:146-166`), defects применяются после (`:211-219`). Repair cap существует, но repeated candidate/defect fingerprint не останавливает повторы.

**Acceptance:** binding deterministic FAIL → 0 model QA calls; repeated unchanged candidate/defects → досрочный BLOCKED/PAUSED; сохраняются diagnostics без authority override.

### N-05 P1 — ledger неполон как mission economics

`ModelCallRecord` не содержит node/delegation/intent/attempt/retry/category identity (`src/utils/model-ledger.ts:8-42`). `execution.totals` суммирует только top-level results (`src/agents/mission-manager.ts:2653-2683`). Это исключает Head, QA/re-QA, repairs, recursive descendants и orphan calls. Prompt Master использует `missionId:null` (`src/agents/prompt-master.ts:63-88`).

Положительный invariant: missing/partial/zero usage различаются, UNKNOWN не превращается в ноль, USD не выдумывается. Один SDK invocation не равен числу HTTP retries и не является invoice line.

**Acceptance:** synthetic graph Head + одинаковые sibling roles + child + repair + QA + orphan даёт per-node attribution; summary проецируется из ledger; known subtotal и completeness разделены; USD без invoice UNKNOWN.

### N-06 P0 перед browser exposure — MCP/browser boundary

Unpinned probe и spawn: `src/config/mcp.ts:86-100,211-227`. Process-wide singleton/cache: `:171-189`; `src/tools/browser.ts:29-54,98-123`. Browser navigation не использует `assertSafeUrl` (`src/tools/browser.ts:275-289`), а MCP process не проходит shell process registry/sandbox. `--isolated` — профиль, не host sandbox/egress boundary.

Для проверенного upstream Playwright MCP 0.0.85 (`gitHead 4e0794dd0a0176519830a5ed27b491137cf9338f`) click/type/snapshot принимают `target`; Nox передаёт `selector` (`src/tools/browser.ts:328-380`). Это source-to-pinned-contract mismatch, не live reproduction. Screenshot возвращается base64, но не регистрируется typed artifact (`:292-325`).

**Acceptance:** exact version/integrity; per-mission/delegation contexts; denied private/off-policy navigation и subresources; schema drift fail-closed; production wrapper navigate→snapshot→click/type→screenshot artifact; cancellation/restart оставляет ноль descendants и stale tools.

### N-07 P1 — checkpoint validation и recovery attribution

`loadCheckpoint` принимает finite, но отрицательный `elapsed_ms` (`src/agents/lifecycle.ts:297-301`), после чего resume вычисляет `timeoutMs - elapsed_ms` (`src/agents/mission-manager.ts:1613-1655`). Это может увеличить budget при malformed durable state. Operator accept проверяет artifact integrity, но не producer node/intent и не исключает reuse одного artifact для двух parallel intents (`src/agents/mission-manager.ts:2788-2807`).

**Acceptance:** negative/NaN/Infinity timing rejected; один artifact не закрывает два intents; recovery сохраняет producer/attempt provenance. API resume позволяет новый `timeout_ms` (`src/api/server.ts:366-393`): это допустимое extension только при явной owner policy и audit, иначе требуется monotonic cap.

### N-08 P1 — planning/specification quality failure

Head parse/schema failure молча превращается в одного generic executor (`src/agents/head-agent.ts:165-180`). Это не расширяет grants, но скрывает planning defect и меняет route. Prompt Master сразу генерирует spec (`src/agents/prompt-master.ts:63-101`); полноценного вопрос→ответ→edit→approval loop в API не показано.

**Acceptance:** malformed plan → typed PLANNING_FAILED или bounded replan, не silent generic execution; ambiguous request требует уточнений; изменение spec создаёт новый binding.

### N-09 P1 до multi-user exposure — single shared-secret model

API использует один `AWE_API_SECRET` (`src/api/server.ts:99-108,138-154`), а mission/artifact/memory storage не имеет tenant partition. `operator` в recovery — строка audit assertion, не независимая cryptographic identity. Для локального trusted-host scope это допустимая граница; для взаимно недоверенных клиентов — нет.

**Acceptance при необходимости multi-tenancy:** authenticated principal, tenant-bound routes/storage/memory/retrieval; IDOR/cross-tenant/recovery/log/artifact negative tests.

## 3. Сохранённые evidence — что именно они доказывают

| Evidence | Подтверждает | Не подтверждает |
|---|---|---|
| `reports/R1-P0-ACCEPTANCE.md:3-19`; `reports/r1-p0/full-offline-verified/summary.json` | Исторические 39/39 offline suites, typecheck/build и finite P0 scope | Fresh HEAD runtime в этом аудите, production readiness, universal competence |
| `reports/r1-live-independent-review.md:3-11,60-95` | Один live CSV: Head→analyst→QA, 3 SDK calls, 22 860 reported tokens, корректная арифметика/artifacts | Полный PM→interactive approval loop, qualification, nested/parallel, invoice/USD |
| `reports/R1-LOCAL-WEB-PRACTICE.md:16-58,106-149`; web `summary.json` | Реальный web artifact; поздний exact-tree 13/13 independent product PASS | Mission acceptance: обе missions paused; полная стоимость UNKNOWN |
| `reports/r1-p1/paired-rerun/r1-p1-lesson-comparison.log`; `reports/r1-p1/evaluation.md:60-76` | 7 paired deterministic cases, нулевой correctness/tool-call delta | Learning uplift, улучшение solver/tool selection, generalized transfer |

Старые failed/partial runs не должны удаляться или смешиваться с более поздними PASS. Хеши доказывают целостность/связь, но не issuer authentication или истинность внешнего claim.
