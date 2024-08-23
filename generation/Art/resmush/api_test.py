import unittest
from api import resmush_get, resmush_post

class TestResmushAPI(unittest.TestCase):
    
    def test_resmush_get(self):
        # Use an example image URL for testing
        img_url = "https://resmush.it/wp-content/uploads/2024/02/testimage.jpg"
        response = resmush_get(img_url, qlty=95, exif=True)
        self.assertIn("dest", response)
        self.assertIn("src_size", response)
        self.assertIn("dest_size", response)

    def test_resmush_post(self):
        # Use an example image file for testing
        file_path = "testimage.jpg"
        response = resmush_post(file_path, qlty=95)
        self.assertIn("dest", response)
        self.assertIn("src_size", response)
        self.assertIn("dest_size", response)

if __name__ == "__main__":
    unittest.main()