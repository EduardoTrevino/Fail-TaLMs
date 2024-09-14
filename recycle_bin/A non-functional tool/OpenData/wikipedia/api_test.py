import unittest
from api import *

class TestWikipediaAPI(unittest.TestCase):

    def test_get_category_metrics(self):
        response = get_category_metrics('example-category', '2022-01-01', '2022-02-01')
        self.assertIn('data', response)

    def test_get_edits_per_category(self):
        response = get_edits_per_category('example-category', 'inclusive', 'all-editor-types', '2022-01-01', '2022-02-01')
        self.assertIn('data', response)

    def test_get_pageviews_per_category(self):
        response = get_pageviews_per_category('example-category', 'inclusive', 'en.wikipedia', '2022-01-01', '2022-02-01')
        self.assertIn('data', response)

    def test_get_top_edited_categories(self):
        response = get_top_edited_categories('inclusive', 'all-editor-types', 2023, 1)
        self.assertIn('data', response)

    def test_get_top_viewed_categories(self):
        response = get_top_viewed_categories('inclusive', 'en.wikipedia', 2023, 1)
        self.assertIn('data', response)

    def test_get_top_pages_per_category(self):
        response = get_top_pages_per_category('example-category', 'inclusive', 'en.wikipedia', 2023, 1)
        self.assertIn('data', response)

    def test_get_unique_devices(self):
        response = get_unique_devices('en.wikipedia', 'desktop', 'daily', '20230101', '20230131')
        self.assertIn('data', response)

    def test_get_edits_aggregate(self):
        response = get_edits_aggregate('en.wikipedia', 'anonymous', 'all-page-types', 'daily', '20230101', '20230131')
        self.assertIn('data', response)

    def test_get_pageviews_aggregate(self):
        response = get_pageviews_aggregate('en.wikipedia', 'all-access', 'all-agents', 'daily', '20230101', '20230131')
        self.assertIn('data', response)

if __name__ == '__main__':
    unittest.main()