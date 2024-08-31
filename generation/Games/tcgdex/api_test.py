import unittest
from api import (
    get_card, search_cards, get_set, search_sets, get_series, search_series,
    list_categories, list_illustrators, list_rarities,
    list_retreats, list_types
)

class TestTCGdexAPI(unittest.TestCase):

    def test_get_card(self):
        response = get_card('swsh3-136')
        self.assertIn('name', response)
        self.assertEqual(response['name'], "Furret")

    def test_search_cards(self):
        response = search_cards(name='Alakazam')
        self.assertIsInstance(response, list)
        if response:
            self.assertIn('name', response[0])
            self.assertEqual(response[0]['name'], "Alakazam")

    def test_get_set(self):
        response = get_set('swsh3')
        self.assertIn('name', response)
        self.assertEqual(response['name'], "Darkness Ablaze")

    def test_search_sets(self):
        response = search_sets()
        self.assertIsInstance(response, list)
        if response:
            self.assertIn('name', response[0])

    def test_get_series(self):
        response = get_series('swsh')
        self.assertIn('name', response)
        self.assertEqual(response['name'], "Sword & Shield")

    def test_search_series(self):
        response = search_series()
        self.assertIsInstance(response, list)
        if response:
            self.assertIn('name', response[0])

    def test_list_categories(self):
        response = list_categories()
        self.assertIsInstance(response, list)

    def test_list_illustrators(self):
        response = list_illustrators()
        self.assertIsInstance(response, list)

    def test_list_rarities(self):
        response = list_rarities()
        self.assertIsInstance(response, list)

    def test_list_retreats(self):
        response = list_retreats()
        self.assertIsInstance(response, list)

    def test_list_types(self):
        response = list_types()
        self.assertIsInstance(response, list)

if __name__ == '__main__':
    unittest.main()