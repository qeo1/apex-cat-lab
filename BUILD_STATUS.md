# Build status

Updated: 2026-10-31

## Delivered

- [x] Built and deployed the APEX CAT LAB practice studio to Cloudflare Pages: [live site](https://f78e4c7a.apex-cat-lab.pages.dev).
- [x] Added original VARC, DILR and Quant practice items with hints, explanations, local progress tracking, responsive layout and a PWA app shell.
- [x] Created private GitHub repository [qeo1/apex-cat-lab](https://github.com/qeo1/apex-cat-lab) and uploaded the source.
- [x] Created Supabase project `adlgchkwmwvoxeaohlhz` in `ap-south-1`; created `practice_events` with owner-scoped row-level security.
- [x] Implemented email sign-up/sign-in and event synchronization using the public Supabase publishable key. Vendored the pinned Supabase client with its license.
- [x] Added a migration and verified the remote table, RLS policies, and Supabase security advisor (no security lint findings).
- [x] Started a provenance-first CAT PYQ source ledger, archive census and preliminary analytics/pattern notes.

## Still needed

- [ ] Add the current Pages URL to Supabase Auth's Site URL and redirect allow-list. This dashboard setting needs an interactive Supabase sign-in. Until configured, email confirmation links may not return to the live site.
- [ ] No end-to-end account confirmation or cross-device sync has been verified with a real user account.
- [ ] The research audit currently contains zero question-level verified PYQs. Current questions are original examples, not previous-year questions. The requested broad archive review and full question bank remain future work.
- [ ] Pages deploys are direct uploads; GitHub is not connected to automatic Cloudflare deployment.

## Evidence and limits

- Current Pages release: `f78e4c7a-9532-4aef-901d-2ca00a71dfb2`, stage `success`; direct upload serves the app and vendored client over HTTPS.
- Supabase project is active and the `practice_events` table has RLS enabled with owner-scoped policies.
- The official CAT site returned HTTP 403 to automated retrieval. CAT 2026 date in the current app is not verified against the official bulletin.
