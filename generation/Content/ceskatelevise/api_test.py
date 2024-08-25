import unittest
from api import get_tv_schedule

class TestCeskateleviseAPI(unittest.TestCase):
    def test_get_tv_schedule_xml(self):
        user = "test"
        date = "04.08.2024"
        channel = "ct24"
        response = get_tv_schedule(user, date, channel)
        self.assertIn("<?xml", response)

    def test_get_tv_schedule_json(self):
        user = "test"
        date = "04.08.2024"
        channel = "ct6"
        response = get_tv_schedule(user, date, channel, json_format=1)
        self.assertTrue(response.startswith("{") and response.endswith("}"))

    def test_get_tv_schedule_with_region(self):
        user = "test"
        date = "04.08.2024"
        channel = "ct1"
        response = get_tv_schedule(user, date, channel, regiony=1)
        self.assertIn("<?xml", response)

if __name__ == '__main__':
    unittest.main()