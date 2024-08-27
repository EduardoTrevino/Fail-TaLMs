import unittest
from api import compress_image_get_method, compress_image_post_method

class TestResmushAPI(unittest.TestCase):
    
    def test_compress_image_get_method_success(self):
        # Test with a valid image URL
        img_url = "https://resmush.it/wp-content/uploads/2024/02/testimage.jpg"
        response = compress_image_get_method(img_url)
        self.assertIn('dest', response)
        self.assertNotIn('error', response)

    def test_compress_image_get_method_invalid_url(self):
        # Test with an invalid image URL
        img_url = "http://invalid-url/image.jpg"
        response = compress_image_get_method(img_url)
        self.assertIn('error', response)

    def test_compress_image_post_method_success(self):
        # Assuming there is a valid test image path
        file_path = "test_image.jpg"
        response = compress_image_post_method(file_path)
        self.assertIn('dest', response)
        self.assertNotIn('error', response)
        
    def test_compress_image_post_method_file_not_found(self):
        # Test with a non-existing file path
        file_path = "nonexistent.jpg"
        response = compress_image_post_method(file_path)
        self.assertIn('error', response)
        self.assertEqual(response['error'], "File not found")

if __name__ == '__main__':
    unittest.main()