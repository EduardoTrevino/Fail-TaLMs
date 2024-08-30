import unittest
from api import get_market_ticker, get_order_book

class TestOKXAPI(unittest.TestCase):

    def test_get_market_ticker(self):
        response = get_market_ticker('BTC-USDT')
        self.assertIn('data', response)
        self.assertEqual(response['data'][0]['instId'], 'BTC-USDT')

    def test_get_order_book(self):
        response = get_order_book('BTC-USDT')
        self.assertIn('data', response)
        self.assertTrue('asks' in response['data'][0] or 'bids' in response['data'][0])

if __name__ == '__main__':
    unittest.main()