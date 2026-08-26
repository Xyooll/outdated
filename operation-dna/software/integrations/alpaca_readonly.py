"""Read-only Alpaca market-data adapter.

This adapter can only read market data. It contains no trading/account mutation
methods and therefore cannot submit, cancel, or modify orders.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from typing import Any

from .shadow import ShadowObservation


class AlpacaConfigurationError(RuntimeError):
    pass


@dataclass
class AlpacaReadOnlyProvider:
    symbol: str = "AAPL"
    feed: str = "iex"
    base_url: str = "https://data.alpaca.markets"
    timeout: float = 10.0
    name: str = "alpaca"

    def _credentials(self) -> tuple[str, str]:
        key = os.getenv("APCA_API_KEY_ID")
        secret = os.getenv("APCA_API_SECRET_KEY")
        if not key or not secret:
            raise AlpacaConfigurationError(
                "Set APCA_API_KEY_ID and APCA_API_SECRET_KEY before live observation."
            )
        return key, secret

    def observe(self) -> ShadowObservation:
        key, secret = self._credentials()
        params = urlencode({"symbols": self.symbol, "feed": self.feed})
        url = f"{self.base_url.rstrip('/')}/v2/stocks/trades/latest?{params}"
        request = Request(
            url,
            headers={
                "APCA-API-KEY-ID": key,
                "APCA-API-SECRET-KEY": secret,
                "Accept": "application/json",
            },
            method="GET",
        )
        with urlopen(request, timeout=self.timeout) as response:
            body: dict[str, Any] = json.loads(response.read().decode("utf-8"))

        trades = body.get("trades", {})
        trade = trades.get(self.symbol)
        if not trade:
            raise RuntimeError(f"Alpaca returned no latest trade for {self.symbol}")

        return ShadowObservation(
            provider=self.name,
            event_type="market.signal",
            payload={
                "symbol": self.symbol,
                "price": trade.get("p"),
                "size": trade.get("s"),
                "timestamp": trade.get("t"),
                "exchange": trade.get("x"),
                "feed": self.feed,
                "source": "alpaca.market_data",
            },
            side_effects=False,
        )
