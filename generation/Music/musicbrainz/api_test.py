import unittest
from api import artist_search, release_lookup, release_group_browse

class TestMusicBrainzAPI(unittest.TestCase):
    def test_artist_search(self):
        response = artist_search("The Beatles")
        self.assertIn('artists', response)
        self.assertGreater(len(response['artists']), 0)
    
    def test_release_lookup(self):
        # Using the MBID for "Abbey Road" by The Beatles
        mbid = "eab8e3bc-b3fe-4ff4-84ee-e9066a1a1e46"
        response = release_lookup(mbid, inc="artists")
        self.assertIn('release', response)
        self.assertEqual(response['id'], mbid)
    
    def test_release_group_browse(self):
        # Using the MBID for The Beatles
        artist_mbid = "b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d"
        response = release_group_browse(artist_mbid, limit=5)
        self.assertIn('release-groups', response)
        self.assertGreater(len(response['release-groups']), 0)

if __name__ == '__main__':
    unittest.main()