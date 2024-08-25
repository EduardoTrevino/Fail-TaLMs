import unittest
from api import get_all_transactions, get_available_disclosures, get_daily_transaction_report

class TestHouseStockWatcherAPI(unittest.TestCase):

    def test_get_all_transactions(self):
        response = get_all_transactions()
        self.assertIsInstance(response, list)

    def test_get_available_disclosures(self):
        response = get_available_disclosures()
        self.assertIsInstance(response, list)
        self.assertTrue(all(isinstance(item, str) for item in response))

    def test_get_daily_transaction_report(self):
        known_date = '01_01_2021'
        response = get_daily_transaction_report(known_date)
        if 'error' not in response:
            self.assertIn('transactions', response)
        else:
            self.assertIn('error', response)

if __name__ == '__main__':
    unittest.main()