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

The corpus-first historical inventory is in [`research/historical/`](research/historical/). It currently contains 72 candidate section records for 2017–2025, hashes for 63 acquired section PDFs from 2017–2024, and 49 question-level records including one unsolved CAT 1991 item. Of those questions, 42 have structural audits and independent answer checks; six have only a secondary answer visible. None is officially key-corroborated, and no full slot paper has passed a completeness audit. The three app questions remain original demonstration examples, not CAT PYQs.

See [BUILD_STATUS.md](BUILD_STATUS.md), [SOURCE_LEDGER.md](SOURCE_LEDGER.md), [PYQ_CENSUS.md](PYQ_CENSUS.md), and [DEPLOYMENT.md](DEPLOYMENT.md) for the current implementation and evidence boundaries.

## Research engineering

- [Initial question-level CAT 2025 audit](research/pyq/cat-2025-initial-audit.md) and machine-readable fingerprint.
- [Global research field map](research/global/field-map.md).
- [Research-to-question validation pipeline](research/pipeline/README.md).

The separate experimental pilot has 25 original questions. It is not evidence of historical corpus coverage or success of the question-generation system.



## Research pilot and audit

The labelled original 25-question pilot is in the app under Research Pilot and remains separate. CAT 2025 still has only 27/204 questions individually audited. The new historical corpus adds 15 independently checked questions from CAT 2017, 2023 and 2024 Slot 1, six CAT 2023/2024 VARC questions with source keys not yet independently checked, and one unsolved CAT 1991 item. See [PYQ_CENSUS.md](PYQ_CENSUS.md), [PYQ_ANALYTICS.md](PYQ_ANALYTICS.md), and [research/historical/README.md](research/historical/README.md). The corpus has not yet been integrated into the app.

