import unittest
from api import *

class SpaceXAPITestCase(unittest.TestCase):

    def test_get_all_capsules(self):
        response = get_all_capsules()
        self.assertIsInstance(response, list)

    def test_get_capsule_by_id(self):
        response = get_capsule_by_id("5e9e2c5bf35918ed873b2664")
        self.assertIsInstance(response, dict)
        self.assertIn("serial", response)

    def test_query_capsules(self):
        response = query_capsules({}, {})
        self.assertIsInstance(response, dict)

    def test_get_company_info(self):
        response = get_company_info()
        self.assertIsInstance(response, dict)
        self.assertIn("name", response)

    def test_get_all_cores(self):
        response = get_all_cores()
        self.assertIsInstance(response, list)

    def test_get_core_by_id(self):
        response = get_core_by_id("5e9e28a6f35918c0803b265c")
        self.assertIsInstance(response, dict)
        self.assertIn("serial", response)

    def test_query_cores(self):
        response = query_cores({}, {})
        self.assertIsInstance(response, dict)

    def test_get_all_crew(self):
        response = get_all_crew()
        self.assertIsInstance(response, list)

    def test_get_crew_member_by_id(self):
        response = get_crew_member_by_id("5ebf1a6e23a9a60006e03a7a")
        self.assertIsInstance(response, dict)
        self.assertIn("name", response)

    def test_query_crew_members(self):
        response = query_crew_members({}, {})
        self.assertIsInstance(response, dict)

    def test_get_all_dragons(self):
        response = get_all_dragons()
        self.assertIsInstance(response, list)

    def test_get_dragon_by_id(self):
        response = get_dragon_by_id("5e9d058759b1ff74a7ad5f8f")
        self.assertIsInstance(response, dict)
        self.assertIn("name", response)

    def test_query_dragons(self):
        response = query_dragons({}, {})
        self.assertIsInstance(response, dict)

    def test_get_all_history_events(self):
        response = get_all_history_events()
        self.assertIsInstance(response, list)

    def test_get_history_event_by_id(self):
        response = get_history_event_by_id("5f6fb2cfdcfdf403df37971e")
        self.assertIsInstance(response, dict)
        self.assertIn("title", response)

    def test_query_history_events(self):
        response = query_history_events({}, {})
        self.assertIsInstance(response, dict)

    def test_get_all_landing_pads(self):
        response = get_all_landing_pads()
        self.assertIsInstance(response, list)

    def test_get_landing_pad_by_id(self):
        response = get_landing_pad_by_id("5e9e3032383ecb90a834e7c8")
        self.assertIsInstance(response, dict)
        self.assertIn("name", response)

    def test_query_landing_pads(self):
        response = query_landing_pads({}, {})
        self.assertIsInstance(response, dict)

    def test_get_all_launches(self):
        response = get_all_launches()
        self.assertIsInstance(response, list)

    def test_get_next_launch(self):
        response = get_next_launch()
        self.assertIsInstance(response, dict)
        self.assertIn("name", response)

    def test_get_launch_by_id(self):
        response = get_launch_by_id("5eb87d42ffd86e000604b384")
        self.assertIsInstance(response, dict)
        self.assertIn("name", response)

    def test_get_all_past_launches(self):
        response = get_all_past_launches()
        self.assertIsInstance(response, list)

    def test_query_launches(self):
        response = query_launches({}, {})
        self.assertIsInstance(response, dict)

    def test_get_all_upcoming_launches(self):
        response = get_all_upcoming_launches()
        self.assertIsInstance(response, list)

    def test_get_all_launchpads(self):
        response = get_all_launchpads()
        self.assertIsInstance(response, list)

    def test_get_launchpad_by_id(self):
        response = get_launchpad_by_id("5e9e4502f509092b78566f87")
        self.assertIsInstance(response, dict)
        self.assertIn("name", response)

    def test_query_launchpads(self):
        response = query_launchpads({}, {})
        self.assertIsInstance(response, dict)

    def test_get_all_payloads(self):
        response = get_all_payloads()
        self.assertIsInstance(response, list)

    def test_get_payload_by_id(self):
        response = get_payload_by_id("5eb0e4c6b6c3bb0006eeb21e")
        self.assertIsInstance(response, dict)
        self.assertIn("name", response)

    def test_query_payloads(self):
        response = query_payloads({}, {})
        self.assertIsInstance(response, dict)

    def test_get_roadster_info(self):
        response = get_roadster_info()
        self.assertIsInstance(response, dict)
        self.assertIn("name", response)

    def test_get_all_rockets(self):
        response = get_all_rockets()
        self.assertIsInstance(response, list)

    def test_get_rocket_by_id(self):
        response = get_rocket_by_id("5e9d0d95eda69974db09d1ed")
        self.assertIsInstance(response, dict)
        self.assertIn("name", response)

    def test_query_rockets(self):
        response = query_rockets({}, {})
        self.assertIsInstance(response, dict)

    def test_get_all_ships(self):
        response = get_all_ships()
        self.assertIsInstance(response, list)

    def test_get_ship_by_id(self):
        response = get_ship_by_id("5ea6ed2e080df4000697c90a")
        self.assertIsInstance(response, dict)
        self.assertIn("name", response)

    def test_query_ships(self):
        response = query_ships({}, {})
        self.assertIsInstance(response, dict)

if __name__ == "__main__":
    unittest.main()