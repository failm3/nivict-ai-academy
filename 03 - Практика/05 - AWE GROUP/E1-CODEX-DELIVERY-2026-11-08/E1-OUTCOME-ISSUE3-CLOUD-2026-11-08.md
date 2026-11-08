# E1 Issue 3 · Router.Cheap · 08.11.2026

**PARTIAL_IMPLEMENTATION / NO_GO_PAID / CANARY_NOT_RUN.** Реализованы отдельный облачный адаптер A3, защищённый host-only discovery и общий финансовый учёт A2/D09. Проверены реальные авторизованные GET и тестовые транзакции E1. Платная генерация, исходная карьерная миссия и E1 Pilot не приняты.

Код: [приватный runtime](https://github.com/failm3/awe-group-runtime), [ветка](https://github.com/failm3/awe-group-runtime/tree/codex/e1-router-cheap-issue3-20261108), [PR](https://github.com/failm3/awe-group-runtime/pull/6), commit [3c22522c52cb6428757fd391e8630c912016b61b](https://github.com/failm3/awe-group-runtime/commit/3c22522c52cb6428757fd391e8630c912016b61b). Base — 09f1a864e6fa26afa62ffac3249c6532a6116175; PR направлен в предыдущую ветку A2/A3. Main не изменён, автоматического merge нет. [Manifest](https://github.com/failm3/awe-group-runtime/blob/3c22522c52cb6428757fd391e8630c912016b61b/release/ISSUE3-SOURCE.json) · [Независимая проверка публикации](https://github.com/failm3/awe-group-runtime/blob/3c22522c52cb6428757fd391e8630c912016b61b/E1/qa3/INDEX-REVIEW.json).

## Реально работавшая команда

| Исполнитель | Реализованный результат |
|---|---|
| cloud_a3 | Отдельный cloud broker, рациональные цены и коэффициенты источников/cache, неизменяемые quotes, запрет fallback/retry, структурированный результат и обязательный reserve/SENDING/settle/UNKNOWN. Локальный Ollama сохранён. |
| cloud_d09 | Аддитивная миграция 0003, один общий бюджет ключа для нескольких проектов, лимиты суммы/попытки/числа попыток, атомарное списание, UNKNOWN и overcharge→HOLD, ACL против обхода учёта. |
| cloud_qa | Независимые offline/host/native отрицательные проверки, совместная композиция broker+PG, проверка точного экспортируемого набора файлов и сохранности базовых исходников. |
| Astra, модель gpt-6-astra | Действительно запущена как тест-лид Codex в отдельном контексте; повторила 50 контрактных тестов и подготовила oracle/handoff исходной Career-миссии. Это не платный агент runtime AWE. |
| Sol | Trusted host helper, реальные GET, интеграция и PG-прогоны, проверка исходников/экспорта, Git и отчёты. |

Области файлов не пересекались; Git/index принадлежали интегратору. Секрет читался только доверенным WSL host-процессом. Ни агентам, ни LLM, ни shell argv/env он не передавался. Файл ключа не копировался. Проверяются владелец, 0600, один regular link и защищённые каталоги через directory descriptors/O_NOFOLLOW; TLS проверяется, proxy/redirect запрещены, вывод ограничен белым списком. [Host source](https://github.com/failm3/awe-group-runtime/blob/3c22522c52cb6428757fd391e8630c912016b61b/E1/host/router-cheap/preflight.py).

## Подтверждённые наблюдения провайдера

В 2026-11-08T03:16:42.687725+00:00 авторизованный GET models дал **75 моделей**. Subscription compatibility API показал soft/hard/system hard limit **$10**, usage endpoint — **0 US cents**. GET каталога без авторизации дал 401, GET несуществующей модели — 404. Это проверки metadata, не генераций. Реальное жёсткое ограничение списаний после всех source/balance коэффициентов остаётся **UNVERIFIED**. Баланс аккаунта и отдельные кредиты Codex/OpenAI не объединялись. [Очищенный readback](https://github.com/failm3/awe-group-runtime/blob/3c22522c52cb6428757fd391e8630c912016b61b/E1/evidence3/READONLY-PREFLIGHT-FINAL.json).

Публичный pricing snapshot a42d372ccf0b5dd13ecf71203521f9d2 содержит маршруты GPT-6 Sol и Claude Opus 4.8. Относительные коэффициенты источников GPT — 3/4…5, Claude — 125/162…3125/504. В payload отдельно присутствуют price_ratio и balance-price; их нельзя перемножать повторно или объявлять фактическими USD. GPT/DeepSeek имеют tier expressions: неизвестные выражения только хешируются, не исполняются. Chat advertised не подтверждает strict JSON schema, полный input-token bound, идентичность фактического source и charged ACK. Поэтому исполняемый каталог остаётся BLOCK. [Catalog](https://github.com/failm3/awe-group-runtime/blob/3c22522c52cb6428757fd391e8630c912016b61b/E1/cloud/catalog-status.json) · [Первичная документация Router.Cheap](https://router.cheap/reference/api.ru.md) · [Pricing](https://router.cheap/api/pricing).

## Что исполнено

| Проверка | Фактический результат |
|---|---|
| Независимые offline | 29/29 PASS, 0 skip; network/subprocess dispatch блокируются |
| Public-only export replay | 29/29 PASS; повтор той же проверки, не дополнительные уникальные тесты |
| Host custody | 7/7 PASS на синтетическом filesystem и transport |
| Независимый native E1 | 9/9 PASS: настоящие транзакции PostgreSQL, fake provider и синтетические суммы |
| Author suites | 13/13 adapter, 8/8 policy/resource, 9/9 native; пересекаются с QA |
| Предыдущая регрессия | 442/442 offline, 38/38 native, 0 fail/skip |
| Astra M0 contract | 50/50 PASS, subset регрессии, без PG/LLM; полная Career M0 NOT_RUN |
| Реальные Router.Cheap генерации | **0, NOT_RUN** |

Проверены гонки двух проектов за общий бюджет, cold readback, lease/fence/revocation, подмена quote/source/request ID, точные дроби за пределами JS safe integer, cache и округление, malformed/length response, потеря ACK и отсутствие слепого retry. D09 хранит confirmed charge, observed held charge, overrun и unknown-charge count отдельно. В синтетическом overcharge 151 при reserve 150 readback показывает booked 0 / held 151 / overrun 1 и HOLD; missing ACK сохраняет actual charge NULL. Ноль booked не означает нулевой фактический расход.

[QA](https://github.com/failm3/awe-group-runtime/blob/3c22522c52cb6428757fd391e8630c912016b61b/E1/qa3/REPORT.md) · [Native oracle](https://github.com/failm3/awe-group-runtime/blob/3c22522c52cb6428757fd391e8630c912016b61b/E1/qa3/NATIVE-REVIEW.json) · [Regression offline](https://github.com/failm3/awe-group-runtime/blob/3c22522c52cb6428757fd391e8630c912016b61b/E1/evidence3/LEGACY-OFFLINE.json) · [Regression native](https://github.com/failm3/awe-group-runtime/blob/3c22522c52cb6428757fd391e8630c912016b61b/E1/evidence3/LEGACY-NATIVE.json) · [D09](https://github.com/failm3/awe-group-runtime/blob/3c22522c52cb6428757fd391e8630c912016b61b/E1/coordinator/CLOUD-ACCOUNTING-REPORT.md).

В ходе интеграции исправлены несовпадения route/model snapshot и provider request ID, подмена ценовых evidence, маркировка fake charges, большие рациональные дроби, вывод выражений/имён из provider metadata и защита пути к секрету. Подготовлен disable-cloud, сохраняющий shim, ledger и UNKNOWN; он не исполнялся. Откат только старого psql entrypoint небезопасен и не поддерживается.

Окончательный readback E1: **0 authenticated funding rows**, reserved/spent 0, реальные лимиты 0/0/0. Платных генераций нет; API ключа сообщает usage 0 cents. Codex orchestration, электричество и изменения баланса всего аккаунта здесь не измерялись. Frozen 0001/0002 и Ollama не изменены. E0/92ef и исходный 51d0 сохранены, подключений к E0 — 0. [Preservation](https://github.com/failm3/awe-group-runtime/blob/3c22522c52cb6428757fd391e8630c912016b61b/E1/evidence3/ORIGINAL-PRESERVATION.json) · [Funding](https://github.com/failm3/awe-group-runtime/blob/3c22522c52cb6428757fd391e8630c912016b61b/E1/evidence3/REAL-FUNDING-DISABLED.json).

## Canary и решения

Подготовлен **не выданный** canary: одинаковая SYNTHETIC code-review задача для GPT-6 Sol и Claude Opus 4.8, до $0.25 на попытку, $0.50 всего, две попытки, без retries. Это предложение лимитов, не разрешение и не подтверждённая оценка цены. [План](https://github.com/failm3/awe-group-runtime/blob/3c22522c52cb6428757fd391e8630c912016b61b/E1/cloud/canary-plan.json).

До исполнения нужны:

1. Подтверждённое провайдером ограничение фактически списываемых денег после всех коэффициентов, включая параллельные запросы и предел одного запроса, и конкретный расходный grant владельца.
2. Техническая проверка конечных цен/источников, полного input bound и контракта actual-charge ACK/readback.
3. Завершение live host binding с реальным native accounting authority. Сегодня send и выдача paid policy отключены; input verifier возвращает false. Fake accounting не может стать live authority при будущем включении.

Исходная миссия и последующие задания: Astra подготовила [handoff](https://github.com/failm3/awe-group-runtime/blob/3c22522c52cb6428757fd391e8630c912016b61b/E1/astra3/LEAD-HANDOFF.md). Параллельно готовы B1 synthetic source/dedup/coverage, B2 проверка фактов/пакета и независимые отрицательные oracle; они не требуют Router расходов или отправки откликов. Реальный пакет требует разрешённых owner facts/материалов, внешний эффект — отдельного мандата. Issue 2 coding pilot остаётся другой задачей без автоматически выданного разрешения. Новые дизайнерские проекты не инициировались.

[Машиночитаемая очищенная сводка](E1-EVIDENCE-ISSUE3-CLOUD-2026-11-08.json).
