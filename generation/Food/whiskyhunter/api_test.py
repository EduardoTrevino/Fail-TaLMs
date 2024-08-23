import unittest
import api

class TestWhiskyHunterAPI(unittest.TestCase):

    def test_auction_data(self):
        response = api.auction_data(slug='catawiki')
        self.assertIn('auctions_data', response)

    def test_auctions_data(self):
        response = api.auctions_data()
        self.assertIn('auctions_data', response)

    def test_auctions_info(self):
        response = api.auctions_info()
        self.assertIn('auctions_info', response)

    def test_distilleries_info(self):
        response = api.distilleries_info()
        self.assertIn('distilleries_info', response)

    def test_distillery_data(self):
        response = api.distillery_data(slug='ardbeg')
        self.assertIn('distillery_data', response)


if __name__ == '__main__':
    unittest.main()