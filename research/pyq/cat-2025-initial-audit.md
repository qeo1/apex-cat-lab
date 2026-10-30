# CAT 2025 Slots 1–3: initial question-level audit

Audit opened: 2026-10-31 (Asia/Kolkata)  
Scope: three sampled QA items across CAT 2025 Slots 1–3, plus secondary-source section-level fingerprints.  
Question-level audited fingerprints admitted: **3**. This is not a complete paper audit and is not an official-key verification.

## Source basis and authenticity

The official CAT 2025 advertisement from IIM Kozhikode confirms that the exam was held on 30 November 2025 in three sessions. It does not contain question-level papers. The full Slot 1 question transcription consulted for this audit is GradeScale, cross-checked against CATKing and Mockat's independent reproduction. These are secondary copies; the official candidate response-sheet/key was not available for direct public retrieval. Therefore this fingerprint is **grade C** (institutional/archive reproduction, not a verified official response sheet).

## Fingerprint PYQ-CAT25-S1-QA-DIGITMIN

| Dimension | Observation |
|---|---|
| Bibliographic identifier | CAT 2025, Slot 1, QA digit-constraint minimisation item. Locator disputed: GradeScale calls it QA Q3; CATKing full-paper PDF Q49 (QA Q3 after the first two sections); Mockat labels it Q9/22. Official item numbering is not checked. |
| Source records | GradeScale Slot 1 page; CATKing Slot 1 QA PDF; Mockat item page. URLs are in `SOURCE_LEDGER.md`. |
| Task family | Digit constraints + primality classification + minimisation + divisor counting |
| Representation | Finite admissible digit set, place-value ordering, prime/non-prime partition, prime factorisation |
| Core reasoning | Filter digits by predicate; infer both non-prime digits are forced; choose the smallest allowable prime; minimise lexicographically; count divisors from exponents |
| Response type | TITA, according to the reproduced question |
| Published answer | 6 (consistent across the consulted transcriptions) |
| Independent verification | Non-zero digits that are not squares are `{2,3,5,6,7,8}`. Prime digits are `{2,3,5,7}` and the only non-prime digits are `{6,8}`. Exactly one prime and distinct digits force 6 and 8 plus one prime. The smallest valid three-digit number is 268 (choose 2 and order as 2,6,8). Since `268 = 2² × 67`, it has `(2+1)(1+1)=6` positive divisors. |
| Source conflict / correction | GradeScale's explanation says 628 is the minimum, which is false: 268 is smaller and satisfies the constraints. Its reported final divisor count 6 is still correct. CATKing gives 268 and the same count. We retain this as an explanation-quality discrepancy, not an answer-key conflict. |
| Originality boundary | This record is a compact structural fingerprint, not a republication of the full PYQ. Any derived pilot item must change the underlying constraint interaction or reasoning path, not merely replace digits. |
| Confidence | Prompt identity: medium-high across independent public copies. Correct answer: independently verified mathematically. Official-key match: unverified. |

## Fingerprint PYQ-CAT25-S3-QA-DIGITRANGE

| Dimension | Observation |
|---|---|
| Bibliographic identifier | CAT 2025, Slot 3, QA four-digit digit-sum range item. GradeScale labels it QA Q6; Scorebuddy labels the matching item QA Q20. The locator mapping is unresolved without the official response sheet. |
| Source records | GradeScale Slot 3 full paper; Scorebuddy Slot 3 item index. URLs are in `SOURCE_LEDGER.md`. |
| Task family | Place-value digit constraints + extrema over a finite feasible set |
| Representation | Four decimal digits and overlapping three-position sums, plus a difference condition between adjacent places |
| Core reasoning | Subtract the two sum equations to link the thousands and units digits; constrain the end digits by digit bounds; enumerate the remaining two cases |
| Published answer | 811 in GradeScale's reproduction |
| Independent verification | Let digits be `A B C D`. The conditions give `A+B+C=15`, `B+C+D=16`, `C=D+6`. Subtraction gives `D=A+1`. Since `C≤9`, `D≤3`; since `A≥1`, `D≥2`. If `D=2`, `(A,B,C)=(1,6,8)` and the number is 1682. If `D=3`, `(A,B,C)=(2,4,9)` and the number is 2493. These are the only feasible cases, and the difference is `2493−1682=811`. |
| Source conflict / correction | Correct answer independently reproduced. Archive numbering differs (GradeScale Q6 vs Scorebuddy Q20); no official locator check. |
| Originality boundary | Do not make a pilot item by changing the digits. A derived item must alter the constraint graph or the optimization target and cite a global-source insight as well as this benchmark. |
| Confidence | Problem fingerprint: high across the matching constraints visible in both archives. Correct answer: independently verified. Official-key match: unverified. |

## Fingerprint PYQ-CAT25-S2-QA-DIVMOD3

| Dimension | Observation |
|---|---|
| Bibliographic identifier | CAT 2025 Slot 2, QA, GradeScale Q14. Career Launcher provides a second reproduction. |
| Task family | Count positive divisors in a specified residue class modulo 3 |
| Representation | Prime exponents in the factorization of a fixed integer; residue classes of each prime |
| Core reasoning | Exclude divisors with a factor of 3; reduce 2 and 5 to −1 and 7 to 1 modulo 3; count exponent tuples with even parity. |
| Published answer | 42 |
| Independent verification | With divisor exponents a=0…6, c=0…3, d=0…2 and b=0…5: b must be 0. The congruence is (−1)^(a+c)=1, giving 14 valid (a,c) pairs and 3 choices of d: 42. |
| Confidence | Fingerprint and arithmetic independently checked against a grade C reproduction. Official-key match unverified. |

## Paper-level fingerprint: CAT 2025 Slot 1

IMS reports 68 total questions in three separately timed 40-minute sections: VARC 24 (16 RC + 8 VA), DILR 22 (five sets sized 5, 4, 5, 4, 4), QA 22. It reports a 45 MCQ / 23 TITA split. Its VARC/section counts and DILR set sizes are useful cross-checks; the precise formats/topic buckets remain secondary-source claims. IMS's QA topic narrative says Algebra 4 while its later table says Algebra 5 (and totals 22 only with 5), so topic frequencies are marked disputed pending item-by-item audit. These are not sufficient evidence for predictive claims.

## Paper-level fingerprints: CAT 2025 Slots 2 and 3

GradeScale’s Slot 2 and Slot 3 transcriptions each report the same 68-question, 24/22/22 section counts and 40 minutes per section. Slot 2’s displayed family list spans assignment, bar-chart/scatter-plot DI, distribution, ranking and scheduling in DILR; its QA list includes divisibility/factors, functions, inequalities, logarithms, extrema, percentages, quadratics, sequences, work/rate and geometry. Slot 3’s DILR list spans arithmetic DI, assignment, circular/dynamic arrangement, connectivity, distribution, line graphs, caselets, grids and tables; QA list includes functions, inequalities, logarithms, quadratics, sequences, rates and geometry. These are archive-level tags, not a verified item-by-item taxonomy. We have only one sampled Slot 2 question; the Slot 3 digit-range record above has locator disagreement with Scorebuddy. Neither is a complete census.

## Next audit steps

1. Record all five DILR set fingerprints and the remaining question families from all CAT 2025 slots; verify answers independently and log suspected source errors.
2. Obtain or inspect primary official response sheets where publicly and legitimately available; otherwise retain grade C.
3. Repeat for Slot 2 and Slot 3, then cross-check 2024 before selecting benchmark structures for the 25-original pilot.

