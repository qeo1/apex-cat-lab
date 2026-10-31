# Build status

Updated: 2026-10-31 (counts are repository inventory, not targets)

## Current verified inventory

| Asset | Implemented count | State |
|---|---:|---|
| Original practice questions in app | 3 | Starter examples only; none are PYQs |
| CAT PYQ source records in ledger | 15 | Index and primary/secondary cross-check sources; audit underway |
| CAT 2025 questions independently audited | 27 | 10 QA, 9 DILR (two complete shared sets), 8 VARC (two passage sets); grade C sources, official key unchecked |
| Research-derived pilot questions | 25 / 25 approved | QA/DILR deterministic checks and VARC textual evidence audit passed; integrated in labelled app section; static preview interaction verified |
| Complete mock examinations | 0 / 100 | Not started |
| Concept Academy lessons | 0 complete | Dashboard placeholder only |
| User data sync | Implemented, not end-to-end verified | Supabase project/table exist; Auth redirect config/account test pending |
| Automated deployments | 0 active | GitHub Actions workflow and static build is ready; repository deployment secrets are not configured, so production still serves its prior release |

## Existing product and infrastructure

- Existing Cloudflare Pages project: `apex-cat-lab`; continue using it. Previously successful deployment: `f78e4c7a-9532-4aef-901d-2ca00a71dfb2`, `https://f78e4c7a.apex-cat-lab.pages.dev`.
- Existing private GitHub repository: [qeo1/apex-cat-lab](https://github.com/qeo1/apex-cat-lab). Local `main` history is not connected to a Git remote; repository contents were uploaded through GitHub's API.
- Existing Supabase project: `adlgchkwmwvoxeaohlhz`; `practice_events` has owner-scoped RLS. Client-side auth and sync are implemented, but email redirect allow-list and account-to-account sync are not yet verified.
- App contains three original demonstration questions, local progress, a PWA shell, and sign-in/sign-up controls.

## Research capability and current work

- Live web research is available in this environment and is being used for source discovery and question-level CAT research. Source capture must include URL, date, evidence grade, audited question identifier and explicit uncertainties.
- CAT 2025 research currently contains 27 question-level records: ten QA questions, two complete DILR sets (nine questions), and two four-question VARC passage groups. All are Grade C secondary transcriptions; no official response-sheet key was verified. The 25-item original Research Pilot is internally approved after 20 blind deterministic QA/DILR re-solves and a five-item VARC textual evidence audit; it is not a psychometrically calibrated bank. Findings include a wrong minimum in one Slot 1 QA explanation, an inequality-direction error in a Slot 2 DILR explanation, and locator conflicts. This is not a complete audit of the 204 archive-indexed questions.
- No 25-question pilot is admitted until each original item has a research rationale, CAT benchmark fingerprint, independent solution check, and adversarial uniqueness check.

## Next milestones

1. Continue the 204-item CAT 2025 paper audit; prioritize image-dependent DILR and remaining QA, VARC.
2. Continue widening the examined CAT 2025 question census beyond 27/204; the 25-item pilot is approved and integrated, with calibration and external editorial review still future work.
3. Only after pilot validation, scope the 1,600-question expansion.
4. Complete 100 mocks and the Concept Academy as later milestones.
5. Verify account auth/sync and activate the prepared GitHub Actions-to-Cloudflare deployment after secure repository secrets are provisioned.

## Evidence limits

- Secondary archives disagree on coverage and sometimes contain unofficial answer keys. A public archive transcription is not equivalent to an official response sheet.
- IIM Ahmedabad links to the official CAT 2026 information bulletin, but the PDF is blocked to automated retrieval (HTTP 403). The working date must remain configurable until its content is directly reviewed.
- The original sample items in the app are not research-derived and are excluded from the future pilot count.




