import unittest
from api import generate_insult


class TestEvilInsultGeneratorAPI(unittest.TestCase):

    def test_generate_insult_default(self):
        """Test generate_insult with default parameters."""
        response = generate_insult()
        self.assertIsInstance(response, dict, "Expected response to be a dict when type is 'json'")
        self.assertIn('insult', response, "Response JSON should contain 'insult' key")

    def test_generate_insult_text(self):
        """Test generate_insult with type text."""
        response = generate_insult(type='text')
        self.assertIsInstance(response, str, "Expected response to be a string when type is 'text'")

    def test_generate_insult_with_lang(self):
        """Test generate_insult with a specific language."""
        response = generate_insult(lang='de', type='json')
        self.assertIsInstance(response, dict, "Expected response to be a dict for type 'json' and lang 'de'")
        self.assertIn('insult', response, "Response JSON should contain 'insult' key")
    

if __name__ == '__main__':
    unittest.main()