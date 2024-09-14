import unittest
from api import get_entry, get_all_entries, get_category_entries, get_master_mode_entry, get_all_master_mode_entries, get_region, get_all_regions


class TestHyruleCompendiumAPI(unittest.TestCase):

    def test_get_entry(self):
        response = get_entry('moblin')
        self.assertIn('data', response)
        self.assertEqual(response['data']['name'], 'moblin')

    def test_get_all_entries(self):
        response = get_all_entries()
        self.assertIn('data', response)

    def test_get_category_entries(self):
        response = get_category_entries('monsters')
        self.assertIn('data', response)

    def test_get_master_mode_entry(self):
        response = get_master_mode_entry('golden_bokoblin')
        self.assertIn('data', response)

    def test_get_all_master_mode_entries(self):
        response = get_all_master_mode_entries()
        self.assertIn('data', response)

    def test_get_region(self):
        response = get_region('eldin')
        self.assertIn('data', response)

    def test_get_all_regions(self):
        response = get_all_regions()
        self.assertIn('data', response)


if __name__ == '__main__':
    unittest.main()