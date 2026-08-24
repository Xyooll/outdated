"""Convert market API payloads into canonical research events."""
from .normalization import ResearchEvent, now_iso


def stock_bar_events(payload: dict, source: str = "alpaca") -> list[ResearchEvent]:
    events = []
    for symbol, bars in payload.get("bars", {}).items():
        for bar in bars:
            ts = bar.get("t", now_iso())
            events.append(ResearchEvent(
                source=source,
                source_id=f"{symbol}:{ts}",
                title=f"{symbol} market bar",
                summary=f"OHLCV {bar.get('o')} {bar.get('h')} {bar.get('l')} {bar.get('c')} volume {bar.get('v')}",
                published_at=ts,
                category="market_data",
                entity=symbol,
                evidence_score=1.0,
            ))
    return events


def crypto_market_events(payload: list[dict], source: str = "coingecko") -> list[ResearchEvent]:
    return [ResearchEvent(
        source=source,
        source_id=str(row.get("id", row.get("symbol", "unknown"))),
        title=f"Crypto market: {row.get('name', row.get('symbol', 'unknown'))}",
        summary=f"Price {row.get('current_price')} market cap {row.get('market_cap')} 24h volume {row.get('total_volume')}",
        category="crypto_market",
        entity=row.get("symbol", ""),
        evidence_score=0.9,
    ) for row in payload]
