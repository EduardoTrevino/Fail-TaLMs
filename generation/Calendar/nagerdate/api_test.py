import unittest
from api import *


class TestNagerDateAPI(unittest.TestCase):

    def test_get_country_info(self):
        result = get_country_info("AT")
        self.assertIsInstance(result, dict)
        self.assertIn("countryCode", result)
        self.assertEqual(result["countryCode"], "AT")

    def test_get_available_countries(self):
        result = get_available_countries()
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_get_long_weekends(self):
        result = get_long_weekends(2024, "AT")
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_get_public_holidays(self):
        result = get_public_holidays(2024, "AT")
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_is_today_public_holiday(self):
        result = is_today_public_holiday("AT")
        self.assertIsInstance(result, dict)
        self.assertIn("status_code", result)

    def test_get_next_public_holidays(self):
        result = get_next_public_holidays("AT")
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_get_next_public_holidays_worldwide(self):
        result = get_next_public_holidays_worldwide()
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_get_version(self):
        result = get_version()
        self.assertIsInstance(result, dict)
        self.assertIn("version", result)


if __name__ == '__main__':
    unittest.main()