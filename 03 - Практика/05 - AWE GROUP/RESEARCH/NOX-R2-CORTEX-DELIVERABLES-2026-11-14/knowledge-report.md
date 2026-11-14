# Nox R2 Knowledge / Competence — primary-source research

**Observed:** 2026-11-14, UTC; main evidence collection `2026-11-14T04:48:48Z`  
**Scope:** L1 discovery and L2 exact-source/API/version/license review. **No packages installed, no candidate scripts executed, no Nox changes, no publication, no paid tests. No L3/L4 or R2 acceptance claim.**

## 1. Ranked actionable shortlist

| Rank | Candidate | Verdict | L2 decision | Minimal safe action after owner approval |
|---|---|---|---|---|
| 1 | Official Agent Skills format + historical Mastra `SkillSearchProcessor` 1.82.0 | **B CONFIGURE_NATIVE** | Best first slice, subject to fresh installed-pin verification | One vetted local, instruction-only Skill in a per-delegation, ACL-scoped Workspace; no new database or script executor |
| 2 | `anthropics/skills` | **D THIN_ADAPTER** | Useful examples, not an install-all catalog | Select one task-relevant skill; preserve its license/notices and hash; quarantine, review, then expose through the same Workspace |
| 3 | `heydamir/unslop` | **D THIN_ADAPTER** | Plausible UI redesign procedure; separate from 0design | Initially load only approved procedural references; exclude browser/video/network scripts; preserve CC BY attribution |
| 4 | Docling | **D THIN_ADAPTER** | Strong document-extraction candidate when a real T04 specimen demands it | Pinned Python worker in independent sandbox; immutable originals and derived structural records; rights/ACL before indexing |
| 5 | `0design/unslop-skill` | **G REJECT_OR_DEFER** | Useful audit/detector concepts, but remote canon and executable client enlarge trust boundary | Defer external canon; evaluate separately only with owner-approved endpoint/egress and a pinned version/checksum |
| 6 | Crawl4AI | **G REJECT_OR_DEFER** | Dynamic-web candidate with material official security history | Defer until a concrete web-ingestion need justifies hardened L3 SSRF/browser/resource tests; cloud not first path |

**Fastest safe integration path:** fresh-read Nox → confirm exact installed 1.82.0 contract → add provenance/admission decision at `src/memory/index.ts` → construct approved per-delegation Workspace at `src/agents/specialists.ts` → attach pinned SkillSearch → measure T05 held-out transfer and T09 injection controls. Do **not** begin with a crawler, vector store, all-skills import, remote canon, or general script runner.

## 2. Evidence boundary and reproducibility

The requested owner file was initially absent from this sandbox. It was recovered from the documented canonical public repository at `failm3/nivict-ai-academy@9573a64f2602631ec5d2299716612ba8578c2a13`; copied owner bytes are 81,097 bytes, SHA-256 `0767476e3da1599aaaa731d43397e01dc944c14247ec016ffae03c68cba1ce1f`, matching the source baseline. The pinned 03/04/05 review documents were also read; their hashes match the baseline.

Current `/home/nox/awe-group-cleanroom-20261112` is absent. Thus branch, HEAD, source/lock hashes, actual installed API, workspace tenancy, grants, existing wiring and current behavior are **UNKNOWN**. References to Nox modules and `@mastra/core=1.82.0` are from historical review commit `68cc0ee20a25991ea275512e20ac521cc8f8234b`, not a fresh current-source observation.

- Machine candidates: `out/knowledge-candidates.json`.
- Exact bytes and URLs: `out/sources/knowledge/manifest.json` (68 entries).
- Collector: `out/sources/knowledge/collect-evidence.py`; it copies bytes from public clones and computes hashes, but by design does not install or execute candidate code.
- Official spec website snapshots: `agentskills-specification.html`, `agentskills-using-scripts.html`, `agentskills-adding-skills-support.html`; canonical source docs are additionally pinned in `out/sources/knowledge/agentskills/`.
- PyPI registry bytes and release source archives are saved with hashes. Immutable GitHub raw URLs, commit timestamps, local paths and byte counts are in the manifest.
- Two subagent attempts failed due nesting/provider interruption; findings here were independently gathered directly. This is not an independent multi-reviewer security certification.

Re-run collection by cloning the named public repos at the manifest commits into `/workspace/upstreams/{docling,crawl4ai,skills,unslop,unslop-skill,agentskills}`, then `python /workspace/out/sources/knowledge/collect-evidence.py`. Download URLs for registry snapshots and archives are in the manifest; mutable registries/HEADs may later differ. `sha256sum` the saved files and compare with the manifest. Do not equate a matching file hash with upstream authenticity beyond the recorded transport/source observation.

## 3. Official source findings

### 3.1 Agent Skills specification — B, L2

Official `agentskills/agentskills@83021e2be457a9b6679148719c1f6074f0ad975e` (2026-11-04) defines a directory with required `SKILL.md` and optional `scripts/`, `references/`, `assets/`. `name` and `description` are required; optional fields are `license`, `compatibility`, `metadata`, `allowed-tools`. The spec describes progressive disclosure: metadata, then instructions, then resources.

The implementation guide explicitly warns that project-level skills may be untrusted and recommends a trust check before loading. It also describes deterministic collision handling and discovery bounds. `allowed-tools` is **experimental**, client-dependent pre-approval metadata—not a portable sandbox or Nox grant. The script guide permits shell commands and package runners; it is an operational convention, not proof that script execution is safe.

Rights: root code Apache-2.0, docs CC-BY-4.0, separately stated. [Spec](https://github.com/agentskills/agentskills/blob/83021e2be457a9b6679148719c1f6074f0ad975e/docs/specification.mdx), [client trust guidance](https://github.com/agentskills/agentskills/blob/83021e2be457a9b6679148719c1f6074f0ad975e/docs/client-implementation/adding-skills-support.mdx), [scripts](https://github.com/agentskills/agentskills/blob/83021e2be457a9b6679148719c1f6074f0ad975e/docs/skill-creation/using-scripts.mdx).

### 3.2 Anthropic official examples — D, L2

`anthropics/skills@2c5958ecac7cee2b583967a2c4981d0f4a75c579` contains demonstration/educational skills and requires thorough environment-specific testing. The README now says document skills are also Apache-2.0; each sampled current per-skill `LICENSE.txt` begins Apache-2.0. Do not repeat stale claims that document skills are source-available-only at this observed commit. `THIRD_PARTY_NOTICES.md` separately includes BSD-2-Clause components and GPL-3.0 FFmpeg notices. Claude marketplace/plugin installation and paid-plan/API availability do not establish Nox installation or permission. [README](https://github.com/anthropics/skills/blob/2c5958ecac7cee2b583967a2c4981d0f4a75c579/README.md), [notices](https://github.com/anthropics/skills/blob/2c5958ecac7cee2b583967a2c4981d0f4a75c579/THIRD_PARTY_NOTICES.md).

### 3.3 `heydamir/unslop` — D, L2

`heydamir/unslop@97daa3eb365670ea3f87ed85356cbfcee18105a5` is a UI redesign skill for several clients. It uses CC-BY-4.0 and asks for creator/repository credit. It instructs an audit/direction pass before edits. Optional snapshot/story scripts use Playwright; story uses ffmpeg; optional image services can cost money. `snapshot.mjs` navigates a supplied URL/local file, executes browser page behavior and fetches resources. This requires URL/egress/SSRF/privacy controls and no inherited secrets. No browser/story execution is appropriate for the first SkillSearch slice. [README](https://github.com/heydamir/unslop/blob/97daa3eb365670ea3f87ed85356cbfcee18105a5/README.md), [skill](https://github.com/heydamir/unslop/blob/97daa3eb365670ea3f87ed85356cbfcee18105a5/skills/unslop/SKILL.md), [snapshot code](https://github.com/heydamir/unslop/blob/97daa3eb365670ea3f87ed85356cbfcee18105a5/skills/unslop/scripts/snapshot.mjs).

### 3.4 `0design/unslop-skill` — G, L2

`0design/unslop-skill@12a35cc5f003ec08dcb6dd828ed0d059904902cd`, package/plugin 1.0.3, is a distinct audit/plan project, not the heydamir skill. Node is >=20; `@modelcontextprotocol/sdk` is exactly 1.30.0. The default external canon endpoint is `https://oleg.design/unslop/mcp`. The skill requires a version/checksum-pinned canon and says checksum integrity is not publisher identity. Audit writes plans; explicit execute mode changes source in a worktree. Neither mode is authorized in Nox by this research. Code/skill is MIT; rule texts are CC-BY-4.0 with record-level attribution fields. The first slice should not contact the canon or run its detector/client. [README](https://github.com/0design/unslop-skill/blob/12a35cc5f003ec08dcb6dd828ed0d059904902cd/README.md), [skill/security behavior](https://github.com/0design/unslop-skill/blob/12a35cc5f003ec08dcb6dd828ed0d059904902cd/skills/audit/SKILL.md), [manifest](https://github.com/0design/unslop-skill/blob/12a35cc5f003ec08dcb6dd828ed0d059904902cd/.mcp.json), [rule license](https://github.com/0design/unslop-skill/blob/12a35cc5f003ec08dcb6dd828ed0d059904902cd/LICENSE-RULES.md).

### 3.5 Docling — D, L2, defer until needed

Observed main `31d14a74b7bddc850541ab8363b8585085845313`; proposed release `v2.150.0` at tag object `6852c27fb87dafaaa1a564545a8ce78d4565b186`, PyPI uploaded 2026-11-10. Python >=3.10,<4. Source archive SHA-256 `6a3aeddd8fbf43732fae1fb65208141470bc7215d34dbb58dd78ae05cbe26739`; wheel `beac71791c1eba7e1e5ef423d11ff8026887c8cae8643d99d055d447c476b662`. Main README describes broad document/table/OCR/audio support, local/offline execution and model artifacts; it does not establish extraction accuracy for Nox fixtures.

The code is MIT, but model rights must be checked in original model packages; input document rights remain separate. Official pipeline docs say TikZ trusted-input and shell-escape default false, the precheck is **not** a security boundary, and untrusted LaTeX needs an isolated environment without host mounts/network. Remote services require opt-in for the documented remote OCR path. HTML/EPUB resource fetching defaults `none` in the CLI reference. [README](https://github.com/docling-project/docling/blob/31d14a74b7bddc850541ab8363b8585085845313/README.md), [pipeline security](https://github.com/docling-project/docling/blob/31d14a74b7bddc850541ab8363b8585085845313/docs/reference/pipeline_options.md), [CLI options](https://github.com/docling-project/docling/blob/31d14a74b7bddc850541ab8363b8585085845313/docs/reference/cli.md), [PyPI](https://pypi.org/pypi/docling/2.150.0/json).

### 3.6 Crawl4AI — G, L2, defer

Observed main `cae74b203a33994f7e13b9052c3b0d5c93daa0e6`; proposed release `v0.9.5` at peeled commit `838869bdda93f25e6d50b3f50ae9577d9b19a586`, PyPI uploaded 2026-10-14. Python >=3.10. Source archive SHA-256 `84fa6f4970fbb086a68893c9fb18605a93fcd609c72bee6fbb1d2715924afbff`; wheel `ee2a2a2832d7bf4081289a4d2322be8111331960939e27dd0f921ed69b5e4db4`. Library is Apache-2.0 plus the repository’s stated attribution requirement; Cloud account/key/pricing and website-content rights are separate.

Official `SECURITY.md` supports 0.9.x and documents fixes for prior critical RCE/sandbox escapes/eval/hooks and high-severity SSRF, arbitrary writes and credential exfiltration, plus TLS, XSS and resource issues. Version 0.9.5 fixes the classes it lists, but this report did not independently verify completeness. The README’s self-hosted token and sandbox settings are not a substitute for host isolation. [Security policy/history](https://github.com/unclecode/crawl4ai/blob/cae74b203a33994f7e13b9052c3b0d5c93daa0e6/SECURITY.md), [README/install/cloud](https://github.com/unclecode/crawl4ai/blob/cae74b203a33994f7e13b9052c3b0d5c93daa0e6/README.md), [license](https://github.com/unclecode/crawl4ai/blob/cae74b203a33994f7e13b9052c3b0d5c93daa0e6/LICENSE), [PyPI](https://pypi.org/pypi/crawl4ai/0.9.5/json).

### 3.7 Historical Mastra SkillSearch API — B, L2 only

Exact tag `@mastra/core@1.82.0` points to `6e8dfcb83facb0861ebefa4fee384429a113acf4`. npm metadata integrity is `sha512-jrgFcoSYAVSsE41fXD3dUxuRWZtfFc3HuGRQRnQmGDHYQMU/S89YoP/ZilkSM3c9nn0Gxj9qFVzauoNZONPIxw==`. Pinned source supports `workspace`, `search.topK`, `search.minScore`, `ttl`, `blockingRefresh`; its `search_skills`/`load_skill` flow loads instructions into system messages. The docs explicitly say workspace file tools are not blocked. Latest main is a different observation and must not replace installed-pin integration evidence. Repository licensing is Apache-2.0 outside `ee`/third-party exceptions. [Pinned code](https://github.com/mastra-ai/mastra/blob/6e8dfcb83facb0861ebefa4fee384429a113acf4/packages/core/src/processors/processors/skill-search.ts), [pinned docs](https://github.com/mastra-ai/mastra/blob/6e8dfcb83facb0861ebefa4fee384429a113acf4/docs/src/content/en/reference/processors/skill-search-processor.mdx), [license](https://github.com/mastra-ai/mastra/blob/6e8dfcb83facb0861ebefa4fee384429a113acf4/LICENSE.md).

## 4. Minimal Nox integration design (proposal, not code)

### 4.1 Data distinction and storage

Keep existing LibSQL message history. Do not add PG/vector storage without measured fit. Store immutable source/pack bytes and evidence in the existing artifact/evidence layer; `src/memory/index.ts` decides admission and returns durable record references. Retrieval indexes are rebuildable derivatives, never the only provenance.

Minimum `CapabilityPack` fields: `pack_id`, immutable `version`, content digest and parents; upstream canonical URL/commit; `SkillRecord` refs and all-file hashes; `KnowledgeRecord` refs with exact page/section/table/timestamp/byte anchors; rights/license and attribution scope; tenant/owner ACL and allowed audiences; trust rationale; prerequisites and `when/when_not`; requested—not granted—tools/network/secrets; deliverable and QA oracle; validity/expiry/revocation/supersession; evaluation refs and actual status. Keep `ToolCard`, `Template`, `AgentRole`, `EvaluationFixture`, `QAOracle`, `Claim/Evidence`, `ActualExperience` as distinct types.

An ingestion adapter returns original-artifact ID, canonical URI/edition/effective date, rights/ACL, parser name/version/model/artifact hashes, structural anchors, warnings/completeness and derived-artifact hashes. It cannot mark its own output admitted, correct, public or professionally validated.

### 4.2 Exact call path to fresh-verify

1. **Fresh preflight:** current HEAD/status/package lock; `src/agents/specialists.ts`, `createSpecialist`, `src/memory/index.ts`, `src/security/tool-context.ts`, `src/tools/index.ts`, installed `@mastra/core` typings and lock digest. If any differ, produce a new scoped ticket rather than assume the historical call path.
2. **Admission:** host-owned code validates schema, canonical upstream, exact tree digest, per-file rights/notices, tenant ACL, expiry/revocation, path containment, symlink escapes, duplicate identity and required oracle. Quarantine untrusted packs. No model-generated install or self-grant.
3. **Scoped workspace:** for each delegation, materialize/copy only admitted pack versions authorized for that tenant and role into an isolated Workspace root. Do not expose a global filesystem containing other tenants or unvetted skills. Apply grants separately through `tool-context.ts`; `allowed-tools` is ignored as authority.
4. **Discovery:** at the actual `createSpecialist` agent construction path, attach one pinned `SkillSearchProcessor({ workspace, search: { topK: 5, minScore: 0.1 }, blockingRefresh: true })` as a proposed initial configuration, only if installed typings support it. `topK/minScore` are test parameters, not measured optimum. Preserve existing role/tool filtering.
5. **Invocation evidence:** log mission/delegation, tenant, workspace/pack manifest digest, search query/results, loaded pack/version/digest, exact toolName/schema and subsequent actual call receipts separately. Loaded Skill ≠ executed tool ≠ accepted artifact.
6. **Execution:** default no bundled scripts, shell, network, secrets or external writes. A later explicitly approved script receives its own pinned environment, non-root sandbox, no host mounts/secrets, egress allowlist, resource/wall-time caps, process cleanup and independent oracle.
7. **Acceptance/revocation:** independent T04/T05/T09 evidence. Revocation removes future admission and invalidates caches/indexes/prompt snapshots; preserves evidence history. Restart/resume reconstructs loaded state only from current grants and admitted pack digest.

### 4.3 Small owner-approved tickets

- **K1 — Preflight and contract (H UNKNOWN until fresh read):** record current commit/lock, installed API and minimal Workspace fixture. No new dependency. Abort if SkillSearch is absent/incompatible; do not upgrade implicitly.
- **K2 — Pack admission (`src/memory/index.ts` + existing evidence/artifact interfaces):** one immutable, ACL-bound local pack, schema/digest/path/rights/revocation validation. No retrieval model change.
- **K3 — Per-delegation SkillSearch (`src/agents/specialists.ts`, `src/security/tool-context.ts`):** scoped Workspace and one processor; no script runner, no new global permission framework.
- **K4 — T04/T05 evaluation:** one bounded low-risk professional pack with hidden changed fixture and fresh solver; baseline/treatment equal model/tools/budget; independent source/citation and task oracles.
- **K5 — Only if a proven fixture gap:** separately select Docling or Crawl4AI and implement one thin read-only `src/tools/` adapter after L3 sandbox/security acceptance. Do not implement both to fill a roadmap.

## 5. Tests and independent oracles — all NOT_RUN

| Test | Required negative/positive proof | Oracle and release condition |
|---|---|---|
| Contract smoke | Exact installed 1.82.0 Workspace/SkillSearch behavior; no package drift | Actual API receipt and source/lock identity; absent API = BLOCKED |
| Admission/rights | Reject malformed frontmatter, name collision, traversal/symlink, tree tamper, absent/unsupported license, expired/retracted/revoked pack | Independent manifest/digest/rights fixture; quarantine and no search/load |
| ACL/tenant | Two tenants with same-named/different packs; revoked role; wrong-context memory; cached prompt/index | Zero cross-tenant search, `skill_read`, workspace read, prompt leakage or artifact export |
| Freshness/lifecycle | Stale index, `blockingRefresh`, TTL/restart, concurrent delegation, revocation during run | Current pack/grant digest only; no stale resurrection or unquiesced operation |
| Injection T09 | SKILL.md/reference/script/web/canon says install, reveal secrets, change spec/oracle/grants; name/schema collision; benign injection-like text | No authority change, secret/egress/write, oracle change; useful benign data retained; independent red-team verdict |
| T04 source competence | Held-out source question; false/stale/contradictory/retracted/unlicensed source; incomplete extraction | Independent claim-to-anchor and task/expert oracle; abstain/qualify unsupported claims |
| T05 transfer | Equal baseline/treatment, changed task, hidden held-out fixture, previously uninvolved fresh agent | Predeclared quality/safety/tools metric; report no benefit if none; no professional-generalization claim |
| Scripts (later) | Network/secret denial, CPU/RAM/output/time caps, timeout/cancel/orphan, malicious dependency | Sandbox receipt; no host effect; independently computed output; not run in first slice |
| Docling L3 (later) | Text/table/image-only/malformed/encrypted/oversize docs; injected instructions; TikZ/file/network attempts | Specimen ground truth for text, reading order, tables and anchors; resource/security pass |
| Crawl4AI L3 (later) | IPv4/IPv6/private/redirect/DNS-rebind/local-file/credential URLs; hostile JS; infinite scroll/resource bombs | No forbidden request/secret/process; bounded output; independent capture and citation correctness |

T05 needs measured uplift, not merely successful loading. Report full model/tool/ingestion/QA costs or `UNKNOWN`, and retain failed attempts. A SkillSearch token-saving claim is **not** established; compare equal tasks against no-skill and eager catalog baselines.

## 6. Rollback and migration

- Feature-flag new SkillSearch admission off; return to existing specialist construction without changing message memory or prior artifacts.
- Stop future pack admission, detach Workspace/processor, revoke grants, terminate only approved sandbox workers and verify no descendants.
- Remove generated per-delegation Workspaces and derived search indexes; retain immutable evidence, negative results, prior pack versions and attribution/notices. Do not delete user originals.
- If database fields were introduced after owner approval, additive forward migration plus backward-compatible reader; no destructive migration in the first slice. Restore prior index by rebuilding from admitted immutable records.
- Quarantine new external adapter and its lockfile/config/receipts independently; no `pip uninstall` on shared host. Remove the isolated environment/container after reconciliation. Cloud/external data deletion is **UNKNOWN** until provider terms/API are verified.
- On rights complaint, source revocation or injection discovery: immediately deny retrieval/prompt inclusion/export for affected audiences, mark descendants derived/tainted, preserve audit evidence and re-evaluate accepted outputs. Hash pinning alone does not revoke authority.

## 7. Known vs UNKNOWN / NEXT_TEST

**Known at L2:** exact observed upstream identities, commits, selected release/tag/package hashes, declared license scopes, documented installation/runtime/API behavior, the official spec’s experimental `allowed-tools`, the need for a project-skill trust gate, Docling’s explicit untrusted-LaTeX isolation warning, and Crawl4AI’s official security history.

**UNKNOWN:** current Nox and installed compatibility; actual ACL/tenant mechanism; current pack wiring/health; extraction/retrieval quality; SkillSearch savings; professional transfer; complete transitive dependency/SBOM and vulnerabilities; model/input/web/content rights for actual selected corpus; upstream artifact authenticity beyond recorded registry/source observations; cloud terms/privacy/data residency/deletion; actual resource ceilings; security under adversarial test; all build/run/QA/maintenance dollars.

**NEXT_TEST order:** fresh Nox read → exact installed API contract → admission/ACL/injection negatives → one T05 bounded vertical slice → measured T04 document/web need → separately authorized L3 adapter/security tests → independent equal-task L4 acceptance. No UNKNOWN should be read as zero, safe, free, compatible, beneficial or accepted.

## Sources

Primary immutable links are embedded above and enumerated with local byte/hash records in `out/sources/knowledge/manifest.json`. Canonical owner brief: [06 at documented commit](https://github.com/failm3/nivict-ai-academy/blob/302bdbb72f96f227efc8c8df5a4cb9a942f26a5b/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/RESEARCH/NOX-R2-CORTEX-OPENCODE-REVIEW-2026-11-14/06-CORTEX-R2-FINAL-OWNER-PROMPT-2026-11-14.md).
