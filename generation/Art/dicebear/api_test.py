import unittest
from api import generate_avatar

class TestDicebearAPI(unittest.TestCase):

    def test_generate_avatar_with_default(self):
        # Test with default parameters
        result = generate_avatar(style_name='pixel-art')
        self.assertIsInstance(result, bytes)

    def test_generate_avatar_with_seed(self):
        # Test with a specific seed
        result = generate_avatar(style_name='lorelei', seed='John')
        self.assertIsInstance(result, bytes)

    def test_generate_avatar_with_hair_options(self):
        # Test with hair options
        result = generate_avatar(style_name='pixel-art', hair=['short01', 'short02'])
        self.assertIsInstance(result, bytes)

    def test_generate_avatar_with_flip(self):
        # Test with flip option
        result = generate_avatar(style_name='lorelei', flip=True)
        self.assertIsInstance(result, bytes)

    def test_generate_avatar_in_different_format(self):
        # Test generating avatar in JSON format
        result = generate_avatar(style_name='pixel-art', format='json')
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()