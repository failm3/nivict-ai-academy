# NOX R1 — Capability Librarian, Knowledge System, Professional Packs

**Date:** 2026-11-13. **Status:** proposal/research, NOT owner-approved for code implementation. **Do not modify or restart live R0, keys, budgets, tool permissions, or deploy.** Architecture extension of current Nox / Mastra / Tool Intelligence, NOT a replacement framework. This document captures the owner's library/librarian/school metaphor and the resulting engineering proposal.

## Owner's thesis / pain point

The system has a catalogue of approximately 4504 historical candidate tools and about 3415 Manus/PG registry entries, but there is no proven operator who can guide Nox from selecting a tool through actually invoking it with legitimate permissions, reliable instructions and verified results. Owner also wants fundamental external knowledge—books, technical documentation, articles, video and posts, professional editorial standards—not ungrounded model self-assertions. Every creation task should activate an appropriate set of procedures, skills, tools and independent quality tests; school should precede production stress tests and autonomous operations.

**Critical distinction:** (1) Tool Intelligence = catalog, (2) Capability Broker within R1 Tool Gateway = discovery/selection/authorization/invocation control, (3) Knowledge System = trusted content retrieval and source curation, (4) Professional Capability Packs = skill/recipe/standards/required tool capabilities and QA rules. Do not deploy a second Head/orchestrator, do not treat registry entries as live tools. Agent factory creates scoped workers, not new model weights.

## Independent research cross-check (2026-11-13)

- Anthropic Building effective agents: simple composable workflows, LLM+tools+retrieval+memory, evaluator/optimizer, orchestration when needed. https://www.anthropic.com/research/building-effective-agents
- Anthropic Writing effective tools: clear namespacing, schemas, token-efficient outputs and evals. Too many nearly identical tools harm selection. https://www.anthropic.com/research/writing-tools-for-agents
- MCP 2026-07-28: tools (actions), resources (context), prompts (templates); server discovery, no authorization guarantee for merely listed tools. https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/docs/2026-07-28/learn/architecture.mdx
- Mastra (existing runtime framework): MCPClient and runtime toolsets; approval and suspension for sensitive tools; workflows, SkillsProcessor. Version compatibility MUST be checked against installed Nox. https://mastra.ai/docs/connections/mcp ; https://mastra.ai/docs/agents/human-in-the-loop ; https://mastra.ai/reference/processors/skills-processor
- Mastra Knowledge is **alpha**, and its own docs explicitly warn scope isolation not guaranteed. Do not place cross-client restricted data in its alpha store without separate isolation. https://mastra.ai/docs/knowledge/overview
- Agent Skills standard: progressive disclosure of metadata, SKILL.md, scripts, references, assets. https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
- LangGraph persistence: separate checkpoint/thread state and long-term store. Reference pattern, do not migrate runtime without proof. https://github.com/langchain-ai/docs/blob/main/src/oss/langgraph/persistence.mdx
- Temporal durable AI workflow: operational reference for reliable retries/resume; do not migrate now. https://docs.temporal.io/ai
- OWASP MCP security: least privilege, malicious schema/prompt injection, pin tool version/description, sandboxes, origin/token audience verification, no broad approvals. https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html
- OpenAI trace grading: distinguish selecting wrong tool, missing handoff, policy violation, and result failure; measure with held-out scenario evaluation. https://developers.openai.com/api/docs/guides/agent-evals
- OPA policy engine: optional if policies become complex; initially use current fail-closed gate to avoid unnecessary services. https://www.openpolicyagent.org/docs
- Unslop specific candidate: audit + fix plans; no auto-code modifications, no guarantee of beautiful design. https://github.com/0design/unslop-skill

## R1 Tool Gateway: minimal broker contract

No new AI planner. Reuse existing Head as task planner and TI as catalog. Introduce deterministic CapabilityBroker/PolicyGate/ConnectionAdapter/ExecutionReceipt interfaces.

Example staged lifecycle:
1. DISCOVERED (candidate metadata)
2. VERIFIED (source/vendor, version, pinned manifest hash, schemas, tested adapter, risks)
3. APPROVED (policy-admin tool-level permissions)
4. CONNECTED (actual healthy MCP/API/CLI adapter, secrets isolated)
5. GRANTED (short-lived, mission+agent+operation+args+resource scoped, approved human where needed)
6. INVOKED (bounded sandbox, abort propagation, idempotency key, rate/cost caps)
7. RECEIPT (input/output digests, tool version, result artifact, error, time, cost)
8. RELEASED (grant revoked/expired; no standing privileges)

**Never infer GRANTED from DISCOVERED, never auto-install unknown candidate, never silently fallback to allTools, never accept a model's claim as approval.**

Example core commands: `capability.search(task,domain)`, `capability.explain(tool_id)`, `capability.request_grant(agent,mission,tool,scope,args_digest)`, `capability.invoke(grant_id,args)`, `capability.verify_receipt(receipt_id)`, `capability.release(grant_id)`. These are proposed application contracts, NOT existing API names.

ToolCard fields: id, category/capability, vendor/source, version+digest, when/when_not, input/output JSON schemas, runnable adapter, permission categories, access boundaries, time/cost estimates, expected artifacts, errors+remedies, test fixtures, source provenance and owner.

Risk tiers: (A) local or public read-only, auto-grant only within policy; (B) reversible local workspace writes, task-scoped policy; (C) external side effects (publishing, sending emails/applications, live site edits), require explicit scoped authorization or preapproved policy; (D) destructive, money, secrets, production deploy, require separate human approval. Never reveal secrets to agent text.

## Knowledge System: not another monolithic memory dump

Distinct libraries:
- Authoritative foundations (standards, vetted manuals, primary documentation).
- Domain SOPs and recipes (procedures, dependencies, exceptions, outputs).
- Tool instructions/examples and failure playbooks (version specific).
- Case evidence (actual verified successful/failed missions and QA feedback).
- Optional external commentary (blogs, posts, videos, opinion marked as such, not authoritative by default).

Curation pipeline: source/license/access check → crawl/import authorized content → for videos transcription with timestamps, image/video frame extraction where justified → normalize/version/chunk → attribution+date+hash → verify facts/contradictions → subject classification + retrieval indexes → access checks before retrieval → bounded relevant excerpts to worker with original citations. Use existing PostgreSQL/approved memory components where practical; pgvector is OPTIONAL and not assumed installed. Don't copy copyrighted full books/videos without rights or permit lower-trust web text to issue system instructions.

KnowledgeCard fields: source URL/title/creator, format, publication+retrieval time, version/sha, rights/license, authority tier, domain, task applicability, verification state, conflicting sources, scope/tenant, freshness policy, citation anchors, extracted fragments/timestamps, reviewer.

**No model-weight finetuning required for initial 'school'.** Skill conditioning + retrieval + real tool execution + environment feedback + deterministic QA and trace-based evaluations should be first. LLM summaries may assist curation but never self-certify source authority.

## Packs = conditional quality contracts, not unconditional plugin installations

Each pack comprises:
1. task classifier / applicability conditions
2. relevant source-backed foundation bundle
3. SOP/recipe and dependency graph
4. necessary **capabilities** and approved adapter candidates
5. role-template references / skills
6. expected artifacts, required tests and QA contract
7. exception conditions, escalation and budget limits

`WEB-PRODUCTION` task recipe: requirements and content → information architecture/design → implement frontend → backend/DB **only if the requirements require server-side behaviour** → responsive/browser/function/accessibility/security tests → source+manifest+launch guide and signed evidence. Avoid dogmatic 'every website must have a backend'. Sources: MDN https://developer.mozilla.org/en-US/docs/Learn_web_development ; W3C WCAG https://www.w3.org/TR/wcag/ ; OWASP ASVS https://asvs.owasp.org/ . Unslop can be an *independent diagnostic* inside visual quality checks, not a substitute for expert design review. Additional starter packs: `CODE-CHANGE` and `RESEARCH-REPORT`; `MARKETING-CAMPAIGN` follows after verification.

Make quality obligations mandatory **when applicable** but permit tasks to legitimately omit tools (e.g. static landing page no backend, text-only research no browser if internal sources sufficient). Agent cannot waive acceptance itself.

## Example end-to-end positive mission

Owner: 'Prepare a responsive service landing'. Prompt Master freezes requirements, Head picks `WEB-PRODUCTION`, Manager provisions tasks and Factory creates bounded Design/Frontend/QA. Knowledge retrieval returns MDN, WCAG plus house style and versioned SOP, each with citations. Capability Broker finds approved file editing + Playwright, grants short-lived scoped permissions, returns usage examples and schemas. Workers create HTML/CSS/JS, test in Chromium and register actual screenshots with SHA. Independent QA compares original immutable acceptance to delivered files and fails missing README/manifest or visual quality issues; limited repair loop and owner judgement. Release provides actual build and receipts, then VERIFIED case memory, not unvetted hallucinations.

## Priority rollout after R0 acceptance

- **Prep now (read-only, no R0 interference):** inventory candidate tools and native Mastra capabilities, draft ToolCards + core KnowledgeCards, domain pack contracts, held-out test cases. Owner approval before any runtime changes.
- **R1A / librarian MVP:** use 5–10 genuinely connected vetted tools, least-privilege grants and receipts; test selections, refusals, abort and recovery.
- **R1B / knowledge & skills:** trusted small foundational corpus, search, versioned procedures, `WEB-PRODUCTION` + `CODE-CHANGE` + `RESEARCH-REPORT` packs; test retrieval quality and wrong-source rejections.
- **R1C / direct supervised Nox missions:** 3 practical diverse tasks, no OpenCode execution assistance, known requirements and independent QA.
- **R2 / stress ('university'):** parallelism, interruptions, hallucinated tools, injection via documents, failure of services, safe approvals, real quality review and cost caps; owner separately authorizes paid live evaluation.
- **R3:** controlled operation with audit/monitoring, only following explicit GO.

## Evaluations (proposed, not executed)

Positive: proper tool selection, correct args, 1-3 linked tool calls, actual artifacts, efficient retrieval, source citations, reusable recipe and QA. Negative: nonexistent tool, candidate not approved, expired grant, changed pinned checksum, injected instruction in imported article, wrong user/client data, forbidden network destination, duplicate external side effect on retry, cancellation in long-running shell, missing backend when demanded, unnecessary backend when not demanded, attractive mock without functional site, missing README/manifest, inaccurate citation and non-cited assertion. Record release SHA, models, tool IDs/versions, trace, test inputs, evidence, token cost and independent verdict. Compare before/after baseline on held-out scenarios; do not assert success from code volume or aggregate pass alone.

## Assessment of owner's direction

**Direction justified**, not R0 interruption. Two corrections: Tool Gateway cannot double as knowledge quality control; separate Knowledge System. A massive 'fundamentals' corpus without tests and proper tool access does not teach reliable execution. Deficiencies in original NIVICT mission also involved quality standards/model/QA and artifact truth, not solely lack of books. The executable scaffold must remain safe first. Introducing a new LangGraph/Temporal/OPA stack is not the default; reuse Mastra, current TI, policy gates, approved MCP adapters and standard Skills wherever possible.

No installations, OpenCode prompts or runtime changes are authorized by this document.
