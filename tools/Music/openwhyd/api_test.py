import unittest
from api import *

class TestAPI(unittest.TestCase):

    def test_get_user_tracks(self):
        response = get_user_tracks(uHandle="adrien", format="json", limit=5)
        self.assertIsInstance(response, list)

    def test_get_hot_tracks(self):
        response = get_hot_tracks(format="json", limit=5)
        self.assertLessEqual(len(response), 5)

    def test_get_user_data(self):
        response = get_user_data(id="4d94501d1f78ac091dbc9b4d")
        self.assertIsInstance(response, dict)
        self.assertIn('_id', response)

    def test_get_playlist_data(self):
        response = get_playlist_data(id="4d94501d1f78ac091dbc9b4d_0")
        self.assertIsInstance(response, list)

    def test_list_followers(self):
        response = list_followers(id="4d94501d1f78ac091dbc9b4d")
        self.assertIsInstance(response, list)

    def test_list_following(self):
        response = list_following(id="4d94501d1f78ac091dbc9b4d")
        self.assertIsInstance(response, list)

if __name__ == "__main__":
    unittest.main()
