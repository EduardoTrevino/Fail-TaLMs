import unittest
from api import get_ip_address_text, get_ip_address_json

class TestArulAPI(unittest.TestCase):

    def test_get_ip_address_text(self):
        result = get_ip_address_text()
        self.assertIsInstance(result, str)
        self.assertRegex(result, r'^(\d{1,3}\.){3}\d{1,3}$')  # Matches IPv4 format

    def test_get_ip_address_json(self):
        result = get_ip_address_json()
        self.assertIsInstance(result, dict)
        self.assertIn('ip', result)
        self.assertRegex(result['ip'], r'^(\d{1,3}\.){3}\d{1,3}$')  # Matches IPv4 format

if __name__ == '__main__':
    unittest.main()