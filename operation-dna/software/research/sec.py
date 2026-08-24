"""Read-only SEC company-facts adapter with accurate fact counts and stable revisions."""
import hashlib
import json
from .http import get_json
from .normalization import now_iso

BASE = "https://data.sec.gov/api/xbrl/companyfacts"


def cik10(cik: str | int) -> str:
    value = str(cik).strip()
    if not value.isdigit():
        raise ValueError("CIK must be numeric")
    return value.zfill(10)


def company_facts(cik: str | int, user_agent: str) -> dict:
    if not user_agent or "@" not in user_agent:
        raise ValueError("SEC user_agent should identify an operator/contact email")
    return get_json(
        f"{BASE}/CIK{cik10(cik)}.json",
        {"User-Agent": user_agent, "Accept-Encoding": "gzip, deflate"},
    )


def fact_observation_count(facts: dict) -> int:
    total = 0
    for namespace in facts.values():
        for concept in namespace.values():
            for units in concept.get("units", {}).values():
                total += len(units)
    return total


def company_event(cik: str | int, ticker: str, user_agent: str) -> dict:
    data = company_facts(cik, user_agent)
    entity = data.get("entityName", ticker)
    facts = data.get("facts", {})
    fact_count = fact_observation_count(facts)
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    revision = hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]
    fetched_at = now_iso()
    return {
        "source": "sec_companyfacts",
        "source_id": f"{cik10(cik)}:{revision}",
        "title": f"SEC company facts: {entity}",
        "summary": f"Structured XBRL facts available for {entity}; {fact_count} observations",
        "entity": ticker,
        "category": "financial_filings",
        "published_at": fetched_at,
        "url": f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik10(cik)}.json",
        "fact_count": fact_count,
    }
