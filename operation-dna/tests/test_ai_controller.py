import unittest
from software.runtime.ai_controller import AIController, Intent
from software.runtime.capabilities import Capability, CapabilityRegistry

class AIControllerTests(unittest.TestCase):
    def test_ai_can_discover_capabilities(self):
        registry = CapabilityRegistry()
        registry.register(Capability("echo", "return input", lambda value: value, requires_authorization=False))
        controller = AIController(registry)
        self.assertEqual(controller.available_capabilities()[0]["name"], "echo")
        self.assertEqual(controller.execute(Intent("echo", {"value": "ok"})), "ok")

    def test_authorization_is_below_ai(self):
        registry = CapabilityRegistry()
        registry.register(Capability("danger", "restricted", lambda: "bad", requires_authorization=True))
        with self.assertRaises(PermissionError):
            AIController(registry).execute(Intent("danger", {}))

if __name__ == "__main__":
    unittest.main()
