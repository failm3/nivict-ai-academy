# 02 — Nox runtime forensic audit

**Статус:** `BLOCKED_UNKNOWN_CURRENT`. Это **не latest audit**: canonical `/home/nox/awe-group-cleanroom-20261112` отсутствует, WSL/computer connector не доступен. Ниже historical baseline `r1/dev@68cc0ee20a25991ea275512e20ac521cc8f8234b` из 03/05; не fresh discoveries.

## Матрица present/wired/call/QA/release

| Контур | Historical source finding | Current state | NEXT_TEST |
|---|---|---|---|
| Artifact identity | Historical basename/root duplication at src/tools/index.ts around 407 | UNKNOWN | Fresh inspect file_write/storage; nested same-basename test OC-01 |
| CandidateEpoch/QA | Historical 6 artifacts/12000 chars each/6000 output truncation; candidate race reported | UNKNOWN | OC-02/03 complete manifest/write fence/stale receipt |
| Head/MM | Historical Head roles/tools/parallel, not models; MM DAG/parallel and runDelegateCall documented | UNKNOWN | Fresh call graph and actual receipts; no scheduler rewrite |
| Delegation/tools | Historical static allTools; Tool/SkillSearch not wired | UNKNOWN | Fresh specialists/tool-context and installed typings; OC-06 |
| Memory/skills | Historical LibSQL message recall off; learned registry unconfirmed | UNKNOWN | Fresh src/memory and actual store; no PG assumption |
| Browser/MCP | Historical unpinned npx @playwright/mcp absent lock | UNKNOWN | Fresh config/lock; no live call before owner G2 |
| Lifecycle/effects | Historical paused web mission with unresolved intent; no late acceptance | UNKNOWN | Fresh run trees/checkpoint; T10 real interruption later |
| Ledger/release | Historical token subtotals incomplete; no current release evidence | UNKNOWN | Complete invocation ledger+invoice; release remains out of scope |

Для всех строк current `CODE_PRESENT/CONFIGURED/CALLABLE/OFFLINE_TESTED/LIVE_OBSERVED/INDEPENDENT_QA_ACCEPTED/RELEASED = UNKNOWN`; historical evidence не повышается автоматически.

## Blocking web chronology

Historical mission `r1-web-fc45eff2-3378-4ebd-8682-006ac71fac0a`: PAUSED/not accepted, `600111/600000 ms`, repair=2, aborted intent `eb2f2fcc-a5b9-47f2-ab2e-0e2f971a0dfc`. Replacement product `r1-static-task-tracker-v1` 13/13 only on tree `a71660c6e6562f9542ed16013f4e24dedd3dcc179106ebc1bb9d72efe31ababe`, contract `4857e261da19afefcf3bcfa80879b5a1d286963a42495d8fa97f90aa30d01bb8`; не old tree. Five completed model calls 337014 tokens; sixth 104613 outcome UNKNOWN; total/USD UNKNOWN. Retained 39/39 offline и R0 252/55 hashes не current rerun.

## Fresh protocol и stop

Owner read-only: initial/final `git status --short --branch`, HEAD, source/package hashes, delta 68cc0ee; package lock/typings, production call graph, both run trees, logs, actual checkpoint, ledger. Concurrent work → scoped snapshot. Отсутствие source оставляет integration H/UNKNOWN; не использовать historical runtime export как current. Sources: `source-baseline.md` §1,2,6,7; `requirements.md` §3,4; `opencode-tickets.md`.
