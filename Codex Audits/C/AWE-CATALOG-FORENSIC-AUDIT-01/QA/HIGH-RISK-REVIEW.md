# Independent high-risk source review

Status: **PARTIAL**. Separate auditor, same GPT family. The different-family requirement remains **NOT_SATISFIED**. All nineteen requested high-risk candidates have source-text review; none received runtime, security, production, APPROVED or INTEGRATED certification.

The review uses pinned README/license caches and six additional pinned licensing sources. Machine-readable details, source URLs, blob SHAs and cache checksums are in `HIGH-RISK-FINDINGS.json` and `SUPPLEMENTAL-LICENSE-EVIDENCE.json`. No upstream code was run; no live credentials were used.

## Critical conclusions

- Agent Zero metadata says NOASSERTION, but the inspected root license text is MIT. NOASSERTION is a classifier result, not absence of a license.
- Mastra, LiteLLM, Activepieces, Langfuse and Infisical are mixed core/enterprise repositories. Core permissive terms must not be applied to excluded EE features. n8n has Sustainable Use plus Enterprise terms.
- MCP Inspector and reference servers are in an MIT-to-Apache-2.0 transition with distinct documentation terms. Reference-server ownership does not establish production readiness.
- Playwright MCP and origin filters explicitly do not form a security boundary. Inspector may store secrets unencrypted when keychain support is absent.
- The current Google Workspace CLI is explicitly not an officially supported Google product. Community bridges require their own OAuth, scope and tenant-isolation tests.
- OpenSandbox records a current release signing/provenance gap. OpenHands local execution and optional conversation sandboxes must not be confused with full service/host isolation.
- Hermes README antivirus exclusions and free-tier/router headlines remain untrusted operational or promotional assertions. No antivirus protection, trust store, runtime or provider account was changed.

## Findings by candidate

### 1. agent0ai/agent-zero

Source: [pinned README](https://github.com/agent0ai/agent-zero/blob/ba9b67df0f54ac78106ae85c552ef5d2458f7c9a/README.md); HEAD `ba9b67df0f54ac78106ae85c552ef5d2458f7c9a`.

**License scope.** Root LICENSE text is MIT; GitHub metadata is NOASSERTION. Dependency/plugin licenses are outside this check.

**Documented facts.** README documents a Linux workspace in Docker, desktop launchers including Windows, persistent storage, browser/desktop access, and optional host access. It still requires a model account/key or local inference.

**Do not infer.** A Docker workspace and launcher do not establish isolation from mounted host files, safe recursive delegation, or AWE recovery. Do not run the README installer commands as part of this audit.

**Minimum next pilot.** Disposable workspace; no host secrets; demonstrate recursive delegation limits, independent QA, abort propagation, deny host-file access, and recover a checkpoint after process termination.

### 2. NousResearch/hermes-agent

Source: [pinned README](https://github.com/NousResearch/hermes-agent/blob/67664e236ddcc45824b871d575677287599af152/README.md); HEAD `67664e236ddcc45824b871d575677287599af152`.

**License scope.** MIT text and metadata agree for the inspected repository.

**Documented facts.** README currently claims native Windows as well as Linux/macOS/WSL2, and local/Docker/SSH plus hosted terminal backends. Backend selection changes the execution boundary.

**Do not infer.** Do not preserve the outdated assumption that Hermes requires WSL. Do not infer all plugins/backends work on Windows. The README assertion that an antivirus alert is a false positive is not independent malware analysis; do not operationalize its antivirus exclusion instruction.

**Minimum next pilot.** Pin a release/artifact; verify provenance separately; exercise only a disposable terminal backend on the target OS, denied paths/network and a killed/resumed session. No blanket antivirus exclusions.

### 3. mastra-ai/mastra

Source: [pinned README](https://github.com/mastra-ai/mastra/blob/6ad8e7eb9d096aa3e2c7d291aa3d4cafa5f960ef/README.md); HEAD `6ad8e7eb9d096aa3e2c7d291aa3d4cafa5f960ef`.

**License scope.** Apache-2.0 outside ee directories; Enterprise License in ee areas, including auth, agent-builder and editor. Additional pinned LICENSE.md and ee/LICENSE inspected.

**Documented facts.** README offers agents/workflows, evals, observability and Node/React/Next integration. Those are source descriptions, not proof of the installed Head behavior.

**Do not infer.** Do not label all Mastra functionality Apache-2.0/free. Enterprise production needs both an appropriate written agreement and an enabling valid license key. Existing runtime identity must be established from owning code, not a product comparison.

**Minimum next pilot.** Map the exact packages/features to licenses. Use a copy of the present Head to compare bounded recursion, cancellation, session recovery and QA separation before considering any replacement.

### 8. BerriAI/litellm

Source: [pinned README](https://github.com/BerriAI/litellm/blob/52d1c4cd80162fbf03d7f92def0cb1631f1edfd4/README.md); HEAD `52d1c4cd80162fbf03d7f92def0cb1631f1edfd4`.

**License scope.** MIT outside litellm/enterprise; that subtree has commercial terms. Root reference without extension returns 404; actual pinned license is LICENSE.md.

**Documented facts.** README documents a gateway/SDK, routing, spend tracking, virtual keys and provider integrations. Some authentication/administration functions are enterprise features.

**Do not infer.** The gateway is not a token seller or a guarantee of provider availability, payment support, cost accuracy or hard spending limits. Readme production-ready and benchmark claims are unproven for AWE.

**Minimum next pilot.** Without paid inference, use a controlled mock upstream to test timeout/retry budgets, duplicate effects, model/tool capability filters, auth and stop-on-budget. Later real inference needs its own cost authorization.

### 9. cheaper-inference/OmniRoute

Source: [pinned README](https://github.com/cheaper-inference/OmniRoute/blob/5a5894a77604e3148b0f76b14d8b0d9e4411edcb/README.md); HEAD `5a5894a77604e3148b0f76b14d8b0d9e4411edcb`.

**License scope.** MIT text and metadata agree for this source repository.

**Documented facts.** README documents eligible provider routing, free-tier pools, opt-in masking, TLS/proxy/MITM features, and exclusions for providers marked avoid.

**Do not infer.** Free-tier headlines and savings are vendor claims; they do not prove usable models, account eligibility, legal/provider permission, recurring quota, RF payment access, or quality. Do not activate trust-store/MITM installation or reuse broad OAuth/subscription tokens.

**Minimum next pilot.** Read-only configuration review first; then mock capability/failover/budget tests with one explicit allowed provider. Prove no unapproved credential forwarding, retries or route to avoid-marked providers.

### 10. stacklok/toolhive

Source: [pinned README](https://github.com/stacklok/toolhive/blob/ac4a1326dc0ab75a43c7ccd2d3932965eab24201/README.md); HEAD `ac4a1326dc0ab75a43c7ccd2d3932965eab24201`.

**License scope.** Apache-2.0 text and metadata agree for ToolHive itself; managed servers retain their own licenses.

**Documented facts.** README documents Docker/Podman/Kubernetes runtime, MCP gateway/registry, and identity/access policy when configured with an authentication source.

**Do not infer.** Containerization is not an independent code-safety audit. Do not claim per-request identity enforcement without configuring and testing its auth source. A curated registry entry is not APPROVED for AWE.

**Minimum next pilot.** Use a harmless test MCP with minimum mounts/caps and no credentials; prove deny filesystem/network/unauthenticated call, per-user access, complete audit evidence and termination.

### 11. modelcontextprotocol/inspector

Source: [pinned README](https://github.com/modelcontextprotocol/inspector/blob/488c30d9d16e4993bc548ad298eb7450f5125c93/README.md); HEAD `488c30d9d16e4993bc548ad298eb7450f5125c93`.

**License scope.** License is transitioning MIT to Apache-2.0, with retained MIT contributions and CC-BY-4.0 documentation; NOASSERTION is expected for this mixed text.

**Documented facts.** Inspector is a connect/list/call/debug tool. README says default secret storage uses OS keychain if available, otherwise a file that is unencrypted without a supplied key.

**Do not infer.** Inspector is not a sandbox, independent QA decision maker, or screenshot-diff tool. Do not assume a headless/container machine has an encrypted keychain-backed store.

**Minimum next pilot.** Inspect storage selection on the target environment using fake tokens. Verify memory-only/encrypted mode, no secret leakage into logs/exports, and negative MCP response handling.

### 12. modelcontextprotocol/servers

Source: [pinned README](https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/README.md); HEAD `e1dc4b18dbb948921da37f3d4224a628730b43b0`.

**License scope.** Same MIT-to-Apache-2.0 transition; documentation license is distinct.

**Documented facts.** Root README explicitly presents these as educational reference MCP implementations and asks users to evaluate their own security safeguards.

**Do not infer.** Official repository ownership does not make these production-ready servers or a collective audit of every third-party server. Archived servers may have newer owners/replacements.

**Minimum next pilot.** Choose one exact server and version; test allowed directories or database scopes, traversal/symlink/URI attacks, auth, cancellation and audit logs. Do not deploy the complete examples collection.

### 13. microsoft/playwright-mcp

Source: [pinned README](https://github.com/microsoft/playwright-mcp/blob/78eca85361efb545a4c0f59b6140aef0721c5412/README.md); HEAD `78eca85361efb545a4c0f59b6140aef0721c5412`.

**License scope.** Apache-2.0 text and metadata agree for the inspected MCP server.

**Documented facts.** README requires Node >=18, defaults to persistent browser profiles, documents isolated sessions, and explicitly says origin controls and Playwright MCP are not security boundaries.

**Do not infer.** Do not grant a personal browser profile to an agent or equate origin allowlists with egress isolation. Redirects and local file access require independent controls; several example modes disable browser sandboxing.

**Minimum next pilot.** Dedicated profile or isolated context, separate per concurrent agent. Test redirected egress, local-file denial, cookie separation, sensitive URL redaction, download handling and explicit approval for account-changing actions.

### 16. github/github-mcp-server

Source: [pinned README](https://github.com/github/github-mcp-server/blob/6fbcd00b2034502ba3001a49dfaf93593aee7069/README.md); HEAD `6fbcd00b2034502ba3001a49dfaf93593aee7069`.

**License scope.** MIT text/metadata in the inspected cache; API usage and account permissions remain separate.

**Documented facts.** README documents OAuth/PAT login, toolsets and exact tools, read-only filtering, and many tools with write/admin scopes. Read-only filtering takes priority in documented configuration.

**Do not infer.** An MCP connection is not blanket owner permission. A repository-readable token does not justify admin, workflow, deletion or write actions. Hosted and local implementations have different auth behavior.

**Minimum next pilot.** Start with a selected disposable repository and read-only tool allowlist plus minimal token scopes. Verify denied writes, repo boundaries, duplicate mutations/leases, secret redaction and approval semantics before any writes.

### 17. googleworkspace/cli

Source: [pinned README](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/README.md); HEAD `cd3697e07eb520056dcf142d0c7439bbb9ba32e9`.

**License scope.** Apache-2.0 source text observed.

**Documented facts.** Despite the googleworkspace organization name, README states this is not an officially supported Google product. It requires a GCP OAuth project/credentials or a supplied token and warns about oversized scope presets in testing-mode apps.

**Do not infer.** Do not promise official support, unrestricted free quotas, existing account consent, or send/write authorization. Local token encryption does not mean the agent cannot use the token with its granted powers.

**Minimum next pilot.** Separate test account/project; select only required read scopes and services. Prove tool discovery, token isolation, revocation and that mail/calendar/Drive writes stay denied until explicitly authorized.

### 18. taylorwilsdon/google_workspace_mcp

Source: [pinned README](https://github.com/taylorwilsdon/google_workspace_mcp/blob/65286d80c77589fbe43c85b870979d67794cc91c/README.md); HEAD `65286d80c77589fbe43c85b870979d67794cc91c`.

**License scope.** MIT source text observed; README dependency-wide license statements have not been independently audited.

**Documented facts.** Community Workspace MCP documents OAuth, read-only mode, service/tool filters, per-service permissions, multi-user HTTP modes and optional tracing.

**Do not infer.** Claims of secure organization hosting, no telemetry and permissive dependency licensing are source assertions. Do not infer tested tenant isolation or least privilege from OAuth 2.1 naming alone. Insecure-transport snippets are local examples.

**Minimum next pilot.** Two test users with disjoint fake data; narrow scopes/tools and read-only mode. Prove cross-user denial, correct bearer-token validation, secret storage, tool-union behavior and absence of trace-content leakage.

### 19. grab/cursor-talk-to-figma-mcp

Source: [pinned README](https://github.com/grab/cursor-talk-to-figma-mcp/blob/ddd90f3a6d454ea0b2fc29f1b084f50fd062b880/README.md); HEAD `ddd90f3a6d454ea0b2fc29f1b084f50fd062b880`.

**License scope.** MIT source text observed; API redirect resolves the original sonnylazuardi URL to grab/cursor-talk-to-figma-mcp.

**Documented facts.** Community bridge uses a Figma plugin and socket connection. README Windows/WSL instructions include binding 0.0.0.0.

**Do not infer.** Do not present this as the official Figma service or assume the socket is authenticated because it is local. Binding all interfaces can expose design-write capability. Successful node edits do not establish visual fidelity or design-system compliance.

**Minimum next pilot.** Disposable Figma document and explicit connection scope; verify origin/channel/auth handling, no other documents accessible, rollback, text fidelity and independent visual QA. Keep the socket loopback-only unless an isolated network design is tested.

### 20. activepieces/activepieces

Source: [pinned README](https://github.com/activepieces/activepieces/blob/4f4ab8973b76e474770a57d544c2fdc967d0e0e2/README.md); HEAD `4f4ab8973b76e474770a57d544c2fdc967d0e0e2`.

**License scope.** Community content is MIT; packages/ee and server API ee areas have commercial terms. Pinned enterprise terms inspected.

**Documented facts.** README describes integrations and a no-code/workflow builder, including enterprise capabilities.

**Do not infer.** Do not treat advertised enterprise RBAC/security functions as available under core MIT, or a workflow builder as proof of dynamic recursive agent orchestration. Workflows can execute account mutations through stored credentials.

**Minimum next pilot.** One deterministic adapter flow with a fake credential, explicit read-only action, error/timeout/retry tests and idempotency. Map every selected piece/dependency and enterprise feature before reuse.

### 21. n8n-io/n8n

Source: [pinned README](https://github.com/n8n-io/n8n/blob/1ae5175a008fc464cc27579b4d7613b60e203ed1/README.md); HEAD `1ae5175a008fc464cc27579b4d7613b60e203ed1`.

**License scope.** Sustainable Use License for covered main-branch content, with separate Enterprise exceptions. The text limits use/distribution; it is not an unrestricted MIT/Apache grant.

**Documented facts.** README offers visual workflows, code, approvals and self-hosted/cloud modes; root license has file/directory and branch restrictions.

**Do not infer.** Do not call the entire product unrestricted open source or assume commercial redistribution/hosted resale is allowed. Internal/personal usage and SaaS redistribution require different scope decisions.

**Minimum next pilot.** Choose exact permitted deployment/use case first. Use a disposable workflow to prove credential scoping, cancellation, retries/idempotency, export/recovery and no unsanctioned account actions.

### 22. langfuse/langfuse

Source: [pinned README](https://github.com/langfuse/langfuse/blob/9621bc46d0e67e7580f6425dea07996f347f0412/README.md); HEAD `9621bc46d0e67e7580f6425dea07996f347f0412`.

**License scope.** MIT outside listed EE directories; enterprise periphery has separate commercial terms.

**Documented facts.** README documents OpenTelemetry-based traces, evals, prompts, costs and self-hosted/cloud deployments.

**Do not infer.** Observability is not an independent QA verdict. Do not infer that traces are secret-free or that self-hosting automatically satisfies retention, tenant isolation or cost accuracy. README scale claims are not AWE load tests.

**Minimum next pilot.** Synthetic traces containing canary secrets; prove redaction before storage/export, retention/deletion and access boundaries. Check instrumented tool actions and missing-event detection independently of the system under review.

### 31. Infisical/infisical

Source: [pinned README](https://github.com/Infisical/infisical/blob/4dcb599d9455c117e7de0ac176744eb20cc37f0e/README.md); HEAD `4dcb599d9455c117e7de0ac176744eb20cc37f0e`.

**License scope.** MIT outside any EE directory; backend/src/ee/LICENSE.md specifies commercial production conditions. Not every advertised access feature is covered by core MIT.

**Documented facts.** README describes secrets, certificates, privileged access and agent access; Docker setup includes Windows instructions.

**Do not infer.** A vault product does not make end-to-end secret handling safe: agents/tools can still exfiltrate grants, environment values or output. Do not infer free entitlements for advertised approvals/enterprise policy functions.

**Minimum next pilot.** Fake secret with narrow machine identity and time-limited access; prove denial outside scope, rotation/revocation and no leak to subprocess output, model context, logs or checkpoint exports. Test backup/restore on disposable data.

### 33. opensandbox-group/OpenSandbox

Source: [pinned README](https://github.com/opensandbox-group/OpenSandbox/blob/dc4c26eaf06131c74c1067ec62e309d11f77040d/README.md); HEAD `dc4c26eaf06131c74c1067ec62e309d11f77040d`.

**License scope.** Apache-2.0 text observed; repository has moved from alibaba/OpenSandbox to opensandbox-group/OpenSandbox.

**Documented facts.** README documents Docker/Kubernetes sandboxes, code/command/file/browser access, optional Firecracker runtime and egress/vault features. It explicitly records a signing/provenance gap for current umbrella releases.

**Do not infer.** Do not state all release images are signed or all backends offer the same security boundary. A sandbox API with commands is a privileged execution service; defaults, mounts, egress and control-plane access need tests.

**Minimum next pilot.** Pin image digest; establish available signing evidence for that release. Validate no host mounts/privileged socket access, egress deny, command quota/timeouts, cancellation, checkpoint isolation and secret brokerage with a disposable payload.

### 34. OpenHands/OpenHands

Source: [pinned README](https://github.com/OpenHands/OpenHands/blob/5b40cc2da4c2bf10f6b6b00204141eab274c4255/README.md); HEAD `5b40cc2da4c2bf10f6b6b00204141eab274c4255`.

**License scope.** Root MIT source text observed for the inspected repository; cloud service and separate backends have their own terms.

**Documented facts.** Current README describes local execution by default, optional Docker sandboxes and multiple conversation sandboxes. It says conversation isolation does not sandbox the whole Canvas/automation service and shared host workspaces remain shared.

**Do not infer.** Do not reuse older product descriptions or claim all execution is containerized. A multi-agent UI does not establish mission-bounded recursion or conflict-free parallel work. Docker/local network-auth examples are conditional.

**Minimum next pilot.** Separate worktrees per agent; minimal container mounts; prove shared-directory conflicts are prevented, host/service boundary, strong session auth, approval for mutations and recovery of both conversation state and source tree.

## Historical hash result

The local source QA literal hash comparison is an **explained historical byte mismatch**, not an upstream content failure. The committed files contain LF and match pinned Git blobs; the old report hashes match a CRLF reconstruction exactly. The report retains both facts instead of manufacturing a byte-equality PASS.

## Remaining acceptance gates

All pilot descriptions above are proposed tests, **NOT_RUN**. Primary-source review supports integration planning only. Dependency/source-code audits, actual OS/backend compatibility, pricing/entitlement, account scopes, malicious-input tests, recovery and independent runtime QA remain pending. The same-family review cannot close the cross-family gate.
