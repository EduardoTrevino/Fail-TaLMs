import unittest
from api import get_robohash_image


class TestRobohashAPI(unittest.TestCase):

    def test_default_image(self):
        # Test with only the required text parameter
        response = get_robohash_image(text="example")
        self.assertTrue(response, "Image should be returned")

    def test_custom_format(self):
        # Test with custom format
        response = get_robohash_image(text="example", fmt="jpg")
        self.assertTrue(response, "Image should be returned as jpg")

    def test_with_size(self):
        # Test with custom size
        response = get_robohash_image(text="example", size="300x300")
        self.assertTrue(response, "Image should be returned with specified size")

    def test_with_set(self):
        # Test with specific set
        response = get_robohash_image(text="example", set="set4")
        self.assertTrue(response, "Image should be returned from specified set")

    def test_with_bgset(self):
        # Test with background set
        response = get_robohash_image(text="example", bgset="bg1")
        self.assertTrue(response, "Image should be returned with specified background")

    def test_with_gravatar(self):
        # Test with gravatar option
        response = get_robohash_image(text="example", gravatar="yes")
        self.assertTrue(response, "Image should be gravatar if available")

    def test_ignoreext_false(self):
        # Test with ignoreext set to False
        response = get_robohash_image(text="example", ignoreext=False)
        self.assertTrue(response, "Image should be returned with the extension considered in the hash")


if __name__ == "__main__":
    unittest.main()