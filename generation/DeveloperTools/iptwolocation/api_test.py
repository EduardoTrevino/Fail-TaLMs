import unittest
from api import ip_geolocation, domain_whois


class TestIPTwoLocationAPI(unittest.TestCase):

    def test_ip_geolocation(self):
        response = ip_geolocation(ip='8.8.8.8')
        self.assertIsInstance(response, dict)
        self.assertIn('ip', response)
        self.assertNotIn('error', response)

    def test_ip_geolocation_valid_ip(self):
        response = ip_geolocation(ip='8.8.8.8')
        self.assertIsInstance(response, dict)
        self.assertIn('country_code', response)

    def test_domain_is_found(self):
        response = domain_whois(domain='google.com')
        self.assertIsInstance(response, dict)
        self.assertNotIn('error', response)

    def test_ip_geolocation_invalid_ip(self):
        response = ip_geolocation(ip='999.999.999.999')
        self.assertIsInstance(response, dict)
        self.assertIn('error', response)

    def test_domain_whois_not_found(self):
        response = domain_whois(domain='doesnotexist.tld')
        self.assertIsInstance(response, dict)
        self.assertIn('error', response)


if __name__ == '__main__':
    unittest.main()