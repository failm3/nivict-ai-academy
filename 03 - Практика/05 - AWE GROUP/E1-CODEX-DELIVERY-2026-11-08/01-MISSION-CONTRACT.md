# A1 · Универсальный контракт миссии и действий
**Статус:** READY_FOR_CODEX · **Зависимости:** E0 evidence и спецификации Astra. **Можно параллельно:** C1 и B1.

## Задача
Провести одну миссию от `mission.create(goal, project, owner, criteria, facts_refs)` до валидированного плана и типизированного набора действий. **Никакой специализации career/email внутри координатора.** Одна схема для A (карьера) и B (независимый цифровой продукт).

## База для реализации
Проверить `AUTO-01/contracts.mjs`, `AUTO-01/draft.schema.json`, существующие DAG validators, `INTEGRATION-01/adapters/int04-host.mjs`, D01/D02 policy и `createInt04OfflineHost` family. Не копировать mock-профиль как live.

## Обязательные интерфейсы
- Версионированные `MissionSpec`, `MissionGrant`, `PlanRevision`, `TaskSpec`, `CapabilityRef`, `ArtifactRef`, `EffectIntent`, `QAResult` с schema validation и canonical hashes.
- `mission.create / mission.revise / mission.revoke`; `plan.propose / plan.validate / plan.publish`. Head предлагает, coordinator исполняет только прошедший валидацию DAG.
- `TaskSpec` связывает `capability_id@version`, input/output schemas, dependency IDs, budget, deadline, data classes, эффект, retry/reconcile, QA rubric. Выбор исполнения — отдельный контракт, не `if career/product` в scheduler.
- Граница scope: owner / project / mission / permission / data-class; grant содержит issued/expiry/revocation/version, allowed capabilities, destinations, bounds, max actions, budget cap; запрет самоповышения.
- Для E1 добавить отдельный composition root/entrypoint; существующие AUTO-01/LOOPBACK тесты и сериализации не ломать.

## Приёмка (реальные автоматические проверки)
1. Одинаковый обычный ingress валидирует два разных fixtures A/B и создаёт DAG с зависимостями; фиксируется одинаковый release/контракт, разные project IDs и domain manifests.
2. Отсутствующая capability, неверный schema digest, цикл DAG, неверный actor, expired/revoked grant, чужой project и self-increased budget приводят к `REJECT/WAIT` до запуска.
3. Head может исправить план только в заданных пределах: bounded replan, записанная причина, неизменяемая история версий. Никто не может сделать `accepted=true` через особый test-only путь.
4. Совместимость с E0 fixtures проверена; никакой операции на E0 PG и никакой внешней отправки.

## Выход
Код + контрактные схемы + позитивные/негативные тесты + пример двух domain manifests + manifest SHA + changelog совместимости + ссылка на PR и следующее задание A2/A3. **Статус:** максимум `TESTED_OFFLINE` до участия настоящих workers.
[Основание Astra](../ASTRA-AUTONOMY-AUDIT-2026-11-08/08-e1-unified-plan.md) · [Capability](../ASTRA-AUTONOMY-AUDIT-2026-11-08/11-executor-capability-architecture.md)
