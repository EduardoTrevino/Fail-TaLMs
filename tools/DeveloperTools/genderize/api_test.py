import unittest
from api import check_gender, check_genders

class TestGenderizeAPI(unittest.TestCase):

    def test_check_gender(self):
        result = check_gender(name="peter")
        self.assertIn('name', result)
        self.assertIn('gender', result)
        self.assertIn('probability', result)
        self.assertIn('count', result)

    def test_check_gender_with_country(self):
        result = check_gender(name="kim", country_id="US")
        self.assertIn('name', result)
        self.assertIn('gender', result)
        self.assertIn('probability', result)
        self.assertIn('count', result)
        self.assertIn('country_id', result)
        self.assertEqual(result['country_id'], "US")

    def test_check_genders(self):
        result = check_genders(names=["peter", "lois", "stewie"])
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        for gender_info in result:
            self.assertIn('name', gender_info)
            self.assertIn('gender', gender_info)
            self.assertIn('probability', gender_info)
            self.assertIn('count', gender_info)

    def test_check_genders_with_country(self):
        result = check_genders(names=["kim", "sasha"], country_id="DK")
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        for gender_info in result:
            self.assertIn('country_id', gender_info)
            self.assertEqual(gender_info['country_id'], "DK")

if __name__ == "__main__":
    unittest.main()