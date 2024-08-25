import unittest
from api import get_iss_location, get_people_in_space

class TestOpenNotifyAPI(unittest.TestCase):

    def test_get_iss_location(self):
        result = get_iss_location()
        self.assertIn('iss_position', result)
        self.assertIn('latitude', result['iss_position'])
        self.assertIn('longitude', result['iss_position'])
        self.assertEqual(result['message'], 'success')

    def test_get_people_in_space(self):
        result = get_people_in_space()
        self.assertIn('number', result)
        self.assertIn('people', result)
        self.assertEqual(result['message'], 'success')
        self.assertIsInstance(result['people'], list)

if __name__ == '__main__':
    unittest.main()