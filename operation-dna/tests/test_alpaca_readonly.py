import os
import unittest
from unittest.mock import patch

from software.integrations.alpaca_readonly import AlpacaReadOnlyProvider, AlpacaConfigurationError


class AlpacaReadOnlyTests(unittest.TestCase):
    def test_requires_credentials(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(AlpacaConfigurationError):
                AlpacaReadOnlyProvider().observe()

    def test_provider_is_read_only(self):
        provider = AlpacaReadOnlyProvider()
        public_names = {name for name in dir(provider) if not name.startswith("_")}
        self.assertEqual(public_names, {"base_url", "feed", "name", "observe", "symbol", "timeout"})


if __name__ == "__main__":
    unittest.main()
