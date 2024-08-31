import unittest
from api import (
    get_all_giveaways,
    get_giveaway_by_id,
    get_giveaways_by_platform,
    get_giveaways_by_type,
    get_giveaways_sorted,
    get_total_worth
)

class TestGamerPowerAPI(unittest.TestCase):

    def test_get_all_giveaways(self):
        response = get_all_giveaways()
        self.assertIsInstance(response, list)

    def test_get_giveaway_by_id(self):
        response = get_giveaway_by_id(525)
        self.assertIsInstance(response, dict)
        self.assertIn("id", response)
        self.assertEqual(response["id"], 525)

    def test_get_giveaways_by_platform(self):
        response = get_giveaways_by_platform("pc")
        self.assertIsInstance(response, list)

    def test_get_giveaways_by_type(self):
        response = get_giveaways_by_type("game")
        self.assertIsInstance(response, list)

    def test_get_giveaways_sorted(self):
        response = get_giveaways_sorted("value")
        self.assertIsInstance(response, list)

    def test_get_total_worth(self):
        response = get_total_worth()
        self.assertIsInstance(response, dict)
        self.assertIn("worth_estimation_usd", response)

if __name__ == "__main__":
    unittest.main()