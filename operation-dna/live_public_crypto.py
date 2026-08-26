"""One-shot real read-only Alpaca crypto observation for Xyool.

No trading/account endpoint is used and no order capability is exposed.
"""
from software.integrations.alpaca_public_crypto import AlpacaPublicCryptoAdapter

def main() -> int:
    adapter = AlpacaPublicCryptoAdapter()
    observation = adapter.latest_quote("BTC/USD")
    print("LIVE provider=alpaca-public-crypto event=crypto.market_quote side_effects=False")
    print(adapter.as_payload(observation))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
