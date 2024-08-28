import unittest
from api import get_books, get_book, get_characters, get_character, get_houses, get_house


class TestIceAndFireAPI(unittest.TestCase):

    def test_get_books(self):
        response = get_books(page=1, page_size=2)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    def test_get_book(self):
        response = get_book(1)
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get("name"), "A Game of Thrones")

    def test_get_characters(self):
        response = get_characters(page=1, page_size=2)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    def test_get_character(self):
        response = get_character(583)
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get("name"), "Jon Snow")

    def test_get_houses(self):
        response = get_houses(page=1, page_size=2)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    def test_get_house(self):
        response = get_house(10)
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get("name"), "House Baelish of Harrenhal")


if __name__ == '__main__':
    unittest.main()