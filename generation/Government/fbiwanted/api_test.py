import unittest
from api import get_wanted_list

class TestFBIWantedAPI(unittest.TestCase):

    def test_get_wanted_list_no_params(self):
        """Test fetching the wanted list with no parameters."""
        response = get_wanted_list()
        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)

    def test_get_wanted_list_with_field_offices(self):
        """Test fetching the wanted list filtered by field office."""
        response = get_wanted_list(field_offices="miami")
        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)

    def test_get_wanted_list_with_page(self):
        """Test fetching the wanted list with a specific page."""
        response = get_wanted_list(page=2)
        self.assertIn('page', response)
        self.assertEqual(response['page'], 2)

if __name__ == "__main__":
    unittest.main()