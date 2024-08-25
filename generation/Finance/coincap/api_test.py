import unittest
from api import get_assets, get_asset_by_id, get_markets, get_exchange_data

class TestCoinCapAPI(unittest.TestCase):

    def test_get_assets(self):
        response = get_assets()
        self.assertIn('data', response)
        self.assertIsInstance(response['data'], list)

    def test_get_asset_by_id(self):
        response = get_asset_by_id('bitcoin')
        self.assertIn('data', response)
        self.assertEqual(response['data']['id'], 'bitcoin')

    def test_get_markets(self):
        response = get_markets()
        self.assertIn('data', response)
        self.assertIsInstance(response['data'], list)

    def test_get_exchange_data(self):
        response = get_exchange_data()
        self.assertIn('data', response)
        self.assertIsInstance(response['data'], list)

if __name__ == '__main__':
    unittest.main()