import tempfile
import unittest
from pathlib import Path
from software.runtime.production_readiness import ResourceBudget, KillSwitch, PersistentState, RuntimeState, VersionStore
from software.runtime.event_log import EventLog, AIEvent

class EndToEndReadinessTests(unittest.TestCase):
    def test_runtime_controls_and_audit(self):
        with tempfile.TemporaryDirectory() as d:
            log = EventLog(str(Path(d)/"events.jsonl"))
            state = PersistentState(str(Path(d)/"state.json")); state.save(RuntimeState("maximize sustainable resources"))
            budget = ResourceBudget(max_cost=2, max_actions=2, max_experiments=2)
            kill = KillSwitch(); versions = VersionStore(str(Path(d)/"versions.json"))
            budget.consume(cost=.25, action=True)
            versions.add("v1", {"strategy":"baseline"}); versions.promote("v1")
            log.append(AIEvent(event_type="runtime_cycle", objective=state.load().mission, result={"version":"v1"}))
            self.assertEqual(len(log.read()), 1)
            self.assertEqual(versions.active().version, "v1")
            kill.stop()
            with self.assertRaises(RuntimeError): kill.check()

if __name__ == "__main__": unittest.main()
