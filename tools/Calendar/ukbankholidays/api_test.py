import unittest
from api import get_bank_holidays


class TestUKBankHolidaysAPI(unittest.TestCase):

    def test_get_bank_holidays_default(self):
        # Test the default call to get_bank_holidays
        response = get_bank_holidays()
        self.assertIn('title', response)
        self.assertIn('events', response)

    def test_get_bank_holidays_england_and_wales(self):
        # Test a specific division: England and Wales
        response = get_bank_holidays('england-and-wales')
        self.assertIn('title', response)
        self.assertIn('events', response)
        
    def test_get_bank_holidays_scotland(self):
        # Test a specific division: Scotland
        response = get_bank_holidays('scotland')
        self.assertIn('title', response)
        self.assertIn('events', response)
    
    def test_invalid_division(self):
        # Test with an invalid division
        response = get_bank_holidays('invalid-division')
        self.assertEqual(response.get('error'), 'Division not found')


if __name__ == "__main__":
    unittest.main()