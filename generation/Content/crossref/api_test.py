import unittest
from api import search_works, get_funders, get_funder_details, list_journals, get_journal_details, get_works_by_journal

class TestCrossrefAPI(unittest.TestCase):

    def test_search_works(self):
        result = search_works("machine learning")
        self.assertIsInstance(result, dict)
        self.assertIn('status', result)

    def test_get_funders(self):
        result = get_funders(query="research foundation")
        self.assertIsInstance(result, dict)
        self.assertIn('status', result)

    def test_get_funder_details(self):
        result = get_funder_details("501100006004")
        self.assertIsInstance(result, dict)
        self.assertIn('status', result)

    def test_list_journals(self):
        result = list_journals(query="pharmacy health")
        self.assertIsInstance(result, dict)
        self.assertIn('status', result)

    def test_get_journal_details(self):
        result = get_journal_details("03064530")
        self.assertIsInstance(result, dict)
        self.assertIn('status', result)

    def test_get_works_by_journal(self):
        result = get_works_by_journal("03064530", query="neuroscience")
        self.assertIsInstance(result, dict)
        self.assertIn('status', result)

if __name__ == '__main__':
    unittest.main()