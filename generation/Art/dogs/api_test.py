import unittest
import api

class TestDogAPI(unittest.TestCase):

    def test_list_all_breeds(self):
        result = api.list_all_breeds()
        self.assertIn("message", result)
        self.assertIn("status", result)
        self.assertEqual(result["status"], "success")
    
    def test_random_image_from_all_dogs(self):
        result = api.random_image_from_all_dogs()
        self.assertIn("message", result)
        self.assertIn("status", result)
        self.assertEqual(result["status"], "success")
        
    def test_multiple_random_images(self):
        result = api.multiple_random_images(count=3)
        self.assertIn("message", result)
        self.assertIn("status", result)
        self.assertEqual(result["status"], "success")
        self.assertIsInstance(result["message"], list)
        self.assertEqual(len(result["message"]), 3)
    
    def test_images_by_breed(self):
        result = api.images_by_breed(breed="hound")
        self.assertIn("message", result)
        self.assertIn("status", result)
        self.assertEqual(result["status"], "success")
        self.assertIsInstance(result["message"], list)
    
    def test_random_image_by_breed(self):
        result = api.random_image_by_breed(breed="hound")
        self.assertIn("message", result)
        self.assertIn("status", result)
        self.assertEqual(result["status"], "success")
    
    def test_multiple_random_images_by_breed(self):
        result = api.multiple_random_images_by_breed(breed="hound", count=3)
        self.assertIn("message", result)
        self.assertIn("status", result)
        self.assertEqual(result["status"], "success")
        self.assertIsInstance(result["message"], list)
        self.assertEqual(len(result["message"]), 3)
    
    def test_list_all_sub_breeds(self):
        result = api.list_all_sub_breeds(breed="hound")
        self.assertIn("message", result)
        self.assertIn("status", result)
        self.assertEqual(result["status"], "success")
        self.assertIsInstance(result["message"], list)
    
    def test_images_by_sub_breed(self):
        result = api.images_by_sub_breed(breed="hound", sub_breed="afghan")
        self.assertIn("message", result)
        self.assertIn("status", result)
        self.assertEqual(result["status"], "success")
        self.assertIsInstance(result["message"], list)
    
    def test_random_image_by_sub_breed(self):
        result = api.random_image_by_sub_breed(breed="hound", sub_breed="afghan")
        self.assertIn("message", result)
        self.assertIn("status", result)
        self.assertEqual(result["status"], "success")
    
    def test_multiple_random_images_by_sub_breed(self):
        result = api.multiple_random_images_by_sub_breed(breed="hound", sub_breed="afghan", count=3)
        self.assertIn("message", result)
        self.assertIn("status", result)
        self.assertEqual(result["status"], "success")
        self.assertIsInstance(result["message"], list)
        self.assertEqual(len(result["message"]), 3)

if __name__ == '__main__':
    unittest.main()