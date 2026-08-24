"""Environment-driven runtime configuration. Secrets never belong in DNA."""
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    node_id: str
    environment: str
    db_path: str
    audit_path: str

def load() -> Config:
    return Config(
        node_id=os.getenv("DNA_NODE_ID", "local"),
        environment=os.getenv("DNA_ENV", "development"),
        db_path=os.getenv("DNA_DB_PATH", "data/operation-dna.sqlite"),
        audit_path=os.getenv("DNA_AUDIT_PATH", "data/audit.jsonl"),
    )
