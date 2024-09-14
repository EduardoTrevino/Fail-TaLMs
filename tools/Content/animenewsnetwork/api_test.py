import unittest
from api import get_reports, get_anime_details

class TestAnimeNewsNetworkAPI(unittest.TestCase):

    def test_get_reports_default(self):
        result = get_reports()
        self.assertIsInstance(result, bytes)

    def test_get_reports_anime_type(self):
        result = get_reports(type="anime")
        self.assertIsInstance(result, bytes)

    def test_get_reports_name_filter(self):
        result = get_reports(name="Z")
        self.assertIsInstance(result, bytes)

    def test_get_anime_details_by_id(self):
        result = get_anime_details(anime='4658')
        self.assertIsInstance(result, bytes)

    def test_get_anime_details_by_title(self):
        result = get_anime_details(title='~jinki')
        self.assertIsInstance(result, bytes)

if __name__ == '__main__':
    unittest.main()