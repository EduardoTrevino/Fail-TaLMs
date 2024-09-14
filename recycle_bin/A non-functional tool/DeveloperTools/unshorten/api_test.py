import unittest
from api import unshorten_url

class TestUnshortenAPI(unittest.TestCase):

    def test_unshorten_url_success(self):
        short_url = "https://bit.ly/3DKWm5t"
        authorization_token = "your_valid_token_here"  # Replace with a valid token
        response = unshorten_url(short_url, authorization_token)
        
        self.assertIn('success', response)
        self.assertTrue(response['success'])
        self.assertIn('unshortened_url', response)
        self.assertEqual(response['shortened_url'], short_url)

    def test_unshorten_url_invalid_token(self):
        short_url = "https://bit.ly/3DKWm5t"
        authorization_token = "invalid_token"  # Intentionally invalid token
        response = unshorten_url(short_url, authorization_token)
        
        self.assertIn('error', response)

    def test_unshorten_url_missing_token(self):
        short_url = "https://bit.ly/3DKWm5t"
        response = unshorten_url(short_url)
        
        self.assertIn('error', response)

if __name__ == '__main__':
    unittest.main()