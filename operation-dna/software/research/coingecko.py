"""Read-only CoinGecko adapter for crypto market research."""
from urllib.parse import urlencode
from .http import get_json

BASE = "https://api.coingecko.com/api/v3"


def markets(ids: list[str], vs_currency: str = "usd") -> list[dict]:
    if not ids:
        return []
    params = {"vs_currency": vs_currency, "ids": ",".join(ids), "sparkline": "false"}
    return get_json(f"{BASE}/coins/markets?{urlencode(params)}")


def coin(id: str, vs_currency: str = "usd") -> dict:
    params = {
        "ids": id,
        "vs_currencies": vs_currency,
        "include_market_cap": "true",
        "include_24hr_vol": "true",
        "include_24hr_change": "true",
    }
    return get_json(f"{BASE}/simple/price?{urlencode(params)}")


def trending() -> dict:
    return get_json(f"{BASE}/search/trending")
