import unittest
import api

class TestNominatumAPI(unittest.TestCase):

    def test_search_freeform(self):
        result = api.search(q="Baker Street, London", limit=1)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_search_structured(self):
        result = api.search(street="Baker Street", city="London", limit=1)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_reverse(self):
        result = api.reverse(lat=51.5235, lon=-0.1586)
        self.assertIn('address', result)
        self.assertEqual(result['address']['road'], "Baker Street")

    def test_lookup(self):
        osm_ids = ["W104393803"]
        result = api.lookup(osm_ids=osm_ids)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn('display_name', result[0])

    def test_status(self):
        result = api.status(format="json")
        self.assertIn('status', result)
        self.assertEqual(result['message'], "OK")


if __name__ == '__main__':
    unittest.main()