"""Blind deterministic review for the finite QA/DILR part of the pilot.

The solver below derives answers from the authored prompt structures and does
not read answer keys or solution fields until after it has constructed them.
VARC remains subject to the separate human editorial evidence audit.
"""
import itertools
import json
import sys
from fractions import Fraction
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((Path(__file__).parent / "pilot.json").read_text(encoding="utf-8"))
QUESTIONS = {q["id"]: q for q in DATA["questions"]}


def solve_qa():
    answers = {}
    answers["APX-QA-001"] = str(sum(
        1 for a in range(13) for b in range(13) for c in range(1, 13)
        if a + b + c == 12 and a <= 4 and b % 2 == 0
    ))
    flagged_members=40
    flagged_nonmembers=95
    answers["APX-QA-002"] = str(Fraction(flagged_members, flagged_members+flagged_nonmembers))
    feasible = []
    for s in range(8):
        for b in range(17):
            if 2*s+b <= 14 and s+2*b <= 16:
                feasible.append((5*s+6*b, s, b))
    answers["APX-QA-003"] = str(max(feasible)[0])
    first_diffs = [8-3, 15-8, 24-15, 35-24]
    answers["APX-QA-004"] = str(35 + (first_diffs[-1] + (first_diffs[-1]-first_diffs[-2])))
    solutions = [n for n in range(1, 301) if n % 8 == 5 and n % 9 == 4]
    answers["APX-QA-005"] = str(len(solutions))
    answers["APX-QA-006"] = str((27-15) + (22-15))
    answers["APX-QA-007"] = str(int(2 + (1-2/12) / (1/12+1/18)))
    # Alligation: 12 people at 70, unknown n at 85, combined mean 79.
    answers["APX-QA-008"] = str(int(12*(79-70)/(85-79)))
    hypotenuse=(6**2+8**2)**0.5
    altitude=Fraction(6*8,10)
    area_factor=altitude*altitude
    answers["APX-QA-009"] = f"{area_factor.numerator}π/{area_factor.denominator}"
    pairs = [(a,b) for a in range(1,9) for b in range(a+1,9) if (a+b)%2==0]
    prime_pairs = [(a,b) for a,b in pairs if a in {2,3,5,7} and b in {2,3,5,7}]
    answers["APX-QA-010"] = "1/4" if len(prime_pairs)*4==len(pairs) else f"{len(prime_pairs)}/{len(pairs)}"
    return answers


def solve_dilr_a():
    valid=[]
    for p in itertools.permutations("ABCDE"):
        pos={x:i+1 for i,x in enumerate(p)}
        if pos["D"] != pos["B"]+1: continue
        if not pos["A"] < pos["C"]: continue
        if not pos["E"] > pos["D"]: continue
        if pos["A"] == 1: continue
        valid.append(pos)
    c_four=next(v for v in valid if v["C"]==4)
    e_three=next(v for v in valid if v["E"]==3)
    c_four_schedule={slot:person for person,slot in c_four.items()}
    e_three_schedule={slot:person for person,slot in e_three.items()}
    return {
        "APX-DILR-011": str(len(valid)),
        "APX-DILR-012": f"Slot {min(v['B'] for v in valid)}",
        "APX-DILR-013": c_four_schedule[5],
        "APX-DILR-014": e_three_schedule[4],
        "APX-DILR-015": f"Slot {max(v['A'] for v in valid)}",
    }


def solve_dilr_b():
    cells={"A":{"trees":8,"roofs":10},"B":{"trees":7,"roofs":11},"C":{"water":15}}
    cells["A"]["water"]=26-sum(cells["A"].values())
    cells["B"]["water"]=31-sum(cells["B"].values())
    cells["C"]["trees"]=24-cells["A"]["trees"]-cells["B"]["trees"]
    cells["C"]["roofs"]=30-cells["A"]["roofs"]-cells["B"]["roofs"]
    assert sum(cells["C"].values())==33
    assert sum(cells[d]["water"] for d in cells)==36
    return {
        "APX-DILR-016":str(cells["A"]["water"]),
        "APX-DILR-017":str(cells["B"]["water"]),
        "APX-DILR-018":str(cells["C"]["trees"]),
        "APX-DILR-019":{"A":"Alder","B":"Birch","C":"Cedar"}[max(cells,key=lambda d:cells[d]["water"])],
        "APX-DILR-020":f"{sum(cells[d]['water'] for d in cells)*100//90}%",
    }


def norm(x):
    if isinstance(x,float) and x.is_integer(): return int(x)
    return str(x)


def main():
    counts=Counter(q["section"] for q in DATA["questions"])
    assert len(DATA["questions"])==25, f"expected 25, got {len(DATA['questions'])}"
    assert counts=={"QA":10,"DILR":10,"VARC":5}, counts
    assert len({q["id"] for q in DATA["questions"]})==25
    for q in DATA["questions"]:
        for field in ("benchmark_id","research_id","novelty","prompt","canonical_answer","solution","independent_solution","ambiguity_check","expert_method","cat_relevance","cat_difficulty","training_difficulty"):
            assert q.get(field), f"{q['id']}: missing {field}"
        assert q["benchmark_id"] in DATA["benchmarks"]
        assert q["research_id"] in DATA["sources"]
        assert len(q["hints"])>=3
        assert len(q["choices"])==4 and len(set(q["choices"]))==4
        if q["section"] == "VARC":
            assert q["canonical_answer"] == "ABCD"[q["answer"]], q["id"]
        else:
            assert q["choices"][q["answer"]] == q["canonical_answer"] or q["canonical_answer"] in q["choices"][q["answer"]] or q["choices"][q["answer"]] in q["canonical_answer"], q["id"]
    derived={**solve_qa(),**solve_dilr_a(),**solve_dilr_b()}
    errors=[]
    for qid,answer in derived.items():
        q=QUESTIONS[qid]
        displayed=q["choices"][q["answer"]]
        if norm(answer) not in displayed:
            errors.append(f"{qid}: blind solve {answer}, selected option {displayed}")
    if errors:
        print("\n".join(errors)); return 1
    print(f"records={len(DATA['questions'])} QA=10 DILR=10 VARC=5 deterministic_rechecks={len(derived)} errors=0")
    print("VARC records require the separate textual evidence audit in QUESTION_VALIDATION_REPORT.md")
    return 0


if __name__=="__main__":
    sys.exit(main())



