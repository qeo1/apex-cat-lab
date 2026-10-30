# CAT question pattern library — coding proposal

Status: framework only. No frequency or forecast claims are supported by the current evidence.

Use one record per inspected question or DILR set. Keep source observations separate from analyst interpretation.

## Shared record fields

- `year`, `slot`, `section`, and source question/set number
- exact source URL and retrieval date
- authenticity grade (`A` official, `B` traceable official response sheet, `C` established reproduction, `D` memory-based, `E` unverified)
- answer-key source and any answer or wording conflict
- response type (MCQ / TITA), if established by the source
- observed task, representation, and dependency structure
- analyst difficulty rationale, kept distinct from any coaching-provider rating

## VARC dimensions

- RC passage domain and central task: main idea, inference, detail, purpose, tone, structure, application
- VA form: para formation, summary, sentence placement, odd sentence, or other (record source wording)
- evidence span and distractor rationale, only when full question text and key can be checked
- passage density and cross-paragraph integration, with a written rubric before scoring

## DILR dimensions

- set entities and attributes
- representation: table, chart, graph, ordering, network, schedule, assignment, or mixed
- constraints: equality, inequality, exclusivity, capacity, sequence, conditional, optimization
- number of cases, cross-question dependencies, and whether one answer unlocks another
- arithmetic load and source-supported set size

## Quant dimensions

- primary topic and any genuine secondary topics
- required operations or theorem, without inferring from superficial story context
- number of reasoning steps, algebraic burden, and calculation load
- MCQ/TITA only if established in the source

## Promotion rules

1. Never fill unknowns with guesses; use `unknown` and a note.
2. Do not calculate topic frequencies until the inspected denominator and missing-slot coverage are published.
3. Do not forecast CAT 2026 from a single slot or coaching commentary.
4. Retain conflicting archive counts and answer keys as explicit unresolved records.
5. Do not republish full copyrighted question text; store bibliographic pointers and short internal tags instead.

This schema is an analysis aid, not a claim that the proposed dimensions are validated predictors of CAT outcomes.

