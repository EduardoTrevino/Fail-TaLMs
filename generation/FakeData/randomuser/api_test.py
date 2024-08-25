import unittest
from api import get_random_user, get_random_user_in_format


class TestRandomUserAPI(unittest.TestCase):

    def test_get_random_user(self):
        # Test retrieving a single random user
        response = get_random_user()
        self.assertIn('results', response)
        self.assertEqual(len(response['results']), 1)

    def test_get_random_users(self):
        # Test retrieving multiple random users
        response = get_random_user(results=5)
        self.assertIn('results', response)
        self.assertEqual(len(response['results']), 5)

    def test_get_random_user_with_seed(self):
        # Test retrieving a random user with a seed
        response1 = get_random_user(seed="abc")
        response2 = get_random_user(seed="abc")
        self.assertEqual(response1, response2)

    def test_get_random_user_with_gender(self):
        # Test retrieving random users filtered by gender
        response_male = get_random_user(gender="male")
        response_female = get_random_user(gender="female")
        self.assertEqual(response_male['results'][0]['gender'], "male")
        self.assertEqual(response_female['results'][0]['gender'], "female")

    def test_get_random_user_in_json_format(self):
        # Test retrieving a random user in JSON format
        response = get_random_user_in_format(format='json')
        self.assertIn('results', response)

    def test_get_random_user_in_xml_format(self):
        # Test retrieving a random user in XML format
        response = get_random_user_in_format(format='xml')
        self.assertTrue(response.startswith('<?xml'))

    def test_get_random_user_in_csv_format(self):
        # Test retrieving a random user in CSV format
        response = get_random_user_in_format(format='csv')
        self.assertIn('gender', response)

    def test_get_random_user_in_yaml_format(self):
        # Test retrieving a random user in YAML format
        response = get_random_user_in_format(format='yaml')
        self.assertIn('gender:', response)


if __name__ == '__main__':
    unittest.main()