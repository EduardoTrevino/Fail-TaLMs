import unittest
from api import *

class TestOpenBreweryAPI(unittest.TestCase):
    
    def test_get_brewery_by_id(self):
        response = get_brewery_by_id('bnaf9f')
        self.assertIn('id', response)
    
    def test_list_breweries(self):
        response = list_breweries()
        self.assertIsInstance(response, list)
    
    def test_get_random_brewery(self):
        response = get_random_brewery()
        self.assertIsInstance(response, list)
    
    def test_search_breweries(self):
        response = search_breweries('ale')
        self.assertIsInstance(response, list)
    
    def test_autocomplete_breweries(self):
        response = autocomplete_breweries('dog')
        self.assertIsInstance(response, list)
    
    def test_get_breweries_metadata(self):
        response = get_breweries_metadata()
        self.assertIsInstance(response, dict)

if __name__ == '__main__':
    unittest.main()