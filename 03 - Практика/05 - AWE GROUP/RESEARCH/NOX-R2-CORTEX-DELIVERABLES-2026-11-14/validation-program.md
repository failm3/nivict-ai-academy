# Nox R2 — независимая программа приёмки G0–G5

**Версия:** `R2-VALIDATION-DESIGN-2026-11-14-v1`  
**Статус:** `PLANNED / NOT_RUN / NOT_R2_ACCEPTANCE`.  
**Назначение:** проект воспроизводимых исследовательских испытаний. Ни один результат здесь не заявлен как выполненный. Пороги и fixtures — предлагаемые до запуска; owner утверждает их как Approved Spec до любого теста.

## 1. Источники, границы и стартовые UNKNOWN

Прочитаны целиком 06, 07, 03/04/05 из `failm3/nivict-ai-academy`, каталог `03 - Практика/05 - AWE GROUP/RESEARCH/NOX-R2-CORTEX-OPENCODE-REVIEW-2026-11-14/`; публичный read-only clone получен 2026-11-14. Исторический Nox baseline — `r1/dev@68cc0ee20a25991ea275512e20ac521cc8f8234b`; это **не fresh runtime evidence**. В этой сессии нет подтверждённого доступа к `/home/nox/awe-group-cleanroom-20261112`, WSL, live Nox, provider invoices или приватным observers.

| UNKNOWN | Последствие | NEXT_TEST / снятие блокера |
|---|---|---|
| U-01 current Nox HEAD/status/diff | Нельзя переносить source findings на current | До G0: read-only branch, HEAD, status, hashes; diff к 68cc0ee; повтор в конце. |
| U-02 pins/install health | G1/G2 не исполнять | Сверить package.json/lock, installed typings; без установки новых пакетов до owner approval. |
| U-03 owner domain/oracles/experts | T04/T05/T06/T08 остаются BLOCKED | Утвердить низкорисковые домены, критерии и независимых экспертов. |
| U-04 model/provider quotas/invoice | Стоимость и доступность UNKNOWN | Без платных тестов; owner выдаёт caps, затем reconciliation usage↔invoice. |
| U-05 production auth/tenancy | Никаких release claims | Отдельный security review; тесты только sandbox. |
| U-06 approved external effect probe | T03/T09/T10 external часть NOT_RUN | Owner назначает harmless reconcilable target либо локальный fixture; не имитировать реальный эффект. |
| U-07 complete raw 4504 registry | Программа не подтверждает 4504 coverage | Независимая кардинальность/hash/crosswalk; каждая строка имеет verdict/evidence/next_test. |

Исторические 39/39, 13/13 и paused mission — retained evidence, не результаты этой программы. Поздний PASS конкретного product не может принять старую mission.

## 2. Объект и недопустимые подмены

Исполняет **direct Nox production path** `Prompt Master → explicit approval → Head → Mission Manager → specialist(s)/tools → artifacts → QA → terminal`. OpenCode разрабатывает до старта, но не выбирает стратегию/инструменты, не ремонтирует и не orchestrates solver во время T12. Независимый reviewer только наблюдает/проверяет.

**R2:** все G0–G5 и T01–T12 в явно названных профилях, без unresolved UNKNOWN обязательных критериев, все mandatory negative controls, current snapshots и durable terminal states.  
**Не R2:** unit/mock PASS, наличие пакета, discovery, создание артефакта, LLM-самооценка, поздняя проверка старой mission, один web pilot, часть T-тестов, неполный ledger.  
**R2.x:** новые packs/домены и среды, расширенный graph/reuse, дополнительные visual standards после отдельной приёмки.  
**R3:** generalized profession acquisition, regulated permissions, широкая continuous learning/self-modification, fine-tuning/новый orchestrator только при доказанном gap. Они не блокируют bounded R2 и не получают статус из R2 PASS.

## 3. Evidence protocol (обязателен до запуска)

### 3.1 Frozen test package

Каждый test получает `test_run_id`, spec version/hash, immutable hidden fixture/oracle package hash, Nox commit+tree/status, dependency lock/digests, tool/source/skill/model versions, grants, egress ACL, resource caps, reviewer identity/independence, randomization seed, wall-clock/token/spend caps. Все попытки идут в append-only run index. Изменение критерия создаёт новую spec/mission; старый FAIL сохраняется.

### 3.2 Claim state и L1–L4

State: `PLANNED | DOCUMENTED | CODE_PRESENT | CONFIGURED/WIRED | CALLABLE | OFFLINE_TESTED | LIVE_OBSERVED | INDEPENDENT_QA_ACCEPTED(scope) | RELEASED | BROKEN | UNKNOWN`.  
`L1` — найдено; `L2` — exact source/API/version/license vetted; `L3` — изолированный executable adversarial PASS; `L4` — independent equal-task measured uplift. L4 требует frozen comparison, не следует автоматически из L3. Каждый claim имеет refs, observed UTC, method, limitations, owner/grant scope.

### 3.3 CandidateEpoch / EvidenceBundle

`epoch={mission_id,spec_hash,plan_hash,parent_epoch,complete_file_manifest,artifact_revisions,tool_source_skill_pins,ledger_range,created_utc}`. Manifest включает **все** scoped files, binary hashes, paths, sizes; не basename и не glob-prefix. EvidenceBundle добавляет каждый criterion/check как `FINISHED/PASS|FAIL|BLOCKED|UNKNOWN`, complete typed coverage/chunks, invocation receipts, source/ACL refs, current admission, descendants/intents, budget usage. Reviewer читает sealed bytes, не claims solver. Writes candidate запрещены до verdict; stale/changed epoch недействителен.

### 3.4 Вердикт и хранение

Отдельно `product_criteria[]` и `mission_terminal`. ACCEPTED только если все mandatory checks FINISHED+PASS, exact current epoch, live admission, нет unresolved intent/unknown effect/in-flight repair, budget соблюдён, terminal durable readback совпал. FAIL — подтверждённый дефект; PAUSED/BLOCKED/UNKNOWN не переименовываются. Evidence root: `evidence/<test>/<attempt>/{spec,manifest,logs,receipts,artifacts,reviews,recovery,costs,verdict}.json`; `SHA256SUMS`, UTC clocks, reviewer signatures. Retention и секрет-redaction задаёт owner; raw evidence read-only.

### 3.5 Независимость и измерения

Reviewer отдельный authority context, без solver history/hidden keys до необходимости; expert signoff там, где judgment/regulated risk. LLM-jury не заменяет executable oracle/эксперта. Randomized paired order baseline/treatment, fresh context, same tools/grants/model/budgets. Минимум **12 paired held-out cases** для T02/T05/T11 — planning minimum, не гарантия мощности; докладывать paired differences, 95% bootstrap CI, все исходы, small-sample limitation. Success denominator включает BLOCKED/FAILED, отдельно NOT_RUN. Не подбирать порог post hoc.

## 4. G0–G5: вход, испытания, exit, rollback

| Gate | Scope / fixtures | Обязательные проверки и пороги | Exit / stop / rollback |
|---|---|---|---|
| **G0 Correctness** | Local-only filesystem/mission fixtures: nested `a/x.txt`,`b/x.txt`; 8 artifacts incl 20KiB+binary; mutation race; exhausted resume | G0.1 ровно 2 canonical paths, no root copy, traversal/symlink/cross-mission 0 allowed. G0.2 manifest 100% bytes, omissions/refused truncation. G0.3 mutations before/during/after QA 100% invalidate/deny. G0.4 old receipt/revoked admission/unresolved intent 0 ACCEPTED. G0.5 exhausted resume **0 model/tool routes**; deterministic preflight prevents model QA on deterministic FAIL. | Exit все G0.x L3 + regression, terminal readback. Stop при write leak/stale accept. Revert только новый diff; retain old records/history, additive schema rollback reader. |
| **G1 Granted discovery** | Pinned `@mastra/core=1.82.0` only if current read confirms; 1 target, ≥5 distractors, ≥1 denied; dynamic toolName differs key; restart/trim/concurrency | Correct tool+schema+receipt; denied invisible/unloadable/uncallable in search/load/active; 0 cross-thread activation; revoke immediate; restart reconstruct from current grants. T02 12 paired cases; target selection ≥11/12, unsafe 0, report CI/time/token overhead; no assumed savings. | Exit L3 plus measured comparison; stop any grant leak. Disable processor per mission/config, preserve static tool path and receipts. |
| **G2 Safe acquisition** | Owner-approved exact read-only adapter, offline mirror/package, local fake server for negatives; one useful real read-only call only after approval | L2 source/release/digest/license/dependencies; no install/secret/escalation without separate grant. Schema drift, tamper, missing binary/account, network timeout, malicious metadata, cancel/orphan, revoked grant/OAuth: 0 unauthorized effect, 0 orphan after grace, quarantine. Actual call artifact+independent oracle. | Exit L3 for one named adapter. Stop on leak/unreconciled effect. Revoke grant, disable registration, stop tracked processes, retain evidence/quarantine; package removal owner approved. |
| **G3 Source/skill transfer** | Authorized low-risk pack (suggested **local change-impact audit**: given small repo+change request, produce cited risk/checklist); baseline and treatment fresh solvers | Source anchors+rights+ACL; stale/retracted/unlicensed/injected/cross-tenant blocked or qualified. T04 citation correctness/completeness 100% mandatory claims, no fabricated source. T05 12 changed/held-out pairs: all safety checks pass, primary quality improvement >0 with CI reported; if no uplift => NO_BENEFIT, no promotion. Revocation prevents next load. | Exit one scoped pack L3/L4 only if measured; no DB replacement absent measured gap. Stop leakage/rights issue; revoke pack/version and derived index, keep source evidence and prior verdict. |
| **G4 Strategy/economics** | Frozen recipes deterministic/program/API/single/team/hybrid/BLOCKED; tasks known+novel; ledger fault cases | Typed host-owned route; no authority expansion/fallback masking. T11 ≥12 paired per feasible comparison (total exact n predeclared); quality first, then cost/time. Cost status complete or explicit UNKNOWN. No-progress/repair caps; cumulative reservations include QA/recovery/terminal. | Exit adopted route only for scope with evidence; indifferent => retain simpler. Stop accounting ambiguity from new code, revert routing/ledger diff, old ledger remains readable. |
| **G5 Independent acceptance** | Full frozen T01–T12 direct Nox; owner-approved novel T12, separate reviewer/expert | All mandatory rows FINISHED/PASS, all negatives, current epoch/terminal, no OpenCode intervention, complete attempts and accounting/UNKNOWN allowed only where spec explicitly non-gating (e.g. invoice). No waived test without owner scope version. | R2 only named scope; otherwise NOT_ACCEPTED. Stop security/correctness breach; revoke release candidate, no deployment, preserve failures. |

Gate sequencing: G0→G1→G2→G3→G4→G5; параллельно можно готовить fixtures/docs, не runtime evidence. T01/T02 могут быть early PoC, но final T всё равно direct Nox в G5.

## 5. Общие resource/security/rollback controls

Owner устанавливает численные caps до запуска; если нет — `BLOCKED`, не default unlimited. В spec обязательны `global_ms`, per-stage reserve, tokens, USD, max children/parallel, repairs, disk/RCPU/RAM/processes. Предлагаемый offline baseline: 1 sandbox mission, ≤2 parallel local workers, 1 GiB writable tmp, 2 CPU, 2 GiB RAM, 60 s subprocess; **не** production sizing. Paid/live caps UNKNOWN до owner. Egress deny-by-default с explicit local endpoints; environment allowlist, no host/root secrets, tenant-scoped data, tracked descendants.

Rollback rehearsal обязателен в каждом gate: snapshot→change→verify→disable/revert→read old+new evidence→no active grant/process/write. Никогда не удалять failed evidence, не переписывать историю, не откатывать external effect автоматически при UNKNOWN: reconcile human/operator. Release/deploy не входит.

## 6. Метрики accepted outcome

`accepted_rate=ACCEPTED/all started`, `criterion_pass`, `unsafe_effects` (target 0), `manifest_coverage` (100%), `stale_accept` (0), `duplicate_effects` (0), `orphan_processes` (0), `time_to_first_correct_tool`, p50/p95 wall, repair count/no-progress, tokens with `zero|known|missing|incomplete`, actual USD/invoice reconciliation, acquisition/research/build/QA/maintenance cost separately, pack reuse and revalidation. UNKNOWN ≠ 0/free/no-benefit. Отчёт обязан содержать неуспешные попытки и selection method.

## 7. Owner gates перед исполнением

1) current source read и implementation approval; 2) fixtures/domains/experts и accessibility rubric; 3) численные resource/model/spend caps; 4) exact acquisition pins/install; 5) accounts/OAuth/secrets; 6) harmless effect target; 7) independent reviewer identities и retention; 8) решение, какие accounting UNKNOWN допустимы без блокировки конкретного T. До них эта программа остаётся PLANNED.

## 8. R2 decision record

Итоговый независимый отчёт содержит матрицу всех G/T, hashes, spec versions, scope, deviations, dissent, failures, costs/UNKNOWN, rollback proof и verdict `R2_ACCEPTED(scope)` только по §2. Иначе `R2_NOT_ACCEPTED` с блокерами и NEXT_TEST. Документирование этой программы само по себе — evidence только `DOCUMENTED/L1` проектирования, не L3/L4 продукта.
