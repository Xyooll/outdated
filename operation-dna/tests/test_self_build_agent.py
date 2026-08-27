import tempfile
import unittest
from pathlib import Path

from operation_dna.software.runtime.self_build_agent import BuildRequest, SelfBuildAgent
from operation_dna.software.runtime.software_factory import SoftwareFactory
from operation_dna.software.runtime.authority import HumanAuthority


class SelfBuildAgentTests(unittest.TestCase):
    def test_agent_builds_candidate_after_feedback(self):
        calls = []

        def generate(request, feedback):
            calls.append(feedback)
            if not feedback:
                return "def broken(:\n    pass\n"
            return "def answer():\n    return 42\n"

        with tempfile.TemporaryDirectory() as td:
            factory = SoftwareFactory(td, HumanAuthority())
            agent = SelfBuildAgent(factory, generate, max_iterations=2)
            result = agent.build(BuildRequest("candidate", "build a callable"))
            self.assertTrue(result.build.syntax_ok)
            self.assertEqual(result.iteration, 2)
            self.assertFalse(result.promoted)
            self.assertEqual(len(calls), 2)

    def test_promotion_still_requires_authority(self):
        with tempfile.TemporaryDirectory() as td:
            factory = SoftwareFactory(td, HumanAuthority())
            candidate = factory.stage("candidate", "def answer():\n    return 1\n")
            test_path = Path(td) / "test_candidate.py"
            test_path.write_text(
                "import sys\n"
                f"sys.path.insert(0, {str(Path(td)).__repr__()})\n"
                "import candidate\n"
                "\n"
                "def test_answer():\n"
                "    assert candidate.answer() == 1\n",
                encoding="utf-8",
            )
            agent = SelfBuildAgent(
                factory,
                lambda request, feedback: candidate.read_text(),
                max_iterations=1,
            )
            result = agent.build(
                BuildRequest(
                    "candidate", "build a callable", test_file=str(test_path),
                    destination=str(Path(td) / "out"),
                ),
                promote=True,
            )
            self.assertTrue(result.build.tests_ok)
            self.assertFalse(result.promoted)

    def test_authorized_promotion_works(self):
        with tempfile.TemporaryDirectory() as td:
            authority = HumanAuthority()
            authority.approve()
            factory = SoftwareFactory(td, authority)
            test_path = Path(td) / "test_candidate.py"
            test_path.write_text(
                "import sys\n"
                f"sys.path.insert(0, {str(Path(td)).__repr__()})\n"
                "import candidate\n"
                "\n"
                "def test_answer():\n"
                "    assert candidate.answer() == 1\n",
                encoding="utf-8",
            )
            destination = str(Path(td) / "out")
            agent = SelfBuildAgent(
                factory,
                lambda request, feedback: "def answer():\n    return 1\n",
                max_iterations=1,
            )
            result = agent.build(
                BuildRequest(
                    "candidate", "build a callable", test_file=str(test_path),
                    destination=destination,
                ),
                promote=True,
            )
            self.assertTrue(result.build.tests_ok)
            self.assertTrue(result.promoted)
            self.assertTrue((Path(destination) / "candidate.py").exists())


if __name__ == "__main__":
    unittest.main()
