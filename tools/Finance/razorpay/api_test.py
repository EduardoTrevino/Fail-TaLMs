import unittest
from api import get_bank_details_by_ifsc

class TestRazorpayAPI(unittest.TestCase):

    def test_valid_ifsc_code(self):
        response = get_bank_details_by_ifsc("YESB0DNB002")
        self.assertIn("BANK", response)
        self.assertEqual(response["BANK"], "Delhi Nagrik Sehkari Bank")

    def test_invalid_ifsc_code(self):
        response = get_bank_details_by_ifsc("INVALIDCODE")
        self.assertIn("error", response)
        self.assertEqual(response["error"], "Invalid IFSC code")

if __name__ == "__main__":
    unittest.main()