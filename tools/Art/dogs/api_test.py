import unittest
from api import (
    list_all_breeds,
    random_image,
    random_images,
    images_by_breed,
    random_image_by_breed,
    random_images_by_breed,
    list_sub_breeds,
    images_by_sub_breed,
    random_image_by_sub_breed,
    random_images_by_sub_breed
)

class TestDogAPI(unittest.TestCase):
    
    def test_list_all_breeds(self):
        result = list_all_breeds()
        self.assertIsInstance(result, dict)
        self.assertEqual(result['status'], 'success')
        self.assertIn('message', result)

    def test_random_image(self):
        result = random_image()
        self.assertIsInstance(result, dict)
        self.assertEqual(result['status'], 'success')
        self.assertIn('message', result)

    def test_random_images(self):
        result = random_images()
        self.assertIsInstance(result, dict)
        self.assertEqual(result['status'], 'success')
        self.assertIn('message', result)
        self.assertEqual(len(result['message']), 3)

    def test_images_by_breed(self):
        result = images_by_breed('hound')
        self.assertIsInstance(result, dict)
        self.assertEqual(result['status'], 'success')
        self.assertIn('message', result)
        self.assertIsInstance(result['message'], list)

    def test_random_image_by_breed(self):
        result = random_image_by_breed('hound')
        self.assertIsInstance(result, dict)
        self.assertEqual(result['status'], 'success')
        self.assertIn('message', result)

    def test_random_images_by_breed(self):
        result = random_images_by_breed('hound', 3)
        self.assertIsInstance(result, dict)
        self.assertEqual(result['status'], 'success')
        self.assertIn('message', result)
        self.assertEqual(len(result['message']), 3)

    def test_list_sub_breeds(self):
        result = list_sub_breeds('hound')
        self.assertIsInstance(result, dict)
        self.assertEqual(result['status'], 'success')
        self.assertIn('message', result)
        self.assertIsInstance(result['message'], list)

    def test_images_by_sub_breed(self):
        result = images_by_sub_breed('hound', 'afghan')
        self.assertIsInstance(result, dict)
        self.assertEqual(result['status'], 'success')
        self.assertIn('message', result)
        self.assertIsInstance(result['message'], list)

    def test_random_image_by_sub_breed(self):
        result = random_image_by_sub_breed('hound', 'afghan')
        self.assertIsInstance(result, dict)
        self.assertEqual(result['status'], 'success')
        self.assertIn('message', result)

    def test_random_images_by_sub_breed(self):
        result = random_images_by_sub_breed('hound', 'afghan', 3)
        self.assertIsInstance(result, dict)
        self.assertEqual(result['status'], 'success')
        self.assertIn('message', result)
        self.assertEqual(len(result['message']), 3)

if __name__ == '__main__':
    unittest.main()