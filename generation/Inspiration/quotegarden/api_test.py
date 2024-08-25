import unittest
from api import get_random_quote, get_quotes, get_all_genres, get_all_authors

class TestQuoteGardenAPI(unittest.TestCase):

    def test_get_random_quote(self):
        response = get_random_quote()
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('data', response)

    def test_get_quotes(self):
        response = get_quotes(author="Bill Gates")
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('data', response)

    def test_get_all_genres(self):
        response = get_all_genres()
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('data', response)

    def test_get_all_authors(self):
        response = get_all_authors()
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('data', response)

if __name__ == '__main__':
    unittest.main()