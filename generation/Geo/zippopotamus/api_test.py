import unittest
from api import get_zip_info_by_postal_code, get_zip_info_by_city


class TestZippopotamusAPI(unittest.TestCase):
    
    def test_get_zip_info_by_postal_code_valid(self):
        result = get_zip_info_by_postal_code("us", "90210")
        self.assertIn("places", result)
        self.assertEqual(result["country abbreviation"], "US")

    def test_get_zip_info_by_postal_code_invalid(self):
        result = get_zip_info_by_postal_code("us", "00000")
        self.assertEqual(result, {})  # Check if the result is an empty dictionary

    def test_get_zip_info_by_city_valid(self):
        result = get_zip_info_by_city("us", "ca", "beverly hills")
        self.assertIn("places", result)  # Assume "places" is a key

    def test_get_zip_info_by_city_invalid(self):
        result = get_zip_info_by_city("us", "xx", "unknown city")
        self.assertEqual(result, {})  # Check if the result is an empty dictiona


if __name__ == '__main__':
    unittest.main()