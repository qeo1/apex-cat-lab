import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_historical_corpus.py"
spec = importlib.util.spec_from_file_location("historical_validator", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class HistoricalCorpusIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        hist = MODULE_PATH.parents[1] / "research" / "historical"
        import json
        cls.data = {
            "sources": json.loads((hist / "source-registry.json").read_text(encoding="utf-8"))["sources"],
            "papers": json.loads((hist / "paper-census.json").read_text(encoding="utf-8"))["papers"],
            "questions": json.loads((hist / "question-corpus.json").read_text(encoding="utf-8"))["questions"],
            "sets": json.loads((hist / "set-corpus.json").read_text(encoding="utf-8"))["sets"],
            "passages": json.loads((hist / "passage-corpus.json").read_text(encoding="utf-8"))["passages"],
            "acquired_files": json.loads((hist / "acquisition-manifest.json").read_text(encoding="utf-8"))["files"],
            "legacy_papers": json.loads((hist / "legacy-papers.json").read_text(encoding="utf-8"))["papers"],
            "conflicts": json.loads((hist / "source-conflicts.json").read_text(encoding="utf-8"))["conflicts"],
            "legacy_records": json.loads((hist / "legacy-candidates.json").read_text(encoding="utf-8"))["records"],
        }

    def test_seed_corpus_integrity(self):
        errors, _ = validator.validate(self.data)
        self.assertEqual([], errors)

    def test_duplicate_question_ids_are_rejected(self):
        data = {k: list(v) for k, v in self.data.items()}
        data["questions"].append(dict(data["questions"][0]))
        errors, _ = validator.validate(data)
        self.assertTrue(any("duplicate question id" in error for error in errors))

    def test_orphan_question_reference_is_rejected(self):
        data = {k: list(v) for k, v in self.data.items()}
        broken = dict(data["sets"][0])
        broken["question_ids"] = broken["question_ids"] + ["CAT-2023-S1-DILR-Q99"]
        data["sets"][0] = broken
        errors, _ = validator.validate(data)
        self.assertTrue(any("unknown question reference CAT-2023-S1-DILR-Q99" in error for error in errors))

    def test_unchecked_material_cannot_be_called_complete(self):
        data = {k: list(v) for k, v in self.data.items()}
        paper = dict(data["papers"][0])
        paper["complete_paper"] = True
        data["papers"][0] = paper
        errors, _ = validator.validate(data)
        self.assertTrue(any("complete-paper claim" in error for error in errors))

    def test_missing_section_pdf_is_rejected(self):
        data = {k: list(v) for k, v in self.data.items()}
        data["acquired_files"].pop()
        errors, _ = validator.validate(data)
        self.assertTrue(any("exactly one file for each 2017-2024" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

