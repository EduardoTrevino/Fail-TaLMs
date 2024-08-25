import unittest
from api import parse_page, search_open_search, get_sitematrix


class TestMediaWikiAPI(unittest.TestCase):
    
    def test_parse_page(self):
        response = parse_page("Pet_door")
        self.assertIn('parse', response)
        self.assertIn('title', response['parse'])
        self.assertEqual(response['parse']['title'], "Pet door")

    def test_search_open_search(self):
        response = search_open_search("Pet door")
        self.assertIsInstance(response, list)
        self.assertGreater(len(response[1]), 0)  # Check that search results are returned
    
    def test_get_sitematrix(self):
        response = get_sitematrix()
        self.assertIn('sitematrix', response)
        self.assertTrue(len(response['sitematrix']) > 0)


if __name__ == '__main__':
    unittest.main()