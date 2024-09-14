import unittest
from api import get_all_resources, get_ability_score, get_alignment, get_background, get_class, get_condition, get_damage_type, get_equipment

class TestDnD5API(unittest.TestCase):

    def test_get_all_resources(self):
        # Test retrieving all resources for the 'classes' endpoint
        response = get_all_resources('classes')
        self.assertIsInstance(response, dict)
        self.assertIn('results', response)

    def test_get_ability_score(self):
        # Test retrieving an ability score by index
        response = get_ability_score('cha')
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get('index'), 'cha')

    def test_get_alignment(self):
        # Test retrieving an alignment by index
        response = get_alignment('neutral-good')
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get('index'), 'neutral-good')

    def test_get_background(self):
        # Test retrieving a background by index
        response = get_background('acolyte')
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get('index'), 'acolyte')

    def test_get_class(self):
        # Test retrieving a class by index
        response = get_class('wizard')
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get('index'), 'wizard')

    def test_get_condition(self):
        # Test retrieving a condition by index
        response = get_condition('blinded')
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get('index'), 'blinded')

    def test_get_damage_type(self):
        # Test retrieving a damage type by index
        response = get_damage_type('fire')
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get('index'), 'fire')

    def test_get_equipment(self):
        # Test retrieving equipment by index
        response = get_equipment('club')
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get('index'), 'club')


if __name__ == '__main__':
    unittest.main()