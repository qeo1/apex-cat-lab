# Deployment

- Live URL: https://26d31cec.apex-cat-lab.pages.dev
- Provider: Cloudflare Pages (`apex-cat-lab`)
- Release: `26d31cec-d1fd-4b1c-bcee-267ef30ebce4` (production; Cloudflare deploy stage `success`)
- Deployment method: direct Pages upload with a bundled `_worker.js` serving the app files.
- Smoke check: HTTPS returned HTTP 200 and the expected page title. Browser verification confirmed dashboard rendering, quiz open, hint display, correct answer explanation, and saved progress after reload.

This is an initial deployed release, not the full research platform from the specification. Authentication, Supabase persistence, cross-device sync and GitHub automation are not connected.

