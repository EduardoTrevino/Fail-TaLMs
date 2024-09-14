import unittest
import api

class TestAPI(unittest.TestCase):

    def test_get_random_joke(self):
        result = api.get_random_joke()
        self.assertIn("setup", result, "Failed to get a random joke")
        self.assertIn("punchline", result, "Failed to get a random joke")

    def test_get_joke_types(self):
        result = api.get_joke_types()
        self.assertIsInstance(result, list, "Failed to get joke types")
        self.assertGreater(len(result), 0, "Failed to get joke types")

    def test_get_ten_random_jokes(self):
        result = api.get_ten_random_jokes()
        self.assertIsInstance(result, list, "Failed to get ten random jokes")
        self.assertEqual(len(result), 10, "Failed to get ten random jokes")

    def test_get_random_jokes(self):
        number = 5
        result = api.get_random_jokes(number)
        self.assertIsInstance(result, list, "Failed to get the specified number of random jokes")
        self.assertEqual(len(result), number, "Failed to get the specified number of random jokes")

    def test_get_jokes_by_type(self):
        joke_type = "programming"
        result = api.get_jokes_by_type(joke_type, "random")
        self.assertIsInstance(result, list, "Failed to get jokes by type")
        self.assertGreater(len(result), 0, "Failed to get jokes by type")

    def test_get_joke_by_id(self):
        joke_id = 1
        result = api.get_joke_by_id(joke_id)
        self.assertIn("setup", result, "Failed to get a joke by ID")
        self.assertIn("punchline", result, "Failed to get a joke by ID")

if __name__ == '__main__':
    unittest.main()
