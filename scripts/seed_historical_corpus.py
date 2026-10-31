"""Create the evidence-first CAT historical corpus seed from reviewed sources.

The committed corpus stores bibliographic metadata and concise structural
fingerprints, not copied CAT question text. The 2IIM ZIP remains in ignored
work/; this script records its file hashes if that acquisition is present.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HIST = ROOT / "research" / "historical"
PYQ = ROOT / "research" / "pyq"
TODAY = date.today().isoformat()

SOURCES = [
    {"id": "2IIM-ARCHIVE", "url": "https://online.2iim.com/CAT-question-paper/", "source_class": "institutional_secondary_archive", "evidence_grade": "C", "independence_group": "2iim", "claims": "CAT 2017-2025 slot and section question collections; 2IIM describes them as actual questions with solutions.", "limitations": "Provider reproduction, not official response-sheet artifacts; individual paper completeness and answer keys are not officially corroborated."},
    {"id": "2IIM-PDF-ARCHIVE", "url": "https://online.2iim.com/CAT-question-paper-pdf/", "source_class": "institutional_secondary_pdf_archive", "evidence_grade": "C", "independence_group": "2iim", "claims": "Download archive advertised as CAT 2017-2024 question papers with answers.", "limitations": "Downloaded files have promotional covers/navigation and scanned question pages; all question/page mappings and image-dependent details still require item-level inspection."},
    {"id": "2IIM-PDF-ZIP", "url": "https://online.2iim.com/CAT-question-paper-pdf/CAT%20PYQ%202017-24.zip", "source_class": "institutional_secondary_pdf_archive_artifact", "evidence_grade": "C", "independence_group": "2iim", "claims": "Direct downloaded ZIP artifact containing 63 CAT 2017-2024 year/slot/section PDFs; the per-file hash and metadata are recorded in acquisition-manifest.json.", "limitations": "Secondary reproductions, not official response sheets. File-level page and image completeness still pending."},
    {"id": "GS23-S1", "url": "https://www.gradscale.in/pyqs/cat/2023/1/view/", "source_class": "secondary_question_transcription", "evidence_grade": "C", "independence_group": "gradscale", "claims": "CAT 2023 Slot 1 displayed as 24 VARC, 20 DILR and 22 QA; actual question text, diagrams and answer explanations opened.", "limitations": "VARC passage transcriptions include ellipses; no official response sheet. Exam set/question locators need cross-source normalization."},
    {"id": "GS24-S1", "url": "https://www.gradscale.in/pyqs/cat/2024/1/view/", "source_class": "secondary_question_transcription", "evidence_grade": "C", "independence_group": "gradscale", "claims": "CAT 2024 Slot 1 displayed as 24 VARC, 22 DILR and 22 QA; actual question text, set constraints, answer and solution displayed.", "limitations": "VARC passage transcriptions include ellipses; no official response sheet. Set/order locators differ from the 2IIM set labels and require item-level normalization."},
    {"id": "GS25-S1", "url": "https://www.gradscale.in/pyqs/cat/2025/1/view/", "source_class": "secondary_question_transcription", "evidence_grade": "C", "independence_group": "gradscale", "claims": "CAT 2025 Slot 1 question-level source for existing audited records.", "limitations": "Some passage text/DI material is abbreviated or image based; no official response sheet."},
    {"id": "GS25-S2", "url": "https://www.gradscale.in/pyqs/cat/2025/2/view/", "source_class": "secondary_question_transcription", "evidence_grade": "C", "independence_group": "gradscale", "claims": "CAT 2025 Slot 2 question-level source for existing audited records.", "limitations": "Some passage text/DI material is abbreviated or image based; no official response sheet."},
    {"id": "GS25-S3", "url": "https://www.gradscale.in/pyqs/cat/2025/3/view/", "source_class": "secondary_question_transcription", "evidence_grade": "C", "independence_group": "gradscale", "claims": "CAT 2025 Slot 3 question-level source for existing audited records.", "limitations": "Some passage text/DI material is abbreviated or image based; no official response sheet."},
    {"id": "CAT-HIST-INDEX", "url": "https://www.thecatexam.com/pyp/cat", "source_class": "secondary_historical_archive_index", "evidence_grade": "C", "independence_group": "thecatexam", "claims": "Opened index lists recent slot papers, CAT 1991-2008 and CAT 2016; identifies two 2003 entries (paper and retake).", "limitations": "Index-level discovery only; each historical item and its authenticity/retrieval state must be checked."},
    {"id": "CAT-HIST-1991", "url": "https://www.thecatexam.com/pyp/cat/cat-1991", "source_class": "secondary_historical_question_transcription", "evidence_grade": "C", "independence_group": "thecatexam", "claims": "Question page says it contains 180 CAT 1991 items in three sections; actual VARC-labelled Q1 and subsequent item prompts were visible in the opened page.", "limitations": "No response-sheet source; archive's retroactive section labels are not normalized to original section names; controls/answers not independently checked; complete page audit not performed."},
    {"id": "PYQ-04", "url": "https://indianexpress.com/article/education/cat-2025-exam-analysis-slot-wise-difficulty-level-section-varc-dilr-answers-expert-students-review-iim-kozhikode-10394020/lite/", "source_class": "secondary_news_analysis", "evidence_grade": "C", "independence_group": "indian-express", "claims": "CAT 2025 post-exam analysis quoting coaching sources; has an internal total-count discrepancy (66 in lead, 68 from 24/22/22 table).", "limitations": "Secondary account, not a question paper or official key."},
    {"id": "PYQ-07", "url": "https://www.imsindia.com/cat-2025-slot-1-analysis/", "source_class": "secondary_coaching_analysis", "evidence_grade": "C", "independence_group": "ims", "claims": "IMS reports 68 CAT 2025 Slot 1 questions (24/22/22).", "limitations": "Secondary analysis; existing ledger notes internal topic-count prose/table discrepancy; not an official response sheet."},
    {"id": "CAT-OLD-PAPERS", "url": "https://www.previousyearpapers.in/CAT/", "source_class": "secondary_historical_archive_index", "evidence_grade": "C", "independence_group": "previousyearpapers", "claims": "Search result advertises CAT 1991 and CAT 1992 paper files.", "limitations": "Index was not opened/downloaded in this pass; individual files and provenance unverified."},
    {"id": "CATKING-1993", "url": "https://catking.in/wp-content/uploads/2020/09/CAT-1993-Question-Paper-with-Solution-1.pdf", "source_class": "secondary_historical_pdf_reproduction", "evidence_grade": "C", "independence_group": "catking", "claims": "Search result identifies a CAT 1993 paper with solutions.", "limitations": "PDF not downloaded or examined in this pass; key and exact completeness unverified."},
    {"id": "CATKING-2000", "url": "https://catking.in/wp-content/uploads/2020/09/CAT-2000-Question-Paper-with-Solution-1.pdf", "source_class": "secondary_historical_pdf_reproduction", "evidence_grade": "C", "independence_group": "catking", "claims": "Search result identifies a CAT 2000 paper with solutions.", "limitations": "PDF not downloaded or examined in this pass; key and exact completeness unverified."},
    {"id": "2IIM-2000-08-ACCESS", "url": "https://online.2iim.com/2iim-marathon/", "source_class": "provider_access_statement", "evidence_grade": "C", "independence_group": "2iim", "claims": "2IIM says CAT 2000-2008 papers are available inside its online course.", "limitations": "Authenticated course not accessed; no restricted material sought."},
    {"id": "CATKING-1991", "url": "https://cetking.com/wp-content/uploads/2016/09/CAT-1991-_Sol.pdf", "source_class": "secondary_historical_pdf_reproduction", "evidence_grade": "C", "independence_group": "cetking", "claims": "A CAT 1991 solved-paper URL was discovered in search during earlier source reconnaissance.", "limitations": "Not downloaded or examined in this pass; authenticity, completeness and answer reliability unknown."},
]


def paper_id(year: int, slot: int, section: str) -> str:
    return f"CAT-{year}-S{slot}-{section}"


def source_for(year: int, slot: int) -> str:
    if year == 2025:
        return f"GS25-S{slot}"
    if year == 2023 and slot == 1:
        return "GS23-S1"
    if year == 2024 and slot == 1:
        return "GS24-S1"
    return "2IIM-PDF-ZIP"


def question_record(year: int, slot: int, section: str, qnum: int, fingerprint: str,
                    answer: str, *, set_id: str | None = None, passage_id: str | None = None,
                    fmt: str = "unknown", topic: str | None = None,
                    source_id: str | None = None, verification: str = "") -> dict:
    src = source_id or source_for(year, slot)
    source_url = next(row["url"] for row in SOURCES if row["id"] == src)
    return {
        "id": f"CAT-{year}-S{slot}-{section}-Q{qnum}",
        "paper_id": paper_id(year, slot, section),
        "legacy_id": None,
        "year": year, "slot": slot, "section": section, "question_number": qnum,
        "set_id": set_id, "passage_id": passage_id,
        "source_ids": [src], "source_urls": [source_url],
        "retrieved_on": TODAY, "authenticity_grade": "C", "retrieval_state": "question_audited",
        "format": fmt, "topic": topic, "subtopic": None,
        "reasoning_fingerprint": fingerprint,
        "core_insight": None, "trap_architecture": None,
        "source_answer": answer, "independent_answer": answer,
        "answer_state": "independently_verified", "official_key_state": "not_checked",
        "difficulty": "unrated",
        "fingerprint_key": f"{year}-{slot}-{section}-{qnum}",
        "rights_status": "metadata_and_structural_summary_only",
        "evidence_note": verification or "Question and published answer opened; independently checked against the stated prompt. Secondary source; official key not checked."
    }


def build() -> None:
    HIST.mkdir(parents=True, exist_ok=True)
    (HIST / "source-registry.json").write_text(json.dumps({"snapshot": TODAY, "sources": SOURCES}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    question_rows: list[dict] = []
    old = json.loads((PYQ / "cat-2025-question-audit.json").read_text(encoding="utf-8"))
    for rec in old["questions"]:
        m = re.search(r"\bQ(\d+)\b", rec["locator"])
        if not m:
            raise ValueError(f"Cannot normalize old locator: {rec['id']}")
        qnum = int(m.group(1))
        set_id = None
        passage_id = None
        if rec["section"] == "DILR":
            set_match = re.search(r"Set\s*(\d+)", rec["locator"], re.I)
            set_id = f"CAT-{rec['year']}-S{rec['slot']}-DILR-SET{set_match.group(1)}" if set_match else None
        if rec["section"] == "VARC":
            passage_id = f"CAT-{rec['year']}-S{rec['slot']}-VARC-P1"
        question_rows.append({
            "id": f"CAT-{rec['year']}-S{rec['slot']}-{rec['section']}-Q{qnum}",
            "paper_id": paper_id(rec["year"], rec["slot"], rec["section"]),
            "legacy_id": rec["id"], "year": rec["year"], "slot": rec["slot"], "section": rec["section"],
            "question_number": qnum, "set_id": set_id, "passage_id": passage_id,
            "source_ids": [f"GS25-S{rec['slot']}"], "source_urls": [rec["source"]],
            "retrieved_on": TODAY, "authenticity_grade": rec["grade"], "retrieval_state": "question_audited",
            "format": "unknown", "topic": None, "subtopic": None,
            "reasoning_fingerprint": rec["fingerprint"], "core_insight": rec["verification"],
            "trap_architecture": rec["conflict"], "source_answer": rec["published_answer"],
            "independent_answer": rec["independent_answer"], "answer_state": "independently_verified",
            "official_key_state": "not_checked", "difficulty": "unrated",
            "fingerprint_key": f"2025-{rec['slot']}-{rec['section']}-{qnum}",
            "rights_status": "metadata_and_structural_summary_only",
            "evidence_note": f"Migrated from existing audited record {rec['id']}; source locator retained in legacy_id and fingerprint notes. Official CAT response-sheet key remains unchecked."
        })

    set23 = "CAT-2023-S1-DILR-SET1"
    passage23 = "CAT-2023-S1-VARC-P1"
    set24 = "CAT-2024-S1-DILR-SET1"
    passage24 = "CAT-2024-S1-VARC-P1"
    additions = [
        question_record(2017, 1, "QA", 1, "Relate a present ratio to an equal future-age ratio; eliminate the common offset by expressing elapsed years as a fraction of the older person's present age.", "20%", fmt="TITA", topic="Ratio and age", source_id="2IIM-PDF-ZIP", verification="The CAT 2017 Slot 1 quantitative PDF (CAT-2017-Slot-1-quants-2IIM-With-Video-Solutions.pdf), page 3, was visually opened. If Arun=.4B now, then .4B+t=.5(B+t), so t=.2B; Barun's increase is 20%. The source's clickable answer tab was not independently opened."),
        question_record(2023, 1, "VARC", 1, "Passage-scope check: distinguish the described South-South Indian Ocean network from an unsupported North-South connection.", "A", passage_id=passage23, fmt="MCQ", topic="RC inference", source_id="GS23-S1", verification="The passage names East Africa, Arab coasts and South/East Asia and calls the connections South-South; option A asserts a North-South link absent from the text."),
        question_record(2023, 1, "QA", 1, "Prime-exponent divisibility in both directions: minimize one power, then satisfy a second componentwise exponent bound.", "15", fmt="MCQ", topic="Number theory", source_id="GS23-S1", verification="168=2^3·3·7 and 1134=2·3^4·7. The least n is 3; 168^m contains 3^(4n)=3^12 only when m≥12, so m+n=15."),
        question_record(2024, 1, "VARC", 1, "Cross-system inference: identify a shared limitation (creativity is not guaranteed) without transferring a one-sided property (guild entry restrictions) to both systems.", "A", passage_id=passage24, fmt="MCQ", topic="RC comparison", source_id="GS24-S1", verification="The visible passage contrasts mass production's efficiency/consistency with guild hierarchy that may suppress innovation; A is the only shared outcome among the displayed options. The key rests on visible excerpts, not omitted passage wording."),
        question_record(2024, 1, "QA", 1, "Count surjections from a six-element domain onto three labelled values by inclusion-exclusion.", "540", fmt="MCQ", topic="Combinatorics", source_id="GS24-S1", verification="Inclusion-exclusion gives 3^6−3·2^6+3·1^6=729−192+3=540; source key agrees. This is an independent direct count."),
    ]
    additions[0]["source_answer"] = None
    for year, passage, source_id, details in [
        (2023, passage23, "GS23-S1", [
            (2, "Relationship-matching: identify which pair attributes a property to the wrong literary category.", "B", "Odd-pair inference"),
            (3, "Weaken-except: test which counterfactual does not weaken the stated contrast between mainstream fiction and Indian Ocean novels.", "D", "Argument evaluation"),
            (4, "Except question: eliminate claims supported by the passage's remapping thesis and select the inconsistent one.", "C", "Argument scope"),
        ]),
        (2024, passage24, "GS24-S1", [
            (2, "NOT-inconsistent inference: retain the option supported by the author's qualification about organization and creativity.", "B", "Qualified inference"),
            (3, "Locate the stated mechanism behind the author's concern about employment scale; separate it from an open question.", "B", "Causal/evidence selection"),
            (4, "Except question: separate the stated recent cause from general or earlier appeals of craftsmanship.", "A", "Temporal scope"),
        ]),
    ]:
        for qn, fp, answer, topic in details:
            row = question_record(year, 1, "VARC", qn, fp, answer, passage_id=passage, fmt="MCQ", topic=topic, source_id=source_id,
                                  verification="Question, options and secondary published key/explanation were visible in the transcription; this item has not received an independent answer check.")
            row["retrieval_state"] = "question_retrieved"
            row["independent_answer"] = None
            row["answer_state"] = "source_key_seen"
            additions.append(row)
    a23 = [
        (1, "Constraint propagation from a price extremum fixes one block's occupancy; boundary conditions leave two cases in the neighboring block.", "3", "TITA", "Case analysis plus price constraints fixes three vacant houses in Block XX."),
        (2, "Use an invariant across the two feasible occupancy branches to identify a house occupied in every model.", "B1", "MCQ", "Both feasible branches retain B1 as occupied; alternatives fail or are not entailed."),
        (3, "Evaluate an aggregate over all feasible occupancy branches rather than over a single completion.", "Either 2 or 3", "MCQ", "Given the two occupancy branches and independent D2/F2 choice, row-2 vacancy count takes exactly 2 or 3."),
        (4, "Optimize a local price expression using the maximum feasible neighbor count under shared occupancy constraints.", "21", "TITA", "E2 is vacant; its base price is 10, one road side contributes 5, and at most two same-block occupied neighbors contribute 6, totaling 21."),
        (5, "Infer a unique parking-space location by combining a minimum quoted price with a single-space condition.", "E1", "MCQ", "The minimum-price Column-E house is E1; its 15-lakh decomposition requires the 12 base and one occupied neighbor. The set's only parking place is therefore E1."),
    ]
    for qn, fp, ans, fmt, proof in a23:
        additions.append(question_record(2023, 1, "DILR", qn, fp, ans, set_id=set23, fmt=fmt, topic="Constraint-satisfaction caselet", source_id="GS23-S1", verification=proof + " Independent exhaustive check enumerated 1,572,864 occupancy/parking candidates while allowing arbitrary Block XX parking; two occupancy patterns and 64 feasible occupancy/parking assignments remain, with all five answers invariant."))
    a24 = [
        (1, "Derive rounds per team from the two within-group opponents and three cross-group opponents played twice.", "8", "TITA", "Each team has 2·1+3·2=8 matches, one per round."),
        (2, "Read a downstream fixture from the uniquely reconstructed schedule; it depends on group membership and repeated-round constraints.", "4", "TITA", "The reconstructed schedule has Team 1 vs Team 4 in Round 5."),
        (3, "Classify group membership by reconstructing the two three-team partitions from match frequencies and anchors.", "5", "MCQ", "The groups are {4,2,3} and {6,1,5}; Team 5 is the listed exception."),
        (4, "Apply an identical-round constraint to infer a team's opponent in a later round.", "3", "TITA", "Round 7 equals Round 4, where Team 1 plays Team 3."),
        (5, "Use the within-group/cross-group schedule to resolve an unlisted opponent from the completed round table.", "5", "TITA", "In Round 3 the listed fixtures are 3–4, 1–2, 5–6, so Team 6 plays Team 5."),
    ]
    for qn, fp, ans, fmt, proof in a24:
        additions.append(question_record(2024, 1, "DILR", qn, fp, ans, set_id=set24, fmt=fmt, topic="Tournament scheduling", source_id="GS24-S1", verification=proof + " Independent finite search across group partitions and all six non-duplicate rounds found two solutions differing only by group labels; all five answers are invariant."))
    question_rows.extend(additions)
    legacy_question = {
        "id": "CAT-1991-PAPER-VARC-Q1", "paper_id": "CAT-1991-PAPER", "legacy_id": None,
        "year": 1991, "slot": None, "section": "VARC", "question_number": 1,
        "set_id": None, "passage_id": None, "source_ids": ["CAT-HIST-1991"],
        "source_urls": ["https://www.thecatexam.com/pyp/cat/cat-1991"], "retrieved_on": TODAY,
        "authenticity_grade": "C", "retrieval_state": "question_retrieved", "format": "MCQ",
        "topic": "Sentence correction", "subtopic": "Subject-verb agreement and complement structure",
        "reasoning_fingerprint": "Choose the grammatically best sentence from near-parallel alternatives; determine agreement from the head of a partitive subject while checking predicate-complement wording.",
        "core_insight": None, "trap_architecture": "Potential ambiguity between a plural predicative complement and a singular one may admit more than one standard-English reading; source key and editorial validity are unchecked.",
        "source_answer": None, "independent_answer": None, "answer_state": "unchecked",
        "official_key_state": "not_found", "difficulty": "unrated", "fingerprint_key": "1991-paper-VARC-1",
        "rights_status": "metadata_and_structural_summary_only",
        "evidence_note": "Actual question and four options were visible on the CAT 1991 archive page. No wording copied here. No answer control opened; do not count as audited or answer-verified. The archive's VARC label is retained as its own taxonomy, not asserted as the exam's historical section name."
    }
    question_rows.append(legacy_question)
    question_rows.sort(key=lambda q: (q["year"], q["slot"], {"VARC": 0, "DILR": 1, "QA": 2}[q["section"]], q["question_number"]))
    (HIST / "question-corpus.json").write_text(json.dumps({"snapshot": TODAY, "copyright_policy": "No CAT question wording or full passages are redistributed here; records contain provenance and concise structural descriptions.", "questions": question_rows}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    sections = ["VARC", "DILR", "QA"]
    papers = []
    for year in range(2017, 2026):
        slots = range(1, 3) if year <= 2019 else range(1, 4)
        for slot in slots:
            for section in sections:
                pid = paper_id(year, slot, section)
                source_id = source_for(year, slot)
                items = [q for q in question_rows if q["paper_id"] == pid]
                if year <= 2024:
                    state = "section_pdf_retrieved_not_fully_audited"
                    retrieval_note = "Section PDF downloaded from the 2IIM 2017-2024 ZIP; sample question pages show actual question statements. Complete page-by-page content and media check pending."
                else:
                    state = "secondary_transcription_partially_audited"
                    retrieval_note = "GradeScale question-level page located; only listed items were individually audited. Do not treat the archive page's full-paper label as a completed audit."
                if year in (2023, 2024) and slot == 1:
                    state = "section_pdf_and_web_transcription_partially_reviewed"
                    retrieval_note = "2IIM section PDF acquired; GradeScale slot page and listed questions opened. VARC passages contain ellipses and source-specific set locators vary."
                papers.append({
                    "id": pid, "year": year, "slot": slot, "section": section,
                    "source_ids": sorted(set([source_id] + [s for q in items for s in q["source_ids"]])),
                    "acquisition_state": state,
                    "candidate_slot_model": "2017-2019 two slots; 2020-2025 three slots, based on available archive indexes; not official census",
                    "section_question_count_claim": 34 if year == 2017 and slot == 1 and section == "QA" else (24 if section == "VARC" and year >= 2021 else (20 if section == "DILR" and year == 2023 else (22 if section in ("DILR", "QA") and year >= 2021 else None))),
                    "question_indexed_count": len(items), "question_audited_count": sum(q["retrieval_state"] == "question_audited" for q in items),
                    "complete_paper": False, "official_corroboration_count": 0,
                    "media_review": "partial" if (year in (2023, 2024) and slot == 1) else "pending",
                    "retrieval_note": retrieval_note
                })
    (HIST / "paper-census.json").write_text(json.dumps({"snapshot": TODAY, "scope_note": "Candidate slot-section inventory for 2017-2025; slot model inferred from secondary archives and must be cross-checked against official records.", "papers": papers}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    sets = [
        {"id": "CAT-2023-S1-DILR-SET1", "paper_id": paper_id(2023, 1, "DILR"), "question_ids": [f"CAT-2023-S1-DILR-Q{i}" for i in range(1, 6)], "source_ids": ["GS23-S1", "2IIM-PDF-ARCHIVE"], "source_urls": ["https://www.gradscale.in/pyqs/cat/2023/1/view/", "https://online.2iim.com/CAT-question-paper-pdf/"], "reconstruction_state": "complete", "completeness": "full shared prompt, essential diagram asset and all five question prompts opened", "independent_set_enumeration": "1,572,864 occupancy/parking candidates enumerated allowing arbitrary Block XX parking; two occupancy patterns and 64 feasible parking-labelled assignments; all five answers invariant", "fingerprint": "Grid occupancy with inter-block roads, local neighbor counts, prices and existential/extremal conditions; branches propagate into dependent questions."},
        {"id": "CAT-2024-S1-DILR-SET1", "paper_id": paper_id(2024, 1, "DILR"), "question_ids": [f"CAT-2024-S1-DILR-Q{i}" for i in range(1, 6)], "source_ids": ["GS24-S1", "2IIM-PDF-ARCHIVE"], "source_urls": ["https://www.gradscale.in/pyqs/cat/2024/1/view/", "https://online.2iim.com/CAT-question-paper-pdf/"], "reconstruction_state": "complete", "completeness": "shared tournament prompt, conditions, fixture reconstruction and all five question prompts opened", "independent_set_enumeration": "finite schedule search found two solutions differing only by exchange of group labels; schedule and all five answers invariant", "fingerprint": "Partition six teams into equal groups; derive cross/within group match multiplicity; reconstruct round-wise perfect matchings under duplicated-round and anchored-pair constraints."},
        {"id": "CAT-2025-S1-DILR-SET5", "paper_id": paper_id(2025, 1, "DILR"), "question_ids": [f"CAT-2025-S1-DILR-Q{i}" for i in range(18, 23)], "source_ids": ["GS25-S1"], "source_urls": ["https://www.gradscale.in/pyqs/cat/2025/1/view/"], "reconstruction_state": "complete", "completeness": "complete shared set among existing audited records", "independent_set_enumeration": "all five recorded items independently checked in existing audit", "fingerprint": "Train route flow and occupancy equations with capacity, divisibility, fractional boarding and downstream aggregation."},
        {"id": "CAT-2025-S2-DILR-SET1", "paper_id": paper_id(2025, 2, "DILR"), "question_ids": [f"CAT-2025-S2-DILR-Q{i}" for i in range(1, 5)], "source_ids": ["GS25-S2"], "source_urls": ["https://www.gradscale.in/pyqs/cat/2025/2/view/"], "reconstruction_state": "complete", "completeness": "complete shared set among existing audited records", "independent_set_enumeration": "all four recorded items independently checked in existing audit", "fingerprint": "Ping outcomes induce a partial order across ball/hoop thresholds; count forced versus possible comparisons and incidences."},
    ]
    passages = []
    for pid, paper, qids, src, url in [
        (passage23, paper_id(2023, 1, "VARC"), [f"CAT-2023-S1-VARC-Q{i}" for i in range(1, 5)], "GS23-S1", "https://www.gradscale.in/pyqs/cat/2023/1/view/"),
        (passage24, paper_id(2024, 1, "VARC"), [f"CAT-2024-S1-VARC-Q{i}" for i in range(1, 5)], "GS24-S1", "https://www.gradscale.in/pyqs/cat/2024/1/view/"),
        ("CAT-2025-S2-VARC-P1", paper_id(2025, 2, "VARC"), [f"CAT-2025-S2-VARC-Q{i}" for i in range(1, 5)], "GS25-S2", "https://www.gradscale.in/pyqs/cat/2025/2/view/"),
        ("CAT-2025-S3-VARC-P1", paper_id(2025, 3, "VARC"), [f"CAT-2025-S3-VARC-Q{i}" for i in range(1, 5)], "GS25-S3", "https://www.gradscale.in/pyqs/cat/2025/3/view/"),
    ]:
        passages.append({"id": pid, "paper_id": paper, "question_ids": qids, "source_ids": [src], "source_url": url, "completeness": "partial; source text contains omissions/ellipses; not a full passage transcript", "rights_status": "not redistributed"})
    (HIST / "set-corpus.json").write_text(json.dumps({"sets": sets}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (HIST / "passage-corpus.json").write_text(json.dumps({"passages": passages}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    conflicts = [
        {"id": "CONFLICT-2IIM-GS-2024-SET-ORDER", "kind": "set_locator", "year": 2024, "slot": 1, "section": "DILR", "sources": ["2IIM-PDF-ARCHIVE", "GS24-S1"], "description": "The visible 2IIM 2024 Slot 1 DILR PDF begins with a DILR set numbered Set 7 about allocating stars, while GradeScale calls the tournament schedule Set 1. These are source-local set labels, not yet normalized; direct question correspondence remains to be mapped."},
        {"id": "CONFLICT-2IIM-WRONG-FOOTER-2024-VARC", "kind": "document-integrity", "year": 2024, "slot": 1, "section": "VARC", "sources": ["2IIM-PDF-ARCHIVE"], "description": "The sampled CAT 2024 Slot 1 VARC PDF page header identifies CAT 2024, but the bottom footer labels the displayed question as an Original CAT 2021 Question Paper. Treat as a possible reused/incorrect footer and inspect the full file before asserting paper authenticity/completeness."},
        {"id": "CONFLICT-2IIM-AGLASEM-SLOT-COVERAGE", "kind": "coverage", "sources": ["2IIM-ARCHIVE"], "description": "Existing research records AglaSem's index as listing fewer CAT 2020 and 2022 slots than 2IIM. The slot model is a secondary archive candidate model, not a reconciled official census."},
        {"id": "CONFLICT-2025-LOCATORS", "kind": "question_locator", "year": 2025, "sources": ["GS25-S1", "GS25-S3"], "description": "Existing CAT 2025 source records retain cross-provider question-number disagreements, including QA numbering; preserve source-local locators in legacy_id rather than force a canonical official number."},
        {"id": "CONFLICT-2025-EXPLANATION", "kind": "published-solution-error", "year": 2025, "sources": ["GS25-S1", "GS25-S2"], "description": "Existing audit records a Slot 1 QA explanation calling 628 the minimum where 268 is smaller and valid; the final factor-count answer coincides. It also records a reversed inequality in the Slot 2 DILR explanation; the answer is supported after correcting the relation. These are source-solution defects, not proven answer-key disagreements."},
        {"id": "CONFLICT-2025-66-68", "kind": "reported-question-count", "year": 2025, "sources": ["PYQ-04", "PYQ-07"], "description": "The Indian Express CAT 2025 analysis lead says 66 total questions while its sectional table and IMS analysis say 68 (24/22/22). No official response sheet has resolved this reporting discrepancy."},
        {"id": "CONFLICT-LEGACY-PDF-URLS", "kind": "retrieval-failure", "sources": ["CATKING-1991", "CATKING-1993", "CATKING-2000"], "description": "The three explored CETKing/CATKing direct PDF URLs returned HTML pages (including 404 pages) rather than PDF bytes. They remain search-result leads only; TheCATExam provides a separate accessible CAT 1991 page."},
        {"id": "CONFLICT-1991-Q1-EDITORIAL", "kind": "item-ambiguity-lead", "year": 1991, "sources": ["CAT-HIST-1991"], "description": "The first VARC-labelled sentence-correction item appears to offer both a plural predicative complement and a singular complement after a singular subject. This may be conventional grammar nuance or a genuine multiple-answer ambiguity; no answer key or editorial resolution was inspected, so it is not approved as a solved item."},
    ]
    (HIST / "source-conflicts.json").write_text(json.dumps({"conflicts": conflicts}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    legacy = {
        "snapshot": TODAY,
        "scope": "Leads for CAT years before 2017. No slot structure is inferred for paper-era examinations.",
        "records": [
            {"year": 1991, "source_ids": ["CAT-HIST-INDEX", "CAT-OLD-PAPERS", "CATKING-1991"], "state": "candidate_index_and_pdf_url_located_not_retrieved", "note": "Identifiable solved-paper URL discovered; file not downloaded or visually audited."},
            {"year": 1992, "source_ids": ["CAT-OLD-PAPERS"], "state": "index_lead_only", "note": "Archive search result lists a 1992 paper; no file examined."},
            {"year": 1993, "source_ids": ["CATKING-1993"], "state": "pdf_url_located_not_retrieved", "note": "CATKing and CETKing results both advertise CAT 1993 reproductions; not yet compared for independence or content."},
            {"year": 1997, "source_ids": ["CAT-HIST-INDEX"], "state": "candidate_download_requires_identity_check", "note": "A result URL named CAT_2000.pdf has extracted text headed CAT 1997 and says 165 questions; filename/content mismatch makes this an unresolved lead."},
            {"year": 2000, "source_ids": ["CATKING-2000", "2IIM-2000-08-ACCESS"], "state": "pdf_url_located_not_retrieved_and_course_access_claim", "note": "Public CATKing URL discovered; 2IIM says 2000-2008 papers are inside a course. No download or restricted access performed."},
            {"year": 2001, "source_ids": ["2IIM-2000-08-ACCESS"], "state": "course_access_claim_only", "note": "Included within provider's 2000-2008 access statement; no paper itself examined."},
            {"year": 2002, "source_ids": ["2IIM-2000-08-ACCESS"], "state": "course_access_claim_only", "note": "Included within provider's 2000-2008 access statement; no paper itself examined."},
            {"year": 2003, "source_ids": ["2IIM-2000-08-ACCESS"], "state": "course_access_claim_only", "note": "Public secondary accounts describe a leaked paper/cancellation context; no exam paper reproduced or examined in this pass."},
            {"year": 2004, "source_ids": ["2IIM-2000-08-ACCESS"], "state": "course_access_claim_only", "note": "Public secondary accounts describe a retest; specific paper source not yet located."},
            {"year": 2005, "source_ids": ["2IIM-2000-08-ACCESS"], "state": "course_access_claim_only", "note": "Included within provider's 2000-2008 access statement; no paper itself examined."},
            {"year": 2006, "source_ids": ["2IIM-2000-08-ACCESS"], "state": "course_access_claim_only", "note": "Included within provider's 2000-2008 access statement; no paper itself examined."},
            {"year": 2007, "source_ids": ["2IIM-2000-08-ACCESS"], "state": "course_access_claim_only", "note": "Included within provider's 2000-2008 access statement; no paper itself examined."},
            {"year": 2008, "source_ids": ["2IIM-2000-08-ACCESS"], "state": "course_access_claim_only", "note": "Included within provider's 2000-2008 access statement; no paper itself examined."},
            {"year_range": "2009-2016", "source_ids": ["CAT-HIST-INDEX"], "state": "unresolved_archive_gap", "note": "Secondary discussion suggests public reproductions may be scarcer after the move to computer-based tests; this is a research lead, not a verified explanation or proof of unavailability."}
        ]
    }
    legacy_records = []
    for year in list(range(1991, 2009)) + [2016]:
        source_ids = ["CAT-HIST-INDEX"]
        state = "index_lead_only"
        note = "TheCATExam year index advertises an annual paper; the document and question count have not been audited. No slot is inferred."
        if year == 1991:
            source_ids.append("CAT-HIST-1991")
            state = "question_transcription_opened_partial_audit_pending"
            note = "TheCATExam claims 180 questions across three archive-labelled sections; Q1 and its options were opened, but answer/key and whole-paper completeness are unchecked."
        elif year in (1993, 2000):
            state = "question_page_located_not_individually_examined"
            note = "TheCATExam page title identifies a full paper with solutions; line-level retrieval timed out, so no question is counted as examined. Separate CATKing PDF URLs returned HTML 404 rather than a PDF."
        elif year == 2003:
            note = "The index lists two entries (a paper and retake); both need separate event identity and authenticity review."
        legacy_records.append({"year": year, "slot": None, "source_ids": source_ids, "state": state, "note": note})
    legacy_records += [
        {"year_range": "2009-2015", "source_ids": ["CAT-HIST-INDEX"], "state": "unresolved_archive_gap", "note": "No year entries for this range appear in the opened TheCATExam index. Other sources remain to be searched; absence from this index does not prove unavailability."},
        {"year": 1990, "slot": None, "source_ids": ["CAT-OLD-PAPERS"], "state": "index_lead_only", "note": "PreviousYearPapers lists CAT 1990; no paper downloaded or examined."}
    ]
    legacy = {"snapshot": TODAY, "scope": "Pre-slot-era annual archive entries; source listings do not establish official completeness. Null slot means the archive presents one annual paper; no exam slot is inferred.", "records": legacy_records}
    (HIST / "legacy-candidates.json").write_text(json.dumps(legacy, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    legacy_papers = [{"id": "CAT-1991-PAPER", "year": 1991, "slot": None, "source_ids": ["CAT-HIST-1991"], "source_url": "https://www.thecatexam.com/pyp/cat/cat-1991", "archive_claimed_question_count": 180, "archive_section_labels": ["VARC", "DILR", "QA"], "state": "secondary_question_page_opened; whole-paper completeness not audited", "question_item_records": 1, "note": "Source calls this a complete paper and displays items in all archive-labelled sections. The labels/count require independent cross-source review. Only Q1 is represented as retrieved but unsolved."}]
    (HIST / "legacy-papers.json").write_text(json.dumps({"papers": legacy_papers}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    archive_dir = ROOT / "work" / "historical" / "2iim-2017-2024" / "CAT PYQ 2017-24"
    files = []
    if archive_dir.exists():
        pdfinfo = shutil.which("pdfinfo")
        if not pdfinfo:
            bundled = Path(r"C:\Users\d work\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdfinfo.exe")
            pdfinfo = str(bundled) if bundled.exists() else None
        for path in sorted(archive_dir.glob("*.pdf")):
            h = hashlib.sha256()
            with path.open("rb") as f:
                for block in iter(lambda: f.read(1024 * 1024), b""):
                    h.update(block)
            name = path.stem.lower()
            ym = re.search(r"20(1[7-9]|2[0-4])", name)
            sm = re.search(r"slot[- ]?(\d+)", name)
            sec = "VARC" if ("varc" in name or "verbal" in name) else ("DILR" if "dilr" in name else ("QA" if ("quant" in name or "quants" in name) else None))
            page_count, title = None, None
            if pdfinfo:
                meta = subprocess.run([pdfinfo, str(path)], capture_output=True, text=True, check=False).stdout
                pm, tm = re.search(r"^Pages:\s+(\d+)", meta, re.M), re.search(r"^Title:\s*(.+)$", meta, re.M)
                page_count = int(pm.group(1)) if pm else None
                title = tm.group(1).strip() if tm else None
            files.append({"filename": path.name, "year": int("20" + ym.group(1)) if ym else None, "slot": int(sm.group(1)) if sm else None, "section": sec, "title_metadata": title, "page_count": page_count, "bytes": path.stat().st_size, "sha256": h.hexdigest(), "local_copy_committed": False, "scope_review": "not page-by-page checked"})
    (HIST / "acquisition-manifest.json").write_text(json.dumps({
        "source_id": "2IIM-PDF-ZIP", "archive_url": "https://online.2iim.com/CAT-question-paper-pdf/CAT%20PYQ%202017-24.zip",
        "retrieved_on": TODAY, "archive_bytes": 78565250 if files else None,
        "local_stage_directory": "work/historical/2iim-2017-2024/CAT PYQ 2017-24" if files else None,
        "pdf_count": len(files), "files": files,
        "spot_checks": [
            {"filename_match": "CAT-2017-Slot-1-quants-2IIM-With-Video-Solutions.pdf", "pages": 74, "page_reviewed": 1, "finding": "Promotional cover; page 2 gives 34-question navigation; page 3 contains an actual CAT-style question prompt. Remaining pages not exhaustively checked."},
            {"filename_match": "CAT 2024 DILR Slot-1.pdf", "pages": 29, "page_reviewed": 3, "finding": "Question page includes a data chart and shared set conditions; page labels a local set number. No complete page-by-page audit."},
            {"filename_match": "CAT 2024 VARC Slot-1.pdf", "pages": 34, "page_reviewed": 3, "finding": "Question text is present; footer says Original CAT 2021 Question Paper despite CAT 2024 header, logged as document integrity conflict."}
        ],
        "interpretation": "63 section PDFs are retrieved. They contain question pages, not merely the two navigation pages; acquisition is not equivalent to complete-paper verification or item-level audit. The PDFs are secondary reproductions, Grade C."
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    verified = sum(q["answer_state"] == "independently_verified" for q in question_rows)
    audited = sum(q["retrieval_state"] == "question_audited" for q in question_rows)
    by_section = {}
    for section in sections:
        subset = [q for q in question_rows if q["section"] == section]
        by_section[section] = {
            "question_records": len(subset),
            "structurally_audited": sum(q["retrieval_state"] == "question_audited" for q in subset),
            "independently_answer_verified": sum(q["answer_state"] == "independently_verified" for q in subset),
            "secondary_key_seen_only": sum(q["answer_state"] == "source_key_seen" for q in subset),
            "retrieved_unsolved": sum(q["answer_state"] == "unchecked" for q in subset),
        }
    (HIST / "audit-status.json").write_text(json.dumps({
        "snapshot": TODAY,
        "scope": "Evidence-backed question records only; candidate paper rows and archive index claims are not counted as audited questions.",
        "discovered_candidate_years": list(range(2017, 2026)),
        "retrieved_legacy_question_page_years": [1991],
        "candidate_slot_count": 24,
        "candidate_section_records": len(papers),
        "registered_source_records": len(SOURCES),
        "acquired_section_pdfs": len(files),
        "complete_slot_papers_page_by_page_audited": 0,
        "question_records": len(question_rows),
        "question_level_audited": audited,
        "independently_answer_verified": verified,
        "source_key_seen_only": sum(q["answer_state"] == "source_key_seen" for q in question_rows),
        "retrieved_unsolved": sum(q["answer_state"] == "unchecked" for q in question_rows),
        "officially_key_corroborated": sum(q["official_key_state"] == "corroborated" for q in question_rows),
        "complete_shared_dilr_sets": sum(s.get("reconstruction_state") == "complete" for s in sets),
        "complete_varc_passages": sum(not ("partial" in p["completeness"] or "ellipsis" in p["completeness"]) for p in passages),
        "source_conflicts": len(conflicts),
        "sections": by_section,
        "unresolved_historical_span": "Pre-slot archive leads cover 1990-2008 and 2016; 2009-2015 remains an unresolved discovery gap, not a confirmed absence."
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"sources={len(SOURCES)} candidate_section_records={len(papers)} questions={len(question_rows)} sets={len(sets)} passages={len(passages)} archived_pdfs={len(files)}")


if __name__ == "__main__":
    build()

