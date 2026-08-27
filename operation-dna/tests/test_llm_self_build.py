import json
import tempfile
import unittest
from pathlib import Path

from operation_dna.software.runtime.llm_self_build import OpenAICompatibleGenerator, AutonomousSelfBuildAgent
from operation_dna.software.runtime.self_build_agent import BuildRequest
from operation_dna.software.runtime.software_factory import SoftwareFactory
from operation_dna.software.runtime.authority import HumanAuthority, AuthorityPolicy


class FakeResponse:
    def __init__(self, payload):
        self.payload = json.dumps(payload).encode()
    def read(self):
        return self.payload


class LLMBuildTests(unittest.TestCase):
    def test_generator_parses_bundle(self):
        def transport(request, timeout):
            return FakeResponse({"choices": [{"message": {"content": json.dumps({
                "source": "VALUE = 42\n",
                "tests": "import unittest\\n\\nclass T(unittest.TestCase):\\n def test_value(self): self.assertEqual(VALUE, 42)\\n"
            })}}]})
        # Use valid test importing the candidate by its staged module name.
        def transport2(request, timeout):
            return FakeResponse({"choices": [{"message": {"content": json.dumps({
                "source": "VALUE = 42\n",
                "tests": "import generated_signal\nimport unittest\nclass T(unittest.TestCase):\n def test_value(self): self.assertEqual(generated_signal.VALUE, 42)\n"
            })}}]})
        generator = OpenAICompatibleGenerator(api_key="x", model="test", transport=transport2)
        bundle = generator.generate_bundle(BuildRequest("generated_signal", "return 42"))
        self.assertIn("VALUE", bundle.source)
        self.assertIn("unittest", bundle.tests)

    def test_agent_builds_and_stops_before_unauthorized_promotion(self):
        def transport(request, timeout):
            return FakeResponse({"choices": [{"message": {"content": json.dumps({
                "source": "VALUE = 42\n",
                "tests": "import generated_signal\nimport unittest\nclass T(unittest.TestCase):\n def test_value(self): self.assertEqual(generated_signal.VALUE, 42)\n"
            })}}]})
        with tempfile.TemporaryDirectory() as td:
            factory = SoftwareFactory(str(Path(td) / "stage"), HumanAuthority(AuthorityPolicy()))
            agent = AutonomousSelfBuildAgent(factory, OpenAICompatibleGenerator(api_key="x", model="test", transport=transport))
            result = agent.build(BuildRequest("generated_signal", "return 42"), promote=True)
            self.assertTrue(result.build.syntax_ok)
            self.assertTrue(result.build.tests_ok)
            self.assertFalse(result.promoted)
            self.assertTrue(any("promotion blocked" in n for n in result.notes))

    def test_agent_can_promote_only_after_authority(self):
        def transport(request, timeout):
            return FakeResponse({"choices": [{"message": {"content": json.dumps({
                "source": "VALUE = 42\n",
                "tests": "import generated_signal\nimport unittest\nclass T(unittest.TestCase):\n def test_value(self): self.assertEqual(generated_signal.VALUE, 42)\n"
            })}}]})
        with tempfile.TemporaryDirectory() as td:
            authority = HumanAuthority(AuthorityPolicy(autonomy_level=0, max_capital=0.0))
            authority.approve()
            factory = SoftwareFactory(str(Path(td) / "stage"), authority)
            agent = AutonomousSelfBuildAgent(factory, OpenAICompatibleGenerator(api_key="x", model="test", transport=transport))
            result = agent.build(BuildRequest("generated_signal", "return 42", destination=str(Path(td) / "active")), promote=True)
            self.assertTrue(result.build.tests_ok)
            self.assertTrue(result.promoted)


if __name__ == "__main__":
    unittest.main()
