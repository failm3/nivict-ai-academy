# Покрытие требований 06 и 18 семейств артефактов

**Статус пакета:** `DESIGN_COMPLETE_FOR_ASSIGNED_DIRECTION / ALL_RUNTIME_TESTS_NOT_RUN`. Эти четыре файла — самостоятельное направление acceptance design и coverage map, **не подмена полного исследования 4504 или фактического содержимого остальных workstreams**. `COVERED` означает, что протокол задаёт требуемые evidence/handoff для семейства; не означает, что внешний артефакт уже создан или принят.

## 1. Матрица 18 семейств

| # / обязательное имя | Покрытие в этом пакете | Обязательный upstream evidence перед R2 | Статус содержимого семейства |
|---|---|---|---|
| 01 `01-R2-EXECUTIVE-VERDICT.md` | validation §1–2,8: bounded verdict, UNKNOWN, no GO; G5 decision record | Все G/T actual verdicts, hashes, scope, deviations/costs | `INTERFACE_COVERED`; executive verdict НЕ выпущен |
| 02 `02-NOX-LATEST-RUNTIME-FORENSIC-AUDIT.md` | validation §1,U-01; tickets preamble fresh HEAD/delta; historical product≠mission | Read-only initial/final HEAD/status/hashes, call graph, real receipts, current web chronology | `BLOCKED_UNKNOWN_CURRENT`; baseline не fresh |
| 03 `03-COMPLETE-4504-REGISTRY.jsonl` | U-07 требует cardinality/hash/crosswalk; compliance §3 machine gate | 1331/3173 raw rows, all IDs/raw fields/many-to-many/status/verdict/next_test | `NOT_PROVIDED_HERE`; acceptance cannot claim 4504 coverage |
| 04 `04-EXPANDED-TOOLS-AND-SKILLS-REGISTRY.jsonl` | G1/G2/G3 candidates preserve separate state/L1–L4; T03 provenance | New source IDs, versions/licenses/digests/crossrefs, rejected/inaccessible retained | `INTERFACE_COVERED`; no invented candidate registry |
| 05 `05-READY-MADE-INTEGRATION-ATLAS.md` | OC-06/07 exact native seam, pins/adapters/rollback; T02/T03 negative proof | Actual installed API/source/license/digest/cost/egress/compat | `DESIGN_ONLY`; no candidate declared working |
| 06 `06-ENTERPRISE-COMPARATIVE-RESEARCH.md` | G4/T11 requires equal-task evidence not vendor slogans; no platform replacement | Primary architecture/cases/benchmarks and translated Nox seam from research workstream | `EXTERNAL_DEPENDENCY`; no enterprise conclusion manufactured |
| 07 `07-OPEN-WORLD-COMPETENCE-GRAPH.md` | validation §2 R2/R2.x/R3; T08 graph diff/prerequisites/scope/expiry | Sourced machine graph, domain nodes/oracles/rights/expert signoff | `PROTOCOL_COVERED`; graph extension NOT_RUN |
| 08 `08-CONTINUOUS-KNOWLEDGE-SYSTEM.md` | G3/T04/OC-08: source anchors, rights/ACL, freshness, contradiction/revoke/rebuild | Real source corpus, ingestion quality/cost, tenant tests and source-engine selection | `DESIGN_ONLY`; rights/access UNKNOWN |
| 09 `09-AUTONOMOUS-TOOL-ACQUISITION.md` | G2/T03/OC-07: discover→vet→pin→grant→invoke→QA→revoke, separate approvals | Exact candidate and real sandbox receipts; install/call authority | `PROTOCOL_COVERED / NOT_RUN` |
| 10 `10-EXECUTION-STRATEGY-INTELLIGENCE.md` | G4/T01/T07/T11/OC-10 typed routes/BLOCKED/equal comparisons | Controlled measured results and host route policy | `DESIGN_ONLY`; no route winner claimed |
| 11 `11-LEARNING-META-INTELLIGENCE.md` | G3/T05/T08 held-out fresh transfer/no-benefit/revoke; G4 no-progress | Pack practice+reuse ledger, L4 or no-uplift, expiry/rollback | `PROTOCOL_COVERED`; no learning claimed |
| 12 `12-DOMAIN-CAPABILITY-PACKS.md` | G3 suggested change-impact pack is only proposed fixture; T05/T06/T08 oracle/expert requirements | Owner chosen domain, immutable pack, rights/grants/oracles/expert and acceptance | `PROPOSED_FIXTURE_ONLY`; no ready pack claimed |
| 13 `13-BUILD-BUY-REUSE-MATRIX.csv` | §2 A–H/L mapping below; OC tickets dependencies/economics/rollback | Every significant candidate row with exact evidence and cost statuses | `DECISION_RULES_COVERED`; registry not duplicated |
| 14 `14-R2-ACCEPTANCE-AND-BENCHMARKS.md` | validation-program + test-matrix fully specify G0–G5/T01–T12 | Actual direct Nox run evidence and independent verdicts | `DESIGN_COMPLETE_HERE / EXECUTION_NOT_RUN` |
| 15 `15-OPENCODE-EXECUTION-PACK/` | opencode-tickets OC-01–OC-12 with files/contracts/tests/rollback/owner gates | Owner authorization and actual code diffs/reviews/test receipts | `TICKETS_DESIGNED / NOT_IMPLEMENTED` |
| 16 `16-FASTEST-SAFE-PATH-TO-R2.md` | G0→G1→G2→G3→G4→G5, strict exit and R2.x/R3 separation | Gate evidence can overturn path; no mandatory new core | `PATH_DESIGNED`; not evidence path works current |
| 17 `17-SOURCE-AND-EVIDENCE-LEDGER.jsonl` | validation §3 claim/state/evidence root and §3 compliance machine gate | Source/claim IDs, UTC, versions/digests/licences, observer limitations, all run attempts | `SCHEMA_AND_REQUIREMENTS_COVERED`; ledger not populated by fake runs |
| 18 `18-OWNER-DECISIONS-ONLY.md` | validation §7 and tickets final section concrete decisions/blockers | Owner answers with exact caps/authority/domains/accounts/expert/release scope | `DECISIONS_ENUMERATED / AWAITING_OWNER` |

## 2. Полное соответствие G/T/A–H/L

- **G0–G5:** validation §4 содержит входы, fixtures, пороги, negatives, exit/stop/rollback; engineering dependencies — OC-01…12.
- **T01–T12:** каждая строка `test-matrix.csv` содержит objective, frozen fixture/variants, independent oracle, numeric pass rules, negatives, evidence и blockers. Общие обязательные epoch/terminal/budget/independence rules находятся в validation §3 и применяются к каждой строке.
- **A–H — классификация решений, не test grade:** A требует current callable+scope evidence; B pinned native config+tests; C/D vetted ready/thin integration; E hidden dependencies/cost/risks; F только proven gap и researched alternatives; G defer/reject+revisit; H missing evidence+next check. Ни один компонент в этой программе автоматически не получил A. Tentative research mapping: existing finite web/CSV oracle `A только historical bounded retained scope, current H`; ToolSearch/SkillSearch `B candidate L1/L2 historical`; new adapter `C/D per owner candidate, now H`; knowledge/pack vertical slice `E proposed`; new orchestrator/fine-tuning `G defer`; custom runtime `F not justified`.
- **L1–L4:** validation §3.2; package presence не L3; inherited documents не current L2 для фактической installation; L4 только equal-task independent uplift. Вся новая программа `PLANNED/DOCUMENTED`, исполнительные levels `NOT_RUN`.
- **Отсечение:** validation §2 и G5 запрещают называть R2 general professional qualification; R2.x/R3 требуют новых specs/evidence и не разблокируются бесконечным platform research.

## 3. Machine/evidence compliance gate перед сдачей общего исследования

Скрипт общего пакета (не создан/не запущен здесь) должен FAIL при: отсутствии любого из 18 canonical names; неверном cardinality/JSON path/source order; dropped raw fields; duplicate stable record ID; dangling entity/source/fixture/evidence FK; illegal semantic merge; UNKNOWN=null/zero/free/safe; missing verdict/status/next_test; hash/size mismatch; T/G criterion missing or NOT_FINISHED treated as PASS; solver exposure hidden oracle; late verdict bound to old epoch; unresolved intent admitted; missing failed attempts; dollars inferred from partial tokens.

Минимальный manifest: `{artifact_id,canonical_name,path,sha256,bytes,spec_version,source_head,created_utc,status,coverage_refs,unknown_refs}`; `SHA256SUMS` после readback. Полный 4504 reconciliation — необходимый вход общего research completion, но **не условие корректности проектирования isolated T fixtures**; R2 verdict всё равно не заявляется без обязательной программы и runtime evidence.

## 4. Требования безопасности, rollback и честного статуса

Нет Nox/OpenCode modifications, install, publish, paid stress, provider runs или external effects в этой работе. Все numeric thresholds/samples являются predeclared proposed acceptance rules и требуют freeze до измерений. Любой security leak, stale acceptance, duplicate effect, hidden descendant или authority escalation — stop/GATE_FAIL. Rollback сохраняет failed evidence, versions и старые readers; UNKNOWN external effect reconciles, не retry blindly. Resource/dollar values отсутствуют => UNKNOWN/BLOCKED, не unlimited.

## 5. Финальный чек assigned direction

| Проверка | Результат проектирования |
|---|---|
| 06/07/03/04/05 прочитаны; baseline/transfer limits учтены | DONE (source-reading only) |
| G0–G5, T01–T12, evidence/A–H/L1–L4/R2 boundary | DONE as design |
| Concrete fixtures/metrics/negatives/resources/rollback/UNKNOWN | DONE as proposed protocols |
| Small OpenCode tickets and dependency order | DONE as specifications |
| 18 families coverage and no false completion | DONE as coverage map |
| Runtime tests/missions/install/paid tests/publication/R2 acceptance | NOT_RUN / NOT_PERFORMED / NOT_CLAIMED |
