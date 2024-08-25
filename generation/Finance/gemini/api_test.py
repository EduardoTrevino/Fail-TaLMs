import unittest
from api import *


class TestGeminiAPI(unittest.TestCase):

    def test_get_symbols(self):
        symbols = get_symbols()
        self.assertIsInstance(symbols, list)
        self.assertGreater(len(symbols), 0)

    def test_get_symbol_details(self):
        details = get_symbol_details('btcusd')
        self.assertIsInstance(details, dict)
        self.assertIn('symbol', details)

    def test_get_network(self):
        network = get_network('btc')
        self.assertIsInstance(network, dict)
        self.assertIn('network', network)

    def test_get_ticker(self):
        ticker = get_ticker('btcusd')
        self.assertIsInstance(ticker, dict)
        self.assertIn('ask', ticker)

    def test_get_ticker_v2(self):
        ticker_v2 = get_ticker_v2('btcusd')
        self.assertIsInstance(ticker_v2, dict)
        self.assertIn('symbol', ticker_v2)

    def test_get_candles(self):
        candles = get_candles('btcusd', '15m')
        self.assertIsInstance(candles, list)
        self.assertGreater(len(candles), 0)

    def test_get_derivatives_candles(self):
        derivatives_candles = get_derivatives_candles('BTCGUSDPERP', '1m')
        self.assertIsInstance(derivatives_candles, list)

    def test_get_fee_promos(self):
        fee_promos = get_fee_promos()
        self.assertIsInstance(fee_promos, dict)
        self.assertIn('symbols', fee_promos)

    def test_get_current_order_book(self):
        order_book = get_current_order_book('btcusd')
        self.assertIsInstance(order_book, dict)
        self.assertIn('bids', order_book)
        self.assertIn('asks', order_book)

    def test_get_trade_history(self):
        trade_history = get_trade_history('btcusd')
        self.assertIsInstance(trade_history, list)

    def test_get_price_feed(self):
        price_feed = get_price_feed()
        self.assertIsInstance(price_feed, list)

    def test_get_funding_amount(self):
        funding_amount = get_funding_amount('btcgusdperp')
        self.assertIsInstance(funding_amount, dict)
        self.assertIn('symbol', funding_amount)


if __name__ == '__main__':
    unittest.main()