import unittest
from api import get_ip, get_country, get_geo_info, get_ptr_record

class TestGeoJSAPI(unittest.TestCase):
    
    def test_get_ip(self):
        result = get_ip()
        self.assertIn('ip', result)

    def test_get_country_with_no_ip(self):
        result = get_country()
        self.assertIn('country', result)
        self.assertIn('name', result)

    def test_get_country_with_ip(self):
        ip = "8.8.8.8"
        result = get_country(ip)
        self.assertEqual(result['ip'], ip)

    def test_get_geo_info_with_no_ip(self):
        result = get_geo_info()
        self.assertIn('country', result)
        self.assertIn('latitude', result)
    
    def test_get_geo_info_with_ip(self):
        ip = "8.8.8.8"
        result = get_geo_info(ip)
        self.assertEqual(result['ip'], ip)

    def test_get_ptr_record(self):
        ip = "8.8.8.8"
        result = get_ptr_record(ip)
        self.assertIn('ptr', result)