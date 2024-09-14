import unittest
from api import get_sunrise_sunset_times

class TestSunriseSunsetAPI(unittest.TestCase):
    
    def test_get_sunrise_sunset_times_standard_request(self):
        # Test with only required parameters
        response = get_sunrise_sunset_times(38.907192, -77.036873)
        self.assertEqual(response.get("status"), "OK")
        self.assertIn("results", response)

    def test_get_sunrise_sunset_times_specific_date(self):
        # Test with a specific date and timezone
        response = get_sunrise_sunset_times(38.907192, -77.036873, date="1990-05-22", timezone="UTC")
        self.assertEqual(response.get("status"), "OK")
        self.assertIn("results", response)

    def test_get_sunrise_sunset_times_date_range(self):
        # Test with a date range
        response = get_sunrise_sunset_times(38.907192, -77.036873, date_start="1990-05-01", date_end="1990-07-01")
        self.assertEqual(response.get("status"), "OK")
        self.assertIn("results", response)

    def test_get_sunrise_sunset_times_24_hour_format(self):
        # Test with 24-hour time format
        response = get_sunrise_sunset_times(38.907192, -77.036873, date="1990-05-22", timezone="UTC", time_format="24")
        self.assertEqual(response.get("status"), "OK")
        self.assertIn("results", response)

if __name__ == '__main__':
    unittest.main()