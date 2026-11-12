# AWE-READINESS-01 — independent evidence review, 12 November 2026

Sources: OpenCode Session Recorder https://github.com/failm3/awe-opencode-recordings/tree/main/timeline/2026-11-12/14-20 and 14-22 (UTC), earlier 13-41, 13-48, 14-11; GitHub runtime repository latest main checked 2026-11-12.

## Outcome
- Third simplified mission ID `61e8f64f-595d-4bf2-ba7f-a9dd07d50745` recorded a completed runtime lifecycle; Head plan 3 delegations, devops/researcher in parallel, writer report, QA score sequence 4 -> 5 -> 7, final status completed.
- Screenshot PNG at `.awe-data/artifacts/61e8f64f-595d-4bf2-ba7f-a9dd07d50745/screenshot.png`, 339260 bytes, 1280x720. Created by AWE devops using a PREPARED shell wrapper `scripts/awe-screenshot.sh`. It proves AWE invoked an allowed shell tool, NOT Playwright MCP agent use or autonomous acquisition of capability. Direct initial screenshot and wrapper were prepared/debugged by OpenCode beforehand.
- TI researcher searches reportedly executed, but user-visible saved `awe-browser-automation-test-report.md` continues to say `Pending transcription of the researcher ti_search result set` for BOTH sections. The report even notes data-propagation gap and `passes subject to filling Section 2`. Therefore QA score 7 PASS is NOT a sound acceptance of all mission criteria. The underlying researcher payload/individual tool calls were not independently checked in this review; the integration of TI search had passed an earlier standalone test.
- Earlier broad missions `974efed1-79c2-4ba2-b585-f30b7c7b738b` and `8ef7b67f-c03e-4571-a885-840d71904e03` were interrupted by 10/15-minute shell timeout, left `running` in stored JSON despite no executing process, and were not successfully resumed. This is concrete lifecycle/recovery gap.
- To obtain a final PASS, OpenCode changed to much narrower third mission explicitly requesting a pre-built screenshot wrapper (original broad mission called for independent capability assessment); important to distinguish bounded proof from original full readiness test.
- QA not proven blind/independent from runtime, and pass threshold at 6 with score-only gate is inadequate: acceptance criteria need immutable and per-critical-condition enforcement.
- Static `selectModelForRole` role mapping was reported for `claude-opus-5-5`, `kimi-k3.1-pro`, `deepseek-v4-flash`, `claude-sonnet-5-5`. No per-call model ledger observed from local runtime; dynamic capability optimization not proven.
- Dynamic role delegation with parallel tasks proven, but dynamically generated recursive nested agents and reuse/resume, permission inheritance and branch cancellation NOT PROVEN.
- Local commits: `050ca8b`, `4888dad`, `9eb422b`. Remote `failm3/awe-group-runtime` main as checked stayed `d5e9d857dbdeb8f31f9a798b10b5af4af639dbda`. No push and no repo readback on these local code changes. Screenshot binary not on remote and only visible through recorder readback/metadata, not independently opened here.
- Browser dependencies installed via local extracted .deb to `.chromium-deps`, non-portable without those libs; TI DB stored under `/tmp/opencode` and is not durable across restarts.
- Previously exposed tokens in recorder logs remain security issue, despite .env not tracked by git.
- No owner UI, independent autonomous development, full TI catalog restore, supervised process restart proven.

## Recommended NEXT (do not repeat months of infrastructure)
1. Fix acceptance gating: independent immutable original owner criteria, critical per-condition check, enforce no PASS with pending placeholder or missing TI result, bind artifacts to evidence and explicit scope. Add a regression with a deliberately incomplete report; it MUST FAIL.
2. Fix interrupted mission semantics: on timeout mark INTERRUPTED/UNKNOWN not lingering RUNNING; demonstrate one deterministic resume from checkpoint, do not restart duplicate work silently.
3. Run one small mission without predefining exact shell script, including retrieval of TI results into final artifact, one real browser tool (MCP preferable), evidence, and true independent QA. Set realistic deadline and tool spending cap.
4. Safely rotate leaked credentials, prevent recorder exposure, make local source snapshot auditable/PR, isolate working TI PG data from volatile /tmp.
5. Only then progress to broader NIVICT professional design and owner UI. Do not change approved original owner mission's acceptance criteria.

**Verdict:** bounded execution proof = PASS for screenshot/delegation; AWE-READINESS-01 overall = PARTIAL, not OWNER_ACCEPTED. Reviewer had access to exported GitHub logs, not direct WSL live checkout and full screenshot binary.

## Sources
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/14-20/part0000.txt
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/14-22/part0000.txt
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/14-11/part0000.txt
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/13-48/part0000.txt
