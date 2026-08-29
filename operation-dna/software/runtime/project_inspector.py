"""Focused local codebase inspection for the Xyool agent."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import ast

DEFAULT_EXCLUDED = {".git", ".venv", "__pycache__", "build", "dist", ".generated_agent", ".generated_api", ".generated_evaluation"}

@dataclass(frozen=True)
class FileInfo:
    path: str
    lines: int
    python: bool
    symbols: tuple[str, ...]

class ProjectInspector:
    def __init__(self, root: str | Path, excluded: set[str] | None = None):
        self.root = Path(root).resolve()
        self.excluded = set(excluded or DEFAULT_EXCLUDED)

    def scan(self, max_files: int = 250) -> list[FileInfo]:
        results: list[FileInfo] = []
        for path in sorted(self.root.rglob("*")):
            if len(results) >= max_files or not path.is_file():
                continue
            relative = path.relative_to(self.root)
            if any(part in self.excluded for part in relative.parts):
                continue
            if relative.parts and relative.parts[0] == "data" and any(part in {"logs", "paper", "learning"} for part in relative.parts):
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            symbols: tuple[str, ...] = ()
            is_python = path.suffix == ".py"
            if is_python:
                try:
                    tree = ast.parse(text)
                    symbols = tuple(node.name for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)))
                except SyntaxError:
                    pass
            results.append(FileInfo(str(relative), len(text.splitlines()), is_python, symbols))
        return results

    def summary(self, max_files: int = 80) -> str:
        files = self.scan(max_files=max_files)
        python_files = sum(f.python for f in files)
        lines = [f"ROOT={self.root}", f"FILES={len(files)} PYTHON={python_files}"]
        for f in files:
            suffix = f" symbols={','.join(f.symbols[:12])}" if f.symbols else ""
            lines.append(f"{f.path} lines={f.lines}{suffix}")
        return "\n".join(lines)
