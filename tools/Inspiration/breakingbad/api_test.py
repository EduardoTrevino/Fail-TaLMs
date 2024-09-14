import unittest
from api import get_random_quote, get_multiple_quotes


class TestBreakingBadAPI(unittest.TestCase):

    def test_get_random_quote(self):
        result = get_random_quote()
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)
        self.assertIn("quote", result[0])
        self.assertIn("author", result[0])

    def test_get_multiple_quotes(self):
        result = get_multiple_quotes(5)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 5)
        for quote in result:
            self.assertIn("quote", quote)
            self.assertIn("author", quote)


if __name__ == '__main__':
    unittest.main()