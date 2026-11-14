# 06 — Enterprise comparative research

**Статус:** L2 primary-source desk research; Nox L3/L4 NOT_RUN. Полный сравнительный текст: `enterprise-practices.md`; 42 resolvable evidence rows: `enterprise-evidence.csv`; synthesis: `four-contours.md`.

## Переносимые компоненты

| Система | Подтверждённый reusable pattern | Nox proof target |
|---|---|---|
| OpenAI Codex/Agents SDK | tool filters, server-owned approvals/RunState, trace, no exactly-once promise | T02/T09/T10 intent/idempotency/reconcile |
| Anthropic Claude/Agent SDK/Skills | deny/ask/hooks, sandbox, progressive resources, no permission from metadata | grant-vs-visibility, T05/T09 |
| Google ADK/Agent Engine | Runner separation, agent/user auth, trajectory+outcome eval | per-handoff identity, T04/T09 |
| Microsoft Agent Framework/ABE | behavior contract, operating envelope, checkpoints, protected release set | G0/G4, current epoch/terminal |
| AWS Bedrock AgentCore | deterministic gateway/policy, scoped memory/eval, ephemeral session boundary | deny/bypass/tenant negatives |
| Devin / Fin / Agentforce | reviewed trajectory, explicit handoff, deterministic/hybrid routes | no vendor metric transfer; T07/T11 |
| LangGraph / Mastra | checkpoint vs store; native search/load filters and pinned API | reuse MM; G1 equal-budget proof |

## Boundary

Proprietary internals UNKNOWN; public docs не measured Nox quality. Devin/Fin/Agentforce numbers VENDOR_REPORTED, не independent uplift. OSS license не hosted rights/TCO. Не вводить platform layer: переносить behavior contracts в existing PM/MM/QA/memory. Equal-task independent T01–T12 обязательны; costs/maintenance UNKNOWN.
