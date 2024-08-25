import unittest
from api import (
    show_current_user,
    show_authorization_information,
    get_fiat_currencies,
    get_cryptocurrencies,
    get_exchange_rates,
    get_buy_price,
    get_sell_price,
    get_spot_price,
    get_current_time
)

class TestCoinbaseAPI(unittest.TestCase):

    def setUp(self):
        self.token = 'TEST_TOKEN'
        self.currency_pair = 'BTC-USD'

    def test_show_current_user(self):
        response = show_current_user(self.token)
        self.assertIn('data', response)

    def test_show_authorization_information(self):
        response = show_authorization_information(self.token)
        self.assertIn('data', response)

    def test_get_fiat_currencies(self):
        response = get_fiat_currencies()
        self.assertIn('data', response)

    def test_get_cryptocurrencies(self):
        response = get_cryptocurrencies()
        self.assertIn('data', response)

    def test_get_exchange_rates(self):
        response = get_exchange_rates()
        self.assertIn('data', response)

    def test_get_buy_price(self):
        response = get_buy_price(self.currency_pair)
        self.assertIn('data', response)

    def test_get_sell_price(self):
        response = get_sell_price(self.currency_pair)
        self.assertIn('data', response)

    def test_get_spot_price(self):
        response = get_spot_price(self.currency_pair)
        self.assertIn('data', response)

    def test_get_current_time(self):
        response = get_current_time()
        self.assertIn('data', response)

if __name__ == '__main__':
    unittest.main()