# Historical CAT census and acquisition ledger

Snapshot: 2026-10-31. The corpus is in [`research/historical/`](research/historical/). Archive claims, downloaded documents, examined questions, verified answers and official evidence are counted separately.

## Current coverage

| Scope | Candidate slots | Candidate section records | Section PDFs acquired | Question-level source coverage |
|---|---:|---:|---:|---|
| CAT 2017–2019 | 6 | 18 | 18 | One item opened and independently solved: CAT 2017 S1 QA Q1 |
| CAT 2020–2024 | 15 | 45 | 45 | Full question text PDF collection acquired; only CAT 2023 S1 and CAT 2024 S1 transcriptions have individual-item work so far |
| CAT 2025 | 3 | 9 | 0 in the 2017–24 ZIP | 27 questions individually audited across all slots; source pages display all sections but only a sample was structurally audited |
| **2017–2025 candidate total** | **24** | **72** | **63** | **48 question records in this scope: 42 audited/answer-checked, 6 retrieved with secondary key only** |

The slot model is based on secondary archive indexes (two slots each in 2017–2019; three each in 2020–2025). It is a working candidate census, not official confirmation that the year/slot universe is complete.

## Acquired files versus complete papers

The downloaded [2IIM CAT 2017–2024 PDF archive](https://online.2iim.com/CAT-question-paper-pdf/) contains 63 files corresponding to 21 candidate slots × 3 sections. The ZIP was 78,565,250 bytes; extracted PDFs total 105,247,856 bytes. Every PDF has a recorded filename, section/year/slot mapping, page count, byte size and SHA-256 hash in [`acquisition-manifest.json`](research/historical/acquisition-manifest.json). The PDFs include actual question pages after navigation pages; rendered samples confirm this for CAT 2017 QA, CAT 2024 DILR and CAT 2024 VARC.

This acquisition is **not** a claim that 21 slot papers are complete or audited. Every PDF remains marked not page-by-page checked. Image-dependent prompts, duplicated/mislabelled material, answer hyperlinks, all question counts and set/passage relationships still need systematic review. Therefore the count of complete slot papers retrieved *and completeness-checked* is 0. The 63 files count as acquired section documents.

## Questions actually opened

- **CAT 2017 Slot 1 QA:** Q1 age-ratio item opened in the scanned 2IIM PDF and independently solved as 20%. The provider's clickable answer was not opened.
- **CAT 2023 Slot 1:** one VARC question; all five questions of DILR Set 1; one QA question. The GradeScale source page reports 24/20/22 questions for the sections. VARC passage source is abbreviated.
- **CAT 2024 Slot 1:** four visible VARC items (Q1 independently checked, Q2–Q4 source key/explanation only); all five questions of the tournament DILR set; one QA question. The page reports 24/22/22 questions. VARC passage source is abbreviated.
- **CAT 2025:** 27 prior audit records—10 QA, 9 DILR, 8 VARC. They remain Grade C public reproductions, with source locator disagreements and two source-explanation errors preserved in the existing audit.

Outside the slot census, the TheCATExam archive page for **CAT 1991** was opened. It advertises 180 questions across three archive-labelled sections and visibly presents Q1 and its choices; that one item is in the corpus as retrieved but unsolved. The page claim is not treated as 180 retrieved or audited questions, and no slot is invented for this annual paper-era record.

Machine-readable question corpus: 49 records in total: 48 in the candidate CAT 2017–2025 slot scope plus one CAT 1991 archive item. Of the 49, 42 are structurally audited and independently answer-checked, six CAT 2023/2024 VARC questions have visible text and secondary explanations but no independent solution, and the CAT 1991 VARC-labelled item is retrieved but unsolved. No answer is officially corroborated. The live item-state totals are maintained in [`audit-status.json`](research/historical/audit-status.json) and checked by the corpus validator.

## DILR sets and VARC passages

Four complete shared DILR sets are represented: CAT 2023 Slot 1 housing grid; CAT 2024 Slot 1 tournament; and the two previously audited CAT 2025 sets. CAT 2023's essential diagram was retrieved and visually inspected. Its rules were exhaustively enumerated over 1,572,864 occupancy/parking candidates, allowing any parking assignment in Block XX and one parking house in Block YY. Two occupancy patterns (64 parking-labelled feasible assignments) remain. CAT 2024 group and schedule constraints were exhaustively enumerated; two solutions differ only by swapping group labels. All five answers in each set are invariant.

Four VARC passage groups are represented (CAT 2023 S1, CAT 2024 S1, CAT 2025 S2 and S3). All are incomplete transcripts or excerpts with ellipses. **Complete VARC passages retrieved: 0.** Question options and visible text are sufficient for the specifically listed item records, but no passage-level completeness is claimed.

## Earlier CAT archive leads

Search expanded earlier than 2017. A separate [`legacy-candidates.json`](research/historical/legacy-candidates.json) records 21 leads: TheCATExam lists 1991–2008 and 2016; PreviousYearPapers lists 1990–2017; 2009–2015 remains a gap in the first index. TheCATExam question pages for 1991, 1993 and 2000 were located; CATKing/CETKing PDF URLs tested for 1991/1993/2000 returned HTML rather than PDF bytes. Only CAT 1991 Q1 was visibly examined at item level, and its answer is unresolved. None is counted as a complete retrieved historical paper.

## Conflicts and gaps

Eight source-conflict records are logged in [`source-conflicts.json`](research/historical/source-conflicts.json), including 2IIM/GradeScale set labels for CAT 2024 DILR, a CAT 2024 VARC PDF footer that says CAT 2021 under a CAT 2024 header, AglaSem/2IIM slot-coverage differences, CAT 2025 locator and explanation defects, the 66-versus-68 reported question-count discrepancy, failed legacy PDF URLs, and an unresolved CAT 1991 grammar item ambiguity. No official response-sheet key disagreement has been established; official keys remain unchecked.

Remaining question-level item count for CAT 2017–2024: not yet computed. The section PDFs have an initial question locator, but no comprehensive item-to-page/set/passage extraction has been completed. Archive index counts are not substituted for this missing inventory.

