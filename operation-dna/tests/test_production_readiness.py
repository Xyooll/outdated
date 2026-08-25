import tempfile
import unittest
from pathlib import Path
from software.runtime.production_readiness import ResourceBudget, KillSwitch, VersionStore, PersistentState, RuntimeState

class ProductionReadinessTests(unittest.TestCase):
    def test_budget(self):
        b = ResourceBudget(max_cost=1, max_actions=1, max_experiments=1)
        b.consume(.5, action=True, experiment=True)
        with self.assertRaises(RuntimeError): b.consume(.6)

    def test_kill_switch(self):
        k = KillSwitch(); k.stop()
        with self.assertRaises(RuntimeError): k.check()
        k.reset(); k.check()

    def test_state_persists(self):
        with tempfile.TemporaryDirectory() as d:
            p = PersistentState(str(Path(d)/"state.json")); p.save(RuntimeState("grow", False, {"x": 1}))
            self.assertEqual(p.load().mission, "grow")

    def test_version_rollback(self):
        with tempfile.TemporaryDirectory() as d:
            v = VersionStore(str(Path(d)/"versions.json")); v.add("v1", "a"); v.promote("v1"); v.add("v2", "b"); v.promote("v2")
            self.assertEqual(v.rollback().version, "v1")

if __name__ == "__main__": unittest.main()
