"""Run one live, read-only observation through an Xyool provider."""
from integrations.alpaca_readonly import AlpacaReadOnlyProvider, AlpacaConfigurationError


def main() -> int:
    provider = AlpacaReadOnlyProvider()
    try:
        observation = provider.observe()
    except AlpacaConfigurationError as exc:
        print(f"NOT CONFIGURED: {exc}")
        return 2
    print(
        f"LIVE-READ provider={observation.provider} "
        f"event={observation.event_type} side_effects={observation.side_effects} "
        f"payload={observation.payload}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
