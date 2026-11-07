# A3 · Настоящий интеллект, единый реестр и выбор исполнителей
**Статус:** READY_FOR_CODEX · **Зависимости:** A1+C1. **Параллельно:** A2 и B1; интегрировать через согласованные контракты.

## Цель
Подключить живую модель к Head Agent и дать AWE возможность выбирать **LLM-вызов, подагента, бота, скрипт, программу или инструмент**. Это общий механизм A/B и следующих линий, не набор жёстких правил под резюме.

## Реализовать
1. **Capability Registry v1:** запись конкретной версии операции, `executor_kind`, schemas, source/build digest, platform, placement, limits, inputs/outputs, data classes, required permissions, cost, QA suite, retry/reconcile, approved status, health/last canary. Каталог 4 504 — discovery-кандидаты; не считать их 4 504 установленными capabilities.
2. **Selector:** перед ранжированием исключать incompatible/unavailable/revoked/denied routes; для детерминированного задания предпочитать проверенный скрипт/службу; ограниченную семантическую задачу отдавать одной LLM; многошаговую — bounded agent; команду создавать только при независимых ветвях и/или независимом QA. Стоимость — accepted result с затратами на коррекцию, а не только токены.
3. **Live model broker:** versioned model binding, privacy labels, region/provider allowlist, structured schema, usage, latency, attempts, cost reserve/settle D09, backoff и no-unsafe-fallback. Qwen3-8B Q4 на Mac — стартовый **кандидат**, наличие/скорость проверить фактически; Windows qwen3:4b-instruct — запасной кандидат, не считать доказанной рабочей конфигурацией.
4. **Cloud:** GPT-6.1 Sol / Terra / другие модели из [09](../ASTRA-AUTONOMY-AUDIT-2026-11-08/09-llm-routing-decision.md) — кандидаты только при разрешённом аккаунте/регионе, типе данных и лимите. Codex-подписка не означает доступ к API. Нельзя посылать резюме/HH-данные в облако по умолчанию.
5. **Head/worker:** Head возвращает только типизированный proposal; scheduler и broker проверяют право на каждый tool вызов. Нет прямого shell/network/DB доступа у сырого вывода LLM. Отдельные bot event adapters, CLI/scripts и interactive browser tools применяют тот же capability contract, но разные policies.
6. **QA:** используй существующий QA-порт, frozen artifact digest, независимую роль, schema + semantic checks; модель не может сама повысить budget, принять свой результат или открыть tool.
7. **Benchmark:** собери исполняемый одинаковый набор задач для local/model competitors (план A/B, анализ источника, небольшой код, реальный browser QA и malformed/tool misuse). Отдельно записать, какие маршруты реально вызваны и почему недоступны остальные.

## Приёмка
- Настоящий локальный model response создаёт либо исправляет типизированный план одной миссии; recorded model ID/digest и usage/latency действительно получены от backend, не synthetic token counts.
- Registry выбирает минимум **два разных executor_kind** для конкретных tasks; программный парсер без LLM, семантический worker с LLM; логируются причины отклонения альтернатив.
- Попытка вызвать отсутствующий tool, изменить grant/budget, направить PII на недопущенный endpoint, вернуть invalid JSON, промпт из внешней вакансии с подменой recipient → BLOCK/REPAIR без эффекта.
- Тестовая модель недоступна: controlled WAIT/fallback **только внутри разрешённой политики**, не бесконечный retry и не безмолвный cloud.
- Независимый QA отклоняет намеренно испорченный результат, а не подтверждает любой `DONE`.
- Таблица benchmark содержит measured vs NOT_RUN; не объявлять «лучшую LLM» на основе документации.

## Выход
Working model adapter + selector/registry + тесты и baseline measured results + manifests и logs без секретов + source PR. Указать влияние на качество, задержки и фактический cost/accepted.
[Capability spec](../ASTRA-AUTONOMY-AUDIT-2026-11-08/11-executor-capability-architecture.md) · [Model spec](../ASTRA-AUTONOMY-AUDIT-2026-11-08/09-llm-routing-decision.md)
