import unittest
from operation_dna.software.runtime.offline_self_build import OfflineGenerator
from operation_dna.software.runtime.self_build_agent import BuildRequest

class OfflineSelfBuildTests(unittest.TestCase):
    def test_generator_returns_complete_bundle(self):
        request = BuildRequest(name="candidate", goal="build a probe")
        bundle = OfflineGenerator().generate_bundle(request)
        self.assertIn("def run", bundle.source)
        self.assertIn("class GeneratedTests", bundle.tests)

    def test_generation_is_deterministic(self):
        request = BuildRequest(name="candidate", goal="build a probe")
        generator = OfflineGenerator()
        a = generator.generate_bundle(request)
        b = generator.generate_bundle(request)
        self.assertEqual(a, b)

if __name__ == "__main__":
    unittest.main()
