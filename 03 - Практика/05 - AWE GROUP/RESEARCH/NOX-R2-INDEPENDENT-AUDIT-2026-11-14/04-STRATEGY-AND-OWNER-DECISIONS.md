# Стратегия, приёмка, риски и решения владельца

Это предложение, не разрешение на выполнение и не начатая реализация.

## 1. Архитектурное решение

**EXTEND.** Сохранить Mission Manager, lifecycle, grants, durable intents, artifact lineage, QA gate и model ledger. Mastra Agents/Tools/Memory продолжать использовать; native processors подключать только за узкими seams.

Mastra Workflows можно рассматривать внутри host-approved fixed recipe, но не как второй orchestrator. LangGraph/Temporal требуют новой state/recovery модели и не доказывают лучший mission outcome. JSON+LibSQL достаточны для текущего single-host scope до измеренной operational потребности. Langfuse — optional exporter, не второй ledger.

## 2. Этапы и exit criteria

### A. Reproducible baseline + early smoke

**Работы после разрешения:** typecheck/build/offline suites; одна новая low-risk direct-Nox mission через PM→approval→Head→MM→QA; independent collector; один bounded interruption/recovery case.

**Exit:** полный run tree, accepted/paused/failed, latency, repairs, unresolved intents, all model records, tokens/USD с UNKNOWN; defects классифицированы. Это не R2 PASS.

### B. Artifact/candidate correctness

**Минимальные изменения:** relative paths + monotonic revisions; versioned CandidateEpoch; complete EvidenceBundle/oracle refs; reviewed-vs-current manifest comparison; fail-closed stale/mutated/unresolved states.

**Exit:** same-basename/rapid rewrite, >6/large/binary, mutation during QA, stale receipt, revoked admission, late child write и unresolved intent tests. Ноль ACCEPTED для несоответствующего candidate.

### C. Outcome/economics/operability

**Работы:** deterministic preflight до paid QA; no-progress; budget/reservation policy; additive node/retry ledger fields; whole-mission projection; read-only usage/trace view; clarification/edit spec; typed planning failure; host route contract.

**Exit:** deterministic FAIL → 0 QA model calls; repeated no-progress stops; каждый call объяснён projection; malformed planning visible; budget extension только по явной policy; USD без invoice UNKNOWN.

### D. Professional vertical slices

Repo patch, затем documents. Для каждого — frozen input, exact deliverable, independent oracle/expert, negative controls, bounded recovery и cost record. Новые packages устанавливаются только отдельным owner approval.

### E. Measured expansion

ToolSearch static-vs-deferred equal-task; repaired Playwright; один source/skill pack с fresh holdout; один API effect. Допускаются `NO_BENEFIT`, `INCONCLUSIVE`, `BLOCKED`. Только затем adaptive routing и broader packs.

### F. Scoped final acceptance

Применимые T01–T12 прямо против Nox, без solver-operated verifier. Вердикт только `R2_ACCEPTED(explicit_scope)`, не универсальная компетентность. Windows и multi-user exposure отдельными tracks.

## 3. Главные риски и сдерживание

| Риск | Уровень | Контроль |
|---|---|---|
| Неверная artifact identity / stale candidate | Высокий, code-confirmed | Canonical path/revision, immutable manifest, preterminal equality |
| Неполная evidence/economics принята за полную | Высокий | Complete coverage receipts, ledger-derived summary, UNKNOWN |
| UNKNOWN external effect повторён | Высокий | Сохранить durable intents/operator recovery; idempotency/status reconciliation |
| Browser supply-chain/egress/state leakage | Высокий до repair | Pin/digest, per-mission context, OS containment, egress policy, cleanup |
| Generic LLM QA как профессиональный oracle | Высокий | Domain executable oracle/expert и held-out tasks |
| Переписывание MM | Высокий | Preserve kernel; framework только после measured unmet requirement |
| Слишком поздний пользовательский baseline | Средний/высокий | Early OC-12-smoke без acceptance claim |
| ToolSearch/RAG/Skills ради платформенности | Средний | Paired comparison, ACL, no-benefit/inconclusive |
| Multi-user через shared secret | Высокий при exposure | Single-tenant boundary или полный tenant isolation до публикации |
| Benchmark overfitting / ложное learning | Средний | Fresh holdout, protected fixtures, independent reviewer, retention failures |

## 4. Решения владельца

1. **Execution authority:** разрешить ли offline baseline и/или один bounded smoke; отдельно разрешить code changes.
2. **Первый outcome:** выбрать repo patch, document workflow или другой полезный bounded mission; назвать non-goals.
3. **Acceptance:** кто независимый reviewer/oracle; какие профессиональные стандарты обязательны.
4. **Budgets:** wall time, tokens/USD или допустимый UNKNOWN, repairs/no-progress, children/parallel, disk/CPU/RAM.
5. **Economics:** достаточно complete token ledger или требуется invoice/USD reconciliation.
6. **Model policy:** allowlist и host routes; planner не получает arbitrary model authority.
7. **Acquisitions:** конкретный package/version/digest/license, install и call approvals, egress; никакого blanket approval каталога.
8. **External effects/recovery:** local fake/draft-only или реальный target; допустимые harmless effects для recovery tests.
9. **Tenancy:** single-user trusted-host или multi-tenant requirement.
10. **Evidence:** retention, redaction, доступ к run trees/traces.
11. **Release scope:** early smoke ≠ R2; обязательные/OUT_OF_SCOPE tests; deployment/publication отдельно.

## 5. Ожидаемый эффект и неизвестные

Ожидаются более надёжная связь verdict↔bytes, меньше бесполезных повторов, измеримая mission economics, ранняя диагностика failure classes и первые scoped professional capabilities. Это качественные прогнозы. Численный uplift, стоимость, сроки, reliability и лучший model/tool route остаются UNKNOWN до independent paired evidence.
