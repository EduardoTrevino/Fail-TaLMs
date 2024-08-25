import unittest
from api import (
    get_server_time,
    get_system_status,
    get_asset_info,
    get_tradable_asset_pairs,
    get_ticker_information,
    get_ohlc_data,
    get_order_book,
    get_recent_trades,
    get_recent_spreads
)

class TestKrakenAPI(unittest.TestCase):

    def test_get_server_time(self):
        response = get_server_time()
        self.assertIn("result", response)
    
    def test_get_system_status(self):
        response = get_system_status()
        self.assertIn("result", response)
    
    def test_get_asset_info(self):
        response = get_asset_info()
        self.assertIn("result", response)
    
    def test_get_tradable_asset_pairs(self):
        response = get_tradable_asset_pairs()
        self.assertIn("result", response)
        
    def test_get_ticker_information(self):
        response = get_ticker_information()
        self.assertIn("result", response)
    
    def test_get_ohlc_data(self):
        response = get_ohlc_data(pair="XBTUSD")
        self.assertIn("result", response)
    
    def test_get_order_book(self):
        response = get_order_book(pair="XBTUSD")
        self.assertIn("result", response)
    
    def test_get_recent_trades(self):
        response = get_recent_trades(pair="XBTUSD")
        self.assertIn("result", response)
    
    def test_get_recent_spreads(self):
        response = get_recent_spreads(pair="XBTUSD")
        self.assertIn("result", response)

if __name__ == '__main__':
    unittest.main()