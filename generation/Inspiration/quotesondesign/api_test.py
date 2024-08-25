import unittest
from api import get_random_quotes


class TestQuotesOnDesignAPI(unittest.TestCase):
    
    def test_get_random_quotes(self):
        # Test the default random quotes retrieval
        response = get_random_quotes()
        self.assertIsInstance(response, list, "Expected response to be a list")
        for quote in response:
            self.assertIn('content', quote, "Expected 'content' in quote")
            self.assertIn('title', quote, "Expected 'title' in quote")


if __name__ == '__main__':
    unittest.main()