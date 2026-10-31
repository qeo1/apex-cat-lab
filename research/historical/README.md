# Historical CAT corpus

This database is separate from the original engineered-question pipeline and the 25-question experimental pilot. It records source evidence and exact acquisition state; an archive tile, a PDF index, a reproduced question, an audited answer, and an official key are distinct things.

## Files

- `paper-census.json`: one row per candidate slot-section from the current 2017–2025 slot model. These are explicitly candidate records, not claims of complete paper coverage.
- `audit-status.json`: derived live evidence counts and per-section coverage state. It distinguishes retrieved PDFs, question items audited, independent answers and official key corroboration.
- `source-registry.json`: source provenance, grade, independence group, coverage claims and known limitations.
- `question-corpus.json`: structurally described question-level records; copyrighted wording is not copied.
- `set-corpus.json`, `passage-corpus.json`: shared DILR and passage relationships.
- `source-conflicts.json`: unresolved coverage/locator/key/source defects.
- `acquisition-manifest.json`: local 2IIM archive acquisition metadata and per-PDF hashes. The PDFs are not committed; rendered samples contain actual question pages, but no full file has passed page-by-page completeness review.
- `legacy-candidates.json`: pre-2017 archive leads and retrieval/authenticity states. An actual CAT 1991 question-level webpage was opened; its archive-level count is not treated as an item audit.
- `legacy-papers.json`: separates the CAT 1991 annual archive page from the slot-based census; `slot: null` prevents inventing a modern slot label for a paper-era examination.
- `question.schema.json`: question record contract.
- The question contract includes optional conceptual, reasoning, solution, construction and analyst-difficulty dimensions. They are deliberately not backfilled where the question has not received that level of direct analysis.

Run `python scripts/validate_historical_corpus.py` from the repository root to check IDs, foreign keys, plausible paper counts, duplicate fingerprints, shared set/passage links and truthful audit counts.

## Evidence counts at seed

The CAT 2025 audit contributes 27 question-level audited records. This seed adds one audited CAT 2017 QA item, 14 audited items from actual CAT 2023/2024 Slot 1 transcriptions (including two complete shared DILR sets, ten questions), one retrieved but unsolved CAT 1991 VARC-labelled item, and six CAT 2023/2024 VARC items with visible secondary keys but no independent solution. This yields 49 actual question records, of which 42 are structurally audited and independently answer-checked. No official response-sheet keys were found. The 2023/2024 paper pages are partial reproductions because the VARC passage transcriptions contain ellipses. The question database does not claim complete papers or complete year/slot coverage.

