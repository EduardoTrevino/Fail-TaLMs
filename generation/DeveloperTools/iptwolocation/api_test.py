import unittest
from api import ip_geolocation, domain_whois


class TestIPTwoLocationAPI(unittest.TestCase):

    def test_ip_geolocation(self):
        response = ip_geolocation(ip='8.8.8.8')
        self.assertIsInstance(response, dict)
        self.assertIn('ip', response)

    # def test_domain_whois(self):
    #     response = domain_whois(domain='google.com')
    #     self.assertIsInstance(response, dict)
    #     self.assertIn('domain', response)

    # def test_bulk_ip_geolocation(self):
    #     ips = ['1.1.1.1', '2.2.2.2']
    #     response = bulk_ip_geolocation(ips=ips)
    #     self.assertIsInstance(response, dict)
    #     for ip in ips:
    #         self.assertIn(ip, response)

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