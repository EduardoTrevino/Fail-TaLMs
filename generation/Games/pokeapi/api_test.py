import unittest
from api import get_berry, get_berry_firmness, get_berry_flavor, get_ability, get_pokemon, get_type


class TestPokeAPI(unittest.TestCase):

    def test_get_berry(self):
        response = get_berry()
        self.assertIn('name', response)
        self.assertEqual(response['name'], 'cheri')

    def test_get_berry_firmness(self):
        response = get_berry_firmness()
        self.assertIn('name', response)
        self.assertEqual(response['name'], 'very-soft')

    def test_get_berry_flavor(self):
        response = get_berry_flavor()
        self.assertIn('name', response)
        self.assertEqual(response['name'], 'spicy')

    def test_get_ability(self):
        response = get_ability()
        self.assertIn('name', response)
        self.assertEqual(response['name'], 'stench')

    def test_get_pokemon(self):
        response = get_pokemon()
        self.assertIn('name', response)
        self.assertEqual(response['name'], 'clefairy')

    def test_get_type(self):
        response = get_type()
        self.assertIn('name', response)
        self.assertEqual(response['name'], 'ground')


if __name__ == '__main__':
    unittest.main()