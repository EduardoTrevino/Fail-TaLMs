import unittest
from api import get_quote, get_quotes, search_quotes

class TestRonSwansonAPI(unittest.TestCase):
    
    def test_get_quote(self):
        response = get_quote()
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 1)
        self.assertIsInstance(response[0], str)

    def test_get_quotes(self):
        count = 3
        response = get_quotes(count)
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), count)
        for quote in response:
            self.assertIsInstance(quote, str)

    def test_search_quotes(self):
        term = "hate"
        response = search_quotes(term)
        self.assertIsInstance(response, list)
        for quote in response:
            self.assertIsInstance(quote, str)
            self.assertIn(term.lower(), quote.lower())

if __name__ == "__main__":
    unittest.main()