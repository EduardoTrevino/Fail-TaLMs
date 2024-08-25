import unittest
from api import (
    get_authors,
    get_author,
    search_author_quotes,
    get_languages,
    like_quote,
    search_quotes,
    create_quote,
    get_random_quote,
    get_quote,
    get_statistics
)

class TestDictumAPI(unittest.TestCase):
    
    def setUp(self):
        self.language = "en"
        self.author_id = "some-author-id"
        self.quote_id = "some-quote-id"
        self.text = "An inspiring quote"
        self.toolbench_rapidapi_key = "088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff"

    def test_get_authors(self):
        response = get_authors(self.language)
        self.assertIsInstance(response, list)

    def test_get_author(self):
        response = get_author(self.language, self.author_id)
        self.assertIsInstance(response, dict)

    def test_search_author_quotes(self):
        response = search_author_quotes(self.language, self.author_id)
        self.assertIsInstance(response, list)

    def test_get_languages(self):
        response = get_languages()
        self.assertIsInstance(response, list)

    def test_like_quote(self):
        response = like_quote(self.language, self.quote_id)
        self.assertIsInstance(response, dict)

    def test_search_quotes(self):
        response = search_quotes(self.language)
        self.assertIsInstance(response, list)

    def test_create_quote(self):
        response = create_quote(self.language, self.author_id, self.text)
        self.assertIsInstance(response, dict)

    def test_get_random_quote(self):
        response = get_random_quote(self.language)
        self.assertIsInstance(response, dict)

    def test_get_quote(self):
        response = get_quote(self.language, self.quote_id)
        self.assertIsInstance(response, dict)

    def test_get_statistics(self):
        response = get_statistics(self.language)
        self.assertIsInstance(response, dict)

if __name__ == '__main__':
    unittest.main()