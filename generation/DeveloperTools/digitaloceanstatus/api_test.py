import unittest
from api import *

class TestDigitalOceanStatusAPI(unittest.TestCase):

    def test_get_summary(self):
        response = get_summary()
        self.assertIn("status", response)

    def test_get_status(self):
        response = get_status()
        self.assertIn("indicator", response)
    
    def test_get_components(self):
        response = get_components()
        self.assertIn("components", response)

    def test_get_unresolved_incidents(self):
        response = get_unresolved_incidents()
        self.assertIn("incidents", response)

    def test_get_all_incidents(self):
        response = get_all_incidents()
        self.assertIn("incidents", response)

    def test_get_upcoming_maintenances(self):
        response = get_upcoming_maintenances()
        self.assertIn("scheduled_maintenances", response)

    def test_get_active_maintenances(self):
        response = get_active_maintenances()
        self.assertIn("scheduled_maintenances", response)

    def test_get_all_maintenances(self):
        response = get_all_maintenances()
        self.assertIn("scheduled_maintenances", response)

if __name__ == '__main__':
    unittest.main()