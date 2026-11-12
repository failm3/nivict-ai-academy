# Воспроизведение и продолжение

Требуются существующие Python 3.10+ и Git. Здесь использовался Windows Python 3.13.2, standard library only. Скрипты не устанавливают зависимости и не импортируют/выполняют исследуемый код.

## Зафиксированные inputs

Academy: `5c611773bff3ccba76b78337534ed8944e137236`, с исходными 04/03 каталогами. Создать отдельную копию с `core.autocrlf=false`; не выполнять checkout/reset в действующем AWE worktree. Сверить Git blob/SHA-256 с EVIDENCE/SOURCE-MANIFEST.json. ZIP Manus передать как отдельный input; ожидаемый SHA-256 `5855ce5cfdb0abda44954108bfe2cfa1bec97dbf7c51db7be822eb04541d5ec1`. Он не включён в публичный PR.

## Offline replay сохранённых observations

Из каталога audit artifacts, заменив пути своими:

```text
python -X utf8 scripts/reproduce.py --audit AUDIT_DIR --repo PINNED_ACADEMY_COPY --archive MANUS_ZIP --target NEW_REPLAY_DIR
```

Target должен быть новым/пустым. Скрипт копирует captured EVIDENCE/QA и TECHNICAL-REVIEWS, затем заново читает исходные 4 504 records, notes/categories/canvas, Manus ZIP, сверяет corpus/overlap и строит enriched registry. Сравнивает байты INVENTORY-ALL, COVERAGE, DEDUP-RECONCILIATION, DUPLICATE-GROUPS и CONTINUATION-QUEUE с captured результатом. Captured metadata/HEAD observations сохраняют старую дату; offline replay не выдаётся за новый online или independent model test. В scratch читается allowlist Manus data/source, ничего не исполняется и БД не восстанавливается.

Основные шаги можно выполнить отдельно:

```text
python -X utf8 scripts/inventory.py --repo PINNED_ACADEMY_COPY --out NEW_OUTPUT_DIR
python -X utf8 scripts/reconcile_manus.py --archive MANUS_ZIP --out NEW_OUTPUT_DIR --work SCRATCH_MANUS
python -X utf8 scripts/context_evidence.py --repo PINNED_ACADEMY_COPY --out NEW_OUTPUT_DIR
python -X utf8 scripts/enrich.py --out NEW_OUTPUT_DIR
python -X utf8 scripts/validate_delivery.py --repo PINNED_ACADEMY_COPY --out NEW_OUTPUT_DIR
```

`enrich` требует captured EVIDENCE, QA и TECHNICAL-REVIEWS. Не перезаписывать final outputs первым inventory.py: он намеренно создаёт исходную NOT_CHECKED стадию, которую потом обогащает evidence join.

Optional earlier cleaned-index/shortlist reconciliation: `python -X utf8 scripts/prior_research.py --repo PINNED_ACADEMY_COPY --out NEW_OUTPUT_DIR`. Она проверяет все occurrences/alternate URLs и 23 mappings, а не runtime claims.

## Повторное чтение primary texts

```text
python -X utf8 scripts/collect_primary.py --audit AUDIT_DIR --cache NEW_PRIMARY_CACHE
```

Только 98 pinned raw README/license URL, с SHA-256/Git blob equality, ограничением размера и retry/backoff. Файлы хранятся как данные, никогда не исполняются. Полные source caches остаются вне public PR. `build_reviews.py` воспроизводит authored desk-review rendering из проверенного cache; ожидает соседний captured CODE-INSPECTION.json для индекса дополнительных source files. Сам текст инженерных выводов и independent QA — authored evidence, не имитация генерации моделью при replay.

## Online continuation

`EVIDENCE/ONLINE-QUEUE.json` содержит все 3 256 GitHub keys; `ONLINE-BATCH-*.json` — непрерывные сохранённые диапазоны, `ONLINE-RETRIES.json` — успешный повтор единственного transport failure. Connector lookup: GET `https://api.github.com/repos/OWNER/REPO`. Не продолжать endless retries для 404/access blocks, не обходить запреты; 207 redirects требуют отдельного owner/repository-ID review. Сохранить новые ответы отдельным checkpoint, не переписывая историю.

```text
python -X utf8 scripts/check_urls.py --out AUDIT_DIR --workers 12
```

HEAD collector использует cache и не повторяет уже сохранённые URL. Для нового dated pass использовать отдельный каталог/evidence file; не удалять старый snapshot. Cookies/auth/payment APIs/JS execution отсутствуют. Получение body/лицензии — отдельный этап, не подменять его HEAD200.

Полный следующий список — CONTINUATION-QUEUE.csv. Первыми нужны другой-family blind QA, source identity для redirects/unresolved, primary docs/license/classification для всех remaining records, semantic reconciliation и отдельный current12 snapshot. Пилоты чужого кода/установок и paid calls требуют отдельного разрешения с cost ceiling; текущие scripts их не выполняют.

## Контрольные суммы и публикация

SHA256SUMS покрывает публичный набор artifacts, исключая сам файл, archive и post-publication receipts. После финального staging повторить `python -X utf8 QA/publication_scan.py`; scan не выводит найденные значения и не является полной PII/security гарантией. Полный исходный Manus index/backup/provenance не публикуется, публичный MANUS-PUBLIC-INDEX хранит только product metadata/URLs/stages/identity hashes. GitHub checkpoint валиден только после remote commit/tree/content readback; receipt сохраняется отдельно.
