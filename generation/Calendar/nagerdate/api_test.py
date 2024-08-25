import unittest
from api import *

class TestNagerdateAPI(unittest.TestCase):

    def test_public_holidays(self):
        response = public_holidays(2024, 'AT')
        self.assertIsInstance(response, list)

    def test_country_info(self):
        response = country_info('AT')
        self.assertIsInstance(response, dict)
        self.assertIn("commonName", response)

    def test_available_countries(self):
        response = available_countries()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    def test_long_weekends(self):
        response = long_weekends(2024, 'AT')
        self.assertIsInstance(response, list)

    def test_is_today_public_holiday(self):
        response = is_today_public_holiday('AT')
        self.assertIsInstance(response, bool)

    def test_next_public_holidays(self):
        response = next_public_holidays('AT')
        self.assertIsInstance(response, list)

    def test_next_public_holidays_worldwide(self):
        response = next_public_holidays_worldwide()
        self.assertIsInstance(response, list)

    def test_version(self):
        response = version()
        self.assertIsInstance(response, dict)
        self.assertIn("name", response)
        self.assertIn("version", response)

if __name__ == '__main__':
    unittest.main()