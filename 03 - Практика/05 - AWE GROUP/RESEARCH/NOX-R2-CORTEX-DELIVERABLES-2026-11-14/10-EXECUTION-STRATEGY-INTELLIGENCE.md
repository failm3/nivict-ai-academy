# 10 — Execution strategy intelligence

**Статус:** design + L2 evaluation research; no route benchmark run. Full candidate evidence: `evals-report.md`.

## Host-owned route

Для whole mission и каждого step отдельно: existing deterministic function; small script; CLI/API/typed workflow; persistent bot/service; single LLM; specialist; parent-managed parallel/nested team; hybrid; BLOCKED. Model selection отдельная подзадача. Known repeat не требует LLM; bot только sustained triggers/uptime/audit; team только independent branches или measured quality; unsafe/missing oracle/authority = BLOCKED.

Recipe: id/version, immutable spec hash, step input/preconditions, program/model/tool/source/skill pins, stage+global wall/token/spend, artifact/oracle/reviewer, retry/idempotency/cancel, checkpoints/touchpoints, denial/fallback, recovery/terminal/ledger/rollback. Head advisory; host authorizes; PM/MM сохраняются. Fallback не расширяет grants и не маскирует FAILED/UNKNOWN.

## Measurement

Same input/fresh contexts/authority/tools/global budget/frozen hidden oracle; all attempts и failed/no-benefit. Metrics: independent accepted rate/quality/citations, first correct tool, repairs/productivity, first/steady latency, complete tokens/USD или UNKNOWN, recovery/unresolved effects, acquisition/build/QA/maintenance. T01 actual zero execution LLM after route; T07 route artifact; T11 paired ≥12 planning cases с CI и small-sample limitation, не гарантия мощности.

REUSE: deterministic fixtures → existing Nox QA → optional Promptfoo 0.125.1 replay harness; OSV/axe narrow preflight; Langfuse only measured trace gap; Inspect/new scheduler deferred. Current Nox/model/provider/price UNKNOWN. Rollback versioned route table/config, ledger сохранить. OC-04/05/10, validation G4.
