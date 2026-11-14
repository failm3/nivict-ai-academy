# Nox: универсальность, самостоятельное расширение и пересмотр стратегии

Дата: 2026-11-14  
Характер: **независимое инженерное заключение; без реализации и испытаний**  
Предмет пересмотра: стратегия из `NOX-R2-INDEPENDENT-AUDIT-2026-11-14`.

## 0. Короткий ответ

**Опасение обосновано, но вывод «вертикальные сценарии вредят универсальности» был бы неверен.** Они необходимы как испытания и источник требований. Опасен другой путь: превращать каждую новую профессию в отдельную ветку Prompt Master, Mission Manager или QA, а затем называть сумму таких веток универсальным интеллектом.

Моя прежняя стратегия была правильной по приоритету correctness, но **недостаточной и слишком поздно выводила на первый план механизмы генерализации**. После минимального P0 она могла привести к надёжному набору профессиональных workflows раньше, чем к системе, способной решать незнакомые задачи без доработки.

Я меняю рекомендацию:

> **Сохранить EXTEND и P0-min, но следующим основным направлением сделать не repo/doc packs, а generalization loop и Capability Plane. Профессиональные задачи использовать как скрытые проверки и разнообразные нагрузки на общий механизм, а не как единицу архитектуры.**

Целью должна быть не метафизическая «универсальность вообще», а измеримая **bounded generality**: замороженная версия Nox решает новые задачи из заранее заданного распределения, в явных бюджетах и полномочиях, без task-specific изменений разработчиком.

---

## 1. Позиция относительно риска специализации

### 1.1. Когда профессиональные slices полезны

Хороший slice выявляет общий недостаток: нехватку контракта инструмента, невозможность проверить binary artifact, слабое перепланирование, неполную стоимость или отсутствие восстановления. Repo patch и document workflow особенно полезны, потому что требуют разных evidence и external oracles.

Нельзя доказать перенос, вообще не решая конкретных задач. Полностью отказаться от прикладных испытаний ради абстрактной «универсальной платформы» было бы хуже: появилась бы сложная capability-инфраструктура без доказанной пользовательской ценности.

### 1.2. Когда они становятся ловушкой

Slice вредит генерализации, если для его PASS:

- добавляется распознавание профессии и отдельный recipe в core;
- Head получает готовый план вместо построения стратегии;
- инструмент жёстко подключается под известный fixture;
- verifier знает заранее ожидаемую форму решения, а не критерии качества;
- после неудачи разработчик меняет prompt/workflow и повторяет тот же тест как доказательство transfer;
- успех измеряется числом покрытых форматов, ролей или доменов.

В текущем Nox уже есть узкие CSV/web/lesson механизмы. Это полезные capabilities и verifiers, но также предупреждение: если аналогичные специальные ветки станут основным способом расширения, получится dispatcher профессиональных recipes.

**Вывод:** проблема не в двух выбранных профессиях, а в прежнем центре тяжести и критерии прогресса. Нужно изменить и архитектурный принцип, и измерение: не «добавили документы», а «неизменённый core научился решать новый класс задач через приобретённую capability».

---

## 2. Соответствие текущей архитектуры конечной цели

### 2.1. Подтверждённые факты: что уже является общей основой

По исходникам `r1/dev@68cc0ee20a25991ea275512e20ac521cc8f8234b` и сохранённым evidence:

| Общий механизм | Текущее состояние | Значение для цели |
|---|---|---|
| Спецификация и approval | Typed spec, acceptance criteria, hash binding | Есть общий входной контракт; clarification/edit loop неполон |
| Head | Динамически формирует задачи, роли, параллельность и tool grants | Не фиксированный roster; есть основа mission-specific команд |
| Рекурсивные специалисты | Синтез инструкций для ролей, depth/agent/concurrency limits | Открытая prompt-специализация, но не автоматическое приобретение навыка |
| Исполнение | Общие files/shell/web/model primitives, параллельные делегации | Можно собирать новые комбинации действий |
| Authority | Deny-by-default, сужение child grants, approved-spec/admission/lease fences | Подходящая база для управляемого acquisition |
| Persistence/recovery | Checkpoints, durable intents, bounded repair, operator recovery | Общий lifecycle, а не отдельные профессиональные сценарии |
| Evidence/QA | Artifacts с hash/size, независимый LLM QA и deterministic gate | Есть контур проверки, но reviewed candidate и полнота evidence требуют P0 |
| Models | Host-owned per-agent/per-role routing | Выбор модели уже отделён от исполнителя, но не является автономной оптимизацией |
| Память | LibSQL history и узкий persisted lesson reuse | Persistence есть; обобщённый retrieval и доказанный transfer отсутствуют |
| Discovery | Research catalogs и один Playwright MCP path | Есть отправные точки, но не сквозной acquisition lifecycle |

Это серьёзный **general-purpose bounded execution kernel**. Переписывать его ради универсальности не нужно.

### 2.2. Подтверждённые факты: что действительно отсутствует

1. **Наблюдаемый общий цикл перепланирования.** Делегация и repair существуют, но это ещё не доказанный `plan → observe → diagnose → replan` для новых задач. Silent fallback Head в generic executor скрывает planning failure.
2. **Общее описание потребности в capability.** Нужны входы/выходы, effects, data sensitivity, ресурсы, требования к verifier и acceptance, а не просто имя инструмента.
3. **Сквозной acquisition:** `discover → select → acquire → inspect → qualify → approve → admit → invoke → observe → update/revoke`.
4. **Per-mission capability broker.** Нужны единые contracts для MCP, API, Skills, sources и verifiers, со scoped grants и изоляцией executable code.
5. **Автономный выбор модели/маршрута в host policy.** Текущий routing статичен по роли/host config; нет measured quality/cost policy, позволяющей Head выбирать из разрешённых вариантов.
6. **Переносимая competence.** Нет версионируемых записей с applicability, exclusions, failures, provenance, qualification evidence и revoke; сохранённый paired CSV result не показал uplift.
7. **Общий evidence contract для незнакомых результатов.** LLM QA остаётся полезным reviewer, но не универсальным ground truth. Нужны executable checks, external state readback, native readers и при необходимости независимый эксперт.
8. **Доказательство bounded generality.** Нет программы скрытых задач, freeze-source, paired baselines и fresh holdouts.

### 2.3. Что не нужно разрабатывать самостоятельно

Не следует создавать собственные протоколы и инфраструктуру там, где есть зрелые стандарты:

- MCP SDK, JSON Schema/OpenAPI — discovery, contracts и invocation;
- Agent Skills и существующие validators/package tooling — packaging/progressive disclosure, но не automatic trust;
- нативные package managers/lockfiles и OCI-инструменты — immutable distribution;
- Sigstore/in-toto/TUF, SPDX/CycloneDX/OSV — provenance, SBOM и vulnerability data, по фактической необходимости;
- OAuth/OIDC, OPA/Cedar — identity/policy, без собственной криптографии;
- OCI runtime, gVisor/Firecracker/VM — изоляция по уровню угрозы;
- OpenTelemetry — traces;
- Playwright, document/data processors, Windows UI Automation — конкретные capabilities.

Mastra можно сохранить как agent/tool/memory integration. Temporal, LangGraph, PostgreSQL, vector DB и Langfuse не должны становиться новыми архитектурными центрами без измеренной потребности. Подпись пакета доказывает происхождение, но не его безопасность или полезность.

---

## 3. Слабые места прежней стратегии именно для универсальности

### 3.1. Слишком поздний capability acquisition

Формулировка «ToolSearch/Skills только после measured gap» защищала от лишней сложности, но была слишком пассивной для заявленной цели. **Само приобретение новой capability — обязательная функция продукта**, а не опциональная оптимизация после профессиональных packs.

Нужно не blanket ToolSearch, а минимальный end-to-end acquisition loop, проверенный на ранее неизвестном сервере/инструменте.

### 3.2. Профессиональные slices были следующим основным этапом

После P0 repo/doc были поставлены раньше общего replanning, discovery и transfer evaluation. Это повышало вероятность оптимизации под два известных направления.

Я переношу их в **development set**: они остаются кандидатами, но не имеют привилегированного статуса и не определяют core design.

### 3.3. Недостаточный контрастный baseline

Сравнение только с прежним Nox не показывает, нужна ли multi-agent архитектура. Тот же результат может дать одна сильная модель с обычными tools.

Для каждого заявления о пользе orchestration/acquisition/memory нужны равнобюджетные controls: single-agent, no-acquisition, frozen capabilities, memory off. Иначе успех нельзя атрибутировать архитектуре.

### 3.4. Смешение внутреннего QA и доказательства новизны

Даже отличный mission QA не доказывает generality. Benchmark acceptance должен быть внешним и скрытым от solver. Candidate-authored tests могут быть частью работы, но не единственным oracle.

### 3.5. Недостаточно явная экономика автономии

Больше агентов и инструментов может увеличить success лишь за счёт непропорциональных tokens, времени и вмешательств. Нужна стоимость **одного независимо подтверждённого результата**, включая failures, repairs и acquisition, а не только стоимость удачных миссий.

---

## 4. Пересмотренная стратегия

### Принцип

Развивать три плоскости, не создавая второй orchestrator:

```text
GENERAL MISSION KERNEL
  spec → plan → delegate → observe → diagnose/replan → verify → recover

HOST-OWNED CAPABILITY PLANE
  requirement → discovery → candidate → qualification → approval
  → scoped invocation → evidence/usage → competence/revoke

INDEPENDENT GENERALITY EVALUATION
  frozen system → hidden tasks → external oracle
  → paired baselines/ablations → fresh holdout
```

Domain knowledge и processors живут в replaceable capabilities и verifiers. Mission Manager не должен узнавать профессию каждой новой задачи.

### Направление 1 — P0-min: доверие к измерениям

Сохранить прежний приоритет, но ограничить его необходимым барьером:

- canonical artifact paths/revisions;
- immutable CandidateEpoch и verdict ↔ exact reviewed bytes;
- полный EvidenceBundle или независимый oracle для binary/domain output;
- fail-closed mutation/stale review/late write/unresolved intent;
- no-progress и полный whole-mission usage ledger.

Это не этап бесконечного production-hardening. Его назначение — сделать последующие generality experiments достоверными.

### Направление 2 — общий loop вместо новых профессиональных веток

Минимально усилить существующий MM/Head:

1. capability gap как typed состояние, а не неудачный generic tool call;
2. диагностика: неверный план, отсутствует tool, неизвестен contract, недостаточно evidence, превышен бюджет, нет полномочий;
3. bounded replanning с новым планом, не безлимитный retry;
4. route selection: deterministic program / API / single agent / team / hybrid / BLOCKED;
5. выбор модели только из host allowlist, с заранее заданными caps и последующей оценкой качества/стоимости;
6. явный PLANNING_FAILED/BLOCKED вместо скрытого generic fallback.

### Направление 3 — минимальный Capability Plane, сразу end-to-end

Не строить заранее marketplace на тысячи пакетов. Реализовать один общий contract и провести через него одну новую capability:

- `CapabilityRequirement` — что нужно получить и как это проверить;
- `Candidate` — kind, version/digest, schemas, provenance, dependencies, declared effects;
- `QualificationReceipt` — candidate digest, tests/scope, runner/policy versions, evidence и expiry;
- `CapabilityGrant` — mission/node, FS/egress/data/secret scopes, budgets, expiry/generation;
- `CompetenceRecord` — applicability/exclusions, проверенная процедура, failures, sources, holdout results, ACL/revoke.

Discovery не означает install; install не означает approval; наличие в registry не означает competence. Solver и внешний content не могут менять policy. Новый digest/schema требует новой квалификации. Executable candidates изолированы; secrets выдаются broker-side; revoke исключает capability и производные lessons.

Первый успех должен быть достигнут **без изменения core source и без ручного wiring под задачу**. Иначе это integration engineering, а не autonomous acquisition.

### Направление 4 — competence и перенос после acquisition

Сначала доказать, что новая capability работает в текущей миссии. Затем отдельно проверить, что компактный experience record помогает свежему агенту на новых входах.

Не начинать с широкого RAG, Knowledge Graph или Skills marketplace. Один source-bound pack, один held-out fresh-agent test и memory-off control достаточно для решения, есть ли измеренная польза. `NO_BENEFIT` и `INCONCLUSIVE` — допустимые результаты.

### Направление 5 — профессиональное разнообразие как нагрузка

После общего seam выполнять разнородные задачи, выбранные по типу неизвестности, а не по желанию собрать каталог профессий:

- repo patch или иной executable artifact;
- document/native output;
- dynamic browser/multimodal result;
- research с противоречивыми источниками;
- analytics на новом формате;
- draft-only external API effect.

Каждый slice обязан либо использовать существующий общий механизм, либо выявить конкретный общий пробел. Специальный domain verifier допустим как подключаемый oracle; специальный core workflow — нежелателен и требует отдельного обоснования.

---

## 5. Как доказать bounded generality

### 5.1. Freeze и независимый holdout

Независимый benchmark owner создаёт задачи, fixtures и скрытые проверки. До раскрытия задач фиксируются hashes кода, prompts, workflows, Skills/plugins, registry snapshots, model/routing config и dependencies.

Разрешены только заранее оговорённые runtime-операции: generic discovery/acquisition, временные artifacts и штатное делегирование. Запрещены task-specific изменения, подсказки, ручной tool wiring и выбор маршрута человеком после просмотра задачи.

После настройки на раскрытом holdout он перестаёт быть holdout: следующий запуск требует новых независимо созданных задач. Полностью исключить training contamination внешней LLM невозможно; проверяется **runtime novelty для Nox**, а не абсолютная новизна для модели.

### 5.2. Минимальные классы испытаний

| Испытание | Что отличает от workflow |
|---|---|
| Known positive control | Проверяет harness, не generality |
| Unseen fixture | Новая структура входов, а не другие числа/имена |
| Compositional transfer | Новая комбинация существующих capabilities без нового workflow |
| Cross-domain task | Другие artifact, environment и oracle, не просто другая тематика |
| Unseen tool/server | Success невозможен без discovery, выбора, qualification и корректного invocation |
| Failed-first-route | Nox должен диагностировать tool/contract/evidence failure и сменить план |
| Recovery | Один заданный сбой после checkpoint; результат проверен без duplicate external effects |
| Impossible/forbidden | Правильный конкретный BLOCKED, без имитации результата |
| Adversarial/no-op/decoy | Solver пытается принять ложный результат; independent oracle должен отклонить |
| Fresh-agent transfer | Experience даёт uplift против memory-off на новых задачах |

Один запуск каждого сценария — smoke, не статистическое доказательство. Для empirical claim нужны несколько независимо созданных задач на класс и повторные стохастические прогоны. Десять seed одной задачи не равны десяти независимым задачам.

### 5.3. Обязательные controls

При одинаковых моделях, fixtures и бюджетах сравнивать:

1. полный Nox;
2. single-agent с теми же generic tools;
3. Nox только с capabilities, существовавшими при freeze;
4. no-acquisition;
5. при исследовании обучения — memory off;
6. при оценке resilience/QA — отдельные no-recovery/no-independent-QA ablations.

Если single-agent не хуже, нет доказанного преимущества multi-agent архитектуры. Если полный Nox проходит unseen-tool task, а no-acquisition корректно блокируется, вклад acquisition атрибутирован. Если разработчик исправил prompt после failure, это assisted engineering, а не автономный transfer.

### 5.4. Метрики и допустимый вывод

Первичная метрика: **strict verified success** — все обязательные критерии, внешняя проверка, бюджет, ноль вмешательств и нарушений freeze.

Дополнительно:

- worst-group success, а не только средний результат;
- false ACCEPT и ложные/корректные BLOCKED;
- human interventions и task-specific host modifications;
- acquisition success/utility и fresh holdout transfer uplift;
- repairs, recovery, duplicate effects;
- wall time, tokens, USD/UNKNOWN и cost per verified success с учётом всех failures.

Правильный BLOCKED — успех калибровки, но не решённая задача. Все попытки сохраняются; лучший rerun не заменяет первый результат.

Конечный benchmark не доказывает универсальность для любых цифровых задач, production security, Windows, длинные горизонты, независимость от LLM или экономическую эффективность. Допустимый вывод:

> На конкретном скрытом распределении замороженная система показала измеримый transfer, acquisition, recovery и stopping behavior в заданных бюджетах и полномочиях; границы определены задачами и ablations.

---

## 6. Наиболее эффективный минимальный путь

Не предлагаю больше последовательность «сначала много профессий, потом универсальность». Наиболее короткий обоснованный путь:

1. **P0-min**, чтобы результатам и стоимости можно было доверять.
2. **Заранее зафиксировать generality protocol**, development/holdout separation, budgets и controls.
3. **Одна скрытая compositional task и одна failed-first-route task** на неизменённом общем loop.
4. **Один unseen-tool acquisition** через общий Capability Plane, без core changes, с decoy/no-op и revoke checks.
5. **Один cross-domain artifact** через тот же kernel и contracts; repo/doc выбираются только если подходят к наблюдаемому gap.
6. **Один fresh-agent transfer experiment** против memory-off.
7. Только после этого расширять набор задач, capabilities и модели; multi-agent scale оправдывать paired преимуществом над single-agent.

Это одновременно быстрее и надёжнее, чем два параллельных больших направления «professional packs» и «platform». P0 и design evaluation harness можно готовить параллельно; acquisition зависит от evidence/authority primitives; learning зависит от acquisition и не должно идти первым.

### Прогноз, не факт

Если эта смена курса успешна, Nox получит не гарантированную универсальность, а воспроизводимый механизм расширения: новые задачи будут всё чаще требовать конфигурации/квалификации capabilities, а не изменения orchestrator. Это и есть практический признак движения к цели.

Главный milestone:

> **Замороженный Nox сам строит план для скрытой задачи, при неудаче меняет маршрут, при необходимости осваивает отсутствующую capability в выданных полномочиях и предъявляет независимо проверенный результат — без изменения core source и подсказок разработчика.**

---

## 7. Что действительно нужно согласовать с владельцем

Не требуется заранее утверждать количество профессий, агентов или инструментов. Нужны решения о границах эксперимента и полномочиях:

1. **Definition of done:** согласовать bounded generality вместо недостижимого «доказать всё».
2. **Independent benchmark ownership:** кто создаёт скрытые задачи/oracles и контролирует leakage; разработчики не должны видеть holdout.
3. **Freeze policy:** какие runtime discovery/acquisition разрешены и что считается запрещённой task-specific доработкой.
4. **Budgets:** wall time, tokens/USD или допустимый UNKNOWN, agents/parallelism, acquisition, repairs/no-progress, resources; бюджеты одинаковы для controls.
5. **Acquisition authority:** можно ли автономно скачивать/устанавливать в isolated environment; какие package kinds, sources, licenses, egress и approvals допустимы. Не blanket approval всего каталога.
6. **Executable isolation:** допустимый sandbox/VM уровень, FS/network/process/secrets policy.
7. **External effects:** local fake/draft-only или реальные targets; idempotency/reconciliation; harmless recovery effects отдельно.
8. **Model authority:** host allowlist/caps; может ли Head сам выбирать route/model внутри них; invoice/USD reconciliation.
9. **Memory/evidence:** retention, ACL, redaction, revoke и запрет переноса приватных данных между задачами/tenants.
10. **Human role:** approvals без подсказок решения; вмешательство фиксируется и исключает trial из autonomous success, но не скрывается.
11. **Scope:** Windows, multi-tenancy, production deployment и publication остаются отдельными tracks, а не неявной частью первого generality milestone.

## Итоговый статус

**EXTEND NOX / REVISE PRIORITIES / GENERALITY_BEFORE_WORKFLOW_COUNT / IMPLEMENTATION_NOT_STARTED.**

Прежний P0 сохраняется. Прежний порядок «сначала repo/doc professional slices, потом acquisition по остаточному gap» отзывается как основной путь. Прикладные slices становятся средством проверки общей системы, а не её архитектурным скелетом.
