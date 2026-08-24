"""Read-only CoinGecko adapter for crypto market research."""
from .http import get_json

BASE = "https://api.coingecko.com/api/v3"


def markets(ids: list[str], vs_currency: str = "usd") -> list[dict]:
    if not ids:
        return []
    joined = ",".join(ids)
    return get_json(f"{BASE}/coins/markets?vs_currency={vs_currency}&ids={joined}&sparkline=false")


def coin(id: str, vs_currency: str = "usd") -> dict:
    return get_json(f"{BASE}/simple/price?ids={id}&vs_currencies={vs_currency}&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true")


def trending() -> dict:
    return get_json(f"{BASE}/search/trending")
