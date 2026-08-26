import unittest
from unittest.mock import Mock
from datetime import datetime, timezone

from software.integrations.alpaca_public_crypto import AlpacaPublicCryptoAdapter

class Quote:
    bid_price = 100.5
    ask_price = 101.0
    timestamp = datetime(2026, 8, 26, 15, 0, tzinfo=timezone.utc)

class AlpacaPublicCryptoTests(unittest.TestCase):
    def test_normalizes_quote_without_writes(self):
        client = Mock()
        client.get_crypto_latest_quote.return_value = {"BTC/USD": Quote()}
        adapter = AlpacaPublicCryptoAdapter(client)
        obs = adapter.latest_quote("BTC/USD")
        self.assertEqual(obs.symbol, "BTC/USD")
        self.assertEqual(obs.bid_price, 100.5)
        self.assertEqual(obs.ask_price, 101.0)
        self.assertFalse(obs.side_effects)
        client.get_crypto_latest_quote.assert_called_once()

    def test_rejects_invalid_symbol(self):
        adapter = AlpacaPublicCryptoAdapter(Mock())
        with self.assertRaises(ValueError):
            adapter.latest_quote("BTCUSD")

    def test_payload_is_serializable(self):
        client = Mock(); client.get_crypto_latest_quote.return_value = {"BTC/USD": Quote()}
        adapter = AlpacaPublicCryptoAdapter(client)
        payload = adapter.as_payload(adapter.latest_quote())
        self.assertFalse(payload["side_effects"])
        self.assertEqual(payload["event_type"], "crypto.market_quote")

if __name__ == "__main__":
    unittest.main()
