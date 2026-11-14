# Nox R2 — финальная независимая проверка публикации

**Итог: FAIL публикации GitHub. Локальный 89-file ZIP: PASS по структурной/data-integrity проверке.** Это новый аудит commit `28c697c23cf53edca929bd7b9ad3ff489880fd2c` и нового ZIP, а не повторное использование предыдущего PASS. Использовались read-only GitHub API/raw downloads и новые stdlib-проверки; репозиторий и пакет не изменялись.

## Дефекты публикации

1. **На pinned commit 112 transport files, не 113.** Recursive Git tree не truncated. Все 112 доступных файлов скачаны по raw URL; размеры и вычисленные Git blob SHA-1 совпали с API. Chunks действительно 25.
2. **Отсутствует `raw-provenance/snapshots/catalog-all-4504.csv`.** Он есть в локальном ZIP и указан в опубликованном `PUBLICATION-MANIFEST-SHA256.txt`, но отсутствует в Git tree на указанном commit. Поэтому publication manifest не имеет exact coverage: 112 entries, 1 extra/missing remote file.
3. **Опубликованный логический пакет после сборки содержит 88 files, не 89:** 112 transport − 25 chunks − 3 transport-only (`PUBLICATION-MANIFEST-SHA256.txt`, `chunks/ASSEMBLY-MANIFEST.json`, `chunks/assemble_verify.py`) + 4 reconstructed originals = 88.
4. **GitHub и локальный ZIP не byte-equivalent для пяти файлов:**
   - `README.md`: GitHub 5628 bytes / `ff394378…e92a`; local 5174 / `864083c7…61f6`.
   - `MANIFEST-SHA256.txt`: GitHub 8596 bytes / `354bbd1a…d75a`; local 8596 / `4189dd11…d75a`.
   - `FINAL-DELIVERY-VALIDATION.json`: GitHub 10074 / `3a53509f…2695`; local 10060 / `8c2689a8…8cae`.
   - `independent-validation/STATUS.txt`: GitHub 359 / `f0e93f3f…0398`; local 309 / `7f885f23…e53`.
   - `R2-RESEARCH-MASTER-TRACKER.md`: GitHub 9145 / `b5131e49…f9`; local 9100 / `44bb117e…967`.
5. **Неблокирующая отдельная ошибка локального summary:** `FINAL-DELIVERY-VALIDATION.json` заявляет `total_uncompressed_bytes=77954631`; фактическая сумма размеров 89 файлов локального ZIP — **77 954 897 bytes** (разница 266). Это не влияет на независимо подтверждённые CRC/hashes, но метрика summary неверна.

## Что независимо прошло

### GitHub transport и chunks

- Pinned recursive tree: **112 blobs**, 25 chunks, `truncated=false`.
- Raw readback: **112/112**; API size и Git blob identity совпали для каждого скачанного файла.
- `PUBLICATION-MANIFEST-SHA256.txt`: все 111 соответствующих remote files hash PASS; один заявленный snapshot отсутствует.
- Chunk manifest: все **25/25** chunk size/hash и последовательность PASS; каждый chunk < 4 MiB.
- Сборка четырёх originals собственной конкатенацией, без запуска приложенного assembler:

| Original | Chunks | Bytes | SHA-256 | Результат |
|---|---:|---:|---|---|
| `03-COMPLETE-4504-REGISTRY.jsonl` | 11 | 32 113 102 | `707a967b53c3cbdc8f0dbc7813c948c4f54710643554884314a1df6d308a6b71` | PASS, равен local ZIP |
| `17-SOURCE-AND-EVIDENCE-LEDGER.jsonl` | 2 | 4 360 381 | `ffb089d277d2527a28bdc500742cc63cf285d37dfd43f62d26b932de59242acb` | PASS, равен local ZIP |
| `catalog-4504.csv` | 4 | 10 886 997 | `8360a991e0529cedb9cb5fd4fd8db51b10c5841295f64241b720253734bbbf7b` | PASS, равен local ZIP |
| `solutions-research.zip` | 8 | 22 702 266 | `fbd330bdf070f91246e43edaf2273579085cde335ed29f07fbb8a21276ff3348` | PASS, равен local ZIP |

Final independent reports и verifier в GitHub присутствуют; их наличие не использовалось как доказательство нового результата.

### Локальный финальный ZIP

- Размер **28 303 788 bytes**; SHA-256 `2f757e00271258e4cebeb07e3098d7588efd131c2a6f3ee1ef221e069773f6f1` — PASS.
- **89 files**, CRC/readback **89/89 PASS**, duplicate paths 0, неправильной nested OpenCode-копии нет.
- Фактический uncompressed total **77 954 897 bytes**.
- `MANIFEST-SHA256.txt`: **88/88 PASS**, exact coverage, исключён только сам манифест.
- `DELIVERY-MANIFEST.json`: 48 entries, размеры/хеши PASS; F15 virtual directory byte total PASS.
- RAW snapshots: 1331 / 3173 / 4504, byte hashes PASS; registry 4504 unique IDs, exact raw/source/pointer/L1-UNVETTED-H reconciliation PASS.
- Canonical F06, F01–F18, матрица 18 rows, OC-01–OC-12 и handoff PASS.
- Nested ZIP: 246 files, hash `fbd330bd…3348`, CRC/readback PASS.
- Включённые первый FAIL и предыдущий final PASS reports присутствуют.
- Очевидные private keys/tokens не найдены.

## Точные ограничения

PASS локального ZIP не отменяет FAIL опубликованной копии: GitHub commit не содержит полный эквивалент локального 89-file пакета. Текущий Nox UNKNOWN, T01–T12 NOT_RUN, L3/L4 не проверены, R2 NOT_ACCEPTED. Runtime, installs и acceptance не выполнялись. Ничего не исправлено и не опубликовано.

Машинный результат: `PUBLISHED-INDEPENDENT-VALIDATION.json`. Детальные fresh проверки: `PUBLISHED-LOCAL-BASE.json`, `PUBLISHED-TRANSPORT-VALIDATION.json`; verifier публикации: `independent_publication_verifier.py`.
