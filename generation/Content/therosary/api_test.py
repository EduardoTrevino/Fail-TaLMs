import unittest
from api import *

class TestTheRosaryAPI(unittest.TestCase):

    def test_get_today_prayer(self):
        response = get_today_prayer()
        self.assertIsInstance(response, list)

    def test_get_yesterday_prayer(self):
        response = get_yesterday_prayer()
        self.assertIsInstance(response, list)

    def test_get_tomorrow_prayer(self):
        response = get_tomorrow_prayer()
        self.assertIsInstance(response, list)

    def test_get_prayer_by_day(self):
        response = get_prayer_by_day("monday")
        self.assertIsInstance(response, list)

    def test_get_prayer_by_date(self):
        response = get_prayer_by_date("082824")
        self.assertIsInstance(response, dict)

    def test_get_random_prayer(self):
        response = get_random_prayer()
        self.assertIsInstance(response, dict)

    def test_get_yearly_prayer_list(self):
        response = get_yearly_prayer_list()
        self.assertIsInstance(response, list)

    def test_get_joyful_prayer(self):
        response = get_joyful_prayer()
        self.assertIsInstance(response, list)

    def test_get_glorious_prayer(self):
        response = get_glorious_prayer()
        self.assertIsInstance(response, list)

    def test_get_sorrowful_prayer(self):
        response = get_sorrowful_prayer()
        self.assertIsInstance(response, list)

    def test_get_luminous_prayer(self):
        response = get_luminous_prayer()
        self.assertIsInstance(response, list)

    def test_get_novena_prayer(self):
        response = get_novena_prayer()
        self.assertIsInstance(response, list)

    def test_get_novena_prayer_by_date(self):
        response = get_novena_prayer_by_date("155")
        self.assertIsInstance(response, list)

    def test_get_54day_novena_prayer(self):
        response = get_54day_novena_prayer()
        self.assertIsInstance(response, list)

if __name__ == '__main__':
    unittest.main()