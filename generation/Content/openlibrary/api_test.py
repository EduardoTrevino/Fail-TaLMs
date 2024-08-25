import unittest
from api import (
    openlibrary_search, works_by_id, editions_by_work, author_search, author_data, author_works, book_by_isbn
)


class TestOpenLibraryAPI(unittest.TestCase):

    def test_openlibrary_search(self):
        result = openlibrary_search(q="The Lord of the Rings")
        self.assertIn("docs", result)

    def test_works_by_id(self):
        result = works_by_id(work_id="OL45804W")
        self.assertIn("title", result)

    def test_editions_by_work(self):
        result = editions_by_work(work_id="OL45804W")
        self.assertIn("entries", result)

    def test_author_search(self):
        result = author_search(q="J. R. R. Tolkien")
        self.assertIn("docs", result)

    def test_author_data(self):
        result = author_data(author_id="OL23919A")
        self.assertIn("name", result)

    def test_author_works(self):
        result = author_works(author_id="OL23919A")
        self.assertIn("entries", result)

    def test_book_by_isbn(self):
        result = book_by_isbn(isbn="9780140328721")  # Using ISBN-13
        self.assertIn("title", result)


if __name__ == '__main__':
    unittest.main()