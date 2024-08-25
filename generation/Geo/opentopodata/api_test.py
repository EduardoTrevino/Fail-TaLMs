import unittest
from api import get_elevation, get_health, get_datasets

class TestOpenTopoDataAPI(unittest.TestCase):

    def test_get_elevation(self):
        response = get_elevation(dataset_name="test-dataset", locations="56,123")
        self.assertEqual(response['status'], "OK")
        self.assertIn('results', response)
        self.assertIsInstance(response['results'], list)

    def test_get_health(self):
        response = get_health()
        self.assertEqual(response['status'], "OK")

    def test_get_datasets(self):
        response = get_datasets()
        self.assertEqual(response['status'], "OK")
        self.assertIn('results', response)
        self.assertIsInstance(response['results'], list)

if __name__ == '__main__':
    unittest.main()