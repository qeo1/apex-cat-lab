"""Integrity checks for the evidence-first historical CAT corpus."""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HIST = ROOT / "research" / "historical"


def read(name):
    return json.loads((HIST / name).read_text(encoding="utf-8"))


def validate(data):
    errors, warnings = [], []
    sources = {s["id"]: s for s in data["sources"]}
    papers = {p["id"]: p for p in data["papers"]}
    legacy_papers = {p["id"]: p for p in data.get("legacy_papers", [])}
    all_papers = {**papers, **legacy_papers}
    questions = data["questions"]
    q_by_id = {q.get("id"): q for q in questions}
    if len(q_by_id) != len(questions):
        errors.append("duplicate question id")
    fingerprint_keys = [q.get("fingerprint_key") for q in questions]
    if len(set(fingerprint_keys)) != len(fingerprint_keys):
        errors.append("duplicate fingerprint_key")
    if len(sources) != len(data["sources"]):
        errors.append("duplicate source id")
    if len(papers) != len(data["papers"]):
        errors.append("duplicate paper-section id")

    for q in questions:
        qid = q.get("id", "<missing-id>")
        if not re.fullmatch(r"CAT-\d{4}-(S\d+|PAPER)-(VARC|DILR|QA)-Q\d+", qid):
            errors.append(f"{qid}: malformed stable question id")
        if q.get("paper_id") not in all_papers:
            errors.append(f"{qid}: unknown paper_id {q.get('paper_id')}")
        else:
            p = all_papers[q["paper_id"]]
            if any(q.get(k) != p.get(k) for k in ("year", "slot")) or (p.get("section") is not None and q.get("section") != p.get("section")):
                errors.append(f"{qid}: year/slot/section disagrees with parent paper")
        for sid in q.get("source_ids", []):
            if sid not in sources:
                errors.append(f"{qid}: unknown source {sid}")
        if len(q.get("source_ids", [])) != len(q.get("source_urls", [])):
            # Multi-source records may need multiple URLs; check every URL is registered.
            registered_urls = {sources[s]["url"] for s in q.get("source_ids", []) if s in sources}
            if any(url not in registered_urls for url in q.get("source_urls", [])):
                errors.append(f"{qid}: source URL lacks a matching registered source")
        for linked in ("set_id", "passage_id"):
            if q.get(linked) is not None and not isinstance(q[linked], str):
                errors.append(f"{qid}: {linked} must be a string or null")
        if q.get("answer_state") == "independently_verified" and not q.get("independent_answer"):
            errors.append(f"{qid}: marked independently verified without an independent answer")
        if q.get("official_key_state") == "corroborated" and not any(sources[s]["evidence_grade"] == "A" for s in q.get("source_ids", []) if s in sources):
            errors.append(f"{qid}: official corroboration lacks a primary-grade source")
        if not q.get("reasoning_fingerprint") or len(q["reasoning_fingerprint"].strip()) < 20:
            errors.append(f"{qid}: missing substantive structural fingerprint")

    for pid, p in papers.items():
        if any(s not in sources for s in p.get("source_ids", [])):
            errors.append(f"{pid}: unknown source foreign key")
        related = [q for q in questions if q.get("paper_id") == pid]
        audited = sum(q.get("retrieval_state") == "question_audited" for q in related)
        if p.get("question_audited_count") != audited:
            errors.append(f"{pid}: audited count {p.get('question_audited_count')} != question records {audited}")
        if p.get("question_indexed_count") != len(related):
            errors.append(f"{pid}: indexed count must equal actual item records; expected {len(related)}")
        if p.get("complete_paper") and p.get("acquisition_state") not in {"paper_complete_and_checked", "official_paper_complete_and_checked"}:
            errors.append(f"{pid}: complete-paper claim without a checked complete acquisition state")
        if p.get("official_corroboration_count", 0) > sum(q.get("official_key_state") == "corroborated" for q in related):
            errors.append(f"{pid}: official corroboration count exceeds individually corroborated questions")

    sets = {s["id"]: s for s in data["sets"]}
    passages = {p["id"]: p for p in data["passages"]}
    for collection_name, collection in (("set", data["sets"]), ("passage", data["passages"])):
        seen = set()
        for group in collection:
            gid = group["id"]
            if gid in seen:
                errors.append(f"duplicate {collection_name} id {gid}")
            seen.add(gid)
            if group.get("paper_id") not in papers:
                errors.append(f"{gid}: unknown paper_id")
            if any(s not in sources for s in group.get("source_ids", [])):
                errors.append(f"{gid}: unknown source foreign key")
            if len(group.get("question_ids", [])) != len(set(group.get("question_ids", []))):
                errors.append(f"{gid}: duplicate question reference")
            for qid in group.get("question_ids", []):
                q = q_by_id.get(qid)
                if not q:
                    errors.append(f"{gid}: unknown question reference {qid}")
                elif q.get("paper_id") != group.get("paper_id"):
                    errors.append(f"{gid}: linked question belongs to another paper")
                elif collection_name == "set" and q.get("set_id") != gid:
                    errors.append(f"{gid}: question {qid} does not point back to its set")
                elif collection_name == "passage" and q.get("passage_id") != gid:
                    errors.append(f"{gid}: question {qid} does not point back to its passage")

    if sets.keys() & passages.keys():
        errors.append("set and passage IDs overlap")
    fingerprint_owners = defaultdict(list)
    for q in questions:
        normalized = re.sub(r"\W+", " ", q.get("reasoning_fingerprint", "").lower()).strip()
        if normalized:
            fingerprint_owners[normalized].append(q["id"])
    for fingerprint, owners in fingerprint_owners.items():
        if len(owners) > 1:
            warnings.append(f"possible repeated structural fingerprint across questions: {', '.join(owners)}")

    # The candidate 2017-2025 slot catalog is metadata only. Keep its exact
    # scope and reject silent omissions/repeats in the currently documented model.
    candidate_rows = [p for p in data["papers"] if 2017 <= p["year"] <= 2025]
    years_slots = Counter((p["year"], p["slot"]) for p in candidate_rows)
    expected = {(y, slot) for y in range(2017, 2026) for slot in range(1, (2 if y <= 2019 else 3) + 1)}
    if set(years_slots) != expected or any(count != 3 for count in years_slots.values()):
        errors.append("candidate slot-section census is incomplete or has duplicate/missing section rows")

    files = data.get("acquired_files", [])
    filenames = [f.get("filename") for f in files]
    if len(set(filenames)) != len(filenames):
        errors.append("duplicate acquired PDF filename")
    file_keys = [(f.get("year"), f.get("slot"), f.get("section")) for f in files]
    expected_files = {(y, slot, section) for y in range(2017, 2025)
                      for slot in range(1, (2 if y <= 2019 else 3) + 1)
                      for section in ("VARC", "DILR", "QA")}
    if len(files) != 63 or set(file_keys) != expected_files or len(file_keys) != len(set(file_keys)):
        errors.append("acquired PDF manifest does not contain exactly one file for each 2017-2024 candidate section")
    for f in files:
        if not isinstance(f.get("page_count"), int) or f["page_count"] < 3:
            errors.append(f"{f.get('filename')}: missing/implausible PDF page count")
        if not re.fullmatch(r"[0-9a-f]{64}", f.get("sha256", "")):
            errors.append(f"{f.get('filename')}: missing SHA-256 digest")
    for conflict in data.get("conflicts", []):
        if any(sid not in sources for sid in conflict.get("sources", [])):
            errors.append(f"{conflict.get('id')}: unknown source foreign key")
    for candidate in data.get("legacy_records", []):
        if any(sid not in sources for sid in candidate.get("source_ids", [])):
            errors.append(f"legacy candidate {candidate.get('year', candidate.get('year_range'))}: unknown source foreign key")

    status_path = HIST / "audit-status.json"
    if status_path.exists():
        status = json.loads(status_path.read_text(encoding="utf-8"))
        count_checks = {
            "registered_source_records": len(data["sources"]),
            "candidate_section_records": len(papers),
            "acquired_section_pdfs": len(files),
            "question_records": len(questions),
            "question_level_audited": sum(q.get("retrieval_state") == "question_audited" for q in questions),
            "independently_answer_verified": sum(q.get("answer_state") == "independently_verified" for q in questions),
            "source_key_seen_only": sum(q.get("answer_state") == "source_key_seen" for q in questions),
            "retrieved_unsolved": sum(q.get("answer_state") == "unchecked" for q in questions),
            "officially_key_corroborated": sum(q.get("official_key_state") == "corroborated" for q in questions),
            "complete_shared_dilr_sets": sum(s.get("reconstruction_state") == "complete" for s in data["sets"]),
            "source_conflicts": len(data.get("conflicts", [])),
        }
        for key, actual in count_checks.items():
            if status.get(key) != actual:
                errors.append(f"audit-status {key} {status.get(key)} != evidence-backed count {actual}")
        if status.get("complete_slot_papers_page_by_page_audited") != sum(bool(p.get("complete_paper")) for p in papers.values()):
            errors.append("audit-status complete paper count disagrees with paper census")
    else:
        errors.append("missing derived audit-status.json")

    return errors, warnings


def main():
    data = {
        "sources": read("source-registry.json")["sources"],
        "papers": read("paper-census.json")["papers"],
        "questions": read("question-corpus.json")["questions"],
        "sets": read("set-corpus.json")["sets"],
        "passages": read("passage-corpus.json")["passages"],
        "acquired_files": read("acquisition-manifest.json")["files"],
        "legacy_papers": read("legacy-papers.json")["papers"],
        "conflicts": read("source-conflicts.json")["conflicts"],
        "legacy_records": read("legacy-candidates.json")["records"],
    }
    errors, warnings = validate(data)
    for warning in warnings:
        print("WARN:", warning)
    for error in errors:
        print("ERROR:", error)
    print(f"source_records={len(data['sources'])} candidate_section_records={len(data['papers'])} acquired_section_pdfs={len(data['acquired_files'])}/63 question_records={len(data['questions'])} question_audited={sum(q['retrieval_state']=='question_audited' for q in data['questions'])} independently_verified={sum(q['answer_state']=='independently_verified' for q in data['questions'])} official_key_corroborated={sum(q['official_key_state']=='corroborated' for q in data['questions'])} shared_sets={len(data['sets'])} passages={len(data['passages'])} errors={len(errors)} structural_duplicate_warnings={len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

