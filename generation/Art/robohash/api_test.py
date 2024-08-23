import unittest
import api

class TestRoboHashAPI(unittest.TestCase):

    def test_generate_image_default(self):
        response = api.generate_image(text="example")
        self.assertIsInstance(response, bytes)
        self.assertTrue(len(response) > 0)

    def test_generate_image_with_format(self):
        response = api.generate_image(text="example", format="jpg")
        self.assertIsInstance(response, bytes)
        self.assertTrue(len(response) > 0)

    def test_generate_image_with_set(self):
        response = api.generate_image(text="example", set="set2")
        self.assertIsInstance(response, bytes)
        self.assertTrue(len(response) > 0)

    def test_generate_image_with_size(self):
        response = api.generate_image(text="example", size="300x300")
        self.assertIsInstance(response, bytes)
        self.assertTrue(len(response) > 0)

    def test_generate_image_with_bgset(self):
        response = api.generate_image(text="example", bgset="bg1")
        self.assertIsInstance(response, bytes)
        self.assertTrue(len(response) > 0)

    def test_generate_image_with_gravatar(self):
        response = api.generate_image(text="example@example.com", gravatar="yes")
        self.assertIsInstance(response, bytes)
        self.assertTrue(len(response) > 0)

    def test_generate_image_with_ignoreext(self):
        response = api.generate_image(text="example.png", ignoreext=True)
        self.assertIsInstance(response, bytes)
        self.assertTrue(len(response) > 0)

if __name__ == '__main__':
    unittest.main()