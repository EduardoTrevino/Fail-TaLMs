import unittest
from api import locations, locations_nearby, stops_reachable_from, stop_info, stop_departures, journeys, radar, lines

class TestBerlinBrandenburgAPI(unittest.TestCase):

    def test_locations(self):
        response = locations(query='alexanderplatz')
        self.assertIsInstance(response, list)

    def test_locations_nearby(self):
        response = locations_nearby(52.52725, 13.4123)
        self.assertIsInstance(response, list)

    def test_stops_reachable_from(self):
        response = stops_reachable_from(latitude=52.52446, longitude=13.40812, address='10178 Berlin-Mitte, Münzstr. 12')
        self.assertIsInstance(response, list)

    def test_stop_info(self):
        response = stop_info('900017101')
        self.assertIsInstance(response, dict)

    def test_stop_departures(self):
        response = stop_departures('900013102', duration=10)
        self.assertIsInstance(response, list)

    def test_journeys(self):
        response = journeys(from_id='900023201', to_id='900980720')
        self.assertIsInstance(response, dict)

    def test_radar(self):
        response = radar(north=52.52411, west=13.41002, south=52.51942, east=13.41709)
        self.assertIsInstance(response, list)

    def test_lines(self):
        response = lines(operator='796')
        self.assertIsInstance(response, dict)

if __name__ == '__main__':
    unittest.main()