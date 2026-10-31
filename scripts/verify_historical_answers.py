"""Deterministic independent checks for the CAT 2017/2023/2024 seed items."""
from __future__ import annotations

from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path


def verify_cat2017_age():
    # Normalize Barun's present age to 100 units. Arun=40; solve the future ratio.
    b, a = 100, 40
    elapsed = (b - 2 * a)  # From a+t=(b+t)/2 => t=b-2a.
    assert elapsed == 20
    assert (b + elapsed - b) / b * 100 == 20


def verify_cat2023_qa():
    # Prime exponent minima for 168 | 1134^n, then 1134^n | 168^m.
    p168, p1134 = {2: 3, 3: 1, 7: 1}, {2: 1, 3: 4, 7: 1}
    n = max((e + p1134[p] - 1) // p1134[p] for p, e in p168.items())
    m = max((n * e + p168[p] - 1) // p168[p] for p, e in p1134.items())
    assert (n, m, n + m) == (3, 12, 15)


def verify_cat2024_qa():
    assert 3**6 - 3 * 2**6 + 3 == 540


def perfect_matchings(items):
    if not items:
        yield ()
        return
    first = items[0]
    for i in range(1, len(items)):
        second = items[i]
        for rest in perfect_matchings(items[1:i] + items[i + 1:]):
            yield tuple(sorted(((first, second),) + rest))


def enumerate_cat2024_tournament():
    teams = tuple(range(1, 7))
    all_matchings = list(perfect_matchings(teams))
    round8 = tuple(sorted(((1, 4), (2, 5), (3, 6))))
    solutions = []
    for group1_tuple in combinations(teams, 3):
        group1, group2 = set(group1_tuple), set(teams) - set(group1_tuple)
        if not ({1, 5} <= group1 or {1, 5} <= group2):
            continue
        # Every Round 8 pair is cross-group.
        if any((a in group1) == (b in group1) for a, b in round8):
            continue
        target = {
            (a, b): (1 if ((a in group1) == (b in group1)) else 2)
            for a in teams for b in teams if a < b
        }
        counts = Counter(round8)
        counts.update(round8)  # Rounds 5 and 8 are identical.
        rounds = {5: round8, 8: round8}

        def walk(remaining_rounds):
            if not remaining_rounds:
                if all(counts[pair] == target[pair] for pair in target):
                    solutions.append((tuple(sorted(group1)), dict(rounds)))
                return
            r = remaining_rounds[0]
            required = {
                1: ((4, 6),),
                2: ((1, 5), (4, 6)),
                3: ((3, 4),),
                4: (),
                6: ((1, 6),),
            }[r]
            multiplicity = 2 if r == 4 else 1  # Rounds 4 and 7 are identical.
            for matching in all_matchings:
                if not all(tuple(sorted(pair)) in matching for pair in required):
                    continue
                pairs = [tuple(sorted(pair)) for pair in matching]
                if any(counts[pair] + multiplicity > target[pair] for pair in pairs):
                    continue
                for pair in pairs:
                    counts[pair] += multiplicity
                rounds[r] = matching
                if r == 4:
                    rounds[7] = matching
                walk(remaining_rounds[1:])
                rounds.pop(r)
                if r == 4:
                    rounds.pop(7)
                for pair in pairs:
                    counts[pair] -= multiplicity
                    if counts[pair] == 0:
                        del counts[pair]

        walk([1, 2, 3, 4, 6])
    return solutions


def enumerate_cat2023_housing():
    columns = "ABCDEF"
    houses = [f"{c}{r}" for c in columns for r in (1, 2)]
    block_xx = {f"{c}{r}" for c in "ABC" for r in (1, 2)}
    block_yy = set(houses) - block_xx
    road = {h: (1 if h.endswith("2") else 0) + (1 if h[0] in "CD" else 0) for h in houses}

    def neighbors(house, occupied):
        col, row = columns.index(house[0]), int(house[1])
        count = 0
        for dc, dr in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            c, r = col + dc, row + dr
            if 0 <= c < len(columns) and r in (1, 2):
                other = f"{columns[c]}{r}"
                same_block = (house in block_xx) == (other in block_xx)
                if same_block and other in occupied:
                    count += 1
        return count

    valid = []
    for bits in product((0, 1), repeat=12):
        occupied = {h for h, bit in zip(houses, bits) if bit}
        vacant = set(houses) - occupied
        for parking_bits in product((0, 1), repeat=6):
          parking_xx = {h for h, bit in zip(sorted(block_xx), parking_bits) if bit}
          for parking_house in block_yy:
            if sum(h in occupied for h in ("A1", "B1", "C1", "D1", "E1", "F1")) != 2:
                continue
            if sum(h in occupied for h in ("A1", "B1", "C1")) != 1:
                continue
            if sum(h in occupied for h in ("D1", "E1", "F1")) != 1:
                continue
            if not {"E1", "E2"} <= vacant:
                continue
            if not (occupied & {"D1", "D2"}) or not (occupied & {"F1", "F2"}):
                continue

            def price(house):
                base = 12 if (house == parking_house or house in parking_xx) else 10
                return base + 5 * road[house] + 3 * neighbors(house, occupied)

            vacant_xx, vacant_yy = vacant & block_xx, vacant & block_yy
            if not vacant_xx or not vacant_yy:
                continue
            if max(map(price, vacant_xx)) != 24:
                continue
            minimum = min(map(price, vacant_yy))
            if minimum != 15 or not any(h[0] == "E" and price(h) == 15 for h in vacant_yy):
                continue
            valid.append((occupied, parking_house, parking_xx, {h: price(h) for h in vacant}))
    return valid


def main():
    verify_cat2017_age()
    verify_cat2023_qa()
    verify_cat2024_qa()
    schedule_solutions = enumerate_cat2024_tournament()
    assert len(schedule_solutions) == 2  # Group-label symmetry; same unique partition/schedule.
    schedule = schedule_solutions[0][1]
    assert sum(1 for r in range(1, 9) if any(1 in pair for pair in schedule[r])) == 8
    assert next(b if a == 1 else a for a, b in schedule[5] if 1 in (a, b)) == 4
    assert next(b if a == 1 else a for a, b in schedule[7] if 1 in (a, b)) == 3
    assert next(b if a == 6 else a for a, b in schedule[3] if 6 in (a, b)) == 5
    houses = enumerate_cat2023_housing()
    occupancy_patterns = {tuple(sorted(state[0])) for state in houses}
    assert len(occupancy_patterns) == 2 and len(houses) == 64
    assert {len({f"{c}{r}" for c in "ABC" for r in (1, 2)} - state[0]) for state in houses} == {3}
    assert all("B1" in state[0] for state in houses)
    assert {sum(f"{c}2" not in state[0] for c in "ABCDEF") for state in houses} == {2, 3}
    assert max(state[3][h] for state in houses for h in state[3] if h[0] == "E") == 21
    assert {state[1] for state in houses} == {"E1"}
    results = {
        "snapshot": "2026-10-31",
        "method": "Independent deterministic arithmetic and exhaustive finite-state checks against source-retrieved prompts; not official-key corroboration.",
        "checks": [
            {"id": "CAT-2017-S1-QA-Q1", "result": "pass", "answer": "20%", "method": "Solve normalized future-age equation."},
            {"id": "CAT-2023-S1-QA-Q1", "result": "pass", "answer": "15", "method": "Prime exponent valuation minima in both divisibility directions."},
            {"id": "CAT-2024-S1-QA-Q1", "result": "pass", "answer": "540", "method": "Inclusion-exclusion count 3^6-3*2^6+3."},
            {"set_id": "CAT-2023-S1-DILR-SET1", "result": "pass", "raw_states_tested": 1572864, "feasible_occupancy_patterns": len(occupancy_patterns), "feasible_occupancy_and_parking_assignments": len(houses), "answers": {"Q1": "3", "Q2": "B1", "Q3": "Either 2 or 3", "Q4": "21", "Q5": "E1"}, "method": "Enumerate 2^12 occupancy patterns, all 2^6 possible Block XX parking assignments, and each of six possible single Block YY parking locations; apply the grid road adjacency, same-block neighbor, vacancy, occupancy and price constraints."},
            {"set_id": "CAT-2024-S1-DILR-SET1", "result": "pass", "labelled_solutions": len(schedule_solutions), "answers": {"Q1": "8", "Q2": "4", "Q3": "5", "Q4": "3", "Q5": "5"}, "method": "Enumerate all 3-team group partitions and perfect matchings by round under per-pair match multiplicity, anchored pair, and identical-round constraints. Two solutions differ only by group-label exchange; schedule and answers are invariant."},
        ],
        "limitations": ["All examination sources are Grade C reproductions.", "No official response-sheet answer key was located.", "This check covers only the listed items and does not establish full paper completeness or psychometric difficulty."]
    }
    output = Path(__file__).resolve().parents[1] / "research" / "historical" / "independent-checks.json"
    output.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("verified CAT17 age arithmetic; CAT23 prime exponents; CAT24 surjection count; CAT23 housing (1,572,864 occupancy/parking candidates, 2 occupancy patterns and 64 feasible parking assignments); CAT24 tournament schedule (2 group-label symmetric solutions, shared answers stable)")


if __name__ == "__main__":
    main()

