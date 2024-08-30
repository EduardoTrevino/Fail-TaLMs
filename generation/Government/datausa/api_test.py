import unittest
from api import get_population_data

class TestDataUSAApi(unittest.TestCase):

    def test_get_population_data_default(self):
        # Test the default API call for national level population data
        result = get_population_data()
        self.assertIn('data', result)
        self.assertIn('source', result)
        self.assertGreater(len(result['data']), 0)
    
    def test_get_population_data_state(self):
        # Test retrieving population data for states
        result = get_population_data(drilldowns='State')
        self.assertIn('data', result)
        self.assertIn('source', result)
        self.assertGreater(len(result['data']), 0)
    
    def test_get_population_data_specific_year(self):
        # Test retrieving population data for a specific year
        result = get_population_data(year='2016')
        self.assertIn('data', result)
        self.assertIn('source', result)
        self.assertGreater(len(result['data']), 0)

if __name__ == '__main__':
    unittest.main()