import unittest
from api import auction_data_slug, auctions_data, auctions_info, distilleries_info, distillery_data

class TestWhiskyHunterAPI(unittest.TestCase):

    def test_auction_data_slug(self):
        response = auction_data_slug(slug='catawiki')
        self.assertIsInstance(response, list)
        self.assertTrue(all(isinstance(item, dict) for item in response))
        self.assertTrue(all('auction_name' in item for item in response))

    def test_auctions_data(self):
        response = auctions_data()
        self.assertIsInstance(response, list)
        self.assertTrue(all(isinstance(item, dict) for item in response))
        self.assertTrue(all('auction_name' in item for item in response))

    def test_auctions_info(self):
        response = auctions_info()
        self.assertIsInstance(response, list)
        self.assertTrue(all(isinstance(item, dict) for item in response))
        self.assertTrue(all('name' in item for item in response))

    def test_distillery_info(self):
        response = auctions_info()
        self.assertIsInstance(response, list)
        self.assertTrue(all(isinstance(item, dict) for item in response))
        self.assertTrue(all('name' in item for item in response))

    def test_distillery_data(self):
        response = distillery_data(slug='ardbeg')
        self.assertIsInstance(response, list)
        self.assertTrue(all(isinstance(item, dict) for item in response))
        self.assertTrue(all('slug' in item and item['slug'] == 'ardbeg' for item in response))



if __name__ == '__main__':
    unittest.main()