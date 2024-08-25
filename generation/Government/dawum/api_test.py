import unittest
from api import get_database, get_last_update

class TestDawumAPI(unittest.TestCase):

    def test_get_database(self):
        """
        Test fetching the entire election polls database to ensure the API endpoint is working.
        """
        data = get_database()
        self.assertIsInstance(data, dict)
        self.assertIn('Database', data)
        self.assertIn('Parliaments', data)

    def test_get_last_update(self):
        """
        Test fetching the last update date of the election polls database.
        """
        last_update = get_last_update()
        self.assertIsInstance(last_update, str)
        self.assertRegex(last_update, r"\d{4}-\d{2}-\d{2}")  # Check if the string is a date

if __name__ == "__main__":
    unittest.main()