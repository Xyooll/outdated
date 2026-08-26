import unittest

from software.integrations.alpaca_paper import AlpacaPaperAdapter, PAPER_BASE_URL


class FakeResponse:
    def __init__(self, payload):
        self.content = b"{}"
        self._payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self._payload


class FakeSession:
    def __init__(self):
        self.calls = []

    def request(self, method, url, **kwargs):
        self.calls.append((method, url, kwargs))
        if method == "GET":
            return FakeResponse({
                "id": "paper-id",
                "status": "ACTIVE",
                "equity": "1000",
                "buying_power": "2000",
                "trading_blocked": False,
            })
        return FakeResponse({"id": "order-id", "status": "accepted"})


class AlpacaPaperTests(unittest.TestCase):
    def test_refuses_non_paper_endpoint(self):
        with self.assertRaises(ValueError):
            AlpacaPaperAdapter("key", "secret", base_url="https://api.alpaca.markets")

    def test_account_preflight_is_read_only(self):
        session = FakeSession()
        adapter = AlpacaPaperAdapter("key", "secret", session=session)
        account = adapter.account()
        self.assertEqual(account.status, "ACTIVE")
        self.assertEqual(session.calls[0][0], "GET")
        self.assertTrue(session.calls[0][1].startswith(PAPER_BASE_URL))

    def test_market_order_is_explicitly_paper(self):
        session = FakeSession()
        adapter = AlpacaPaperAdapter("key", "secret", session=session)
        order = adapter.submit_market_order("AAPL", 1, "buy", "xyool-test")
        self.assertEqual(order["status"], "accepted")
        self.assertEqual(session.calls[0][0], "POST")
        self.assertEqual(session.calls[0][1], PAPER_BASE_URL + "/v2/orders")

    def test_invalid_order_is_rejected_before_network(self):
        session = FakeSession()
        adapter = AlpacaPaperAdapter("key", "secret", session=session)
        with self.assertRaises(ValueError):
            adapter.submit_market_order("AAPL", 0, "buy")
        self.assertEqual(session.calls, [])


if __name__ == "__main__":
    unittest.main()
