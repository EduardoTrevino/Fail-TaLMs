import unittest
from api import get_characters, get_character_by_id, get_locations, get_location_by_id, get_episodes, get_episode_by_id

class TestRickAndMortyAPI(unittest.TestCase):

    def test_get_characters(self):
        response = get_characters()
        self.assertIn('info', response)
        self.assertIn('results', response)

    def test_get_character_by_id(self):
        response = get_character_by_id(1)  # Rick Sanchez
        self.assertEqual(response['name'], "Rick Sanchez")

    def test_get_locations(self):
        response = get_locations()
        self.assertIn('info', response)
        self.assertIn('results', response)

    def test_get_location_by_id(self):
        response = get_location_by_id(1)  # Earth
        self.assertEqual(response['name'], "Earth")

    def test_get_episodes(self):
        response = get_episodes()
        self.assertIn('info', response)
        self.assertIn('results', response)

    def test_get_episode_by_id(self):
        response = get_episode_by_id(1)  # Pilot
        self.assertEqual(response['name'], "Pilot")

if __name__ == '__main__':
    unittest.main()