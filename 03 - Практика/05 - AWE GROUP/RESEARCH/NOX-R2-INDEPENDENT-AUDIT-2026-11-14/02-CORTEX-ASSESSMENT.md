# Оценка Cortex: принять, исправить, отклонить

Проверен снимок `failm3/nivict-ai-academy@f9d8460b093b27a80fb0c04d9a3159733717f77d`, каталог `03 - Практика/05 - AWE GROUP/RESEARCH/NOX-R2-CORTEX-DELIVERABLES-2026-11-14/`. Это оценка содержимого, не изменение исходного пакета.

## 1. Независимо подтверждённая целостность

- 118 физических файлов; Git blob SHA каждого скачанного файла совпал с деревом pinned commit.
- `PUBLICATION-MANIFEST-SHA256.txt`: 117/117 OK; self-entry отсутствует ожидаемо.
- Все 27 chunks и пять originals собраны в памяти; размеры/SHA-256 совпали с `chunks/ASSEMBLY-MANIFEST.json`.
- Registry: 4 504 rows и 4 504 unique record IDs; все `UNVETTED`. Это полный structural inventory, не 4 504 vetted/callable tools.
- Expanded registry: 32 role-specific rows, не 32 независимые технологии.
- `test-matrix.csv`: 12 rows, все `PLANNED/NOT_RUN`; OC-01…OC-12 — спецификации, не реализация.

Машинные результаты: `verification.json` и `cortex-download-verification.json` (последний — отдельный record рядом с публикацией deliverable). Эти проверки не повышают runtime/R2 статус.

## 2. Главная ценность — принять как normative design baseline

1. Честные уровни evidence и граница structural PASS ≠ runtime acceptance.
2. Product verdict ≠ mission terminal verdict; late PASS не принимает paused mission.
3. Independent oracle/reviewer, frozen fixtures, negative controls, сохранение всех attempts/UNKNOWN.
4. G0-first correctness и reuse-first; не заменять существующий orchestration без доказанного gap.
5. Discovery/registry/install/grant/load/invoke/QA — отдельные authority states.
6. Source rights/ACL до indexing/prompt/cache, held-out fresh-agent transfer, no-benefit как допустимый результат.
7. Конкретные T01–T12 fixtures/oracles полезнее generic LLM self-assessment.

## 3. Что подтверждено текущим Nox

- OC-01 basename defect — реален.
- OC-02 CandidateEpoch/complete EvidenceBundle — отсутствуют; truncation уже fail-closed, а не silent acceptance.
- OC-03 нужен как gap closure: существующие fencing/seal/final revalidation нельзя игнорировать.
- OC-04: deterministic preflight/no-progress/reservations неполны, но cumulative elapsed/exhausted-resume и repair caps уже есть.
- OC-05: базовый durable UNKNOWN-safe ledger есть; неполны per-node и whole-mission projections.
- OC-06: ToolSearch не wired; installed Mastra предоставляет candidate seam, но benefit не доказан.
- OC-07: Playwright уже wired; нужна repair/pinning/security/contract квалификация, не обязательно новый adapter.
- OC-08/09/10/11/12 — разумные draft specifications, не готовые capabilities или результаты.

## 4. Ошибки, устаревшие или слишком широкие формулировки

### 4.1 Current Nox UNKNOWN

Это было корректным ограничением Cortex без canonical source. Для текущего аудита HEAD доступен, поэтому source/wiring состояния больше не UNKNOWN. Live provider, live MCP, текущая runtime acceptance и costs остаются UNKNOWN.

### 4.2 Метаданные пакета требуют исправления

Подтверждены чтением/структурными проверками и независимым package reviewer:

- конфликтующие 89/93/83-file package counts без достаточного version scoping;
- malformed F12 hash field в `DELIVERY-MANIFEST.md`;
- старый nested ZIP hash/bytes в нескольких ledger/validation documents при фактическом `22 702 266` bytes, SHA-256 `fbd330bdf070f91246e43edaf2273579085cde335ed29f07fbb8a21276ff3348`;
- противоречие о наличии алгоритма F15 directory hash;
- stale утверждения «HASH_MISMATCH cause UNKNOWN», хотя CRLF/LF причина отдельно воспроизведена;
- incomplete reproduction instructions: named validator/log отсутствуют;
- legacy manifests не эквивалентны current chunked physical package.

Исторические records можно сохранить, но нужен superseded-by pointer и один current package identity/manifest.

### 4.3 Research depth и licenses

«All 32 L2» слишком широко: например Inspector license описан как MIT в одних строках и mixed MIT/Apache/CC-BY в pinned shortlist. Нужно reconciliation по scope. Повторяющиеся upstream под разными role IDs допустимы, но требуется `upstream_entity_id ↔ role`, а не слепая дедупликация.

### 4.4 Статистика и «fastest»

12 pairs — planning minimum, не доказательство power. Положительный point estimate без заранее заданного практического effect и убедительного CI не должен становиться accepted uplift; нужен `INCONCLUSIVE`. «Fastest safe path» не измерен; корректнее «lowest-dependency proposed path».

### 4.5 Жёсткая линейность OC-01→…→OC-12

Ticket number не должен управлять promotion. Fixtures, ledger schema design и independent harness могут готовиться параллельно. T08 competence-graph extension и remediation после T06/T09 требуют явных owners, а не только общего acceptance harness.

## 5. Что изменить в порядке работ

Не отклонять G0→G5 как release dependency graph, но изменить engineering sequence:

1. G0-min: artifact/candidate/terminal correctness.
2. **OC-12-smoke:** ранний bounded direct-Nox baseline текущего продукта, без R2 claim.
3. Ledger/economics completeness и OC-10-lite: typed route/planning failure/outcome metrics.
4. OC-06/07 только при конкретном tool/browser gap.
5. OC-08/09: один source/skill pack с held-out test.
6. Adaptive optimization и OC-12-final: полный согласованный scope.

Ранний diagnostic запуск не заменяет G0–G5 и не даёт права объявить R2.

## 6. Take / rephrase / reject

**Take:** `validation-program.md`, `test-matrix.csv`, evidence boundaries, G0 correctness, OC-01/02, additive OC-05, scoped OC-08/09/10/11/12.

**Rephrase:** OC-03/04 с учётом уже существующих lifecycle controls; OC-06 как measured experiment; OC-07 как repair текущего adapter; candidate ranking, metadata, statistics и traceability.

**Reject:** любые выводы о production security, working R2, measured savings/uplift, universal professional competence, proven fastest path или пригодности tool только по package presence/hash/registry membership.

**Итог:** `CONDITIONAL_TAKE`: сильная research/design основа, но не unchanged execution manifest и не acceptance evidence.
