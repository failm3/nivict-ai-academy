# AWE GROUP — OpenCode Recorder GitHub publication, conditional 5-second sync

Owner confirmed 2026-11-12:
- awe-session-recorder.service active
- 5 matched OpenCode sessions (one root, four children)
- 370 local records collected
- last_poll=2026-11-12T04:36:19.274+00:00, last_error=None

The full local Recorder v1 is running, but GitHub synchronization is still local-only.

Prepared guarded patch file AWE-Recorder-GitHub-5s-Upgrade.py (sha256 dfb10b391b6a5489122bddf4e893bba69cd103b55608955b464603e4b4a4e55f). Requires previous location.directory and API limit 200 fixes. Sets sync_seconds=5 and replaces GitHub sync with a change-aware check: remote API calls only when the redacted mirror changed; skip empty pushes, preserve original OpenCode runtime, default model and existing polling. Makes 0600 backups. Source checked in synthetic HOME; original six unit tests passed and fake GitHub tests confirmed no API calls when unchanged and no redundant LATEST writes.

NOT DEPLOYED on owner's host. No remote GitHub session journal exists yet. A separate PRIVATE repository failm3/awe-opencode-recordings must be created by owner; existing failm3/awe-group-observer remains for sanitized technical telemetry. Owner must create an access-restricted GitHub fine-grained PAT with Contents: read/write on new private repo and configure it with Recorder's built-in configure-github command.

Five seconds is the change-detection cadence, not a guaranteed GitHub delivery latency, because GitHub/network rate limits and initial history upload may delay it. Redaction is best-effort, never fully guaranteed; raw local data remains local.
