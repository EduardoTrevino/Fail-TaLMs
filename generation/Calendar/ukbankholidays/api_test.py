import unittest
from api import uk_bank_holidays_json

class UKBankHolidaysAPITest(unittest.TestCase):
    
    def test_uk_bank_holidays_json(self):
        response = uk_bank_holidays_json()
        self.assertIsInstance(response, dict)
        # self.assertIn('division', response)
        self.assertIn('england-and-wales', response['division'])
        self.assertIn('scotland', response['division'])
        self.assertIn('northern-ireland', response['division'])

if __name__ == '__main__':
    unittest.main()