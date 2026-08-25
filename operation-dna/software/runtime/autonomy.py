"""Explicit autonomy modes. Human authority remains above every mode."""
from enum import IntEnum

class Autonomy(IntEnum):
    OBSERVE = 0
    SIMULATE = 1
    PROPOSE = 2
    CONTROLLED_EXECUTION = 3
    AUTONOMOUS_EXECUTION = 4

class AutonomyError(PermissionError):
    pass

def require_mode(current: Autonomy, required: Autonomy) -> None:
    if current < required:
        raise AutonomyError(f"autonomy level {current.name} cannot perform {required.name} action")
