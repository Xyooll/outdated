"""Runtime configuration from environment variables; no secrets are committed."""
import os


class Config:
    alpaca_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret = os.getenv("ALPACA_API_SECRET")
    sec_user_agent = os.getenv("SEC_USER_AGENT")
    coingecko_api_key = os.getenv("COINGECKO_API_KEY")
    research_db = os.getenv("RESEARCH_DB", "data/research.db")


def missing_credentials() -> list[str]:
    missing = []
    if not Config.sec_user_agent:
        missing.append("SEC_USER_AGENT")
    return missing
