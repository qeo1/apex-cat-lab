# Build status

Updated: 2026-10-31 (counts are repository inventory, not targets)

## Current verified inventory

| Asset | Implemented count | State |
|---|---:|---|
| Original practice questions in app | 3 | Starter examples only; none are PYQs |
| CAT PYQ source records | 10 | Index, primary and secondary cross-check sources |
| CAT PYQs with question-level audited fingerprints | 1 | CAT 2025 Slot 1 QA: grade C, answer independently verified; official-key match pending |
| Global research sources | 10 | First scope across discrete math, probability, OR, philosophy, economics, statistics and analytical writing |
| Research-derived pilot questions | 0 / 25 | Pilot not started |
| Complete mock examinations | 0 / 100 | Not started |
| Concept Academy lessons | 0 complete | Dashboard placeholder only |
| User data sync | Implemented, not end-to-end verified | Supabase project/table exist; Auth redirect config/account test pending |
| Automated deployments | 0 | Current Pages uploads are manual |

## Existing product and infrastructure

- Existing Cloudflare Pages project: `apex-cat-lab`; latest recorded successful deployment: `f78e4c7a-9532-4aef-901d-2ca00a71dfb2`, `https://f78e4c7a.apex-cat-lab.pages.dev`.
- Existing private GitHub repository: [qeo1/apex-cat-lab](https://github.com/qeo1/apex-cat-lab). Local `main` history is not connected to a Git remote; contents are kept in sync through GitHub's API.
- Existing Supabase project: `adlgchkwmwvoxeaohlhz`; `practice_events` has owner-scoped RLS. Auth/sync implementation exists; email redirect allow-list and real-account cross-device sync remain unverified.

## Research work recorded

- Live web research is available and used for source discovery and question-level audit.
- The first question-level record is [CAT 2025 Slot 1 QA 9](research/pyq/cat-2025-slot-1-audit.md). It identifies a faulty minimum-number explanation in one public reproduction while confirming the final divisor-count answer independently. Authenticity grade is C because official response-sheet provenance has not been matched.
- Sources and access limits are in [SOURCE_LEDGER.md](SOURCE_LEDGER.md); global field map is in [research/global/field-map.md](research/global/field-map.md).
- Research-to-question evidence gates and machine-readable schema/validator are in [research/pipeline](research/pipeline/).
- No pilot item has passed validation. The three app examples are excluded from the pilot count.

## Next milestones

1. Continue question-level audit of the latest accessible CAT 2025 slot papers; preserve source conflicts and avoid republishing paper text.
2. Expand machine-readable fingerprints and source records.
3. Conduct broader global source review and map specific insights to original structures.
4. Publish and independently validate 25 research-derived originals before any scale-up.
5. Implement question bank, Concept Academy and mocks as validated content permits.
6. Verify auth/sync and connect GitHub-to-Cloudflare deployment if the existing account supports it.

## Evidence limits

- Public archives are secondary reproductions; official response-sheet/answer-key artifacts remain inaccessible to this automated research session.
- IIM Ahmedabad links the official CAT 2026 information bulletin, but the PDF is blocked from automated retrieval (HTTP 403); exam details remain configurable pending direct review.
