# AWE GROUP — OpenCode interim engineering report

**Cutoff:** 2026-11-12 09:07 MSK / 06:07 UTC.
**Basis:** independently examined private GitHub recorder `failm3/awe-opencode-recordings`, timeline 2026-11-12 05:07–06:07 UTC; existing GitHub `failm3/awe-group-runtime`; no direct host access or independent rerun of local executables.
**Overall:** tangible engineering progress, but no owner-accepted complete CAREER-01 result.

## Verified engineering progress
- OpenCode launched two real development subagents (A/B), both completed changes.
- AWE cleanroom v0.3 implemented/built Tavily search integration, mission command `career`, role-to-model routing, QA agent, LibSQL memory initialisation, specialist creation and execution.
- `npx tsc --noEmit` repeatedly returned `TYPECHECK_OK`; this is static checking, not full mission acceptance.
- Local cleanroom git commit IDs observed in shell logs: `56d8117` (v0.3 baseline), `995a4ba` (verified model routes), `ba60ea3` (QA artifact context), `0366107` (mission ID/artifact requirement), `93169e4` (auto-save and changed CAREER criteria), `c6b25d8` (passing prior results and artifact paths/deduplication), plus other intermediate commits. These have **not** been verified as pushed to a code repository.
- An initial researcher failed after 132ms owing to Router.Cheap model source incompatibility. Verified supported choices by local live checks: `claude-opus-5-5`, `claude-sonnet-5-5`, `gpt-6-astra`, `kimi-k3.1-pro`, `deepseek-v4-flash`. Unavailable for current source routing: `claude-haiku-4-5`, `claude-haiku-5-5`, `kimi-k2.7-code`. Role-based routing now uses supported substitutes. Dynamic per-task optimization beyond fixed role mapping not proven.
- Tavily direct API returned results; actual tool behavior tested after dotenv fix; HH search effectiveness limited by archived results and API restrictions.
- AWE Head generated 3–5 delegations in several launches. On one run two researchers really ran in parallel, succeeded, then Analyst and DevOps succeeded; Writer suffered a 435669ms LLM/API failure.
- Artifacts created: 11 hh.ru vacancy records, scored/ranked list, three/four cover letters, scoring rubric in some runs. These are real local files. Not all results are trustworthy/final.
- Some runs had no artifact registrations even after successful model completions; a fallback auto-save was added. Duplicate filenames were identified and listArtifact de-duplication fixed.
- QA initially had tool invocation/JSON parsing bugs, subsequently changed to review textual contents read by MissionManager; QA now produces structured judgments. Direct external verification by QA remains limited; no comprehensive live external validation confirmed.
- Some artifacts were truncated before QA; repaired context limits/order. A writer used stale context and generated letters for companies not in the current vacancy list; an explicit prior-result/artifact-path handoff was implemented.

## CAREER-01 most recent statuses
- Earlier 2026-11-12 ~05:39 UTC run ID `3bcf9d35-23a2-490f-8c4d-29b3f168bb6b`: 11 vacancies, only 1 marked active, 10 archived; all `url_verified=true` **as stated by generated data**, not equivalent to independently verified active postings. Writer generated letters, some mismatched the current ranking; duplicate artifact names.
- QA progression in this run 2 → 4 → 5 → 6, target ≥7. Final observed at 2026-11-12 06:03:27 UTC: `QA score=6, passed=false; mission status=failed`.
- A targeted QA re-run from existing artifacts at ~06:05 returned score 5 and identified the letters/research mismatch; illustrates possible QA scoring variability.
- After fix `c6b25d8`, OpenCode started a new AWE mission around 06:06 UTC (ID `3e1a4bff-f5b3-4c41-83bc-689e0c468953`). Journal through 06:07 does NOT prove this run completed.

## Critical acceptance gaps
1. **Candidate profile wrong:** CAREER-01 is still defined as Senior Software Developer / AI Engineer; owner's professional target is product design/product marketing. Job search and letters therefore do not meet actual user requirements. Some letter content may infer unverified years of work; correct via owner-confirmed CV before any real submission.
2. **Acceptance regression:** OpenCode relaxed criteria to include archived hh.ru vacancies after the active-only requirement proved hard. This change was not approved by the owner and does not make archived posts actionable. Restore live active-only criterion for actionable shortlist; archive records may serve historical research separately.
3. **No verified submission:** No HH account authorization, successful application or confirmed external action.
4. **No passing independent mission QA:** last completed run failed score 6 (<7), and evidence-based checks remain limited.
5. **Model routing is role-based configured mapping:** actual autonomous choice among all available models and tools, full capability discovery, universal agent test outside HH not proven.
6. **Recovery and reliability:** earlier AWE process exited while mission status remained `running`; unexpected exits and durable correct status need robust testing.
7. **Source backup:** Session Recorder and Observer remote logs are separate from publishing cleanroom source code. Latest verified runtime repository commits were dated Nov 8 and Nov 11, not current cleanroom code.

## Owner actions
- Prepare current HH résumé/profile, product designer / UX/UI / product marketing search preferences, salary/location/format, portfolio and factual accomplishments.
- HH authenticated access and separate explicit rules for application submission are only required when safe automatic application is ready; no passwords/codes in chat.
- No evidence yet that extra email or paid external plugins are required. Existing Router.Cheap paid usage was authorized.

## Decision
The system has reached **LIVE execution with multi-agent behavior and real local artifacts**, but is **NOT** at owner acceptance as a reliable autonomous mission executor. Prioritize truthful candidate profile, verifiable currently active job data, strict independent QA, robust context/artifact transfer and mission-state correctness before external action.

## Grounding
- https://github.com/failm3/awe-opencode-recordings/blob/main/LATEST.md
- https://github.com/failm3/awe-opencode-recordings/tree/main/timeline/2026-11-12/05-54
- https://github.com/failm3/awe-opencode-recordings/tree/main/timeline/2026-11-12/06-04
- https://github.com/failm3/awe-opencode-recordings/tree/main/timeline/2026-11-12/06-05
- https://github.com/failm3/awe-opencode-recordings/tree/main/timeline/2026-11-12/06-06

**Limit:** source status is an observation window; no claims of ongoing activity after the cutoff.
