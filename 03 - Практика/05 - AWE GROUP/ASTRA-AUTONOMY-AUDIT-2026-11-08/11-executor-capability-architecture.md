# 11 · Реестр исполнителей и выбор способа выполнения

**08.11.2026 · PROPOSED.** Действующие контракты AUTO-01/TR-01 и границы проверены по исходникам e74f. Описанный E1-реестр предстоит связать с настоящими workers. [Общий план](08-e1-unified-plan.md) · [Инвентаризация оригинала](02-inventory.md)

## Какая сущность за что отвечает

| Сущность | Что она возвращает | Какую работу ей выбирать |
|---|---|---|
| LLM-вызов | Версионированный ответ, tool proposal или JSON, usage | Одна ограниченная интерпретация, классификация или генерация. Выполнение предложенного инструмента отдельно допускает broker |
| Главный агент и мастер ТЗ | Spec/plan/replan proposal | Прояснение критерия, выбор специализаций и пересмотр плана. Мастер может быть режимом того же агента с отдельной схемой вывода |
| Специализированный подагент | Артефакт и компактный отчёт с refs | Несколько зависимых решений в ограниченной области, например исправить дефект и прогнать тест. Новый профиль = шаблон роли + model policy + subset capabilities + rubric, без нового daemon |
| Команда | Набор tasks, зависимости и join | Независимые специализации либо объективно независимый QA. Каждый ребёнок получает свой lease, лимит и контекст |
| Бот / обработчик события | Нормализованное событие и cursor | Регулярный poll, webhook, alarm и notification. LLM нужна только для семантического разбора отдельных входов |
| Скрипт | Детерминированные данные/файл, exit, digest | SQL-выборка, dedupe, парсер, build, проверка схемы, smoke. Зафиксировать версию интерпретатора, argv и ресурсы |
| Программа / сервис | Результат вызова интерфейса и receipt | Браузер, конвертер, БД, индексатор, компилятор, HTTP-клиент. Длительно живущий процесс и конкретный вызов имеют разные права |
| Инструмент | Capability с методом и схемой | API, MCP, CLI, SDK, browser или Git — интерфейсы доступа. Сервер MCP сам по себе не удостоверяет надёжность реализации |
| Человек · независимый экзаменатор или владелец | Ограниченная приёмка, бизнес-решение, новый мандат | Права на публикацию, существенная смена цели, итоговая экспертная оценка UX. Обычные решения внутри мандата остаются у системы |
| «PDA-агент» | `NEEDS_DEFINITION` | Поиск PDA/ПДА в доступных исходниках/архитектурных материалах не дал определения, достаточного для исполнения. Не заводить новый тип и не расширять права. Можно добавить alias, когда появится первичный контракт |

## Capability Contract v1

Единица регистрации — **операция конкретной версии**, допускаемая под определённым principal. Имя сервиса используется как metadata. Данные discovery и фактический допуск хранятся отдельно. Пример декларации, без учётных данных:

```json
{
  "capability": "product.preview.verify",
  "version": "1.0.0",
  "executor_kind": "program",
  "implementation_ref": "release:qa-browser",
  "input_schema": "preview.ref.v1",
  "output_schema": "journey.receipt.v1",
  "requires_llm": false,
  "uses": ["browser.chromium"],
  "platform": ["linux", "windows"],
  "placement": "isolated-qa-worker",
  "resources": {"cpu_slots": 1, "ram_mib": 1024, "timeout_s": 120, "max_parallel": 1},
  "permissions": ["preview.read", "test-account.write"],
  "data_classes": ["project-approved"],
  "effect_class": "staging_test",
  "retry": "fresh_test_namespace",
  "reconcile": "read_task_record",
  "quality_suite": "product-primary-journey-v1",
  "cost_basis": "worker_seconds",
  "owner_role": "qa-maintainer"
}
```

Registry envelope дополняет декларацию digest схем/исполняемого кода и зависимостей, лицензией, compatibility range core, подписью reviewer, health TTL, доступными узлами, secret handles, верхней квотой денег/времени, результатами последнего canary и QA по классам задач. Измерения содержат attempts, accepted, стоимость, latency, дату, язык/тип данных, sample size, failure class. Не публиковать пароли или provider keys. `effect_class=external_write` требует функции построения стабильного business key, схемы receipt, reconcile и политики UNKNOWN. Не умеющий сверяться sender исключается из unattended режима.

**Жизненный цикл.** Нормализовать URL и сохранить исходный ID → сопоставить операцию и schema → собрать версии, license, владельца и риски → проверить фактическую установку и hash на worker → прогнать isolated positive/negative/timeout → зарегистрировать подписанный manifest → выдать разрешение конкретной миссии → наблюдать quality и ошибки → revoke/quarantine по истекшему pin/совместимости. После отзыва остановить новые claims и сверить начатые эффекты. Из ранее проверенных 4 504 записей получено 4 466 нормализованных URL. Повторное массовое сканирование не является шагом Pilot. [Данные и граница проверки](05-career-integrations.md)

### Что переиспользовать до написания нового адаптера

| Уже есть в AWE | Оставить и подключить | Чего не обещает исходник |
|---|---|---|
| `awe/tool_registry/importer.mjs, discovery.mjs, runtime-adapter.mjs` | Source IDs, dedupe, индекс возможностей и review pins | Предложение binding не даёт runtime dispatch |
| `AUTO-01/contracts.mjs`, `INTEGRATION-01/adapters/int04-host.mjs` | Spec, DAG, ready nodes, handoff и coordinator family | Mock и последовательный цикл требуют отдельного E1 composition root |
| `awe/executable_tools/host.mjs`, RT-02 process adapters | Scoped files, fixed programs, resource limits | `api.get/browser.snapshot` в этом профиле — fixtures |
| `llm02/broker.mjs`, `llm02/protocol.mjs` | Кодеки/структура single attempt и D09 reserve | Нужен live endpoint с разрешённой сетью, реальной ценой, receipt и recovery |
| `DATA-02/src/memory.mjs`, `awe/qa_profiles/worker.mjs` | Provenance, ссылки, локальная Chromium QA, mutation tests | Отдельно потребуются site/API journeys, визуальный reviewer и mail readback |
| Hermes runtime и OmniRoute на Windows, боты из архитектурных предложений | Проверять готовую установку как кандидата/leaf по тому же registry | Наличие CLI и кода не доказывает текущую доступность подписок, inbox, сети, реальных отправок или recovery |

## Алгоритм выбора

Вход selector: task, критерий успеха, deadline, data labels, mission grant, оставшиеся резервы, здоровые worker slots и версии capabilities. Выход: execution plan с причинами выбора и исключения, worst-case reserve и следующей разрешённой альтернативой.

```text
1. Выбрать зарегистрированные версии, производящие нужную схему и тип результата.
2. Отбросить отозванные, несовместимые и непроверенные для риска операции.
   Применить grant, origin, ACL, регион, secret scope, тип эффекта и наличие readback.
3. Для события по расписанию выбрать trigger/poller; отдельно подобрать обработчик.
   Если задача полностью покрыта программой с проходным экзаменом — запланировать её.
4. Для одного семантического решения сравнить model routes. Для нескольких связанных
   решений рассмотреть bounded leaf с разрешёнными инструментами и лимитом шагов.
5. Разделять на несколько tasks при известных интерфейсах и независимых ветвях
   либо обязательном разделении QA. Включить затраты coordination + join + QA.
6. Для допущенных планов требовать p95 времени <= deadline и worst_reserve <= остатка.
   Ранжировать по полной ожидаемой цене принятого результата при минимальном качестве.
   При близком результате предпочесть меньше процессов, переходов и привилегий.
7. Атомарно зарезервировать строго один выбранный attempt. Не прошёл claim —
   перечитать revision и оценить заново. Нет допустимого варианта — WAIT/BLOCKED,
   предложение новой capability через обычный PR. Право на установку не наследуется.
```

Для нового executor с малым числом наблюдений разрешён только bounded canary на разрешённых данных. Сравнивать build/buy через `стоимость интеграции + эксплуатация за горизонт + ожидаемые переделки + поддержка обновлений`, отдельно фильтровать лицензию, изоляцию и качество. Например, Playwright уже проходит локальные QA: расширить профиль дешевле второго браузерного движка. Писать самому узкий первичный sender оправдано, когда готовый почтовый агент даёт лишнюю операцию reply или не возвращает независимый receipt. Перед заменой повторить одинаковые сценарии и сравнить стоимость и p95.

| Запрос | Выбор из одинакового registry | Фальсифицирующая проверка |
|---|---|---|
| Найти вакансии, откликнуться, наблюдать | API reader + парсер, одинаковые записи объединяет SQL, локальная LLM оценивает соответствие, writer готовит пакет, send broker и monitor-bot обслуживают канал | Два источника одной позиции дают один intent; потеря ACK не создаёт второе сообщение |
| Создать сайт/продукт | Для одного шаблонного экрана достаточно build-скрипта. Для B — UX и инженерные tasks, при независимых API/UI две ветви, независимый браузерный QA | После рестарта продукта сохранённое состояние видно второму клиенту, запрещённый клиент его не видит |
| Исправить ошибку в коде | Локальный reproducer и тест детерминированы, ограниченный coding leaf чинит в отдельной ветке; reviewer сверяет diff и поведение | Исходная версия падает на воспроизведении, исправленная проходит, соседнее поведение сохранено |
| Следить за сервером | Таймер + probe + конечный автомат для подавления повторных уведомлений. LLM только при необходимости обобщить неизвестную причину | На outage, reboot и повторной доставке считаются один инцидент и одно восстановление |

<a id="offline-ab"></a>
## Выполненная проверка двух планов

В e74f на 08.11.2026 выполнен код ниже через `node --require ./baseline/offline-guard.cjs --input-type=module -` со stdin из корня AWE. Это новый вопрос к существующей fixture. Имена `apply` и `deliver` обозначают шаги синтетического плана. Mock создаёт Markdown-артефакты; внешних отправок, работающего сайта и реальной модельной политики здесь нет.

```js
import assert from 'node:assert/strict';
import {fixture} from './AUTO-01/fixture.mjs';
import {createMockModel} from './AUTO-01/mock.mjs';
import {draftFor, node} from './AUTO-01/tests/scenarios.mjs';
const vectors = {
  careerab: [['discover','research',[]],['match','analysis',['discover']],['draft','writing',['match']],['review','qa',['draft']],['apply','writing',['review']],['monitor','analysis',['apply']]],
  productab: [['brief','analysis',[]],['design','writing',['brief']],['build','coding',['design']],['exercise','qa',['build']],['deliver','writing',['exercise']]]
};
for (const [id, steps] of Object.entries(vectors)) {
  const nodes = steps.map(([key, cap, deps]) => node(key, cap, ['r1'], deps));
  const model = createMockModel({draft: c => draftFor([id], c), plan: () => ({nodes})});
  const run = await fixture({sessionId:id, model});
  await run.message('Observe mission ' + id);
  await run.run();
  const state = run.host.snapshot();
  assert.equal(state.phase, 'MOCK_WORK_COMPLETED');
  assert.equal(state.realAutonomyVerified, false);
  assert.equal(state.accepted, false);
  assert.deepEqual(run.executors.calls.map(c=>c.handoff.node_id), steps.map(s=>s[0]));
  console.log(id, steps.length, state.phase, state.realAutonomyVerified, state.accepted);
}
```

Выход: `careerab 6 MOCK_WORK_COMPLETED false false` и `productab 5 MOCK_WORK_COMPLETED false false`. Вывод ограничен общей формой планов и одним механизмом handoff. Для live-проверки дополнительно требуются один runner digest, одинаковые registry/broker/memory/QA contracts, реальные A/B evidence и trace межпроектной изоляции. [Критерий переноса](08-e1-unified-plan.md) · [Модельный selector](09-llm-routing-decision.md) · [Runtime](12-agent-runtime-and-learning.md) · [Сдача Sol](13-delivery-handoff-to-sol.md)
