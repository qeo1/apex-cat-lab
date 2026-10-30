# CAT 2025 Slot 1: first question-level audit

Audit opened: 2026-10-31 (Asia/Kolkata)  
Scope: selected CAT 2025 Slot 1 items and source-level sectional fingerprints.  
Question-level audited fingerprints admitted: **1**. This is not a complete paper audit and is not an official-key verification.

## Source basis and authenticity

The official CAT 2025 advertisement from IIM Kozhikode confirms that the exam was held on 30 November 2025 in three sessions. It does not contain question-level papers. The full Slot 1 question transcription consulted for this audit is GradeScale, cross-checked against CATKing and Mockat's independent reproduction. These are secondary copies; the official candidate response-sheet/key was not available for direct public retrieval. Therefore this fingerprint is **grade C** (institutional/archive reproduction, not a verified official response sheet).

## Fingerprint PYQ-CAT25-S1-QA-09

| Dimension | Observation |
|---|---|
| Bibliographic identifier | CAT 2025, Slot 1, QA, item 9 of 22 in the question-level archive (some full-paper PDFs use a different overall sequence number) |
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

## Paper-level fingerprint: CAT 2025 Slot 1

IMS reports 68 total questions in three separately timed 40-minute sections: VARC 24 (16 RC + 8 VA), DILR 22 (five sets sized 5, 4, 5, 4, 4), QA 22. It reports a 45 MCQ / 23 TITA split. Its VARC/section counts and DILR set sizes are useful cross-checks; the precise formats/topic buckets remain secondary-source claims. IMS's QA topic narrative says Algebra 4 while its later table says Algebra 5 (and totals 22 only with 5), so topic frequencies are marked disputed pending item-by-item audit. These are not sufficient evidence for predictive claims.

## Next audit steps

1. Record all five DILR set fingerprints and the remaining question families from each section; verify answer keys independently and log suspected source errors.
2. Obtain or inspect primary official response sheets where publicly and legitimately available; otherwise retain grade C.
3. Repeat for Slot 2 and Slot 3, then cross-check 2024 before selecting benchmark structures for the 25-original pilot.

