# Build status

Updated: 2026-10-31 (counts are repository inventory, not targets)

## Current verified inventory

| Asset | Implemented count | State |
|---|---:|---|
| Original practice questions in app | 3 | Starter examples only; none are PYQs |
| CAT PYQ source records in ledger | 10 | Index and primary/secondary cross-check sources; audit underway |
| CAT PYQs with question-level audited fingerprints | 1 | CAT 2025 Slot 1 QA: grade C, answer independently verified; official-key match pending |
| Research-derived pilot questions | 0 / 25 | Pilot not started |
| Complete mock examinations | 0 / 100 | Not started |
| Concept Academy lessons | 0 complete | Dashboard placeholder only |
| User data sync | Implemented, not end-to-end verified | Supabase project/table exist; Auth redirect config/account test pending |
| Automated deployments | 0 | Current Pages uploads are manual |

## Existing product and infrastructure

- Existing Cloudflare Pages project: `apex-cat-lab`; continue using it. Previously successful deployment: `f78e4c7a-9532-4aef-901d-2ca00a71dfb2`, `https://f78e4c7a.apex-cat-lab.pages.dev`.
- Existing private GitHub repository: [qeo1/apex-cat-lab](https://github.com/qeo1/apex-cat-lab). Local `main` history is not connected to a Git remote; repository contents were uploaded through GitHub's API.
- Existing Supabase project: `adlgchkwmwvoxeaohlhz`; `practice_events` has owner-scoped RLS. Client-side auth and sync are implemented, but email redirect allow-list and account-to-account sync are not yet verified.
- App contains three original demonstration questions, local progress, a PWA shell, and sign-in/sign-up controls.

## Research capability and current work

- Live web research is available in this environment and is being used for source discovery and question-level CAT research. Source capture must include URL, date, evidence grade, audited question identifier and explicit uncertainties.
- Latest available paper family located: CAT 2025, three slots. The first question-level record is [CAT 2025 Slot 1 QA 9](research/pyq/cat-2025-slot-1-audit.md). It records a faulty explanation in one reproduction while confirming the final answer; official-key match remains unverified.
- No 25-question pilot is admitted until each original item has a research rationale, CAT benchmark fingerprint, independent solution check, and adversarial uniqueness check.

## Next milestones

1. Audit CAT 2025 slot papers at question level, starting from the most recent accessible sources; preserve source conflicts and do not reproduce protected paper text.
2. Build machine-readable question fingerprint and source ledger records.
3. Research global intellectual sources and map them to original problem structures.
4. Publish and independently validate exactly 25 pilot originals before any scale-up.
5. Implement usable question bank, academy and mock experiences only as content and validation permit.
6. Verify account auth/sync, restore stable live URL, and connect GitHub-to-Cloudflare deployment if supported by the existing account.

## Evidence limits

- Secondary archives disagree on coverage and sometimes contain unofficial answer keys. A public archive transcription is not equivalent to an official response sheet.
- IIM Ahmedabad links to the official CAT 2026 information bulletin, but the PDF is blocked to automated retrieval (HTTP 403). The working date must remain configurable until its content is directly reviewed.
- The original sample items in the app are not research-derived and are excluded from the future pilot count.


