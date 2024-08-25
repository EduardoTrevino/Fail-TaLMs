import unittest
from api import get_standard_exchange_rates, pair_conversion, get_historical_data, get_supported_codes

class TestExchangeRateAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
    
    def test_get_standard_exchange_rates(self):
        result = get_standard_exchange_rates(base_currency="USD", toolbench_rapidapi_key=self.api_key)
        self.assertEqual(result.get('result'), 'success')
        self.assertIn('conversion_rates', result)

    def test_pair_conversion(self):
        result = pair_conversion(base_currency="USD", target_currency="EUR", toolbench_rapidapi_key=self.api_key)
        self.assertEqual(result.get('result'), 'success')
        self.assertIn('conversion_rate', result)

        result_with_amount = pair_conversion(base_currency="USD", target_currency="EUR", amount=100, toolbench_rapidapi_key=self.api_key)
        self.assertEqual(result_with_amount.get('result'), 'success')
        self.assertIn('conversion_result', result_with_amount)

    def test_get_historical_data(self):
        result = get_historical_data(base_currency="USD", year=2020, month=3, day=27, toolbench_rapidapi_key=self.api_key)
        self.assertEqual(result.get('result'), 'success')
        self.assertIn('conversion_rates', result)

        result_with_amount = get_historical_data(base_currency="USD", year=2020, month=3, day=27, amount=100, toolbench_rapidapi_key=self.api_key)
        self.assertEqual(result_with_amount.get('result'), 'success')
        self.assertIn('conversion_amounts', result_with_amount)

    def test_get_supported_codes(self):
        result = get_supported_codes(toolbench_rapidapi_key=self.api_key)
        self.assertEqual(result.get('result'), 'success')
        self.assertIn('supported_codes', result)

if __name__ == '__main__':
    unittest.main()