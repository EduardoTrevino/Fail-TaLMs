import unittest
from api import words, sug

class TestDatamuseAPI(unittest.TestCase):
    def test_words_standard_query(self):
        response = words(ml="ringing in the ears", max=3)
        self.assertIsInstance(response, list)
        self.assertTrue(len(response) > 0)
        self.assertTrue(all('word' in result for result in response))

    def test_words_with_relational_constraints(self):
        response = words(ml="spoon", sp="*a", max=3)
        self.assertIsInstance(response, list)
        self.assertTrue(len(response) > 0)

    def test_sug_autocomplete(self):
        response = sug(s="rawand", max=5)
        self.assertIsInstance(response, list)
        self.assertTrue(len(response) > 0)
        self.assertTrue(all('word' in result for result in response))

    def test_empty_query(self):
        response = words()
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 0)

    def test_invalid_s_query(self):
        response = sug(s="")
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 10)

if __name__ == "__main__":
    unittest.main()