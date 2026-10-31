# CAT PYQ structural analytics — evidence-limited seed

Date: 2026-10-31. This note describes inspected questions only. The sample is purposive, small and non-random; it is not a topic-frequency estimate, prediction, psychometric calibration or representative difficulty distribution.

## New cross-year analysis

| Examination evidence | Observed reasoning architecture | Why it matters | Verification boundary |
|---|---|---|---|
| CAT 2017 S1 QA Q1 | A ratio is stated now and changes to another ratio after a common time increment; normalize one age and solve one linear equation | Converts a verbal time relation to a compact equation without needing actual ages | Independently solved from the scanned question; 2IIM's answer control not checked |
| CAT 2023 S1 QA Q1 | Prime valuations impose componentwise lower bounds in two successive divisibility directions | The first minimum changes the exponent target for the second minimum | Independent exponent comparison yields 15; source is Grade C |
| CAT 2023 S1 DILR Set 1 | Spatial adjacency and occupancy interact with local neighbor counts and an extremal/threshold price; shared deductions drive five dependent questions | Representation must preserve block boundaries and road edges; cases must be carried rather than prematurely completed | Exhausted 1,572,864 candidates with all possible Block XX parking assignments allowed; two occupancy patterns and 64 parking-labelled assignments remain, with the same five answers |
| CAT 2023 S1 VARC P1 Q1 | Reject a statement by controlling geographic scope and regional category | A plausible global framing is invalid when the passage describes South-South links only | Visible passage supports the check; source passage contains ellipses |
| CAT 2024 S1 QA Q1 | Count onto functions by inclusion–exclusion over missing codomain values | Overlapping exclusions require adding back functions omitting two values | Direct arithmetic confirms 540; Grade C key agrees |
| CAT 2024 S1 DILR Set 1 | Partition six teams, infer pair multiplicities, then construct perfect matchings by round under duplicated-round and anchored fixtures | Pair frequency and round scheduling are coupled; label symmetry can look like distinct solutions | Finite enumeration returns two solutions related only by group labels; all five answers invariant |
| CAT 2024 S1 VARC P1 Q1 | Compare two systems by a shared consequence while rejecting a tempting attribute true of only one | Requires separating parallel mechanisms (both can inhibit creativity) from one-sided mechanisms (guild entry restrictions) | Relevant passage excerpts are visible; full passage is not reproduced |
| CAT 2025 audited sample | Includes divisibility parity, exponent thresholds, constrained digit minimization, piecewise inequalities, workforce-rate updates, partial orders and scope/exception inference | Shows a mix of short mathematical pivots and shared-constraint reasoning; correction of source explanations matters | 27 actual questions individually audited; all sources Grade C and official key unchecked |

## Seed corpus composition

The 2017–2025 slot corpus has 48 question-level records: 42 independently answer-checked and structurally audited, and six CAT 2023/2024 VARC questions retrieved with only a secondary published answer/explanation. One additional record is a CAT 1991 VARC-labelled question retrieved from an annual-paper webpage but left unsolved. For audited slot questions, the counts are 13 QA, 19 DILR and 10 VARC. Four shared DILR sets are complete at the set-prompt/question level; four represented VARC passage groups remain incomplete. No question has official answer-key corroboration.

The 2023 housing set's candidate-space enumeration and the 2024 tournament schedule enumeration are deterministic validation, not human response-time data. The six VARC records whose answers remain unchecked are not included in independent answer-validation counts.

## Emerging taxonomy (provisional)

- **Constraint representation:** grid plus graph adjacency; tournament pair-frequency matrix; route-flow equations; partial order.
- **Constraint propagation:** a maximum/minimum statement fixes a branch or a group partition and then unlocks dependent items.
- **State-space management:** enumerate only feasible cases; test answer invariants over remaining states.
- **Algebraic compression:** normalize a ratio; compare prime exponents; use inclusion–exclusion rather than listing mappings.
- **Scope and evidence control:** regional scope, comparison class, qualifier, and distinction between evidence and a question left open by the author.
- **Source-aware reasoning:** preserve source-local numbering and explanation defects rather than silently harmonizing them.

These labels are candidate tools for annotation. The corpus is too small and too uneven to assert that they characterize CAT globally.

## Difficulty state

The historical records remain `unrated` in the machine-readable database. No candidate-performance or response-time data was available, and no complete difficulty comparison across years was performed. The old CAT 2025 analyses are retained as secondary commentary and do not calibrate this broader corpus. Difficulty should be assigned item by item after further paper coverage and independent review.

## Source and coverage limits

The 63 section PDFs downloaded for 2017–2024 are Grade C reproductions. They have page counts, hashes, sampled question-page rendering and source-local controls. They are not officially sourced response sheets; a wrong year footer is present in one sampled CAT 2024 VARC file, and source set labels differ for CAT 2024 DILR. Complete paper/page/item coverage review is still pending. Legacy CAT paper links discovered before 2017 are not counted as retrieved material. No frequency chart is calculated from a source index or topic list.

