import unittest
from api import get_graphical_forecast, get_machine_readable_forecast

class TestSevenTimerAPI(unittest.TestCase):

    def test_get_graphical_forecast(self):
        # Test with a known location for graphical forecast
        response = get_graphical_forecast(lon=113.17, lat=23.09)
        self.assertEqual(response[:8], b'\x89PNG\r\n\x1a\n')  # PNG files start with this signature

    def test_get_machine_readable_forecast_json(self):
        # Test with a known location for machine-readable forecast in JSON
        response = get_machine_readable_forecast(lon=113.17, lat=23.09, output='json')
        self.assertIn('dataseries', response)  # Expecting 'dataseries' key in JSON response

    def test_get_machine_readable_forecast_xml(self):
        # Test with a known location for machine-readable forecast in XML
        response = get_machine_readable_forecast(lon=113.17, lat=23.09, output='xml')
        self.assertTrue(response.startswith('<?xml'))

if __name__ == '__main__':
    unittest.main()