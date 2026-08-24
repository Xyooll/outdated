"""SEC company-facts adapter.

Uses the public data.sec.gov endpoint. It is read-only and never submits filings.
The SEC requires a descriptive User-Agent for automated access.
"""
from .http import get_json

BASE = "https://data.sec.gov/api/xbrl/companyfacts"


def cik10(cik: str | int) -> str:
    return str(cik).zfill(10)


def company_facts(cik: str | int, user_agent: str) -> dict:
    if not user_agent or "@" not in user_agent:
        raise ValueError("SEC user_agent should identify an operator/contact email")
    return get_json(f"{BASE}/CIK{cik10(cik)}.json", {"User-Agent": user_agent, "Accept-Encoding": "gzip, deflate"})


def company_event(cik: str | int, ticker: str, user_agent: str) -> dict:
    data = company_facts(cik, user_agent)
    entity = data.get("entityName", ticker)
    facts = data.get("facts", {})
    return {
        "source": "sec_companyfacts",
        "source_id": cik10(cik),
        "title": f"SEC company facts: {entity}",
        "summary": f"Structured XBRL facts available for {entity}",
        "entity": ticker,
        "category": "financial_filings",
        "url": f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik10(cik)}.json",
        "fact_count": sum(len(namespace) for namespace in facts.values()),
    }
