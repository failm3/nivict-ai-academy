# NOX / AWE GROUP R2 — source baseline and availability (этап 1)

Наблюдение выполнено 2026-11-14, основная readback-точка `2026-11-14T04:26:44Z`; UTC. Статус: **DOCS_AND_RAW_SOURCE_BASELINE; CURRENT_NOX_UNKNOWN; NOT_R2_ACCEPTANCE**.

## 1. Репозитории и точные revisions

| Источник | Точная ссылка / revision | Фактическая доступность и граница |
|---|---|---|
| Канонические документы | `https://github.com/failm3/nivict-ai-academy`; cloned `main`, HEAD `9573a64f2602631ec5d2299716612ba8578c2a13` | **AVAILABLE / READ**. Локально `/workspace/nivict-ai-academy`, clean `## main...origin/main`. Финальный `git ls-remote` снова вернул HEAD/main `9573a64f2602631ec5d2299716612ba8578c2a13`. |
| 06 owner-final | commit `302bdbb72f96f227efc8c8df5a4cb9a942f26a5b`; файл не изменён на HEAD `9573a64…` | **AVAILABLE / FULLY_READ**; 81 097 bytes, SHA-256 `0767476e3da1599aaaa731d43397e01dc944c14247ec016ffae03c68cba1ce1f`. |
| 07 transfer register | commit `9573a64f2602631ec5d2299716612ba8578c2a13` | **AVAILABLE / FULLY_READ**; 22 009 bytes, SHA-256 `97ab44d3b1ca5a78f8e8155bcacb5ed2ee026a2c62f600777a06d3b1742b78ed`. |
| 03/04/05 review | commit `3c3fed07b8222946204cfa8169d9aef04f9f4097` | **AVAILABLE / FULLY_READ_FROM_PINNED_REVISION**. `git cat-file -t`=commit; извлечённые байты в `/workspace/out/baseline-3c3fed07/`. `git diff 3c3fed07…HEAD` для этих трёх файлов пуст. |
| Nox canonical working source | `/home/nox/awe-group-cleanroom-20261112`, ожидаемая branch `r1/dev` | **UNAVAILABLE_IN_THIS_SANDBOX / CURRENT_UNKNOWN**. Проверенный `ls -ld` дал `No such file or directory`. Никакого cleanroom read/HEAD/status/hash/second readback не выполнено. |
| Nox historical review baseline | `r1/dev @ 68cc0ee20a25991ea275512e20ac521cc8f8234b`, clean на 2026-11-14 по 03/05 | **HISTORICAL_DOCUMENTED_ONLY**. Object отсутствует в docs clone (`git cat-file`: could not get object info); это не fresh Nox evidence. |
| Observer project | `https://github.com/failm3/awe-group-observer`; `main` commit `53853f048c412399bcedc5f2dfa268d7e2ee4f6b` | **AVAILABLE_READ_VIA_GITHUB_CONNECTOR**, root API HTTP 200. Это observer, не current Nox source. |
| OpenCode recordings | `https://github.com/failm3/awe-opencode-recordings`; `main` commit `304e5848d64e3bc9c73f80f2a4a642e34a1c300c` | **AVAILABLE_READ_VIA_GITHUB_CONNECTOR**, root API HTTP 200. Timeline/captured events не fresh source или mission verdict. |
| Historical runtime export | `https://github.com/failm3/awe-group-runtime`; HEAD/main `d5e9d857dbdeb8f31f9a798b10b5af4af639dbda` | **AVAILABLE_AS_HISTORICAL_EXPORT_ONLY**. Публичный `ls-remote` и connector root HTTP 200. Не использован как current Nox substitute и не принят за canonical runtime. |
| Запрещённая подмена | `/workspace/new-gemini/nox-r2` | Путь отсутствует в sandbox; **не использовался и не должен использоваться как canonical Nox**. `acceptance/git-state-default104.json` не создавался. |

GitHub connector: `github-31dz69`, connected account label `failm3`; использованы только read calls `get_repository_content` и `get_a_commit`. Анонимный `git ls-remote` двух private observer repos вернул запрос credentials/exit 128, после чего authenticated read-only connector успешно подтвердил доступ. Никаких write calls.

## 2. Точные файлы обязательного baseline

Общий каталог: `03 - Практика/05 - AWE GROUP/RESEARCH/NOX-R2-CORTEX-OPENCODE-REVIEW-2026-11-14/`.

| Файл | Immutable URL | Bytes / SHA-256 | Проверка |
|---|---|---|---|
| `06-CORTEX-R2-FINAL-OWNER-PROMPT-2026-11-14.md` | https://github.com/failm3/nivict-ai-academy/blob/302bdbb72f96f227efc8c8df5a4cb9a942f26a5b/03%20-%20Практика/05%20-%20AWE%20GROUP/RESEARCH/NOX-R2-CORTEX-OPENCODE-REVIEW-2026-11-14/06-CORTEX-R2-FINAL-OWNER-PROMPT-2026-11-14.md | 81 097 / `0767476e3da1599aaaa731d43397e01dc944c14247ec016ffae03c68cba1ce1f` | Полное чтение двумя последовательными диапазонами. |
| `07-CORTEX-ACCOUNT-TRANSFER-FAILURES-2026-11-14.md` | https://github.com/failm3/nivict-ai-academy/blob/9573a64f2602631ec5d2299716612ba8578c2a13/03%20-%20Практика/05%20-%20AWE%20GROUP/RESEARCH/NOX-R2-CORTEX-OPENCODE-REVIEW-2026-11-14/07-CORTEX-ACCOUNT-TRANSFER-FAILURES-2026-11-14.md | 22 009 / `97ab44d3b1ca5a78f8e8155bcacb5ed2ee026a2c62f600777a06d3b1742b78ed` | Полное чтение. |
| `03-OPENCODE-ENGINEERING-REVIEW.md` | https://github.com/failm3/nivict-ai-academy/blob/3c3fed07b8222946204cfa8169d9aef04f9f4097/03%20-%20Практика/05%20-%20AWE%20GROUP/RESEARCH/NOX-R2-CORTEX-OPENCODE-REVIEW-2026-11-14/03-OPENCODE-ENGINEERING-REVIEW.md | 27 136 / `e3c421d40daf886462600b33f0bcc8fd990349a639f758d6a79b68ba55614ea4` | Полное чтение pinned bytes; совпадает 05 §10. |
| `04-CORTEX-R2-BRIEF-REVISED-BY-OPENCODE.md` | https://github.com/failm3/nivict-ai-academy/blob/3c3fed07b8222946204cfa8169d9aef04f9f4097/03%20-%20Практика/05%20-%20AWE%20GROUP/RESEARCH/NOX-R2-CORTEX-OPENCODE-REVIEW-2026-11-14/04-CORTEX-R2-BRIEF-REVISED-BY-OPENCODE.md | 69 871 / `579edcaa62d8e20bc4bfd6feba3ac9bd018899c824a01941b7ef0d8fe1b5ed60` | Полное чтение pinned bytes двумя диапазонами; совпадает 05 §10. |
| `05-REVIEW-EVIDENCE-MANIFEST.md` | https://github.com/failm3/nivict-ai-academy/blob/3c3fed07b8222946204cfa8169d9aef04f9f4097/03%20-%20Практика/05%20-%20AWE%20GROUP/RESEARCH/NOX-R2-CORTEX-OPENCODE-REVIEW-2026-11-14/05-REVIEW-EVIDENCE-MANIFEST.md | 22 789 / `bfd9690624dab166bbe65507e8579ca61d33ec2a67e2ee6d1f7a298b69b46227` | Полное чтение pinned bytes. Внешний hash; self-hash в самом 05 отсутствует by design. |

Все 03/04/05 были прочитаны из `git show 3c3fed07:<path>` и сохранены как readback-копии, без повторной публикации.

Дополнительно по 07 §5.2 прочитаны:

- `03 - Практика/05 - AWE GROUP/CHECKPOINTS/CHAT-TRANSFER-NOX-R2-CORTEX-2026-11-14/01-CHAT-HANDOFF-FULL.md` — **AVAILABLE / FULLY_READ** на `9573a64…`.
- `03 - Практика/05 - AWE GROUP/CHECKPOINTS/CHAT-TRANSFER-NOX-R2-CORTEX-2026-11-14/02-RECENT-DECISIONS-AND-QUOTES.md` — **AVAILABLE / FULLY_READ** на `9573a64…`.
- Их утверждение «финальный промпт ещё не создан» исторически устарело и прямо superseded документом 07; не является заданием создавать prompt заново.

## 3. Канонические RAW: фактические байты и кардинальность

Base path: `04 - Инструменты/Каталог кандидатов/90 - Данные/`. Все ниже находятся в docs commit `9573a64f2602631ec5d2299716612ba8578c2a13`; первоначально импортированы commit `3e0ce118dab770b609e39ed5fde901dd4f5c98bc` (2026-11-04T15:08:02+03:00, `catalog: import 4504 tool candidates`). JSON распарсены стандартным `json`; CSV — `csv.reader` с `newline=''` и UTF-8-SIG, поэтому multiline fields не считались физическими строками. Машинный результат: `/workspace/out/raw-baseline.json`; read-only script: `/workspace/out/inspect_raw.py`.

| ID / файл | Exact pinned URL | Bytes | SHA-256 | Фактическая структура |
|---|---|---:|---|---|
| **RAW-IIR** `iirepresent.json` | https://github.com/failm3/nivict-ai-academy/blob/9573a64f2602631ec5d2299716612ba8578c2a13/04%20-%20Инструменты/Каталог%20кандидатов/90%20-%20Данные/iirepresent.json | 850 896 | `01dc8a9f15f769f0c240fe7d64442ea279ef6461675f9f4204eb47571701ddc5` | JSON list, **1331** records, все objects; первые keys `link,description`. Git blob `eb5c857c66af7701e58745ebce66585e48ab119e`. |
| **RAW-RADAR** `Радар.json` | https://github.com/failm3/nivict-ai-academy/blob/9573a64f2602631ec5d2299716612ba8578c2a13/04%20-%20Инструменты/Каталог%20кандидатов/90%20-%20Данные/Радар.json | 2 257 187 | `2f5c6806030dba7ac7b3e8e3c1cf9510054e88ac7085d46b08a941ecf9dc4221` | JSON list, **3173** records, все objects; первые keys `link,description`. Git blob `09cbfa76a6aeebb6d208e7b6c565604549854f9c`. |
| **RAW-CSV** `catalog-all-4504.csv` | https://github.com/failm3/nivict-ai-academy/blob/9573a64f2602631ec5d2299716612ba8578c2a13/04%20-%20Инструменты/Каталог%20кандидатов/90%20-%20Данные/catalog-all-4504.csv | 4 048 275 | `8ad601eb0ff81cf8b8597da7276819c58bd4f156d1c269789fd4907bae9b3fa4` | **4504 data records + 1 header**, 16 columns, **0 uneven-width records**. Git blob `4f2a4739b5e6bb6a412de26bfefccaa51d39b7f7`. |

Фактический arithmetic invariant на текущих RAW: `1331 + 3173 = 4504`; CSV data cardinality = 4504. Это **parse/cardinality check**, не complete crosswalk/semantic audit и не 4504 installed/unique/callable tools.

CSV columns, точно: `id, source, source_row, url, description, host, title, category, confidence, resource_type, multi_service_description, exact_duplicate_group_size, address_group_size, note_path, secondary_categories, flags`.

### Обнаруженное расхождение historical validation

`validation-report.json` утверждает `source_json_copied_byte_exact=true`, но его старые hashes не совпадают с текущими RAW:

- `iirepresent.json`: report `ee54b674c057f0c67b584b77e02454a175c6853c769452e4654559f2582b1c3b`; actual `01dc8a9f15f769f0c240fe7d64442ea279ef6461675f9f4204eb47571701ddc5`.
- `Радар.json`: report `3a73e487a8187369753c627010bd36a22559b3b51b3ecae724265ef617c1c800`; actual `2f5c6806030dba7ac7b3e8e3c1cf9510054e88ac7085d46b08a941ecf9dc4221`.

Это подтверждённый **SOURCE_HASH_MISMATCH**. Причина/характер изменений **UNKNOWN** до byte/field diff против исходных bytes (которых в этом report нет). Нельзя использовать старые hashes как текущие или утверждать byte-exact preservation.

## 4. Related exports/cards — доступны, но не RAW substitute

| Источник | Bytes / SHA-256 | Фактическая доступность |
|---|---|---|
| `all-records-classified.json` | 5 620 443 / `5a83c501b290b83a17f6ffaeb0fe9cae772e26be7a6a4c5cbcb948908fc76b56` | JSON list, 4504 objects, те же 16 primary fields; derived classified export. |
| `NIVICT-Radar-Cleaned-2026-11-04.json` | 3 821 780 / `6565a67e7d6342abda58e8da2a7f111a1ee976d46b0dd73f6c79f695fc6e927e` | JSON object с `entries` и metadata; cleaned derived export. |
| `NIVICT-Tool-Shortlist-2026-11-04.json` | 16 486 / `31745efd9f4f15cdedb09620fe718de899a18da010e3265dc4f5c67fa1026f0f` | Shortlist only, не полный registry. |
| `NIVICT-Tools-Radar-Review-2026-11-04.md` | 12 953 bytes | Historical narrative review; не current runtime evidence. |
| `duplicates.csv` | 8 260 / `d3bbbd6b26aeabd46c1bd85f4ba6a029fc5b5b50390c9d04f7db4a545494bbd9` | 71 data records; derived duplicate report. |
| `issues.csv` | 315 799 / `43568762d8f8ae8f3a151db94e0bc67fc2c0334c4a1a3ce43d272b3a755f214b` | 4090 data records; derived issues report. |
| `import-manifest.json` | 669 / `a4c1d6debdb69c447ae15c8f3c03edc154fd0a6b6edf9c257c5d3221dc82c652` | Declares candidate_to_study, 4504=1331+3173, 72 category files, source archive hash; no live verification. |
| `validation-report.json` | 2 584 / `dfd4a0bbb143d86c9fe420c5c98b5accaeeb3333e6700f3b9a085799b4cc27b5` | Historical counts/classification; website validation NOT PERFORMED; hash mismatch выше. |
| `04 - Инструменты/Каталог кандидатов/20 - Записи/` | 4504 `.md` files | Available card set; crosswalk ещё не выполнен. |
| `04 - Инструменты/Каталог кандидатов/10 - Категории/` | 72 `.md` files | Available category set. |

`import-manifest.json` ссылается на `NIVICT-Obsidian-Tools-2026-11-04.zip` и `source_archive_sha256=c244692a73e3dfd3d39ee5e6561297d8cf6abe43831f340a04d24997fc4b1fb9`; сам archive в найденном raw-data каталоге отсутствует/не проверен как доступный объект. Поэтому archive bytes и соответствие hash **UNKNOWN**.

## 5. Доступность остальных canonical docs (06 §2.4)

Все пути ниже **PRESENT** на docs `9573a64…`; наличие docs не означает, что их содержимое полностью проаудитировано этим этапом:

| Под `03 - Практика/05 - AWE GROUP/` | Фактическое число файлов | Статус |
|---|---:|---|
| `R1-CAPABILITY-PROGRAM/` | 10 | Available canonical docs, не current source. |
| `RESEARCH/KORTIX-2026-11-13-ENTERPRISE-RESEARCH/` | 23 | Historical research package, не R2 implementation. |
| `RESEARCH/CORTEX-NOX-CAPABILITY-KNOWLEDGE-MARKET-AUDIT-SCOPE-2026-11-13.md` | 1 | Present. |
| `PROMPTS/CORTEX-NOX-ENTERPRISE-CAPABILITY-RESEARCH-FINAL-2026-11-13.md` | 1 | Present. |
| `IDEAS/` | 4 | Present. |
| `ASTRA-AUTONOMY-AUDIT-2026-11-08/` | 8 | Present. |
| `CHECKPOINTS/` | 18 | Present, включая transfer 01/02. |
| `DECISIONS/` | 18 | Present. |
| `TESTS/` | 13 | Historical test docs, не fresh tests. |

## 6. Runtime vs historical evidence — строгая классификация

- **CURRENT_NOX = UNKNOWN.** В этом sandbox нет `/home/nox/awe-group-cleanroom-20261112`; computer/WSL connector в `kortix connectors ls` отсутствует (есть только GitHub). Нет fresh branch/HEAD/status/package-lock/call graph/logs/checkpoint read.
- `68cc0ee20a25991ea275512e20ac521cc8f8234b`, installed pins, 39/39, R0 252/55, web 13/13, PAUSED timeout/intents и token subtotals взяты из **исторического OpenCode review 03/05**, не из свежего runtime чтения этим этапом.
- `awe-group-runtime @ d5e9d857…` — доступный **historical export only**; его root read не доказывает current source HEAD, healthy runtime или accepted mission.
- Observer/recordings HEAD доступны, но их root listings не использовались как runtime proof; никакого current Nox inference из events.
- Документы 03/04/05 исторически уже опубликованы; неизменность до docs HEAD проверена. Ничего из них не перепубликовано.
- Все T01–T12, G0–G5 и новые проверки **NOT_RUN / PROGRAM_ONLY** в этом этапе. Нет R2 acceptance.

## 7. UNKNOWN / BLOCKED registry и точные NEXT_TEST

| ID | UNKNOWN / фактический пробел | Следствие | NEXT_TEST / условие |
|---|---|---|---|
| U-01 | Current Nox branch/HEAD/status, source hashes и delta от `68cc0ee…` | Нельзя делать latest/wired/current claims | При действующем owner read-only access выполнить `git status --short --branch`, `git rev-parse HEAD`, hashes package/source; initial+final readback в `/home/nox/awe-group-cleanroom-20261112`. |
| U-02 | Current package.json/package-lock, production call graph, installed Mastra/Playwright contracts | Baseline pins не current | Fresh-read exact files/installed typings на authorized cleanroom; сравнить pins/lock/digest. |
| U-03 | Current run trees/logs/checkpoints/model ledger и mission terminal state | Historical PAUSED/PASS нельзя обновлять или подтверждать current | Fresh-read `reports/R1-LOCAL-WEB-PRACTICE.md`, обе run trees, actual checkpoint/intent/logs/ledger; no mission resume. |
| U-04 | Current provider/model/MCP health, quality, task-sensitive suitability, dynamic discovery savings | Никаких current CALLABLE/L3/L4 claims | Отдельно owner-approved bounded nonprod probes/oracles; до этого NOT_RUN. |
| U-05 | Complete usage, transport retries, provider invoice/USD | 337014 и 104613 не total/bill | Reconcile complete invocation ledger+provider invoice; missing остаётся UNKNOWN, не суммировать как полную стоимость. |
| U-06 | Полный JSON↔CSV↔cards↔exports crosswalk, dup/missing/unexpected/dangling | Cardinality известна, reconciliation не выполнена | Создать durable per-row IDs и many-to-many map по всем 4504; hashes/counts/invariants/exceptions. |
| U-07 | Current per-row upstream version/health/license/security/auth/cost/compatibility/call/QA | Нет executable/current verdict для 4504 | L1/L2 source research per row; приоритизированные separately authorized sandboxes для L3/L4; no execution of all required. |
| U-08 | Причина mismatch старых validation hashes vs actual RAW | Нельзя подтвердить byte-exact copy или характер изменений | Получить исходные bytes/archive, сопоставить hash и field-level diff; сохранить обе identities, не перезаписывать RAW. |
| U-09 | `NIVICT-Obsidian-Tools-2026-11-04.zip` bytes/availability | Archive hash не подтверждён | Найти canonical archive/location через owner-authorized source, затем SHA-256/readback; не выдумывать archive. |
| U-10 | Previous Cortex agents completion/results/cost после account transfer | UI tasks не completion; нельзя claim prior work | Получить реально доступные artifacts с source/byte verification; иначе оставить UNKNOWN, не повторять публикацию baseline. |
| U-11 | `/workspace/new-gemini/nox-r2`, `acceptance/git-state-default104.json`, `NOX_R2_NATIVE_HIVE_REVIEW_V1` origin/relevance | Нет scoped native review evidence; не блокирует desk research | Только проследить source path/session/task/version при наличии; не создавать fake snapshot. |
| U-12 | Mastra 404 observed old account: точные URLs и влияние | 404 ≠ absent API | Логировать exact failed URL/date; installed pinned typings/source first; latest supported docs separately. |
| U-13 | Current production auth/tenancy/Windows computer-use isolation/professional qualification/release | Нет security/pro qualification claim | Owner-scoped threat model+qualified independent tests; current direct Nox required. |
| U-14 | Current source licensing/corpus ACL/held-out transfer/domain expert acceptance | Knowledge≠competence | Source rights/ACL vetting and frozen fresh-agent/domain evaluations after owner approval. |
| U-15 | Latest upstream versions/compat outside historical installed pins | Нет version-drift-free integration claim | Exact primary upstream release/tag/SHA/LICENSE/package digest compared to fresh installed pin. |
| U-16 | Все proposed repairs/tickets и T01–T12/G0–G5 outcomes | **NOT_RUN**, no PASS/GO | Реализовать только после owner approval; direct Nox+independent QA+negative controls+budget+rollback по 06. |
| U-17 | Research/build/acquisition/run/QA/maintenance/failed-attempt full TCO | Нет calendar/cost estimate | Использовать actual invoices/ledgers и pinned API smoke при отдельном разрешении; иначе UNKNOWN. |

## 8. Readback выполненного этапа

- Полный checklist: `/workspace/out/requirements.md`.
- Настоящий baseline: `/workspace/out/source-baseline.md`.
- RAW machine facts: `/workspace/out/raw-baseline.json`.
- Воспроизводимый parser: `/workspace/out/inspect_raw.py`.
- Pinned readback 03/04/05: `/workspace/out/baseline-3c3fed07/`.
- Read-only connector receipts: `/workspace/out/access-evidence/`.
- Source docs repository остаётся clean; исходные 01–07 и RAW не изменялись, commits/push/publication не выполнялись.
