# Полный аудит исходных 4504 записей

**Статус:** `STRUCTURAL_INVENTORY_COMPLETE / ALL_ROWS_L1_H / L2_L3_L4_NOT_COMPLETE`. Это не реестр 4504 установленных или испытанных инструментов.

## 1. Кардинальность и происхождение

- `iirepresent.json`: **1331**, SHA-256 `01dc8a9f15f769f0c240fe7d64442ea279ef6461675f9f4204eb47571701ddc5`.
- `Радар.json`: **3173**, SHA-256 `2f5c6806030dba7ac7b3e8e3c1cf9510054e88ac7085d46b08a941ecf9dc4221`.
- `catalog-all-4504.csv`: **4504** data records, 16 columns, SHA-256 `8ad601eb0ff81cf8b8597da7276819c58bd4f156d1c269789fd4907bae9b3fa4`; это derived crosswalk, не дополнительные записи.
- Канонический реестр: `03-COMPLETE-4504-REGISTRY.jsonl`, одна запись на исходную строку, stable ID, JSON pointer, все raw fields, aliases/groups, verdict, evidence и NEXT_TEST. Плоский экспорт: `catalog-4504.csv`.
- Независимая структурная проверка upstream: `inventory-validation-report.json` = PASS; 4504/4504 raw JSON round-trip, 4504 unique IDs, CSV URL+description+raw JSON round-trip, missing cards=0, dangling historical issue IDs=0. Эти факты не являются URL/executable/security/QA tests.

## 2. Сохранение duplicates и исключений

Все строки сохранены: exact unique 4466, exact extra 38; normalized-address unique 4424, address extra 80. Это **кандидатные связи**, не semantic merge: fork/upstream, service/self-hosted и SDK/service не объединяются без отдельного evidence. Historical `issues.csv` = 4090 rows, `duplicates.csv` = 71; все IDs разрешены.

`SOURCE_HASH_MISMATCH`: старые validation hashes не равны текущим RAW. Причина UNKNOWN до получения исходного archive/bytes; hash текущего RAW не подменяется старым. Archive `NIVICT-Obsidian-Tools-2026-11-04.zip` не проверен; его hash из manifest не принят.

## 3. Распределение — только deterministic heuristic

| semantic class | records |
|---|---:|
| library | 1713 |
| service | 1110 |
| app | 794 |
| API | 168 |
| workflow | 136 |
| Skill | 118 |
| MCP | 104 |
| CLI | 102 |
| catalogue | 94 |
| documentation | 88 |
| article | 46 |
| SDK | 29 |
| other/unknown | 2 |


Контурные метки (многозначные): {"B_KNOWLEDGE_COMPETENCE": 2734, "A_TOOL_CAPABILITY": 1792, "C_EXECUTION_STRATEGY": 393, "D_META_INTELLIGENCE": 441}. Все 4504 `UNVETTED/H/L1`; low-confidence semantic labels не upstream facts.

## 4. Execution coverage и оставшийся UNKNOWN

L1 structural coverage = 4504/4504; L3=0; L4=0. Для каждой записи installed/authorized/called/QA/released/license/version/cost = UNKNOWN, если не доказано отдельно. Полный L2 по каждой из 4504 не выполнен; никакой shortlist не заменяет это. Дальнейшая работа: риск/usefulness-prioritized L2, затем отдельно owner-approved L3; не требуется исполнять все 4504.

Источники и ограничения: `source-baseline.md` §3–7, `inventory-README.md`, `inventory-validation-report.json`, `03-COMPLETE-4504-REGISTRY.jsonl`.
