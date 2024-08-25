import unittest
from api import card_search, card_named_exact, card_named_fuzzy, cards_autocomplete, card_random

class TestScryfallAPI(unittest.TestCase):

    def test_card_search(self):
        result = card_search(q="c:blue mv=1")
        self.assertIn("data", result)

    def test_card_named_exact(self):
        result = card_named_exact(exact="Black Lotus")
        self.assertEqual(result.get("name"), "Black Lotus")

    def test_card_named_fuzzy(self):
        result = card_named_fuzzy(fuzzy="blck lot")
        self.assertEqual(result.get("name"), "Black Lotus")

    def test_cards_autocomplete(self):
        result = cards_autocomplete(q="thal")
        self.assertIn("data", result)

    def test_card_random(self):
        result = card_random()
        self.assertIn("name", result)

if __name__ == '__main__':
    unittest.main()