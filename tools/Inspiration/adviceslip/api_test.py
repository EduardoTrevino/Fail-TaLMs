import unittest
from api import get_random_advice, get_advice_by_id, search_advice


class TestAdviceSlipAPI(unittest.TestCase):

    def test_get_random_advice(self):
        # Test getting a random advice slip
        response = get_random_advice()
        self.assertIn('slip', response)
        self.assertIn('advice', response['slip'])

    def test_get_advice_by_id(self):
        # Test getting advice by a specific ID
        known_id = 1  # Example known slip ID; this ID should exist in their system
        response = get_advice_by_id(known_id)
        self.assertIn('slip', response)
        self.assertEqual(response['slip']['id'], known_id)

    def test_search_advice(self):
        # Test searching advice by a query
        query = "life"
        response = search_advice(query)
        self.assertIn('total_results', response)
        self.assertIn('slips', response)
        self.assertIsInstance(response['slips'], list)


if __name__ == '__main__':
    unittest.main()