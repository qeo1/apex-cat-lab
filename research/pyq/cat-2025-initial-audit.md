# CAT 2025 Slots 1–3: initial question-level audit

Audit opened: 2026-10-31 (Asia/Kolkata)  
Scope: 25 actual question items from CAT 2025 Slots 1–3. This is still a partial paper audit and not an official-key verification.  
Question-level audited fingerprints admitted: **27** (10 QA, 9 DILR, 8 VARC), all Grade C public reproductions. Machine-readable inventory: [question audit JSON](cat-2025-question-audit.json).

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

## Audited question coverage beyond the three detailed QA fingerprints

The complete CAT 2025 Slot 1 DILR Set 5 (Q18–22) was inspected and independently re-solved. It is a five-item train-route occupancy model combining segment-capacity sums, a divisibility condition, a fractional boarding rule, and a route-flow table. The independently derived sequence of answers is **140, 50, 80, 40, 60**. No answer-key conflict was found in the visible transcription.

The complete CAT 2025 Slot 2 DILR Set 1 (Q1–4) was inspected and independently re-solved. It uses ping/non-ping results to form a partial order over ball and hoop diameters. The answers **6**, **D (not necessarily true)**, **H2<H3<H4<H1**, and **12 or 13** follow from the original ping rule. The archive explanation contains a direction error: a ball that pings is no larger than the hoop, but one H4 explanation sentence says the pinging balls are larger. This is an explanation error; the four keyed results remain independently supported.

For VARC, Q1–Q4 under Passage 1 were inspected in the Slot 2 and Slot 3 transcriptions. Slot 2 fingerprints the distinction between examples of biased/erroneous output and explicit uncertainty, figurative mapping, and central-claim disagreement. Slot 3 fingerprints historical bridge, weaken-except, causal attribution, and identifying an explicitly unmet policy demand. The excerpted text supports the audited keys, but ellipses limit full-passage evidence checks. All eight keys were checked against the visible text and option logic; official keys are unchecked.

Additional QA items independently checked from the same public archives are CAT 2025 Slot 1 Q6 (power-product threshold m=58), Slot 2 Q1–Q3 (exponential substitution/root products: 20; shifted averages: 49; absolute-value inequality: (-∞,-3)∪(3,∞)), and Slot 3 Q1–Q3 (weighted marked price: 525; changing work crew: two additional members; constrained stream maximum: 700). Full compact fingerprints and calculations are in the JSON inventory.

## Paper-level fingerprints: CAT 2025 Slots 2 and 3

GradeScale’s Slot 2 and Slot 3 transcriptions each report 68 questions and 40 minutes per section. Slot 2’s visible DILR opening includes threshold-order Set 1 and an author-publication data set; its top-level family list also names assignment, distribution, relative ranking, scatter and scheduling. Slot 3’s DILR list names trade-flow arithmetic, assignments, circular/dynamic arrangement, connectivity, line graphs, caselets and grids. These are archive-level topic tags, not an item-by-item taxonomy. The sampled question locators in other archives still conflict for two QA items. The audit remains **27/204**, not complete.

## Next audit steps

1. Continue the remaining 179 question items, prioritizing QA and text-readable DILR/VARC content; log image or excerpt access gaps rather than reconstructing them.
2. Obtain or inspect primary official response sheets where publicly and legitimately available; otherwise retain grade C.
3. Repeat for Slot 2 and Slot 3, then cross-check 2024 before selecting benchmark structures for the 25-original pilot.


