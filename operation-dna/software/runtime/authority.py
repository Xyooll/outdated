"""Human authority boundary for Operation DNA."""
from dataclasses import dataclass


@dataclass(frozen=True)
class AuthorityPolicy:
    autonomy_level: int = 0
    max_capital: float = 0.0
    require_human_for_irreversible: bool = True

    def allows(self, *, autonomy_level: int, capital: float, irreversible: bool) -> bool:
        if autonomy_level > self.autonomy_level:
            return False
        if capital < 0 or capital > self.max_capital:
            return False
        if irreversible and self.require_human_for_irreversible:
            return False
        return True


class HumanAuthority:
    """Explicit approval gate controlled outside the AI decision layer.

    A protected capability is denied by default. Approval must be granted by
    the human-facing control plane and can be revoked independently of the AI.
    """

    def __init__(self, policy: AuthorityPolicy | None = None):
        self.policy = policy or AuthorityPolicy()
        self._approved = False

    @property
    def approved(self) -> bool:
        return self._approved

    def approve(self) -> None:
        self._approved = True

    def revoke(self) -> None:
        self._approved = False

    def authorize(self, *, autonomy_level: int = 0, capital: float = 0.0, irreversible: bool = False) -> bool:
        if not self._approved:
            return False
        return self.policy.allows(
            autonomy_level=autonomy_level,
            capital=capital,
            irreversible=irreversible,
        )
