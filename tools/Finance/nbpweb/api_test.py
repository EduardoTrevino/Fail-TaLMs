import unittest
import api


class TestNBPWebAPI(unittest.TestCase):
    
    def test_get_exchange_rate_table(self):
        result = api.get_exchange_rate_table(table='A')
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn('table', result[0])  # Check the first dictionary in the list

    def test_get_currency_exchange_rate(self):
        result = api.get_currency_exchange_rate(table='A', code='USD')
        self.assertIn('currency', result)

    def test_get_gold_price(self):
        result = api.get_gold_price()
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()