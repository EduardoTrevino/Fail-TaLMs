import unittest
from api import *

class TestBinanceAPI(unittest.TestCase):
    def setUp(self):
        self.toolbench_rapidapi_key = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'

    def test_get_agg_trades(self):
        response = get_agg_trades(symbol="BTCUSDT", toolbench_rapidapi_key=self.toolbench_rapidapi_key)
        self.assertIn('data', response)

    def test_get_avg_price(self):
        response = get_avg_price(symbol="BTCUSDT", toolbench_rapidapi_key=self.toolbench_rapidapi_key)
        self.assertIn('price', response)

    def test_get_exchange_info(self):
        response = get_exchange_info(toolbench_rapidapi_key=self.toolbench_rapidapi_key)
        self.assertIn('symbols', response)

    def test_ping(self):
        response = ping(toolbench_rapidapi_key=self.toolbench_rapidapi_key)
        self.assertEqual({}, response)

    def test_get_24hr_ticker_price_change(self):
        response = get_24hr_ticker_price_change(symbol="BTCUSDT", toolbench_rapidapi_key=self.toolbench_rapidapi_key)
        self.assertIn('lastPrice', response)

    def test_get_all_ticker_prices(self):
        response = get_all_ticker_prices(toolbench_rapidapi_key=self.toolbench_rapidapi_key)
        self.assertIsInstance(response, list)

    def test_get_system_status(self):
        response = get_system_status(toolbench_rapidapi_key=self.toolbench_rapidapi_key)
        self.assertIn('status', response)

    def test_get_account_status(self):
        timestamp = 1640000000000  # example timestamp
        response = get_account_status(timestamp=timestamp, toolbench_rapidapi_key=self.toolbench_rapidapi_key)
        self.assertIn('data', response)

    def test_get_api_trading_status(self):
        timestamp = 1640000000000  # example timestamp
        response = get_api_trading_status(timestamp=timestamp, toolbench_rapidapi_key=self.toolbench_rapidapi_key)
        self.assertIn('data', response)

if __name__ == '__main__':
    unittest.main()