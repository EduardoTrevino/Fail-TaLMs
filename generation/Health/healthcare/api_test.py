import unittest
from api import get_content_object, get_content_collection, get_content_index

class TestHealthCareAPI(unittest.TestCase):

    def test_get_content_object(self):
        result = get_content_object("accessibility")
        self.assertIn("url", result)

    def test_get_content_collection(self):
        result = get_content_collection("glossary")
        self.assertIn("glossary", result)

    def test_get_content_index(self):
        result = get_content_index()
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], dict)
        self.assertIn("tags", result[0])

if __name__ == "__main__":
    unittest.main()