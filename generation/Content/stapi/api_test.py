import unittest
from api import (
    get_animal, search_animals,
    get_book, search_books,
    get_character, search_characters,
    get_data_version,
    get_episode, search_episodes
)


class TestStapiEndpoints(unittest.TestCase):

    def test_get_animal(self):
        uid = "example_uid"
        response = get_animal(uid)
        self.assertIn("animal", response)

    def test_search_animals(self):
        response = search_animals()
        self.assertIn("animals", response)

    def test_get_book(self):
        uid = "example_uid"
        response = get_book(uid)
        self.assertIn("book", response)

    def test_search_books(self):
        response = search_books()
        self.assertIn("books", response)

    def test_get_character(self):
        uid = "example_uid"
        response = get_character(uid)
        self.assertIn("character", response)

    def test_search_characters(self):
        response = search_characters()
        self.assertIn("characters", response)

    def test_get_data_version(self):
        response = get_data_version()
        self.assertIn("dataVersion", response)

    def test_get_episode(self):
        uid = "example_uid"
        response = get_episode(uid)
        self.assertIn("episode", response)

    def test_search_episodes(self):
        response = search_episodes()
        self.assertIn("episodes", response)


if __name__ == '__main__':
    unittest.main()