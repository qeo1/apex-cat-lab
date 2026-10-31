# CONTENT DIVERSITY AUDIT

Date: 2026-10-31

The comparison is at the reasoning-operator level. Broad topic overlap with a benchmark is expected; “superficial variant” means retaining its same core state variables and operation with only names/numbers/context changed. No item is a superficial renumbering or context swap. This is a documented editorial judgment, not a learned semantic-similarity score.

| Pilot item | Core structure | CAT benchmark | Nearest overlap / distinction | Review |
|---|---|---|---|
| APX-QA-001 | bounded integer compositions / coefficient counting | CAT 2025 Slot 2 QA Q14, GradeScale | bounded compositions/parity vs prime-exponent residue tuples | Distinct; no superficial variant flagged. |
| APX-QA-002 | Bayesian base-rate update | CAT 2025 Slot 2 QA Q2, GradeScale | Bayes posterior/base rate vs overlapping means | Distinct; no superficial variant flagged. |
| APX-QA-003 | two-constraint integer optimization | CAT 2025 Slot 3 QA Q3, GradeScale | two-resource integer profit optimum vs demographic linear constraint | Distinct; no superficial variant flagged. |
| APX-QA-004 | finite differences / quadratic sequence | CAT 2025 Slot 2 QA Q1, GradeScale | finite differences / extrapolation vs exponential substitution and roots | Distinct; no superficial variant flagged. |
| APX-QA-005 | Chinese remainder / periodic counting | CAT 2025 Slot 2 QA Q14, GradeScale | CRT periodic count vs modular exponent tuples | Distinct; no superficial variant flagged. |
| APX-QA-006 | inclusion–exclusion / exactly-one count | CAT 2025 Slot 2 QA Q14, GradeScale | exactly-one inclusion–exclusion vs digit-constrained minimum | Distinct; no superficial variant flagged. |
| APX-QA-007 | piecewise work-rate integration | CAT 2025 Slot 3 QA Q2, GradeScale | piecewise rate integration vs changing-workforce CAT rate model; same broad family, different event schedule | Distinct; no superficial variant flagged. |
| APX-QA-008 | weighted mean / solve unknown group size | CAT 2025 Slot 2 QA Q2, GradeScale | weighted-mean recovery of unknown group size vs overlapping consecutive means | Distinct; no superficial variant flagged. |
| APX-QA-009 | right-triangle altitude as point-to-line distance | CAT 2025 Slot 2 QA Q16, GradeScale | right-triangle altitude, circle area vs hexagon/trapezium area construction | Distinct; no superficial variant flagged. |
| APX-QA-010 | conditional probability by parity classes | CAT 2025 Slot 2 QA Q14, GradeScale | finite conditional pair probability vs broad CAT number/divisibility structures | Distinct; no superficial variant flagged. |
| APX-DILR-011 | permutation with adjacency block, precedence and case enumeration | CAT 2025 Slot 2 DILR Set 1 Q1–Q4, GradeScale | count schedules under adjacency/order rules vs threshold-derived partial order | Distinct; no superficial variant flagged. |
| APX-DILR-012 | derive a forced endpoint from shared permutation constraints | CAT 2025 Slot 2 DILR Set 1 Q1–Q4, GradeScale | minimum position across valid permutations vs identify necessary precedence | Distinct; no superficial variant flagged. |
| APX-DILR-013 | conditional completion of shared schedule | CAT 2025 Slot 2 DILR Set 1 Q1–Q4, GradeScale | conditional completion under C=4 vs infer order from noisy tests | Distinct; no superficial variant flagged. |
| APX-DILR-014 | conditional chain completion | CAT 2025 Slot 2 DILR Set 1 Q1–Q4, GradeScale | conditional slot occupant under E=3 vs threshold comparison | Distinct; no superficial variant flagged. |
| APX-DILR-015 | extremal position over all valid schedules | CAT 2025 Slot 2 DILR Set 1 Q1–Q4, GradeScale | extremal position over solution set vs partial-order comparability | Distinct; no superficial variant flagged. |
| APX-DILR-016 | matrix completion from row and column margins | CAT 2025 Slot 1 DILR Set 5 Q18–Q22, GradeScale | recover one cell from a row margin vs chained route occupancy | Distinct; no superficial variant flagged. |
| APX-DILR-017 | row-margin deduction | CAT 2025 Slot 1 DILR Set 5 Q18–Q22, GradeScale | recover another margin-linked cell; different row state, same shared table | Distinct; no superficial variant flagged. |
| APX-DILR-018 | column-margin deduction | CAT 2025 Slot 1 DILR Set 5 Q18–Q22, GradeScale | column residual using three row totals vs train-flow terminal segment | Distinct; no superficial variant flagged. |
| APX-DILR-019 | compare column allocations | CAT 2025 Slot 1 DILR Set 5 Q18–Q22, GradeScale | compare reconstructed column values vs route-flow equation | Distinct; no superficial variant flagged. |
| APX-DILR-020 | column-total share / ratio interpretation | CAT 2025 Slot 1 DILR Set 5 Q18–Q22, GradeScale | column/grand-total ratio vs route occupancy fractions | Distinct; no superficial variant flagged. |
| APX-VARC-021 | main idea / qualified thesis | CAT 2025 Slot 2 VARC Passage 1 Q1–Q4, GradeScale | qualified thesis of an original measurement-policy passage vs CAT passage central-claim inference | Distinct; no superficial variant flagged. |
| APX-VARC-022 | role of evidence / contrast | CAT 2025 Slot 2 VARC Passage 1 Q1–Q4, GradeScale | function of contrastive examples vs CAT examples/exception task | Distinct; no superficial variant flagged. |
| APX-VARC-023 | inference / model limitation | CAT 2025 Slot 3 VARC Passage 1 Q1–Q4, GradeScale | bounded proxy limitation inference vs CAT causal/history inference | Distinct; no superficial variant flagged. |
| APX-VARC-024 | identify implicit warrant | CAT 2025 Slot 2 VARC Passage 1 Q1–Q4, GradeScale | implicit warrant to a limited action vs CAT passage purpose/inference | Distinct; no superficial variant flagged. |
| APX-VARC-025 | application / resolve evidence conflict | CAT 2025 Slot 3 VARC Passage 1 Q1–Q4, GradeScale | apply decision rule to model/local-evidence conflict vs CAT passage-specific reform inference | Distinct; no superficial variant flagged. |

## Shared-set integrity and repeated operations

DILR-A is one five-event permutation space. Every question refers to the same five hard rules and solution set, then asks a different statistic or conditional; the set has three valid schedules. DILR-B is one shared 3×3 ledger with stated row and column margins and known cells; all five questions reuse the same uniquely completed table. Neither group is five unrelated prompts.

Some pilot items intentionally share mathematical families (e.g., two weighted-mean items, and three margin-linked DILR recovery/comparison prompts). They differ in unknown, representation, or operation; these are acknowledged local similarities rather than disguised claims of maximal diversity. QA-007 is the closest broad-family proximity to the CAT work-rate benchmark and is flagged for additional reviewer scrutiny before any scaled bank reuse. The CAT-2025 comparison corpus is only a 27-question sample and cannot support claims of uniqueness against all CAT papers or all candidate items.

