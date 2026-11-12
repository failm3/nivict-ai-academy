# AWE GROUP — independent OpenCode status at 2026-11-12 ~08:18 MSK

Sources: private GitHub session recorder `failm3/awe-opencode-recordings` minute folders `timeline/2026-11-12/05-11` through `05-18` UTC. This is analysis of recorded data, not direct host inspection.

## Confirmed engineering activities
- Two OpenCode development subagents finished their tasks; edits to Tavily search, model role routing, QA tools, agent memory, mission CLI and error handling.
- `npx tsc --noEmit` resulted `TYPECHECK_OK` twice.
- Local Git commit `56d8117` recorded 23 files changed / 9706 insertions / 138 deletions, includes imported 4504 catalog files; this is only **local**, not a verified code push.
- Direct Tavily HTTP smoke test returned 3 results. An initial attempted import of the TS web_search module via node -e failed with module resolution error. Later targeted startup test inside project: role routing researcher -> claude-haiku-4-5, coder -> kimi-k2.7-code, analyst -> deepseek-v4-flash; agent creation OK; memory creation OK; Tavily web_search returns success=true with 0 results for that query. No demonstrated verified HH vacancies. Not all 50 Router.Cheap models have been live-tested; role selection is a mapping rather than proven live calls to each configured model.
- AWE CLI CAREER-01 really launched at 05:11:45Z, mission ID `8d95c4ac-47ac-40df-b8b9-b3401bccf36c`; Head planned 3 delegations. Researcher failed in 132ms. Analyst hung 4+min with no additional mission log lines or artifacts; `running` status became stale when AWE process exited unexpectedly. OpenCode observed the process exit and is debugging it, not a successful outcome.
- Important correctness issue: CAREER-01 mission was hard-coded to `senior software developer / AI engineer`; owner is primarily product designer/product marketing. Must use verified resume and accurate role preferences before the next real run.
- OpenCode stated only owner dependency: authenticated HH.ru account to actually submit job applications, optional for research and drafts. Independent recommendation: prepare verified CV/profile, target roles, constraints, portfolio, explicit sending authorization before any real application; separate email only if a later integration truly needs it.
- Recorder itself is actively publishing; latest reviewed commit `76262d7046` 2026-11-12 05:18:44Z. Keep Recorder outside engineering scope.

## Status
- Router.Cheap direct API access for Claude Opus 5.5, GPT-6 Astra, Kimi K3.1 Pro already confirmed by previous owner terminal tests; this log did NOT establish live success for 50 models or dynamic runtime model invocation.
- Tavily direct call yes; inside AWE tool startup test returns 0 results; genuine search on HH and actual research result not proven.
- Catalog 4504 imported as metadata, not installed or integrated as 4504 executable tools.
- Local TypeScript typecheck passes; this is not autonomous mission QA.
- First genuine live user deliverable: NOT YET.
