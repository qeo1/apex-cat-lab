"""Evidence gates for APEX original-question JSON records (standard library only)."""

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED = {
    "research": ["source_ids", "insight"],
    "benchmark": ["pyq_ids", "shared_skill", "structural_difference"],
    "engineering": ["structure_family", "novelty_rationale", "difficulty_rationale"],
    "validation": ["independent_solution", "uniqueness_check", "edge_case_check", "reviewer"],
}


def nonempty(value):
    return isinstance(value, str) and len(value.strip()) >= 20


def validate(record):
    errors = []
    if not re.fullmatch(r"APX-[A-Z]+-\d{3}", str(record.get("id", ""))):
        errors.append("id must match APX-SECTION-###")
    if record.get("section") not in {"VARC", "DILR", "QA"}:
        errors.append("section must be VARC, DILR or QA")
    for name in ("prompt", "explanation"):
        if not nonempty(record.get(name)):
            errors.append(f"{name} must contain at least 20 non-whitespace characters")
    if record.get("response_type") == "MCQ":
        choices, answer = record.get("choices"), record.get("answer")
        if not isinstance(choices, list) or len(choices) < 3 or len(set(choices)) != len(choices):
            errors.append("MCQ choices must have at least 3 unique entries")
        elif not isinstance(answer, int) or answer < 0 or answer >= len(choices):
            errors.append("MCQ answer must be a valid zero-based choice index")
    elif record.get("response_type") == "TITA":
        if record.get("choices") not in ([], None) or not isinstance(record.get("answer"), (str, int, float)):
            errors.append("TITA must have no choices and a scalar answer")
    else:
        errors.append("response_type must be MCQ or TITA")
    hints = record.get("hint_ladder")
    if not isinstance(hints, list) or len(hints) < 2 or not all(nonempty(h) for h in hints):
        errors.append("hint_ladder must contain at least two substantive hints")
    for block, keys in REQUIRED.items():
        values = record.get(block)
        if not isinstance(values, dict):
            errors.append(f"{block} must be an object")
            continue
        for key in keys:
            value = values.get(key)
            if key.endswith("_ids"):
                if not isinstance(value, list) or not value or not all(isinstance(v, str) and v.strip() for v in value):
                    errors.append(f"{block}.{key} must contain at least one identifier")
            elif not nonempty(value):
                errors.append(f"{block}.{key} must contain at least 20 characters")
    if record.get("status") not in {"draft", "research_ready", "validation_pending", "approved"}:
        errors.append("status must be draft, research_ready, validation_pending or approved")
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--approved-only", action="store_true")
    args = parser.parse_args()
    records = json.loads(args.path.read_text(encoding="utf-8"))
    if not isinstance(records, list):
        raise SystemExit("Question file must be a JSON array")
    seen = set()
    total_errors = 0
    for i, record in enumerate(records, 1):
        errors = validate(record)
        qid = record.get("id", f"row {i}")
        if qid in seen:
            errors.append("duplicate id")
        seen.add(qid)
        if args.approved_only and record.get("status") != "approved":
            errors.append("not approved; excluded from publishable count")
        for error in errors:
            total_errors += 1
            print(f"{qid}: {error}")
    approved = sum(r.get("status") == "approved" for r in records)
    print(f"records={len(records)} approved={approved} errors={total_errors}")
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())

