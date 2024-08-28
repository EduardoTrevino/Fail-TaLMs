import unittest
from api import list_competitions
# from api import (
#     get_area_by_id, list_areas, get_competition_by_code, list_competitions, 
#     get_competition_standings, get_matches_for_competition, get_team_info,
#     list_teams, get_player_info, list_matches_across_competitions,
#     get_match_by_id, list_head2head_matches
# )

class TestSoccerDataAPI(unittest.TestCase):

    # def test_get_area_by_id(self):
    #     response = get_area_by_id(2267)
    #     self.assertIn("id", response)
    #     self.assertEqual(response["id"], 2267)

    # def test_list_areas(self):
    #     response = list_areas()
    #     self.assertIn("areas", response)
    #     self.assertIsInstance(response["areas"], list)

    # def test_get_competition_by_code(self):
    #     response = get_competition_by_code("PL")
    #     self.assertIn("code", response)
    #     self.assertEqual(response["code"], "PL")

    def test_list_competitions(self):
        response = list_competitions()
        self.assertIn("competitions", response)
        self.assertIsInstance(response["competitions"], list)

    # def test_get_competition_standings(self):
    #     response = get_competition_standings(2021)
    #     self.assertIn("competition", response)
    #     self.assertEqual(response["competition"]["id"], 2021)

    # def test_get_matches_for_competition(self):
    #     response = get_matches_for_competition(2002)
    #     self.assertIn("matches", response)
    #     self.assertIsInstance(response["matches"], list)

    # def test_get_team_info(self):
    #     response = get_team_info(66)
    #     self.assertIn("id", response)
    #     self.assertEqual(response["id"], 66)

    # def test_list_teams(self):
    #     response = list_teams()
    #     self.assertIn("teams", response)
    #     self.assertIsInstance(response["teams"], list)

    # def test_get_player_info(self):
    #     response = get_player_info(44)
    #     self.assertIn("id", response)
    #     self.assertEqual(response["id"], 44)

    # def test_list_matches_across_competitions(self):
    #     response = list_matches_across_competitions(date_from="2022-05-17", date_to="2022-05-18")
    #     self.assertIn("matches", response)
    #     self.assertIsInstance(response["matches"], list)

    # def test_get_match_by_id(self):
    #     response = get_match_by_id(327117)
    #     self.assertIn("id", response)
    #     self.assertEqual(response["id"], 327117)

    # def test_list_head2head_matches(self):
    #     response = list_head2head_matches(327125)
    #     self.assertIn("matches", response)
    #     self.assertIsInstance(response["matches"], list)

if __name__ == '__main__':
    unittest.main()