# NOX R2 — reproducible complete RAW inventory

Scope: 4504 original rows from canonical RAW at docs HEAD `9573a64f2602631ec5d2299716612ba8578c2a13`. Read-only inputs; no Nox/source changes, installs, tests, external publication or R2 acceptance.

## Files

- `../build_inventory.py` — deterministic stdlib parser/classifier/crosswalk builder.
- `../verify_inventory.py` — independent structural and byte/readback assertions.
- `03-COMPLETE-4504-REGISTRY.jsonl` — full nested registry, one record per original row.
- `catalog-4504.csv` — flat analysis/export view with raw JSON round-trip column.
- `registry.schema.json` — required core contract; `UNKNOWN` string sentinel is intentional.
- `data-quality.json`, `DATA-QUALITY.md` — invariants, counts, anomalies, coverage and UNKNOWNs.
- `duplicates.csv`, `duplicate-groups.json` — candidate exact/address groups, no source deletion.
- `taxonomy.json`, `TAXONOMY.md` — four contours, purposes, maturity/reuse/evidence/confidence.
- `evidence-ledger.jsonl` — input and per-record provenance/evidence/next-check ledger.
- `anomalies.csv` — structural/URL anomalies; not security/health verdicts.
- `manifest.json` — input/output hashes (created before post-build reports/validator; `checksum-manifest.json` covers final set).
- `validation-report.json` — independent PASS facts.
- `../inventory-validation.log` — validator output.
- `../RANKED-ACTIONABLE-SHORTLIST.md` — separate RAW-only upstream-vetted shortlist.
- `../shortlist-upstream-research.{md,json}` — detailed shortlist evidence.

## Reproduce

```bash
python3 /workspace/out/build_inventory.py \
  --repo /workspace/nivict-ai-academy \
  --out /workspace/out/inventory

python3 /workspace/out/verify_inventory.py \
  --repo /workspace/nivict-ai-academy \
  --out /workspace/out/inventory \
  > /workspace/out/inventory-validation.log
```

Parser uses Python standard library only. It aborts if any of the three canonical RAW hashes differs from the pinned baseline. Builder regeneration replaces generated inventory files, never RAW or Nox. Reports/validator are intentionally separate so generation and independent verification are visible.

## Query examples

```bash
# Count records by origin and evidence.
jq -r '.origin_collection' /workspace/out/inventory/03-COMPLETE-4504-REGISTRY.jsonl | sort | uniq -c
jq -r '.evidence.level' /workspace/out/inventory/03-COMPLETE-4504-REGISTRY.jsonl | sort | uniq -c

# Inspect a source identity.
rg '^.*"record_id":"Радар-1737"' /workspace/out/inventory/03-COMPLETE-4504-REGISTRY.jsonl | jq .

# Metrics.
jq '{counts:.counts_by_source, dedup:.candidate_dedup, crosswalk:.crosswalk}' \
  /workspace/out/inventory/data-quality.json
```

## Evidence boundary

All 4504 rows are L1/H until specific further research. No URL health, semantic uniqueness, executable status, installation, authorization, health, actual call, QA, release, cost or Nox compatibility is inferred. Shortlist L2 is limited to cited upstream facts, not an integration PASS. `SOURCE_HASH_MISMATCH` is confirmed but its cause remains UNKNOWN pending original bytes/archive.
