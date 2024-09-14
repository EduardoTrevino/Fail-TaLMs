import unittest
from api import list_competitions

class TestSoccerDataAPI(unittest.TestCase):
    def test_list_competitions(self):
        response = list_competitions()
        self.assertIn("competitions", response)
        self.assertIsInstance(response["competitions"], list)

if __name__ == '__main__':
    unittest.main()