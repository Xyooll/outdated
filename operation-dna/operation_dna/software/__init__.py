"""Compatibility package exposing the implementation in ``operation-dna/software``.

This keeps the repository's historical directory name while providing a valid
Python import path: ``operation_dna.software.<module>``.
"""
from pathlib import Path

_IMPL = Path(__file__).resolve().parents[2] / "software"
__path__.append(str(_IMPL))
