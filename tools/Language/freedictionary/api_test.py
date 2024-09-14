import unittest
from api import get_word_definition

class TestFreeDictionaryAPI(unittest.TestCase):

    def test_get_word_definition_valid(self):
        """
        Test fetching a valid word definition.
        """
        response = get_word_definition("hello")
        self.assertIsInstance(response, list)
        self.assertIn("word", response[0])
        self.assertEqual(response[0]["word"], "hello")

    def test_get_word_definition_invalid(self):
        """
        Test checking response for an invalid word.
        """
        response = get_word_definition("nonexistentwordthatisunlikely")
        self.assertTrue(any("title" in entry for entry in response))  # API should return a title for error

if __name__ == "__main__":
    unittest.main()