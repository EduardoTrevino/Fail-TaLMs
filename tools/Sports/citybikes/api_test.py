import unittest
from api import get_networks, get_network_details

class TestCityBikesAPI(unittest.TestCase):

    def test_get_networks(self):
        response = get_networks(fields="id,name,href")
        self.assertIn('networks', response)
        self.assertIsInstance(response['networks'], list)

    def test_get_network_details(self):
        network_id = "velib"
        response = get_network_details(network_id)
        self.assertIn('network', response)
        self.assertEqual(response['network']['id'], network_id)

    def test_get_networks_with_invalid_field(self):
        response = get_networks(fields="invalid_field")
        self.assertNotIn('error', response)

if __name__ == '__main__':
    unittest.main()