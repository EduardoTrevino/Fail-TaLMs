import unittest
from api import get_random_quote, get_random_quotes, list_quotes, get_quote_by_id, list_authors, search_quotes, search_authors, get_author_by_slug, list_tags

class TestQuotableAPI(unittest.TestCase):

    def test_get_random_quote(self):
        response = get_random_quote()
        self.assertIn('content', response)
        self.assertIn('author', response)

    def test_get_random_quotes(self):
        response = get_random_quotes(limit=3)
        self.assertEqual(len(response), 3)
        for quote in response:
            self.assertIn('content', quote)
            self.assertIn('author', quote)

    def test_list_quotes(self):
        response = list_quotes(limit=5, page=1)
        self.assertIn('results', response)
        self.assertEqual(len(response['results']), 5)

    def test_get_quote_by_id(self):
        quote_id = "5d91b45d99d0d60001d72745"  # Example ID, replace with a valid ID if needed
        response = get_quote_by_id(quote_id)
        self.assertIn('content', response)
        self.assertIn('author', response)

    def test_list_authors(self):
        response = list_authors(limit=3, page=1)
        self.assertIn('results', response)
        self.assertEqual(len(response['results']), 3)

    def test_search_quotes(self):
        response = search_quotes(query="life")
        self.assertIn('results', response)

    def test_search_authors(self):
        response = search_authors(query="Einstein")
        self.assertIn('results', response)

    def test_get_author_by_slug(self):
        author_slug = "albert-einstein"  # Example slug
        response = get_author_by_slug(author_slug)
        self.assertIn('name', response)

    def test_list_tags(self):
        response = list_tags()
        self.assertIn('results', response)

if __name__ == '__main__':
    unittest.main()