# Independent QA: corpus and overlap

Status: **PARTIAL**. A separate agent independently read the original files and recomputed the results. It uses the same GPT model family as the lead auditor. The required different-family review is **NOT_SATISFIED**. No upstream code was executed, installed, or imported; the two QA scripts use the Python standard library only.

## Reproducible evidence

Run from the audit workspace root:

```powershell
& 'C:\Users\1\AppData\Local\Programs\Python\Python313\python.exe' -X utf8 outputs/QA/independent_qa.py
& 'C:\Users\1\AppData\Local\Programs\Python\Python313\python.exe' -X utf8 outputs/QA/independent_manus_qa.py
```

`INDEPENDENT-COUNTS.json` contains the independently recomputed checks. All 4,504 original rows are present: 1,331 iirepresent and 3,173 Радар. JSON, CSV, and 4,504 Obsidian notes preserve the same ID multiset. Notes also preserve URL, category, confidence, resource type, and original descriptions after decoding 16 HTML-escaped note descriptions. No content mismatch remains.

One literal historical hash comparison differs: `validation-report.json` records CRLF hashes, whereas the pinned Git commit stores LF. Reconstructing CRLF reproduces both old hashes exactly. All eight mandatory files match the pinned Git blobs. The classification is **EXPLAINED_HISTORICAL_BYTE_MISMATCH**, not an upstream content failure. This does not justify claiming the old archive bytes and committed bytes are identical.

Independent URL counts are 4,472 exact strings, 4,471 conservative resource URLs, 4,466 legacy normalized full URLs, 4,424 legacy host/path keys, and 4,465 GitHub-project-or-resource keys. The last number is **not** a verified unique technology count. All 38 exact duplicate groups and 33 query-collision groups in the old duplicate report match by source ID. All 4,090 issues rows match the original classification flags.

`NEGATIVE-CASES.json` records checks for path case, query identity, encoded slash, GitHub project versus file, fragments, and unproven www aliases. `URL-COLLISION-EXAMPLES.json` preserves the real collision groups. These fixtures test identity methodology, not tool operability or security.

## Manus reconciliation

The independently opened local ZIP has SHA-256 `5855ce5cfdb0abda44954108bfe2cfa1bec97dbf7c51db7be822eb04541d5ec1`, 485 members, and 3,415 research rows with unique IDs/identity keys. All archive CRCs and the two backup-member hashes pass. The bundle has the manifest's expected hash under a different filename. The separately named source ZIP and delivery tarball are absent from the outer ZIP; they were not independently hashed.

Using primary URLs plus explicitly marked imported URL-claim aliases reproduces the lead auditor's row matches: 3,309 NIVICT rows map to 3,270 Manus rows. There are 1,195 NIVICT rows without a match and 145 Manus rows without a match under these rules. Match tiers and primary-URL-only sensitivity metrics are preserved in `MANUS-INDEPENDENT-COUNTS.json`; multiple aliases per row must not be reported as additional resources.

The archive records stages DISCOVERED=3,403, DOCUMENTED=8, LIVE_TESTED=4, and zero approvals/export approvals. Its verification labels are research_only=3,405, official_metadata_observed=6, live_tested=4. These are imported historical assertions. They have not been rerun or adopted by this audit.

The three-row `research/live_stack_resources.jsonl` contains Beautiful Soup, FastAPI and Psycopg. It is not a snapshot of the current 12-row working AWE database. No live AWE database was inspected. Capitalized/lowercase GitHubRadar post files are byte-identical, so they are not independent sources.

## Stratified source checks and disagreements

`STRATIFIED-SAMPLE.json` selects one deterministic record from each of all 59 nonempty original category/confidence strata, covering all 22 categories and all four confidence levels. Source consistency was checked for every row. This does **not** validate all sample descriptions or capabilities against external sources.

Four sample README sources were separately read. Evidence URLs and blob SHAs are in `PRIMARY-SOURCE-SPOTCHECKS.json`. Confirmed category mistakes include MapSCII as RAG/memory, Screenshot Studio as high-confidence audio/speech, and OWASP Cheat Sheet Series as data/database tooling. PaperGuru-Benchmark's memory description is supported by its README and was not rejected based on its name. Its claimed benchmark superiority remains unverified.

During QA, naive `split('---')` frontmatter parsing falsely reported a mismatch for Радар-1809 because its URL contains `---`. Parsing delimiter lines resolves it. HTML escaping and whitespace in semicolon-separated flags likewise required interpretation before claiming source defects. The producer corrected these issues; they remain useful negative cases.

The first producer's coding regex matched every GitHub URL. This was a capability false-positive risk and was reported for correction. IPv6 authority reconstruction, control characters, invalid URL grouping, and duplicate note-stem multiplicity were also flagged as parser/methodology edges; no claim is made that those URLs occur in this corpus.

## Outstanding gates

- A reviewer from another model family must audit the methodology and unresolved disagreements.
- Nineteen selected high-risk candidates subsequently received separate README/license source review; see `HIGH-RISK-REVIEW.md`. This does not establish code safety, runtime acceptance, or different-family review.
- Remaining stratified samples need external claim checks. URL availability, README review, license evidence and sandbox tests must remain separate statuses.
- Current AWE runtime, prices, compatibility and safety were not tested by these scripts.
