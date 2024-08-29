import unittest
from api import *

class TestOpenLibraryAPI(unittest.TestCase):
    
    def test_search_books(self):
        response = search_books(q="harry potter")
        self.assertIn('docs', response)
        self.assertGreater(len(response['docs']), 0)

    def test_get_work_by_id(self):
        response = get_work_by_id(work_id="OL45804W")
        self.assertIn('title', response)
        self.assertEqual(response['key'], "/works/OL45804W")

    def test_get_edition_by_id(self):
        response = get_edition_by_id(edition_id="OL7353617M")
        self.assertIn('title', response)
        self.assertEqual(response['key'], "/books/OL7353617M")

    def test_get_author_by_id(self):
        response = get_author_by_id(author_id="OL23919A")
        self.assertIn('name', response)
        self.assertEqual(response['key'], "/authors/OL23919A")

    def test_search_authors(self):
        response = search_authors(q="j.k. rowling")
        self.assertIn('docs', response)
        self.assertGreater(len(response['docs']), 0)

    def test_get_subject_works(self):
        response = get_subject_works(subject_name="love")
        self.assertIn('works', response)
        self.assertGreater(len(response['works']), 0)

    def test_get_book_cover(self):
        url = get_book_cover(key="isbn", value="0385472579", size="S")
        self.assertIsNotNone(url)
        self.assertTrue(url.startswith("https://covers.openlibrary.org/"))

    def test_recent_changes(self):
        response = recent_changes(limit=5)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

if __name__ == "__main__":
    unittest.main()
