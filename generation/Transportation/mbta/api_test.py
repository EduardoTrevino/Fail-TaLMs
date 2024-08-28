import unittest
from api import get_alerts, get_alert_detail, get_facilities, get_facility_detail, get_lines, get_line_detail

class TestMBTAApi(unittest.TestCase):
    
    def test_get_alerts(self):
        response = get_alerts()
        self.assertIn("links", response)  # Testing if an expected structure exists
        # self.assertEqual(response.get("links").get("self"), "string")  # Testing if an expected structure exists

    def test_get_alert_detail(self):
        response = get_alert_detail("589935")  # Use a valid alert ID for actual testing
        self.assertIn("links", response) 
        # self.assertEqual(response.get("links").get("self"), "string")  # Testing if an expected structure exists
    
    def test_get_facilities(self):
        response = get_facilities()
        self.assertIn("links", response) 
        # self.assertEqual(response.get("links").get("self"), "string")  # Testing if an expected structure exists
    
    def test_get_facility_detail(self):
        response = get_facility_detail("fvm-201318")  # Use a valid facility ID for actual testing
        self.assertIn("links", response) 
        # self.assertEqual(response.get("links").get("self"), "string")  # Testing if an expected structure exists
    
    def test_get_lines(self):
        response = get_lines()
        self.assertIn("links", response) 
        # self.assertEqual(response.get("links").get("self"), "string")  # Testing if an expected structure exists
    
    def test_get_line_detail(self):
        response = get_line_detail("line-Red")  # Use a valid line ID for actual testing
        self.assertIn("links", response) 
        # self.assertEqual(response.get("links").get("self"), "string")  # Testing if an expected structure exists

# The unittest.main() entry point is typically used to run all tests
if __name__ == '__main__':
    unittest.main()
