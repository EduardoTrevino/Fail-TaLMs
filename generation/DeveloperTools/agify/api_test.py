import unittest
from api import estimate_age, estimate_age_batch

class TestAgifyAPI(unittest.TestCase):

    def test_estimate_age(self):
        response = estimate_age(name="michael")
        self.assertIn("age", response)
        self.assertIn("count", response)
        self.assertEqual(response["name"], "michael")

    def test_estimate_age_with_country(self):
        response = estimate_age(name="michael", country_id="US")
        self.assertIn("age", response)
        self.assertIn("count", response)
        self.assertEqual(response["name"], "michael")
        self.assertEqual(response["country_id"], "US")

    def test_estimate_age_batch(self):
        response = estimate_age_batch(names=["michael", "matthew", "jane"])
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 3)
        for item in response:
            self.assertIn("age", item)
            self.assertIn("count", item)
            self.assertIn("name", item)

    def test_estimate_age_batch_with_country(self):
        response = estimate_age_batch(names=["michael", "matthew", "jane"], country_id="US")
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 3)
        for item in response:
            self.assertIn("age", item)
            self.assertIn("count", item)
            self.assertIn("name", item)
            self.assertEqual(item.get("country_id"), "US")