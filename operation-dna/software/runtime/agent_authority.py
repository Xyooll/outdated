"""Explicit authority states for autonomous software engineering."""
from __future__ import annotations
from enum import IntEnum


class Authority(IntEnum):
    OBSERVE = 0
    BUILD = 1
    TEST = 2
    REPAIR = 3
    VALIDATE = 4
    REQUEST_PROMOTION = 5
    PROMOTE = 6


def allowed(level: int, required: Authority) -> bool:
    return int(level) >= int(required)


def promotion_requires_authority(level: int) -> bool:
    return allowed(level, Authority.PROMOTE)
