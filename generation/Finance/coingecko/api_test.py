import unittest
from api import coins_list, top_gainers_losers, recently_added_coins, coins_markets, coin_data_by_id

class TestCoinGeckoAPI(unittest.TestCase):

    def test_coins_list(self):
        result = coins_list()
        self.assertIsInstance(result, list, "The response should be a list of coins.")

    def test_top_gainers_losers(self):
        result = top_gainers_losers(vs_currency='usd')
        self.assertIn('top_gainers', result[0], "The response must contain 'top_gainers'")
        self.assertIn('top_losers', result[0], "The response must contain 'top_losers'")

    def test_recently_added_coins(self):
        result = recently_added_coins()
        self.assertIsInstance(result, list, "The response should be a list of recently added coins.")

    def test_coins_markets(self):
        result = coins_markets(vs_currency='usd')
        self.assertIsInstance(result, list, "The response should be a list of market data for coins.")

    def test_coin_data_by_id(self):
        result = coin_data_by_id(id='bitcoin')
        self.assertIsInstance(result, dict, "The response should be a dictionary with bitcoin's data.")
        self.assertIn('id', result, "Bitcoin data should have an 'id' field.")
        self.assertEqual(result['id'], 'bitcoin', "The 'id' field should be 'bitcoin'.")

if __name__ == '__main__':
    unittest.main()