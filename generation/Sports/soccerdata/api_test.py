import unittest
from api import list_competitions
# from api import (
#     get_area_by_id, list_areas, get_competition_by_code, list_competitions, 
#     get_competition_standings, get_matches_for_competition, get_team_info,
#     list_teams, get_player_info, list_matches_across_competitions,
#     get_match_by_id, list_head2head_matches
# )

class TestSoccerDataAPI(unittest.TestCase):
    def test_list_competitions(self):
        response = list_competitions()
        self.assertIn("competitions", response)
        self.assertIsInstance(response["competitions"], list)

if __name__ == '__main__':
    unittest.main()