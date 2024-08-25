import unittest
from api import *

class TestNexchangeAPI(unittest.TestCase):

    def test_get_currencies(self):
        response = get_currencies()
        self.assertIsInstance(response, list)

    def test_get_pairs(self):
        response = get_pairs()
        self.assertIsInstance(response, list)

    def test_get_price(self):
        response = get_price(pair_name="BTCLTC", amount_base=1.0, amount_quote=100.0)
        self.assertIsInstance(response, dict)

    def test_get_rate_info(self):
        response = get_rate_info(rate_id="PINDUF8")
        self.assertIsInstance(response, dict)

    def test_get_latest_price(self):
        response = get_latest_price(pair_name="BTCLTC")
        self.assertIsInstance(response, list)

    def test_get_price_history(self):
        response = get_price_history(pair_name="BTCLTC")
        self.assertIsInstance(response, list)

    def test_get_prices_info_list(self):
        response = get_prices_info_list()
        self.assertIsInstance(response, list)

    def test_get_orders(self):
        response = get_orders()
        self.assertIsInstance(response, dict)

    def test_get_order(self):
        response = get_order(unique_reference="1CPL5")
        self.assertIsInstance(response, dict)

    def test_get_ticker(self):
        response = get_ticker()
        self.assertIsInstance(response, dict)

    def test_get_volume(self):
        response = get_volume()
        self.assertIsInstance(response, dict)

if __name__ == '__main__':
    unittest.main()