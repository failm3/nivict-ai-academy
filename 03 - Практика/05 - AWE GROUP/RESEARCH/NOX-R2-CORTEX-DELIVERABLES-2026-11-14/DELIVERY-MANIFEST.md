# Nox R2 delivery manifest

**Статус:** `RESEARCH_PACKAGE_READY_WITH_EXPLICIT_LIMITATIONS`. GitHub: готов **только как research/design snapshot**, не R2/production/release evidence. Current Nox UNKNOWN; G0–G5/T01–T12 NOT_RUN. Публикация этим синтезом не выполнялась.

## 18 обязательных семейств

| ID | Canonical path | Bytes | SHA-256 | Фактический статус | Источник | Ограничение |
|---|---|---:|---|---|---|---|
| F01 | `01-R2-EXECUTIVE-VERDICT.md` | 1296 | `c081c54234f78bb090b30f8fa157d61b75b9a89c750c25bc35d423d04a178d07` | DOCUMENTED_RESEARCH_COMPLETE_NO_GO | `NOX-R2-RESEARCH-REPORT.md`, `requirements.md`, `artifact-compliance.md` | Synthesis of supplied directions; no runtime evidence |
| F02 | `02-NOX-LATEST-RUNTIME-FORENSIC-AUDIT.md` | 3077 | `b4e75c71c83d9e58b1214e5402db2db9389d3256d52b575994c2a2641787497c` | BLOCKED_UNKNOWN_CURRENT | `source-baseline.md`, `validation-program.md`, `opencode-tickets.md` | Historical baseline only; no fresh HEAD/call graph/receipts/readback |
| F03 | `03-COMPLETE-4504-REGISTRY.jsonl` | 32113102 | `707a967b53c3cbdc8f0dbc7813c948c4f54710643554884314a1df6d308a6b71` | STRUCTURAL_COMPLETE_4504_L1_H | `catalog-4504.csv`, `raw-baseline.json`, `inventory-validation-report.json` | Raw rows preserved; per-row L2/L3/L4 not complete |
| F04 | `04-EXPANDED-TOOLS-AND-SKILLS-REGISTRY.jsonl` | 66262 | `945d9f58654035a1a5ef965f23911086cf2532a0799eeda54282740c847c8d14` | L2_32_CANDIDATES_NOT_RUN | `solutions-catalog.csv`, `solutions-research.zip:knowledge-candidates.json`, `solutions-research.zip:evals-candidates.json` | 19 solutions + 7 knowledge + 6 evals; not exhaustive universe; Nox fit UNKNOWN |
| F05 | `05-READY-MADE-INTEGRATION-ATLAS.md` | 11109 | `675c9c3eafcf44f69c86d830d00c915f0143e88d03622e08ab8be0bf7f193429` | L2_DESIGN_NOT_COMPATIBILITY_PROOF | `solutions-catalog.csv`, `solutions-evidence.md`, `knowledge-report.md`, `evals-report.md` | Exact observed upstreams, historical seams; no install/call |
| F06 | `06-ENTERPRISE-AGENT-COMPARATIVE-RESEARCH.md` | 1762 | `409e76d12b5f680c9dedd66cec1b2a9c34fa5830183aa379af3ea840a0478c0f` | L2_42_EVIDENCE_ROWS | `enterprise-practices.md`, `enterprise-evidence.csv`, `four-contours.md` | Vendor metrics not Nox uplift; proprietary internals UNKNOWN |
| F07 | `07-OPEN-WORLD-COMPETENCE-GRAPH.md` | 1992 | `9307c296c2bb9d41aab281a1ca601f2654e92098c6d0860076995f5747acc3ca` | PROPOSED_GRAPH_NOT_RUN | `four-contours.md`, `knowledge-report.md`, `validation-program.md` | Machine skeleton supplied; T08 extension not performed |
| F08 | `08-CONTINUOUS-KNOWLEDGE-SYSTEM.md` | 2216 | `a5a319b6df8e56656c72d0b49fcd61c0e68177a5778d43e467e248f7e87ea684` | L2_DESIGN_NOT_RUN | `knowledge-report.md`, `solutions-research.zip`, `four-contours.md` | 68 source snapshots; actual corpus/ACL/quality/cost UNKNOWN |
| F09 | `09-AUTONOMOUS-TOOL-ACQUISITION.md` | 2197 | `25a55b4678e921f204ec1143a6b6dcb2c088e74dc4cc7cb318386032b5b4d684` | PROTOCOL_DESIGN_NOT_RUN | `four-contours.md`, `RANKED-ACTIONABLE-SHORTLIST.md`, `opencode-tickets.md` | No acquisition/install/call/revoke; owner gates required |
| F10 | `10-EXECUTION-STRATEGY-INTELLIGENCE.md` | 1921 | `d37c7eb57833ef82d857c7b836b00fcb6e266faab6a1c4babed3fc067a5ad90c` | DESIGN_NO_MEASURED_WINNER | `four-contours.md`, `evals-report.md`, `validation-program.md` | No equal-task route benchmark; cost/uplift UNKNOWN |
| F11 | `11-LEARNING-META-INTELLIGENCE.md` | 1931 | `8221e307ef1bcc1c43b865049109055225c7f81082f3f42649094a18df7e3aae` | DESIGN_NO_LEARNING_CLAIM | `four-contours.md`, `knowledge-report.md`, `validation-program.md` | No transfer/self-improvement evidence |
| F12 | `12-DOMAIN-CAPABILITY-PACKS.md` | 2101 | `1762 bytes; see MANIFEST-SHA256.txt` | PROPOSED_NO_ACCEPTED_PACK | `knowledge-report.md`, `validation-program.md`, `solutions-catalog.csv` | No ready/accepted pack; domain/expert/oracle owner required |
| F13 | `13-BUILD-BUY-REUSE-MATRIX.csv` | 49978 | `2e2c7a3b83a049f3f4b3e051026f7627a65aefc082f8011fab23708e02ef9c72` | 32_CANDIDATES_A_H_L1_L2 | `solutions-catalog.csv`, `solutions-research.zip` | Significant candidates, not all 4504; costs UNKNOWN |
| F14 | `14-R2-ACCEPTANCE-AND-BENCHMARKS.md` | 2325 | `c9777a15a4f9f3ad1f7e62ebba80f43a0a8202497e94645a2220c05068f0945e` | PROGRAM_COMPLETE_ALL_TESTS_NOT_RUN | `validation-program.md`, `test-matrix.csv`, `validation-checkpoint.md` | TR/T/G designed; no direct-Nox execution or acceptance |
| F15 | `15-OPENCODE-EXECUTION-PACK` | 25780 | `6f5e75ed156b645e8a2627404d3c41d1aaa70415a99cda77fff08b2e96bbb497` | 12_TICKETS_PLANNED_NOT_IMPLEMENTED | `opencode-tickets.md` | No code changes; owner authorization and fresh callsite mapping required |
| F16 | `16-FASTEST-SAFE-PATH-TO-R2.md` | 2168 | `9b745e8ef21bb0736a3e27d02218eba88b42c5da64d5b97f30d9b3118f0a579c` | PATH_DESIGNED_NOT_PROVEN | `FASTEST-SAFE-INTEGRATION-PATH.md`, `solutions-shortlist.md`, `opencode-tickets.md` | G0-G5 order; calendar/cost/current feasibility UNKNOWN |
| F17 | `17-SOURCE-AND-EVIDENCE-LEDGER.jsonl` | 4360381 | `ffb089d277d2527a28bdc500742cc63cf285d37dfd43f62d26b932de59242acb` | 4556_LEDGER_RECORDS_L1_L2 | `catalog-4504.csv`, `enterprise-evidence.csv`, `solutions-research.zip`, `source-baseline.md` | 4504 raw + 42 enterprise + 7 package + 3 archive manifests; not runtime ledger |
| F18 | `18-OWNER-DECISIONS-ONLY.md` | 2182 | `490f23c8991bf52c0cf36df9c67439ed1735d29b5f35a0e730e2d5e0577aad7e` | DECISIONS_ENUMERATED_AWAITING_OWNER | `validation-program.md`, `opencode-tickets.md`, `CRITICAL-QUESTIONS.md` | No owner approvals obtained by synthesis |

Для F15 SHA-256 — deterministic digest sorted relative-path+file-hash list; bytes — сумма файлов каталога. Индивидуальные hashes включены в `SHA256SUMS`.

## Machine proof

`DELIVERY-MANIFEST.json` — полная машинная форма, включая каждый supporting artifact. `FINAL-VALIDATION.json` = PASS только для artifact structure/readback/hash/evidence refs: 18 families; 4504 unique raw records (1331+3173), raw equality/status/NEXT_TEST; 32 expanded/matrix rows; 12 T rows; 4556 ledger records; zip SHA-256 `5745cbfe…216f`; 68 knowledge и 96 eval snapshots; exact Mastra 1.82.0 tarball SHA-512; 42 enterprise source hashes. Это не Nox/L3/L4 tests.

## Фактические ограничения публикации

- Нет current Nox fresh source/HEAD/lock/call graph/receipts; F02 остаётся BLOCKED_UNKNOWN_CURRENT.
- Нет реализации, installs, live calls, G/T, independent L3/L4, transfer/security proof или R2 acceptance.
- 4504 structurally complete, но per-row upstream L2+ incomplete; expanded registry 32 candidates не exhaustive universe.
- Полный TCO/calendar/uplift UNKNOWN; owner gates не получены.
- Причина historical SOURCE_HASH_MISMATCH и archive bytes UNKNOWN.

Resume: `resume.md`; сводка: `NOX-R2-RESEARCH-REPORT.md`; разделы: `SECTIONS-0-22-AUDIT.md`; критические вопросы: `CRITICAL-QUESTIONS.md`.
