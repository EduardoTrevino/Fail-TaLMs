import unittest
from api import auction_data, auctions_data, auctions_info, distilleries_info, distillery_data

class TestWhiskyHunterAPI(unittest.TestCase):

    def test_auction_data(self):
        response = auction_data(slug='catawiki')
        self.assertIn('auctions_data', response)

    def test_auctions_data(self):
        response = auctions_data()
        self.assertIn('auctions_info', response)

    def test_auctions_info(self):
        response = auctions_info()
        self.assertIn('auctions_info', response)

    def test_distilleries_info(self):
        response = distilleries_info()
        self.assertIn('distilleries_info', response)

    def test_distillery_data(self):
        response = distillery_data(slug='ardbeg')
        self.assertIn('distillery_data', response)


if __name__ == '__main__':
    unittest.main()