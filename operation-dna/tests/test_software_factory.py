import tempfile
import unittest
from pathlib import Path
from software.runtime.software_factory import SoftwareFactory

class SoftwareFactoryTests(unittest.TestCase):
    def test_invalid_source_cannot_promote(self):
        with tempfile.TemporaryDirectory() as tmp:
            factory = SoftwareFactory(tmp)
            path = factory.stage("bad_tool", "def broken(:\n")
            result = factory.validate(path)
            self.assertFalse(result.syntax_ok)
            with self.assertRaises(PermissionError):
                factory.promote(result, str(Path(tmp) / "prod"))

    def test_valid_source_requires_tests(self):
        with tempfile.TemporaryDirectory() as tmp:
            factory = SoftwareFactory(tmp)
            path = factory.stage("tool", "def add(a,b): return a+b\n")
            result = factory.validate(path)
            self.assertTrue(result.syntax_ok)
            self.assertFalse(result.tests_ok)

if __name__ == "__main__":
    unittest.main()
