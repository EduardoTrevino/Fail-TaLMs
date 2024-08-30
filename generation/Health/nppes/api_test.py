import unittest
from api import search_npi

class TestNPPESAPI(unittest.TestCase):
    
    def test_search_npi_with_name(self):
        response = search_npi(first_name='John', use_first_name_alias=False)
        self.assertIn('results', response)

    def test_search_npi_with_organization(self):
        response = search_npi(organization_name='Health Corp')
        self.assertIn('results', response)

if __name__ == '__main__':
    unittest.main()