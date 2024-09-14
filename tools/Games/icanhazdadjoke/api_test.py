import unittest
from api import fetch_random_joke, fetch_random_slack_joke, fetch_joke_by_id, search_jokes


class TestIcanhazdadjokeAPI(unittest.TestCase):

    def test_fetch_random_joke_json(self):
        result = fetch_random_joke(accept="application/json")
        self.assertIn("joke", result)
        self.assertEqual(result["status"], 200)

    def test_fetch_random_joke_text(self):
        result = fetch_random_joke(accept="text/plain")
        self.assertIn("joke", result)
        self.assertEqual(result["status"], 200)

    def test_fetch_random_slack_joke(self):
        result = fetch_random_slack_joke()
        self.assertIn("attachments", result)

    def test_fetch_joke_by_id(self):
        result = fetch_joke_by_id("R7UfaahVfFd", accept="application/json")
        self.assertEqual(result["id"], "R7UfaahVfFd")

    def test_search_jokes(self):
        result = search_jokes(term="hipster")
        self.assertGreater(len(result["results"]), 0)


if __name__ == '__main__':
    unittest.main()