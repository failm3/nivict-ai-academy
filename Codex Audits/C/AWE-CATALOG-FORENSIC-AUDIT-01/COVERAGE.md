# Покрытие и достоверность

**PARTIAL.** Числа относятся к зафиксированному корпусу, не к числу одобренных/работающих инструментов.

| Уровень | Подтверждённый объём |
|---|---:|
| Raw / preserved / processed | 4 504 / 4 504 |
| JSON / CSV / Obsidian IDs | 4 504 / 4 504 / 4 504 |
| Внешняя попытка по ID | 4 504 / 4 504 |
| Внешнее наблюдение (API metadata или HTTP response) | 4169 / 4 504 |
| Различные GitHub project keys проверены | 3 256 / 3 256 |
| Metadata observed / redirects / unresolved | 3 010 / 207 / 39 |
| Архивированные по GitHub metadata | 68 проектов |
| Остальные различные URL, HEAD attempt | 1 209 / 1 209 |
| HEAD 200 / другие HTTP / network-policy unknown | 973 / 149 / 87 |
| Технические desk reviews | 50 решений |
| Exact-project shortlist linkage | 30 решений / 32 исходные строки |
| Архитектурные дополнения shortlist | 20 решений |
| Pinned README/license texts | 98 |
| Additional source/config files read | 2 implementation + 8 manifest/config |
| Independent stratified source screening | 59 / 59 непустых strata |
| Runtime / sandbox / approved / integrated | 0 / 0 / 0 / 0 |
| Другой family / blind examiner | NOT_SATISFIED / NOT_RUN |

HTTP200, metadata/license classifier, root-license text и desk review — разные уровни. GitHub entity lookup не проверяет исходный deep URL path. `externally_verified=0` — reserved independent gate, не отсутствие сетевых запросов. `unresolved=4504` относится к AWE admission/functional/security acceptance. Поля и category/source breakdown: `COVERAGE.json`.

## NIVICT и Manus

| Проверка | Результат |
|---|---:|
| Полный Manus JSON/JSONL export | 3 415, byte-semantic equality / unique IDs |
| DISCOVERED / DOCUMENTED / LIVE_TESTED | 3 403 / 8 / 4 |
| APPROVED / exported approved | 0 / 0 |
| Matched NIVICT rows → Manus records | 3 309 → 3 270 |
| Без stable-ID match: NIVICT rows / Manus records | 1 195 / 145 |
| Exact URL match / project identity match | 1 898 / 1 411 NIVICT rows |

Все 3 309 matched descriptions имеют различающийся текст; семантическая оценка всех пар NOT_DONE. Match не доказывает независимость источников, новая строка не равна новой технологии. Два регистра `GitHubRadar`/`githubradar` в архиве содержат byte-identical post exports. Три library rows `live_stack_resources.jsonl` не являются working12 snapshot.

## Ключевые ограничения

За пределами 32 shortlist-linked исходных строк нет такого же desk-review уровня; отдельные QA source spotchecks сохранены дополнительно. Автоматические categories/capability hints не признаются проверенной функциональностью. Полная проверка лицензий зависимостей, binary provenance, всех semantic contradictions, совместимости, стоимости, безопасности и AWE acceptance отсутствует. Разные модели/слепая проверка и текущая рабочая БД не были доступны в требуемом виде. Продолжение дано в CHECKPOINT/queue.
