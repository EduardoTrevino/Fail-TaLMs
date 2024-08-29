import unittest
from api import artist_search, release_lookup, release_group_browse

class TestMusicBrainzAPI(unittest.TestCase):
    def test_artist_search(self):
        response = artist_search("The Beatles")
        self.assertIn('artists', response)
        self.assertGreater(len(response['artists']), 0)
    
    def test_release_group_browse(self):
        # Using the MBID for The Beatles
        artist_mbid = "b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d"
        response = release_group_browse(artist_mbid, limit=5)
        self.assertIn('release-groups', response)
        self.assertGreater(len(response['release-groups']), 0)

if __name__ == '__main__':
    unittest.main()