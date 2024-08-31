import unittest
from api import (
    get_all_cards, get_all_sets, get_set_by_code,
    get_all_types, get_all_subtypes,
    get_all_supertypes, get_all_formats, get_cards_by_name,
    get_cards_by_foreign_name
)

class TestAPI(unittest.TestCase):

    def test_get_all_cards(self):
        response = get_all_cards(page=1, page_size=2)
        self.assertIn('cards', response, "Cards key not in response")

    # def test_get_card_by_id(self):
    #     response = get_card_by_id("02ea5ddc89d7847abc77a0fbcbf2bc74e6456559")
    #     self.assertIn('card', response, "Card key not in response")
    #     self.assertEqual(response['card']['name'], 'Archangel Avacyn', "Card name does not match")

    def test_get_all_sets(self):
        response = get_all_sets()
        self.assertIn('sets', response, "Sets key not in response")

    def test_get_set_by_code(self):
        response = get_set_by_code("KTK")
        self.assertIn('set', response, "Set key not in response")
        self.assertEqual(response['set']['name'], 'Khans of Tarkir', "Set name does not match")

    # def test_generate_booster_pack(self):
    #     response = generate_booster_pack("KTK")
    #     self.assertIn('cards', response, "Cards key not in response")

    def test_get_all_types(self):
        response = get_all_types()
        self.assertIn('types', response, "Types key not in response")

    def test_get_all_subtypes(self):
        response = get_all_subtypes()
        self.assertIn('subtypes', response, "Subtypes key not in response")

    def test_get_all_supertypes(self):
        response = get_all_supertypes()
        self.assertIn('supertypes', response, "Supertypes key not in response")

    def test_get_all_formats(self):
        response = get_all_formats()
        self.assertIn('formats', response, "Formats key not in response")

    def test_get_cards_by_name(self):
        response = get_cards_by_name("Archangel Avacyn")
        self.assertIn('cards', response, "Cards key not in response")

    def test_get_cards_by_foreign_name(self):
        response = get_cards_by_foreign_name(name="Arcángel Avacyn", language="Spanish")
        self.assertIn('cards', response, "Cards key not in response")

if __name__ == '__main__':
    unittest.main()
