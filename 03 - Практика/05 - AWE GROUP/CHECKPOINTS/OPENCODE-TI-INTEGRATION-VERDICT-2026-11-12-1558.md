# OpenCode Tool Intelligence v2 integration verdict audit — 2026-11-12

**Evidence cut-off:** Session Recorder timeline `2026-11-12/12-57/part0000.txt` and `12-58/part0000.txt` (UTC). OpenCode `session.execution.succeeded` at **12:58:01 UTC = 15:58:01 Moscow**. GitHub Observer status 13:10 UTC. Local WSL not directly accessible to reviewer.

**Actually implemented:**
- Copied source-only Manus v2 Git clone from `/home/nox/awe-tool-intelligence-v2-review` into `/home/nox/awe-group-cleanroom-20261112/ti-service`.
- Started isolated PostgreSQL **18** as `nox` on port **5448**, data dir `/tmp/opencode/ti-pgdata`, not affecting installed PG 18/main:5432. Applied five migrations. This is **NOT** restored v2 canonical backup.
- Ingested **12 source-derived resources**, NOT the original **3415** records. No approved executables. All imported entries DISCOVERED.
- Launched read-only FastAPI server localhost:8871; `/health` returned `{"status":"ok","database":"reachable","deployment_claim":false}`. Catalog search returned real records.
- Created `src/tools/ti-search.ts`, registered in `src/tools/index.ts`, updated `src/agents/head-agent.ts`. TypeScript `npx tsc --noEmit` succeeded after fixes.
- Created `src/tests/ti-integration.ts`; integration logged 5/5 passing checks. Direct query `browser automation` returned **Activepieces, Papermorph**; Head Agent with cloud LLM issued **three ti_search calls**, reported Beautiful Soup, Activepieces, Papermorph all DISCOVERED/nonapproved; note semantic precision remains weak.
- Local cleanroom git commits `050ca8b` and `4888dad`, **not pushed** to `failm3/awe-group-runtime` (remote HEAD still `d5e9d857...` as checked). TI source tree copied wholesale into cleanroom.
- TI service runs via manually created local processes; persistence/autostart after WSL reboot not proven. Temporary `/tmp/opencode` PG state is not reliable durable deployment.
- Despite passing checks, not proved: actual UI, automated installation/invocation of a discovered tool, full v2 DB, supervised long-running service, independent blind QA, universal coding/design.

**Security issue**:
- OpenCode printed generated TI API/admin tokens and Postgres password and a pre-existing search provider secret into recorder events. Treat as exposed and rotate/revoke as appropriate, remove access from future logs. Do not include exact values in artifacts. Check logs/Git tracking; `.env` excluded from commit per observed git ignore.

**Minimal next work recommended**:
1. Reconcile source-only handoff vs canonical v2 backup and explicit requirement for lockfile: do not claim complete catalog if absent; request only location of already supplied full backup when necessary. Avoid destructive DB overwrites or reinstall.
2. Rotate exposed credentials safely before production; never print secret values.
3. Bring up existing **AWE operator UI**, ideally compatible Mastra Studio if project supports, otherwise existing AWE frontend. Prove actual Head chat tool invocation and screenshot. Not OpenCode Web UI and not custom dashboard.
4. Run one capability-probing Head mission for professional Russian product portfolio: inspect actual frontend/browser/screenshot/visual QA options, perform one safe browser screenshot smoke-test, describe missing capabilities with evidence; no full portfolio yet.
5. End task with URL, exact start/restart instructions, logs and tests, costs, Git commit and explicit push/backup status. No new framework, unbounded autonomous modification or changing acceptance criteria.

**Supporting URLs**:
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/12-57/part0000.txt
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/12-58/part0000.txt
- https://github.com/failm3/awe-group-runtime/issues/11
- https://github.com/failm3/awe-group-runtime/issues/12
