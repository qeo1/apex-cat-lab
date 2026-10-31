# Build status

Updated: 2026-10-31 (measured from repository records and validated acquisition artifacts)

## Historical CAT corpus — Phase 1 seed

| Measure | Count | Meaning |
|---|---:|---|
| Candidate years in current slot census | 9 (2017–2025) | Secondary-archive slot model; not an official year census |
| Candidate slots | 24 | 2017–2019: 2/year; 2020–2025: 3/year |
| Candidate section records | 72 | Three sections per candidate slot |
| Registered research sources | 17 | Archives, question-level reproductions, secondary reporting and legacy leads; source count is not independent corroboration |
| Acquired CAT section PDFs | 63 | 2017–2024 ZIP, all named year/slot/section files hashed; PDFs contain question pages; page-by-page completeness is still unchecked |
| Complete slot papers retrieved and completeness checked | 0 | No full slot paper has passed a question/image/page completeness audit |
| Partial question-level paper transcriptions examined | 6 slot/year records plus CAT 1991 annual page | CAT 2017 S1, CAT 2023 S1, CAT 2024 S1, CAT 2025 S1–S3, and CAT 1991 Q1 visible |
| Question-level records | 49 | 42 audited; 6 more CAT 2023/24 questions have only a secondary key; CAT 1991 Q1 is retrieved but unsolved |
| Structurally audited and independently answer-checked | 42 | CAT 2025: 27; CAT 2023 S1: 7; CAT 2024 S1: 7; CAT 2017 S1: 1 |
| Official-key corroborated questions | 0 | All examined materials are secondary reproductions; no official response sheet verified |
| Complete shared DILR sets reconstructed | 4 | CAT 2023 S1, CAT 2024 S1, and two CAT 2025 sets; two new sets have deterministic enumeration checks |
| Complete VARC passages retrieved | 0 | All four represented passage groups contain omissions/ellipses or otherwise lack a full passage transcript |
| Legacy year leads before 2017 | 21 records | TheCATExam lists 1991–2008 and 2016; PreviousYearPapers lists 1990–2017; 2009–2015 is an unresolved gap; one CAT 1991 question page opened |
| Duplicate question records removed | 0 | No exact duplicate question records found; structural similarity warnings: 0 in this seed |

## Existing application and content

| Asset | Implemented count | State |
|---|---:|---|
| Original practice questions in app | 3 | Starter examples; not PYQs |
| Research-derived experimental pilot questions | 25 / 25 | Retained as a separate labelled collection; not counted as historical research progress |
| Complete mock examinations | 0 / 100 | Not started |
| Concept Academy lessons | 0 complete | Dashboard placeholder only |
| User data sync | Implemented, not end-to-end verified | Existing Supabase/Auth work preserved |
| Automated deployments | 0 active | Workflow is prepared; production was not deployed in this milestone |

## Infrastructure preserved

- Existing Cloudflare Pages project: `apex-cat-lab`; production URL remains [26d31cec.apex-cat-lab.pages.dev](https://26d31cec.apex-cat-lab.pages.dev/).
- Existing GitHub repository: [qeo1/apex-cat-lab](https://github.com/qeo1/apex-cat-lab).
- Existing Supabase project and authentication/sync implementation are untouched.
- The 2IIM ZIP and rendered inspection images remain in ignored `work/`; the committed manifest stores filenames, page counts, sizes and SHA-256 hashes, not the 105 MB extracted PDF corpus.
- No production deployment was triggered.

## Research findings from examined questions

- A CAT 2017 QA age-ratio question reduces to one linear relation after normalizing present ages.
- CAT 2023 QA tests two sequential prime-exponent divisibility minima; CAT 2024 QA uses inclusion–exclusion for onto functions.
- The CAT 2023 DILR housing grid has two feasible occupancy patterns (64 parking-labelled states) after enumerating 1,572,864 occupancy/parking candidates without assuming Block XX has no parking; all five answers are invariant.
- The CAT 2024 DILR tournament has two labelled solutions related only by group-name symmetry; the schedule and all five answers are invariant.
- Cross-year VARC samples require scope discipline: region-category mismatch (2023) and identifying a shared consequence without transferring a one-sided feature (2024).

## Remaining Phase 1 work

1. Validate every page, item, answer control, diagram and locator in the 63 acquired section PDFs; count individual questions and reconstruct all set/passage relationships.
2. Cross-map those items to independent reproductions and preserve source-specific numbering.
3. Continue CAT 2025 audit beyond the 27 individually audited questions.
4. Retrieve and examine earlier-year public paper files. Legacy archive listings are discovery leads only; no inaccessible course material was accessed.
5. Independently solve more historical questions and check against official keys if any become reliably accessible.
6. Continue structural/difficulty analysis only from actual inspected questions. No psychometric calibration exists.

## Validation run in this milestone

- `python scripts/validate_historical_corpus.py` — source registry, 72 candidate section records, all 63 acquired PDFs mapped once to the 2017–2024 candidate sections, 49 question records, no data integrity errors, no exact structural fingerprint duplicates.
- `research/historical/audit-status.json` records current state counts and the validator checks them against item, set, conflict and paper records; counts come from actual evidence records, not archive index totals.
- `python scripts/verify_historical_answers.py` — deterministic checks for CAT 2017 QA Q1, CAT 2023 QA Q1, CAT 2024 QA Q1, the complete CAT 2023 housing set and CAT 2024 tournament set.
- `python -m unittest discover -s tests -v` — 5 integrity tests pass, including duplicate ID, orphan reference, incomplete PDF manifest, and false complete-paper claim rejection.
- These checks validate only the represented records and sampled solutions. They do not establish that any full historical examination paper has been completely audited.

