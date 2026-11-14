# Nox R2 — execution strategy, meta-intelligence and evaluation candidates

**Scope/date:** primary-source research observed 2026-11-14 UTC. **Status: L2 source/API/version/license vetting only.** No package was installed or executed; no Nox files were changed; no paid/provider test, external publication or R2 acceptance was performed.

## Decision first

1. **OSV-Scanner v2.7.1 — C READY_MADE_INTEGRATION.** Add later, after owner approval, as a read-only lockfile/SBOM check around `src/tools/` acquisition and the independent QA evidence bundle. It detects *known dependency vulnerabilities*, not malicious packages generally, exploitability universally, license correctness, or safety.
2. **axe-core v4.14.0 — D THIN_ADAPTER.** Add as a development-only QA check in the existing browser/Playwright path for the bounded T06 web slice. It is one oracle component, never a WCAG certificate or substitute for keyboard, screen-reader, visual and expert review.
3. **Promptfoo 0.125.1 — D THIN_ADAPTER.** Use outside the solver loop for frozen route/strategy fixtures, tool-call/trajectory assertions and repeated equal-budget comparisons (T02/T05/T09/T11). Start with replayed local evidence, not paid model generation or red-team scanning. Its configuration/code execution is trusted-code execution, not a sandbox.
4. **Langfuse JS v6.1.1 — D, conditional.** Only if actual Nox cannot already provide queryable traces linking spec → plan → model/tool calls → costs → oracle → terminal state. Use scoped `@langfuse/*` packages with client-side redaction and an owner-approved endpoint. Do not install the deprecated unscoped `langfuse` client.
5. **Inspect AI 0.3.289 — G REJECT_OR_DEFER for the first R2 slice.** Revisit only for a demonstrated need for a separate Python agent-evaluation/sandbox harness that Promptfoo plus existing Nox QA cannot satisfy. It is not a drop-in Nox oracle or an execution-strategy selector.
6. **Langfuse self-host v4.80.0 — E/G; defer.** Justified only when a managed endpoint is disallowed or local retention is required and operations capacity is approved. Web/worker/Postgres/ClickHouse/Redis/blob storage, backup, upgrades and tenant/security operations make this materially more than an SDK dependency.

**Fastest safe path:** first repair and bind Nox's existing current-candidate/terminal QA (G0), then independently measure existing execution. Add OSV-Scanner and axe-core as narrow deterministic preflight checks; add Promptfoo fixtures for route and regression comparisons. Add telemetry only after an actual trace-query gap is measured. None of these packages repairs G0, grants authority, chooses a safe strategy by itself, or supplies L4 uplift.

## Evidence boundary and Nox fit

The owner contract was recovered from the parent session after the initially supplied path was absent; its SHA-256 is `0767476e3da1599aaaa731d43397e01dc944c14247ec016ffae03c68cba1ce1f`. The authorized Nox path `/home/nox/awe-group-cleanroom-20261112` was absent in this sandbox. Therefore actual branch, HEAD, dirty state, Node/Python versions, current call graph, package presence, authorization and runtime compatibility are **UNKNOWN**. The integration locations below are *proposals derived from the owner brief*, not fresh code observations. The brief's historical `@playwright/test=1.49.1` is not a current compatibility finding.

For every implementation ticket: freeze the approved mission/spec, exact package and lock digest, fixture/oracle, resources and data policy before execution; run only in an owner-approved isolated development/QA environment; retain failed attempts; and bind results to the complete current candidate epoch. **UNKNOWN never means zero cost, safe, compatible, no vulnerabilities, or no benefit.**

## L2 release and supply-chain matrix

| Candidate | Repository HEAD observed via `git ls-remote` | Latest stable release page / resolved tag commit | Install/runtime evidence | License evidence |
|---|---|---|---|---|
| Promptfoo | `aaeebf25ea3a17e4f053f52ad5aedcc4551c43f8` | `0.125.1`, 2026-10-25, `8569e72ed6cf7737082a6042be8d925e40f9739d` | `promptfoo@0.125.1`; Node `>=22.22.0`; CLI and Node API | MIT in tagged package/LICENSE |
| Langfuse JS | `280e323c3d5c1408ef0c52e83fe03e70ceb7bcb6` | `v6.1.1`, 2026-11-02, peeled commit `7ba77b7c8517829b1e5dc2985de851fa3e6f89ec` | `@langfuse/tracing`, `@langfuse/otel`, optionally `@langfuse/client`, all `6.1.1`; Node `>=22`; OTel SDK 2.x line | MIT, including acknowledged PostHog-derived portions |
| Langfuse self-host | `48a31810e1c6e6a4a589b1eacc5eecc7960c9b87` | `v4.80.0`, 2026-11-13, `fd23d7e66992ae9e19eadcd3a7cf6421137cd076` | pinned Docker Compose image/configuration still requires digest review | MIT Expat outside listed `ee` trees; `ee` and third-party terms are separate |
| Inspect AI | `f72aaad97e8baad440e256bad542a075a83e427c` | `0.3.289`, 2026-11-10, `ad7dc3c94145438b352ca8c1c19b63adf85b56c6` | PyPI `inspect-ai==0.3.289`; Python `>=3.11` | MIT |
| axe-core | `d991e05ac6eb42df88f9e61c1679692534bb92e2` | `v4.14.0`, 2026-10-05, `e797173108eadfa4355fe06af331791734e1757f` | `axe-core@4.14.0`; browser script + `axe.run`; Node engine metadata `>=4` is not proof of Nox/Playwright fit | MPL-2.0 plus `LICENSE-3RD-PARTY.txt` |
| OSV-Scanner | `80fe50567a5d6e0ec408353e2ceacca1561b91be` | `v2.7.1`, 2026-11-09, peeled commit `02f96a40691c2d155fdda799af436e111231e365` | official release binaries for Linux/macOS/Windows; source install requires Go 1.26.2+ in tagged docs | Apache-2.0 |

HEAD and release are intentionally separate observations; HEAD is not an install recommendation. Exact package integrity and PyPI wheel hash are in `evals-candidates.json` and saved registry metadata. Verify artifacts/provenance again at acquisition time; a hash observed in metadata is not proof that a future downloaded artifact was verified.

## Candidate assessments and minimal tickets

### EVAL-01 — OSV-Scanner: dependency advisory gate (recommended)

**Official API/use.** `osv-scanner scan source --format json --lockfile=/path/to/package-lock.json` scans specified lockfiles; recursive source scans discover lockfiles/SBOMs/Git inputs. JSON is written to stdout and other output to stderr. Exit code `1` means vulnerabilities were found; infrastructure/parse failures must not be converted to “clean.” Release v2.7.1 specifically fixes npm lockfile entries with omitted `resolved` URLs, so an earlier scanner should not silently be substituted. [S-OSV-USE, S-OSV-OUT, S-OSV-REL]

**Proposed path:** a host-owned, read-only QA/acquisition helper around `src/tools/` and the evidence/QA boundary, never an agent-selected install or `osv-scanner fix`. Scan the exact immutable lockfile/SBOM and store scanner version, binary digest, input hash, OSV source/offline snapshot time, raw JSON, stderr and exit status in the evidence bundle.

**Minimum integration test (NOT_RUN):** one synthetic lockfile fixture with a frozen known advisory, one fixture with no known match, one malformed input and one unavailable/offline database. Independently precompute expected package/advisory identity. Assert vulnerable fixture → exit 1 + matching advisory; clean fixture → exit 0 + valid parse + nonempty scan metadata; malformed/unavailable → ERROR/UNKNOWN, never PASS. Add fixture with omitted npm `resolved` to protect the v2.7.1 behavior.

**Security/limitations:** network matching sends dependency queries unless a separately verified offline database is used. Offline freshness is explicit. `.gitignore` affects recursive discovery; explicit lockfiles are safer for acceptance. Do not enable experimental plugins/call analysis initially: Rust call analysis can execute dependency build scripts. Zero findings is only “no matched known advisory in this input/database snapshot,” not a secure/supply-chain-clean certificate. [S-OSV-USE, S-OSV-OFF]

**Rollback:** remove the QA check and exact binary/lock entry after preserving evidence; no Nox data migration or dependency auto-fix. Restoring an older vulnerable dependency is not rollback of product code. Revalidate at scanner/OSV snapshot changes.

### EVAL-02 — axe-core: bounded browser accessibility preflight (recommended)

**Official API/use.** Install as a development dependency, inject `axe.min.js` into the actual browser page and call `axe.run`. Results distinguish `violations`, `incomplete` (review required), `passes` and `inapplicable`. `runOnly` selects rules/tags; do not discard `incomplete`. [S-AXE-README, S-AXE-API]

**Proposed path:** a thin helper alongside `src/agents/web-qa.ts` / existing Playwright QA, invoked only against the immutable local candidate snapshot. Store URL/route, viewport/browser, axe version/hash, selected tags, results and screenshot/functional evidence under the same candidate epoch.

**Minimum integration test (NOT_RUN):** local static fixtures: (a) missing image alternative and unnamed button, (b) accessible corrected version, (c) a dynamic modal after it opens, and (d) a keyboard/focus case requiring human judgment. Run the declared WCAG tag set and verify known rule IDs on (a), no selected violations on (b), route/state coverage on (c), and retained `incomplete`/manual result on (d). Repeat at all owner-approved viewports/browsers. A wrong/stale candidate hash must block the verdict.

**Security/limitations:** real browser context is required for meaningful layout/contrast; upstream notes limited JSDOM support and color-contrast does not work there. Frame injection and `allowedOrigins` need review; do not use `<unsafe_all_origins>`. Upstream states automated detection averages **57% of WCAG issues** and `incomplete` requires manual review. **No violations is not WCAG conformance, full accessibility, professional design quality, or certification.** T06 still needs functional, responsive, keyboard, screen-reader/visual and qualified accessibility review as specified. [S-AXE-README, S-AXE-API]

**Rollback:** remove the dev-only script injection/check and pin; preserve old reports. No production bundle or user data migration is needed.

### EVAL-03 — Promptfoo: strategy and regression eval runner (recommended, constrained)

**Official API/use.** Promptfoo offers YAML/CLI and Node `evaluate()`; test cases combine inputs/providers/assertions. A custom JS/TS provider implements `id()` and `callApi()`; custom JavaScript assertions can inspect output, metadata and traces. CLI supports JSON/JSONL/JUnit outputs, `--no-cache`, `--no-write`, repetition and `--safe-mode`. The release package requires Node `>=22.22.0`. [S-PF-README, S-PF-PKG, S-PF-DOCS, S-PF-EXAMPLE]

**Proposed path:** a separate QA harness outside Nox's solver and product tree. A reviewed custom provider adapts the approved direct-Nox host harness only for later authorized live tests. Initial tests replay frozen, synthetic route/evidence JSON without any provider/model key. Emit Promptfoo results plus original Nox receipts; do not let Promptfoo mutate mission state or QA policy.

**Minimum integration test (NOT_RUN):** frozen fixtures for T02/T11: expected route (`deterministic | program/API | single | team | hybrid | blocked`), allowed/denied tools, expected schema and exact candidate epoch. Include ambiguous input that must BLOCK, denied-tool selection, stale epoch, over-budget result, and a no-benefit parallel route. Independently frozen oracle asserts route and safety fields, not mere output text. Run `--no-cache`; later repeated direct-Nox comparisons use equal input, authority, model/tool access, fresh context and wall/token budgets. Promptfoo PASS alone is not terminal mission acceptance.

**Security/limitations:** upstream states OSS has **no general sandbox** for adversarial content. Configs, scripts, providers and file callbacks can execute code; `--safe-mode` only rejects selected inline expressions and is explicitly not a sandbox. Use trusted reviewed configs in isolation, least-privilege/no secrets, restricted egress and no untrusted PR execution. Sharing, telemetry, remote generation/grading and configured providers are separate data paths; disable only documented paths and verify egress, not assumptions. Exports can contain active markup/formulas. Model-graded assertions are not independent professional oracles. [S-PF-SEC]

**Rollback:** remove the separate harness, provider adapter, exact dev dependency and CI invocation; preserve fixtures/results. No Nox runtime or stored mission migration.

### EVAL-04 — Langfuse JS SDK: conditional meta/ledger telemetry

**Official API/use.** Current v6 uses `@langfuse/tracing` (`startActiveObservation` / `startObservation`) and `LangfuseSpanProcessor` from `@langfuse/otel`; `@langfuse/client` covers prompts/datasets/scores. Initialize OpenTelemetry before application code and call `shutdown()` to flush short-lived processes. v6 requires Langfuse Cloud or self-host **v4.59.0+**; older servers stay on v5. The README warns OTel JS SDK 3.x is not yet supported and prescribes SDK 2.x. [S-LFJS-README, S-LF-DOCS]

**Proposed path:** optional instrumentation near model/tool invocation and ledger creation, linked to existing mission/spec/plan/candidate IDs—not a new orchestrator or source of truth. Default to metadata-only; omit prompt/output/artifact content and secrets unless separately approved. The authoritative Nox ledger remains local and durable even when export fails.

**Minimum integration test (NOT_RUN):** against an owner-approved local/test project, export one synthetic trace containing no real user content. Independently assert mission/spec/candidate IDs, model/tool names, timestamps, reported token counts, terminal status and unknown-cost semantics. Test export endpoint unavailable, shutdown/flush, retry/cancellation and malformed/unknown usage; Nox outcome must not be relabelled PASS and missing telemetry must not erase local evidence. Query back only after ingestion freshness is established. Redaction tests must prove secrets/PII never enter payloads.

**Security/limitations:** tracing changes data egress and retention. Client-side masking can occur before transmission; self-host server-side masking is EE, fails open by default, and raw events may temporarily land in blob storage. Use client-side omission/redaction regardless. Trace presence is not correct execution; reported tokens are not invoice dollars. [S-LF-MASK]

**Rollback:** disable exporter and remove scoped packages/endpoint credentials; preserve local ledger and export/delete remote test data under approved retention policy. No automatic migration of Nox memory.

### EVAL-05 — Inspect AI: capable but deferred separate harness

**Official API/use.** Python `Task` combines dataset, solver and scorer; CLI `inspect eval` and Python `eval()` run it. It supports custom/MCP tools, agent and external-agent evaluations, logs and Docker/other sandboxes. [S-IA-DOCS, S-IA-EXAMPLE]

**Why defer:** Nox is TypeScript and already has Head/MM/QA. Inspect adds a Python runtime, eval definitions, logs and operational model. It does not intrinsically measure Nox's immutable candidate epoch, real terminal state, authority boundaries or accepted-result economics. Use only after a small Promptfoo/existing-QA spike demonstrates an unmet need (for example, required Inspect-specific agent sandbox/scoring).

**Conditional minimum integration test (NOT_RUN):** separate approved Python ≥3.11 environment, no production Nox import. Replay immutable Nox result bundles as dataset samples; custom scorer independently rejects stale spec/candidate hashes, incomplete oracle records, denied calls and nonterminal state. Only a later owner-approved live adapter may invoke direct Nox. Compare against the simpler harness for identical held-out tasks and retain no-benefit results.

**Security/limitations:** `local` sandbox is no isolation; tasks/solvers/scorers/configs are Python code; Docker is limited isolation and upstream recommends stronger isolation such as gVisor for untrusted code. Host/runtime patching remains the operator's responsibility. Custom Compose replaces generated protections and must explicitly retain `network_mode: none` unless network is essential. Do not infer safety from use of Inspect. [S-IA-SEC, S-IA-SANDBOX]

**Rollback:** remove the separate environment/harness and retain logs; no Nox migration. Revisit only with measured differentiating value.

### EVAL-06 — Langfuse self-host: conditional infrastructure, not first-step QA

**Official use/security.** Official Docker Compose is the simplest trial path but explicitly lacks HA, horizontal scaling and backup functionality. The architecture includes web/worker, Postgres, ClickHouse, Redis/Valkey and S3/blob storage. Change default secrets, restrict network exposure and pin image digests before any real deployment. [S-LF-COMPOSE, S-LF-SELFHOST]

**Minimum integration test (NOT_RUN):** only after owner approval, use a disposable synthetic-data deployment pinned to v4.80.0 artifacts/digests. Verify health/readiness, authentication, project isolation negatives, restart/persistence, backup/restore, export/delete, resource ceilings and SDK v6 ingestion/query. No public port or production trace data in the spike. Oracle: restored synthetic trace and metadata match exactly; cross-project query is denied; failed backup means not operationally accepted.

**Rollback:** disable SDK export, stop the isolated stack, export/delete test data, remove secrets and infrastructure according to approved retention; preserve Nox local evidence. Never treat `docker compose down` alone as verified data deletion/backup.

**Limitations/cost:** license fee for core can be zero while compute, storage, maintenance, upgrades, security and incident costs remain UNKNOWN. EE features are not covered by the MIT core grant.

## What these tools do not establish

- **No universal professional qualification or competence transfer.** Only frozen, held-out, fresh-context direct-Nox tasks with independent domain oracles can support bounded claims (T01–T12).
- **No full WCAG/accessibility certification.** axe-core is explicitly partial automation; manual and qualified review remain mandatory.
- **No security certificate.** Promptfoo red-team output, OSV results and Inspect sandboxes each have limited scope; absence of findings is not safety.
- **No accepted-result economics.** Langfuse/provider traces can be incomplete; actual invoice reconciliation or UNKNOWN remains separate.
- **No proof of strategy uplift or learning.** A package/fixture PASS is not L3/L4 or evidence that a future mission will succeed. L4 requires equal-task measured uplift with an independent frozen oracle.
- **No G0 repair.** Current candidate binding, complete artifact coverage, inspection write lock, unresolved effects and durable terminal state must be established by Nox itself before broad evaluation claims.

## Source and snapshot notes

All successful raw snapshots are content-addressed by SHA-256 in `/workspace/out/sources/evals/*manifest.json`; official release HTML is saved per repository. `SHA256SUMS` covers delivered files. GitHub REST requests returned HTTP 403 rate-limit errors; those error bodies were preserved and not treated as repository evidence. Releases were instead read from official GitHub release pages and tags resolved with `git ls-remote`. Four guessed Promptfoo documentation raw paths and one guessed axe example path returned 404; no content claim relies on those failed fetches. Official current docs and release files supply the cited behavior.

### Source IDs

- **S-PF-README / S-PF-PKG / S-PF-SEC / S-PF-EXAMPLE:** [official repository](https://github.com/promptfoo/promptfoo), [tagged package](https://github.com/promptfoo/promptfoo/blob/0.125.1/package.json), [security policy](https://github.com/promptfoo/promptfoo/blob/main/SECURITY.md), [getting-started fixture](https://github.com/promptfoo/promptfoo/blob/0.125.1/examples/getting-started/promptfooconfig.yaml); [release](https://github.com/promptfoo/promptfoo/releases/tag/0.125.1).
- **S-PF-DOCS:** [custom provider](https://www.promptfoo.dev/docs/providers/custom-api), [JS assertions and safe-mode limitation](https://www.promptfoo.dev/docs/configuration/expected-outputs/javascript), [CLI](https://www.promptfoo.dev/docs/usage/command-line), [Node API](https://www.promptfoo.dev/docs/usage/node-api-reference).
- **S-LFJS-README:** [JS SDK README](https://github.com/langfuse/langfuse-js/blob/main/README.md); [v6.1.1 release and package digests](https://github.com/langfuse/langfuse-js/releases/tag/v6.1.1).
- **S-LF-DOCS / S-LF-MASK:** [SDK overview](https://langfuse.com/docs/observability/sdk/overview), [data masking](https://langfuse.com/self-hosting/security/data-masking).
- **S-LF-SELFHOST / S-LF-COMPOSE:** [self-host architecture](https://langfuse.com/self-hosting), [Docker Compose limitations/security](https://langfuse.com/self-hosting/deployment/docker-compose); [core/EE license split](https://github.com/langfuse/langfuse/blob/main/LICENSE); [v4.80.0 release](https://github.com/langfuse/langfuse/releases/tag/v4.80.0).
- **S-IA-DOCS / S-IA-EXAMPLE / S-IA-SEC / S-IA-SANDBOX:** [official overview](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/docs/index.qmd), [hello-world example](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/examples/hello_world.py), [security policy](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/SECURITY.md), [sandboxing](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/docs/sandboxing.qmd); [0.3.289 release](https://github.com/UKGovernmentBEIS/inspect_ai/releases/tag/0.3.289).
- **S-AXE-README / S-AXE-API:** [release README](https://github.com/dequelabs/axe-core/blob/v4.14.0/README.md), [API](https://github.com/dequelabs/axe-core/blob/v4.14.0/doc/API.md), [third-party licenses](https://github.com/dequelabs/axe-core/blob/v4.14.0/LICENSE-3RD-PARTY.txt); [v4.14.0 release](https://github.com/dequelabs/axe-core/releases/tag/v4.14.0).
- **S-OSV-USE / S-OSV-OUT / S-OSV-OFF / S-OSV-REL:** [source scanning](https://github.com/google/osv-scanner/blob/v2.7.1/docs/scan-source.md), [output/exit codes](https://github.com/google/osv-scanner/blob/v2.7.1/docs/output.md), [offline mode](https://github.com/google/osv-scanner/blob/v2.7.1/docs/offline-mode.md), [installation/provenance](https://github.com/google/osv-scanner/blob/v2.7.1/docs/installation.md); [v2.7.1 release](https://github.com/google/osv-scanner/releases/tag/v2.7.1).
