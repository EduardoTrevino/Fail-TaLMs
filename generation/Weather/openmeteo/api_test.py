import unittest
from api import get_weather_forecast

class TestOpenMeteoAPI(unittest.TestCase):

    def test_get_weather_forecast(self):
        response = get_weather_forecast(latitude=52.52, longitude=13.41, hourly=["temperature_2m"])
        self.assertIn("latitude", response)
        self.assertIn("longitude", response)
        self.assertIn("hourly", response)
        self.assertNotIn("error", response)

    def test_get_weather_forecast_with_daily(self):
        response = get_weather_forecast(
            latitude=52.52, 
            longitude=13.41,
            daily=["temperature_2m_max", "temperature_2m_min"]
        )
        self.assertIn("daily", response)
        self.assertNotIn("error", response)

if __name__ == '__main__':
    unittest.main()