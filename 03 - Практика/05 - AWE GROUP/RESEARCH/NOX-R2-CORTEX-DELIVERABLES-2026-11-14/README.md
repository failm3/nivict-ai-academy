# Nox R2 Cortex — research deliverables (2026-11-14)

**Статус:** `research/design snapshot` / **R2_NOT_ACCEPTED**. Публикация содержит исследование, проекты протоколов и evidence, а не принятый R2, production release или реализацию Nox.

## Обязательные ограничения

- **Current Nox: UNKNOWN.** Свежий source/HEAD/wiring/runtime не проверен.
- **G0–G5 и T01–T12: NOT_RUN.** Независимые **L3/L4 отсутствуют**.
- Реестр **4504/4504** структурно полон (L1/H), но **per-row L2+ incomplete**.
- `SOURCE_HASH_MISMATCH`: **CAUSE_ESTABLISHED_CRLF_VS_LF**; инструмент преобразования и pre-Git archive bytes UNKNOWN.
- Structural/hash/readback PASS относится только к артефактам и **не является R2 acceptance**.

## Навигация

- [Master tracker: направления 0–22, 18 семейств, gates/tests](R2-RESEARCH-MASTER-TRACKER.md)
- [Главный исследовательский отчёт](NOX-R2-RESEARCH-REPORT.md)
- [Executive verdict](01-R2-EXECUTIVE-VERDICT.md)
- [Delivery manifest](DELIVERY-MANIFEST.md) и [machine manifest](DELIVERY-MANIFEST.json)
- [Acceptance design](14-R2-ACCEPTANCE-AND-BENCHMARKS.md), [test matrix](test-matrix.csv), [validation program](validation-program.md)
- [4504 registry](03-COMPLETE-4504-REGISTRY.jsonl), [expanded registry](04-EXPANDED-TOOLS-AND-SKILLS-REGISTRY.jsonl)
- [Solutions research](solutions-research.zip), [solutions evidence](solutions-evidence.md), [Build–Buy–Reuse matrix](13-BUILD-BUY-REUSE-MATRIX.csv)
- [Source/evidence ledger](17-SOURCE-AND-EVIDENCE-LEDGER.jsonl)
- [Owner decisions](18-OWNER-DECISIONS-ONLY.md)
- [SHA-256 manifest](MANIFEST-SHA256.txt)
- [Фактическая validation запись](FINAL-DELIVERY-VALIDATION.json)
- [RAW provenance](raw-provenance/RAW-PROVENANCE.md), [requirements matrix](REQUIREMENTS-18-MATRIX.md), [OpenCode handoff/readiness](OPENCODE-HANDOFF-READYNESS.md)

## Структура

Корень содержит 18 canonical families (`01`–`18`), supporting evidence/reports, registry CSV/JSONL, `solutions-research.zip`, tracker, этот README и checksum manifest. `15-OPENCODE-EXECUTION-PACK/` — только 12 будущих tickets, без изменений Nox. Публикация не меняет существующие каталоги `03`–`07` и исходный Nox.

### Privacy-safe derivative

Пакет является privacy-safe derivative очищенной 81-file версии; 14 доказанно идентичных nested copies удалены. Внутри `solutions-research.zip` исключены 5 внутренних `sources/input/` handoff/review-документов; в двух сохранённых public commit evidence JSON email владельца заменён на `[REDACTED_EMAIL]`. Поэтому SHA вложенного ZIP отличается от исходного. Остальные 77 входных файлов byte-identical. Публичные maintainer/security contacts из upstream registry metadata не считались секретами. Приватный исходник Nox не включён.

## Проверка целостности

Из корня каталога после скачивания GitHub checkout:

```bash
sha256sum -c MANIFEST-SHA256.txt
```

`MANIFEST-SHA256.txt` содержит SHA-256 каждого файла пакета кроме самого manifest (self-reference невозможна). Внешний ZIP hash находится только в sidecar `NOX-R2-CORTEX-RESEARCH-FINAL.zip.sha256` рядом с ZIP. ZIP не включает сам себя или sidecar. `SHA256SUMS` — legacy 63-entry subset, не полный manifest. Canonical F06 renamed without content change. RAW supplied as pinned Git snapshots, not reconstructed originals; CRLF/LF mismatch cause established, pre-Git conversion tool UNKNOWN. Nested solutions SHA-256 отдельно записан в `FINAL-DELIVERY-VALIDATION.json`.

Для проверки исходной 4504-структуры и статусов используйте `inventory-validation-report.json`, `FINAL-VALIDATION.json`, `DELIVERY-MANIFEST.json`; их PASS ограничен artifact structure/readback/hash/evidence refs.

## GitHub limits

GitHub блокирует обычные Git-файлы строго больше **100 MiB** и предупреждает о файлах больше **50 MiB**. Фактический размер финального ZIP указан в `FINAL-DELIVERY-VALIDATION.json` и repair report. Он меньше 100 MiB; отдельные JSONL также меньше лимита. Это ограничение хранилища, не признак исследовательской приёмки.

## Final independent report boundary

Final independent PASS covers previous 87-file ZIP only. Current 89-file package after report addition is locally validated only.
