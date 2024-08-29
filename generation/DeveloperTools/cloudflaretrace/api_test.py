import unittest
from api import cloudflaretrace

class TestCloudflareTraceAPI(unittest.TestCase):
    
    def test_cloudflaretrace_default_endpoint(self):
        """Test the cloudflaretrace API with the default endpoint."""
        response = cloudflaretrace()
        self.assertIsInstance(response, dict)
        self.assertIn("ip", response)
        self.assertIn("ts", response)
        self.assertIn("uag", response)
    
    def test_cloudflaretrace_specific_endpoint(self):
        """Test the cloudflaretrace API with a specific endpoint."""
        response = cloudflaretrace(endpoint="https://1.0.0.1/cdn-cgi/trace")
        self.assertIsInstance(response, dict)
        self.assertIn("ip", response)
        self.assertIn("ts", response)
        self.assertIn("uag", response)

if __name__ == "__main__":
    unittest.main()