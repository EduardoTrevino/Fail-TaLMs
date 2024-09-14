import unittest
from api import get_favicon


class TestGoogleFaviconsAPI(unittest.TestCase):

    def test_get_favicon_default_size(self):
        # Test the retrieval of a favicon with the default size
        result = get_favicon(domain="dev.to")
        self.assertTrue(len(result) > 0)  # Assert that data is returned

    def test_get_favicon_specific_size(self):
        # Test the retrieval of a favicon with a specific size
        result = get_favicon(domain="dev.to", sz=128)
        self.assertTrue(len(result) > 0)  # Assert that data is returned

    def test_get_favicon_invalid_domain(self):
        # Test with an invalid domain, expecting fallback/favicon not found
        result = get_favicon(domain="invalid_domain_abc")
        self.assertTrue(len(result) > 0)  # Fallback icon data should be returned

    def test_get_favicon_invalid_size(self):
        # Test with an invalid size, expecting default size
        result = get_favicon(domain="dev.to", sz=512)
        self.assertTrue(len(result) > 0)  # Default size icon data should be returned


if __name__ == '__main__':
    unittest.main()