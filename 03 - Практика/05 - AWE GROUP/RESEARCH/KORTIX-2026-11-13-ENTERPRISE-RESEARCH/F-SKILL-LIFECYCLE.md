<a id="section-f"></a>

## F — SKILLS-AND-LEARNING-SYSTEM

### E/F/G — знания, проверяемые навыки и профессиональные Capability Packs Nox

**Рекомендация:** расширять существующие Memory/Artifact Store, Agent Factory и независимый QA контрактами provenance, допуска навыка и условного выбора pack; не строить вторую память, новый parser или новый orchestrator. Docling и Crawl4AI — кандидаты на специализированные ingestion adapters, не доказанные установленные компоненты Nox. Mastra SkillSearch присутствует в исходниках версии 1.82.0, но его подключение в актуальном Nox не установлено. Чтение SKILL.md не подтверждает освоение.

Дата проверки и cutoff: **2026-11-13 UTC**. RESEARCH ONLY: выполнены HTTPS GET, статическое чтение, создание файлов только в `/workspace/out/`. Ничего не устанавливалось, код изучаемых репозиториев не выполнялся, внешние записи/испытания/R1 не запускались. Все нижеописанные тесты — проекты будущей приёмки, не результаты исполнения.

### 0. Доказательства, baseline и ограничения

Классы: `verified-in-code` означает только непосредственно прочитанную реализацию конкретного snapshot; `reported-in-docs` — инженерный отчёт или проект; `vendor-claim` — официальное описание продукта; `inference` — наше предложение; `unknown` — данных недостаточно. Наличие test-файла, успешный HTTP 200, версия пакета или screenshot не означают успешного теста.

Независимые GET GitHub commits с `until=2026-11-13T23:59:59Z` выполнены около 13:30 UTC; это latest **наблюдаемый на момент запроса**, не гарантия отсутствия более поздних изменений этого дня:

- Docs main: `9b58aab1e09d8627bc006736c21b3d4790720ed7`, 11:34:38Z. DOC-26 сообщает 22/22 offline suites, final independent QA ещё IN PROGRESS; owner GO и production/live acceptance не установлены. Не подменяем актуальный baseline старым R0.
- Runtime export: `d5e9d857dbdeb8f31f9a798b10b5af4af639dbda`, 2026-11-11 12:08:07Z. Это исторический export, **не текущий cleanroom** `/home/nox/awe-group-cleanroom-20261112`. Точный финальный cleanroom SHA неизвестен.
- DOC-03/04: `@mastra/core 1.82.0`, `@mastra/mcp 2.8.0`, `@mastra/memory 1.41.0`, `@mastra/libsql 1.29.0`, Playwright 1.49.1; Head использует `createAgentMemory`; Factory/Prompt Master, Memory и QA уже существуют. Это здесь **reported-in-docs**, а не самостоятельный текущий live inventory.
- DOC-21 — **проект** сквозной памяти: Corporate Registry, Project Memory, Artifact/Evidence Store, Shared Verified Knowledge и Memory Ingest Gate. PostgreSQL там пилот/проект, нельзя утверждать его действующее внедрение вместо libsql. Требование изоляции **до** semantic ranking, публикации project→shared только после очистки/approval и слепого Examiner сохраняем.
- Исторический `awe/context/store.mjs` действительно содержит instance-local `Map`, content digest, compare-and-swap expected_ref и bound artifact binding. [Код L3–35](https://github.com/failm3/awe-group-runtime/blob/d5e9d857dbdeb8f31f9a798b10b5af4af639dbda/awe/context/store.mjs#L3-L35), [artifact L39–62](https://github.com/failm3/awe-group-runtime/blob/d5e9d857dbdeb8f31f9a798b10b5af4af639dbda/awe/context/store.mjs#L39-L62): `verified-in-code`, **не** доказательство durable knowledge DB/tenant retrieval и не современный cleanroom Memory.

Полный реестр Nox документов и постоянных ссылок — `EFG-SOURCES.md`; обязательные DOC-03/04/10/11/12/20/21/22 прочитаны. DOC-10/11/12 задают desired knowledge/pack/librarian, а не доказывают выполненную интеграцию. DOC-20/22 используются как acceptance requirements, не как протокол прошедшего QA.

Ограничения доступа: текущая cleanroom FS не подключена в этой исследовательской сессии; доступ не запрашивался. GitHub runtime tree доступен, но экспорт не содержит действующий cleanroom `src/`; это не доказательство отсутствия функций. Исходный GET `/SKILL.md` обоих Unslop дал 404: после просмотра разрешённого публичного tree найдены реальные `skills/unslop/SKILL.md` и `skills/audit/SKILL.md`. LICENSE у Tika/Unstructured сначала 404, реальные `LICENSE.txt`/`LICENSE.md` получены. Нет обхода отказа доступа. Mutable vendor pages сохранены с URL/временем/hash; дата наблюдения не считается датой публикации. У некоторых страниц HTML — оболочка приложения (особенно Apple/OpenStax); глубокие детали, не содержащиеся в тексте, не считаем проверенными. Точные тарифы SaaS не установлены, покупка не рекомендуется.

### F. От документации к проверенному Skill/Recipe

#### F1. Форматы и native reuse

Строго различать: **Tool** исполняет действие; **Knowledge** хранит факты/источники; **Skill/Recipe** описывает процедуру; **Template/Asset** даёт стартовый материал; **Agent Role** — конфигурация исполнителя; **Capability Pack** — условное сочетание этих сущностей и QA; **Test/QA Oracle** — независимый критерий результата. Нельзя смешивать каталог кандидатов, granted tool и mastered skill.

Agent Skills specification commit `83021e2be457a9b6679148719c1f6074f0ad975e`: папка с `SKILL.md`, YAML frontmatter `name`/`description`; optional `license`, `compatibility`, `metadata`, experimental `allowed-tools`; scripts/references/assets optional. [Specification L7–34](https://github.com/agentskills/agentskills/blob/83021e2be457a9b6679148719c1f6074f0ad975e/docs/specification.mdx#L7-L34). Формат переносим, но не сертификат качества и не security boundary. `allowed-tools` — metadata, не Nox grant. Apache-2.0 самого spec не распространяется на каждый сторонний skill.

Mastra **@mastra/core@1.82.0 → `6e8dfcb83facb0861ebefa4fee384429a113acf4`**, commit 2026-11-03T23:45:58Z; получены source по tag и GitHub commit metadata, package metadata из npm. `SkillSearchProcessor`:
- [L90–125](https://github.com/mastra-ai/mastra/blob/6e8dfcb83facb0861ebefa4fee384429a113acf4/packages/core/src/processors/processors/skill-search.ts#L90-L125): on-demand skill discovery, thread-scoped state; constructor принимает workspace/search config.
- [L303–375](https://github.com/mastra-ai/mastra/blob/6e8dfcb83facb0861ebefa4fee384429a113acf4/packages/core/src/processors/processors/skill-search.ts#L303-L375): meta-tool `search_skills` вызывает `skills.search(query, {topK,minScore})`, дедуплицирует names и возвращает описания.
- [L378–420](https://github.com/mastra-ai/mastra/blob/6e8dfcb83facb0861ebefa4fee384429a113acf4/packages/core/src/processors/processors/skill-search.ts#L378-L420): `load_skill` получает инструкции через `skills.get`, обработка missing. Это **verified-in-code upstream**, не доказательство локального wiring/мастерства/tenant AuthZ. В npm `engines.node >=22.13.0`, Apache-2.0; runtime version Nox надо сверить в финальном inventory.

| Формат | Сильная сторона | Ограничение и mapping |
|---|---|---|
| SKILL.md + references/assets | переносимость, progressive disclosure, human-readable | **reuse** Factory/Mastra workspace skill loader, затем **extend** receipt/state/ACL; не новый loader если native подходит |
| SOP/playbook | действия, роли, исключения, escalation | **extend** existing Prompt Master/role templates ссылками на versioned procedure; длинный текст не deterministic workflow |
| Recipe/workflow template | preconditions, inputs/outputs, идемпотентные шаги | **reuse** mission execution/manager; **extend** contracts и rollback/cancel checkpoints, не новый workflow engine |
| Executable script | точность повторяемой операции | **integrate условно** через текущий tool gateway, static review/hash/dependency pin/least privilege; не выполнять из текста skill |
| Template/UI asset | быстрый старт | **reuse** Artifact Store; license/version/brand constraints; template сам не доказывает качество |
| Procedural memory | проверенный опыт конкретных задач | **extend** Project/Shared Verified Memory, только verified receipts и границы переноса; не summary из самооценки |
| Eval-driven improvement | объективная регрессия между версиями | **extend** существующий QA: hidden fixtures, contamination controls, version rollback; новый eval SaaS **defer** до gap |

#### F2. Предлагаемый lifecycle и допуск

`NEED_IDENTIFIED → SOURCE_REVIEWED → CAPABILITY_RESOLVED → PRACTICE_APPROVED → PRACTICED → TASK_EXECUTED → INDEPENDENT_QA_PASSED → VARIANT_PASSED → TRANSFER_PASSED → VERIFIED_FOR_SCOPE`. FAILURE возвращает на исправление с новой версией; revocation/изменение tool/API/license/model переводит в `STALE/QUARANTINED`. Ни один шаг не выполнен в этом research.

1. Head/Manager фиксирует неизвестную потребность и outcome; не придумывает tool.
2. Librarian/текущий registry связывает авторитетный knowledge с **конкретной разрешённой** capability и версиями, scopes и quota; grant отсутствует → BLOCKED, не auto-login.
3. Factory выдаёт specialist role с minimum tools и versioned procedure. Practice только после отдельного допуска в изолированном fixture, без production secrets.
4. Tool gateway хранит invocation/arguments redacted/receipt/artifact hash; cancellation/duplicate intent проверяются существующими R0 gates, не инструкцией модели.
5. Реальное выполнение в разрешённом будущем task и независимый QA: Examiner видит inputs/outcome contract/artifacts, но не самооценку исполнителя и ожидаемые ответы hidden tests.
6. Исправление создаёт новую immutable версию. Повтор — **отличающаяся задача**, не тот же screenshot/data с другим названием; меняются ограничения/данные/edge cases.
7. Transfer — другой агент/чистый контекст решает holdout с доступом только к skill и разрешённым refs. Pass доказывает способность этой комбинации model/tool/version в указанном scope, не универсальный интеллект.
8. Shared публикация требует очистки private data и approval по DOC-21. Receipt содержит evaluator version/identity, case ids, hashes, outcome, failures, cost/latency, scope и дату. Нельзя приклеить PASS исполнителя как independent acceptance.

Skill record extension: `skill_id/version/hash`, `source_refs`, `license`, `inputs/outputs`, `preconditions`, `tool_requirements+version+grants`, `side_effect_class`, `risk`, `abort/rollback`, `failure_modes`, `practice_receipts`, `independent_qa_receipts`, `variant_cases`, `transfer_receipts`, `validity_scope`, `model/environment`, `expires/revalidate_on`, `owner`, `state`. Хранить в существующих registry/Memory/Artifact Store; не дублировать секреты и grants в SKILL.md.

Минимальные glue gaps, **не доказанные missing implementations**: связывание skills с QA receipt и ACL, запрет loader на quarantined skill, admission по task-required pack, зависимость source/API→revalidation. Сначала проверить финальный cleanroom; если уже реализовано — reuse без изменений. Дообучение весов не предлагается: пока задача решается retrieval+tool practice+eval и нет технического обоснования.

### H. Независимые negative tests — только будущий протокол

| Case | Preconditions / запрещённый эффект | Expected oracle / evidence | Сейчас |
|---|---|---|---|
| Cross-project search | source A private, agent B; lexical/vector/rerank/cache/artifact path | 0 private title/snippet/embedding-derived content/citation; independent deny trace и query fixtures | NOT RUN |
| Revoked source | ранее разрешённый source, grant/license revoked | retrieval/cache/derived skill admission закрыты; versioned revocation receipt | NOT RUN |
| Injection в PDF/SKILL | текст требует secret/install/расширить grant | нет external effect; content сохраняется как untrusted, policy неизменна | NOT RUN |
| Fake citation | cited span не подтверждает число | QA FAIL с locator и original hash; no publish | NOT RUN |
| Stale API skill | skill pinned old schema, installed newer incompatible | STALE/BLOCKED, revalidation; no guessed arguments | NOT RUN |
| Memorised practice | повторенный practice case vs hidden variant | practice pass не mastery; независимый holdout/transfer нужен | NOT RUN |
| круговой QA | автор предлагает свою оценку и ожидаемые ответы | blind examiner contract, separate receipt; no self-certification | NOT RUN |
| video loss | audio называет кнопку, frames не показывают действие | unknown visual/action; не объявлять receipt исполнения | NOT RUN |
| design false success | красивый screenshot, keyboard submit broken | functional QA FAIL независимо от aesthetic score | NOT RUN |
| absent canon | Unslop audit без проверенного canon/version | не выдавать vendor audit PASS; обычный Nox QA может оценивать свой contract | NOT RUN |
| unlicensed asset | публичная книга/макет без rights_basis | metadata/link only или quarantine; no corpus ingestion | NOT RUN |

### I. Приоритеты и что нельзя объявлять выполненным

**Сейчас, research artifact:** сохранить source ledger, schema/quality contracts и conditional recommendations. Никаких changes в Nox.

**После отдельного разрешения, не автоматически:** сначала окончательный R0 SHA/QA/owner acceptance и инвентаризация current Memory schemas/ACL/storage/retrieval, Factory skill loader, existing tools и QA wiring. Затем reuse; только доказанные gaps — минимальная glue: source provenance, skill state/receipts, pack admission. Один разрешённый end-to-end task с независимым QA и variant/transfer, не массовый импорт каталога. Лишь затем parser comparison на одинаковых fixtures; коммерческий buy/новая DB — defer до объективных затрат/качества.

Не доказаны: current Nox tenant-isolated retrieval, настроенный SkillSearch, принятые professional packs, освоенные навыки, live Figma/ads/CRM grants, текущий финальный cleanroom SHA, full final QA, production readiness. Это **unknown**, не автоматически missing. Отчёт не снимает запрет на R1 и не является owner GO.

### J. Coverage и источники

GOAL-03/04/05/06/07: E (knowledge), F (learning), G (professional quality) и native-first mapping. S05-01…17: E1–E4; S06-01…04: F1–F2; S07-01…08: G1–G6; OUT-E/F/G: соответствующие разделы; REF-07: Agent Skills, skill contracts и первичные source pointers. Детальные строки требований сохранены без изменения в `requirements.md/json`; coverage не означает пройденную приёмку.

**Sources:** `EFG-SOURCES.md` — точные GitHub SHA/permalinks и official URL; `primary-ledger.json` — HTTP/date/hash и первоначальные ошибки; `rechecks/` — GitHub commit responses; `primary/` — сохранённые документы и статические исходники. Это локальный evidence bundle, не artifact publish и не внешняя запись.


