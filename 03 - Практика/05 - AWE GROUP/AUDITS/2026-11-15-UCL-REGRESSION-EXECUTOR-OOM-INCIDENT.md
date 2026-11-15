# AWE GROUP — incident evidence: executor cgroup OOM during UCL regression
Date: 2026-11-15 20:09 Moscow. Status: CONFIRMED OOM EVENTS; USER-REPORTED TERMINAL EXITS NOT YET CAUSALLY ATTRIBUTED. Source: user-supplied `NOX-DIAGNOSTICS.txt` inspected in ChatGPT.

## Direct observations
- WSL2 Linux 6.18.58.1; up 2h35m at time of snapshot, available system memory 14 GiB of 15 GiB, swap 4 GiB entirely free, root disk 2% used, load averages near zero.
- Root cgroup `memory.events`: max=92, oom=4, oom_kill=18, oom_group_kill=4 (counters may aggregate across scopes).
- Kernel at 17:42:58 and 17:48:08-09: `Memory cgroup out of memory`, `constraint=CONSTRAINT_MEMCG`; killed `python3` and `bwrap` members inside transient user scopes `awe-exec-*.scope`; `memory.oom.group` set.
- OpenCode process PID 387 still alive at 20:09, elapsed 2:35; no proof that OpenCode itself crashed or WSL shut down.
- `/tmp/opencode/ucl-live-final.log` absent at snapshot. `/tmp/opencode/ucl-release-regression.log` and numerous suite-specific logs present, including `r1-resource-limits.log`, `ucl-bridge.log`, `r1-p1-lesson-comparison.log`. Mod times around 17:47-17:48.
- User reported Windows Terminal command exited 5 times, code 1 screenshot; previous UCL test log screenshot had QA FAIL: `Missing deliverable (image)`. Both require separate causal diagnosis.

## Critical caveat
Resource-limit regression tests may **deliberately** trigger cgroup OOM to verify fail-closed behavior. The OOM events alone DO NOT prove a production memory-sizing defect or explain all terminal exits. Inspect `r1-resource-limits.log`, main regression log, exact test process exit code, and live/current scope limits before changing any resource guard.

## Required bounded repair/verification path
- Inspect `/tmp/opencode/ucl-release-regression.log`, `/tmp/opencode/ucl-release-regression/r1-resource-limits.log`, bridge and QA logs; correlate timestamps, process parents/exit codes, expected negative tests and actual failures.
- Locate code/config creating `awe-exec-*.scope`, read effective `MemoryMax`/`MemoryHigh`/`MemorySwapMax` and parent cgroup settings. Determine whether memory limit is intentional, mis-sized, or a bug. Do not turn off sandbox, cgroups, QA or security checks.
- If a genuine defect exists, minimal isolated reversible patch to host-owned resource-budget and error handling with bounded test and regression. Preserve canonical R2 `bd3859a550a046c16454f44ddc2648c81318f14e`, no unapproved push/production changes. Distinguish OOM from QA missing image and shell wrapper exit code.
- Test both expected OOM negative path and representative real execution with appropriately justified finite memory budget; assert informative terminal status, clean lifecycle and no silent retries.
- Report factual root causes, fix hashes, check results, remaining risks and next continuation point for Cortex UCL integration. OpenCode Recorder appears stale after 04:08 UTC; observer `DATABASE_SCHEMA_UNSUPPORTED`, therefore no claims of seeing present session via these sources.

This is an incident checkpoint, not proof of deployed fix.
