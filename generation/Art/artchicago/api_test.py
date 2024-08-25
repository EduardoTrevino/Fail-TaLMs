import unittest
from api import *

class TestArtChicagoAPI(unittest.TestCase):
    def test_artworks(self):
        response = artworks()
        self.assertIn('data', response)

    def test_artworks_search(self):
        response = artworks_search(q="monet")
        self.assertIn('data', response)
        
    def test_artwork_by_id(self):
        response = artwork_by_id(4)
        self.assertIn('data', response)
        
    def test_artwork_manifest(self):
        response = artwork_manifest(4)
        self.assertIn('sequences', response)

    def test_agents(self):
        response = agents()
        self.assertIn('data', response)

    def test_agents_search(self):
        response = agents_search(q="john")
        self.assertIn('data', response)
        
    def test_agent_by_id(self):
        response = agent_by_id(2)
        self.assertIn('data', response)
        
    def test_places(self):
        response = places()
        self.assertIn('data', response)

    def test_places_search(self):
        response = places_search(q="chicago")
        self.assertIn('data', response)
        
    def test_place_by_id(self):
        response = place_by_id(1)
        self.assertIn('data', response)

# More test functions for other endpoints should follow the same pattern

if __name__ == '__main__':
    unittest.main()