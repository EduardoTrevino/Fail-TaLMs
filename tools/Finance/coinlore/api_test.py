import unittest
from api import (
    get_global_stats,
    get_all_tickers,
    get_ticker,
    get_markets_for_coin,
    get_all_exchanges,
    get_exchange,
    get_social_stats
)

class TestCoinloreAPI(unittest.TestCase):

    def test_get_global_stats(self):
        result = get_global_stats()
        self.assertIn('coins_count', result[0])

    def test_get_all_tickers(self):
        result = get_all_tickers()
        self.assertIn('data', result)

    def test_get_ticker(self):
        result = get_ticker("90")
        self.assertEqual(result[0]['symbol'], "BTC")

    def test_get_markets_for_coin(self):
        result = get_markets_for_coin("90")
        self.assertIsInstance(result, list)

    def test_get_all_exchanges(self):
        result = get_all_exchanges()
        self.assertIn('5', result)

    def test_get_exchange(self):
        result = get_exchange("5")
        self.assertIn('0', result)
        self.assertIn('pairs', result)

    def test_get_social_stats(self):
        result = get_social_stats("80")
        self.assertIn('reddit', result)
        self.assertIn('twitter', result)

if __name__ == '__main__':
    unittest.main()