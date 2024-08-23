import unittest
import api  # Import the api module

class TestDicebearAPI(unittest.TestCase):

    def test_get_avatar_default(self):
        # Test getting a default SVG avatar with no options
        response = api.get_avatar('bottts')
        self.assertTrue(response.startswith(b'<?xml'), "The response should be an SVG image.")

    def test_get_avatar_with_seed(self):
        # Test getting an avatar with a specific seed
        response = api.get_avatar('pixel-art', seed='John')
        self.assertTrue(response.startswith(b'<?xml'), "The response should be an SVG image.")

    def test_get_avatar_with_hair_options(self):
        # Test getting a pixel-art avatar with specific hair options
        response = api.get_avatar('pixel-art', hair=['short01', 'short02'])
        self.assertTrue(response.startswith(b'<?xml'), "The response should be an SVG image.")

    def test_get_avatar_with_flip_option(self):
        # Test getting an avatar with the flip option enabled
        response = api.get_avatar('lorelei', flip=True)
        self.assertTrue(response.startswith(b'<?xml'), "The response should be an SVG image.")

# Run the test cases
if __name__ == '__main__':
    unittest.main()