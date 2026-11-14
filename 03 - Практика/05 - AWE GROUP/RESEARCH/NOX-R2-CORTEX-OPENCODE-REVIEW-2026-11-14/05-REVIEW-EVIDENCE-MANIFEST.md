# NOX R2 review — source and evidence manifest

Дата review: 2026-11-14.
Статус: **SOURCE_READBACK / DOCS_ONLY / NOT_R2_ACCEPTANCE / NOT_RELEASE**.
Этот manifest сопровождает `03-OPENCODE-ENGINEERING-REVIEW.md` и `04-CORTEX-R2-BRIEF-REVISED-BY-OPENCODE.md`, не заменяет их. Никакие хеши ниже не аутентифицируют issuer, не повышают permissions и не являются новым тестовым прогоном.

## 1. Scope and repositories

| Объект | Зафиксированное состояние на review | Граница |
|---|---|---|
| Nox source | `/home/nox/awe-group-cleanroom-20261112`, branch `r1/dev`, `HEAD=68cc0ee20a25991ea275512e20ac521cc8f8234b`, clean `git status --short --branch` gives `## r1/dev` | Initial/final readback локального checkout. Не universal newest across hosts, not remote release. Ветка не получила от review commit/test/mutation. |
| Nox subsequent commits | В local checkout после `68cc0ee20a25991ea275512e20ac521cc8f8234b` более новых работ не обнаружено при readback | Это не доказательство отсутствия других refs/remotes/worktrees. |
| Documentation repository | `https://github.com/failm3/nivict-ai-academy`, local separate checkout `/tmp/opencode/nivict-ai-academy-r2-review`, branch `main`, initial `HEAD=189851ff4195c5ad0003b60333f144c6d3ef8555`, clean before docs writing | Read permission и local write/commit permission owner дал ранее. Authenticated GitHub write, commit identity и push не подтверждены. No push attempted. |
| Remote read | `git ls-remote` HTTPS earlier gave `main=189851ff4195c5ad0003b60333f144c6d3ef8555` | Anonymous/read proof, not current authenticated write proof, not publication. |
| Observer | Original source link `https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-14/00-34/part0000.txt` as draft historical checkpoint | Не использован как замена primary Nox source/current logs. |
| Old export | `failm3/awe-group-runtime` | Не подменяет local cleanroom production source. No dependence on its old status. |
| Input inventory 4504 | Declared originals: 1331+3173=4504; all raw files remain for Cortex | Cortex must locate/read all named raw inputs; their current availability and bytes not inventoried by this engineering review. **INDEPENDENT_COUNT=UNKNOWN**, не fabricated 4504-read claim. |

## 2. Immutable source documents

Destination directory:
`/tmp/opencode/nivict-ai-academy-r2-review/03 - Практика/05 - AWE GROUP/RESEARCH/NOX-R2-CORTEX-OPENCODE-REVIEW-2026-11-14/`.

| File | Bytes / lines | SHA-256 | Preservation/read |
|---|---:|---|---|
| `01-CORTEX-R2-BRIEF-DRAFT.md` | 37243 / 309 | `5996f876df65d2c35657e242e9ba532a25824622fe2fc2b56201a7f5fbc730f1` | Fully read; not rewritten. |
| `02-OPENCODE-ENGINEERING-REVIEW-TASK.md` | 8769 / 76 | `4230d33b0b633bac784502e2e40eb65bd5f15fdd178f87754a9183701f48bd1d` | Fully read; controls exact requested files/no implementation; not rewritten. |

`03`, `04`, `05` newly created. Промежуточные staging bytes replaced только внутри нового `03` до финальной записи, не original input. Generated-file hashes приводятся в последнем разделе после readback. `05` не помещает собственный SHA-256 внутрь себя: такое значение меняется при записи; external final readback supplies it.

## 3. Nox dependency evidence

Данные `package.json`, `package-lock.json` и локально установленных package documents:

| Dependency | Exact observed pin/version | Evidence boundary |
|---|---|---|
| `@mastra/core` | `1.82.0` | Actual typings/docs inspected; this does not make processors Nox-wired/callable. |
| `@mastra/memory` | `1.41.0` | Version inspected; broad learned competence not inferred. |
| `@mastra/libsql` | `1.29.0` | Version inspected; current message memory not knowledge/ACL registry. |
| `@mastra/mcp` | `2.8.0` | Version inspected; no new real MCP invocation in this review. |
| `@playwright/test` | `1.49.1` | Host verifier dependency; recorded web host browser was `158.0.8127.18`, not proof of current `@playwright/mcp` compatibility. |
| `@playwright/mcp` | Not direct manifest dependency; absent in lockfile at this revision | Current `npx @playwright/mcp` runtime bootstrap unpinned; install/safety/lifecycle remains gap. |

Local documentation evidence is tied to exact source bytes below, not unstable latest web docs. Installed `ToolSearchProcessor` constructor and phase/filter semantics are documented in `.d.ts` and packaged docs. `SkillSearchProcessor`/Workspace instructions require own version-specific sandbox proof; neither native processor shown wired in `createSpecialist` at reviewed HEAD.

## 4. Inspected Nox source — SHA-256

Все пути в следующей таблице — относительно `/home/nox/awe-group-cleanroom-20261112`. Это **readback of bytes actually consulted**, не blanket assertion every function of every file manually executed/verified. Where specific lines used, they are cited in 03; hashes protect against source drift and future ambiguous references.

| Path | SHA-256 |
|---|---|

| `package.json` | `aecfd4ecc1c68b6d48dcbf55a3395f0aa86ff779811a976577ea030a7d7468f7` |
| `package-lock.json` | `9a7af16588ff329ab5b901216390156f562aef20e07f8bbc6efdf3012e9d24f3` |
| `src/types/index.ts` | `f3378fa98143febb71ee8cf6d0b7a8110b0ae565065db8c46c33840e1bda7eca` |
| `src/agents/prompt-master.ts` | `8b4bd31a31c7fd6aa3ef316b64fe7f4b38a52b501b28a596711fcf6356f7a008` |
| `src/agents/head-agent.ts` | `f6d3b901b93bac54c8f1802bbca6e5c890b8b3be7344cb1f1f4d643d1f64c55d` |
| `src/agents/mission-manager.ts` | `00c5475c03fdf3809aeeca76d68c5c0cd50e82240c990048daa6c7fe28ea7dfc` |
| `src/agents/specialists.ts` | `1f0c2e115d1305ceba929a173abd37c7490172cc59e42a1567450c1e4bf4e9aa` |
| `src/agents/recursion.ts` | `6154aead6a7a7ff84afb0fe74f0f1b83445efae46c3c9c5437b69eb3971938fd` |
| `src/agents/qa-agent.ts` | `b60f79970f4204176fb7692987c7f4615c833e06c5301dfd0214cd68fc5796c6` |
| `src/agents/qa-gate.ts` | `ba881eebacecd1b37b48c292da0ab55910cea4e0665b0481f6f80fbfd14c8e48` |
| `src/agents/web-qa.ts` | `8513d2fef0f91fbf684310b6518cd58b8f6b0e7b84309174695588c502196b65` |
| `src/agents/csv-qa.ts` | `e1afe00348a35108b202c2634644787a902db3dfa2aea0ba06e368d48c9b5ce6` |
| `src/agents/lifecycle.ts` | `dc9647586704ae23cc5c7285f5e9d87bc4fdfab09e9a73c2aef3bd3add334aa0` |
| `src/config/models.ts` | `dfd1ff36df4a306c293625afc53d1f2281a741db0596f0cfc6d0b6e058ed7928` |
| `src/config/mcp.ts` | `57152cfc16f03a3b1709c00657aa90092e938c1b4e4880d7ba855b1dc4c8eb7f` |
| `src/config/mission-policy.ts` | `b86ee168206855163e6924222300be0f2c139c1f080e962bba51a784c6001cd0` |
| `src/memory/index.ts` | `727c1b666ae14f88d9413ce08328a3ba7d865c764c1c8570fd51394214cb6e1a` |
| `src/tools/index.ts` | `c050fbecb0c50851ee8406a6001a28091c40f97bad97630626daba7ee1428026` |
| `src/tools/browser.ts` | `3355b6ea7f19dfaca0078451fb3793345cc68594373b1ecd2cda7235e6adb4b8` |
| `src/tools/ti-search.ts` | `4d15f23c563954b6e7fe4a623694b0d110908f6abf94d14c1fbe23f7cbce097c` |
| `src/tools/manus-search.ts` | `0397d72a31fe242da0eb1dbc03c72c668c86ada5d56bb94cd079bfea6844922c` |
| `src/tools/csv-analytics.ts` | `6a5a50a80c4b1325a0ac4340e19944168c206f657b38362cabae01564611c5d5` |
| `src/capabilities/web-product.ts` | `c6c45e292cef59796d3d664baa014c4e812bc42aad192eefff87d7f7556a94fb` |
| `src/capabilities/csv-analytics.ts` | `524fb0232ca33aa6b005434de4ce0b5f35548d9040188fa03a3adc4308ae9979` |
| `src/capabilities/csv-verifier.ts` | `a663cee200fd23347c95a11cf968bee537a5386daaaf6504423c3289d6d5dc04` |
| `src/capabilities/analytics-mission.ts` | `39d9704e19819329c7fe285921cd40b7941d5bbcafdfeefc66fb18e2426f4a6c` |
| `src/security/workspace-fs.ts` | `d7ecdc94d94e1be8348ad5a8f7af5130a5e523388f2446195c2cce3c19d2b07c` |
| `src/security/tool-context.ts` | `d84ec016c7debbfdfb0f238a74a749726444684092b8ad3405632a377bba9973` |
| `src/security/shell-sandbox.ts` | `d250136cd1f3fbb2074604bb712fa2b06feefdbf0b2868027892f554ec98ae4b` |
| `src/security/resource-limits.ts` | `1600d273e060a6af8543d458f8836d130d12e26e78992a01676df3f4c8b6ac88` |
| `src/utils/storage.ts` | `618a50012a75336c21d98771b1762f2c1e354412d666f6b7d105e475a11cfc51` |
| `src/utils/model-ledger.ts` | `13deb2ef0718689e5c8e94044b285346f3eb9885719efbb3401e80990337102a` |
| `src/utils/spec-binding.ts` | `26757301630d2f17288428eab91e4a2e343c990491be8b75ce2aea32167e2cfe` |
| `src/utils/mission-admission.ts` | `0ea2b8153332b7b785b827f7c862200a5fab8c74d829ffda2db030fdc68287d6` |
| `src/utils/qualification.ts` | `5cd73931ce7eb995fa4b6d88a2a8a22a7873166e3379983dc7a225f1a8b0ca77` |
| `src/utils/process-registry.ts` | `6d04390bac42cb45119f53d3bc3d0322666c63fa893c91e645def9fb4fdb0afe` |
| `src/api/server.ts` | `7cc19b7e14571bf1cd92044d0cd0ce035a34bfa005aa00363865076ab8143a1c` |
| `src/cli/index.ts` | `75d065b878741e4414b6a4bb1c3940d9f3f15f5959735dd0ffc825cf84934286` |
| `node_modules/@mastra/core/dist/processors/processors/tool-search.d.ts` | `1103ec29ede4018768dc515a2f43fb0527d8fb20a09a57762736c6cfde2ac4cc` |
| `node_modules/@mastra/core/dist/docs/references/reference-processors-tool-search-processor.md` | `69ec15a5c610220bff5005bcbe7e9e1fe035c5dc81b1b08bac79caedc345b563` |
| `node_modules/@mastra/core/dist/docs/references/reference-processors-skill-search-processor.md` | `c21b907a33e93e4b419869d19a94074b9d776778da2723049764219d98bb6d65` |

## 5. Retained test/run evidence — not fresh tests

| Evidence | Preserved result | What it proves / does not prove |
|---|---|---|
| `reports/r1-local-web-followup/full-offline/summary.json` | **39/39 separately executed suites PASS**, 2026-11-14T00:11:52.954Z–00:19:22.735Z, fresh isolated data per suite | Earlier offline regression result at current retained bytes. Does not certify open-world correctness or R2, and was not rerun here. |
| `reports/R1-P0-ACCEPTANCE.md` | Limited acceptance of five P0 boundary behaviors | Not whole R1 acceptance, production deployment or professional competence. |
| `reports/r1-release-inventory.md`; R0 preserved evidence references | R0 252 files, 55/55 historical manifest match, tree `85b9030f8bcc8b91a438b8b65fa9bf1f7647887ac631537446e8ffc4ea72ee6b` | Preservation history, not new sandbox qualification. System timestamps preserved rather than rewritten to session date. |
| `reports/r1-p1/evaluation.md` | Seven equal lesson/no-lesson tasks both succeeded; outputs equal; no tool-call/quality improvement shown | Scoped lesson reuse with no measured uplift; not generalized professional learning. Routing primitive≠task-sensitive model validation. |
| `reports/R1-LOCAL-WEB-PRACTICE.md` and two named run trees | First FAIL/paused preserved; replacement exact product finite PASS but mission unresolved | No historical failure converted into success; two runs remain separate. |
| `reports/r1-local-web-1794615675176-cad6b269/final-state-audit.json` | `PASS` product contract and `NOT_ACCEPTED_PAUSED_TIMEOUT`, 600111/600000 ms; four exact product bytes+tree | Product PASS bound to `a71660c6e6562f9542ed16013f4e24dedd3dcc179106ebc1bb9d72efe31ababe`; not mission ACCEPTED. |
| Same run `independent-verification.json` + artifact `.independent-qa/web-verification.json` | 13/13 finite checks for selected snapshot, contract `4857e261da19afefcf3bcfa80879b5a1d286963a42495d8fa97f90aa30d01bb8` | Bounded functionality/resource/keyboard/viewport checks, not visual design, universal accessibility or security certification. |
| Same run checkpoint/log/mission state | `paused`, `accepted=false`, repair=2, intent `eb2f2fcc-a5b9-47f2-ab2e-0e2f971a0dfc`; actual old-tree FAIL recorded before late verification | Old tree `198243a173248fd3ca8e21ff5a2cea15bc14034bdbe908f2fd3ef25b46b223c5` and final bytes not conflated. Deadline/quiescence pause is valid fail-closed evidence. |
| Same run `state/model-calls/*.json` | Six starts and finishes. Five completed subtotal 337014 tokens; sixth outcome UNKNOWN, reported 104613 | Complete usage/provider dollars UNKNOWN. Arithmetic sum 441627 including UNKNOWN is not a total or invoice. |

Artifact `run-evidence.sha256` preserves the original run-level hashes; its existence does not replace targeted source readback above. `final-state-audit.json` also lists four unrelated root artifacts; inspection of `src/tools/index.ts:407` identified basename registration as concrete wiring cause. This finding does not imply cross-mission filesystem escape.

### Retained evidence SHA-256

Paths below relative to Nox root:

| Path | SHA-256 |
|---|---|

| `reports/R1-P0-ACCEPTANCE.md` | `0d6164eaa9e1b5928973e0d913f7baca254009957e38dbc4e47336729a512564` |
| `reports/r1-release-inventory.md` | `e22b5832daef94b5898557d1c5f45a7711fada834a3952b1bad8e1cf0898f7b1` |
| `reports/r1-p1/evaluation.md` | `3bdba82d5982d76344e694a19f03f1d8f72adaf044945783166bf2f2ba40ad0a` |
| `reports/R1-LOCAL-WEB-PRACTICE.md` | `298d877416f7d1e8c4a6bbac6d74ea7ceb337eb17ab3c602b88ad72674ab0165` |
| `reports/r1-local-web-followup/full-offline/summary.json` | `ff38fa576927f9da2024b92c44b98c083644cd65c46a7866f00194ab83e8f6c7` |
| `reports/r1-local-web-1794615675176-cad6b269/run-evidence.sha256` | `636c52f6b8bc9db1aca66ac6314926edf0a0945326590df6c46e770b5acb215a` |
| `reports/r1-local-web-1794615675176-cad6b269/summary.json` | `cdef61b1131cd1564eb7895e69a53c62c663c8534a2aa218eaaac99f5350a0a2` |
| `reports/r1-local-web-1794615675176-cad6b269/final-state-audit.json` | `0f0d4a1c0e674792fef9913602180a338c9c950bbc74478d7dc635575fe77439` |
| `reports/r1-local-web-1794615675176-cad6b269/approval-scope.json` | `7576e9fe985b64e4e5e066c0508f6e356eaeb7e157ad81deef084bdf49b0dbf2` |
| `reports/r1-local-web-1794615675176-cad6b269/independent-verification.json` | `c7eb8c63e1e34548b29d9195545c4e329fcb40987b18060d50ae9c838728b013` |
| `reports/r1-local-web-1794615675176-cad6b269/r0-evidence-recheck.log` | `878cb6986edf2276a027aba25625680096db1e2b84fc389402a829efbaf9b6de` |
| `reports/r1-local-web-1794615675176-cad6b269/r0-preservation-recheck.json` | `62f7683977e0bc660bb689153c194350eeee81111d7c4b7296956c7062ff6dc0` |
| `reports/r1-local-web-1794615675176-cad6b269/state/checkpoints/r1-web-fc45eff2-3378-4ebd-8682-006ac71fac0a.json` | `8209b77340efaf8cb03869dd7fa078635c01aebdd949b68d9f108e64ab3ffa95` |
| `reports/r1-local-web-1794615675176-cad6b269/state/r1-web-fc45eff2-3378-4ebd-8682-006ac71fac0a.log` | `0facfc349ac83498ec51b9711365cb81f8056de592e3a3ff4495b4083dda70f8` |
| `reports/r1-local-web-1794615675176-cad6b269/state/missions/r1-web-fc45eff2-3378-4ebd-8682-006ac71fac0a.json` | `40e3fa80953b8be06b826270717098eb3939e15026ec025fe1ee42ca02200636` |
| `reports/r1-local-web-1794615675176-cad6b269/state/model-calls/2d478e68-33cd-4df1-b485-7d8dd5aaf726.finished.json` | `1fe54f2647636f4042c37b6919dfec346cd72e3dfcc11b049d86f6a71ad5da1b` |
| `reports/r1-local-web-1794615675176-cad6b269/state/artifacts/r1-web-fc45eff2-3378-4ebd-8682-006ac71fac0a/.independent-qa/web-verification.json` | `3f4f1340c2af93298af52540f8980fbb3871529cdfd4c56fe377413dd8cf2509` |

## 6. External documentation actually consulted

| Source | Method/date | Limited use in this review |
|---|---|---|
| `https://agentskills.io/specification` | Read-only web fetch, 2026-11-14 | Minimum skill directory/SKILL.md metadata, optional resources and experimental allowed-tools. Does not prove Nox integration, security, skills transfer or authority. |
| `https://modelcontextprotocol.io/registry/about` | Read-only web fetch, 2026-11-14 | Registry purpose/discovery metadata context. Review conclusion: metadata inclusion не executable vetting/sandbox/authorization. No blanket official security endorsement attributed. |
| Local installed Mastra paths in section 4 | Exact package bytes read from allowed Nox workspace | Native processor APIs at current installed version. No generic claim about future latest Mastra, no native integration test run. |
| Original draft observer URL and named docs paths | Historical reference, not substituted for source/runtime | Enables Cortex followup. The actual current corpus has not been completely re-inventoried by this review. |

No external docs snapshot is represented as cryptographically immutable here where no saved bytes/hash exists. Future Cortex registry/vendor claims need new primary URLs, version/observed date and exact evidence levels.

## 7. Explicit non-actions and UNKNOWNs

### NOT_RUN / NOT_PERFORMED in this review

* No Nox mission, resume, repair, live model call, fresh browser/MCP call, test suite, build, install or deployment.
* No paid provider/API action, infrastructure purchase, external publication or attempt to bypass GitHub authentication.
* No writes/commits to active Nox; no edits to original 01/02; only three new docs in separate permitted checkout.
* No implementation of candidate epochs, ToolSearch/SkillSearch/Workspace, retrieval memory, PG, professional pack, LLM routing change or lifecycle fix. These are proposed NEXT_TEST/implementation tickets only.
* No use of OpenCode subagent to manufacture independent organizational QA. This is source review, not R2 accepted mission.

### UNKNOWN or not established

1. Complete mission tokens, transport-level retries/actual provider usage and dollar invoice; costs cannot be derived from six incomplete invocation records.
2. Current general model suitability/professional quality, healthy external provider/tool/MCP integrations and exact cost/benefit of dynamic discovery.
3. Full original 4504 dataset cardinality/crosswalk/completeness because this review did not inventory raw data; these remain mandatory Cortex obligations.
4. Production authentication/identity/tenant security, new Windows/computer-use isolation, general professional qualification and remote-release status.
5. Current professional source licensing, corpus ACL behavior, held-out transfer and domain expert acceptance.
6. Current upstream package latest versions or compatibility beyond the pinned installed/local evidence cited above.
7. Whether the listed proposed repairs pass adversarial tests: all new module/live acceptance checks in 03/04 are NEXT_TEST/NOT_RUN.

## 8. Coverage readback for requested standalone research scope

| Obligation | Standalone 04 location | Required status |
|---|---|---|
| Fresh local runtime and evidence audit | §2–4 | Cortex must read latest source, no old export substitution. |
| Full 1331+3173=4504 rows and source identities | §5 and artifact 03 in §20 | Every source row reconciled; no test all 4504 required, no shortlist substitute. |
| Additional unrestricted research | §6, §19 | No numerical cap, but actual authority/resources apply. |
| Tool/capability lifecycle | §7–9 | Discovery and grant/call/receipt/QA/revoke separate. |
| Knowledge/source provenance/ACL | §10 | Sources and rights/ACL before retrieval, citations and contradiction/revocation. |
| Profession graph + skills/packs | §11 and artifact 07/12 | Open-world model with bounded qualification; no universal accreditation. |
| Strategy + meta improvement | §12–13 | Deterministic/code/API/bot/LLM/team/hybrid/blocked; learning without authority escalation. |
| Enterprise research + reuse economics | §14–16, §18 | Ready-made-first; A–H and L1–L4; actual dependency gaps/costs/rollback. |
| T01–T12 and negative controls | §17 | All mandatory for eventual R2; early slices not acceptance. |
| Research freedom vs owner-only actions | §19, §22 and artifact 18 | No extended production/secrets/purchase/external-action rights. |
| 18 output families + machine checksum/consistency | §20 | Names and identity preservation mandatory. |
| Direct Nox independent acceptance | §17, §22 | Review/research documents not final R2 acceptance. |

## 9. Reproducible read-only checks

From Nox root, after any future changes treat values as new snapshot rather than forcing equality:

```sh
git status --short --branch
git rev-parse HEAD
sha256sum package.json package-lock.json src/agents/mission-manager.ts src/agents/specialists.ts src/agents/qa-agent.ts src/agents/web-qa.ts src/config/mcp.ts src/config/models.ts
```

For run ledger arithmetic, parse only `*.finished.json`; do not count started/finished twice; sum only known-complete outcomes into a named subtotal. Keep UNKNOWN-call reported usage separate and never infer full dollars.

For docs readback from Nox workdir (space-containing paths quoted):

```sh
git -C /tmp/opencode/nivict-ai-academy-r2-review status --short --branch
sha256sum "/tmp/opencode/nivict-ai-academy-r2-review/03 - Практика/05 - AWE GROUP/RESEARCH/NOX-R2-CORTEX-OPENCODE-REVIEW-2026-11-14/"0{1,2,3,4,5}-*.md
```

GitHub URL exists only after verified push. Local file, staged file and local commit are not publication. Commit identity must be legitimate user-supplied identity; absent identity was not invented.


## 10. Final generated-file readback and publication boundary

| New file | Lines / bytes | SHA-256 at final content freeze |
|---|---:|---|
| `03-OPENCODE-ENGINEERING-REVIEW.md` | 207 / 27136 | `e3c421d40daf886462600b33f0bcc8fd990349a639f758d6a79b68ba55614ea4` |
| `04-CORTEX-R2-BRIEF-REVISED-BY-OPENCODE.md` | 391 / 69871 | `579edcaa62d8e20bc4bfd6feba3ac9bd018899c824a01941b7ef0d8fe1b5ed60` |

All five documents undergo full UTF-8 byte readback. 03 contains 207 source-backed review lines at initial freeze; 04 contains sequential sections 0–22, individual mandatory T01–T12 directions and all 18 Cortex deliverable families. Original 01/02 retained the exact section-2 hashes.

Run-level byte verification read `run-evidence.sha256` and rechecked **50/50 manifest records MATCH**, including both root/product artifacts, ledger files, browser receipt, logs and checkpoint. This is only retained-evidence integrity verification, not a new test run or changed mission verdict.

At this freeze Nox remains `68cc0ee20a25991ea275512e20ac521cc8f8234b`, clean, with no commits after it in this local branch. Documentation checkout remains at baseline `189851ff4195c5ad0003b60333f144c6d3ef8555`; only 03/04/05 are untracked. **No staging, commit, push or GitHub publication has occurred.** Repository Git author identity was unavailable and none was invented. Authenticated write access remains unconfirmed.

The external final SHA-256 of 05 must be reported after this append; no self-referential SHA is inserted in this file. The 04 GitHub link is deliberately absent because local creation is not publication.
