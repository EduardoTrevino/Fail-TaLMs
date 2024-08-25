import unittest
from api import (
    get_item,
    get_user,
    get_max_item,
    get_top_stories,
    get_new_stories,
    get_best_stories,
    get_ask_stories,
    get_show_stories,
    get_job_stories,
    get_updates,
)


class TestHackerNewsAPI(unittest.TestCase):

    def test_get_item(self):
        result = get_item(8863)
        self.assertIn("id", result)
        self.assertEqual(result["id"], 8863)

    def test_get_user(self):
        result = get_user("jl")
        self.assertIn("id", result)
        self.assertEqual(result["id"], "jl")

    def test_get_max_item(self):
        result = get_max_item()
        self.assertIsInstance(result, int)

    def test_get_top_stories(self):
        result = get_top_stories()
        self.assertIsInstance(result, list)

    def test_get_new_stories(self):
        result = get_new_stories()
        self.assertIsInstance(result, list)

    def test_get_best_stories(self):
        result = get_best_stories()
        self.assertIsInstance(result, list)

    def test_get_ask_stories(self):
        result = get_ask_stories()
        self.assertIsInstance(result, list)

    def test_get_show_stories(self):
        result = get_show_stories()
        self.assertIsInstance(result, list)

    def test_get_job_stories(self):
        result = get_job_stories()
        self.assertIsInstance(result, list)

    def test_get_updates(self):
        result = get_updates()
        self.assertIn("items", result)
        self.assertIn("profiles", result)


if __name__ == '__main__':
    unittest.main()