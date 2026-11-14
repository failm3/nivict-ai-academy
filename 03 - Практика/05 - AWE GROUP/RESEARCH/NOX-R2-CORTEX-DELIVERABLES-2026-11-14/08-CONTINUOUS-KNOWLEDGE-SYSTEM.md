# 08 — Continuous knowledge system

**Статус:** source research L2 + design; actual ingestion/retrieval/transfer NOT_RUN. Полные upstream facts: `knowledge-report.md`; candidates: `04-EXPANDED-TOOLS-AND-SKILLS-REGISTRY.jsonl`.

## Records и pipeline

KnowledgeRecord ≠ SkillRecord ≠ ToolCard ≠ Template/Role ≠ CapabilityPack ≠ ActualExperience/EvaluationFixture. KnowledgeRecord обязателен: canonical URL/location, author/owner, edition/effective+observed UTC, immutable bytes/pointer+hash, rights/license, trust rationale, language, tenant ACL, page/section/figure/table/timecode/byte anchors, transformations, claims/citations, contradictions, freshness/reindex, retraction/revocation, completeness/error.

Event/schedule/mission trigger → rights/ACL before acquisition/index → format-specific extraction/OCR/transcription → authority/corroboration → immutable original + rebuildable ACL-preserving index → bounded pack → practice/held-out independent QA → scoped experience → refresh/revoke/delete/unshare/redact. Partial ingest не complete; read right не reproduce/fine-tune; secrets/illegal corpora excluded.

## Engine choice / REUSE FIRST

Сохранить LibSQL message history; PG/vector/embeddings только measured fit. Сначала один local instruction-only Skill через confirmed historical Mastra 1.82.0 Workspace/SkillSearch; `allowed-tools` не grant, scripts не выполняются. Docling 2.150.0 conditional для authorized document fixture; Crawl4AI deferred после security need; LightRAG не первый слой. Exact API/license/digests в `knowledge-report.md`.

## UNKNOWN, tests, rollback

Current corpus/ACL/extraction quality/cost/compatibility UNKNOWN. T04/T05/T09: false/stale/contradictory/retracted/unlicensed/injected/cross-tenant, malformed/encrypted/image-only, held-out fresh agent, citation completeness и no-benefit. Revoke record/pack и index/prompt/cache/artifact derivatives по policy; immutable evidence/failures сохранить; external deletion UNKNOWN до provider verification. `src/memory/index.ts` и `specialists.ts` — historical seams, fresh read first; OC-08/09.
