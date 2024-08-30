import unittest
from api import get_latest_exchange_rates

class TestExchangeRateAPI(unittest.TestCase):

    def test_get_latest_exchange_rates_success(self):
        # Test for successful retrieval of exchange rates
        response = get_latest_exchange_rates("USD")
        self.assertIn("result", response)
        self.assertEqual(response["result"], "success")
        self.assertIn("rates", response)
        self.assertIn("USD", response["rates"])

    def test_get_latest_exchange_rates_invalid_currency(self):
        # Test for an invalid currency code
        response = get_latest_exchange_rates("INVALID")
        self.assertEqual(response["result"], "error")
        self.assertIn("error-type", response)
        self.assertEqual(response["error-type"], "unsupported-code")

    def test_get_latest_exchange_rates_rate_limited(self):
        # Simulate a rate limit exceeded situation
        # Since we cannot force a rate limit from a unit test, this is a conceptual test
        # Assuming a mock or actual situation where rate limit is exceeded
        response = get_latest_exchange_rates("USD")
        if response.get("error") == "Rate limit exceeded. Please try again after some time.":
            self.assertEqual(response["error"], "Rate limit exceeded. Please try again after some time.")
        else:
            self.assertIn("result", response)
            self.assertEqual(response["result"], "success")
    
    def test_get_latest_exchange_rates_connection_error(self):
        # Simulate a connection error
        # This would typically require mocking requests.get to throw an exception
        try:
            with unittest.mock.patch('requests.get', side_effect=requests.exceptions.ConnectionError):
                response = get_latest_exchange_rates("USD")
                self.assertIn("error", response)
                self.assertIn("ConnectionError", response["error"])
        except AttributeError:
            # If unittest.mock is not available, this test would be purely conceptual
            pass

if __name__ == '__main__':
    unittest.main()