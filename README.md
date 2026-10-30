# APEX CAT LAB

A responsive CAT practice studio deployed on Cloudflare Pages. The current release includes three original sample questions, answer explanations, a PWA app shell, browser-local progress, and account-based progress sync through Supabase.

## Run locally

Serve this directory over HTTP (for example, `python -m http.server 8000`) and open `http://localhost:8000`. The service worker and browser authentication require a secure context; `localhost` is treated as secure by modern browsers.

## Backend

- Supabase project: `adlgchkwmwvoxeaohlhz` in `ap-south-1`.
- The client uses only the public publishable key. Never put a Supabase secret or service-role key in the browser.
- The pinned Supabase JavaScript client (`2.118.0`) is vendored under `vendor/` with its MIT license so the app does not depend on a third-party CDN at runtime.
- `supabase/migrations/20261030231050_create_practice_events.sql` defines practice events with owner-scoped RLS. The remote table was created and checked after the project was provisioned.
- Configure Supabase Authentication's Site URL and redirect allow-list to include `https://f78e4c7a.apex-cat-lab.pages.dev/` before email-confirmation links are used. The dashboard currently requires an interactive sign-in to change these settings.

## Research status

Question-level PYQ audit count is currently zero. The source ledger and preliminary archive census document access limits and archive disagreements. The three sample questions are original examples, not CAT PYQs.

See [BUILD_STATUS.md](BUILD_STATUS.md), [SOURCE_LEDGER.md](SOURCE_LEDGER.md), [PYQ_CENSUS.md](PYQ_CENSUS.md), and [DEPLOYMENT.md](DEPLOYMENT.md) for the current implementation and evidence boundaries.
