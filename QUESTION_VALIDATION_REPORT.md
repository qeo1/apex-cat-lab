# QUESTION VALIDATION REPORT

Date: 2026-10-31

## Scope and result

The 25-item pilot has 10 QA, 10 DILR questions (two complete five-question shared-rule sets), and 5 VARC questions on one original passage. All 25 are approved for the labelled Research Pilot, subject to the evidence limits below. They are original practice items, never authentic PYQs.

The blind deterministic solver independently derived 20 numerical/logical answers from the prompts and set rules without reading authored answer or solution fields. Result: 20 checked, 0 mismatches. The QA solver enumerates complete bounded domains / exact formulas; DILR-A enumerates all 120 schedules under shared rules; DILR-B reconstructs table cells from margins and checks row/column totals. Validator: `research/pilot/validate_pilot.py`. VARC was reviewed in a separate evidence/ambiguity pass below. This is an independent solution pass within the build, not an external human peer review or psychometric field trial.

## Deterministic checks

| Group | Method | Result |
|---|---|---|
| QA-001–010 | Bounded enumeration, exact rational arithmetic, feasible integer enumeration, sequence verification, congruence scan, work/mixture calculations, geometry identities, finite pair enumeration | 10/10 match canonical choices |
| DILR-011–015 | Enumerate all permutations satisfying the five shared scheduling rules; derive each requested statistic/conditional | 5/5 match |
| DILR-016–020 | Reconstruct six missing table cells from row/column margins; check all margins and requested comparisons | 5/5 match |
| VARC-021–025 | Manual editorial evidence map, scope/distractor audit, uniqueness check | 5/5 have one text-supported best answer; see below |

## VARC textual evidence and distractor audit

Passage paragraph references below count from the first paragraph of the original passage in `research/pilot/pilot.json`.

| Item | Key | Textual evidence for key | Distractor/evidence audit | Ambiguity result |
|---|---|---|---|---|
| APX-VARC-021 | B | P2: maps can direct scarce crews but a first-pass signal is not a final verdict. P4–P5: publish limits, invite local input, keep decisions revisable. | A says replace residents, contradicted by P4–P5. C says maps cannot inform policy, contradicted by P2. D proposes equal allocation and claims maps cannot measure need; neither follows, and P2 explicitly uses maps to prioritize inspection. | B alone preserves both usefulness and qualification. |
| APX-VARC-022 | B | P1 names choices of surface, hour, height and averaging scale; noon roof vs dusk bus stop illustrates a mismatch between measured location/time and human exposure. | A denies satellite measurement capability, which the passage does not say. C asserts a universal temperature comparison not established. D attributes systematic memory error to residents, absent from the text. | B describes the example’s stated function without asserting which site is hotter. |
| APX-VARC-023 | B | P3: canopy percentage is not identical to access to shade and says little about whether shade reaches pavement when needed. | A reverses P1’s warning about equal block averages. C makes an “every sensor” superiority claim absent from the passage. D asserts automatic fairness from more measurements, contrary to the emphasis on assumptions and use. | B is directly licensed; distractors add universals or reverse the stated limit. |
| APX-VARC-024 | A | P2 says maps can direct crews toward places otherwise overlooked; P4 says use the map to select sites for closer observation. | B’s equal density premise is absent and unnecessary. C’s “always free of bias” claim is absent. D turns a screening tool into a sole funding rule, which P2/P4 reject. | A supplies the limited bridge from a first-pass signal to inspection; no other option supports that narrow claim. |
| APX-VARC-025 | C | P4: where model and local accounts diverge, treat disagreement as information about omissions; use maps to select closer observations. | A dismisses local accounts, contrary to P4. B treats a revised score as final, contrary to P2/P5. D demands a perfect map, explicitly rejected in P4. | C follows the passage’s specified response to divergence. |

The passage is self-contained and original; its claims are framed as a reasoned argument about measurement and municipal decisions, not as sourced empirical findings. Correct options track explicit or narrowly inferable text. No two choices are defensible under the question wording after the scope terms (“best”, “according to the author”, “can”) are applied.

## Approval limits

Approval here means internal content/answer validation and permission to include in a clearly labelled pilot. It does not establish item-response performance, calibrated difficulty, CAT equivalence, external editorial sign-off, or broad population fairness. CAT and training difficulty are separate expert estimates, not measured statistics. The source benchmark records are Grade C reproductions.

