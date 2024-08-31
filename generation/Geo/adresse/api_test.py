import unittest
from api import search_address, reverse_geocode, mass_geocode_csv, mass_reverse_geocode_csv


class TestAdresseAPI(unittest.TestCase):

    def test_search_address(self):
        response = search_address(q="8 bd du port", limit=1)
        self.assertIn("features", response)
        self.assertIsInstance(response["features"], list)

    def test_reverse_geocode(self):
        response = reverse_geocode(lat=48.357, lon=2.37)
        self.assertIn("features", response)
        self.assertIsInstance(response["features"], list)

if __name__ == '__main__':
    unittest.main()