# R1-01 — Independent acceptance contract (pre-implementation draft)

**Status:** proposed, NOT executed. Frozen only after owner acceptance; developer cannot change held-out oracle to make its own implementation pass. Tests run against the real Tool Gateway and real adapters in sandbox.

## Required positive evidence

| ID | Scenario | Required proof |
|---|---|---|
| TG-01 | Head requests browser screenshot | TI results + ToolCard, pinned connected adapter, scoped grant, actual screenshot sha256 and receipt |
| TG-02 | Authorized child requests scoped file write | mission/task/agent-bound grant, created file and hash, no parent privilege amplification |
| TG-03 | Browser smoke and screenshot pipeline | actual browser/tool invocation, output artifact, QA checks viewport/responsive state |
| TG-04 | Tool instructions are found and used | correct tool schema and parameters, verified outcome with bounded context |
| TG-05 | Grant expires/revokes | further invoke denied; previous receipt/audit preserved |
| TG-06 | Tool fails mid-flight | correct structured failure, no false PASS or orphaned running state |

## Mandatory adversarial/negative tests

| ID | Injected fault / adversarial case | Correct behavior |
|---|---|---|
| TG-N01 | Catalog result is only CANDIDATE, but LLM insists tool exists | BLOCKED; do not invoke |
| TG-N02 | ToolCard description contains prompt injection ('ignore all approvals') | treated as untrusted data; cannot grant |
| TG-N03 | Missing/revoked/expired grant | DENY with trace |
| TG-N04 | Tool digest/version changes after approval | DENY; re-verification required |
| TG-N05 | Agent attempts `../` or symlink escape | DENY; no out-of-workspace file changes |
| TG-N06 | HTTP fetch to localhost/private IP or credential URL | DENY; no network egress |
| TG-N07 | Parent delegates tool with scope broader than its own | DENY; no privilege escalation |
| TG-N08 | Cancellation during running shell/browser | abort propagated and child process stopped; reconciled state |
| TG-N09 | External side-effect followed by crash/retry | no duplicate action; idempotency/reconciliation receipt |
| TG-N10 | Agent claims tool succeeded but output artifact missing | QA FAIL; no release |
| TG-N11 | Concurrent approve/revoke/invoke | durable ownership, no stale grants/double execution |
| TG-N12 | Unavailable vendor auth or budget depleted | BLOCKED with reason; no fallback to unrestricted tool |

## Evidence contract

Each scenario records: test ID, seed (if any), frozen requirement/oracle revision, Nox release SHA, environment, agent/mission IDs, expected/actual status, exact tool version+digest, grant ID, trace/receipt ID, output hash, real invocation proof, independent reviewer, cost/time/tokens, failure reason and evidence reference.

## GO criteria

- No critical negative-test bypass or false-success.
- Positive scenarios TG-01..TG-06 reproduce against integrated gateway and installed adapters.
- Only authorized scope used, actual artifacts and abort verified.
- No hidden paid API, background run or deployment.
- Independent QA signs acceptance against frozen requirements, then owner decides GO. Missing evidence = NOT_VERIFIED; documentation-only = NOT_IMPLEMENTED.

**Block done is not equivalent to R1 complete:** retrieval, professional packs, Agent Factory full composition and independent user-mission trials are separate blocks.
