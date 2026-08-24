"""Capability-based permission boundaries for future executors."""
from dataclasses import dataclass
from enum import Enum


class Capability(str, Enum):
    READ_RESEARCH = "read_research"
    WRITE_CODE = "write_code"
    RUN_TESTS = "run_tests"
    MANAGE_INFRA = "manage_infra"
    EXECUTE_TRADE = "execute_trade"
    SPEND_FUNDS = "spend_funds"


@dataclass(frozen=True)
class PermissionSet:
    capabilities: frozenset[Capability]

    def allows(self, capability: Capability) -> bool:
        return capability in self.capabilities


READ_ONLY = PermissionSet(frozenset({Capability.READ_RESEARCH}))
RESEARCH = PermissionSet(frozenset({Capability.READ_RESEARCH, Capability.RUN_TESTS}))


def require(permission: PermissionSet, capability: Capability) -> None:
    if not permission.allows(capability):
        raise PermissionError(f"Capability denied: {capability.value}")
