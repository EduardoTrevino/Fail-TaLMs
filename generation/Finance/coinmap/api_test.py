import unittest
from api import get_venues, create_venue, get_venue, update_venue, delete_venue, get_comments, create_comment, get_rating, create_rating, get_atm_operators, get_coins, get_providers

class TestCoinmapAPI(unittest.TestCase):

    def test_get_venues(self):
        response = get_venues()
        self.assertIn('venues', response)

    def test_create_venue(self):
        # This test requires a venue object with minimal required fields.
        venue = {"name": "Test Venue", "location": {"lat": 0.0, "lon": 0.0}}
        response = create_venue(venue)
        self.assertIn('venue', response)

    def test_get_venue(self):
        venue_id = 1  # Example ID, replace with a valid ID
        response = get_venue(venue_id)
        self.assertIn('venue', response)

    def test_update_venue(self):
        venue_id = 1  # Example ID, replace with a valid ID
        venue = {"name": "Updated Venue"}
        response = update_venue(venue_id, venue)
        self.assertIn('venue', response)

    def test_delete_venue(self):
        venue_id = 1  # Example ID, replace with a valid ID
        response = delete_venue(venue_id)
        self.assertIn('status', response)

    def test_get_comments(self):
        venue_id = 1  # Example ID, replace with a valid ID
        response = get_comments(venue_id)
        self.assertIn('comments', response)

    def test_create_comment(self):
        venue_id = 1  # Example ID, replace with a valid ID
        response = create_comment(venue_id, "Test comment")
        self.assertIn('comments', response)

    def test_get_rating(self):
        venue_id = 1  # Example ID, replace with a valid ID
        response = get_rating(venue_id)
        self.assertIn('ratings', response)

    def test_create_rating(self):
        venue_id = 1  # Example ID, replace with a valid ID
        response = create_rating(venue_id, 1)
        self.assertIn('ratings', response)

    def test_get_atm_operators(self):
        response = get_atm_operators()
        self.assertIn('operators', response)

    def test_get_coins(self):
        response = get_coins()
        self.assertIn('coins', response)

    def test_get_providers(self):
        response = get_providers()
        self.assertIn('providers', response)

if __name__ == '__main__':
    unittest.main()