# Синхронизация GitHub · 09.11.2026

**Только синхронизация.** Программная логика не изменялась, ошибки не исправлялись. AWE, утилиты, LLM, платные API, БД, миграции и тесты не запускались. Проверены Git metadata, текстовые файлы, JSON и хеши. [Manifest](MANIFEST.json).

## Что опубликовано

[Runtime draft PR #10](https://github.com/failm3/awe-group-runtime/pull/10), commit `0975b891645fe9f0523415c09dd8e21ebbe3a9dd`, содержит 66 безопасных файлов из фактического локального HEAD `c9f8fd548175b68029e8dcecc061b77a154170c9` и его незакоммиченного overlay. SHA-256 каждого экспортированного Git blob совпал с оригиналом. В снимке есть Coding Executor, Head REPAIR, recovery/session, mission-runner, tool discovery/review/dispatch, тесты, checkpoints и сохранённые coding evidence.

Это **частичный аудитный экспорт, не самостоятельный runtime-пакет**. Три файла с абсолютными host-specific PostgreSQL bindings оставлены локально: `E1/coordinator/coding-run.mjs`, `E1/coordinator/migrations/0007-coding-run-state.sql`, `E1/coordinator/migrations/0008-coding-head-authority.sql`. Их SHA-256 приведены в manifest. Они не редактировались и не обезличивались. Зависимые модули нельзя считать готовым к запуску дистрибутивом без этих файлов.

Существующий [Runtime PR #9](https://github.com/failm3/awe-group-runtime/pull/9) и его опубликованная ветка сохранены. Локальные `a790a824da0e2dff15d97b98605090f29bfb30d7`, `28ad8f2e33267ed66fce466c8eb21b62cab4a482`, `c9f8fd548175b68029e8dcecc061b77a154170c9` не отправлялись: их история содержит исключённые host bindings. Новая ветка создана от опубликованного PR #9, без rebase, reset, force push или merge.

В Academy сохранены в исходных байтах четыре найденных файла: AWE-CURRENT-STATE.md и отчёты E1-CODING-IMPLEMENTATION-2026-11-08. Эта линия реализации продолжает commit `9fc932e14acacaf295f918e8777514bb430715ba`; существующий [аудит PR #29](https://github.com/failm3/nivict-ai-academy/pull/29) не переписывался. Новый документ синхронизации уточняет границы прежних WIP-отчётов, не заменяя их содержимое.

Отдельно сохранён [исторический clean-verify test report](legacy-validation/clean-verify-OFFLINE-TESTS.json) с указанием исходной линии и хеша. Это прежняя проверка, не новый PASS и не тест текущего E1. Изменённый test source в том worktree уже байт-в-байт совпадает с версией опубликованного PR #9; повторно смешивать его с новой линией не потребовалось.

## Что не подтверждено

Сохранённые coding evidence показывают FAIL исходного G1 и остановку repair на 4/4 подтверждённых запросах, без успешного продукта. Два cooperative child-restart не доказывают полный G2, произвольный crash/power-loss recovery или динамические агенты G3. Новых проверок этого вывода при синхронизации не было.

Исходники native tool canary, installed-tool probe reports и последние UTC/verifier изменения опубликованы как найдены. Исправленное полное native cold-tool evidence отсутствует: прежняя сессия остановилась на usage limit до окончания публикации и проверки последнего verifier. Ни final tool-cold PASS, ни live-сравнение script/program/local/cloud LLM здесь не утверждаются.

Прежние числовые PASS в сохранённых отчётах — исторические записи соответствующих scope. Текущая работоспособность, воспроизводимость последнего незавершённого verifier, paid Router.Cheap и production readiness не проверялись.

## Что сохранено локально

Исходные ветки/worktrees и их незакоммиченные файлы не удалялись, не перезаписывались и не откатывались. Private config, raw logs/evidence старых cloud/recruit/base линий, credential stores и PGDATA не публиковались. Данные независимых веток не объединялись в runtime-код.

HEAD исходного 51d0 — `c6c2db24c4648d96fd93c8fe7da63ba98dd9af19`; прочитанный HEAD E0/92ef — `3579aeeda379caf78dafe5351704956f1ecc0ea5`. В E0 не выполнялись операции записи, а БД не открывалась. Часть Git status-запросов к старому worktree вернула ошибку 128; его конфигурация не исправлялась, полный актуальный status этим снимком не доказывается.

Для публикации оставшихся binding-модулей требуется отдельное решение о допустимости этих путей либо отдельная задача переносимой конфигурации. В синхронизации такой разработки и изменения правил публикации не было.
