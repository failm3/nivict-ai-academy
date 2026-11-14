# 18 критических вопросов — консолидированные ответы

**Статус:** desk research/design synthesis; current Nox UNKNOWN, T01–T12 NOT_RUN.

| ID | Вопрос | Ответ и граница | Доказательства / NEXT_TEST |
|---|---|---|---|
| CQ01 | Current wired/invoked/independent accepted | UNKNOWN. Historical baseline 68cc0ee и retained 39/39/13/13 не current proof. | source-baseline.md U-01–U-04; 02 audit |
| CQ02 | Почему late browser PASS не accepted | Mission осталась PAUSED: 600111/600000 ms, repair=2, aborted intent; late PASS относится к new tree, не old epoch/terminal. | source-baseline.md §6; validation-program §3.4 |
| CQ03 | Доказанный bottleneck | Не доказан current. Candidate hypotheses: candidate identity/coverage, route, model/context/provider, dependency, QA. Discriminating test: one-variable paired equal-budget direct-Nox runs после G0. | validation-program §3.5; test-matrix T11 |
| CQ04 | Самый limiting accepted-mission gap | G0 current candidate/full evidence/terminal. Затем G1 granted ToolSearch; external component не заменяет G0. | opencode-tickets OC-01–06 |
| CQ05 | Installed Mastra | Historical @mastra/core 1.82.0; exact tarball SHA-512 проверен solutions workstream, но current installation UNKNOWN. Falsifying smoke: fresh lock+typings+minimal processor call. | solutions-research.zip:sources/mastra/manifest.json; SOL-002 |
| CQ06 | Safe acquisition | Protocol documented, not run: owner approval → exact source/digest/license → sandbox/pin/register/least grant → one read-only call → independent QA → revoke/reconcile. | 09-AUTONOMOUS-TOOL-ACQUISITION.md; T03 |
| CQ07 | Citations/rights/ACL | KnowledgeRecord contract documented; actual corpus/tenant quality UNKNOWN. NEXT_TEST T04 false/stale/contradictory/retracted/unlicensed/cross-tenant. | 08-CONTINUOUS-KNOWLEDGE-SYSTEM.md; T04 |
| CQ08 | Open-world bounded scope | Graph primitives and expert/no-safe-scope BLOCKED specified; graph extension NOT_RUN. | 07-OPEN-WORLD-COMPETENCE-GRAPH.md; T08 |
| CQ09 | Knowledge vs skill/tool/strategy/runtime learning | Distinct assets/authority/eval specified. Transfer only via changed+held-out fresh-agent paired evidence; none run. | 11-LEARNING-META-INTELLIGENCE.md; T05 |
| CQ10 | Route selection | Deterministic/script/API/bot/single/team/hybrid/BLOCKED matrix documented; no measured winner. | 10-EXECUTION-STRATEGY-INTELLIGENCE.md; T01/T07/T11 |
| CQ11 | Failure/no-progress/recovery | Cumulative budget, no-progress cap, durable intents, quiescence and UNKNOWN reconciliation designed; real interruption NOT_RUN. | validation-program G0/G4; T10 |
| CQ12 | Minimum footprint | Fresh read → OC-01–05 G0 → native ToolSearch → one adapter → one pack → route/ledger → direct T12. Effort/calendar UNKNOWN. | 16-FASTEST-SAFE-PATH-TO-R2.md; OC-01–12 |
| CQ13 | Truncation/candidate race/old receipt | OC-01–03: canonical nested path, CandidateEpoch complete binary manifest, write fence, preterminal revalidation; no self-approval. Tests NOT_RUN. | opencode-tickets OC-01–03; G0 |
| CQ14 | Expiry/revocation/sharing | Version/digest/rights/ACL/expiry/revoke and rebuildable derived indexes specified; enforcement UNKNOWN. | 08,09,11; T03–T05/T09 |
| CQ15 | Accepted-outcome economics | UNKNOWN. 337014 tokens five completed calls + sixth 104613 outcome UNKNOWN ≠ total/bill. Reconcile full ledger+invoice; separate research/build/run/QA/maintenance/failures. | source-baseline U-05/U-17; OC-05 |
| CQ16 | Overfit-resistant T01–T12 | Frozen fixtures/hidden variants/oracles/negatives designed; execution coverage zero. Owner freezes before measurement. | 14-R2-ACCEPTANCE-AND-BENCHMARKS.md; test-matrix.csv |
| CQ17 | Owner blockers | Current read, ticket authority, exact packages, domain/oracles/experts, budgets, accounts/OAuth/secrets/egress, harmless effects, reviewer/release scope. | 18-OWNER-DECISIONS-ONLY.md |
| CQ18 | Что доказательно defer | R2.x additional domains/transfer/Windows/visual standards; R3 generalized professions/continuous learning/regulated/self-modification/fine-tuning. No evidence justifies building them before bounded R2. | validation-program §2; four-contours §8 |
