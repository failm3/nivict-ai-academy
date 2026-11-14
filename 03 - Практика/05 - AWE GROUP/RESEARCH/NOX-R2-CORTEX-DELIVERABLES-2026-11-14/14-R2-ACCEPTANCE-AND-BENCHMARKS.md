# 14 — R2 acceptance and benchmarks

**Статус:** `PROGRAM_COMPLETE_AS_DESIGN / ALL_TESTS_NOT_RUN / R2_NOT_ACCEPTED`. Нормативные полные протоколы: `validation-program.md` (TR/evidence/G0–G5/resources/rollback) и `test-matrix.csv` (12 complete T01–T12 rows). Здесь не дублируются выдуманные результаты.

## Frozen acceptance

Owner Approved Spec, direct production Nox, independent reviewer, hidden frozen variants/oracle, exact CandidateEpoch+complete binary EvidenceBundle, sealed candidate during QA, current admission/grants, all criteria FINISHED/PASS, no unresolved intent/effect/repair, cumulative budget, durable terminal readback. Product verdict и mission terminal отдельны; FAILED/PAUSED/BLOCKED/UNKNOWN не переименовываются; late PASS не retroactive accept.

| Test | Proof target | Actual status |
|---|---|---|
| T01 | deterministic no-LLM after routing | NOT_RUN |
| T02 | granted ready tool/schema/search-load-active | NOT_RUN |
| T03 | novel pinned tool safe acquisition | NOT_RUN |
| T04 | unknown source knowledge+citations/rights | NOT_RUN |
| T05 | skill changed+held-out fresh transfer | NOT_RUN |
| T06 | professional web function+visual+accessibility | NOT_RUN |
| T07 | bot/script/workflow choice+artifact | NOT_RUN |
| T08 | bounded unknown profession graph extension | NOT_RUN |
| T09 | adversarial injection without authority/effect | NOT_RUN |
| T10 | real interruption/recovery/budget/no duplicate | NOT_RUN |
| T11 | equal-budget route efficiency/no-benefit | NOT_RUN |
| T12 | direct novel Nox without OpenCode solver control | NOT_RUN |

G0→G5 strict evidence gates; early PoC не final acceptance. TR07 negatives, TR09 expert signoff обязательны. Metrics accepted rate, unsafe effects=0, coverage=100%, stale accept=0, duplicates/orphans=0, repairs/time/tokens/full cost или UNKNOWN. Owner может изменить scope только новой versioned spec, failed history сохранить.

Rollback rehearsal каждого gate; evidence append-only. Final report verdict `R2_ACCEPTED(scope)` только после complete direct-Nox independent evidence; сейчас `R2_NOT_ACCEPTED`. Tickets OC-01–12, source checkpoint `validation-checkpoint.md`.
