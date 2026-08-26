"""Read-only Alpaca crypto market-data adapter.

Alpaca documents crypto market-data endpoints that can be used without
account trading credentials. This adapter intentionally exposes observation
only and converts the SDK result into a small canonical payload.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoLatestQuoteRequest

@dataclass(frozen=True)
class PublicCryptoObservation:
    provider: str
    event_type: str
    symbol: str
    bid_price: float | None
    ask_price: float | None
    timestamp: str | None
    side_effects: bool = False

class AlpacaPublicCryptoAdapter:
    name = "alpaca-public-crypto"
    side_effects = False

    def __init__(self, client: CryptoHistoricalDataClient | None = None):
        self.client = client or CryptoHistoricalDataClient()

    def latest_quote(self, symbol: str = "BTC/USD") -> PublicCryptoObservation:
        if not symbol or "/" not in symbol:
            raise ValueError("symbol must use the BASE/QUOTE form, e.g. BTC/USD")
        request = CryptoLatestQuoteRequest(symbol_or_symbols=symbol)
        data = self.client.get_crypto_latest_quote(request)
        quote = data.get(symbol)
        if quote is None:
            raise LookupError(f"no quote returned for {symbol}")
        return PublicCryptoObservation(
            provider=self.name,
            event_type="crypto.market_quote",
            symbol=symbol,
            bid_price=float(quote.bid_price) if quote.bid_price is not None else None,
            ask_price=float(quote.ask_price) if quote.ask_price is not None else None,
            timestamp=quote.timestamp.isoformat() if quote.timestamp else None,
        )

    def as_payload(self, observation: PublicCryptoObservation) -> dict[str, Any]:
        return {
            "provider": observation.provider,
            "event_type": observation.event_type,
            "symbol": observation.symbol,
            "bid_price": observation.bid_price,
            "ask_price": observation.ask_price,
            "timestamp": observation.timestamp,
            "side_effects": observation.side_effects,
        }
