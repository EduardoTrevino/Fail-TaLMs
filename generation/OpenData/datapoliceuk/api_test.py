import unittest
from api import *

class TestPoliceAPI(unittest.TestCase):

    def test_available_datasets(self):
        response = available_datasets()
        self.assertIsInstance(response, list)

    def test_list_forces(self):
        response = list_forces()
        self.assertIsInstance(response, list)

    def test_specific_force(self):
        force_id = "leicestershire"
        response = specific_force(force_id)
        self.assertIsInstance(response, dict)
        self.assertEqual(response['id'], force_id)

    def test_force_senior_officers(self):
        force_id = "leicestershire"
        response = force_senior_officers(force_id)
        self.assertIsInstance(response, list)

    def test_street_level_crimes(self):
        lat, lng = 52.629729, -1.131592
        response = street_level_crimes(lat, lng)
        self.assertIsInstance(response, list)

    def test_crimes_at_location_by_location_id(self):
        location_id = 884227
        response = crimes_at_location(location_id=location_id)
        self.assertIsInstance(response, list)

    def test_crimes_with_no_location(self):
        category, force = "all-crime", "leicestershire"
        response = crimes_with_no_location(category, force)
        self.assertIsInstance(response, list)

    def test_crime_categories(self):
        response = crime_categories()
        self.assertIsInstance(response, list)

    def test_crime_last_updated(self):
        response = crime_last_updated()
        self.assertIsInstance(response, dict)
        
    def test_outcomes_for_specific_crime(self):
        crime_id = "590d68b69228a9ff95b675bb4af591b38de561aa03129dc09a03ef34f537588c"
        response = outcomes_for_specific_crime(crime_id)
        self.assertIsInstance(response, dict)

    def test_neighbourhoods_by_force(self):
        force_id = "leicestershire"
        response = neighbourhoods_by_force(force_id)
        self.assertIsInstance(response, list)

    def test_specific_neighbourhood(self):
        force_id, neighbourhood_id = "leicestershire", "NC04"
        response = specific_neighbourhood(force_id, neighbourhood_id)
        self.assertIsInstance(response, dict)

    def test_neighbourhood_boundary(self):
        force_id, neighbourhood_id = "leicestershire", "NC04"
        response = neighbourhood_boundary(force_id, neighbourhood_id)
        self.assertIsInstance(response, list)

    def test_neighbourhood_team(self):
        force_id, neighbourhood_id = "leicestershire", "NC04"
        response = neighbourhood_team(force_id, neighbourhood_id)
        self.assertIsInstance(response, list)

    def test_neighbourhood_events(self):
        force_id, neighbourhood_id = "leicestershire", "NC04"
        response = neighbourhood_events(force_id, neighbourhood_id)
        self.assertIsInstance(response, list)

    def test_neighbourhood_priorities(self):
        force_id, neighbourhood_id = "leicestershire", "NC04"
        response = neighbourhood_priorities(force_id, neighbourhood_id)
        self.assertIsInstance(response, list)

    def test_locate_neighbourhood(self):
        lat, lng = 51.500617, -0.124629
        response = locate_neighbourhood(lat, lng)
        self.assertIsInstance(response, dict)

    def test_stop_and_searches_by_area(self):
        lat, lng = 52.629729, -1.131592
        response = stop_and_searches_by_area(lat, lng)
        self.assertIsInstance(response, list)

    def test_stop_and_searches_by_location(self):
        location_id = 883407
        response = stop_and_searches_by_location(location_id)
        self.assertIsInstance(response, list)

    def test_stop_and_searches_no_location(self):
        force = "leicestershire"
        response = stop_and_searches_no_location(force)
        self.assertIsInstance(response, list)

    def test_stop_and_searches_by_force(self):
        force = "avon-and-somerset"
        response = stop_and_searches_by_force(force)
        self.assertIsInstance(response, list)

if __name__ == "__main__":
    unittest.main()