import unittest
import api

class TestOpenBreweryAPI(unittest.TestCase):

    def test_single_brewery(self):
        result = api.single_brewery('madtree-brewing-cincinnati')
        self.assertIn('id', result)
        self.assertEqual(result['id'], 'madtree-brewing-cincinnati')

    def test_list_breweries(self):
        result = api.list_breweries()
        self.assertIsInstance(result, list)

    def test_random_brewery(self):
        result = api.random_brewery()
        self.assertIn('id', result)

    def test_search_breweries(self):
        result = api.search_breweries('dog')
        self.assertIsInstance(result, list)

    def test_autocomplete(self):
        result = api.autocomplete('dog')
        self.assertIsInstance(result, list)

    def test_breweries_by_city(self):
        result = api.breweries_by_city('San Diego')
        self.assertIsInstance(result, list)

    def test_breweries_by_state(self):
        result = api.breweries_by_state('California')
        self.assertIsInstance(result, list)

    def test_breweries_by_postal(self):
        result = api.breweries_by_postal('44113')
        self.assertIsInstance(result, list)

    def test_breweries_by_type(self):
        result = api.breweries_by_type('micro')
        self.assertIsInstance(result, list)

    def test_breweries_by_name(self):
        result = api.breweries_by_name('dog')
        self.assertIsInstance(result, list)

    def test_breweries_by_dist(self):
        result = api.breweries_by_dist(39.7589478, -84.1916069) # Example coordinates
        self.assertIsInstance(result, list)

    def test_breweries_by_ids(self):
        result = api.breweries_by_ids('madtree-brewing-cincinnati,dogtown-brewing-cincinnati')
        self.assertIsInstance(result, list)

    def test_breweries_metadata(self):
        result = api.breweries_metadata()
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()