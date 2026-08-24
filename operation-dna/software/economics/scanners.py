"""Domain-neutral scanners for business, investment, and trading candidates.

Scanners produce research candidates only. They never place trades, spend money,
or claim that a candidate is investable.
"""
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Candidate:
    name: str
    domain: str
    thesis: str
    evidence_score: float
    capital_required: float
    expected_upside: float
    downside: float
    reversible: bool = True
    time_to_test_days: int = 30
    source_ids: tuple[str, ...] = ()

    @property
    def risk_adjusted_efficiency(self) -> float:
        if self.capital_required <= 0:
            return 0.0
        risk_factor = max(0.0, 1.0 - min(1.0, self.downside))
        return self.expected_upside / self.capital_required * self.evidence_score * risk_factor


def scan(events: Iterable[dict], domain: str, keywords: Iterable[str]) -> list[Candidate]:
    terms = tuple(k.lower() for k in keywords)
    candidates = []
    for event in events:
        text = f"{event.get('title', '')} {event.get('summary', '')}".lower()
        hits = [term for term in terms if term in text]
        if not hits:
            continue
        candidates.append(Candidate(
            name=event.get('title', 'untitled'),
            domain=domain,
            thesis=f"Signal matched: {', '.join(hits)}",
            evidence_score=float(event.get('evidence_score', 0.0)),
            capital_required=float(event.get('capital_required', 0.0)),
            expected_upside=float(event.get('expected_upside', 0.0)),
            downside=float(event.get('downside', 0.5)),
            reversible=bool(event.get('reversible', True)),
            time_to_test_days=int(event.get('time_to_test_days', 30)),
            source_ids=tuple(event.get('source_ids', ())),
        ))
    return sorted(candidates, key=lambda c: c.risk_adjusted_efficiency, reverse=True)


BUSINESS_SIGNALS = ("customer", "demand", "contract", "backlog", "shortage", "pricing", "partnership", "funding")
INVESTMENT_SIGNALS = ("earnings", "guidance", "backlog", "contract", "insider", "buyback", "capacity", "valuation")
TRADING_SIGNALS = ("breakout", "momentum", "volatility", "volume", "liquidity", "funding", "open interest", "regime")


def scan_business(events):
    return scan(events, "business", BUSINESS_SIGNALS)


def scan_investments(events):
    return scan(events, "investment", INVESTMENT_SIGNALS)


def scan_trading(events):
    return scan(events, "trading", TRADING_SIGNALS)
