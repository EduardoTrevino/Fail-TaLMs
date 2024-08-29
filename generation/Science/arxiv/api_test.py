import unittest
from api import query_arxiv


class TestArxivAPI(unittest.TestCase):

    def test_query_with_search(self):
        result = query_arxiv(search_query="all:electron")
        self.assertIn("<feed", result)  # Check if it returns XML starting with <feed> tag

    def test_query_with_id_list(self):
        result = query_arxiv(id_list=["cs/9901002v1"])
        self.assertIn("<entry", result)  # Check for an <entry> element in the result

    def test_query_with_paging(self):
        result = query_arxiv(search_query="all:electron", start=10, max_results=5)
        self.assertIn("<feed", result)

    def test_query_with_sorting(self):
        result = query_arxiv(search_query="all:electron", sort_by="submittedDate", sort_order="ascending")
        self.assertIn("<feed", result)

    def test_invalid_query(self):
        result = query_arxiv(search_query="id_list=wrong")
        self.assertIn("<summary xmlns", result)  # Error messages are within <summary>