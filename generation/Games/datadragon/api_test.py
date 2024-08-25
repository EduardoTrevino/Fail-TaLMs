import unittest
from api import get_latest_version, get_champion_data, get_item_data, get_rune_data, get_language_data

class TestDataDragonAPI(unittest.TestCase):

    def test_get_latest_version(self):
        response = get_latest_version()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    def test_get_champion_data(self):
        latest_version = get_latest_version()[0]
        response = get_champion_data(version=latest_version)
        self.assertIsInstance(response, dict)
        self.assertIn("data", response)

    def test_get_item_data(self):
        latest_version = get_latest_version()[0]
        response = get_item_data(version=latest_version)
        self.assertIsInstance(response, dict)
        self.assertIn("data", response)
    
    def test_get_rune_data(self):
        latest_version = get_latest_version()[0]
        response = get_rune_data(version=latest_version)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    def test_get_language_data(self):
        response = get_language_data()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

if __name__ == '__main__':
    unittest.main()