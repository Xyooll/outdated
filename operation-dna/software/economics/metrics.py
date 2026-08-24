"""Economic and infrastructure efficiency metrics."""

def capital_efficiency(output: float, capital: float) -> float:
    return output / capital if capital > 0 else 0.0


def infrastructure_ratio(infrastructure_cost: float, productive_output: float) -> float:
    return infrastructure_cost / productive_output if productive_output > 0 else float("inf")


def return_on_deployed_capital(gain: float, deployed: float) -> float:
    return gain / deployed if deployed > 0 else 0.0
