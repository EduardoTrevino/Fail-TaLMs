import unittest
from api import get_amiibos, get_amiibo_type, get_game_series, get_amiibo_series, get_character, get_last_updated

class TestAmiiboAPI(unittest.TestCase):

    def test_get_amiibos(self):
        result = get_amiibos()
        self.assertIn("amiibo", result)

    def test_get_amiibo_type_by_key(self):
        result = get_amiibo_type(key='0x00')
        self.assertIn("amiibo", result)

    def test_get_game_series_by_key(self):
        result = get_game_series(key='0x000')
        self.assertIn("amiibo", result)

    def test_get_amiibo_series_by_key(self):
        result = get_amiibo_series(key='0x06')
        self.assertIn("amiibo", result)

    def test_get_character_by_key(self):
        result = get_character(key='0x1996')
        self.assertIn("amiibo", result)

    def test_get_last_updated(self):
        result = get_last_updated()
        self.assertIn("lastUpdated", result)

if __name__ == '__main__':
    unittest.main()