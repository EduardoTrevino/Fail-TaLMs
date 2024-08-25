import unittest
from api import get_pairs_by_chain_and_address, get_pairs_by_token_address, search_pairs

class TestDexScreenerAPI(unittest.TestCase):

    def test_get_pairs_by_chain_and_address(self):
        response = get_pairs_by_chain_and_address('bsc', ['0x7213a321F1855CF1779f42c0CD85d3D95291D34C'])
        self.assertIsInstance(response, dict)
        self.assertIn('pairs', response)

    def test_get_pairs_by_token_address(self):
        response = get_pairs_by_token_address(['0x2170Ed0880ac9A755fd29B2688956BD959F933F8'])
        self.assertIsInstance(response, dict)
        self.assertIn('pairs', response)

    def test_search_pairs(self):
        response = search_pairs('WBNB USDC')
        self.assertIsInstance(response, dict)
        self.assertIn('pairs', response)

if __name__ == '__main__':
    unittest.main()