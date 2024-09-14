import unittest
from api import get_location_by_ip, currency_converter

class TestGeoPluginAPI(unittest.TestCase):

    def test_get_location_by_ip(self):
        """Test the geolocation retrieval by IP address."""
        # Test with auto IP
        result = get_location_by_ip()
        self.assertIn('geoplugin_request', result)
        self.assertIn('geoplugin_status', result)
        
        # Test with a specific IP
        specific_ip = "8.8.8.8"
        result = get_location_by_ip(specific_ip)
        self.assertIn('geoplugin_request', result)
        self.assertEqual(result['geoplugin_request'], specific_ip)

    def test_currency_converter(self):
        """Test the currency conversion"""
        result = currency_converter(base_currency="USD", amount=50)
        self.assertIn('amount', result)
        self.assertEqual(result['local_currency'], 'USD')
        self.assertIn('exchange_rate', result)
    
if __name__ == '__main__':
    unittest.main()