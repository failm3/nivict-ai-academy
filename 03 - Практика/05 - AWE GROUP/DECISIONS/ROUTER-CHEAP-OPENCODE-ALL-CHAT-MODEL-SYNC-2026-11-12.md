# AWE GROUP — OpenCode catalog sync permission (2026-11-12)

The owner approved automatically registering all identifiable OpenCode-compatible **chat/reasoning** models returned by the existing Router.Cheap key's `GET https://router.cheap/v1/models`, without changing the OpenCode default model or existing model overrides. The full list of 75 catalog entries contains non-text models; these require separate integrations and are not automatically text-chat compatible. Being listed is not evidence of a successful paid live invocation.

Prepared local archive `AWE-RouterCheap-Model-Sync.zip` with SHA-256 `6704a08e9b13eaca3e7f5fe530835f9cb5de8344c84484d153eecd0a61873faa`: `sync_models.py` (preview, `--apply`, optional `--verify-all`), `install_weekly_sync.sh` (optional user-level weekly systemd timer), and README. The package was syntactically checked, ZIP integrity checked and dry-run/write behavior tested against synthetic data. **Not yet installed or executed in owner's WSL; no real Router.Cheap calls or costs incurred from the assistant's development environment.**

Original owner permission to use prepaid Router.Cheap funds for genuine LIVE tests remains. No new purchase, top-up, model default switch or disruption of existing OpenCode sessions authorized/necessary for the catalog registration.
