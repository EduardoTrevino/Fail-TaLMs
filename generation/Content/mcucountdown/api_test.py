import unittest
from api import get_next_mcu_production

class TestMCUCountdownAPI(unittest.TestCase):
    
    def test_get_next_mcu_production_default(self):
        """ Test the default call to get the next MCU production with today's date """
        response = get_next_mcu_production()
        self.assertIn('days_until', response)
        self.assertIn('title', response)

    def test_get_next_mcu_production_with_date(self):
        """ Test the call to get the next MCU production starting from a specific date """
        response = get_next_mcu_production(date="2020-11-01")
        self.assertIn('days_until', response)
        self.assertIn('title', response)

    def test_get_next_mcu_production_invalid_date(self):
        """ Test the call with an invalid date format """
        response = get_next_mcu_production(date="invalid-date")
        self.assertIn('error', response)

if __name__ == '__main__':
    unittest.main()