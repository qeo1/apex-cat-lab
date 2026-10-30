# Research-to-question pipeline

The pipeline is evidence-gated. A source or PYQ fingerprint alone never counts as a pilot question.

1. **Capture sources.** Record source URL, author/institution, publication/update date, accessed date, source type, confidence grade, exact claim used, and access limits in `SOURCE_LEDGER.md`.
2. **Fingerprint CAT benchmarks.** Store the examination identifier, structural task, representation, dependency pattern, response mode, and source conflicts. Do not copy full copyrighted question wording into generated content.
3. **State a research insight.** Cite a specific research source and extract only the idea or reasoning operator being used.
4. **Engineer an original structure.** Write down the transformation and why it changes the actual reasoning path, rather than merely swapping names, context or values.
5. **Solve independently.** A second derivation or exhaustive finite check must verify the answer; for reading items, an independent evidence audit must support the key and rule out distractors.
6. **Adversarially review.** Check ambiguity, edge cases, alternative interpretations, accidental duplication and answer-key leakage.
7. **Compare with CAT.** State the shared benchmark skill and the structural differences. Assign an internal difficulty rationale; never convert it to a percentile prediction.
8. **Admit only validated items.** An item counts toward the 25-question pilot only when all required fields are complete and status is `approved`.

The current pipeline is documented, but no pilot items have passed it yet. Current auditable benchmark content: three CAT fingerprints spanning CAT 2025 Slots 1–3; zero original pilot questions.

