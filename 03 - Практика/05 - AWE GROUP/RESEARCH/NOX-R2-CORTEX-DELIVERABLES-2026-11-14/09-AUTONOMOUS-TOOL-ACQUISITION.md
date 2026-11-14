# 09 — Autonomous tool acquisition under explicit authority

**Статус:** protocol design/L2 candidates; acquisition/install/call/revoke NOT_RUN. «Autonomous» не означает self-grant.

## Transition contract

`NEED→DISCOVER→COMPARE→VET→EXPLICIT AUTHORITY→PIN/INSTALL IN SANDBOX→REGISTER→GRANT→DISCOVER ACTIVE→INVOKE→RECEIPT→INDEPENDENT QA→REUSE→REVALIDATE/REVOKE`. Каждый transition: actor/policy, typed I/O, persistent record, idempotency key, failure semantics/evidence. Metadata/install/health/grant/loaded/invoked/accepted/released — отдельные состояния.

ToolCard: stable tool_id, upstream/kind, exact version/commit/digest, license per component/assets, actual dynamic toolName+schema, when/when_not, OS/Node/WSL/deps, preconditions, requested vs actual minimal grants, identity/auth/OAuth, data/egress, read/effect class, idempotency/reconciliation, retries/timeout/cancel, process/resources, health/compat, failure/rollback, L1–L4 refs. Missing = UNKNOWN.

## Host controls и candidate order

Low-risk read-only только preapproved host policy; install/paid/secrets/publish/destructive/new rights — отдельный owner gate. No host/root env secrets, untrusted registry/skill/web policy, implicit latest/npx, broad autoLoad. Active restore только current grants; execution сохраняет `assertToolAllowed`, durable intent/effect ledger.

После G0/G1 выбрать **один** real-gap candidate: Inspector local schema diagnostic, Playwright read-only browser или Docling source ingestion; Registry metadata only. ToolHive/managed OAuth deferred. Exact pins/oracles: `05-READY-MADE-INTEGRATION-ATLAS.md`, `RANKED-ACTIONABLE-SHORTLIST.md`.

T03/T09/T10: tampered/missing package, malicious metadata/name collision/schema drift, missing account/revoked OAuth, no network/timeout/cancel/orphan, duplicate unknown effect, revoked grant/restart. PASS только real useful read-only receipt+independent QA. Stop/quarantine/revoke/disable/quiesce/remove exact integration после reconciliation; evidence и unresolved effects сохранить. Ticket OC-07; current Nox UNKNOWN.
