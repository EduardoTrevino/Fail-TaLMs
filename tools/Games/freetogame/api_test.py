import unittest
from api import list_games, game_details, games_by_category, games_by_platform, sorted_games, games_by_filters


class TestFreeToGameAPI(unittest.TestCase):

    def test_list_games(self):
        response = list_games()
        self.assertIsInstance(response, list)

    def test_game_details(self):
        response = game_details(452)
        self.assertIsInstance(response, dict)
        self.assertIn('id', response)

    def test_games_by_category(self):
        response = games_by_category('shooter')
        self.assertIsInstance(response, list)

    def test_games_by_platform(self):
        response = games_by_platform('pc')
        self.assertIsInstance(response, list)

    def test_sorted_games(self):
        response = sorted_games('alphabetical')
        self.assertIsInstance(response, list)

    def test_games_by_filters(self):
        response = games_by_filters(tag='3d', platform='pc')
        self.assertIsInstance(response, list)


if __name__ == '__main__':
    unittest.main()