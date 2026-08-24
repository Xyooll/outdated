"""Runtime configuration from environment variables; no secrets are committed."""
import os


class Config:
    alpaca_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret = os.getenv("ALPACA_API_SECRET")
    sec_user_agent = os.getenv("SEC_USER_AGENT")
    coingecko_api_key = os.getenv("COINGECKO_API_KEY")
    research_db = os.getenv("RESEARCH_DB", "data/operation_dna.db")


def missing_credentials() -> list[str]:
    """Return credentials required by currently configured integrations.

    SEC is the only required credential for the SEC adapter. Alpaca and CoinGecko
    credentials remain optional because those adapters may be unused or use public
    endpoints where applicable.
    """
    return ["SEC_USER_AGENT"] if not Config.sec_user_agent else []
