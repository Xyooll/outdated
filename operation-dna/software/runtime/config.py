"""Environment-driven runtime configuration. Secrets never belong in DNA."""
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    node_id: str
    environment: str
    db_path: str
    audit_path: str
    rss_timeout: int
    poll_interval_seconds: int
    log_level: str

def load() -> Config:
    return Config(
        node_id=os.getenv("DNA_NODE_ID", "local"),
        environment=os.getenv("DNA_ENV", "development"),
        db_path=os.getenv("DNA_DB_PATH", "data/operation-dna.sqlite"),
        audit_path=os.getenv("DNA_AUDIT_PATH", "data/audit.jsonl"),
        rss_timeout=int(os.getenv("DNA_RSS_TIMEOUT", "20")),
        poll_interval_seconds=int(os.getenv("DNA_POLL_INTERVAL", "900")),
        log_level=os.getenv("DNA_LOG_LEVEL", "INFO"),
    )
