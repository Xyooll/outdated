"""Compatibility import shim for the repository's source-tree layout.

The implementation lives in ``operation-dna/software``. This shim lets
``from software...`` imports work when commands are launched from the repo
root, including unittest discovery on Windows.
"""
from pathlib import Path

_SOURCE = Path(__file__).resolve().parent.parent / "operation-dna" / "software"
__path__ = [str(_SOURCE)]
