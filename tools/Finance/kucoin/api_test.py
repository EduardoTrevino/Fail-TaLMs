import unittest
from api import *

class TestAPI(unittest.TestCase):

    def test_get_currency_list(self):
        response = get_currency_list()
        self.assertIsInstance(response, dict)
        self.assertIn('data', response)

    def test_get_currency_detail(self):
        response = get_currency_detail(currency="BTC")
        self.assertIsInstance(response, dict)
        self.assertIn('data', response)
        self.assertEqual(response['data']['currency'], "BTC")

    def test_get_symbols_list(self):
        response = get_symbols_list()
        self.assertIsInstance(response['data'], list)
        self.assertGreater(len(response['data']), 0)
        self.assertIn('symbol', response['data'][0])


    def test_get_ticker(self):
        response = get_ticker(symbol="BTC-USDT")
        self.assertIsInstance(response, dict)
        self.assertIn('price', response['data'])

    def test_get_all_tickers(self):
        response = get_all_tickers()
        self.assertIsInstance(response['data']['ticker'], list)
        self.assertGreater(len(response['data']['ticker']), 0)

    def test_get_24hr_stats(self):
        response = get_24hr_stats(symbol="BTC-USDT")
        self.assertIn('symbol', response['data'])
        self.assertEqual(response['data']['symbol'], "BTC-USDT")


    def test_get_market_list(self):
        response = get_market_list()
        self.assertIsInstance(response, dict)
        self.assertIn('data', response)

    def test_get_part_order_book(self):
        response = get_part_order_book(symbol="BTC-USDT", level="level2_20")
        self.assertIn('bids', response['data'])
        self.assertIn('asks', response['data'])

    def test_get_trade_histories(self):
        response = get_trade_histories(symbol="BTC-USDT")
        self.assertIsInstance(response['data'], list)
        self.assertGreater(len(response['data']), 0)
        self.assertIn('price', response['data'][0])

    def test_get_klines(self):
        response = get_klines(symbol="BTC-USDT", type="1min")
        self.assertIsInstance(response['data'], list)
        self.assertGreater(len(response['data']), 0)
        self.assertIsInstance(response['data'][0], list)

    def test_get_fiat_price(self):
        response = get_fiat_price(base="USD", currencies="BTC,ETH")
        self.assertIsInstance(response, dict)
        self.assertIn('data', response)

    def test_get_server_time(self):
        response = get_server_time()
        self.assertIsInstance(response, dict)
        self.assertIn('data', response)

    def test_get_service_status(self):
        response = get_service_status()
        self.assertIsInstance(response, dict)
        self.assertIn('data', response)

if __name__ == '__main__':
    unittest.main()
