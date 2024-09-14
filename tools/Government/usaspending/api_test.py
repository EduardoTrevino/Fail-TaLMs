import unittest
from api import get_agency_details, get_agency_awards_summary, get_award_details, search_spending_by_award

class TestUSASpendingAPI(unittest.TestCase):

    def test_get_agency_details(self):
        response = get_agency_details(toptier_agency_code="012")
        self.assertIn('fiscal_year', response)

    def test_get_agency_awards_summary(self):
        response = get_agency_awards_summary(toptier_agency_code="012")
        self.assertIn('fiscal_year', response)

    def test_get_award_details(self):
        response = get_award_details(award_id=1018950)
        self.assertIn('generated_unique_award_id', response)

    def test_search_spending_by_award(self):
        filters = {
            "award_type_codes": ["10"]
        }
        fields = ["Award ID", "Recipient Name"]
        response = search_spending_by_award(filters=filters, fields=fields, sort="Recipient Name", order="desc")
        self.assertIn('results', response)

if __name__ == '__main__':
    unittest.main()