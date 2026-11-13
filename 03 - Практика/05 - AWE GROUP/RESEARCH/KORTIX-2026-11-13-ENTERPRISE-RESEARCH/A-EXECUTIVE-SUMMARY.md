<a id="section-a"></a>

## A — Практический вывод для Nox

**Не переписывать Nox. Подтвердить финальный R0, затем включать существующие native interfaces и добавлять узкие contract adapters.** Это даёт наиболее обоснованный путь к профессиональным результатам без второго Head, Factory, каталога, Memory или QA. Дата исследования и отсечения: 2026-11-13. RESEARCH ONLY; реализация и испытания не выполнялись.

### Что уже является основанием

DOC-04 сообщает о Mastra core 1.82.0/MCP 2.8.0, Prompt Master, Head, Mission Manager, createSpecialist, recursion, Playwright MCP, tools, TI, memory/libsql и QA. Это **reported-in-docs**, не непосредственная проверка актуального cleanroom. Другая lane статически подтвердила ToolSearchProcessor, SkillSearchProcessor и MCP API на upstream SHA `6e8dfcb83facb0861ebefa4fee384429a113acf4`; это аргумент против нового search engine, но не доказательство конфигурации Nox.

Последний доступный engineering snapshot сообщает 22/22 offline suites и последующий независимый audit IN PROGRESS / NO FINAL GO SEEN с отдельными failures. Final cleanroom SHA, окончательная независимая приёмка и owner GO **UNKNOWN**. Собственная повторная проверка GitHub HEAD получила 403; свежесть после успешных baseline checks не утверждается. Исторический public runtime `d5e9d857dbdeb8f31f9a798b10b5af4af639dbda` не подменяет актуальный runtime. Прямые доказательства/даты/линии — M.

### Какой прирост компетентности предлагается

1. **Правильный инструмент, не больше плагинов:** TI + native search выбирают только разрешённый binding; existing tools/MCP дают receipt, не словесное заявление успеха.
2. **Знания с проверяемыми ссылками:** существующая память получает provenance/ACL/freshness; Docling лишь при неподдержанном формате, Crawl4AI лишь при gap web acquisition. Ни нового RAG стека, ни cloud отправки по умолчанию.
3. **Навык как доказанная процедура:** native SkillSearch загружает versioned SKILL.md; практика, независимая QA, новая задача и transfer evidence определяют proficiency. Чтение документа не освоение.
4. **Условные профессиональные packs:** UX, engineering, marketing, business, data/research используют общие tools/memory/Factory, но разные frozen quality contracts. Первый результат — ограниченный research/data либо sandbox code/UI artifact, без новых external writes.
5. **Прямая пользовательская миссия:** owner request → существующий Prompt Master/Head/Manager → специалист → artifact → independent QA. OpenCode участвует только как инженер до эксплуатации, не как обязательный оператор миссии.

Это **целевой прирост, не измеренный результат**. Нельзя сейчас назвать процент автономности, ROI, срок внедрения или production readiness. Границы полномочий, final acceptance и actual evidence важнее количества источников/инструментов.

### Почему reuse лучше rewrite

D подтверждает native APIs точной версии; EFG — переносимый Skill формат и готовые parsers; C — инженерные контракты, которые должны жить у существующего effect boundary; H — большинство альтернативных frameworks дублируют control plane. Замена framework не исправляет гонку revoke/send, unknown remote outcome, ACL или независимость QA автоматически. Managed connector покупается только ради доказанного OAuth/app-action gap; Composio/Pipedream/Arcade — альтернативы, не обязательный комплект. Temporal, RAGFlow/new memory, новый orchestrator, дополнительный eval/trace SaaS отложены до конкретного gap.

### Приёмка полезности без выдуманных оценок

Все нижеследующие измерения — будущий протокол, **NOT_RUN**. Перед выполнением заморозить набор задач/hidden variants, версии и независимые oracles; одинаковый набор и budget для baseline и candidate, failures/unknown не исключать.

- Completion = independently accepted tasks / все назначенные tasks; отдельно от технического pass.
- Tool selection и argument correctness = correct choices/args по frozen labeled oracle; unauthorized effect count должен быть нулём по raw observer, а не по тексту ошибки.
- Citation precision = подтверждённые cited assertions / проверенные cited assertions; retrieval recall только на размеченном corpus с известными relevant items. ACL leaks считать отдельно, не усреднять с quality.
- Artifact quality: доменный rubric (UI visual/usability/a11y, engineering regression/security, marketing evidence/no fabricated claims, business assumptions/actionability, data reproducibility/uncertainty). Независимый reviewer, не self-score исполнителя.
- Cost/time per accepted result: все затраты/время включая неуспешные attempts делить на accepted outputs; если accepted=0, показатель undefined, не 0. Валюта, units, источник spend, latency distribution и unknown spend отдельно.
- Transfer/reproducibility: новые held-out задачи и повтор на pinned release; report exact sample count/selection, не универсальный benchmark. Без данных эффект не вычисляется.

Минимальные задания K разделяют R0 prerequisites, config-only и code, содержат permissions/tests/artifact/acceptance/rollback/blockers. I задаёт interfaces, schema и state compatibility; L — реальные owner decisions и проверяемые UNKNOWN; M — доказательства. **Дальше нужен не новый market scan и не разрешение от исследователя, а существующий процесс финальной приёмки R0 и затем отдельно допущенная реализация небольших delta.**


