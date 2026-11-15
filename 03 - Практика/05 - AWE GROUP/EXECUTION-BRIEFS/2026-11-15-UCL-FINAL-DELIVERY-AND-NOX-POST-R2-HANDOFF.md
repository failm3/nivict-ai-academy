# AWE GROUP — UCL final delivery and post-R2 OpenCode handoff
**Date:** 2026-11-15. **Purpose:** factual context, not an instruction to apply any patch without independent review.

## Current Nox
- Local OpenCode `r1/dev` checkpoint: `bd3859a550a046c16454f44ddc2648c81318f14e` (`R2: verify autonomous generalization with durable evidence`).
- Evidence reported and command-verified in recorder: 43/43 offline suites, 22/22 fresh live host checks, 23/23 post-run integrity checks; typecheck/build pass. See [recorded final result](https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-15/04-08/part0000.txt).
- This is a **local** Git commit; **not pushed** into the public runtime repo.
- Owner's **original** six R2 acceptance criteria are broader than the six checks in the local live-run report. Fresh-agent transfer of stored useful experience on a *new* task against memory-off has not been established by the recorded final report. See [independent audit](https://github.com/failm3/nivict-ai-academy/blob/main/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/AUDITS/2026-11-15-R2-LOCAL-CLOSURE-INDEPENDENT-REVIEW.md).

## Cortex final delivered archive
- File: `ucl-nox-r2-final.tar.gz`, received as a ChatGPT conversation attachment **only**. It is **NOT proven to exist on the user's Windows / WSL machine or in OpenCode**. Ensure local OpenCode has been given this exact archive before starting integration. Do not assume it can read ChatGPT attachments or the GitHub repo holds the archive.
- Verified whole-archive SHA-256: `1a5c8638007dc64ee40595a195eb9401f824e60e9da88b72c1dce7d8888d2bd7`.
- Reviewed via safe archive inspection (no archive code executed): 14 regular files, 13 entries in `MANIFEST.sha256`, **13/13 hash matches**, no symlinks, absolute-path or parent-traversal members.
- `ucl-nox-r2-delivery/nox-r2-ucl-bridge.patch`: SHA-256 `878af216b8e3d978b530d2aa53b41363c9f905e4a76346c13fbab4c669dccaee`; `optional-acquisition-wiring.patch`: SHA-256 `fb963e0122db3ebb038d397c2a3d2b48b39562160e38c9681f99d316f8b83dcf`; prebuilt index sha256 `ef2bee5e689d484b86c2dbff0138347cb5f6e1a5f9a4dcd45c58aef51e39e1be`.
- Included files: `HANDOVER-RU.md`, `README.md`, `COMPATIBILITY-REPORT.md`, `INTEGRATION-R2.md`, `INDEPENDENT-QA-R2.md`, `VERIFICATION-OF-FIXES.md`, 2 patches, 4504-row catalog data and 4466-entity SQLite index.
- Core UCL: 12 library modules, builder-reported 56/56; one proposed Nox advisory Mastra tool `capability_library`, with explicit deny-by-default semantics: candidates are `UNVETTED`, `approved:false`, `execution_authority:false`.
- QA reported `PASS_WITH_FINDINGS` after 3 rounds. F1 lazy-import of node:sqlite with disabled flag, F2 truly read-only index opening, F7 host-only hazardous opt-in, F10 fail-loudly when test data missing, F12 readonly SQLite index avoiding WAL sidecars all resolved/confirmed in delivered report. Unresolved but documented: F5, F6, F8, F9; F11 opt-in acquisition probe wiring semantics.
- Cortex tested against **older snapshot** `68cc0ee20a25991ea275512e20ac521cc8f8234b`, captured 2026-11-15 04:01 UTC, with uncommitted modifications; **not** against `bd3859a`.
- Under Cortex's snapshot environment, Nox suite 33 passed / 11 failed with same failure list before/after. QA observed hardcoded `/tmp/opencode` assumption in six suites (portability defect). Of remaining 11 failures **7 are confirmed environmental, 4 probable/unproven**: `r0-closure-adapters`, `r0-reqa-adapters`, `r1-parallel-artifacts`, `r1-shell-isolation`. Some prose in the package calls all 11 environmental; the more precise QA correction supersedes that claim.
- `capability_library` visibility in planning is *not* real-model execution proof. Cortex did not validate planner adoption via an actual model or on Node 24; adapter integration requires verification on the latest R2 commit.
- F11: optional `mission-manager.ts` one-line wiring allows the acquisition probe to consult UCL, but changes behavior for allowed-tools set exactly `[save_artifact, capability_library]`; the original probe blocked where now it delegates. No widening of tool grants was observed, but this is still a behavioral change requiring explicit engineering assessment.

## Owner-approved engineering intent
- Owner's goal: universal autonomous digital employee, competent at novel tasks, dynamic specialist teams, model/tool choice, safe capability acquisition, independently verified work, transferable experience, reusable verified agent blueprints, recoverable and truthful operation.
- Priority **EXTEND NOX / REUSE BEFORE REBUILD / GENERALITY BEFORE WORKFLOW COUNT**; do not invent profession-specific workflows; do not install a second orchestration, permission or memory control plane without compelling reason.
- Owner wants OpenCode to independently inspect **the actual final archive and current local R2 code** and make its own technically defensible decision: if beneficial, compatible and reversible within existing permissions/budget, independently implement and validate **only in isolated branch/worktree**, commit locally and report; if risky, permission-dependent or not verifiable, stop and ask owner.
- No unconditional green light for `optional-acquisition-wiring.patch` (F11), automatic production integration, base-directory changes, additional credentials, spend-cap expansion, publication/push, or irreversible external actions.
- Tests must include off-by-default, auth/grant boundary, malformed/foreign SQLite, catalogue freshness, full regression *relative to same clean local base*, independent QA, rollback, and if budget/permissions permit measured real-model routing; failures must not be mislabeled environmental without diagnosis.
- Keep R2 canonical commit and existing worktree safe. Snapshot/patch applicability alone must never be treated as proof of live R2 compatibility.
- Once accepted, stop feature growth and prepare R3; UCL integration is a distinct optional evolution workstream, not a rewrite of R2.

## Integrity and provenance
This handoff was authored after directly inspecting the **user-provided** archive in an isolated ChatGPT runtime, independently verifying hashes and reading delivery docs. The package is **not** published here; a recipient who needs the actual code must have the separate 4.2 MB archive. Neither this handoff nor Cortex's self-report is proof of the complete live integration.
