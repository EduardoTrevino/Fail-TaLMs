import unittest
from api import get_boards, get_threads, get_catalog, get_archive, get_thread, get_page

class Test4ChanAPI(unittest.TestCase):

    def test_get_boards(self):
        response = get_boards()
        self.assertIn('boards', response)

    def test_get_threads(self):
        response = get_threads('po')
        self.assertIsInstance(response, list)

    def test_get_catalog(self):
        response = get_catalog('po')
        self.assertIsInstance(response, list)

    def test_get_archive(self):
        response = get_archive('po')
        self.assertIsInstance(response, list)

    def test_get_thread(self):
        response = get_thread('po', 570368)
        self.assertIn('posts', response)

    def test_get_page(self):
        response = get_page('po', 1)
        self.assertIn('threads', response)

if __name__ == '__main__':
    unittest.main()