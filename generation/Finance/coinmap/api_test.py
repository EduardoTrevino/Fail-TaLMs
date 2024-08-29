import unittest
from api import get_venues, get_venue, get_comments, get_rating, get_atm_operators, get_coins

class TestCoinmapAPI(unittest.TestCase):

    def test_get_venues(self):
        response = get_venues()
        self.assertIn('venues', response)

    def test_get_venue(self):
        venue_id = 1  # Example ID, replace with a valid ID
        response = get_venue(venue_id)
        self.assertIn('venue', response)

    def test_get_comments(self):
        venue_id = 1  # Example ID, replace with a valid ID
        response = get_comments(venue_id)
        self.assertIn('comments', response)

    def test_get_rating(self):
        venue_id = 1  # Example ID, replace with a valid ID
        response = get_rating(venue_id)
        self.assertIn('rating', response)

    def test_get_atm_operators(self):
        response = get_atm_operators()
        self.assertIn('operators', response)

    def test_get_coins(self):
        response = get_coins()
        self.assertIn('coins', response)
        
if __name__ == '__main__':
    unittest.main()