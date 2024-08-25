import unittest
from api import *

class TestTvMazeAPI(unittest.TestCase):

    def test_search_shows(self):
        result = search_shows(query='girls')
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_show_single_search(self):
        result = show_single_search(query='girls')
        self.assertIsInstance(result, dict)
        self.assertIn('name', result)

    def test_show_lookup(self):
        result = show_lookup(imdb_id='tt0944947')
        self.assertIsInstance(result, dict)
        self.assertIn('id', result)

    def test_search_people(self):
        result = search_people(query='lauren')
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_schedule(self):
        result = schedule()
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_web_schedule(self):
        result = web_schedule()
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_show_main_information(self):
        result = show_main_information(show_id=1)
        self.assertIsInstance(result, dict)
        self.assertIn('name', result)

    def test_show_episode_list(self):
        result = show_episode_list(show_id=1)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_show_seasons(self):
        result = show_seasons(show_id=1)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_season_episodes(self):
        result = season_episodes(season_id=1)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_person_main_information(self):
        result = person_main_information(person_id=1)
        self.assertIsInstance(result, dict)
        self.assertIn('id', result)

    def test_person_cast_credits(self):
        result = person_cast_credits(person_id=1)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_person_crew_credits(self):
        result = person_crew_credits(person_id=1)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_updates_shows(self):
        result = updates_shows()
        self.assertIsInstance(result, dict)

    def test_updates_people(self):
        result = updates_people()
        self.assertIsInstance(result, dict)

if __name__ == "__main__":
    unittest.main()