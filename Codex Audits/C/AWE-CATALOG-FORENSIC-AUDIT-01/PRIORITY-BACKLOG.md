# Приоритеты после forensic inventory

**PARTIAL; новые исполнения не разрешены этим списком автоматически.** Все acceptance pilots NOT_RUN. Полная очередь на каждую исходную строку — `CONTINUATION-QUEUE.csv`.

## Десять наиболее полезных направлений переиспользования

| Порядок | Готовая основа | Какую самописную работу сокращает | Следующее ограниченное доказательство |
|---|---|---|---|
| 1 | Существующий Mastra Head + structured workflows | Новый общий Head/оркестратор/UI | Получить exact current source/version; sealed mission + cancellation/checkpoint, без замены runtime |
| 2 | Playwright MCP + DevTools | Браузерный движок и сбор screenshots/console/network | Два viewport, DOM/assertions, отдельный профиль, redirect/file/cookie denial |
| 3 | Official GitHub MCP | Самописный универсальный GitHub adapter | Read-only selected repo; write denial; позже leased/idempotent mutation в disposable repo |
| 4 | Один Workspace CLI/MCP adapter | OAuth и Gmail/Calendar/Drive clients | Test account/scopes, two-user isolation, revoke; никаких реальных sends |
| 5 | Official Figma MCP + выбранный image diff | Сложный design RPC и примитивы визуального diff | Draft-only operation, token/text/layout fidelity + independent visual QA |
| 6 | Manus discovery/provenance + ToolHive/FastMCP primitives | Новый общий каталог, MCP plumbing и container launch code | Read-only discovery; forged status/attestation cannot cross admission gate; TR-01 remains separate |
| 7 | Existing relational memory + pgvector | Новый vector database/индекс | Disposable target PG/schema, auth before retrieval, poison/correction/delete/restore |
| 8 | Langfuse/OTel | Общий сбор traces и prompt/model/tool telemetry | Canary redaction, retention/ACL, missing-event detector; не QA examiner |
| 9 | Promptfoo + reviewed Cloudflare methodology | Generic eval harness и coverage ledger | Seeded negative cases, sealed critical checks; framework code не загружать автоматически |
| 10 | Agent Zero/Hermes execution primitives | Собственный terminal/skill/subagent executor | Одинаковая bounded recursive/resume mission с Mastra baseline; выбор по измерениям |

Это приоритет по архитектурной полезности и дублированию разработки, не рейтинг доказанной безопасности или ROI. Реальные latency, стоимость, Windows/WSL compatibility и operator effort не измерялись.

## Продолжение исследования

1. Независимый examiner другого семейства моделей: методика, corrected/unknown classifications, 59 strata и все high-risk primary findings. Не передавать ему conclusions до blind verdict, затем отдельная сверка разногласий.
2. Разрешить 207 repository redirects по immutable GitHub repository ID/owner transfer; 39 unresolved и 87 web network/policy cases сохранить UNKNOWN до фактов. Проверить GitHub subpaths, login/parking и HTTP200 content identity; HEAD этого не решает.
3. По очереди исходных IDs читать primary docs/license/requirements; фиксировать field-level source/status. Только 32 исходные строки связаны с shortlist desk reviews, остальные не имеют такого уровня проверки. Дополнительные QA spotchecks не превращают остальной корпус в inspected code.
4. Проверить семантические разногласия NIVICT/Manus по matched IDs; все 3 309 matched descriptions текстуально различаются, но это не 3 309 доказанных противоречий. Не объявлять 145 unmatched Manus rows новыми уникальными инструментами.
5. Получить отдельный read-only source/working-registry snapshot у владельца AWE, не обращаться к активному OpenCode/runtime ради догадок. Сопоставить exact12 IDs с canonical3415; не выполнять restore поверх действующей БД.
6. После отдельного разрешения на установку/чужой код и фиксированного лимита платных вызовов провести один пилот. Проверить им критерии матрицы и native integration, затем обсуждать второй компонент. Здесь не выполнены installers, source tests, paid APIs или изменения infra.

Приостановленные альтернативы: дополнительный общий orchestrator, отдельный graph memory store, второй workflow engine, личный logged-in Chrome bridge, Continue с прекращённой активной поддержкой. Возвращаться к ним по измеренному пробелу, не из-за популярности.
