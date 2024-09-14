import unittest
from api import *

class TestWorldBankAPI(unittest.TestCase):

    def test_get_country_data(self):
        response = get_country_data("BR")
        self.assertIsInstance(response, list)
        self.assertEqual(response[1][0]['id'], "BRA")

    def test_get_indicator_data(self):
        response = get_indicator_data("BR", "NY.GDP.MKTP.CD", "2006")
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    def test_list_countries(self):
        response = list_countries()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    def test_list_indicators(self):
        response = list_indicators()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    def test_list_regions(self):
        response = list_regions()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    def test_list_income_levels(self):
        response = list_income_levels()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    def test_list_lending_types(self):
        response = list_lending_types()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

if __name__ == "__main__":
    unittest.main()