import unittest
from api import get_genres, get_stories

class TestBinaryJazzAPI(unittest.TestCase):

    def test_get_single_genre(self):
        """Test fetching a single genre"""
        result = get_genres(1)
        self.assertNotIn("error", result)

    def test_get_multiple_genres(self):
        """Test fetching multiple genres"""
        count = 5
        result = get_genres(count)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), count)

    def test_get_single_story(self):
        """Test fetching a single story"""
        result = get_stories(1)

    def test_get_multiple_stories(self):
        """Test fetching multiple stories"""
        count = 3
        result = get_stories(count)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), count)

if __name__ == '__main__':
    unittest.main()