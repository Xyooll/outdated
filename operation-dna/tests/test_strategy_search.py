import unittest
from operation-dna.software.runtime.strategy_search import StrategySearch, create_trading_candidates, create_business_candidates

class StrategySearchTests(unittest.TestCase):
    def test_trading_search_is_reproducible(self):
        search = StrategySearch()
        result = search.search_trading(create_trading_candidates(), runs=10, ticks=100)
        self.assertEqual(result.domain, "trading")
        self.assertEqual(len(result.candidates), 2)

    def test_business_search(self):
        result = StrategySearch().search_business(create_business_candidates(), runs=10, opportunities=100)
        self.assertEqual(result.domain, "business")
        self.assertEqual(len(result.candidates), 2)

if __name__ == "__main__":
    unittest.main()
