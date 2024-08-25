import unittest
import api

class TestWazirxAPI(unittest.TestCase):

    def test_ping(self):
        response = api.ping()
        self.assertEqual(response, {})

    def test_system_status(self):
        response = api.system_status()
        self.assertIn('status', response)
        self.assertIn('message', response)

    def test_server_time(self):
        response = api.server_time()
        self.assertIn('serverTime', response)

    def test_exchange_info(self):
        response = api.exchange_info()
        self.assertIn('timezone', response)
        self.assertIn('serverTime', response)
        self.assertIn('symbols', response)

    def test_tickers_24hr(self):
        response = api.tickers_24hr()
        self.assertIsInstance(response, list)
        if response:  # Check if list is non-empty
            self.assertIn('symbol', response[0])

    def test_ticker_24hr(self):
        response = api.ticker_24hr('btcinr')
        self.assertIn('symbol', response)

    def test_klines(self):
        response = api.klines('btcinr')
        self.assertIsInstance(response, list)
        if response:  # Check if list is non-empty
            self.assertEqual(len(response[0]), 6)

    def test_depth(self):
        response = api.depth('btcinr', limit=5)
        self.assertIn('asks', response)
        self.assertIn('bids', response)

    def test_recent_trades(self):
        response = api.recent_trades('btcinr')
        self.assertIsInstance(response, list)
        if response:  # Check if list is non-empty
            self.assertIn('id', response[0])
            self.assertIn('price', response[0])

if __name__ == '__main__':
    unittest.main()