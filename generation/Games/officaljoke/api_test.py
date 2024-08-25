import unittest
from api import (
    grab_random_joke, grab_random_joke_v2, get_joke_types, grab_ten_random_jokes, 
    grab_ten_random_jokes_v2, grab_any_number_of_random_jokes, grab_jokes_by_type, grab_joke_by_id
)


class TestOfficialJokeAPI(unittest.TestCase):

    def test_grab_random_joke(self):
        response = grab_random_joke()
        self.assertIn('setup', response)
        self.assertIn('punchline', response)

    def test_grab_random_joke_v2(self):
        response = grab_random_joke_v2()
        self.assertIn('setup', response)
        self.assertIn('punchline', response)

    def test_get_joke_types(self):
        types = get_joke_types()
        self.assertIsInstance(types, list)

    def test_grab_ten_random_jokes(self):
        jokes = grab_ten_random_jokes()
        self.assertEqual(len(jokes), 10)

    def test_grab_ten_random_jokes_v2(self):
        jokes = grab_ten_random_jokes_v2()
        self.assertEqual(len(jokes), 10)

    def test_grab_any_number_of_random_jokes(self):
        jokes = grab_any_number_of_random_jokes(5)
        self.assertEqual(len(jokes), 5)

    def test_grab_jokes_by_type(self):
        jokes = grab_jokes_by_type('programming', 5)
        self.assertGreaterEqual(len(jokes), 1)
        self.assertTrue(all(joke['type'] == 'programming' for joke in jokes))

    def test_grab_joke_by_id(self):
        joke = grab_joke_by_id(1)
        self.assertIn('setup', joke)
        self.assertIn('punchline', joke)


if __name__ == '__main__':
    unittest.main()