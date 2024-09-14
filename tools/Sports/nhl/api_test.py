import unittest
from api import *

class TestNHLApi(unittest.TestCase):

    def test_get_player_spotlight(self):
        response = get_player_spotlight()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertNotIn('error', response)

    def test_get_standings(self):
        response = get_standings('2023-11-08')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertNotIn('error', response)

    def test_get_standings_season(self):
        response = get_standings_season()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertNotIn('error', response)

    def test_get_player_game_log(self):
        response = get_player_game_log(8476453, 20232024, 2)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertNotIn('error', response)

    def test_get_player_landing(self):
        response = get_player_landing(8476453)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertNotIn('error', response)

    def test_get_score(self):
        response = get_score('2023-11-08')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertNotIn('error', response)

    def test_get_location(self):
        response = get_location()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertNotIn('error', response)

    def test_get_schedule(self):
        response = get_schedule('2023-11-08')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertNotIn('error', response)

    def test_get_schedule_calendar(self):
        response = get_schedule_calendar('2023-11-08')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertNotIn('error', response)

if __name__ == '__main__':
    unittest.main()