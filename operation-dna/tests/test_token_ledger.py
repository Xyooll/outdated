import tempfile
import unittest
from pathlib import Path

from operation_dna.software.runtime.token_ledger import TokenLedger, TokenUsage
from operation_dna.software.runtime.metered_ai_provider import MeteredAIProvider
from operation_dna.software.runtime.ai_provider import LocalStubProvider


class TokenLedgerTests(unittest.TestCase):
    def test_estimate_is_deterministic(self):
        ledger = TokenLedger()
        self.assertEqual(ledger.estimate("12345678"), 2)
        self.assertEqual(ledger.estimate("12345678"), ledger.estimate("12345678"))

    def test_measured_usage_is_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger = TokenLedger(str(Path(tmp) / "tokens.jsonl"))
            event = ledger.record("api", TokenUsage(10, 7, True))
            self.assertEqual(event.total_tokens, 17)
            self.assertTrue(event.measured)
            self.assertEqual(ledger.summary()["total_tokens"], 17)

    def test_metered_provider_records_operations(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger = TokenLedger(str(Path(tmp) / "tokens.jsonl"))
            provider = MeteredAIProvider(LocalStubProvider(), ledger)
            provider.plan("build a probe")
            provider.repair(provider.plan("build a probe"), "syntax failure")
            self.assertGreaterEqual(ledger.summary()["events"], 3)
            self.assertIn("plan", ledger.operation_summary())
            self.assertIn("repair", ledger.operation_summary())


if __name__ == "__main__":
    unittest.main()
