import unittest
from api import get_content_object, get_content_collection, get_content_index


class TestHealthcareAPI(unittest.TestCase):

    def test_get_content_object(self):
        result = get_content_object('accessibility')
        self.assertIn('url', result)
        self.assertIn('title', result)

    def test_get_content_collection(self):
        result = get_content_collection('glossary')
        self.assertIn('glossary', result)

    def test_get_content_index(self):
        result = get_content_index()
        self.assertIsInstance(result, list)
        if result:
            self.assertIn('tags', result[0])
            self.assertIn('title', result[0])


if __name__ == '__main__':
    unittest.main()