import unittest
from api import search_universities

class TestUniversitySearchAPI(unittest.TestCase):

    def test_search_universities_by_name(self):
        result = search_universities(name="Middle")
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn("Middle", result[0]['name'])

    def test_search_universities_by_name_and_country(self):
        result = search_universities(name="Middle", country="Turkey")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['country'], "Turkey")
        self.assertIn("Middle", result[0]['name'])

    def test_search_universities_with_limit(self):
        result = search_universities(name="Middle", limit=1)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)

    def test_search_universities_with_offset(self):
        initial_result = search_universities(name="Middle", limit=1)
        offset_result = search_universities(name="Middle", offset=1, limit=1)
        self.assertIsInstance(offset_result, list)
        self.assertEqual(len(offset_result), 1)
        self.assertNotEqual(initial_result[0]['name'], offset_result[0]['name'])

if __name__ == '__main__':
    unittest.main()