import unittest
from api import *

class JokeAPITestCase(unittest.TestCase):
    
    def test_get_joke(self):
        response = get_joke()
        self.assertIn('error', response)
        self.assertFalse(response['error'])

    def test_get_joke_info(self):
        response = get_joke_info()
        self.assertIn('error', response)
        self.assertFalse(response['error'])

    def test_get_joke_categories(self):
        response = get_joke_categories()
        self.assertIn('error', response)
        self.assertFalse(response['error'])

    def test_get_language_code(self):
        response = get_language_code("English")
        self.assertIn('error', response)
        self.assertFalse(response['error'])
        self.assertEqual(response['code'], 'en')

    def test_get_supported_languages(self):
        response = get_supported_languages()
        self.assertIn('defaultLanguage', response)

    def test_get_flags(self):
        response = get_flags()
        self.assertIn('error', response)
        self.assertFalse(response['error'])

    def test_get_formats(self):
        response = get_formats()
        self.assertIn('error', response)
        self.assertFalse(response['error'])

    def test_ping_jokeapi(self):
        response = ping_jokeapi()
        self.assertIn('ping', response)
        self.assertEqual(response['ping'], 'Pong!')

    def test_get_endpoints_info(self):
        response = get_endpoints_info()
        for endpoint in response:
            self.assertIn('name', endpoint)
        # If you want to assert something else, like no errors
        self.assertFalse(any('error' in endpoint and endpoint['error'] for endpoint in response))

if __name__ == '__main__':
    unittest.main()