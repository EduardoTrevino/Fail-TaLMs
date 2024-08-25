import unittest
from api import get_random_kanye_quote

class TestKanyeAPI(unittest.TestCase):
    def test_get_random_kanye_quote(self):
        response = get_random_kanye_quote()
        self.assertIn('quote', response, "Response should contain a 'quote' key.")
        self.assertIsInstance(response['quote'], str, "The 'quote' value should be a string.")

if __name__ == '__main__':
    unittest.main()