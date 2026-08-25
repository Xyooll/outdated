import unittest
from software.runtime.storage import MemoryStorage, StorageRouter

class StorageTests(unittest.TestCase):
    def test_memory_backend(self):
        backend = MemoryStorage()
        backend.put("mission", {"name": "test"})
        self.assertEqual(backend.get("mission"), {"name": "test"})
        backend.delete("mission")
        self.assertIsNone(backend.get("mission"))

    def test_router_requires_registered_backend(self):
        router = StorageRouter()
        with self.assertRaises(KeyError):
            router.put("operational", "x", 1)

    def test_router_routes_logical_class(self):
        router = StorageRouter(); backend = MemoryStorage()
        router.register("operational", backend)
        router.put("operational", "x", 42)
        self.assertEqual(router.get("operational", "x"), 42)

if __name__ == "__main__":
    unittest.main()
