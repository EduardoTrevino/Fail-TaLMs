import unittest
from api import get_user_agent_info

class TestApicAgentAPI(unittest.TestCase):

    def test_get_user_agent_info(self):
        ua_string = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
        response = get_user_agent_info(ua_string)
        
        # Check if the response has expected keys
        self.assertIn("browser_family", response)
        self.assertIn("client", response)
        self.assertIn("device", response)
        self.assertIn("os", response)
        self.assertIn("os_family", response)

        # Check if "browser_family" is as expected
        self.assertEqual(response.get("browser_family"), "Chrome")

if __name__ == '__main__':
    unittest.main()