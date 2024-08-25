import unittest
from api import shorten_url


class TestIsGdAPI(unittest.TestCase):

    def test_shorten_url_simple_success(self):
        long_url = "https://www.example.com"
        response = shorten_url(url=long_url, format='simple')
        self.assertTrue(response.startswith("https://"))

    def test_shorten_url_json_success(self):
        long_url = "https://www.example.com"
        response = shorten_url(url=long_url, format='json')
        self.assertIn("shorturl", response)

    def test_shorten_url_custom_shorturl(self):
        long_url = "https://www.example.com"
        custom_short = "myexample"
        response = shorten_url(url=long_url, format='simple', shorturl=custom_short)
        self.assertTrue("Error:" in response or response.startswith("https://is.gd/"))

    def test_shorten_url_with_logstats(self):
        long_url = "https://www.example.com"
        response = shorten_url(url=long_url, format='simple', logstats=1)
        self.assertTrue(response.startswith("https://"))

    def test_shorten_url_with_callback(self):
        long_url = "https://www.example.com"
        response = shorten_url(url=long_url, format='json', callback='myFunction')
        self.assertTrue(response.startswith("myFunction("))


if __name__ == "__main__":
    unittest.main()