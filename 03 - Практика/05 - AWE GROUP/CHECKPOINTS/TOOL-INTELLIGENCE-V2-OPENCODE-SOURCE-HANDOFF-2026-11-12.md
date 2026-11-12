# AWE Tool Intelligence v2 -> OpenCode: read-only source handoff

Owner asked to first expose Manus v2 **code** to OpenCode and verify that OpenCode can see/read it, **before** integration/installation.

Uploaded ChatGPT archive `AWE-Tool-Intelligence-v2-all(1).zip` has embedded canonical Git bundle `awe-tool-intelligence/awe-tool-intelligence.bundle`. Verified with git clone against commit `58d3132c139b3e45ff7cd24289a2d618d87d373a`; bundle SHA256 `334c0b2735d18aeccb6ab76b4b23c368fbe1845480b473d9a486e8ee6e3d2f7e` matches Manus v2 manifest. Repo contains 96 tracked source files including Python implementation, migrations, tests, documentation, and requirements.lock.

Created downloadable code-only handoff artifact `AWE-TI-OpenCode-Handoff-v2.zip` (ZIP SHA256 `48ce6024b5dc6c68bbf8869086f21f3d955798339a8ba1ec9bff2780f48a77e3`), including the original upstream Git bundle and a PowerShell script that **on owner's local WSL after the owner runs it** performs SHA validation and clones to `$HOME/awe-tool-intelligence-v2-review`. Does not touch AWE cleanroom, Postgres, processes, services, or secrets. Git/bundle read-only cloning was tested twice independently in the working sandbox; no claim of live WSL access. Reuse existing directory only if HEAD matches target commit. No actual user-host run has occurred yet.

OpenCode review goal after user executes the handoff:
- Confirm `git -C ~/awe-tool-intelligence-v2-review rev-parse HEAD` exact commit.
- Read `awe_ti/api.py`, `awe_ti/registry.py`, `awe_ti/mcp_discovery.py`, `requirements.lock`, `OPERATIONS.md`.
- Map API registry/search/approval contract to AWE TR-01 and report compatibility/blockers.
- Make no modifications/installs and do not claim 3415 candidates are installed/approved tools.
- Source-only visibility is not PostgreSQL deployment or catalog restoration. Manus v2 currently has `approved_executable_records=0`; separate approved integration task required.

The ChatGPT sandbox file link is not an automatically accessible path in user's WSL; owner needs one local download and PowerShell execution before claiming OpenCode sees source.
