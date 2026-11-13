# Cortex — NOX Capability, Tools, Knowledge & Professional Competence: Research Scope

**Дата:** 2026-11-13. **Статус:** OWNER DISCUSSION / NOT FINAL PROMPT / NOT SENT. 
**Тип:** карта программы будущего **независимого исследовательского аудита**, не разрешение на изменения R0/R1, установку, платные тесты, деплой или отправку промпта.

## 0. Какую задачу на самом деле поставил владелец

НЕ просто выбрать новый Tool Gateway; НЕ просто построить систему self-update; НЕ написать новый Agent Framework. **Нужно превратить существующий Nox в самостоятельную компетентную исполняющую среду:** Nox разбирает запрос, определяет незнакомое, достаёт проверенные первичные и профессиональные знания, находит реально рабочие tools/API/MCP/CLI, получает законные scoped permissions, применяет подходящие профессиональные SOP/skills/templates, делает фактический продукт, независимый QA проверяет deliverable, опыт возвращается в управляемую базу знаний. При появлении пробела Nox должен найти максимально готовую совместимую интеграцию и безопасно предложить/подготовить расширение без повреждения текущего ядра.

**Главный итог исследования:** source-based gap matrix + extensive qualified market/source catalogue + один реально совместимый integration target plan для Nox + **крошечные исполнимые изменения** и готовые OpenCode implementation tickets с тестами. Не бесконечная архитектура, не новый фреймворк. **Не вводить произвольных потолков на число кандидатов, компаний, видов источников, областей и документов**. Но завершать исследование по достаточности доказательств, покрытию реальных Nox use cases и возможности выдать однозначные решения. Любой вариант за пределами scope должен попасть в backlog, а не задерживать интегрируемое ядро.

## 1. Source of truth / архитектура, которую нельзя случайно переписать

Канонические источники в `failm3/nivict-ai-academy`, префикс `03 - Практика/05 - AWE GROUP/`:
- `CHECKPOINTS/NEXT-CHAT-START-HERE.md`
- `R1-CAPABILITY-PROGRAM/README.md`
- `R1-CAPABILITY-PROGRAM/CHECKPOINT-CURRENT-TRUTH-2026-11-13.md`
- `R1-CAPABILITY-PROGRAM/RESEARCH/NOX-IMPLEMENTED-CAPABILITIES-SOURCE-AUDIT-2026-11-13.md`
- `R1-CAPABILITY-PROGRAM/RESEARCH/MARKET-REUSE-AUDIT-2026-11-13.md`
- `R1-CAPABILITY-PROGRAM/01-TOOL-GATEWAY/SPEC.md`, `CANDIDATES.md`, `ACCEPTANCE.md`, `tool-card.schema.json`
- `IDEAS/NOX-R1-CAPABILITY-LIBRARIAN-AND-KNOWLEDGE-SYSTEM-2026-11-13.md`
- `IDEAS/NOX-MANDATORY-PROFESSIONAL-CAPABILITY-PACKS-CONCEPT-2026-11-13.md`
- `ASTRA-AUTONOMY-AUDIT-2026-11-08/` включая `03-architecture.md`, `04-models.md`, `06-resilience-updates.md`, `07-delivery.md`.
- `02 - Аудит 4504 инструментов.md`, `CHECKPOINTS/TOOL-INTELLIGENCE-V2-OPENCODE-SOURCE-HANDOFF-2026-11-12.md`, `DECISIONS/AWE-TOOL-INTELLIGENCE-CONTINUOUS-MONITORING-2026-11-12.md`, `04 - Блок 04 — AWE Quality Assurance System.md`, `Память — сквозная архитектура и правила.md`, `TESTS/AWE-ARCHITECTURE-ACCEPTANCE-PLAN-2026-11-12.md`, `REPORTS/NOX-OWNER-READINESS-REVIEW-01-2026-11-13.md`, `REPORTS/NOX-R0-LIVE-STATUS-2026-11-13-0338UTC.md`.

Прочие связанные репозитории: `failm3/awe-group-runtime` (его `main` — **устаревший exported baseline**, не текущий cleanroom); `failm3/awe-opencode-recordings` и `failm3/awe-group-observer` (доступные **read-only evidence**); локальный рабочий R0 checkout `/home/nox/awe-group-cleanroom-20261112` — **только при фактической доступности** и не прерывая R0. Если что-либо не доступно — explicitly UNKNOWN, не выдумывать.

Подтверждённая ранее версия Mastra `@mastra/core 1.82.0`, `@mastra/mcp 2.8.0`, memory/libsql, Prompt Master, Head, Mission Manager, `createSpecialist`, `runDelegateCall`, Playwright MCP, tool handlers, Tool Intelligence search, QA. Нельзя повторно «внедрять» эти модули, пока не доказано отсутствие конкретной способности. `ToolSearchProcessor` и `SkillSearchProcessor` — исследовать как потенциально доступные **native features**, а не считать автоматически настроенными. R0 по последней проверке **IN PROGRESS/NO-GO**.

## 2. Независимый forensic audit Nox

Для каждого компонента: real source path/function/version/release SHA; deployment topology; actual API/call surface; rights; tests; real artifacts; defects; observed performance; status `CODE_EXISTS`, `WIRED`, `CALL_PASS`, `QA_PASS`, `BROKEN`, `UNKNOWN`. Несовпадения документации и кода — отдельный раздел.

Проверить end-to-end `user → Prompt Master → Head → Mission Manager → dynamic Factory/subagents → model routing → memory/knowledge → Tool Intelligence & real adapters → permissions/grants → invoke → artifact → independent QA → receipt/recovery`; не притворяться, что running code доказан простым импортом. Отдельно проверить Prompt Master и AI feedback loop, reliability during cancellation/retry, data/permissions isolation, vision/design QA, source versioning. Дать **capability maturity map** по реальным миссиям: сайт/приложение; программная задача; документ/исследование; маркетинг; корпоративный workflow. Результаты P0/P1/P2 и список того, что **уже есть и должно быть оставлено**.

## 3. Enterprise landscape: что реально делают крупные организации и проверенные builders

Искать в инженерных блогах, документации SDK, архитектурных материалах, коде, публичных production cases, CI/eval reports, failure postmortems, conference talks и открытых samples. **Исследовательские цели, не заявления об их текущем стеке:** Anthropic, OpenAI, Google/Google Cloud, Microsoft/Azure, Amazon/AWS, IBM, Salesforce, ServiceNow, GitHub, Cloudflare, Databricks, NVIDIA, Stripe, Shopify; зрелые платформы Mastra, LangChain/LangGraph, LlamaIndex, Haystack, PydanticAI, CrewAI, AutoGen/Microsoft Agent Framework, Temporal, Agno и применимые enterprise integrators.

Зафиксировать: конкретный пользовательский use-case; архитектуру tool discovery, approval, memory, retrieval и eval; публичные инциденты и отказоустойчивость; реальную практику enterprise onboarding; что является SDK functionality, что proprietary, что vendor claim, какие фрагменты безопасно заимствовать для нашего Mastra runtime. **Не мигрировать на другой framework ради переноса красивого паттерна.** Проверять источник по дате и актуальной версии, не приписывать компании использование тех компонентов, по которым нет публичного доказательства.

Сравнить: tool use accuracy, tool overload/context limits, layered architecture, dynamic vs declared workflows, specialized workforce, resource isolation, resumability, approval, mission contracts, independent verification, documentation grounded tasks, cost, user feedback.

## 4. Tool Gateway «библиотекарь» — реализация вместо метафоры

Изучить целиком: tool catalog/TI data vs live adapters; semantic/hybrid search and ranking; dedup/normalization, capabilities taxonomy, aliases, synonyms, tool selection counterexamples, dependency and compatibility checks; healthcheck/connection test; schema discovery, dynamic registration/loading; tools documentation, tool calling examples and correct argument construction; auth and scoped lease/grant; run execution + timeout/cancellation; artifact receipt/trace; exception repair and source-backed explanation; evidence-based promotion from candidate to approved; revocation/uninstall and rollback. Lifecycle не обязательно один ENUM; **grant и inventory разные независимые процессы**.

**Integration formats and hands:** Mastra native tools, MCP (stdio/Streamable HTTP, resources/prompts/tool capabilities), REST/OpenAPI, GraphQL, gRPC where appropriate, SDKs, CLI/subprocess, browser automation (Playwright/DevTools), authorized desktop/computer-use, webhooks, workflow engines/RPA, Git, SQL, SSH, cloud services, Figma design resources, document parsers and artifact producers. Enterprise access: OAuth/OIDC, API keys, per-user/tenant vault, allowlists, costs, resource scope, approved HTTP destinations, sandbox, audit, safe action idempotency. No self-grant and no unvetted code auto-install.

Compare native Mastra processor/MCP/HITL first; then candidate ecosystems Composio/Pipedream/Arcade/ToolHive/Activepieces/n8n or others where **real gaps** proven. Terms/license/lock-in & security are first-class.

Evaluate the existing approximately 4504 research candidates by **applicability, duplicate functions, maintenance, real execution connection, safety and verified quality**; do not claim 4504 installed. Discover additional relevant tools with no arbitrary artificial cap.

## 5. Knowledge system — expand *all* sources, not just books

Cortex should discover repositories/sources **and their methods of import, indexing, citation, updating and validating**.

### Types of inputs
- Standards/RFC/ISO/IEC/W3C/OWASP, specifications, official vendor docs, language/framework refs, API reference, release notes, changelogs, migration guides and security advisories.
- Academic papers, peer-reviewed journals, preprints with caution, whitepapers, benchmarks, reproducible experiments, public datasets and benchmarks.
- Professional books/textbooks/handbooks; curated bibliographies, dictionaries, glossaries, professional encyclopedias, patterns and design patterns.
- Documented SOPs, process maps, checklists, implementation guides, runbooks, postmortems, architecture decision records (ADRs), real case studies, working reference implementations, annotated examples.
- Videos: conference talks, university lectures, screen recordings, user research sessions, walkthroughs, courses, webinars; subtitles/transcripts **plus frame/video/screenshot content when necessary**, timestamps.
- Podcasts, interviews, transcripts, meetups, panel discussions, technical Q&A and recorded workshops.
- Technical blogs, newsletters, engineering writeups, editorial columns, high-quality community posts, discussion forums, Stack Overflow answers, GitHub Issues/PR/reviews, engineering RFCs, release changelogs.
- Production app and UI screenshots; Figma Community components; design tokens; icon libraries; interface templates; style guides, interaction patterns, motion references, accessible component implementations; web demos and Storybook galleries.
- Research reports, user interviews, usability tests, comparative UX benchmark datasets, conversion research, heatmaps/session-recording interpretations under rights and privacy controls.
- Code examples, boilerplates, open-source repositories, software packages, tests, examples and fixtures, security test cases, official tutorials, sandbox playgrounds.
- Industry/domain sources: marketing platform manuals, analytics, attribution, paid campaigns, SEO, product strategy, operations, finance, HR, customer support, legal compliance, data science, research methods and project management.
- User/org-specific approved knowledge: existing NIVICT Obsidian/GitHub material, accepted products, business rules, templates, documented customer requirements, success/failure logs; explicit separation of private data and externally sourced materials.

### Ingestion / retrieval / trust
Crawling and content extraction (HTML/PDF/Office/EPUB/video), transcript and timecodes, table/formula/image/diagram handling, citation to original chapter/page/minute, edition/license/access check, source version+digest+timestamp, source reliability tiers and human review for contested facts, contradiction and staleness detection, canonical dedup, local vs cloud storage, project ACL isolation before retrieval, search (keyword/BM25/vector/hybrid + re-ranking), retrieval quality tests, recency refresh. **Do not treat external content instructions as system commands, and do not ingest copyrighted materials without proper rights.** Use existing memory/storage if sufficient; compare Docling/Crawl4AI/standard skills, optional retrieval services, instead of building our own parsers, browsers and RAG stack.

Professional knowledge is **not automatic LLM finetuning**. Evidence-backed retrieval + executable skills + live practice + evals should precede any model training. Distinguish verified learnings from LLM summaries.

## 6. «Научить Nox работать»: procedural skills, tool practice, competence promotion

Discover reusable **Agent Skills/SKILL.md** instructions, recipes, domain-specific workflows, tested agents, reference scripts, ready-made tool-use playbooks, error-handling patterns, scoped templates. Lifecycle: identify unfamiliar task → retrieve authoritative materials → propose tool workflow → try in isolated safe environment → parse actual receipts → independent evaluator checks use of correct API and result → refine → store versioned skill + source/limits → prove generalization on unseen variant → promote to production capability pack. Add explicit **when NOT to use tool**, examples of errors, alternatives, prerequisites and expected outputs.

Distinguish `tool` (action), `skill` (procedure), `knowledge` (facts/provenance), `template` (starter structure), `agent role` (executor configuration), `pack` (conditional professional contract), `QA test` (oracle). They should not be collapsed into one giant plugin or agent. Self-learning cannot grant broader privileges.

## 7. Domain competence & ready-made ecosystems — wide investigation

### A. UX/UI and Product Design
- Real design process (discovery, problem framing, research, personas/JTBD, IA, flows, wireframes, prototypes, design system, component/tokens, interactions/motion, copy, handoff, review).
- Design knowledge and templates: Figma official SDK/MCP/integration, Figma Community where permitted; professional design systems e.g. Material Design, IBM Carbon, Microsoft Fluent, Shopify Polaris, Apple HIG, Adobe Spectrum; web component libraries such as Radix/shadcn, React Aria, MUI, AntD and others; Storybook, design tokens, iconography, WCAG and relevant accessibility patterns.
- Design QA: anti-slop skills (e.g. Unslop as candidate), visual hierarchy, typography, spacing, contrast, accessibility, mobile/responsive, functional click paths, semantic HTML, screenshot diff and expert independent visual review; no automatic artistic PASS from screenshot similarity alone.
- Design study material: usability research methods, NN/g, Baymard and other professional research respecting licenses/terms; independent evidence vs opinion.

### B. Software Engineering / Website & App Production
- Web/mobile/desktop stacks as needed; implementation with frontend, backend **when required**, API, data/storage, authentication, security, tests and deployment; standard libraries and boilerplates; package registries/official docs/versioned examples.
- Playwright, browser DevTools, test runners, linters/formatters/typecheck, SAST, dependency audit, CodeQL/Trivy candidates, test fixtures, CI/CD, profiling and monitoring.
- Production standards: MDN/Web Platform Tests, OWASP, language/framework docs; complete artifacts/manifest/README/source code, real run, negative tests; no fictitious success.

### C. Marketing / Growth / Product Marketing
- User/market and competitor research, positioning, messaging/copy, segmentation, creative production, channels, SEO/SEM/SMM, ads platform official APIs, analytics/attribution/ROI, A/B and experiment design, conversion, CRM, email deliverability, attribution and lifecycle.
- Ready-made integration providers and compliant app account access (Google/Meta/Yandex, CRM/analytics as applicable); licensed benchmark research, regional legal constraints and privacy.
- Quality contracts: sources for stats, campaign budgets, independently tested tracking, measurable KPI, consent and reporting.

### D. Business, Management & Operations
- Economics, unit economics, operations, project management, pricing, service operations, BPMN, resource planning, procurement, product strategy, customer support and documented decision-making processes.
- ERP/CRM/accounting/task tools, templates, SOP repositories, risk and compliance checklists, reporting & spreadsheet/document creation tools.

### E. Research, Data & Knowledge Work
- Search/evidence synthesis, datasets, charts, files, PDFs, presentations, transcription, fact checking, software/data analytics, citation verification, reproducibility and independent reviewer patterns.

### F. Other industry verticals
- Survey what domains can be enabled through *packs* rather than custom architecture. Classify availability, license, risks, specialist validation, regulatory/legal constraints and applicability. Do not install all domain packs by default. Pick case-based role combinations and tool requirements.

For every domain: `business task → expected professional deliverable → source knowledge → ready-made tool/API/MCP → SKILL/SOP → QA rubric/tests → compatibility/security/cost/license → ready-to-integrate proposal`.

## 8. Safety & autonomous improvement, without rebuilding Nox

Different classes: add source/corpus, add skill, add package, configure tool, grant/revoke rights, add adapter, update model, change runtime/core, update DB. Each has appropriate privilege and acceptance path. Safe low-risk configuration must not require redeploying the entire kernel. High-risk policy/core/tool/plugin changes require isolated branch, clean tests, independent QA, signed release and risk-scoped owner approval. Reuse current R0 cancel/lease/receipt and ASTRA secure self-update proposal; no second giant orchestrator/update system without proof of need. Persist active mission version pins; failure rollback/roll-forward and migration compatibility to be addressed, never assume rollback DB is trivial.

Distinguish research from execution permission. No automatic install from scraped untrusted package listing. Consent for external side effects; protect secrets and private customer data.

## 9. Independent critical reviewer

Cortex must act **not as an advocate for existing proposals**: identify architectural overengineering, duplicated module, aspirational capability incorrectly labelled working, security gaps, design visual quality weaknesses, source trust gaps, vendor lock-in, excessive token/cost/context, missing access, poor documentation, QA circularity, hallucinated abilities. Bring counterexamples and disconfirming evidence. Incorporate validated feedback from actual agent engineering teams and professional communities; label vendor cases vs independently reproduced tests.

Publish explicit **red-team failure scenarios**: nonexistent/unapproved tool, malicious MCP/tool description, fake citation, stale framework docs, wrong-context memory, revoked OAuth, hostile article prompt injection, improper domain workflow, broken design/website, incomplete artifact, external duplicate action, aborted shell, model behavior regression, unwanted self-install or policy escalation.

## 10. Measurement and practical end-state

Success is not number of plugins, source pages, tokens or architectural diagrams. Ground in **real owner tasks** and compare baseline Nox vs planned enabled capabilities:
- task completion & verified artifacts,
- tool-selection and correct-args success rate,
- useful source retrieval with valid citations, factual correctness,
- time to first successful tool use, time-to-finish, cost by task,
- quality (visual/domain/functional/accessibility where applicable),
- permission breaches and false-success rate, failure recovery, ability to disable/rollback,
- availability of actual connected adapters rather than catalogue count,
- repeatability across novel tasks, independent QA verdict.

No arbitrary ceiling on literature, candidates or integration opportunities. **Stop searching when** all owner-specified domains, failure modes and required integration interfaces have evidence-based decisions and actionable remaining gaps; defer speculative nonblocking cases to research annex. Completion requires unambiguous per-capability verdict, not endless exploration.

## 11. Required deliverables for future Cortex task (no arbitrary size caps)

1. `NOX-AS-IS-SOURCE-AUDIT`: exact version/commit/path, code/provenance evidence; connected/tested vs not installed vs no access.
2. `ENTERPRISE-AGENT-ENGINEERING-BENCHMARK`: independent patterns at large companies, primary sources and critical comparisons.
3. `TOOLS-AND-CONNECTORS-CATALOG`: comprehensive, normalized/deduplicated tool/protocol/service/API/MCP/CLI registry with source, usage, risks, compatibility, license, verified status and actual fit for Nox; map historical 4504 candidates.
4. `PROFESSIONAL-KNOWLEDGE-SOURCES-ATLAS`: wide source taxonomy with machine-readable provenance, ingestion approach, trustworthy primaries, multimodal handling, license and refresh.
5. `DOMAIN-CAPABILITY-MAPS`: Design/UX, Software, Marketing, Business/Ops, Research/Data and additional useful domains; applicable skill/tool/QA packs, optional vs mandatory.
6. `BUILD-BUY-REUSE-VERDICT`: `ALREADY_EXISTS / CONFIGURE_NATIVE / CONNECT_READY_MADE / SMALL_ADAPTER / NECESSARY_NEW_CODE / REJECT / UNKNOWN`; comparative evidence, SaaS vs self-host, privacy, cost and complexity.
7. `TARGET-INTEGRATION-DIFF`: specify what existing Nox module each chosen ready-made component plugs into and what does **not** change, explicit dependencies, environment, secrets, state migration, grant model, rollback.
8. `SAFE-IMPROVEMENT-LIFECYCLE`: trust boundary for learning, tooling, config and code updates (reuse ASTRA and R0; no blind self-modification).
9. `INDEPENDENT-EVALS-AND-CAPABILITY-EXAMS`: actual owner tasks and adversarial scenarios, positive/negative outcomes and evidence.
10. `OPENCODE-READY-TICKETS`: small independently verifiable work units, objective, target file/module, exact reuse version/service, wiring, tests, deliverables/commit/hash, blockers and rollback. Avoid asking OpenCode to do market research again.
11. `SKEPTICAL-INDEPENDENT-REVIEW`: major risks, duplicate parts, evidence gaps, alternatives, disagreements with our plan and go/no-go conditions.
12. `OWNER-DECISIONS-ONLY`: genuine choice requiring a human (vendor cost, trusted tenant data egress, installation, new rights, external production actions), not routine architecture questions.

All significant external claims require original publication URL, date/version, independent evidence grade. Every candidate gets source-check and applicability. Provide curated *ranked recommendations* **in addition to** the large exhaustive catalogue, so owner and OpenCode can act without reading a giant undifferentiated list. If a topic is unknown, mark `UNKNOWN` and give a safe verification method.

## 12. Scope and staging

- **Now:** write research-only recommendations, read public docs, read permitted repositories; **do not** touch ongoing R0, budgets, CLI, secrets, CI, schemas or paid providers.
- **After owner approval and R0 acceptance:** OpenCode read-only final checkout inventory + isolated tiny integration tests, then gated implementation of smallest proven gaps; run QA; owner decides release.
- **Never** claim R0 released from an observer PID, old exported main or source read alone.

### Core question for Cortex to answer

> «Какая максимальная профессиональная самостоятельность Nox достижима путём настройки уже существующего стека и подключения зрелых внешних решений, без фундаментального рефакторинга? Какие реальные missing capabilities остаются, и какие точные небольшие интеграционные задачи должен выполнить OpenCode, чтобы закрыть их с проверяемым результатом?»
