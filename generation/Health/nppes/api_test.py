import unittest
from api import search_npi

class TestNPPESAPI(unittest.TestCase):
    
    def test_search_npi_default(self):
        response = search_npi()
        self.assertIn('Results', response)
        print("Default parameters:", response['Results'])

    def test_search_npi_with_number(self):
        response = search_npi(number='1234567890')
        self.assertIn('Results', response)
        self.assertEqual(response['Results'][0]['number'], '1234567890')
        print("Search with Number:", response['Results'])

    def test_search_npi_with_name(self):
        response = search_npi(first_name='John', use_first_name_alias=False)
        self.assertIn('Results', response)
        print("Search with First Name 'John':", response['Results'])

    def test_search_npi_with_organization(self):
        response = search_npi(organization_name='Health Corp')
        self.assertIn('Results', response)
        print("Search with Organization Name 'Health Corp':", response['Results'])

if __name__ == '__main__':
    unittest.main()