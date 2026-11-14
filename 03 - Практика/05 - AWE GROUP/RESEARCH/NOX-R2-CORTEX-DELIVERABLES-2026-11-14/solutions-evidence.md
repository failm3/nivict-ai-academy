# Nox R2 solutions — evidence ledger

Observed: 2026-11-14 UTC. Research only; no Nox mutation, OpenCode review, publication, dependency installation, live provider or paid test.

## Decision summary

The strongest route is **reuse Nox first, then configure its pinned Mastra, then add one small adapter**. The first dependency to consider is not a new framework: it is the exact native `ToolSearchProcessor` at the installed baseline. G0 correctness remains a prerequisite and is not replaced by any external package. All integration compatibility and Nox runtime states below are **UNKNOWN** until fresh source access and independent tests.

## Evidence scale and scope

- **L1**: official identity/claim located. **L2**: primary source, exact API/version/license metadata inspected. **L3**: isolated executable adversarial test — **none performed here**. **L4**: independent equal-task uplift — **none performed here**.
- `DOCUMENTED` means upstream documentation/code exists, not Nox-wired, callable or accepted. `A` for SOL-001 is strictly the retained historical bounded scope; it is not a current runtime claim.
- A repository `HEAD` is an observed moving branch snapshot, not a release endorsement. npm/PyPI latest is not a recommended automatic upgrade. Use exact artifact integrity in a future approved lockfile change.
- Costs, production availability, current provider health, actual uplift, live MCP calls and professional qualification are UNKNOWN unless explicitly bounded otherwise.

## Owner contract readback

Read completely: 06 (437 lines, 81,097 bytes), 07 (83 lines, 22,009 bytes), 03 (207 lines), 04 (391 lines), 05 (219 lines). The docs repository `main` read returned commit `9573a64f2602631ec5d2299716612ba8578c2a13`; the historical review commit `3c3fed07b8222946204cfa8169d9aef04f9f4097` was independently retrieved. Fetched 03 and 04 SHA-256 exactly match 05 §10:

| Input | SHA-256 |
|---|---|
| 03 | `e3c421d40daf886462600b33f0bcc8fd990349a639f758d6a79b68ba55614ea4` |
| 04 | `579edcaa62d8e20bc4bfd6feba3ac9bd018899c824a01941b7ef0d8fe1b5ed60` |
| 05 | `bfd9690624dab166bbe65507e8579ca61d33ec2a67e2ee6d1f7a298b69b46227` |
| 06 | `0767476e3da1599aaaa731d43397e01dc944c14247ec016ffae03c68cba1ce1f` |
| 07 | `97ab44d3b1ca5a78f8e8155bcacb5ed2ee026a2c62f600777a06d3b1742b78ed` |

The authorized Nox path `/home/nox/awe-group-cleanroom-20261112` is absent in this VM. No connected-computer read was available here. Therefore no current Nox HEAD, lockfile or source claims were made. All module paths come from the historical `68cc0ee…` review.

## Reproducible source capture

- `collect_sources.py`: uses `git ls-remote --symref` for official repository default branch and HEAD; captures raw README/LICENSE; writes `sources/upstream/manifest.json` with UTC and SHA-256. No unauthenticated GitHub REST dependency. Initial REST attempt returned 403 rate-limit; raw Git and npm/PyPI remained usable.
- `collect_packages.py`: captures selected npm/PyPI registry fields including exact versions, engines, dependencies, license and npm integrity into `sources/packages/manifest.json`.
- `build_catalog.py`: generates the CSV; `verify_outputs.py` checks schema, IDs, hashes and source snapshot consistency.
- Evaluation workstream: `evals-report.md`, `evals-candidates.json`, and 96 snapshots under `sources/evals/` with source manifests. It confirmed OSV-Scanner `v2.7.1`, axe-core `v4.14.0`, Promptfoo `0.125.1`, Langfuse JS `6.1.1`, Inspect AI `0.3.289`, Langfuse self-host `4.80.0`. All L2/NOT_RUN. MCP/Mastra delegated sessions failed at provider stream completion; their partial findings were not treated as completed reports.

## High-value upstream facts

### Native Mastra (SOL-002)

Nox historical pin: `@mastra/core=1.82.0`, `@mastra/mcp=2.8.0`. npm metadata confirms Apache-2.0, Node `>=22.13.0`, and integrity `sha512-jrgFcoSYAVSsE41fXD3dUxuRWZtfFc3HuGRQRnQmGDHYQMU/S89YoP/ZilkSM3c9nn0Gxj9qFVzauoNZONPIxw==` for core and `sha512-7OjXbUCfSAyosue9VkC9DPL+pdVrDHYH/LhIfmLbzxcp3GOniFxznrpcYlRyvRBdXL4jRh1ARZRHjIJfZdWcrQ==` for MCP. Registry capture observed latest `1.83.0` and `2.9.0`; this is **not** an upgrade recommendation. Historical local typings/docs in 03/05 establish the installed processor's phase filters and storage semantics. Native wiring and measured token savings remain UNKNOWN. A delegated source pass additionally reported that filtering is not execution authorization, `LocalSandbox` defaults to `isolation: 'none'`, and read-only `LocalSkillSource` does not itself prove base-path containment; these must be checked against the saved exact source before engineering.

### Microsoft Playwright MCP (SOL-003)

Official repository HEAD: `78eca85361efb545a4c0f59b6140aef0721c5412`; Apache-2.0. npm observed `0.0.85`, Node `>=18`, integrity `sha512-bSfECMbLXhJdWkGhLzNMxTZuazG+9IDJ679gflji3yyD94e7ARnGdqmJmG6lTPB+gYX+OiFLmX5myBl62+wZEw==`. Its exact npm dependencies include `playwright` and `playwright-core` `1.66.0-alpha-2026-11-09`; this must not be silently conflated with Nox `@playwright/test=1.49.1`. Upstream README supplies browser MCP config and itself discusses CLI+Skills versus MCP context tradeoffs. Neither proves Nox fit or savings.

### Official MCP Registry (SOL-007)

Repository HEAD: `115f85225c9fac5281d8a2dc8551cf49b004d2f9`. Root LICENSE describes a transition: new code/spec contributions Apache-2.0, some earlier contributions MIT, docs excluding specifications CC-BY-4.0. README documents publishing authentication. This establishes a metadata source only, not trusted executable content, a sandbox, current server health or permission.

### MCP Inspector (SOL-008)

Official HEAD `488c30d9d16e4993bc548ad298eb7450f5125c93`; npm `2.15.0`, Node `^22.23.4 || ^24.22.1 || >=26.12.1`. README exposes UI/CLI/TUI commands. Important negative constraint: secrets default to OS keychain where available, but on keychain-less Linux they may be stored unencrypted in `~/.mcp-inspector/secrets.json` unless an encryption key or memory-only mode is used. Nox testing must use a harmless local fixture and no real secrets.

### Docling and Crawl4AI (SOL-004/010)

Docling HEAD `31d14a74b7bddc850541ab8363b8585085845313`, MIT, PyPI `2.150.0`; Crawl4AI HEAD `cae74b203a33994f7e13b9052c3b0d5c93daa0e6`, Apache-2.0, PyPI `0.9.5`. These are candidate format-specific ingestion components, not a universal parser or source-rights/ACL system. Real source ground truth and citation coverage must be measured before use.

### Agent Skills and Unslop (SOL-005/015/016)

Anthropic official examples HEAD `2c5958ecac7cee2b583967a2c4981d0f4a75c579`; no root LICENSE was captured, so reuse is per-path and otherwise UNKNOWN. `heydamir/unslop` HEAD `97daa3eb365670ea3f87ed85356cbfcee18105a5` has CC-BY-4.0 root license. `0design/unslop-skill` HEAD `12a35cc5f003ec08dcb6dd828ed0d059904902cd` has MIT root license. They are separate candidates. None supplies Nox authority or proven professional transfer; scripts/resources need their own rights and sandbox review.

### Evaluation and observability (SOL-006/009/013/014)

Promptfoo HEAD `aaeebf25ea3a17e4f053f52ad5aedcc4551c43f8`, npm `0.125.1`, Node `>=22.22.0`, root MIT terms. Langfuse server HEAD `48a31810e1c6e6a4a589b1eacc5eecc7960c9b87`; root LICENSE is MIT Expat outside `ee/` paths and separate terms inside, so hosted/EE rights cannot be generalized. The separate current JS SDK is `6.1.1` (scoped `@langfuse/tracing`/`@langfuse/otel`); unscoped npm `langfuse=3.39.2` is deprecated and not the proposed path. `@axe-core/playwright` `4.14.0`, Node `>=22.12.0`, MPL-2.0 package metadata; axe-core HEAD `d991e05ac6eb42df88f9e61c1679692534bb92e2`, MPL-2.0. Inspect AI HEAD `f72aaad97e8baad440e256bad542a075a83e427c`, MIT, PyPI `0.3.289`. These support test/tracing functions, not self-certification, invoice completion, universal accessibility or professional accreditation.

### Typed APIs and supply chain (SOL-011/012)

openapi-typescript HEAD `d46a319ae2efab30e135ba9b223a3cffd1a67eab`, npm `7.13.0`, MIT; integrity is preserved in the package snapshot. It generates types, not an authenticated runtime or automatic side-effect safety. OSV-Scanner HEAD `80fe50567a5d6e0ec408353e2ceacca1561b91be`, Apache-2.0; scan coverage/database version must be recorded, and no findings must not be treated as a security proof.

### Managed/deferred options (SOL-017/018/019)

ToolHive HEAD `b9de592d816b84716d0cdddc786fc8ae21be9ca3`, Apache-2.0. Its README's token-saving claim is vendor-reported, not a Nox benchmark. Composio repository HEAD `fdee7595166f8b5dcff026dc609760d1ce82b2e2` has a root MIT license, but `@composio/core` `0.29.0` package metadata declares ISC and Node `>=22.22.3`: the actual package license must be inspected before reuse. The repository README says Node 22+ generally. Arcade HEAD `0d5b9130041361ff516f8182ac982684842c9e9c`, MIT repo; README describes OAuth token injection and production resource-server auth. All add account/network/control-plane considerations and are deferred until a concrete authorized external-account need is shown. Their code license does not price or authorize hosted services.

## Explicit not-run and next evidence

No candidate advanced beyond L2. `NEXT_TEST` for each is in the CSV and shortlist. Common first proof: a harmless local/read-only fixture under owner-approved isolation, exact package lock/digest, no host secrets, current-grant filter, actual schema/call/receipt, independent oracle, cancellation and orphan checks. Failure or missing evidence remains FAILED/BLOCKED/UNKNOWN; it never becomes PASS by documentation.

## Research limitations

This solutions direction does not perform the separate complete 4504-row audit, current Nox forensic audit or full T01–T12 execution. Those remain other workstreams/owner-approved tests. It supplies the requested ready-made solution catalog, evidence and ranked integration route without claiming whole-R2 completion.
