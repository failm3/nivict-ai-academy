# A2 · Durable coordinator, конкурентные workers и outbox
**Статус:** READY_FOR_CODEX · **Зависимости:** A1 + C1. **Параллельно:** A3 и работа с фактами B1.

## Цель
Превратить существующий AUTO-01/D03/D09 foundation в жизнеспособный исполняющий контур **обеих** миссий. Настоящие concurrent workers, зависимости, lease/fence, persistent state, бюджеты и outbox при сохранённой совместимости E0. Не писать отдельный scheduler для B.

## База и изменения
- Проверить реальные `AUTO-01` validation/runner, D03 CAS, D09 ledger, `awe/persistence/migrations`, `INTEGRATION-01`, SEC gate и `DATA-02`.
- Разработать generic `mission, task, task_dependency, lease, event_cursor, effect_intent, inbox_event` и внешние domain tables как **отдельные** от горячего snapshot; большие payload в object store по refs/hash. Не нарушать инвариант одного authority.
- Интерфейс: `plan.publish → job.claim(task, capability, worker, lease/fence) → execute → artifact.put → qa.evaluate → job.complete`; зависимые задачи не становятся ready до принятых upstream results.
- Два независимых worker могут исполняться параллельно; нет гонки резервов/прав. Leases имеют owner, generation, expiry; старый worker после takeover не вправе выполнить эффект и завершить задачу.
- Обязательные `deadline, cancellation, bounded replan, max_parallel, priority, backpressure, per-source/account/GPU slots`, продолжение от persistent cursor.
- `EffectIntent` и резерв D09 записываются в согласованной транзакционной границе (outbox). `PROPOSED → RESERVED → SENDING → CONFIRMED/FAILED/OUTCOME_UNKNOWN`. При неизвестном исходе **не повторять сетевую отправку**, пытаться сверить и при невозможности HOLD.
- Budget reservation и current grant переносятся после restart; no dual-write двух БД, no negative reserve, deny expired grants.

## Фактические проверки (не mock как финальный результат)
1. Два независимых read jobs имеют пересечение исполнения во времени по trace; зависимое задание ждёт. Worker processes/leases реальны, а не списки mock calls.
2. `kill -9` worker во время read: lease истекает, другой worker продолжает; late result старого rejected по fence.
3. Два contenders, один canonical business effect → один `effect_intent` даже при двух mission/версий резюме; уникальность в новой PG E1, не только в SQLite fixture.
4. Сбой **до** вызова провайдера → UNKNOWN/HOLD без отправки; сбой **после** эффекта при lost ACK → только provider reconciliation, второй submit не происходит. На тестовом fake-provider отдельно записать provider effect count.
5. Превышение общего бюджета/слота, отмена, отзыв grant и перезапуск: отсутствие незаконного dispatch, сохранённые суммы и cursor.
6. Негативный ACL/проектный тест; без E0 PG и без внешнего письма. Независимый QA принимает только persisted readback.

## Передача
Изменения source, новые additive migrations, тестовые fixtures/fault scripts, результаты реального запуска на E1 staging, журнал scheduler/ledger и commit/PR. Указать, что по состоянию `TESTED_OFFLINE`, а что `VERIFIED_LIVE`. Не объявлять crash-устойчивость для суток без отдельного теста C2.
[Основание Astra](../ASTRA-AUTONOMY-AUDIT-2026-11-08/13-delivery-handoff-to-sol.md) · [Recovery](../ASTRA-AUTONOMY-AUDIT-2026-11-08/06-resilience-updates.md)
