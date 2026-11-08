# AWE GROUP · E1 — исполняемые технические задания для Codex
**Дата:** 2026-11-08 · **Статус ТЗ:** READY_FOR_OWNER_HANDOFF. Реализация A1/C1 и bounded A2/A3 выполнена в указанном в outcome scope; Issue 3 — PARTIAL / NO_GO_PAID, E1 Pilot не принят.
**Основание:** независимый аудит Astra и комплект спецификаций в PR [#24](https://github.com/failm3/nivict-ai-academy/pull/24), исходная редакция `0ebbe9352daeb0fd5c6b1b309793d81ecf754937`.

## Цель
Не создавать карьерного email-бота. Доработать **общее ядро AWE GROUP**, чтобы оно принимало миссию владельца, выбирало LLM/агента/бота/скрипт/службу, исполняло реальную работу, сохраняло состояние, проверяло результат независимым QA и восстанавливалось после отказа. Доказательство: **A — карьерная миссия** и **B — независимый цифровой продукт**, на одном release ядра; далее E1 Full.

## Как передавать Codex
Передай **ссылку на этот README** и назови один или несколько ID задач. Codex должен прочитать [правила выполнения](00-EXECUTION-RULES.md) и первичные спецификации Astra, затем создать изолированную ветку/worktree **в репозитории исполняемого AWE**, а не разрабатывать runtime внутри Academy. Все зафиксированные решения и ссылки на доказательства возвращать в GitHub. В этой папке — ТЗ и отчёты с доказательствами; исполняемый код хранится в отдельном runtime-репозитории.

### Параллельная команда Codex
Для быстрого исполнения Sol выступает интегратором и может использовать до трёх встроенных subagents: A1 Contracts, C1 Infrastructure, независимый QA. [Правила делегирования и готовое сообщение Sol](10-SOL-SUBAGENT-TEAM.md). Subagents Codex — помощники разработчика, не внедрённые агенты AWE.

### Очередь
| ID | ТЗ | Зависимости / параллельность | Что считаем сдачей |
|---|---|---|---|
| A1 | [01-MISSION-CONTRACT.md](01-MISSION-CONTRACT.md) | Первым; параллельно C1 и B1 | Один контракт для двух разных миссий |
| C1 | [02-E1-ISOLATION-BOOTSTRAP.md](02-E1-ISOLATION-BOOTSTRAP.md) | Первым; параллельно A1 и B1 | Новый изолированный E1 runtime и ресурсы |
| A2 | [03-DURABLE-COORDINATOR.md](03-DURABLE-COORDINATOR.md) | A1+C1 | Настоящие параллельные workers, durable queue, restore/outbox |
| A3 | [04-MODEL-AND-CAPABILITY-BROKER.md](04-MODEL-AND-CAPABILITY-BROKER.md) | A1+C1; параллельно A2 | Настоящая локальная модель, выбор разных исполнителей, QA и бюджет |
| B1/B2 | [05-CAREER-RESEARCH-AND-PACKAGE.md](05-CAREER-RESEARCH-AND-PACKAGE.md) | Исследование/факты — сразу; интеграция — A1/A3 | Два источника, dedupe, проверяемые CV/материалы |
| B3 | [06-LIVE-EFFECT-AND-MONITOR.md](06-LIVE-EFFECT-AND-MONITOR.md) | A2+A3+B2, живое разрешение для внешнего эффекта | Один реальный допустимый отклик, readback, мониторинг |
| B4/A4 | [07-SECOND-MISSION-AND-PILOT-ACCEPTANCE.md](07-SECOND-MISSION-AND-PILOT-ACCEPTANCE.md) | A1–A3; тестовый product brief | Второй тип задачи через **то же ядро**, независимый QA |
| B5/C2 | [08-E1-FULL-AND-OPERATIONS.md](08-E1-FULL-AND-OPERATIONS.md) | A/B pilot; подготовка материалов параллельно | Реальные проекты, кампания, наблюдение и recovery |
| QA | [09-RELEASE-GATES-AND-HANDOFF.md](09-RELEASE-GATES-AND-HANDOFF.md) | Сквозной | Реальные evidence, статусы, публикация результатов |

**Параллельный старт:** A1 + C1 + подготовительная часть B1. Не создавать три конкурирующих координатора. После A1/C1 двигать A2 и A3 независимо, затем интегрировать. Рекомендация порядка не запрещает дополнительную безопасную параллельность.

### Авторитетные ссылки
- [План Astra 08](../ASTRA-AUTONOMY-AUDIT-2026-11-08/08-e1-unified-plan.md)
- [Модели и испытания 09](../ASTRA-AUTONOMY-AUDIT-2026-11-08/09-llm-routing-decision.md)
- [Портфолио 10](../ASTRA-AUTONOMY-AUDIT-2026-11-08/10-portfolio-production-plan.md)
- [Capability registry 11](../ASTRA-AUTONOMY-AUDIT-2026-11-08/11-executor-capability-architecture.md)
- [Runtime/learning 12](../ASTRA-AUTONOMY-AUDIT-2026-11-08/12-agent-runtime-and-learning.md)
- [Handoff 13](../ASTRA-AUTONOMY-AUDIT-2026-11-08/13-delivery-handoff-to-sol.md)
- [Evidence E0](../ASTRA-AUTONOMY-AUDIT-2026-11-08/01-evidence.md) и [инвентаризация](../ASTRA-AUTONOMY-AUDIT-2026-11-08/02-inventory.md)
- [Текущее состояние AWE](../AWE-CURRENT-STATE.md)

## Точки готовности
- **E0:** принят, не реконструировать.
- **E1 Pilot A:** одно подтверждённое внешнее действие + readback + монитор + recovery.
- **E1 Pilot A+B:** то же ядро, тот же runner/registry/broker/policy/QA, выполнен отдельный сценарий цифрового продукта и независимый readback после restart.
- **E1 Full:** подтверждённые материалы и живые проекты портфолио, серия разрешённых откликов, мониторинг, сутки, аварийное восстановление и безопасные обновления.
- Не выводить из двух успешных миссий доказанную универсальность ко всем будущим задачам.

## Статус и отчёты
Единая карточка для каждой задачи: `NOT_STARTED → IMPLEMENTING → TESTED_OFFLINE → VERIFIED_LIVE / BLOCKED / PARTIAL`. Каждый исполнитель пишет report: base/runtime SHA, branch, PR, exact команды и результаты, hash/refs, реальные vs mock действия, дефекты и блокеры. **Никаких заявлений DONE без проверки по критериям задания.** Старт реализации и опасные внешние действия требуют отдельного ограниченного мандата владельца; создание этих ТЗ их не запускает.


## Результат Issue 3

[Router.Cheap outcome](E1-OUTCOME-ISSUE3-CLOUD-2026-11-08.md) · [Очищенная сводка](E1-EVIDENCE-ISSUE3-CLOUD-2026-11-08.json). Код и evidence опубликованы в отдельном приватном runtime PR; здесь только документация. Paid canary NOT_RUN. Astra запущена как тест-лид Codex; исходная карьерная миссия не исполнена.
