import unittest
from api import get_cards, get_sets, get_card_by_id

class TestPokemonTCGAPI(unittest.TestCase):

    def test_get_cards(self):
        response = get_cards(name='Charizard')
        self.assertIn('data', response)  # Check if 'data' key is in the response
        self.assertIsInstance(response['data'], list)  # Ensure the list of cards

    def test_get_sets(self):
        response = get_sets()
        self.assertIn('data', response)  # Check if 'data' key is in the response
        self.assertIsInstance(response['data'], list)  # Ensure the list of sets

    def test_get_card_by_id(self):
        card_id = "xy7-54"  # Example card ID for testing
        response = get_card_by_id(card_id)
        self.assertIn('data', response)  # Check if 'data' key is in the response
        self.assertIsInstance(response['data'], dict)  # Ensure individual card returned as dict

if __name__ == '__main__':
    unittest.main()