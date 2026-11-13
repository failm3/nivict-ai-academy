# 09 · Контроль готовности, независимый QA и handoff между Codex
**Статус:** ОБЯЗАТЕЛЬНЫЙ ПРОТОКОЛ ПРИЁМКИ.

## Модульные gate
| Gate | Доказательство | Нельзя принимать вместо |
|---|---|---|
| G0 — E0 baseline | Только чтение оригинальных evidence, source SHA/pins, 7/7 signed QA | Новый запуск/переписывание E0 |
| G1 — contracts + isolated host | A/B schemas, deny tests, отдельный DB/project, start/restart | README о «готовой архитектуре» |
| G2 — durable coordinator | Временное перекрытие двух worker, fence takeover, persisted budget/outbox на E1 PG | Один последовательный mock run |
| G3 — real intelligence/selector | Действительный model ID/digest/usage, два executor kinds, независимый QA reject на seeded error | Подставной model output, рейтинг из документации |
| G4 — A внешний эффект | Актуальная вакансия, ограниченный grant, одна реальная разрешённая отправка, независимый Sent readback, cursor monitor | Изображение кнопки, mock почта или локальное `DONE` |
| G5 — B другая предметная область | Иной goal, тот же core release и brokers, продуктовый staging с реальным client journey, персистентность/roles после restart | Дизайн-макет, fixture с заранее прописанным «успехом», ручная работа Codex без AWE |
| G6 — Full | Принятые CV/реальные портфолио проекты, серия откликов, наблюдение 24 ч, restore и мониторинг | Один email и зелёные offline тесты |

Никакой один passing gate не автоматически закрывает другие.

## Как проверяющий определяет статус
- `IMPLEMENTED` — код есть; runtime не обязательно запускался.
- `TESTED_OFFLINE` — исполнены названные tests/fixtures; live не доказан.
- `VERIFIED_LIVE` — подтверждён реальный эффект в указанной среде, с provider/independent readback и digest, без конфиденциальных данных в открытом отчёте.
- `PARTIAL` — работающая часть плюс явный gap.
- `BLOCKED` — недостающий доступ/грант/материал или ошибка; требуется точное условие разблокировки.
- `UNKNOWN` — исследование/измерение не выполнено.

## Чеклист каждого Codex handoff
- Название задания, scope и исходная спецификация/commit, base source worktree и actual `git rev-parse HEAD`.
- Implementation branch / PR / source commits, build/registry/model/policy/migration versions.
- Команды, exit status, реальные результаты positive/negative/crash tests, timestamps и duration, когда важны.
- Что действительно происходило: actual calls, mock counts, no. external effects, provider IDs только через безопасные ссылки/редакцию.
- QA независим от исполнителя: principal и hashes, фальсифицирующий seeded test.
- Отдельные unresolved issues, explicit limits и **следующие готовые задачи**, блокеры и зависимости.
- Правило публикации: документы и статус → GitHub Academy в согласованную ветку, код → отдельный приватный runtime source repo/ветку; secrets/PGDATA/private CV/полные receipts — нет.
- Перед изменением `AWE-CURRENT-STATE.md` прочитать **актуальный удалённый ref**, не затирать чужой статус. Не отмечать owner acceptance без владельца.

## Отдельные ограничения проекта
- Документы этого пакета **не** разрешают сетевую отправку откликов, выдачу ключей, открытие платных аккаунтов или деплой.
- Для живой кампании нужна одна понятная owner policy, не отдельные подтверждения на каждую штатную операцию. Нельзя обойти ограничения платформы Codex собственным ТЗ.
- Если решение Astra требует изменений, фиксировать конкретный error/invariant и сравнительное доказательство, а не запускать заново бесконечный архитектурный аудит.
- Измерять принятый результат, не обещать дату. Отдельная разработка сайтов не становится «автономной AWE», пока не предъявлена трасса AWE и независимая приёмка.

## Финальный документ этапа
`E1-OUTCOME-<ID>.md` в этой директории либо другом явно указанном GitHub-пути: gate, status, delivered vs missing, tests, evidence URL, limitations, next ID. Ссылку передать следующему Codex. После G4 и G5 сообщить владельцу отдельно; full AWE GROUP не объявлять finished.
[Индекс ТЗ](README.md) · [Handoff Astra](../ASTRA-AUTONOMY-AUDIT-2026-11-08/13-delivery-handoff-to-sol.md)
