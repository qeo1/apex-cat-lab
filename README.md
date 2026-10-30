# APEX CAT LAB

A responsive CAT practice studio deployed on Cloudflare Pages. The current release includes three original sample questions, answer explanations, a PWA app shell, browser-local progress, and account-based progress sync through Supabase.

## Run locally

Serve this directory over HTTP (for example, `python -m http.server 8000`) and open `http://localhost:8000`. The service worker and browser authentication require a secure context; `localhost` is treated as secure by modern browsers.

## Backend

- Supabase project: `adlgchkwmwvoxeaohlhz` in `ap-south-1`.
- The client uses only the public publishable key. Never put a Supabase secret or service-role key in the browser.
- The pinned Supabase JavaScript client (`2.118.0`) is vendored under `vendor/` with its MIT license so the app does not depend on a third-party CDN at runtime.
- `supabase/migrations/20261030231050_create_practice_events.sql` defines append-only practice events with owner-scoped RLS. The remote table was created and checked after the project was provisioned.
- Configure Supabase Authentication's Site URL and redirect allow-list to include `https://f78e4c7a.apex-cat-lab.pages.dev/` before email-confirmation links are used. The dashboard currently requires an interactive sign-in to change these settings.

## Research status

The source ledger contains 15 CAT and official-source records. Three sampled CAT 2025 QA items have question-level structural fingerprints and independently derived answers across Slots 1–3; all are secondary-source grade C, not official-key verified. The three app questions remain original demonstration examples, not CAT PYQs.

See [BUILD_STATUS.md](BUILD_STATUS.md), [SOURCE_LEDGER.md](SOURCE_LEDGER.md), [PYQ_CENSUS.md](PYQ_CENSUS.md), and [DEPLOYMENT.md](DEPLOYMENT.md) for the current implementation and evidence boundaries.

## Research engineering

- [Initial question-level CAT 2025 audit](research/pyq/cat-2025-initial-audit.md) and machine-readable fingerprint.
- [Global research field map](research/global/field-map.md).
- [Research-to-question validation pipeline](research/pipeline/README.md).

The pilot count remains zero until each original question includes its research sources, CAT benchmark comparison, independent answer verification and adversarial checks.



