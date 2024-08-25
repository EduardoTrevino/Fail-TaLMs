import unittest
from api import get_random_affirmation

class TestAffirmationsAPI(unittest.TestCase):

    def test_get_random_affirmation(self):
        result = get_random_affirmation()
        self.assertIn("affirmation", result)
        self.assertIsInstance(result["affirmation"], str)

if __name__ == '__main__':
    unittest.main()