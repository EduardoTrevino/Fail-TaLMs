import unittest
from api import get_current_comic, get_comic_by_number

class TestXKCDAPI(unittest.TestCase):
    
    def test_get_current_comic(self):
        response = get_current_comic()
        self.assertIsInstance(response, dict)
        self.assertIn("num", response)
        self.assertIn("title", response)
        self.assertIn("img", response)
    
    def test_get_comic_by_number(self):
        response = get_comic_by_number(614)
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get("num"), 614)
        
        # Test invalid comic number
        response = get_comic_by_number(-1)
        self.assertIsInstance(response, dict)
        self.assertIn("error", response)

if __name__ == '__main__':
    unittest.main()