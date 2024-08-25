import unittest
from api import *

class TestNHLAPI(unittest.TestCase):

    def test_get_awards(self):
        response = get_awards()
        self.assertIn('awards', response)

    def test_get_award(self):
        response = get_award(1)
        self.assertIn('awards', response)

    def test_get_conferences(self):
        response = get_conferences()
        self.assertIn('conferences', response)

    def test_get_conference(self):
        response = get_conference(6)
        self.assertIn('conferences', response)
    
    def test_get_divisions(self):
        response = get_divisions()
        self.assertIn('divisions', response)

    def test_get_division(self):
        response = get_division(17)
        self.assertIn('divisions', response)

    def test_get_franchises(self):
        response = get_franchises()
        self.assertIn('franchises', response)

    def test_get_franchise(self):
        response = get_franchise(1)
        self.assertIn('franchises', response)

    def test_get_tournament_types(self):
        response = get_tournament_types()
        self.assertIn('types', response)

    def test_get_tournaments_playoffs(self):
        response = get_tournaments_playoffs()
        self.assertIn('name', response)

    def test_get_venues(self):
        response = get_venues()
        self.assertIn('venues', response)

    def test_get_venue(self):
        response = get_venue(5064)
        self.assertIn('venues', response)

    def test_get_game_live_feed(self):
        response = get_game_live_feed(2017020010)
        self.assertIn('gameData', response)

    def test_get_game_boxscore(self):
        response = get_game_boxscore(2017020010)
        self.assertIn('teams', response)

    def test_get_game_linescore(self):
        response = get_game_linescore(2017020010)
        self.assertIn('teams', response)

    def test_get_game_content(self):
        response = get_game_content(2017020010)
        self.assertIn('media', response)

    def test_get_game_statuses(self):
        response = get_game_statuses()
        self.assertIsInstance(response, list)

    def test_get_game_types(self):
        response = get_game_types()
        self.assertIsInstance(response, list)

    def test_get_play_types(self):
        response = get_play_types()
        self.assertIsInstance(response, list)

    def test_get_draft(self):
        response = get_draft()
        self.assertIn('drafts', response)

    def test_get_draft_year(self):
        response = get_draft(2021)
        self.assertIn('drafts', response)

    def test_get_people(self):
        response = get_people(8477474)
        self.assertIn('people', response)

    def test_get_people_stats(self):
        response = get_people_stats(8477474)
        self.assertIn('stats', response)

    def test_get_positions(self):
        response = get_positions()
        self.assertIsInstance(response, list)

    def test_get_prospects(self):
        response = get_prospects()
        self.assertIn('prospects', response)

    def test_get_schedule(self):
        response = get_schedule()
        self.assertIn('dates', response)

    def test_get_seasons(self):
        response = get_seasons()
        self.assertIn('seasons', response)

    def test_get_season(self):
        response = get_season("20172018")
        self.assertIn('seasons', response)

    def test_get_current_season(self):
        response = get_current_season()
        self.assertIn('seasons', response)

    def test_get_standings(self):
        response = get_standings()
        self.assertIn('teamRecords', response)

    def test_get_standings_types(self):
        response = get_standings_types()
        self.assertIsInstance(response, list)

    def test_get_team_stats(self):
        response = get_team_stats(5)
        self.assertIn('stats', response)

    def test_get_teams(self):
        response = get_teams()
        self.assertIn('teams', response)

    def test_get_team_roster(self):
        response = get_team_roster(5)
        self.assertIn('roster', response)

    def test_get_configurations(self):
        response = get_configurations()
        self.assertIsInstance(response, dict)

if __name__ == '__main__':
    unittest.main()