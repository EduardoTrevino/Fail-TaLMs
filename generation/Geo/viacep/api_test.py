import unittest
from api import query_cep, search_address


class TestViaCepAPI(unittest.TestCase):

    def test_query_cep_valid(self):
        result = query_cep('01001000')
        self.assertIn('cep', result)
        self.assertEqual(result['cep'], '01001-000')

    def test_query_cep_invalid_format(self):
        result = query_cep('01000-000')
        self.assertIn('error', result)
        self.assertEqual(result['error'], 'Invalid ZIP code format. Must be 8 digits.')

    def test_query_cep_nonexistent(self):
        result = query_cep('9999999999')
        self.assertIn('error', result)
        self.assertTrue(result['error'])

    def test_search_address_valid(self):
        result = search_address('RS', 'Porto Alegre', 'Domingos')
        self.assertIsInstance(result, list)
        if len(result) > 0:
            self.assertIn('cep', result[0])
    
    def test_search_address_invalid_params(self):
        result = search_address('RS', 'Po', 'Domingos')
        self.assertIn('error', result)
        self.assertEqual(result['error'], 'City and street names must be at least 3 characters long.')

    def test_search_address_no_results(self):
        result = search_address('RS', 'Porto Alegre', 'Nonexistent Street')
        self.assertEqual(result, [])  # Expect an empty list if no results are found


if __name__ == '__main__':
    unittest.main()