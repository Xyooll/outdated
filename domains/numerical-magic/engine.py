"""Deterministic utilities for the Xyool numerical-magic domain.

This module computes arithmetic and carrier mappings only. Symbolic meanings are
loaded from ROOT-REGISTRY.json and returned with provenance; the engine does not
claim that symbolic meanings or magical effects are empirically causal.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

REGISTRY_PATH = Path(__file__).with_name("ROOT-REGISTRY.json")


@dataclass(frozen=True)
class NumberAnalysis:
    surface: str
    digits: list[int]
    ordered_path: list[str]
    sum: int
    reduction_chain: list[int]
    final_root: int
    final_root_name: str
    repetition: dict[str, int]
    zero_count: int


@dataclass(frozen=True)
class LetterValue:
    letter: str
    ordinal: int
    ordinal_reduction_chain: list[int]
    root: int
    root_name: str
    glyph_name: str | None


@dataclass(frozen=True)
class TextAnalysis:
    surface: str
    letters: list[str]
    values: list[int]
    ordinals: list[int]
    letter_values: list[LetterValue]
    glyph_path: list[str]
    root_sequence_surface: str
    numeric_analysis: NumberAnalysis
    ordinal_sum: int
    ordinal_sum_reduction_chain: list[int]


def load_registry(path: Path = REGISTRY_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _digits(value: int | str) -> list[int]:
    text = str(value).strip()
    if text.startswith("+"):
        text = text[1:]
    if not text or not text.isdigit():
        raise ValueError("expression must contain decimal digits only")
    return [int(ch) for ch in text]


def digital_root(value: int) -> int:
    if value < 0:
        raise ValueError("value must be non-negative")
    if value == 0:
        return 0
    return 1 + ((value - 1) % 9)


def reduction_chain(value: int | str) -> list[int]:
    """Return the preserved reduction chain, including the surface integer.

    Examples:
        7777 -> [7777, 28, 10, 1]
        38   -> [38, 11, 2]
    """
    digits = _digits(value)
    current = int("".join(str(d) for d in digits))
    chain = [current]
    while current >= 10:
        current = sum(int(ch) for ch in str(current))
        chain.append(current)
    return chain


def root_family(root: int, count: int = 12) -> list[int]:
    if root not in range(1, 10):
        raise ValueError("root must be 1 through 9")
    if count < 1:
        raise ValueError("count must be positive")
    return [root + 9 * k for k in range(count)]


def _root_name(root: int, registry: dict) -> str:
    if root == 0:
        return registry["zero"]["name"]
    return registry["roots"][str(root)]["name"]


def analyze_number(value: int | str, registry: dict | None = None) -> NumberAnalysis:
    registry = registry or load_registry()
    text = str(value).strip()
    digits = _digits(text)
    chain = reduction_chain(text)
    root = chain[-1]

    ordered_path: list[str] = []
    for digit in digits:
        ordered_path.append(_root_name(digit, registry))

    counts: dict[str, int] = {}
    for digit in digits:
        key = str(digit)
        counts[key] = counts.get(key, 0) + 1
    repetition = {k: v for k, v in counts.items() if v > 1}

    return NumberAnalysis(
        surface=text,
        digits=digits,
        ordered_path=ordered_path,
        sum=sum(digits),
        reduction_chain=chain,
        final_root=root,
        final_root_name=_root_name(root, registry),
        repetition=repetition,
        zero_count=digits.count(0),
    )


def alphabet_ordinal(letter: str, registry: dict | None = None) -> int:
    """Return A=1 ... Z=26 from the canonical letter protocol."""
    registry = registry or load_registry()
    ch = letter.strip().upper()
    if len(ch) != 1 or not ch.isalpha():
        raise ValueError("letter must be one alphabetic character")
    mapping = registry["letter_numeric_protocol"]["ordinal_mapping"]
    if ch not in mapping:
        raise ValueError(f"unsupported letter: {ch}")
    return int(mapping[ch])


def letter_value(letter: str, registry: dict | None = None) -> LetterValue:
    """Return the canonical dual numerical identity for one letter.

    Every letter preserves both its alphabet ordinal and the digital-root family
    generated from that ordinal. Example: W = 23 -> 5.
    """
    registry = registry or load_registry()
    ch = letter.strip().upper()
    ordinal = alphabet_ordinal(ch, registry)
    chain = reduction_chain(ordinal)
    root = chain[-1]
    glyph = registry.get("glyph_extensions", {}).get(ch)
    return LetterValue(
        letter=ch,
        ordinal=ordinal,
        ordinal_reduction_chain=chain,
        root=root,
        root_name=_root_name(root, registry),
        glyph_name=glyph["name"] if glyph else None,
    )


def letters_for_root(root: int, registry: dict | None = None) -> list[LetterValue]:
    """Return all letters eligible to encode a root digit.

    Root eligibility is strict. Ordinal pathways are returned so a higher layer
    can choose among eligible letters according to declared symbolic intent.
    """
    if root not in range(1, 10):
        raise ValueError("root must be 1 through 9")
    registry = registry or load_registry()
    mapping = registry["letter_numeric_protocol"]["ordinal_mapping"]
    values = [letter_value(ch, registry) for ch in mapping]
    return [value for value in values if value.root == root]


def letter_options_for_number(value: int | str, registry: dict | None = None) -> list[list[LetterValue]]:
    """Return eligible letter choices for every digit of a numerical ring.

    Zero has no canonical A-Z carrier. A ring containing zero requires a
    separately declared zero-symbol profile and therefore fails closed here.
    """
    registry = registry or load_registry()
    digits = _digits(value)
    if 0 in digits:
        raise ValueError("zero has no canonical A-Z carrier; declare a zero-symbol profile")
    return [letters_for_root(digit, registry) for digit in digits]


def pythagorean_values(text: str, registry: dict | None = None) -> tuple[list[str], list[int]]:
    """Return letters and their root-family values.

    This remains backward-compatible with the original Pythagorean carrier API.
    The root values are now explicitly derived from alphabet ordinals.
    """
    registry = registry or load_registry()
    mapping = registry["carrier_profiles"]["pythagorean"]["mapping"]
    letters = [ch for ch in text.upper() if ch.isalpha()]
    unsupported = [ch for ch in letters if ch not in mapping]
    if unsupported:
        raise ValueError(f"unsupported letters for Pythagorean profile: {unsupported}")
    return letters, [mapping[ch] for ch in letters]


def analyze_text(text: str, registry: dict | None = None) -> TextAnalysis:
    registry = registry or load_registry()
    letters, values = pythagorean_values(text, registry)
    if not values:
        raise ValueError("text contains no supported letters")

    details = [letter_value(ch, registry) for ch in letters]
    ordinals = [detail.ordinal for detail in details]
    glyph_path = [
        detail.glyph_name if detail.glyph_name else f"{detail.letter}:{detail.root}"
        for detail in details
    ]

    root_sequence_surface = "".join(str(value) for value in values)
    ordinal_sum = sum(ordinals)

    return TextAnalysis(
        surface=text,
        letters=letters,
        values=values,
        ordinals=ordinals,
        letter_values=details,
        glyph_path=glyph_path,
        root_sequence_surface=root_sequence_surface,
        numeric_analysis=analyze_number(root_sequence_surface, registry),
        ordinal_sum=ordinal_sum,
        ordinal_sum_reduction_chain=reduction_chain(ordinal_sum),
    )


def candidates_for_root(root: int, digits: int = 2) -> list[int]:
    """Generate positive fixed-width numbers whose digital root equals root.

    Leading-zero expressions are intentionally excluded from canonical candidate
    generation because they are alternate surface forms of shorter numbers.
    """
    if root not in range(1, 10):
        raise ValueError("root must be 1 through 9")
    if digits < 1:
        raise ValueError("digits must be positive")
    start = 1 if digits == 1 else 10 ** (digits - 1)
    stop = 10 ** digits
    return [value for value in range(start, stop) if digital_root(value) == root]


def candidates_for_path(required_roots: Iterable[int], final_root: int | None = None) -> list[int]:
    """Return permutations of a declared digit path, optionally root-filtered.

    This is intentionally conservative: it does not infer intention from free
    text. It only operates on root digits explicitly supplied by the caller.
    """
    from itertools import permutations

    roots = tuple(required_roots)
    if not roots or any(root not in range(1, 10) for root in roots):
        raise ValueError("required_roots must contain digits 1 through 9")
    if final_root is not None and final_root not in range(1, 10):
        raise ValueError("final_root must be 1 through 9")

    seen: set[int] = set()
    out: list[int] = []
    for perm in permutations(roots):
        value = int("".join(str(root) for root in perm))
        if value in seen:
            continue
        seen.add(value)
        if final_root is None or digital_root(value) == final_root:
            out.append(value)
    return sorted(out)


def _print_json(data: object) -> None:
    print(json.dumps(data, indent=2, ensure_ascii=False))


def main() -> None:
    parser = argparse.ArgumentParser(description="Xyool numerical-magic deterministic engine")
    sub = parser.add_subparsers(dest="command", required=True)

    number = sub.add_parser("number", help="analyze a decimal number")
    number.add_argument("value")

    text = sub.add_parser("text", help="analyze letters with dual ordinal/root values")
    text.add_argument("value")

    letter = sub.add_parser("letter", help="show one letter's ordinal and root identity")
    letter.add_argument("value")

    letter_options = sub.add_parser("letter-options", help="show eligible letters for each digit of a ring")
    letter_options.add_argument("value")

    family = sub.add_parser("family", help="generate a root family ladder")
    family.add_argument("root", type=int)
    family.add_argument("--count", type=int, default=12)

    candidates = sub.add_parser("candidates", help="list fixed-width numbers for a final root")
    candidates.add_argument("root", type=int)
    candidates.add_argument("--digits", type=int, default=2)

    args = parser.parse_args()

    if args.command == "number":
        _print_json(asdict(analyze_number(args.value)))
    elif args.command == "text":
        _print_json(asdict(analyze_text(args.value)))
    elif args.command == "letter":
        _print_json(asdict(letter_value(args.value)))
    elif args.command == "letter-options":
        _print_json([[asdict(item) for item in group] for group in letter_options_for_number(args.value)])
    elif args.command == "family":
        _print_json(root_family(args.root, args.count))
    elif args.command == "candidates":
        _print_json(candidates_for_root(args.root, args.digits))


if __name__ == "__main__":
    main()
