# AWE GROUP · текущее состояние

**08.11.2026 · Issue 3: Router.Cheap PARTIAL / NO_GO_PAID. Отдельный A3 и native D09 проверены; платных генераций 0. Astra запущена как тест-лид Codex. Исходная Career-миссия и E1 Pilot не приняты.**

| Что проверять в начале следующего чата | Актуальная запись |
|---|---|
| Принятый рубеж | **E0 COMPLETE / OWNER_ACCEPTED** для одной локальной задачи. Runtime source c53d1fb3606218a4f3961f37f57ebc41ac6681ef, итоговый HEAD 3579aeeda379caf78dafe5351704956f1ecc0ea5, D03 commit 54, QA 7/7, артефакт 36 B. Исторические NO-GO относятся к более ранним состояниям. [Evidence](ASTRA-AUTONOMY-AUDIT-2026-11-08/01-evidence.md) |
| Обязательные решения владельца | Текущий приоритет — первый автономный контур и затем разрешённая GitHub self-development задача. A1/C1 приняты только в пределах offline-проверок; E1 Pilot не принят. Новые дизайнерские идеи/проекты не инициировать. Реальные отклики/production/auto merge не разрешены. Платные генерации заблокированы до подтверждения hard actual-charge cap и конкретного расходного grant. |
| Результат проектирования | Готов один рекомендуемый план. В существующем AUTO-01 две синтетические миссии по одному entrypoint завершились MOCK_WORK_COMPLETED: 6 и 5 задач. Ни одной live миссии этим не подтверждено. Публичный кейс портфолио прочитан на двух размерах браузера. [План](ASTRA-AUTONOMY-AUDIT-2026-11-08/08-e1-unified-plan.md) |
| Предложения до решения владельца | Исторические предложения Astra сохранены в исходных документах. В текущем scope выполняется A2/A3 + подготовка Coding Executor; отдельный новый дизайнерский проект не запускается. |
| Активные работы / блокеры | [Issue 3 runtime PR](https://github.com/failm3/awe-group-runtime/pull/6), commit 3c22522c52cb6428757fd391e8630c912016b61b. 29 independent offline + 7 synthetic host + 9 actual-PG/fake-provider PASS; регрессия 442/38 PASS. GET: 75 моделей, номинальный лимит $10, usage 0. Фактический hard cap после коэффициентов и charged ACK не подтверждены; paid host отключён. Прежние gaps OS sandbox/global GPU/24 h и Coding Executor live WAIT сохраняются. |
| Ближайшее действие | Astra: synthetic B1/B2 source coverage/dedup/facts и независимые oracle. Для cloud canary — подтверждённый actual-charge hard cap, конкретный grant и завершённый live host/native accounting binding. [Outcome](E1-CODEX-DELIVERY-2026-11-08/E1-OUTCOME-ISSUE3-CLOUD-2026-11-08.md). |

**Версия действующего комплекта документов:** [77fe177c411239034ee2851c0f3e9fbf3f4cfe03](https://github.com/failm3/nivict-ai-academy/commit/77fe177c411239034ee2851c0f3e9fbf3f4cfe03). Полный исходный аудит собран в [8c8faa2fca4c8a889e3cd27fcc0da93e6e5da47f](https://github.com/failm3/nivict-ai-academy/commit/8c8faa2fca4c8a889e3cd27fcc0da93e6e5da47f). SHA последнего изменения **самого указателя** доступен в [истории этого файла](https://github.com/failm3/nivict-ai-academy/commits/main/03%20-%20Практика/05%20-%20AWE%20GROUP/AWE-CURRENT-STATE.md). Так указатель может ссылаться на точную версию спецификаций без самоссылки на ещё не созданный commit.

[Модели и benchmark](ASTRA-AUTONOMY-AUDIT-2026-11-08/09-llm-routing-decision.md) · [Портфолио и B](ASTRA-AUTONOMY-AUDIT-2026-11-08/10-portfolio-production-plan.md) · [Исполнители](ASTRA-AUTONOMY-AUDIT-2026-11-08/11-executor-capability-architecture.md) · [Runtime и обучение](ASTRA-AUTONOMY-AUDIT-2026-11-08/12-agent-runtime-and-learning.md) · [Полнота импорта](ASTRA-AUTONOMY-AUDIT-2026-11-08/IMPORT-STATUS.md)


## 08.11.2026 — пакет исполняемых ТЗ Codex (добавлено ChatGPT)

**Статус:** `E1_TECHNICAL_TASKS_READY / IMPLEMENTATION_NOT_STARTED`. На основе архитектурных документов Astra созданы [10 отдельных технических заданий для Codex](E1-CODEX-DELIVERY-2026-11-08/README.md). Внутри: общий runtime-contract (A1), отдельный E1 namespace (C1), durable coordinator (A2), live LLM и реестр исполнителей (A3), карьерный ingest/package (B1/B2), разрешённый effect+monitor (B3), вторая предметная область и QA (B4/A4), E1 Full (B5/C2), сквозные критерии приёмки. **Дизайнерские концепции не утверждены и не предложены вместо brief владельца.**

Задания опубликованы **в ветке открытого PR #24**, не в `main`. Для запуска Codex читать [индекс](E1-CODEX-DELIVERY-2026-11-08/README.md) на ветке `codex/awe-master-architecture-e1-20261108`. Первоисточник архитектуры Astra закреплён коммитом `0ebbe9352daeb0fd5c6b1b309793d81ecf754937`; исходное дерево E0 `92ef` — только для чтения. Исполняемый AWE runtime в Academy не хранится. **Подготовка ТЗ не разрешает запуск E1, новых PostgreSQL, платных API, реальных откликов или деплоя** без подходящего мандата.

Первый логический параллельный пакет: **A1 + C1 + подготовительная B1**. После этого A2 и A3. Отчёт по каждому этапу публиковать с actual code commit, independent QA и измеренным уровнем доказательств.


## 08.11.2026 — предложена команда субагентов Sol

**[TEAM_PLAN_READY / NOT_LAUNCHED]** Для реализации A1 и C1 в Codex составлено [ТЗ на встроенную multi-agent команду](E1-CODEX-DELIVERY-2026-11-08/10-SOL-SUBAGENT-TEAM.md): Sol — интегратор; A1 Contracts, C1 Infrastructure и независимый QA — до трёх subagents. Они не являются запущенными агентами AWE. Изменения разделять по worktree/file scope, итог Sol проверяет на одном release. Встроенные подтверждения Codex и отдельные ограничения для E1/live остаются действующими. Новый E1 runtime ещё не реализован.


## 08.11.2026 — выполнен первый A1/C1 этап (Sol)

**A1 TESTED_OFFLINE / C1 PARTIAL-BLOCKED / G1 PARTIAL.** Владелец разрешил локальную реализацию и три встроенных субагента; реально работали Contracts A1, Infrastructure C1 и Independent QA. Реализованы versioned mission/grant/plan contracts, общий AWE_E1 ingress двух доменов, изоляционный preflight и локальные process/filesystem fixtures. Финально **679/679 PASS, 0 FAIL, 0 SKIP**; отдельный QA проверил 130 тестов и хеши evidence. Native PostgreSQL suite явно NOT_RUN. Это не автономность, signed D08 или E1 Pilot/Full.

Локальный source commit `b689248952a3282fdda0b9f020f4cc014f610926`, ветка `codex/awe-e1-a1-c1-20261108`, build `sha256:891bb008f1a0c7bf7a0303c98990cd8c44d000cee84d2b65ec2dd54c0d0159c1`. Оригинальные E0/92ef и PGDATA не изменялись. Runtime repository/source PR не созданы: перенос истории остановлен по условию владельца после обнаружения закрытых E0 metadata. История не переписывалась и не отправлялась. Нужен выбор способа сохранения закрытой истории; новая PostgreSQL E1 также требует отдельного ресурса/разрешения. В Academy опубликована только очищенная сводка, без runtime кода, secrets, PII или PGDATA. Записи `IMPLEMENTATION_NOT_STARTED` в прежних разделах описывают состояние до этого разрешённого запуска.

[Подробный outcome и handoff](E1-CODEX-DELIVERY-2026-11-08/E1-OUTCOME-A1-C1-2026-11-08.md) · [Очищенная сводка evidence](E1-CODEX-DELIVERY-2026-11-08/E1-EVIDENCE-A1-C1-2026-11-08.json)


## 08.11.2026 — выполнен A2/A3 этап (Sol)

**VERIFIED_BOUNDED_LOCAL_G2_G3 / FULL_E1_PARTIAL / PILOT_NOT_ACCEPTED.** Владелец разрешил отдельную чистую runtime-историю и изолированную PostgreSQL E1. Эти два прежних организационных блокера сняты. Реально работали coordinator_a2, broker_a3 и qa_a2_a3; интегратор соединил normal A1 ingress, native coordinator, реальный Ollama, script и независимый QA. https://github.com/failm3/awe-group-runtime/pull/1 · source 09f1a864e6fa26afa62ffac3249c6532a6116175. Финально 442/442 offline + 38/38 native, независимый повтор 45/45, zero skip. Никакого merge в main.

Две действительные model responses привели к плану revision 2 и COMPLETE с сохранёнными usage/cursor после нового OS-процесса. Сохранены первоначальный timeout UNKNOWN/HOLD/quota 1 и E0/92ef; quiescence освободил только физический слот. PostgreSQL E1 прошёл clean migration/restart/backup-restore/изоляционные отрицательные проверки. Подготовленный Coding Executor проверен на tempGit fixtures, но реальную GitHub-задачу не исполнял. G4/G5/G6, owner/D08 acceptance, production и 24 h не заявлены.

[Outcome](E1-CODEX-DELIVERY-2026-11-08/E1-OUTCOME-A2-A3-2026-11-08.md) · [Evidence](E1-CODEX-DELIVERY-2026-11-08/E1-EVIDENCE-A2-A3-2026-11-08.json). Предыдущие записи о запрете ресурса/публикации описывают состояние до нового решения владельца.


## 08.11.2026 — Issue 3: Router.Cheap и Astra

**PARTIAL_IMPLEMENTATION / NO_GO_PAID / CANARY_NOT_RUN.** Реально работали cloud_a3, cloud_d09, cloud_qa; затем отдельная Astra (gpt-6-astra) как тест-лид Codex. Host-only секрет не передавался агентам. Реальные metadata GET подтвердили 75 моделей, compatibility limit $10 и usage 0; точные actual-charge цены/пределы и live host binding ещё не доказаны. Native shared D09 выдержал отрицательные гонки, UNKNOWN, overcharge и финансовый readback; реальные funding rows отсутствуют. Новых paid calls, E0 изменений и merge нет. Исторические утверждения выше относятся к своим прежним этапам.

[Outcome](E1-CODEX-DELIVERY-2026-11-08/E1-OUTCOME-ISSUE3-CLOUD-2026-11-08.md) · [Evidence](E1-CODEX-DELIVERY-2026-11-08/E1-EVIDENCE-ISSUE3-CLOUD-2026-11-08.json) · [Runtime PR](https://github.com/failm3/awe-group-runtime/pull/6). Astra повторила 50 синтетических контрактных тестов; реальная Career-миссия NOT_RUN, E1 Pilot не принят.
