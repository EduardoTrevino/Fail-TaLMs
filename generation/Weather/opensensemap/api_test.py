import unittest
from api import *

class TestOpenSenseMapAPI(unittest.TestCase):

    def test_get_boxes(self):
        response = get_boxes("57000b8745fd40c8196ad04c")
        self.assertIn("_id", response)
        self.assertEqual(response["_id"], "57000b8745fd40c8196ad04c")

    def test_get_all_boxes(self):
        response = get_all_boxes(limit=1)
        # self.assertIsInstance(response, list)
        self.assertTrue(len(response) > 0)

    def test_get_locations(self):
        response = get_locations("57000b8745fd40c8196ad04c")

    def test_get_idw_statistics(self):
        response = get_idw_statistics("7.6,51.2,7.8,51.4", "Temperatur")
        self.assertIn("featureCollection", response)

    def test_get_statistics_descriptive(self):
        response = get_statistics_descriptive("57000b8745fd40c8196ad04c", "Temperatur", "2023-01-01T00:00:00Z", "2023-01-31T23:59:59Z", "arithmeticMean", "1d")
        self.assertIsNotNone(response)

    def test_get_latest_measurements_for_sensor(self):
        response = get_latest_measurements_for_sensor("57000b8745fd40c8196ad04c", "57000b8745fd40c8196ad050")
      
    def test_get_latest_measurements_of_sense_box(self):
        response = get_latest_measurements_of_sense_box("57000b8745fd40c8196ad04c")
        self.assertIn("_id", response)

    def test_get_stats(self):
        response = get_stats()

    def test_print_routes(self):
        response = print_routes()
        self.assertIsInstance(response, dict)

if __name__ == '__main__':
    unittest.main()