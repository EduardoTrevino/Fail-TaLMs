import unittest
from api import edit_alert, manage_alerts, get_alerts

class TestCheapSharkAPI(unittest.TestCase):

    def test_edit_alert_set(self):
        # This test assumes the API will return True or False for valid or invalid inputs.
        response = edit_alert(action='set', email='someone@example.org', game_id=59, price=14.99)
        self.assertTrue(isinstance(response, bool))

    def test_edit_alert_delete(self):
        # This test assumes the API will return True or False for valid or invalid inputs.
        response = edit_alert(action='delete', email='someone@example.org', game_id=59)
        self.assertTrue(isinstance(response, bool))

    def test_manage_alerts(self):
        # This test assumes the API will return a string response.
        response = manage_alerts(email='address-with-alerts@example.org')
        self.assertTrue(isinstance(response, str))

    def test_get_alerts_valid_key(self):
        # This test assumes a valid key will return a list of alerts.
        response = get_alerts(key='valid-key-with-alerts')
        if isinstance(response, list):
            self.assertTrue(all(isinstance(alert, dict) for alert in response))
        else:
            self.fail("Expected a list of alerts, got a string error message instead.")

    def test_get_alerts_invalid_key(self):
        # Get the response from the function
        response = get_alerts(key='invalid-key')
        
        # Check if the response is a string, bool, None, or an empty list
        self.assertTrue(isinstance(response, (str, bool, type(None), list)), f"Expected a string, False, None, or list for invalid key, got {type(response)}")
        
        if isinstance(response, bool):
            self.assertFalse(response, "Expected False for an invalid key.")
        elif isinstance(response, list):
            self.assertEqual(len(response), 0, "Expected an empty list for an invalid key.")




if __name__ == '__main__':
    unittest.main()
