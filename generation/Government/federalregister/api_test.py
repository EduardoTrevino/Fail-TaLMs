import unittest
from api import (
    fetch_single_document,
    fetch_multiple_documents,
    search_documents,
    fetch_single_pi_document,
    fetch_multiple_pi_documents,
    search_pi_documents,
    get_current_pi_documents,
    get_pi_documents_by_date,
    get_agency_data
)

class TestFederalRegisterAPI(unittest.TestCase):

    def test_fetch_single_document(self):
        response = fetch_single_document(fr_document_number="2021-12345")
        self.assertIn("document_number", response)

    def test_fetch_multiple_documents(self):
        response = fetch_multiple_documents(fr_document_numbers=["2021-12345", "2021-12346"])
        self.assertIsInstance(response, list)

    def test_search_documents(self):
        response = search_documents(query="environment")
        self.assertIn("results", response)

    def test_fetch_single_pi_document(self):
        response = fetch_single_pi_document(pi_document_number="2021-12345")
        self.assertIn("document_number", response)

    def test_fetch_multiple_pi_documents(self):
        response = fetch_multiple_pi_documents(pi_document_numbers=["2021-12345", "2021-12346"])
        self.assertIsInstance(response, list)

    def test_search_pi_documents(self):
        response = search_pi_documents(query="policy")
        self.assertIn("results", response)

    def test_get_current_pi_documents(self):
        response = get_current_pi_documents()
        self.assertIn("results", response)

    def test_get_pi_documents_by_date(self):
        response = get_pi_documents_by_date(date="2023-10-01")
        self.assertIn("results", response)

    def test_get_agency_data(self):
        response = get_agency_data()
        self.assertIn("results", response)

if __name__ == '__main__':
    unittest.main()