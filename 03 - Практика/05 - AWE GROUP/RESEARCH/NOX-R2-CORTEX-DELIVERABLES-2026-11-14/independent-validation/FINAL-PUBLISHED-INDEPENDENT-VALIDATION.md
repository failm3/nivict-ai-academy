# Nox R2 — финальный независимый аудит pinned publication

**Итог: FAIL из-за двух несогласованных манифестов и устаревшего status text.** Сам pinned GitHub package теперь полностью соответствует локальному логическому ZIP: **91/91 файлов byte-identical**, включая пять ранее различавшихся metadata-файлов. Все transport files, chunks, originals, RAW и структурные данные проверены заново. Ничего не изменялось и не публиковалось.

Pinned commit: `778cfcda3a3d0631f65e818158b08ffc67c857f7`.

## Блокирующие дефекты

### 1. Логический `MANIFEST-SHA256.txt`: 85 entries, не 90/90

В файле нет пяти reconstructed originals:

- `03-COMPLETE-4504-REGISTRY.jsonl`
- `17-SOURCE-AND-EVIDENCE-LEDGER.jsonl`
- `catalog-4504.csv`
- `raw-provenance/snapshots/catalog-all-4504.csv`
- `solutions-research.zip`

Все **85/85 перечисленных** SHA-256 правильные, но exact coverage 90 файлов отсутствует. Следовательно, заявление manifest 90/90 не подтверждено.

### 2. `PUBLICATION-MANIFEST-SHA256.txt`: 115 entries, exact coverage, но 2 stale hashes

| Файл | Declared SHA-256 | Actual SHA-256 |
|---|---|---|
| `FINAL-DELIVERY-VALIDATION.json` | `c256fe3f26905fc4cb83f1b7095f7486d5d3ced00c2e73799b51e31bfeab8721` | `01d96d6d061a40e49b6cc770a289654ee06189774189282499b85468d6fd5d68` |
| `MANIFEST-SHA256.txt` | `e763349040874fd67400144557c921881140073dc8b10c826c55a44b897f5d6d` | `2c03ba8450f0c083c1d6e8a7f8f90de18b4e746f235340191312fc4716154524` |

Остальные **113/115** publication hashes совпали.

### 3. Устаревший `independent-validation/STATUS.txt`

Он по-прежнему содержит `CURRENT_89_FILE_PACKAGE_WITH_ADDED_REPORT`, хотя проверяемый пакет содержит 91 file. Это документационный дефект; содержимое файла byte-identical в GitHub и локальном ZIP.

## Независимо подтверждённые метрики

### GitHub transport и эквивалентность

| Проверка | Результат |
|---|---|
| Pinned recursive tree | **116 transport blobs**, `truncated=false` |
| Raw downloads | **116/116 PASS**; каждый downloaded size и вычисленный Git blob SHA-1 совпал с API |
| Chunks | **27/27 PASS**: paths, order, sizes, SHA-256 |
| Publication manifest coverage | 115 entries, ни missing, ни extra paths; 113 hash PASS / 2 FAIL |
| Reconstructed originals | **5/5 PASS**, каждый равен assembly manifest и local ZIP |
| Remote logical package | **91 files** |
| GitHub ↔ local logical ZIP | **91/91 byte-identical**, 0 mismatches |
| Пять прежних metadata divergences | Все resolved: README, MANIFEST-SHA256, FINAL-DELIVERY-VALIDATION, STATUS, master tracker |

### Сборка пяти originals

| Original | Chunks | Bytes | SHA-256 |
|---|---:|---:|---|
| `03-COMPLETE-4504-REGISTRY.jsonl` | 11 | 32 113 102 | `707a967b53c3cbdc8f0dbc7813c948c4f54710643554884314a1df6d308a6b71` |
| `17-SOURCE-AND-EVIDENCE-LEDGER.jsonl` | 2 | 4 360 381 | `ffb089d277d2527a28bdc500742cc63cf285d37dfd43f62d26b932de59242acb` |
| `catalog-4504.csv` | 4 | 10 886 997 | `8360a991e0529cedb9cb5fd4fd8db51b10c5841295f64241b720253734bbbf7b` |
| `raw-provenance/snapshots/catalog-all-4504.csv` | **2: 2 500 000 + 1 548 275** | **4 048 275** | `8ad601eb0ff81cf8b8597da7276819c58bd4f156d1c269789fd4907bae9b3fa4` |
| `solutions-research.zip` | 8 | 22 702 266 | `fbd330bdf070f91246e43edaf2273579085cde335ed29f07fbb8a21276ff3348` |

### Локальный ZIP и содержимое

- ZIP size: **28 313 341 bytes**.
- ZIP SHA-256: `813b3e4caa5f2f9c12e788c7859ce76f66d968980221e9ee3aad480cf9e023dc` — PASS.
- Files: **91**; CRC/readback **91/91 PASS**; duplicate paths 0.
- Actual uncompressed total: **77 994 571 bytes** — совпал с заявленным.
- `DELIVERY-MANIFEST.json`: 48 entries, file sizes/hashes PASS; F15 directory byte total PASS.
- RAW: 1331 / 3173 / 4504 rows, hashes PASS; registry 4504 unique IDs и exact source/raw/pointer/L1-UNVETTED-H reconciliation PASS.
- Nested `solutions-research.zip`: 246 files, заявленный SHA-256, CRC/readback PASS.
- F01–F18, canonical F06, matrix 18 rows и OC-01–OC-12/handoff PASS.
- Очевидные private keys/tokens не найдены.

### Все версии независимых аудитов

- `INDEPENDENT-DELIVERY-VALIDATION.*`: присутствует, **FAIL** (два stale metadata).
- `FINAL-INDEPENDENT-DELIVERY-VALIDATION.*`: присутствует, **PASS** предыдущего 87-file ZIP.
- `PUBLISHED-INDEPENDENT-VALIDATION.*`: присутствует, **FAIL** предыдущей публикации, 5 defects.
- `STATUS.txt` и verifier присутствуют, но status text устарел, как указано выше.

Эти отчёты проверены на presence/status; новый результат вычислен из pinned downloads и нового ZIP, а не принят из старых отчётов.

## Ограничения

FAIL относится к заявленным manifest/status guarantees, а не к потере или различию опубликованного содержимого: pinned GitHub и local ZIP совпадают побайтно. Current Nox UNKNOWN, T01–T12 NOT_RUN, L3/L4 не проверены, R2 NOT_ACCEPTED. Runtime/installs/acceptance не выполнялись.

Машинный итог: `FINAL-PUBLISHED-INDEPENDENT-VALIDATION.json`. Детали fresh checks: `FINAL-PUBLISHED-LOCAL-BASE.json`, `FINAL-PUBLISHED-TRANSPORT-VALIDATION.json`.
