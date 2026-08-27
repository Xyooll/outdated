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
            # Empty test path exercises syntax-only validation for this minimal loop.
            agent = SelfBuildAgent(factory, generate, max_iterations=2)
            result = agent.build(BuildRequest("candidate", "build a callable"))
            self.assertTrue(result.build.syntax_ok)
            self.assertEqual(result.iteration, 2)
            self.assertFalse(result.promoted)
            self.assertEqual(len(calls), 2)

    def test_promotion_still_requires_authority(self):
        with tempfile.TemporaryDirectory() as td:
            factory = SoftwareFactory(td, HumanAuthority())
            agent = SelfBuildAgent(
                factory,
                lambda request, feedback: "def answer():\n    return 1\n",
            )
            result = agent.build(
                BuildRequest("candidate", "build a callable", destination=str(Path(td) / "out")),
                promote=True,
            )
            self.assertFalse(result.promoted)

    def test_authorized_promotion_works(self):
        with tempfile.TemporaryDirectory() as td:
            authority = HumanAuthority()
            authority.approve()
            factory = SoftwareFactory(td, authority)
            destination = str(Path(td) / "out")
            agent = SelfBuildAgent(
                factory,
                lambda request, feedback: "def answer():\n    return 1\n",
            )
            result = agent.build(
                BuildRequest("candidate", "build a callable", destination=destination),
                promote=True,
            )
            self.assertTrue(result.promoted)
            self.assertTrue((Path(destination) / "candidate.py").exists())


if __name__ == "__main__":
    unittest.main()
