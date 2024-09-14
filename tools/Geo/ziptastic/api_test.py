import unittest
from api import get_location_by_zip


class TestZiptasticAPI(unittest.TestCase):

    def test_get_location_by_zip_valid(self):
        # Using a well-known ZIP code for test
        zipcode = "90210"  # Beverly Hills, CA, USA
        response = get_location_by_zip(zipcode)
        self.assertIn("city", response)
        self.assertIn("state", response)
        self.assertIn("country", response)

    def test_get_location_by_zip_invalid(self):
        # Using an invalid ZIP code to test
        zipcode = "00000"
        response = get_location_by_zip(zipcode)
        self.assertIn("error", response)


if __name__ == '__main__':
    unittest.main()