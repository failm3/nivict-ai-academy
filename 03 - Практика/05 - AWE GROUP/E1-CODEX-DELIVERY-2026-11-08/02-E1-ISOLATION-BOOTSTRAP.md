# C1 · Изолированная инфраструктура E1 и повторяемый старт
**Статус:** READY_FOR_CODEX · **Зависимости:** актуальная инвентаризация и право подготовить отдельный E1 namespace. **Параллельно:** A1 и B1.

## Задача
Подготовить воспроизводимую, не затрагивающую E0 среду исполнения для одного authority и worker, локальной модели, отдельных QA/SEC identities и будущих карьерной/продуктовой миссий. Ресурсы запускать только в согласованном scoped окружении.

## Реализация
- Выбрать отдельное source worktree/ветку от проверенной AWE runtime revision; original `92ef` оставить read-only.
- Отдельная PostgreSQL **E1**, роли и schema/migrations с rollback strategy; никаких соединений на исторический E0 DSN, ноль монтирований E0 PGDATA. Конфигурацию создавать из template, секреты отдельно.
- Развести `owner/issuer/coordinator/worker/qa` principals; QA signing key недоступен worker; секретный store выдаёт только scoped handles для разрешённого origin.
- Служба/supervisor с health, readiness, graceful stop, crash recovery, журналом версий и резервным storage для объектов. Выделить authority node по измеренной доступности, не предполагать постоянную доступность ноутбука.
- Подготовить тестовый локальный model endpoint и adapter без облачного PII; кандидат Qwen3-8B Q4 на Mac M4 Pro 24 GB, но выбор подтверждать доступностью узла и измерениями. При отсутствии Mac runner отдельно проверять найденный Windows Qwen3:4b, не объявлять его равнозначным заранее.
- Зафиксировать `source commit, build digest, migr_version, model digest, registry version, policy version, worker IDs`.

## Проверки
1. Команда запуска из пустого E1 namespace поднимает **только** необходимые службы, повторный запуск идемпотентен; E0 storage и сервисы не затрагиваются.
2. Тестовая задача переживает штатный stop/restart; неверный principal и секрет не своего origin отвергаются.
3. Миграция на чистой E1 БД и восстановление тестовой копии проверены; при недоступном vault выполнение переходит в WAIT, не сбрасывая курсор.
4. Health/status показывают runtime version и active workload без CV, ключей, тел писем и приватных receipts.
5. Если отдельный E1 PostgreSQL ещё не разрешён/недоступен, подготовить конфигурацию и безопасные тесты, отметить `BLOCKED`; **не** переключаться на E0 ради зелёного результата.

## Выход
Runbook, конфигурационные шаблоны, миграции, smoke/recovery test, доказательство изоляции, manifest с версиями, PR исходного AWE и ссылка на результат для A2/A3.
[Основание Astra](../ASTRA-AUTONOMY-AUDIT-2026-11-08/12-agent-runtime-and-learning.md) · [Стабильность](../ASTRA-AUTONOMY-AUDIT-2026-11-08/06-resilience-updates.md)
