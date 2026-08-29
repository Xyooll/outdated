"""Model-facing view of the existing repository as a capability environment."""
from __future__ import annotations
from pathlib import Path

class CapabilityEnvironment:
    def __init__(self, root: str | Path):
        self.root = Path(root).resolve()

    def inspect(self, objective: str = "") -> str:
        rows = []
        for p in sorted(self.root.rglob("*")):
            if any(part in {".git", ".venv", "__pycache__", "build", "dist"} for part in p.parts):
                continue
            if p.is_file() and p.suffix in {".py", ".md", ".yaml", ".yml", ".json"}:
                try:
                    rows.append(str(p.relative_to(self.root)))
                except ValueError:
                    pass
            if len(rows) >= 250:
                break
        return "OBJECTIVE=" + objective + "\nEXISTING_RESOURCES:\n" + "\n".join(rows)
