import unittest
from api import get_country_by_own_ip, get_country_by_ip, get_data_sources_info

class TestCountryIsApi(unittest.TestCase):

    def test_get_country_by_own_ip(self):
        # Test the retrieval of the country based on own IP
        result = get_country_by_own_ip()
        self.assertIn('ip', result)
        self.assertIn('country', result)

    def test_get_country_by_ip(self):
        # Test the retrieval of the country for a specific IP
        ip = "9.9.9.9"
        result = get_country_by_ip(ip)
        self.assertIn('ip', result)
        self.assertIn('country', result)
        self.assertEqual(result['ip'], ip)

    def test_get_data_sources_info(self):
        # Test the retrieval of information about the data sources
        result = get_data_sources_info()
        self.assertIn('cloudflare', result)
        self.assertIn('maxmind', result)

if __name__ == '__main__':
    unittest.main()