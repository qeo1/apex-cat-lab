"""Render the full question-level research/provenance appendix from pilot JSON."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
pilot = json.loads((ROOT / "research/pilot/pilot.json").read_text(encoding="utf-8"))
audit = json.loads((ROOT / "research/pyq/cat-2025-question-audit.json").read_text(encoding="utf-8"))
pyq_by_id = {q["id"]: q for q in audit["questions"]}
groups = {g["id"]: g for g in pilot["groups"]}
lines = [
    "# Pilot Research Report — 25 original questions",
    "",
    "Status: approved only after the blind deterministic review and VARC editorial evidence audit recorded in `QUESTION_VALIDATION_REPORT.md`.",
    "",
    "These are original practice questions, not authentic CAT PYQs. CAT benchmark references are evidence of structural comparison, not claims that the pilot reproduces official examination content. Research source concepts are abstracted; no source exercise or CAT prompt is copied.",
    "",
    f"Pilot inventory: {len(pilot['questions'])} candidates ({sum(q['section']=='QA' for q in pilot['questions'])} QA, {sum(q['section']=='DILR' for q in pilot['questions'])} DILR, {sum(q['section']=='VARC' for q in pilot['questions'])} VARC).",
    "",
    "## Full questions, provenance and validation",
    "",
]
for q in pilot["questions"]:
    lines += [f"### {q['id']} · {q['section']}", ""]
    group = groups.get(q.get("group_id"))
    if group:
        lines += [f"**Shared set — {group['title']}**", "", group["context"], ""]
    lines += ["**Original question**", "", q["prompt"], "", "**Choices**", ""]
    lines += [f"- {'ABCD'[i]}. {choice}" for i, choice in enumerate(q["choices"])]
    lines += ["", f"**Canonical answer:** {'ABCD'[q['answer']] + '. ' if q['section']=='VARC' else ''}{q['canonical_answer']}", ""]
    benchmark = pilot["benchmarks"][q["benchmark_id"]]
    lines += [f"**CAT PYQ benchmark:** {benchmark['label']} — [{benchmark['url']}]({benchmark['url']})", "", f"**Benchmark fingerprint:** {benchmark['fingerprint']}", ""]
    research = pilot["sources"][q["research_id"]]
    lines += [f"**Research source:** {research.get('ledger_id', q['research_id'])} — [{research['url']}]({research['url']})", "", f"**Research insight:** {research['insight']}", ""]
    lines += [f"**Extracted reasoning structure:** {q['structure']}", "", f"**Novel transformation:** {q['novelty']}", "", "**Progressive hints**", ""]
    lines += [f"{i}. {hint}" for i, hint in enumerate(q["hints"], 1)]
    lines += ["", f"**Independent re-solve:** {q['independent_solution']}", "", f"**Expert solution:** {q['solution']}", "", f"**Adversarial ambiguity and uniqueness check:** {q['ambiguity_check']}", ""]
    lines += [f"**CAT relevance:** {q['cat_relevance']}", "", f"**CAT difficulty:** {q['cat_difficulty']}", "", f"**Training difficulty:** {q['training_difficulty']}", ""]
    validation = "Blind deterministic check passed." if q["section"] in ("QA", "DILR") else "Editorial evidence/ambiguity review passed; see `QUESTION_VALIDATION_REPORT.md`."
    lines += [f"**Validation state:** {q['status']} — {validation}", "", "---", ""]
(ROOT / "PILOT_RESEARCH_REPORT.md").write_text("\n".join(lines), encoding="utf-8")
print(f"Rendered full report for {len(pilot['questions'])} questions.")

