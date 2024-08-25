import unittest
from api import get_random_joke, get_random_joke_by_category, get_joke_categories, search_jokes

class TestChuckNorrisJokesAPI(unittest.TestCase):

    def test_get_random_joke(self):
        response = get_random_joke()
        self.assertIn('value', response)

    def test_get_random_joke_by_category(self):
        categories = get_joke_categories()
        if categories:
            response = get_random_joke_by_category(categories[0])  # Test with the first category
            self.assertIn('value', response)

    def test_get_joke_categories(self):
        response = get_joke_categories()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    def test_search_jokes(self):
        response = search_jokes("chuck")
        self.assertIn('result', response)
        self.assertIsInstance(response['result'], list)

if __name__ == '__main__':
    unittest.main()