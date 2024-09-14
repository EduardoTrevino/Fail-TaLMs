import unittest
from api import get_people, get_films, get_starships, get_vehicles, get_species, get_planets

class TestSWAPI(unittest.TestCase):

    def test_get_people(self):
        response = get_people()
        self.assertIn('results', response)

    def test_get_person(self):
        response = get_people(1)
        self.assertEqual(response['name'], 'Luke Skywalker')

    def test_search_people(self):
        response = get_people(search='skywalker')
        self.assertIn('results', response)
        self.assertTrue(any('Skywalker' in person['name'] for person in response['results']))

    def test_get_films(self):
        response = get_films()
        self.assertIn('results', response)

    def test_get_single_film(self):
        response = get_films(1)
        self.assertEqual(response['title'], 'A New Hope')

    def test_get_starships(self):
        response = get_starships()
        self.assertIn('results', response)

    def test_get_starship(self):
        response = get_starships(9)
        self.assertEqual(response['name'], 'Death Star')

    def test_get_vehicles(self):
        response = get_vehicles()
        self.assertIn('results', response)

    def test_get_vehicle(self):
        response = get_vehicles(4)
        self.assertEqual(response['name'], 'Sand Crawler')

    def test_get_species(self):
        response = get_species()
        self.assertIn('results', response)

    def test_get_specific_species(self):
        response = get_species(3)
        self.assertEqual(response['name'], 'Wookie')

    def test_get_planets(self):
        response = get_planets()
        self.assertIn('results', response)

    def test_get_specific_planet(self):
        response = get_planets(1)
        self.assertEqual(response['name'], 'Tatooine')

if __name__ == '__main__':
    unittest.main()