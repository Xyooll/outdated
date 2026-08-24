"""Portable node manifest: configuration and schema, never secrets."""
from dataclasses import dataclass, asdict
import json
from pathlib import Path

@dataclass(frozen=True)
class NodeManifest:
    dna_version: str
    node_id: str
    region: str
    schema_version: str
    enabled_applications: list[str]

def write(path: str, manifest: NodeManifest) -> None:
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(asdict(manifest), indent=2, sort_keys=True), encoding="utf-8")
