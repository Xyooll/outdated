"""Local codebase inspection for the Xyool agent."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import ast


@dataclass(frozen=True)
class FileInfo:
    path: str
    lines: int
    python: bool
    symbols: tuple[str, ...]


class ProjectInspector:
    def __init__(self, root: str | Path):
        self.root = Path(root).resolve()

    def scan(self, max_files: int = 250) -> list[FileInfo]:
        results: list[FileInfo] = []
        for path in sorted(self.root.rglob("*")):
            if len(results) >= max_files:
                break
            if not path.is_file() or any(part in {".git", ".venv", "__pycache__", ".generated_agent"} for part in path.parts):
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
                    symbols = tuple(
                        node.name for node in tree.body
                        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
                    )
                except SyntaxError:
                    symbols = ()
            results.append(FileInfo(str(path.relative_to(self.root)), len(text.splitlines()), is_python, symbols))
        return results

    def summary(self, max_files: int = 80) -> str:
        files = self.scan(max_files=max_files)
        python_files = sum(f.python for f in files)
        lines = [f"ROOT={self.root}", f"FILES={len(files)} PYTHON={python_files}"]
        for f in files:
            symbol_text = ",".join(f.symbols[:12])
            lines.append(f"{f.path} lines={f.lines}" + (f" symbols={symbol_text}" if symbol_text else ""))
        return "\n".join(lines)
