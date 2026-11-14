# Nox R2 — независимая проверка поставки

**Итог: FAIL по целостности метаданных поставки.** Основной ZIP, `MANIFEST-SHA256.txt`, вложенный архив, RAW snapshots и реестр 4504 проверки прошли. Блокирующий дефект: `DELIVERY-MANIFEST.json` содержит устаревшие размеры и SHA-256 для двух реальных файлов. Пакет не изменялся, код из пакета не запускался, публикация не выполнялась.

## Дефекты

1. **`DELIVERY-MANIFEST.json` → `NOX-R2-RESEARCH-REPORT.md`: несовпадение.**
   - В манифесте: 7439 bytes, SHA-256 `65eb1e44a8327954a2cae1ebf48e8dc2fd29635dfc4fe88f8ec34dd7de65911c`.
   - Фактически: 7445 bytes, SHA-256 `37cf269dae8a4db034d3c4c189715f43e0f09a55c52997524fd2a7ed6734efc3`.
2. **`DELIVERY-MANIFEST.json` → `solutions-research.zip`: несовпадение.**
   - В манифесте: 22 804 517 bytes, SHA-256 `5745cbfe4c4326f358907a835de3899e5967471320ad79ea0ebb0d38c96b216f`.
   - Фактически: 22 702 266 bytes, SHA-256 `fbd330bdf070f91246e43edaf2273579085cde335ed29f07fbb8a21276ff3348`.
3. **Неблокирующая несогласованность инвентаря:** `raw-provenance/checksums.json` называет себя списком final files, но включает отсутствующие `verify_raw_provenance.py` и `validation.log`. Это не мешает пересчёту, но список не является exact coverage каталога.

`MANIFEST-SHA256.txt` при этом правильный: 82 записи, ровно все payload-файлы кроме самого себя, все хеши совпадают. Устаревший `SHA256SUMS` содержит старые имена/хеши, но заявленный контрольный манифест — именно `MANIFEST-SHA256.txt`.

## Независимо подтверждено

| Проверка | Результат |
|---|---|
| Outer ZIP | 28 279 248 bytes; SHA-256 `3f836b9bed092d819b5db54802ff6cf7f3d187a288c641b9841a1d248b0e2ad3` |
| Outer sidecar | Точный digest и ожидаемое имя файла |
| Outer CRC/readback | 83/83 файлов, ошибок CRC/размера нет |
| Duplicate paths | Нет; вложенной копии `15-OPENCODE-EXECUTION-PACK/15-OPENCODE-EXECUTION-PACK/` нет |
| Общий uncompressed size | 77 878 426 bytes |
| `MANIFEST-SHA256.txt` | 82/82 PASS, exact coverage, исключён только сам манифест |
| `solutions-research.zip` | 246 файлов (+72 directory entries), заявленный SHA-256 совпал; CRC/readback всех entries PASS; duplicate paths нет |
| RAW `iirepresent.json` | 1331 rows, 850 896 bytes, SHA-256 совпал |
| RAW `Радар.json` | 3173 rows, 2 257 187 bytes, SHA-256 совпал |
| RAW `catalog-all-4504.csv` | 4504 data rows + header, 4 048 275 bytes, SHA-256 совпал |
| Реестр | 4504 записей, 4504 unique IDs, split 1331/3173 |
| Порядок и source pointers | 4504/4504 совпали |
| `raw` object exact equality | 4504/4504 совпали |
| `raw_record_json` | 4504/4504 совпали с канонической JSON-сериализацией исходных объектов |
| L1 / UNVETTED / H | 4504/4504 |
| CSV ↔ registry | 4504/4504 по ключевым полям; `www.`-нормализация host учтена независимо |
| CRLF/LF | LF→CRLF побайтно даёт оба исторических SHA-256; обратное преобразование точное |
| 18 семейств | F01–F18 присутствуют; матрица содержит 18 строк |
| Фактические статусы матрицы | F02 BLOCKED; F03/F05/F15/F17 PARTIAL; остальные 13 COMPLETE |
| F06 | Канонический `06-ENTERPRISE-AGENT-COMPARATIVE-RESEARCH.md` присутствует и хеш совпал |
| OpenCode | OC-01…OC-12, все ticket files, `tickets.json` и `OPENCODE-HANDOFF-READYNESS.md` присутствуют |
| PENDING | Незавершённых status-marker не найдено. Есть обычные слова `pending` в прозе/исходниках (например, pending approvals/domain proof), это не статус PENDING |
| Private keys / очевидные tokens | Не найдены. Совпадения `sk-…` в трёх HTML — атрибуты `data-chat-payload-element-id`, не credentials |

## Email

Личные и корпоративные адреса **присутствуют во вложенном `solutions-research.zip`** в публичных upstream README, package metadata, security contacts и notices (например, Gmail-адреса maintainer'ов). Это не выглядит утечкой owner email и не отнесено к блокирующему дефекту, но утверждение «personal email отсутствуют» было бы неверным. Полный per-file список сохранён в JSON.

## Воспроизводимость без helper-файлов

`raw-provenance/verify_raw_provenance.py` и `raw-provenance/validation.log` отсутствуют. **Это не мешает самостоятельной воспроизводимости структурной проверки:** snapshots, их размеры/хеши, CSV, упорядоченный JSONL registry и reconciliation-поля достаточны для нового stdlib verifier. `validation.log` — лишь transcript, а не независимое доказательство. Ограничение: offline-проверка подтверждает equality с приложенными snapshots, но сама по себе не доказывает их identity с конкретными Git commits; для этого нужен независимый fetch/readback pinned Git blobs. Исходные pre-Git bytes и конкретный инструмент CRLF→LF остаются UNKNOWN, однако причина исторического hash mismatch доказана побайтным преобразованием.

## Runtime boundary

Это только структурная/data integrity проверка. **Current Nox: UNKNOWN; T01–T12: NOT_RUN; L3/L4: не проверены; R2: NOT_ACCEPTED.** Ни Nox, ни генераторы, ни скрипты из пакета не выполнялись.

## Артефакты аудита

- `independent_nox_r2_verifier.py` — новый stdlib-only verifier.
- `INDEPENDENT-DELIVERY-VALIDATION.json` — машинные детали и все статусы.

Повтор: `python3 independent_nox_r2_verifier.py audit.zip --sidecar audit.zip.sha256 --output INDEPENDENT-DELIVERY-VALIDATION.json` (exit 1 до исправления двух записей `DELIVERY-MANIFEST.json`).
