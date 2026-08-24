"""Read-only Alpaca market-data adapter.

Credentials are read from the environment. This module intentionally exposes no
order-placement functions; market data feeds the research/backtest layers.
"""
import os
from .http import get_json

DATA_URL = "https://data.alpaca.markets"


def _headers() -> dict[str, str]:
    key = os.getenv("ALPACA_API_KEY")
    secret = os.getenv("ALPACA_API_SECRET")
    if not key or not secret:
        raise RuntimeError("ALPACA_API_KEY and ALPACA_API_SECRET are required")
    return {"APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": secret}


def stock_bars(symbol: str, start: str, end: str | None = None, timeframe: str = "1Day", feed: str = "iex") -> dict:
    params = f"symbols={symbol}&timeframe={timeframe}&start={start}&feed={feed}"
    if end:
        params += f"&end={end}"
    return get_json(f"{DATA_URL}/v2/stocks/bars?{params}", _headers())


def crypto_bars(symbol: str, start: str, end: str | None = None, timeframe: str = "1Day") -> dict:
    params = f"symbols={symbol}&timeframe={timeframe}&start={start}"
    if end:
        params += f"&end={end}"
    return get_json(f"{DATA_URL}/v1beta3/crypto/us/bars?{params}", _headers())


def latest_stock(symbol: str, feed: str = "iex") -> dict:
    return get_json(f"{DATA_URL}/v2/stocks/{symbol}/snapshot?feed={feed}", _headers())
