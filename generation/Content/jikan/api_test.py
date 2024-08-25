import unittest
from api import (get_anime_full_by_id, get_anime_by_id, get_anime_staff, 
                 get_anime_characters, get_anime_videos, get_anime_streaming, 
                 get_character_by_id, get_character_anime, get_character_pictures)


class TestJikanAPI(unittest.TestCase):

    def test_get_anime_full_by_id(self):
        response = get_anime_full_by_id(1)
        self.assertEqual(response['data']['mal_id'], 1)

    def test_get_anime_by_id(self):
        response = get_anime_by_id(1)
        self.assertEqual(response['data']['mal_id'], 1)

    def test_get_anime_staff(self):
        response = get_anime_staff(1)
        self.assertIn('data', response)

    def test_get_anime_characters(self):
        response = get_anime_characters(1)
        self.assertIn('data', response)

    def test_get_anime_videos(self):
        response = get_anime_videos(1)
        self.assertIn('data', response)

    def test_get_anime_streaming(self):
        response = get_anime_streaming(1)
        self.assertIn('data', response)

    def test_get_character_by_id(self):
        response = get_character_by_id(1)
        self.assertEqual(response['data']['mal_id'], 1)

    def test_get_character_anime(self):
        response = get_character_anime(1)
        self.assertIn('data', response)

    def test_get_character_pictures(self):
        response = get_character_pictures(1)
        self.assertIn('data', response)


if __name__ == '__main__':
    unittest.main()