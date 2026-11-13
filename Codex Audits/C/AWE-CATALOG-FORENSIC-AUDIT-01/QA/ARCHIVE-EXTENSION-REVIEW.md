# Independent review of archive-extension ranks 42-50

Status: **PARTIAL**. All nine added source-linked reviews were independently checked against their pinned README/license caches. Additional BlazeDiff licensing sources were read separately. No upstream code was executed. The same-family reviewer cannot close the different-model-family gate.

The nine recommendations are broadly supported; no decision change is required. Apply the qualifications below before presenting the final review. Source-line pointers refer to the immutable README URL recorded for each rank in `ARCHIVE-EXTENSION-REVIEW.json`.

Independent archive linkage: 50 review entries include 30 exact-project entries linked to **32 distinct original source rows**, plus 20 architecture additions. No ID/project mismatch was found. This does not mean 50 archive tools or 50 runtime audits.

## 42. cloudflare/security-audit-skill

[Pinned README](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/README.md). Verdict: `SUPPORTED_WITH_REQUIREMENT_QUALIFICATION`.

- **requirements**: Add Node.js for validators and an OS-enforced sandbox with sanitized environment, networking disabled and resource/write limits before executing any target-controlled tests. Tool-using subagents alone do not provide that boundary. (README:86-97)
- **decision**: Keep REUSE explicitly limited to reviewed methodology/ledger/schema as already described in the acceptance criterion; it is not approval to install/execute the skill or a completed security certification. (README:9-22)

## 43. vercel-labs/dev3000

[Pinned README](https://github.com/vercel-labs/dev3000/blob/e5573ae23a62fad58194881ef8642a7ee2b273fe/README.md). Verdict: `SUPPORTED_WITH_MATERIAL_SCOPE_AND_BUDGET_QUALIFICATIONS`.

- **requirements**: Separate local d3k requirements from the remote/sandbox launcher, which the README limits to macOS, with Vercel login/access and additional tools. Do not imply Windows supports the sandbox mode. (README:74-91)
- **risk**: The source has inconsistent budget descriptions: an earlier fx section says a non-renewing $5 session cap, while the newer Eve default section says no session spending cap. Budget default must remain UNKNOWN/harness-dependent until source-code/configuration review and a bounded test; do not claim a safe cap from this README. (README:85-89, 128-140)
- **minimum_acceptance**: The live timeline is bounded to 5,000 events/8 MiB and disappears on exit; body/redaction capture is selective and best effort. Add evidence-gap/eviction handling and an explicitly authorized durable evidence export rather than treating d3k as a durable audit ledger. (README:46-58)

## 44. teimurjan/blazediff

[Pinned README](https://github.com/teimurjan/blazediff/blob/eafe393ce40ee22833a9aefe593ff779a7e8f8f3/README.md). Verdict: `SUPPORTED_WITH_LICENSE_SCOPE_CORRECTION`.

- **license_scope**: Use: MIT for inspected BlazeDiff code; embedded MILO weights are Apache-2.0; original reference-code terms and notices are separately described. Algorithm/dependency/commercial-rights clearance remains NOT_AUDITED. The reference MATLAB SSIM/MS-SSIM restrictions must not be blindly applied to the independently MIT-claimed implementation, or ignored for imported reference code. (README:107-124)
- **risk**: Distinguish deterministic core/metric calculations from the optional agent-in-the-loop product. Vendor speed/parity claims and learned perceptual metrics are not independently tested or UX acceptance. (README:24-56)

## 45. browser-use/browser-harness

[Pinned README](https://github.com/browser-use/browser-harness/blob/c2420943526d41b9af6182d5c5f11b9cad506ab9/README.md). Verdict: `SUPPORTED_NO_SUBSTANTIVE_CORRECTION`.

- **risk**: Retain the explicit whole-running-Chrome/logged-in-user boundary and DEFER decision. The current README says Browser Harness is the engine inside Browser Use; installing both is not an independent engine comparison. Its benchmark used a shared fresh cloud browser, not each tool's default local session. (README:3-18, 61-91)

## 46. microsoft/markitdown

[Pinned README](https://github.com/microsoft/markitdown/blob/ed178952a6672abdfd35b5f9e76a80b6cefc086e/README.md). Verdict: `SUPPORTED_WITH_RISK_WORDING_QUALIFICATION`.

- **risk**: Replace ambiguous URL/ZIP traversal wording with: untrusted file paths, remote URLs and archive contents require validation and resource limits; no specific path-traversal vulnerability was demonstrated. The README expressly states current-process I/O privileges, broad convert(), and narrower convert_local/convert_stream APIs. Narrow APIs are not a sandbox by themselves. (README:459-467)
- **requirements**: Python 3.10-3.14 is supported by README. Preserve selective extras/plugins-off-by-default and local-only dependencies; image captioning/transcription and Azure conversion paths are remote/billable options. (README:26-38, 92-117)

## 47. HKUDS/LightRAG

[Pinned README](https://github.com/HKUDS/LightRAG/blob/9929013d1d8ead19b485a43a3ccb373e633cb5e9/README.md). Verdict: `SUPPORTED_WITH_AUTH_ROUTE_AND_STORAGE_QUALIFICATIONS`.

- **risk**: Authentication configuration alone does not close the README's default-open Ollama-compatible /api/* routes. Include the documented whitelist restriction and verify unauthenticated access is denied across every exposed route. The host=0.0.0.0/auth-off statement is a pinned README observation, not a current AWE runtime finding. (README:98-105)
- **requirements**: Default KV/vector/graph/doc-status backends are in-memory with local file persistence and are described as evaluation-only, not production. Storage/model/embedding configuration and reindex/delete behavior need separate acceptance. (README:289-299, 339-343, 391)

## 48. alibaba/zvec

[Pinned README](https://github.com/alibaba/zvec/blob/0e83a2b15926aeb9791222edc46760064a50e705/README.md). Verdict: `SUPPORTED_WITH_CONCURRENCY_QUALIFICATION`.

- **requirements**: README now lists Windows as well as Linux/macOS/mobile and OS-specific SDK features; do not preserve a Linux-only assumption. It specifies 64-bit Python 3.10-3.14. Writes are single-process exclusive although multiple processes may read. (README:36-44, 57-85)
- **risk**: WAL durability/performance claims are source assertions to test, not evidence of PostgreSQL transaction/RLS/auth equivalence. Keep the crash/reopen, isolation and measured-advantage pilot rather than replacing current storage. (README:50-59)

## 49. VectifyAI/PageIndex

[Pinned README](https://github.com/VectifyAI/PageIndex/blob/2ac8694bf8fe89a3840dda9bdb88db5119b77fc4/README.md). Verdict: `SUPPORTED_WITH_LOCAL_DATAFLOW_QUALIFICATION`.

- **risk**: Local SDK/index storage does not imply offline inference: source examples still use an LLM API key. Cloud mode also transfers indexing/storage to the vendor; make dataflow, model cost and cloud storage explicit. Subscription-based Claude invocation remains an advertised integration, not an independent grant of provider permission or guaranteed quota. (README:84-105, 179-217)
- **cost**: Keep source benchmark/indexing-cost headlines separate from AWE measurements and from cloud/subscription pricing. No quoted savings/cost/accuracy figure has been reproduced in this audit. (README:116-165)

## 50. google/langextract

[Pinned README](https://github.com/google/langextract/blob/0e441bf77ddc3119dd0aa413322959234dd84ee5/README.md). Verdict: `SUPPORTED_WITH_GROUNDING_AND_SUPPORT_QUALIFICATIONS`.

- **minimum_acceptance**: Explicitly reject/filter extractions whose char_interval is None. The README acknowledges hallucinated extraction from few-shot examples; a valid schema or source-looking text is insufficient. Also test wrong/overlapping spans and factual attributes that go beyond source text. (README:106-108, 153-157)
- **requirements**: Do not promise identical schema enforcement across providers: the README says Ollama does not currently support output_schema. Google organization ownership does not mean an officially supported Google product; the disclaimer says otherwise. (README:403-405, 535-541)

BlazeDiff supplemental immutable URLs/blob SHAs and observation limits are in `BLAZEDIFF-SUPPLEMENTAL-SOURCES.json`. The upstream model weight digest was not downloaded/recomputed. No legal clearance, dependency-wide license audit, actual OS compatibility or performance comparison was performed.

For every added candidate: runtime **NOT_RUN**, security audit **NOT_PERFORMED**, AWE acceptance **NOT_PROVEN**.
