import unittest
from api import wayback_availability

class TestWaybackMachineAPI(unittest.TestCase):

    def test_wayback_availability(self):
        # Test for an available URL
        result = wayback_availability('example.com')
        self.assertIn('archived_snapshots', result)
        
        # Test for an unavailable URL
        result = wayback_availability('nonexistenturlfortesting.com')
        self.assertEqual(result['archived_snapshots'], {})
        
        # Test with timestamp
        result = wayback_availability('example.com', timestamp='20060101')
        self.assertIn('archived_snapshots', result)

if __name__ == '__main__':
    unittest.main()