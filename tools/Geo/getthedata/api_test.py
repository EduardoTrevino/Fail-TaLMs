import unittest
from api import bng2latlong

class TestGetTheDataAPI(unittest.TestCase):

    def test_bng2latlong_json_success(self):
        result = bng2latlong(326897, 673919)
        self.assertIn('status', result)
        self.assertEqual(result['status'], 'ok')
        self.assertAlmostEqual(result['latitude'], 55.95271, places=5)
        self.assertAlmostEqual(result['longitude'], -3.17227, places=5)

    def test_bng2latlong_json_error(self):
        result = bng2latlong(-9999, 673919)  # Invalid easting
        self.assertIn('status', result)
        self.assertEqual(result['status'], 'error')

    def test_bng2latlong_xml_success(self):
        result = bng2latlong(326897, 673919, response_format='xml')
        self.assertIn('<status>ok</status>', result)

    def test_bng2latlong_xml_error(self):
        result = bng2latlong(-9999, 673919, response_format='xml')
        self.assertIn('<status>error</status>', result)

if __name__ == '__main__':
    unittest.main()