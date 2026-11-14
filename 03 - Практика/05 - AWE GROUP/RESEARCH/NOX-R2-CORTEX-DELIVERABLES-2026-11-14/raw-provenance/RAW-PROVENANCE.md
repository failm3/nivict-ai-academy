# NOX R2 — RAW provenance, snapshots and reconciliation

Status: **PINNED_SOURCE_SNAPSHOTS / 4504_L1_UNVETTED_H / NOT_RUNTIME_OR_R2_ACCEPTANCE**.

## 1. Source snapshots supplied

The three files in `snapshots/` are **byte-exact copies of Git blobs from the canonical GitHub repository**, not reconstructions and not regenerated catalogues:

- Source repository: `https://github.com/failm3/nivict-ai-academy`.
- Original import commit: **`3e0ce118dab770b609e39ed5fde901dd4f5c98bc`**, author/commit date `2026-11-04T15:08:02+03:00`, subject `catalog: import 4504 tool candidates`.
- Readback HEAD: **`9573a64f2602631ec5d2299716612ba8578c2a13`**.
- For all three, `git show import:path`, `git show HEAD:path`, original clean worktree and supplied snapshot are byte-identical.
- Git history for the three RAW and historical validation report contains only the import commit; no later RAW rewrite was found.

| Snapshot | Exact GitHub path | Bytes | Git-stored SHA-256 | Rows |
|---|---|---:|---|---:|
| `snapshots/iirepresent.json` | `04 - Инструменты/Каталог кандидатов/90 - Данные/iirepresent.json` | 850896 | `01dc8a9f15f769f0c240fe7d64442ea279ef6461675f9f4204eb47571701ddc5` | 1331 |
| `snapshots/Радар.json` | `04 - Инструменты/Каталог кандидатов/90 - Данные/Радар.json` | 2257187 | `2f5c6806030dba7ac7b3e8e3c1cf9510054e88ac7085d46b08a941ecf9dc4221` | 3173 |
| `snapshots/catalog-all-4504.csv` | `04 - Инструменты/Каталог кандидатов/90 - Данные/catalog-all-4504.csv` | 4048275 | `8ad601eb0ff81cf8b8597da7276819c58bd4f156d1c269789fd4907bae9b3fa4` | 4504 data + header |

Pinned raw URLs (use the same commit, not floating main):

- https://raw.githubusercontent.com/failm3/nivict-ai-academy/3e0ce118dab770b609e39ed5fde901dd4f5c98bc/04%20-%20%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B/%D0%9A%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3%20%D0%BA%D0%B0%D0%BD%D0%B4%D0%B8%D0%B4%D0%B0%D1%82%D0%BE%D0%B2/90%20-%20%D0%94%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5/iirepresent.json
- https://raw.githubusercontent.com/failm3/nivict-ai-academy/3e0ce118dab770b609e39ed5fde901dd4f5c98bc/04%20-%20%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B/%D0%9A%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3%20%D0%BA%D0%B0%D0%BD%D0%B4%D0%B8%D0%B4%D0%B0%D1%82%D0%BE%D0%B2/90%20-%20%D0%94%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5/%D0%A0%D0%B0%D0%B4%D0%B0%D1%80.json
- https://raw.githubusercontent.com/failm3/nivict-ai-academy/3e0ce118dab770b609e39ed5fde901dd4f5c98bc/04%20-%20%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B/%D0%9A%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3%20%D0%BA%D0%B0%D0%BD%D0%B4%D0%B8%D0%B4%D0%B0%D1%82%D0%BE%D0%B2/90%20-%20%D0%94%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5/catalog-all-4504.csv

These are canonical **Git-stored source snapshots**. The separate pre-Git/original-archive byte streams were not independently retained; no claim is made that Git bytes equal those unavailable pre-Git bytes.

## 2. Independent reproduction

```bash
git clone https://github.com/failm3/nivict-ai-academy.git nox-raw-check
cd nox-raw-check
git checkout --detach 3e0ce118dab770b609e39ed5fde901dd4f5c98bc
base='04 - Инструменты/Каталог кандидатов/90 - Данные'
sha256sum "$base/iirepresent.json" "$base/Радар.json" "$base/catalog-all-4504.csv"
wc -c "$base/iirepresent.json" "$base/Радар.json" "$base/catalog-all-4504.csv"

# Full independent snapshot + registry check:
python3 /workspace/out/raw-provenance/verify_raw_provenance.py \
  --repo /workspace/nivict-ai-academy \
  --registry /workspace/out/inventory/03-COMPLETE-4504-REGISTRY.jsonl \
  --work /workspace/out/raw-provenance
```

The validator uses Python stdlib only, performs no network operation or runtime test, and fails on any wrong hash, row count, order, identity, raw object or L1/UNVETTED/H status.

## 3. SOURCE_HASH_MISMATCH — cause established

Historical `validation-report.json` and `01 - Аудит.md` report:

- `iirepresent.json`: `ee54b674c057f0c67b584b77e02454a175c6853c769452e4654559f2582b1c3b`;
- `Радар.json`: `3a73e487a8187369753c627010bd36a22559b3b51b3ecae724265ef617c1c800`.

Verified explanation: those are SHA-256 values of **CRLF** byte variants; canonical Git blobs contain **LF** newlines.

| File | Git LF count | LF bytes / SHA-256 | CRLF bytes / SHA-256 | Exact match to historical |
|---|---:|---|---|---|
| `iirepresent.json` | 5326 | 850896 / `01dc8a9f…1ddc5` | 856222 / `ee54b674…2b1c3b` | **YES** |
| `Радар.json` | 12694 | 2257187 / `2f5c6806…dc4221` | 2269881 / `3a73e487…c1c800` | **YES** |

For both files: `LF_bytes.replace(b"\n", b"\r\n")` produces exactly the historical SHA; reverse CRLF→LF reproduces Git bytes exactly. No BOM/content/record change is required. `catalog-all-4504.csv` was not listed in historical JSON source hashes and has no such mismatch.

Reproduce only the hash relationship without writing alternative files:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib
base=Path('/workspace/out/raw-provenance/snapshots')
for name in ['iirepresent.json','Радар.json']:
    b=(base/name).read_bytes()
    assert b'\r\n' not in b
    print(name, 'LF', len(b), hashlib.sha256(b).hexdigest())
    c=b.replace(b'\n',b'\r\n')
    print(name, 'CRLF', len(c), hashlib.sha256(c).hexdigest())
    assert c.replace(b'\r\n',b'\n')==b
PY
```

**Remaining limited UNKNOWN:** no record establishes which local tool/configuration performed the line-ending conversion before Git storage, and separately retained pre-Git bytes/archive are unavailable. The transformation and mismatch cause are nevertheless proven. The original archive is not required to verify the pinned Git snapshots; it would only establish earlier provenance.

## 4. Registry reconciliation

Independent report: `RAW-VALIDATION-REPORT.json`; detailed data: `RAW-RECONCILIATION.json`; console readback: `validation.log`.

- **4504/4504** ordered original rows reconciled.
- **4504/4504** raw JSON object exact equality.
- **4504/4504** stable identity and source pointer equality.
- **4504** unique record IDs; missing **0**, unexpected **0**, duplicate IDs **0**.
- Source split: **1331 iirepresent + 3173 Радар**.
- **4504/4504** preserve **L1 / UNVETTED / H**.
- No L2/L3/L4 or current Nox/health/install/call/QA/acceptance claim is added.

## 5. Additional provenance material

Also copied from the same import commit for independent context: `snapshots/validation-report.json`, `snapshots/import-manifest.json`. Historical `01 - Аудит.md` is supplied as `snapshots/historical-audit-2026-11-04.md`. These support the line-ending diagnosis but remain historical claims, not live verification. Final file hashes: `checksums.json`.
