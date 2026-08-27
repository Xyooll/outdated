"""Offline self-build provider used before an LLM API is available.

It exercises the complete build contract with deterministic templates. When
an LLM provider is connected, it can be replaced without changing the agent.
"""
from __future__ import annotations
from .self_build_agent import BuildRequest
from .llm_self_build import GeneratedBundle

class OfflineGenerator:
    """Deterministic generator for integration testing of the self-builder."""
    def generate_bundle(self, request: BuildRequest, feedback: str = "") -> GeneratedBundle:
        source = f'''"""Generated capability: {request.goal}"""\n\ndef run(value):\n    return value\n'''
        tests = '''import unittest\nfrom candidate import run\n\nclass GeneratedTests(unittest.TestCase):\n    def test_identity(self):\n        self.assertEqual(run("probe"), "probe")\n\nif __name__ == "__main__":\n    unittest.main()\n'''
        return GeneratedBundle(source, tests)
