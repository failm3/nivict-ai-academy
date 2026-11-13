# Приоритетные технологии: 50 технических desk reviews

**PARTIAL.** 49 репозиториев + официальный Figma MCP. Это анализ документации/лицензий с ограниченным чтением кода, не 50 runtime/security-аудитов. Для добавленных 9 репозиториев даты релизов отдельно не исследованы; pinned HEAD/README/LICENSE и repository metadata сохранены.

Для всех решений: установки и upstream code execution не выполнялись; AWE acceptance NOT_PROVEN, APPROVED=0. REUSE означает рекомендацию использовать существующий компонент после проверок, а не допуск в runtime. Cross-family QA NOT_SATISFIED. Кандидаты вне исходных URL архива явно помечены.

## 1. agent0ai/agent-zero

**Решение: PILOT.** Создание и возобновление дочерних контекстов, terminal/browser/desktop executor

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `ba9b67df0f54ac78106ae85c552ef5d2458f7c9a`.

Подключение и требования: Docker/Linux workspace; Windows launcher documented; model backend.

Лицензия: MIT. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: call_subordinate validates available profiles; profile creation and full AWE governance need separate proof.

Минимальная приёмка: Создать новый профиль по неизвестной миссии, дочернего и внучатого агента; resume context_id, cancel, depth/concurrency/budget denial, crash recovery.

Источники: [readme](https://github.com/agent0ai/agent-zero/blob/ba9b67df0f54ac78106ae85c552ef5d2458f7c9a/README.md), [license](https://github.com/agent0ai/agent-zero/blob/ba9b67df0f54ac78106ae85c552ef5d2458f7c9a/LICENSE).

Активность: commit date `2026-11-01T21:10:32Z`; последний наблюдаемый релиз `v2.15` (2026-11-01T23:52:00Z). Релизный бинарник не проверялся.

## 2. NousResearch/hermes-agent

**Решение: PILOT.** Skills, isolated conversations and leaf/orchestrator delegation primitives

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `67664e236ddcc45824b871d575677287599af152`.

Подключение и требования: CLI/gateway, selectable terminal backend; native Windows/WSL/Linux documented.

Лицензия: MIT. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Backend defines isolation; README antivirus exclusion is not malware analysis or an accepted operating instruction.

Минимальная приёмка: Два параллельных изолированных child, вложенный orchestrator, запрет инструментов/путей, остановка и восстановление без дублирования эффекта.

Источники: [readme](https://github.com/NousResearch/hermes-agent/blob/67664e236ddcc45824b871d575677287599af152/README.md), [license](https://github.com/NousResearch/hermes-agent/blob/67664e236ddcc45824b871d575677287599af152/LICENSE).

Активность: commit date `2026-11-12T11:46:33Z`; последний наблюдаемый релиз `v0.23.1` (2026-11-10T01:42:15Z). Релизный бинарник не проверялся.

## 3. mastra-ai/mastra

**Решение: REUSE.** Agents, structured output, graph workflows with branch/parallel, memory, eval/trace interfaces

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `6ad8e7eb9d096aa3e2c7d291aa3d4cafa5f960ef`.

Подключение и требования: TypeScript/Node; existing Head first, adapter to its exact pinned packages.

Лицензия: Apache-2.0 core; Mastra Enterprise in ee/. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Published AWE main lacks current cleanroom Head; EE production entitlement and actual package versions require proof.

Минимальная приёмка: На копии текущего Head: неизменяемое ТЗ, новая/возобновлённая миссия, bounded delegation, suspend/resume and independent critical gate.

Источники: [readme](https://github.com/mastra-ai/mastra/blob/6ad8e7eb9d096aa3e2c7d291aa3d4cafa5f960ef/README.md), [license](https://github.com/mastra-ai/mastra/blob/6ad8e7eb9d096aa3e2c7d291aa3d4cafa5f960ef/LICENSE.md).

Активность: commit date `2026-11-12T14:05:50Z`; последний наблюдаемый релиз `@mastra/core@1.82.0` (2026-11-04T10:59:56Z). Релизный бинарник не проверялся.

## 4. langchain-ai/langgraph

**Решение: DEFER.** Stateful orchestration, persistence, interrupts and subgraph building blocks

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `b4cb0f19e3d8984e8a57f85667b8d1bec018f0ab`.

Подключение и требования: Python SDK, explicit graph/checkpointer/storage integration.

Лицензия: MIT core; managed services separate. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: SDK requires engineering; MIT core is not a grant for every deployment service; effects still need idempotency.

Минимальная приёмка: Kill a persisted workflow between effect and acknowledgement; replay must produce one effect and preserve Owner criteria.

Источники: [readme](https://github.com/langchain-ai/langgraph/blob/b4cb0f19e3d8984e8a57f85667b8d1bec018f0ab/README.md), [license](https://github.com/langchain-ai/langgraph/blob/b4cb0f19e3d8984e8a57f85667b8d1bec018f0ab/LICENSE).

Активность: commit date `2026-11-12T01:43:53Z`; последний наблюдаемый релиз `sdk==0.4.14` (2026-11-06T03:03:34Z). Релизный бинарник не проверялся.

## 5. agno-agi/agno

**Решение: PILOT.** Agents, teams, workflows, storage and control interfaces

Привязка к архиву: Радар-3152. Версия: `dc03a2c6f1dd760f2ead89140ea946321fb211e4`.

Подключение и требования: Python/AgentOS REST and MCP; PostgreSQL storage; telemetry configuration.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Teams do not prove arbitrary dynamic recursion; hosted control and model costs are separate; verify telemetry choice.

Минимальная приёмка: Same sealed recursion/resume/budget mission as Mastra and Agent Zero; compare artifacts and operator effort.

Источники: [readme](https://github.com/agno-agi/agno/blob/dc03a2c6f1dd760f2ead89140ea946321fb211e4/README.md), [license](https://github.com/agno-agi/agno/blob/dc03a2c6f1dd760f2ead89140ea946321fb211e4/LICENSE).

Активность: commit date `2026-11-12T14:01:27Z`; последний наблюдаемый релиз `v3.1.12` (2026-10-29T14:00:55Z). Релизный бинарник не проверялся.

## 6. microsoft/agent-framework

**Решение: DEFER.** Agent and workflow SDK with orchestration primitives

Привязка к архиву: Радар-1187. Версия: `30285709c1d60736a9b8b8ad87cd4f94a3719f6a`.

Подключение и требования: Python or .NET SDK; application composition required.

Лицензия: MIT. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Not a preconfigured AWE operator product; cross-language stack adds support burden.

Минимальная приёмка: Prove one model/tool adapter and checkpoint contract before considering replacement of the current Head.

Источники: [readme](https://github.com/microsoft/agent-framework/blob/30285709c1d60736a9b8b8ad87cd4f94a3719f6a/README.md), [license](https://github.com/microsoft/agent-framework/blob/30285709c1d60736a9b8b8ad87cd4f94a3719f6a/LICENSE).

Активность: commit date `2026-11-12T13:35:49Z`; последний наблюдаемый релиз `python-1.25.0` (2026-11-07T15:52:42Z). Релизный бинарник не проверялся.

## 7. camel-ai/camel

**Решение: DEFER.** Agent cooperation and task decomposition building blocks

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `0366b64bf3609c76f50e396715aab73ba58a930c`.

Подключение и требования: Python SDK/workforce integration and configured model/tools.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Workforce description does not establish durable crash recovery or per-project policy.

Минимальная приёмка: Dynamically decompose a new mission, enforce resource limits, recover state and pass blind QA.

Источники: [readme](https://github.com/camel-ai/camel/blob/0366b64bf3609c76f50e396715aab73ba58a930c/README.md), [license](https://github.com/camel-ai/camel/blob/0366b64bf3609c76f50e396715aab73ba58a930c/LICENSE).

Активность: commit date `2026-11-09T10:25:05Z`; последний наблюдаемый релиз `v0.2.90` (2026-03-22T08:37:36Z). Релизный бинарник не проверялся.

## 8. BerriAI/litellm

**Решение: PILOT.** Model routing, retries, virtual keys and spend instrumentation

Привязка к архиву: Радар-1437. Версия: `52d1c4cd80162fbf03d7f92def0cb1631f1edfd4`.

Подключение и требования: Python SDK or local OpenAI-compatible gateway; provider keys separate.

Лицензия: MIT outside litellm/enterprise; enterprise terms excluded. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Gateway is not a token seller; entitlement, provider capability, double retry and budget overshoot require testing.

Минимальная приёмка: Mock upstream: tool/vision/JSON compatibility, streaming, 429/timeouts, bounded fallback, stop-on-budget and no credential forwarding.

Источники: [readme](https://github.com/BerriAI/litellm/blob/52d1c4cd80162fbf03d7f92def0cb1631f1edfd4/README.md), [license](https://github.com/BerriAI/litellm/blob/52d1c4cd80162fbf03d7f92def0cb1631f1edfd4/LICENSE).

Активность: commit date `2026-11-12T09:10:23Z`; последний наблюдаемый релиз `v1.109.1` (2026-11-12T02:07:01Z). Релизный бинарник не проверялся.

## 9. cheaper-inference/OmniRoute

**Решение: PILOT.** Provider routing/fallback and optional context compression interfaces

Привязка к архиву: iirepresent-0146, Радар-0621. Версия: `5a5894a77604e3148b0f76b14d8b0d9e4411edcb`.

Подключение и требования: Node gateway; original URL now cheaper-inference/OmniRoute.

Лицензия: MIT. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Free/savings claims unmeasured; avoid MITM/trust-store changes and broad subscription/OAuth credential reuse.

Минимальная приёмка: Read existing config first; mock one allowlisted upstream, no secret forwarding, bounded retries; compare quality before enabling compression.

Источники: [readme](https://github.com/cheaper-inference/OmniRoute/blob/5a5894a77604e3148b0f76b14d8b0d9e4411edcb/README.md), [license](https://github.com/cheaper-inference/OmniRoute/blob/5a5894a77604e3148b0f76b14d8b0d9e4411edcb/LICENSE).

Активность: commit date `2026-11-12T09:58:01Z`; последний наблюдаемый релиз `v3.8.53` (2026-11-06T10:53:35Z). Релизный бинарник не проверялся.

## 10. stacklok/toolhive

**Решение: PILOT.** MCP runtime, access and registry primitives

Привязка к архиву: Радар-2978. Версия: `ac4a1326dc0ab75a43c7ccd2d3932965eab24201`.

Подключение и требования: Go CLI/gateway with Docker/Podman/Kubernetes; each managed server separately licensed.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Containers and curated listings are not source audits or AWE approval; runtime auth must be configured.

Минимальная приёмка: Harmless MCP only: deny unauthenticated calls, cross-project paths/egress and excess capabilities; record actor/project/tool version.

Источники: [readme](https://github.com/stacklok/toolhive/blob/ac4a1326dc0ab75a43c7ccd2d3932965eab24201/README.md), [license](https://github.com/stacklok/toolhive/blob/ac4a1326dc0ab75a43c7ccd2d3932965eab24201/LICENSE).

Активность: commit date `2026-11-12T14:01:45Z`; последний наблюдаемый релиз `v0.64.0` (2026-11-10T11:46:58Z). Релизный бинарник не проверялся.

## 11. modelcontextprotocol/inspector

**Решение: REUSE.** MCP list/call/protocol debugging

Привязка к архиву: Радар-1349. Версия: `488c30d9d16e4993bc548ad298eb7450f5125c93`.

Подключение и требования: Node inspection UI/CLI; fake credentials only.

Лицензия: MIT-to-Apache-2.0 transition; retained MIT and CC-BY-4.0 docs. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Not a sandbox or visual examiner; keychain fallback may store unencrypted secrets.

Минимальная приёмка: Malformed responses/timeouts and tool schemas; inspect actual secret-storage backend using canaries and verify redacted logs.

Источники: [readme](https://github.com/modelcontextprotocol/inspector/blob/488c30d9d16e4993bc548ad298eb7450f5125c93/README.md), [license](https://github.com/modelcontextprotocol/inspector/blob/488c30d9d16e4993bc548ad298eb7450f5125c93/LICENSE).

Активность: commit date `2026-11-12T00:40:59Z`; последний наблюдаемый релиз `2.15.0` (2026-11-12T00:46:29Z). Релизный бинарник не проверялся.

## 12. modelcontextprotocol/servers

**Решение: DEFER.** Reference MCP implementations and protocol examples

Привязка к архиву: Радар-2476. Версия: `e1dc4b18dbb948921da37f3d4224a628730b43b0`.

Подключение и требования: Select one exact reference server and its runtime.

Лицензия: MIT-to-Apache-2.0 transition; docs distinct. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Educational/reference status is not production assurance; no bulk enablement.

Минимальная приёмка: One server: traversal/symlink/URI tests, narrow roots, auth, cancellation and evidence; inspect its own license/dependencies.

Источники: [readme](https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/README.md), [license](https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/LICENSE).

Активность: commit date `2026-11-11T06:50:30Z`; последний наблюдаемый релиз `v2.4.0` (2026-11-11T07:07:16Z). Релизный бинарник не проверялся.

## 13. microsoft/playwright-mcp

**Решение: PILOT.** Accessibility-based browser tools and screenshots

Привязка к архиву: Радар-3084. Версия: `78eca85361efb545a4c0f59b6140aef0721c5412`.

Подключение и требования: Node >=18 per README; browser binary; isolated or dedicated profile.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Explicitly not a security boundary; origin filters do not secure redirects; persistent profiles risk cookie sharing.

Минимальная приёмка: Two viewports + DOM assertions; separate profiles per agent, deny local files and redirected egress, verify download handling.

Источники: [readme](https://github.com/microsoft/playwright-mcp/blob/78eca85361efb545a4c0f59b6140aef0721c5412/README.md), [license](https://github.com/microsoft/playwright-mcp/blob/78eca85361efb545a4c0f59b6140aef0721c5412/LICENSE).

Активность: commit date `2026-11-11T18:08:38Z`; последний наблюдаемый релиз `v0.0.85` (2026-11-09T18:28:53Z). Релизный бинарник не проверялся.

## 14. ChromeDevTools/chrome-devtools-mcp

**Решение: PILOT.** Console, network and browser-performance debugging

Привязка к архиву: Радар-1491. Версия: `83d2ba4dde9663a8cd0bdb8af6c99fea50726003`.

Подключение и требования: Node/Chrome versions per pinned package; isolated Chrome debugging session.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Debugger can expose page secrets; no automatic visual or security acceptance.

Минимальная приёмка: Collect one trace/error/screenshot from a disposable app; enforce profile separation and redact headers/tokens.

Источники: [readme](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/83d2ba4dde9663a8cd0bdb8af6c99fea50726003/README.md), [license](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/83d2ba4dde9663a8cd0bdb8af6c99fea50726003/LICENSE).

Активность: commit date `2026-11-12T06:58:55Z`; последний наблюдаемый релиз `chrome-devtools-mcp-v1.13.0` (2026-11-11T12:40:09Z). Релизный бинарник не проверялся.

## 15. browser-use/browser-use

**Решение: DEFER.** Browser-agent planning and interaction

Привязка к архиву: iirepresent-0664. Версия: `7fdd63c03fd342aab4fe44507c77c3221ffd43c6`.

Подключение и требования: Python, browser backend and configured model/vision provider.

Лицензия: MIT. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Extra inference/latency and credential exposure; do not replace deterministic tests with agent prose.

Минимальная приёмка: Same browser task against Playwright baseline; measure completion, calls and cost with separately authorized model budget.

Источники: [readme](https://github.com/browser-use/browser-use/blob/7fdd63c03fd342aab4fe44507c77c3221ffd43c6/README.md), [license](https://github.com/browser-use/browser-use/blob/7fdd63c03fd342aab4fe44507c77c3221ffd43c6/LICENSE).

Активность: commit date `2026-11-11T00:05:55Z`; последний наблюдаемый релиз `1.0.2` (2026-11-11T04:00:00Z). Релизный бинарник не проверялся.

## 16. github/github-mcp-server

**Решение: PILOT.** Repository, issue and coding-workflow tool integration

Привязка к архиву: Радар-3090. Версия: `6fbcd00b2034502ba3001a49dfaf93593aee7069`.

Подключение и требования: OAuth/PAT; remote MCP or Go/container local server; exact toolsets.

Лицензия: MIT. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Read access is not write/admin permission; connector availability in Codex does not prove AWE integration.

Минимальная приёмка: Disposable repository with read-only token/allowlist; prove denied writes and repo boundaries, then test leased/idempotent writes only if authorized.

Источники: [readme](https://github.com/github/github-mcp-server/blob/6fbcd00b2034502ba3001a49dfaf93593aee7069/README.md), [license](https://github.com/github/github-mcp-server/blob/6fbcd00b2034502ba3001a49dfaf93593aee7069/LICENSE).

Активность: commit date `2026-11-09T14:28:25Z`; последний наблюдаемый релиз `v2.1.0` (2026-11-03T11:11:41Z). Релизный бинарник не проверялся.

## 17. googleworkspace/cli

**Решение: PILOT.** Discovery-driven Google Workspace API CLI and agent-facing commands

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `cd3697e07eb520056dcf142d0c7439bbb9ba32e9`.

Подключение и требования: Rust CLI/npm distribution; Node >=18 for npm install; GCP OAuth project.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: README says not officially supported Google product; broad test-mode scope presets can fail.

Минимальная приёмка: Dedicated test user, chosen read scopes/services, revocation and token isolation; deny mail/calendar/Drive mutation.

Источники: [readme](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/README.md), [license](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/LICENSE).

Активность: commit date `2026-10-30T15:47:59Z`; последний наблюдаемый релиз `v0.22.5` (2026-03-31T18:53:24Z). Релизный бинарник не проверялся.

## 18. taylorwilsdon/google_workspace_mcp

**Решение: PILOT.** Workspace tools, service filters, read-only and multi-user modes

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `65286d80c77589fbe43c85b870979d67794cc91c`.

Подключение и требования: Python >=3.10, OAuth and enabled Google APIs; stdio/HTTP MCP.

Лицензия: MIT. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Community implementation; OAuth version and README claims do not prove tenant isolation or dependency licensing.

Минимальная приёмка: Two disjoint test users: cross-user denial, token audience/issuer, tool filters, secret storage and no content leakage.

Источники: [readme](https://github.com/taylorwilsdon/google_workspace_mcp/blob/65286d80c77589fbe43c85b870979d67794cc91c/README.md), [license](https://github.com/taylorwilsdon/google_workspace_mcp/blob/65286d80c77589fbe43c85b870979d67794cc91c/LICENSE).

Активность: commit date `2026-11-11T23:16:44Z`; последний наблюдаемый релиз `v2.4.2` (2026-11-12T02:48:04Z). Релизный бинарник не проверялся.

## 19. grab/cursor-talk-to-figma-mcp

**Решение: DEFER.** Read/write Figma document bridge

Привязка к архиву: iirepresent-0637. Версия: `ddd90f3a6d454ea0b2fc29f1b084f50fd062b880`.

Подключение и требования: Community Figma plugin plus socket/Bun bridge; Windows/WSL documented.

Лицензия: MIT. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Moved to grab; socket binding/auth and broad design-write access need review; prefer official service where compatible.

Минимальная приёмка: Disposable file, loopback-only connection, auth/channel isolation, rollback, text/design-token fidelity and independent visual QA.

Источники: [readme](https://github.com/grab/cursor-talk-to-figma-mcp/blob/ddd90f3a6d454ea0b2fc29f1b084f50fd062b880/README.md), [license](https://github.com/grab/cursor-talk-to-figma-mcp/blob/ddd90f3a6d454ea0b2fc29f1b084f50fd062b880/LICENSE).

Активность: commit date `2026-07-26T07:14:26Z`; последний наблюдаемый релиз `NOT_OBSERVED` (UNKNOWN). Релизный бинарник не проверялся.

## 20. activepieces/activepieces

**Решение: PILOT.** Deterministic integration flows and reusable connectors

Привязка к архиву: Радар-3154. Версия: `4f4ab8973b76e474770a57d544c2fdc967d0e0e2`.

Подключение и требования: Self-hosted workflow/connectors; per-piece credentials.

Лицензия: MIT community outside EE directories; commercial EE. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Workflow automation is not recursive AWE governance; retries can duplicate account effects.

Минимальная приёмка: One read-only connector with fake/test credentials; cancellation, timeout, retry/idempotency and exported evidence.

Источники: [readme](https://github.com/activepieces/activepieces/blob/4f4ab8973b76e474770a57d544c2fdc967d0e0e2/README.md), [license](https://github.com/activepieces/activepieces/blob/4f4ab8973b76e474770a57d544c2fdc967d0e0e2/LICENSE).

Активность: commit date `2026-11-12T13:01:42Z`; последний наблюдаемый релиз `0.93.0` (2026-11-08T14:30:22Z). Релизный бинарник не проверялся.

## 21. n8n-io/n8n

**Решение: DEFER.** Visual workflows and integrations

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `1ae5175a008fc464cc27579b4d7613b60e203ed1`.

Подключение и требования: Self-hosted or hosted workflow engine; exact permitted use case.

Лицензия: Sustainable Use License with Enterprise/branch/file exceptions. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Do not label unrestricted OSS or presume hosted resale/redistribution rights; duplicate engine may add burden.

Минимальная приёмка: Scope license first; one disposable workflow with narrow credentials, replay/idempotency and backup/restore.

Источники: [readme](https://github.com/n8n-io/n8n/blob/1ae5175a008fc464cc27579b4d7613b60e203ed1/README.md), [license](https://github.com/n8n-io/n8n/blob/1ae5175a008fc464cc27579b4d7613b60e203ed1/LICENSE.md).

Активность: commit date `2026-11-12T14:03:18Z`; последний наблюдаемый релиз `n8n@2.47.5` (2026-11-12T08:34:10Z). Релизный бинарник не проверялся.

## 22. langfuse/langfuse

**Решение: PILOT.** Traces, prompts, evaluations and cost instrumentation

Привязка к архиву: Радар-1734. Версия: `9621bc46d0e67e7580f6425dea07996f347f0412`.

Подключение и требования: OTel/SDK instrumentation; separate self-host stack or cloud.

Лицензия: MIT outside listed EE directories; commercial EE. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Not an independent examiner; traces can retain secrets; provider invoices remain authoritative for spend.

Минимальная приёмка: Canary secrets in synthetic traces: redact before export, enforce retention/ACL, detect missing tool events and compare usage ledger.

Источники: [readme](https://github.com/langfuse/langfuse/blob/9621bc46d0e67e7580f6425dea07996f347f0412/README.md), [license](https://github.com/langfuse/langfuse/blob/9621bc46d0e67e7580f6425dea07996f347f0412/LICENSE).

Активность: commit date `2026-11-12T13:47:32Z`; последний наблюдаемый релиз `v4.79.0` (2026-11-12T09:40:45Z). Релизный бинарник не проверялся.

## 23. promptfoo/promptfoo

**Решение: REUSE.** LLM evaluation and adversarial/prompt-injection scenarios

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `e4ecd0e48b08aedebe186b2ee868b0f31c62e3fe`.

Подключение и требования: Node CLI and explicit providers; deterministic vs paid judge modes separate.

Лицензия: MIT. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: A judge score is not truth or independent acceptance; generated/evaluation calls may cost money.

Минимальная приёмка: Sealed requirements, negative tool/policy cases and reproducible fixtures; any paid judge run needs a separate ceiling and authorization.

Источники: [readme](https://github.com/promptfoo/promptfoo/blob/e4ecd0e48b08aedebe186b2ee868b0f31c62e3fe/README.md), [license](https://github.com/promptfoo/promptfoo/blob/e4ecd0e48b08aedebe186b2ee868b0f31c62e3fe/LICENSE).

Активность: commit date `2026-11-12T07:12:47Z`; последний наблюдаемый релиз `0.125.1` (2026-10-25T01:53:11Z). Релизный бинарник не проверялся.

## 24. confident-ai/deepeval

**Решение: DEFER.** Evaluation metrics and Python test integration

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `debe7955c0029add96f8340e38932ae62a77907c`.

Подключение и требования: Python >=3.10 and configured evaluator/provider.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: LLM grading variance and external calls; test quality and independence require their own checks.

Минимальная приёмка: Same positive/negative corpus as Promptfoo, deterministic critical failures cannot be overridden by score; measure evaluator disagreement.

Источники: [readme](https://github.com/confident-ai/deepeval/blob/debe7955c0029add96f8340e38932ae62a77907c/README.md), [license](https://github.com/confident-ai/deepeval/blob/debe7955c0029add96f8340e38932ae62a77907c/LICENSE.md).

Активность: commit date `2026-11-11T20:11:29Z`; последний наблюдаемый релиз `python-v4.2.4` (2026-09-22T16:36:00Z). Релизный бинарник не проверялся.

## 25. pgvector/pgvector

**Решение: REUSE.** Vector search inside existing relational storage

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `66accb3af6705ea9975a33f6704f1cde50d99447`.

Подключение и требования: Extension supports PostgreSQL >=13; Windows build needs C++ toolchain; SQL interface.

Лицензия: PostgreSQL License. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Vector ranking does not establish facts or tenant ACL; no extension was installed in this audit.

Минимальная приёмка: Disposable matching PG version: pre-retrieval project auth, cross-tenant deny, recall baseline, versioned deletion and restored checkpoint.

Источники: [readme](https://github.com/pgvector/pgvector/blob/66accb3af6705ea9975a33f6704f1cde50d99447/README.md), [license](https://github.com/pgvector/pgvector/blob/66accb3af6705ea9975a33f6704f1cde50d99447/LICENSE).

Активность: commit date `2026-11-11T07:47:38Z`; последний наблюдаемый релиз `NOT_OBSERVED` (UNKNOWN). Релизный бинарник не проверялся.

## 26. supermemoryai/supermemory

**Решение: PILOT.** Memory/context ingestion and retrieval interfaces

Привязка к архиву: iirepresent-0059, Радар-1876. Версия: `8af3b9108f1a4dce45b10cfa4f8f0af027b4197b`.

Подключение и требования: Local API/container or hosted API; model/embedding backend; API key even on localhost.

Лицензия: MIT repository; service/EE terms separate. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: URL ingestion can use hosted reader; telemetry/provider paths and memory truth require control.

Минимальная приёмка: Start with text-only synthetic records; auth before retrieval, TTL/update/delete, poisoned-memory rejection and restore without duplicate facts.

Источники: [readme](https://github.com/supermemoryai/supermemory/blob/8af3b9108f1a4dce45b10cfa4f8f0af027b4197b/README.md), [license](https://github.com/supermemoryai/supermemory/blob/8af3b9108f1a4dce45b10cfa4f8f0af027b4197b/LICENSE).

Активность: commit date `2026-11-11T06:38:24Z`; последний наблюдаемый релиз `server-v0.0.9` (2026-10-12T18:59:36Z). Релизный бинарник не проверялся.

## 27. mem0ai/mem0

**Решение: DEFER.** User/session/agent memory extraction and retrieval

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `f1791daa86d469249c9b002f62644d58a1eb96a0`.

Подключение и требования: Python/JS memory layer with explicit model, embedding and vector-store configuration.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Default external providers and inferred memories can expand data exposure; provenance and approval not automatic.

Минимальная приёмка: Adversarial corrections and project isolation; compare against existing SQL+vector baseline before adding another memory store.

Источники: [readme](https://github.com/mem0ai/mem0/blob/f1791daa86d469249c9b002f62644d58a1eb96a0/README.md), [license](https://github.com/mem0ai/mem0/blob/f1791daa86d469249c9b002f62644d58a1eb96a0/LICENSE).

Активность: commit date `2026-11-06T16:53:06Z`; последний наблюдаемый релиз `ts-v3.3.1` (2026-09-25T17:36:35Z). Релизный бинарник не проверялся.

## 28. getzep/graphiti

**Решение: DEFER.** Temporal entity/fact graph framework

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `ebef986a0b2360211b65751c111cacb4a7d790eb`.

Подключение и требования: Python >=3.10; supported graph DB and LLM/embedding configuration.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Additional database and LLM extraction burden; framework is not a turnkey verified corporate memory.

Минимальная приёмка: Versioned conflicting facts, time-window queries, tenant deny, deletion and recovery; only pilot if relational baseline has a measured gap.

Источники: [readme](https://github.com/getzep/graphiti/blob/ebef986a0b2360211b65751c111cacb4a7d790eb/README.md), [license](https://github.com/getzep/graphiti/blob/ebef986a0b2360211b65751c111cacb4a7d790eb/LICENSE).

Активность: commit date `2026-11-11T01:25:27Z`; последний наблюдаемый релиз `v0.31.2` (2026-10-20T17:25:21Z). Релизный бинарник не проверялся.

## 29. DeusData/codebase-memory-mcp

**Решение: PILOT.** Code graph/navigation and code-context retrieval

Привязка к архиву: Радар-0206. Версия: `ff812bfdf07b24b94a6210ed7d6bc27d6c5b8ebd`.

Подключение и требования: Local C binary/MCP; supported OS builds claimed in README.

Лицензия: MIT. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Not corporate truth memory; indexing can ingest secrets or follow paths beyond project.

Минимальная приёмка: Index a disposable repo, deny symlinks/secrets/outside roots; check answer provenance and compare latency/tokens against text search.

Источники: [readme](https://github.com/DeusData/codebase-memory-mcp/blob/ff812bfdf07b24b94a6210ed7d6bc27d6c5b8ebd/README.md), [license](https://github.com/DeusData/codebase-memory-mcp/blob/ff812bfdf07b24b94a6210ed7d6bc27d6c5b8ebd/LICENSE).

Активность: commit date `2026-11-11T23:13:14Z`; последний наблюдаемый релиз `v0.12.1` (2026-10-16T23:35:48Z). Релизный бинарник не проверялся.

## 30. temporalio/temporal

**Решение: DEFER.** Durable workflow replay and retry primitives

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `03ecd1d228d2b8d9d433da55785afc9aeeead918`.

Подключение и требования: Temporal server plus worker SDK and persistent store.

Лицензия: MIT server; cloud terms separate. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Activities need idempotency; operational stack is material; avoid a second orchestration engine without failure evidence.

Минимальная приёмка: Crash after an external-effect stub before acknowledgement; replay yields exactly one durable effect and correct checkpoint.

Источники: [readme](https://github.com/temporalio/temporal/blob/03ecd1d228d2b8d9d433da55785afc9aeeead918/README.md), [license](https://github.com/temporalio/temporal/blob/03ecd1d228d2b8d9d433da55785afc9aeeead918/LICENSE).

Активность: commit date `2026-11-11T03:39:18Z`; последний наблюдаемый релиз `v1.32.2` (2026-11-02T18:38:48Z). Релизный бинарник не проверялся.

## 31. Infisical/infisical

**Решение: PILOT.** Secret storage and distribution primitives

Привязка к архиву: Радар-2707. Версия: `4dcb599d9455c117e7de0ac176744eb20cc37f0e`.

Подключение и требования: CLI/SDK or self-hosted vault; narrow machine identity.

Лицензия: MIT outside EE; enterprise production conditions. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Vault does not prevent downstream model/log exfiltration; some advertised features are enterprise.

Минимальная приёмка: Fake secret: scope denial, expiry/rotation/revocation, subprocess/log/model redaction and disposable restore.

Источники: [readme](https://github.com/Infisical/infisical/blob/4dcb599d9455c117e7de0ac176744eb20cc37f0e/README.md), [license](https://github.com/Infisical/infisical/blob/4dcb599d9455c117e7de0ac176744eb20cc37f0e/LICENSE).

Активность: commit date `2026-11-12T12:12:15Z`; последний наблюдаемый релиз `v0.167.8` (2026-11-10T18:04:03Z). Релизный бинарник не проверялся.

## 32. open-policy-agent/opa

**Решение: PILOT.** Reusable policy decision engine

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `1c62a3e715055a013c184fe87da6d1d5c3006bc8`.

Подключение и требования: OPA/Rego decision API or embedded policy evaluation.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Enforcement point and AWE actor/project context still need implementation; LLM prompts cannot replace it.

Минимальная приёмка: Default deny, project/tool/action matrix, immutable policy version, denied actions never invoke tool and decisions are auditable.

Источники: [readme](https://github.com/open-policy-agent/opa/blob/1c62a3e715055a013c184fe87da6d1d5c3006bc8/README.md), [license](https://github.com/open-policy-agent/opa/blob/1c62a3e715055a013c184fe87da6d1d5c3006bc8/LICENSE).

Активность: commit date `2026-11-12T10:53:02Z`; последний наблюдаемый релиз `v1.22.4` (2026-11-12T10:35:24Z). Релизный бинарник не проверялся.

## 33. opensandbox-group/OpenSandbox

**Решение: DEFER.** Code/command/file/browser sandbox lifecycle interfaces

Привязка к архиву: Радар-1331. Версия: `dc4c26eaf06131c74c1067ec62e309d11f77040d`.

Подключение и требования: Docker local/Kubernetes backend, SDKs/CLI/MCP; Python >=3.10 examples.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Moved to opensandbox-group; README records umbrella signing/provenance gap; benchmark claims not reproduced.

Минимальная приёмка: Verify selected image/binary provenance first; then deny host paths/egress, quotas, kill, cleanup and checkpoint recovery.

Источники: [readme](https://github.com/opensandbox-group/OpenSandbox/blob/dc4c26eaf06131c74c1067ec62e309d11f77040d/README.md), [license](https://github.com/opensandbox-group/OpenSandbox/blob/dc4c26eaf06131c74c1067ec62e309d11f77040d/LICENSE).

Активность: commit date `2026-11-12T14:06:17Z`; последний наблюдаемый релиз `release-1.2.0` (2026-10-27T12:50:49Z). Релизный бинарник не проверялся.

## 34. OpenHands/OpenHands

**Решение: PILOT.** Autonomous coding/operator agent interface

Привязка к архиву: Радар-1731. Версия: `5b40cc2da4c2bf10f6b6b00204141eab274c4255`.

Подключение и требования: Local default with optional agent backends/containers/VMs; exact backend matters.

Лицензия: MIT root; external components/services separate. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Local/default execution and a conversation sandbox do not isolate the whole host/Canvas.

Минимальная приёмка: One disposable checkout/backend: scoped patch, meaningful tests, artifact hashes, no host-secret access and independent review.

Источники: [readme](https://github.com/OpenHands/OpenHands/blob/5b40cc2da4c2bf10f6b6b00204141eab274c4255/README.md), [license](https://github.com/OpenHands/OpenHands/blob/5b40cc2da4c2bf10f6b6b00204141eab274c4255/LICENSE).

Активность: commit date `2026-11-12T14:00:01Z`; последний наблюдаемый релиз `v1.40.0` (2026-11-12T14:22:00Z). Релизный бинарник не проверялся.

## 35. Aider-AI/aider

**Решение: DEFER.** Code editing, repository context and test-driven iteration

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `5dc9490bb35f9729ef2c95d00a19ccd30c26339c`.

Подключение и требования: Python CLI, Git checkout and chosen model provider.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Coding worker is not recursive Head/QA; provider spend and workspace writes need bounds.

Минимальная приёмка: Same small issue as existing executor: minimal diff, tests, token ledger and rollback; compare maintenance before adding another worker.

Источники: [readme](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md), [license](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/LICENSE.txt).

Активность: commit date `2026-05-22T14:02:20Z`; последний наблюдаемый релиз `v0.86.0` (2025-08-09T17:42:19Z). Релизный бинарник не проверялся.

## 36. continuedev/continue

**Решение: DEFER.** Coding-agent source for possible reuse

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `5522c6f44ca0ac3528b37244818fbfa39b5af470`.

Подключение и требования: CLI/editor extensions; README final 2.0.0 release.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: README explicitly no longer actively maintained/read-only; recent repository activity is not a support promise.

Минимальная приёмка: Do not select a new dependency without a maintained owner/fork and security/update plan.

Источники: [readme](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/README.md), [license](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/LICENSE).

Активность: commit date `2026-07-21T04:00:09Z`; последний наблюдаемый релиз `v2.0.0-vscode` (2026-06-19T00:24:01Z). Релизный бинарник не проверялся.

## 37. upstash/context7

**Решение: PILOT.** Version-aware library documentation retrieval

Привязка к архиву: Радар-3106. Версия: `c5e26f6919055d29b8d3ead20500eb06e8036295`.

Подключение и требования: ctx7 CLI requires Node >=22.13; OAuth/API or MCP mode.

Лицензия: MIT client; hosted API terms separate. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Retrieved text remains untrusted and cannot replace compilation/tests; hosted quota/cost unknown here.

Минимальная приёмка: Pin library version, resolve correct docs, test citation/version mismatches and prompt injection; verify generated API usage in normal checks.

Источники: [readme](https://github.com/upstash/context7/blob/c5e26f6919055d29b8d3ead20500eb06e8036295/README.md), [license](https://github.com/upstash/context7/blob/c5e26f6919055d29b8d3ead20500eb06e8036295/LICENSE).

Активность: commit date `2026-11-12T11:47:48Z`; последний наблюдаемый релиз `@upstash/context7-tools-ai-sdk@1.0.4` (2026-11-12T09:03:18Z). Релизный бинарник не проверялся.

## 38. Unstructured-IO/unstructured

**Решение: DEFER.** Document partitioning and ingestion

Привязка к архиву: Радар-3165. Версия: `293d235cfcd5f5e89c3cc5ff85562005e182ae33`.

Подключение и требования: Python document parsing; format-specific system/model dependencies.

Лицензия: Apache-2.0 library; extras/models separate. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Untrusted documents, parser attack surface and model downloads; Manus attested test is not local AWE proof.

Минимальная приёмка: Small synthetic PDF/HTML corpus, malformed files, time/memory limits, deterministic provenance and zero network without approval.

Источники: [readme](https://github.com/Unstructured-IO/unstructured/blob/293d235cfcd5f5e89c3cc5ff85562005e182ae33/README.md), [license](https://github.com/Unstructured-IO/unstructured/blob/293d235cfcd5f5e89c3cc5ff85562005e182ae33/LICENSE.md).

Активность: commit date `2026-11-06T20:48:09Z`; последний наблюдаемый релиз `0.27.37` (2026-11-06T21:29:04Z). Релизный бинарник не проверялся.

## 39. huggingface/tokenizers

**Решение: REUSE.** Local tokenization primitives for supported tokenizers

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `aeaf6c9d6aa069e3f5b1cada4b15d77b067056e6`.

Подключение и требования: Rust tokenizer engine with language bindings and exact tokenizer assets.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Cannot infer proprietary chat/tool/reasoning framing or invoice from a generic tokenizer.

Минимальная приёмка: Known tokenizer vectors; per-provider capability profiles and conservative context headroom; server usage compared only in authorized live tests.

Источники: [readme](https://github.com/huggingface/tokenizers/blob/aeaf6c9d6aa069e3f5b1cada4b15d77b067056e6/README.md), [license](https://github.com/huggingface/tokenizers/blob/aeaf6c9d6aa069e3f5b1cada4b15d77b067056e6/LICENSE).

Активность: commit date `2026-11-12T13:44:44Z`; последний наблюдаемый релиз `v0.23.3` (2026-10-09T10:20:12Z). Релизный бинарник не проверялся.

## 40. PrefectHQ/fastmcp

**Решение: REUSE.** MCP adapter primitives and transport integration

Привязка к архиву: ARCHITECTURE_ADDITION_NOT_IN_ORIGINAL_PROJECT_URLS. Версия: `713042447f2db8c16dcf2f1ff5b8e837be1ea3b4`.

Подключение и требования: Python MCP server/client SDK; moved to PrefectHQ/fastmcp.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Not an approval registry or sandbox; auth/transport versions and tool permissions need tests.

Минимальная приёмка: One minimal read-only adapter: schema, auth, cancellation, bad input, context boundaries and redacted evidence.

Источники: [readme](https://github.com/PrefectHQ/fastmcp/blob/713042447f2db8c16dcf2f1ff5b8e837be1ea3b4/README.md), [license](https://github.com/PrefectHQ/fastmcp/blob/713042447f2db8c16dcf2f1ff5b8e837be1ea3b4/LICENSE).

Активность: commit date `2026-11-11T23:34:05Z`; последний наблюдаемый релиз `v4.1.8` (2026-11-10T20:44:13Z). Релизный бинарник не проверялся.

## 41. Официальный Figma MCP

**Решение: PILOT.** Official remote MCP documents design context, native canvas writes and code-to-canvas workflows

Привязка к архиву: ARCHITECTURE_ADDITION. Версия: `hosted docs 2026-11-12`.

Подключение и требования: Compatible remote MCP client and file permissions; Full seat for writes outside drafts.

Лицензия: Hosted service terms, not an OSS grant. Транзитивные зависимости не аудированы. Write beta currently free; docs say future usage charging. Existing plan/access not checked.

Ограничение: Beta/plan/client constraints; actual AWE connection and visual correctness unproven.

Минимальная приёмка: Disposable draft: read design context, make one authorized write, independent screenshot/token/layout QA and exact file rollback.

Источники: [official_documentation](https://developers.figma.com/docs/figma-mcp-server/).

## 42. cloudflare/security-audit-skill

**Решение: REUSE.** Coverage ledger, candidate validation and independent source-claim review method

Привязка к архиву: Радар-0017. Версия: `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8`.

Подключение и требования: Coding-agent skill with isolated subagents, Node validators and OS-enforced sandbox.

Лицензия: MIT. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: A methodology is not security certification; its commands/permissions are untrusted until separately admitted.

Минимальная приёмка: Use only the reviewed ledger/schema as a reference; injected false finding and uncovered trust boundary must be rejected or left unresolved.

Источники: [readme](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/README.md), [license](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/LICENSE).

## 43. vercel-labs/dev3000

**Решение: DEFER.** Combined application/browser console, network and interaction timeline

Привязка к архиву: Радар-2620. Версия: `e5573ae23a62fad58194881ef8642a7ee2b273fe`.

Подключение и требования: d3k runtime; Node >=24, pnpm/Chrome; Bun source path; remote/sandbox path macOS-only per README.

Лицензия: MIT. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Timeline is bounded/ephemeral, not durable audit; Portless may need admin; README $5-cap vs uncapped-default paths conflict, so default budget UNKNOWN.

Минимальная приёмка: Disposable profile, no trust-store changes in audit; inspect exact backend spending controls, redaction, shutdown and external durable evidence export.

Источники: [readme](https://github.com/vercel-labs/dev3000/blob/e5573ae23a62fad58194881ef8642a7ee2b273fe/README.md), [license](https://github.com/vercel-labs/dev3000/blob/e5573ae23a62fad58194881ef8642a7ee2b273fe/LICENSE).

## 44. teimurjan/blazediff

**Решение: PILOT.** Deterministic pixel/perceptual comparison for visual regression

Привязка к архиву: Радар-2875. Версия: `eafe393ce40ee22833a9aefe593ff779a7e8f8f3`.

Подключение и требования: Image-diff libraries/CLI and test-runner adapters.

Лицензия: MIT own code; embedded MILO weights Apache-2.0; reference algorithm notices differ. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Reference research-only notices do not automatically license independent implementations; no blanket rights clearance; diff is not UX acceptance.

Минимальная приёмка: Map selected package/code/weights first; fixed fonts/viewports, seeded regression and tolerated anti-alias noise; independent layout review remains required.

Источники: [readme](https://github.com/teimurjan/blazediff/blob/eafe393ce40ee22833a9aefe593ff779a7e8f8f3/README.md), [license](https://github.com/teimurjan/blazediff/blob/eafe393ce40ee22833a9aefe593ff779a7e8f8f3/LICENSE.md).

## 45. browser-use/browser-harness

**Решение: DEFER.** Browser operation through a real Chrome session

Привязка к архиву: Радар-1167. Версия: `c2420943526d41b9af6182d5c5f11b9cad506ab9`.

Подключение и требования: Browser Harness now engine inside Browser Use; CDP/CLI/MCP surfaces.

Лицензия: MIT. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Personal logged-in Chrome has broad powers; not an independent second engine or isolation boundary.

Минимальная приёмка: Reuse only after existing browser inventory; dedicated disposable profile, explicit sites/actions, cookie separation and cancellation.

Источники: [readme](https://github.com/browser-use/browser-harness/blob/c2420943526d41b9af6182d5c5f11b9cad506ab9/README.md), [license](https://github.com/browser-use/browser-harness/blob/c2420943526d41b9af6182d5c5f11b9cad506ab9/LICENSE).

## 46. microsoft/markitdown

**Решение: PILOT.** Document-to-Markdown conversion with structure preservation

Привязка к архиву: Радар-2474. Версия: `ed178952a6672abdfd35b5f9e76a80b6cefc086e`.

Подключение и требования: Python 3.10-3.14; choose format extras; narrow convert_local/stream APIs.

Лицензия: MIT. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Current-process I/O privileges and optional cloud paths; URL/ZIP/path attacks are threats to validate, not vulnerabilities established here.

Минимальная приёмка: Offline synthetic corpus, deny network/path traversal, limit recursion/file size and preserve source/page provenance.

Источники: [readme](https://github.com/microsoft/markitdown/blob/ed178952a6672abdfd35b5f9e76a80b6cefc086e/README.md), [license](https://github.com/microsoft/markitdown/blob/ed178952a6672abdfd35b5f9e76a80b6cefc086e/LICENSE).

## 47. HKUDS/LightRAG

**Решение: DEFER.** RAG indexing/retrieval and optional local backends

Привязка к архиву: Радар-1714. Версия: `9929013d1d8ead19b485a43a3ccb373e633cb5e9`.

Подключение и требования: Python >=3.11 per README; configured models/embedding/storage.

Лицензия: MIT. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Default binds all interfaces/auth off; enabling auth alone leaves API whitelist exposure; not an AWE ACL replacement.

Минимальная приёмка: Require auth, loopback and restricted API whitelist before pilot; poisoned docs, project isolation, deletion and grounded retrieval baseline.

Источники: [readme](https://github.com/HKUDS/LightRAG/blob/9929013d1d8ead19b485a43a3ccb373e633cb5e9/README.md), [license](https://github.com/HKUDS/LightRAG/blob/9929013d1d8ead19b485a43a3ccb373e633cb5e9/LICENSE).

## 48. alibaba/zvec

**Решение: DEFER.** Dense/sparse/multivector indexing without a separate server

Привязка к архиву: Радар-1691. Версия: `0e83a2b15926aeb9791222edc46760064a50e705`.

Подключение и требования: Embedded local vector engine with OS-specific SDK/build matrix and single-process writer constraint.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Do not copy performance claims to AWE; concurrency, auth and durability are not equivalent to PostgreSQL.

Минимальная приёмка: Synthetic corpus: writer/process conflicts, recall, crash/reopen, corrupt files, isolation wrapper and measured advantage over pgvector.

Источники: [readme](https://github.com/alibaba/zvec/blob/0e83a2b15926aeb9791222edc46760064a50e705/README.md), [license](https://github.com/alibaba/zvec/blob/0e83a2b15926aeb9791222edc46760064a50e705/LICENSE).

## 49. VectifyAI/PageIndex

**Решение: DEFER.** Tree/document-oriented reasoning retrieval

Привязка к архиву: Радар-1902. Версия: `2ac8694bf8fe89a3840dda9bdb88db5119b77fc4`.

Подключение и требования: Python/local or hosted document-index/search SDK; configured LLM.

Лицензия: MIT repository; cloud/subscription terms separate. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: Local mode is not offline inference; model data transfer remains; token-saving claims unmeasured and subscription auth not blanket permission.

Минимальная приёмка: Long-document gold set with exact page evidence, privacy/backend inspection, latency/token ledger and bounded retries.

Источники: [readme](https://github.com/VectifyAI/PageIndex/blob/2ac8694bf8fe89a3840dda9bdb88db5119b77fc4/README.md), [license](https://github.com/VectifyAI/PageIndex/blob/2ac8694bf8fe89a3840dda9bdb88db5119b77fc4/LICENSE).

## 50. google/langextract

**Решение: PILOT.** Structured text extraction with source-linked spans

Привязка к архиву: Радар-2132. Версия: `0e441bf77ddc3119dd0aa413322959234dd84ee5`.

Подключение и требования: Python library, few-shot schema and explicit cloud/local provider; not officially supported Google product.

Лицензия: Apache-2.0. Транзитивные зависимости не аудированы. License scope above; model/API/hosting and EE charges separate; actual AWE cost NOT_MEASURED.

Ограничение: README allows ungrounded spans with char_interval=None; schema is not truth; model cost and privacy vary.

Минимальная приёмка: Reject/filter ungrounded spans; negative documents, contradictory fields, injection, exact source offsets, abstention and deterministic critical checks.

Источники: [readme](https://github.com/google/langextract/blob/0e441bf77ddc3119dd0aa413322959234dd84ee5/README.md), [license](https://github.com/google/langextract/blob/0e441bf77ddc3119dd0aa413322959234dd84ee5/LICENSE).
