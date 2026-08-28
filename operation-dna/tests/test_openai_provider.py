import json
import unittest

from operation_dna.software.runtime.openai_provider import OpenAIProvider
from operation_dna.software.runtime.token_ledger import TokenLedger


class FakeResponse:
    content = b'{}'

    def raise_for_status(self):
        return None

    def json(self):
        return {
            "id": "resp_test",
            "output_text": json.dumps({
                "source": "def probe():\n    return 42\n",
                "tests": "import unittest\nfrom generated import probe\n\nclass T(unittest.TestCase):\n    def test_probe(self): self.assertEqual(probe(), 42)\n",
            }),
            "usage": {"input_tokens": 100, "output_tokens": 80},
        }


class FakeSession:
    def post(self, *args, **kwargs):
        return FakeResponse()


class OpenAIProviderTests(unittest.TestCase):
    def test_records_provider_reported_usage(self):
        ledger = TokenLedger("data/test_openai_tokens.jsonl")
        provider = OpenAIProvider(api_key="test-key", ledger=ledger, session=FakeSession())
        class Request:
            name = "probe"
            goal = "build probe"
            requirements = ()
        bundle = provider.generate_bundle(Request())
        self.assertEqual(bundle.usage.input_tokens, 100)
        self.assertEqual(bundle.usage.output_tokens, 80)
        self.assertTrue(bundle.usage.measured)
        self.assertEqual(ledger.summary()["total_tokens"], 180)


if __name__ == "__main__":
    unittest.main()
