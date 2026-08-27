import tempfile
import unittest
from pathlib import Path

from operation_dna.software.runtime.build_memory import BuildMemory, BuildMemoryRecord
from operation_dna.software.runtime.repair_loop import analyze_failure, RepairLoop
from operation_dna.software.runtime.self_build_agent import BuildRequest


class RepairLoopTests(unittest.TestCase):
    def test_failure_analysis_categories(self):
        self.assertEqual(analyze_failure("syntax error near line 2").category, "syntax")
        self.assertEqual(analyze_failure("AssertionError expected 2 got 1").category, "test")

    def test_memory_persists_and_finds_repairs(self):
        with tempfile.TemporaryDirectory() as tmp:
            memory = BuildMemory(str(Path(tmp) / "memory.jsonl"))
            memory.record(BuildMemoryRecord("x", "goal", 1, True, True, "import failure", "fix import", True))
            self.assertEqual(memory.successful_repairs("import failure"), ["fix import"])
            self.assertEqual(memory.summary()["resolved"], 1)

    def test_repair_loop_can_use_repair_generator(self):
        class Factory:
            root = "."
        class Result:
            syntax_ok = True
            tests_ok = True
            reason = "ok"
        class Agent:
            generate = object()
            def build(self, request, promote=False, autonomy_level=0):
                return type("R", (), {"request": request, "build": Result(), "iteration": 1, "promoted": False, "notes": ()})()
        with tempfile.TemporaryDirectory() as tmp:
            loop = RepairLoop(Agent(), BuildMemory(str(Path(tmp) / "m.jsonl")))
            result = loop.run(BuildRequest("x", "goal"))
            self.assertTrue(result.build.tests_ok)


if __name__ == "__main__":
    unittest.main()
