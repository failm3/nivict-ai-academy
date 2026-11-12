# Review of flagged source records

Status: **PARTIAL**. All 12 keyword-flagged records received a separate source review: 10 README sources observed, two repositories unavailable via public GitHub APIs. No source was declared malware from keywords. No code, installer, exploit, prompt payload or endpoint-protection change was executed.

The three system-prompt collections contain descriptive archived records, not active instructions to the auditor. They remain untrusted reference material, with provenance and reuse rights unresolved. CrowdSec is a confirmed defensive-tool keyword false positive. The `ai-model-bypass` README actually includes adversarial prompt payloads; they were treated as data.

| Source ID | Repository | Classification | Decision |
|---|---|---|---|
| Радар-0259 | [Sophomoresty/turnstile-bypass](https://github.com/Sophomoresty/turnstile-bypass/blob/main/README.md) | RISK_REVIEW | DEFER_NOT_REQUIRED_FOR_AWE_BASELINE |
| Радар-0977 | [LiveContainer/LiveContainer](https://github.com/LiveContainer/LiveContainer/blob/main/README.md) | RISK_REVIEW | DEFER_OUTSIDE_AWE_SCOPE |
| Радар-1101 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool/blob/master/README.md) | RISK_REVIEW | DEFER_EXECUTION_NOT_AUTHORIZED |
| Радар-1212 | [crowdsecurity/crowdsec](https://github.com/crowdsecurity/crowdsec/blob/master/README.md) | FALSE_POSITIVE | PILOT_ONLY_IF_HOST_DEFENSE_GAP_EXISTS |
| Радар-1219 | [CyberAlbSecOP/Awesome_GPT_Super_Prompting](https://github.com/CyberAlbSecOP/Awesome_GPT_Super_Prompting) | UNKNOWN | DEFER_SOURCE_UNAVAILABLE |
| Радар-1386 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts/blob/main/README.md) | FALSE_POSITIVE | REFERENCE_ONLY_PROVENANCE_AND_RIGHTS_UNKNOWN |
| Радар-1499 | [matro7sh/BypassAV](https://github.com/matro7sh/BypassAV/blob/main/README.md) | RISK_REVIEW | DEFER_OUTSIDE_AWE_BASELINE |
| Радар-2226 | [SteamAutoCracks/ManifestHub](https://github.com/SteamAutoCracks/ManifestHub/blob/main/README.md) | UNKNOWN | DEFER_UNRELATED_AND_AUTHORIZATION_UNKNOWN |
| Радар-2541 | [l0gicx/ai-model-bypass](https://github.com/l0gicx/ai-model-bypass/blob/main/README.md) | RISK_REVIEW | ADVERSARIAL_QA_REFERENCE_ONLY_AFTER_SCOPE_REVIEW |
| Радар-3062 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/blob/main/README.md) | FALSE_POSITIVE | REFERENCE_ONLY_PROVENANCE_AND_RIGHTS_UNKNOWN |
| Радар-3116 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks/blob/main/README.md) | FALSE_POSITIVE | REFERENCE_ONLY_PROVENANCE_AND_RIGHTS_UNKNOWN |
| Радар-3127 | [Gezine/BD-JB-1250](https://github.com/Gezine/BD-JB-1250) | UNKNOWN | DEFER_SOURCE_UNAVAILABLE_OUTSIDE_AWE_SCOPE |

Per-ID observations, caution, immutable README blob references and unknowns are in `FLAGGED-SOURCE-REVIEW.json`. A source-review classification does not establish malware absence, operational safety, license compliance, or AWE acceptance. Both 404 records remain preserved as UNKNOWN rather than being silently discarded.

No current AWE infrastructure, OpenCode session, browser profile, account token, antivirus rule or target system was changed. The required other-model-family gate remains NOT_SATISFIED.

Publication pattern-scan results are recorded separately in `PUBLICATION-SCAN.json`; rerun `publication_scan.py` after the final public artifact set is assembled. Matching values are never included in that report.
