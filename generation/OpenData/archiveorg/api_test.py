import unittest
from api import get_metadata, search_items

class ArchiveOrgAPITest(unittest.TestCase):

    def test_get_metadata(self):
        result = get_metadata('popeye_taxi-turvey')
        self.assertIn('metadata', result, "Metadata should be in the result")
        
    def test_search_items(self):
        results = search_items('collection:nasa')
        self.assertIn('items', results, "Items should be in the results")
        self.assertIsInstance(results['items'], list, "Items should be a list")
    
    def test_search_items_with_cursor(self):
        initial_results = search_items('collection:nasa')
        cursor = initial_results.get('cursor', None)
        results_with_cursor = search_items('collection:nasa', cursor=cursor)
        self.assertIn('items', results_with_cursor, "Items should be in the results with cursor")

if __name__ == '__main__':
    unittest.main()