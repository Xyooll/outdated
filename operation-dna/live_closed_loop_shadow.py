"""Continuous closed-loop shadow runner.

Runs live public crypto observations through attention, AI decisioning,
forecasting, synthetic outcome evaluation, calibration, and append-only memory.
It never places orders or touches a trading account.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path

from software.economics.learning import Forecast, Outcome, calibration, evaluate
from software.integrations.alpaca_public_crypto import AlpacaPublicCryptoAdapter
from software.runtime.ai_controller import AIController, Intent
from software.runtime.attention import AttentionEngine, AttentionRule, Event
from software.runtime.capabilities import Capability, CapabilityRegistry
from software.runtime.event_log import AIEvent, EventLog
from software.runtime.production_readiness import KillSwitch, PersistentState, ResourceBudget, RuntimeState


def stable_id(*parts: object) -> str:
    return hashlib.sha256("|".join(map(str, parts)).encode()).hexdigest()[:24]


def decision(bid: float, ask: float, history: list[dict]) -> dict:
    spread = ask - bid
    previous = history[-1].get("decision", {}) if history else {}
    # Bounded policy: memory can inform the rationale, but cannot grant execution authority.
    if spread > 0:
        action = "OBSERVE"
        confidence = min(0.95, 0.70 + min(spread / 1000.0, 0.20))
    else:
        action = "IGNORE"
        confidence = 0.90
    return {
        "action": action,
        "confidence": round(confidence, 4),
        "expected_upside": 0.0,
        "expected_downside": 0.0,
        "rationale": f"shadow policy; spread={spread:.6f}; prior_action={previous.get('action', 'none')}",
    }


def build_controller() -> AIController:
    registry = CapabilityRegistry()
    registry.register(Capability(
        name="shadow.make_decision",
        description="Create a bounded decision without execution.",
        handler=lambda bid_price, ask_price, history: decision(float(bid_price), float(ask_price), history),
        requires_authorization=False,
        reversible=True,
        risk_class="none",
    ))
    return AIController(registry)


def run_once(adapter, controller, attention, log, state_store, budget, kill, history) -> dict:
    kill.check()
    quote = adapter.latest_quote("BTC/USD")
    payload = adapter.as_payload(quote)
    event = Event(quote.provider, quote.event_type, payload, importance=1.0)
    signals = attention.evaluate(event)
    if not signals or not signals[0].wake_ai:
        return {"woke": False, "payload": payload}

    budget.consume(experiment=True)
    intent = Intent(
        capability="shadow.make_decision",
        arguments={"bid_price": payload["bid_price"], "ask_price": payload["ask_price"], "history": history[-20:]},
        rationale="live attention signal reached bounded shadow decision policy",
        autonomy_level=0,
        capital=0.0,
        irreversible=False,
    )
    result = controller.execute(intent)
    forecast = Forecast(
        forecast_id=stable_id(quote.symbol, quote.timestamp, result["action"], payload["bid_price"]),
        opportunity_key=quote.symbol,
        predicted_score=result["confidence"],
        predicted_upside=result["expected_upside"],
        predicted_downside=result["expected_downside"],
        created_at=datetime.now(timezone.utc).isoformat(),
    )
    outcome = Outcome(forecast.forecast_id, 0.0, 0.0, datetime.now(timezone.utc).isoformat())
    evaluation = evaluate(forecast, outcome)
    result_record = {"payload": payload, "decision": result, "forecast": forecast.__dict__, "outcome": outcome.__dict__, "evaluation": evaluation}
    history.append(result_record)
    state_store.save(RuntimeState(mission="live closed-loop shadow", paused=False, data={"last": result_record, "samples": len(history)}))
    log.append(AIEvent(
        event_type="shadow.closed_loop",
        objective="evaluate live decision policy",
        trigger=signals[0].rule,
        attention_score=signals[0].priority,
        context=payload,
        plan=intent.__dict__,
        capabilities=[intent.capability],
        actions=[{"action": result["action"], "side_effects": False}],
        result=result,
        expected_outcome=forecast.predicted_upside,
        actual_outcome=outcome.realized_return,
        confidence=result["confidence"],
        cost=0.0,
        lessons=["shadow outcome is synthetic until paper execution exists"],
    ))
    return {"woke": True, "payload": payload, "signals": len(signals), "decision": result, "evaluation": evaluation}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cycles", type=int, default=1)
    parser.add_argument("--interval", type=float, default=0.0)
    args = parser.parse_args()
    if args.cycles < 1:
        raise SystemExit("--cycles must be >= 1")

    adapter = AlpacaPublicCryptoAdapter()
    controller = build_controller()
    attention = AttentionEngine()
    attention.register(AttentionRule("live_crypto_closed_loop", "alpaca-public-crypto", lambda e: e.data.get("bid_price", 0) < e.data.get("ask_price", 0), priority=10.0))
    log = EventLog("data/logs/live_closed_loop.jsonl")
    state_store = PersistentState("data/live_closed_loop_state.json")
    budget = ResourceBudget(max_cost=float(max(1, args.cycles)), max_actions=0, max_experiments=max(1, args.cycles))
    kill = KillSwitch()
    history = []
    for _ in range(args.cycles):
        out = run_once(adapter, controller, attention, log, state_store, budget, kill, history)
        if out.get("woke"):
            print(f"LIVE {out['payload']['symbol']} AI_WAKE=YES DECISION={out['decision']['action']} CONFIDENCE={out['decision']['confidence']:.4f} SIDE_EFFECTS=False")
        else:
            print("AI_WAKE=NO")
        if args.interval:
            time.sleep(args.interval)

    results = [x["evaluation"] for x in history]
    print(f"SAMPLES={len(results)}")
    print(f"CALIBRATION={json.dumps(calibration(results), sort_keys=True)}")
    print(f"EVENT_LOG={log.path}")
    print(f"STATE={state_store.path}")
    print("EXECUTION=DISABLED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
