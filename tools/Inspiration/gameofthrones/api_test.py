import unittest
from api import (
    get_random_quote,
    get_random_quotes,
    get_quotes_by_character,
    get_houses,
    get_house_details,
    get_characters,
    get_character_details
)

class TestGameOfThronesAPI(unittest.TestCase):

    def test_get_random_quote(self):
        result = get_random_quote()
        self.assertIn('sentence', result)
        self.assertIn('character', result)

    def test_get_random_quotes(self):
        result = get_random_quotes(3)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)

    def test_get_quotes_by_character(self):
        result = get_quotes_by_character('tyrion', 2)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
    
    def test_get_houses(self):
        result = get_houses()
        self.assertIsInstance(result, list)

    def test_get_house_details(self):
        result = get_house_details('lannister')
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_get_characters(self):
        result = get_characters()
        self.assertIsInstance(result, list)

    def test_get_character_details(self):
        result = get_character_details('jon')
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()