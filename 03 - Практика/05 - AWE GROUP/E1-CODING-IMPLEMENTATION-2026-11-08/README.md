# E1 coding implementation: bounded execution and measured failure

**Статус coding: STOPPED_MODEL_ATTEMPT_CAP_EXHAUSTED. G1 не пройден; полный G2 и G3 не доказаны.** Это результат реального исполнения после [аудита PR #29](https://github.com/failm3/nivict-ai-academy/pull/29), а не новый архитектурный проект. [Runtime draft PR #9](https://github.com/failm3/awe-group-runtime/pull/9). Исторический ограниченный SANDBOX-RECRUIT PASS остаётся действительным в прежнем scope.

## Реализованный код

На существующих A1/A2/A3/PostgreSQL/Coding Executor добавлены P0 host authority и immutable brief, реальные scoped Git/model/test/QA/local-intent ports, двухфайловый Python runner с bwrap/seccomp, независимый component QA и bounded repair controller. Одна новая таблица coding_run хранит решения/ссылки/CAS; задачи, leases/fences, usage и расходы остаются в A2/D09. Миграции 0007/0008 применены только к закреплённому E1 на 5433; 0001–0006 и E0 не менялись.

Нативные gates проверяют исходную проваленную попытку, запрет повторного принятия её как нового бюджета, реальный принятый Head и его число попыток, текущие scope/fence, отдельный product_gate и независимый QA. Сохранённый CONFIRMED ответ восстанавливается без повторного wire. Потерянный ответ/UNKNOWN не разрешает новую отправку.

## Что сделала AWE

Исходный [Issue #8](https://github.com/failm3/awe-group-runtime/issues/8) требует normalizer.py и cli.py для synthetic JSONL. Sol передал аутентифицированный GitHub snapshot, не runtime GitHub connector.

1. AWE сгенерировала оба файла; commit `0e79374b60ab35e089ab36d6d9e6787dd63dc6e9`, tree `e71dc3f0a66d1f29a09cdb572ed6d03666bf5592`. CLI содержит буквальные backslash-n вне строк; настоящий Python вернул SyntaxError. Astra независимо воспроизвела ошибку и записала QA_FAIL.
2. В новом явно ограниченном repair scope AWE Head сама выбрала REPAIR и максимум две code-попытки. Диагноз Head был неверным: предлагалось дополнительное экранирование вместо исправления переводов строк.
3. Первая repair-попытка создала commit `c63d6b1144b719788018f694acbbe83bb4ba3d02`, tree `de327dece27145f68744ce8c495f48d9f7901bcd`. Library прошла проверки, CLI/empty/sentinel не прошли. Независимый native QA записал FAIL.
4. Вторая repair-попытка вернула оба файла без изменений относительно предыдущего candidate. Контракт остановил её как CODING_NO_CHANGE; новый commit/result не выдумывались.

Драйвер автоматически выбрал второй разрешённый repair после подтверждённого провала. Два объявленных cooperative exit(90) после сохранения model response и после native completion привели к двум реальным автоматическим child-restart без команд Sol. Повторной генерации для восстановления не было. Это доказательство ограниченного продолжения фаз; произвольный SIGKILL, потеря питания, restart самого supervisor и новая lease после expiry не доказаны.

Итоговый продукт не принят. Sol после остановки по лимиту выполнил отдельное terminal finalization: outer STOPPED, новая mission CANCELLED, leases 0. Это одно ручное действие после завершения опыта; оно не скрывается как автономное продолжение.

## Фактические расходы и ограничения

| Попытка | Input | Output | Native accounting | API cost |
|---|---:|---:|---|---:|
| Исходная code | 763 | 554 | CONFIRMED | 0 |
| Head | 837 | 184 | CONFIRMED | 0 |
| Repair r02 | 1647 | 523 | CONFIRMED | 0 |
| Repair r03 | 1478 | 528 | CONFIRMED | 0 |
| Всего | **4725** | **1789** | **4/4, UNKNOWN 0** | **0** |

API cost равен нулю для локальной Ollama. Стоимость компьютера и включённого Codex usage здесь не измерялась. Исчерпанный лимит не сбрасывался новым task/project. В закрытом опыте новых генераций не будет. Router.Cheap остаётся NO_GO_PAID из-за технически не подтверждённых actual-debit cap/ACK, а не отсутствия повторного согласия владельца.

## Проверки

- 85/85 совместных host/recovery/session/repair-QA проверок, включая реальные временные Git и child-process/cache сценарии; model/native fixtures там явно offline.
- 7/7 настоящих WSL bwrap проверок runner, 21/21 offline profile проверок.
- Настоящие native CAS двух сессий и prior/Head/product/role отрицательные проверки прошли; fixtures не названы AWE-generated исполнением.
- Astra независимо перечитала PostgreSQL, raw Git commit/tree/blob, модельные квитанции, source pins и оба fault witness; семь свежих программных probes подтвердили FAIL. Это чтение не делало новых model calls.

Суммировать эти счётчики нельзя: наборы пересекаются. Финальная regression и tooling evidence публикуются в runtime PR.

## Инструменты и дальнейший путь

Существующий каталог 4 504 кандидатов найден по исходному import hash. Новый E1 bridge использует его metadata discovery, затем отдельные host review/activation, A1 refs и scoped dispatch. Весь каталог не устанавливался и повторно не собирался. Проверяемый subset — установленные ripgrep и ripgrep-all. Состояние native canary фиксируется отдельной runtime квитанцией, без смешения с coding PASS.

Политика выбора script/program/local LLM/cloud LLM реализована с quality/cost/rights/health gates. Четырёхстороннее живое сравнение LLM не заявляется. Облачная ветка закрыта финансовыми техническими gates.

Следующий coding шаг — версионированная передача исходного текста и квалификация маршрута на этом классе задач. Текущая Qwen4B дала 0 принятых code-продуктов в трёх связанных попытках; это наблюдение одного scope, не общая оценка модели. В локальном каталоге есть gpt-oss:20b, но его качество, ресурсный запас и A3 binding не проверялись. Полный G2 требует отдельного трёхфайлового задания с принятым результатом, исправлением и восстановлением; P5/G3 следуют после него.

## Кто работал

- Sol: P0, A1 mission composition, integration driver/supervisor, запуск и terminal finalization, Git/PR/отчёты. Решение candidate не писал и не исправлял.
- coding_host_p1: P1 ports, P4 native state/gates/tests; независимое инженерное review tooling и tiny native canary.
- program_runner_p2: program runner, recovery/session, каталог/review/selection/dispatch и установленные utility probes.
- Astra: независимые оракулы/QA, preflight, реальные отрицательные native/cold проверки, замечания и контроль границ результатов.

Найденные инженерные ошибки исправлены: async revoke race, Git journal intent после invalid before digest, source/test tree binding, отдельный final product gate, native Head acceptance/attempt authority, local clone transport, tool case semantics/dependency shadow и async prelaunch guard. Неисправленный candidate оставлен в точных байтах AWE.
