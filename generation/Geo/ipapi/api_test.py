import unittest
from api import get_ip_location, get_ip_location_field, get_client_ip_location, get_client_ip_location_field

class TestIpApi(unittest.TestCase):

    def test_get_ip_location(self):
        ip = "8.8.8.8"
        response = get_ip_location(ip)
        self.assertIn("ip", response)
        self.assertEqual(response["ip"], ip)

    def test_get_ip_location_field(self):
        ip = "8.8.8.8"
        field = "country"
        response = get_ip_location_field(ip, field)
        self.assertEqual(response, "US")

    def test_get_client_ip_location(self):
        response = get_client_ip_location()
        self.assertIn("ip", response)

    def test_get_client_ip_location_field(self):
        field = "ip"
        response = get_client_ip_location_field(field)
        self.assertTrue(response)  # should return a valid IP address string

if __name__ == "__main__":
    unittest.main()