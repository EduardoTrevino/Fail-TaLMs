import unittest
from api import *

class TestPostcodesAPI(unittest.TestCase):

    def test_lookup_postcode(self):
        response = lookup_postcode("SW1A1AA")
        self.assertEqual(response['status'], 200)

    def test_bulk_lookup_postcodes(self):
        response = bulk_lookup_postcodes(["SW1A1AA", "OX49 5NU"])
        self.assertEqual(response['status'], 200)

    def test_nearest_postcodes(self):
        response = nearest_postcodes(lon=-0.127758, lat=51.507351)
        self.assertEqual(response['status'], 200)

    def test_validate_postcode(self):
        response = validate_postcode("SW1A1AA")
        self.assertEqual(response['status'], 200)

    def test_nearest_postcodes_for_postcode(self):
        response = nearest_postcodes_for_postcode("SW1A1AA")
        self.assertEqual(response['status'], 200)

    def test_autocomplete_postcode(self):
        response = autocomplete_postcode("SW1A")
        self.assertEqual(response['status'], 200)

    def test_query_postcodes(self):
        response = query_postcodes("SW1A")
        self.assertEqual(response['status'], 200)

    def test_lookup_random_postcode(self):
        response = lookup_random_postcode()
        self.assertEqual(response['status'], 200)

    def test_lookup_terminated_postcode(self):
        response = lookup_terminated_postcode("EX16 5BL")
        self.assertEqual(response['status'], 200)

    def test_lookup_outward_code(self):
        response = lookup_outward_code("EC1A")
        self.assertEqual(response['status'], 200)

    def test_nearest_outcode_for_outcode(self):
        response = nearest_outcode_for_outcode("EC1A")
        self.assertEqual(response['status'], 200)

    def test_nearest_outcode(self):
        response = nearest_outcode(lon=-0.127758, lat=51.507351)
        self.assertEqual(response['status'], 200)

    def test_lookup_scottish_postcode(self):
        response = lookup_scottish_postcode("EH1 1AA")
        self.assertEqual(response['status'], 200)

    def test_lookup_place(self):
        response = lookup_place("osgb4000000074564391")
        self.assertEqual(response['status'], 200)

    def test_query_places(self):
        response = query_places("London")
        self.assertEqual(response['status'], 200)

    def test_lookup_random_place(self):
        response = lookup_random_place()
        self.assertEqual(response['status'], 200)

if __name__ == '__main__':
    unittest.main()