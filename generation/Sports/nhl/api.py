import requests
from typing import Optional

# API_BASE_URL = "https://api-web.nhle.com/v1" # works but not with these endpoints
API_BASE_URL = "https://statsapi.web.nhl.com/api/v1"

def get_awards(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/awards"
    response = requests.get(url)
    return response.json()

def get_award(award_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/awards/{award_id}"
    response = requests.get(url)
    return response.json()

def get_conferences(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/conferences"
    response = requests.get(url)
    return response.json()

def get_conference(conference_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/conferences/{conference_id}"
    response = requests.get(url)
    return response.json()

def get_divisions(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/divisions"
    response = requests.get(url)
    return response.json()

def get_division(division_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/divisions/{division_id}"
    response = requests.get(url)
    return response.json()

def get_franchises(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/franchises"
    response = requests.get(url)
    return response.json()

def get_franchise(franchise_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/franchises/{franchise_id}"
    response = requests.get(url)
    return response.json()

def get_tournament_types(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/tournamentTypes"
    response = requests.get(url)
    return response.json()

def get_tournaments_playoffs(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/tournaments/playoffs"
    response = requests.get(url)
    return response.json()

def get_venues(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/venues"
    response = requests.get(url)
    return response.json()

def get_venue(venue_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/venues/{venue_id}"
    response = requests.get(url)
    return response.json()

def get_game_live_feed(game_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/game/{game_id}/feed/live"
    response = requests.get(url)
    return response.json()

def get_game_boxscore(game_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/game/{game_id}/boxscore"
    response = requests.get(url)
    return response.json()

def get_game_linescore(game_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/game/{game_id}/linescore"
    response = requests.get(url)
    return response.json()

def get_game_content(game_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/game/{game_id}/content"
    response = requests.get(url)
    return response.json()

def get_game_statuses(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/gameStatus"
    response = requests.get(url)
    return response.json()

def get_game_types(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/gameTypes"
    response = requests.get(url)
    return response.json()

def get_play_types(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/playTypes"
    response = requests.get(url)
    return response.json()

def get_draft(year: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/draft"
    if year:
        url += f"/{year}"
    response = requests.get(url)
    return response.json()

def get_people(person_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/people/{person_id}"
    response = requests.get(url)
    return response.json()

def get_people_stats(person_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/people/{person_id}/stats"
    response = requests.get(url)
    return response.json()

def get_positions(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/positions"
    response = requests.get(url)
    return response.json()

def get_prospects(prospect_id: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/draft/prospects"
    if prospect_id:
        url += f"/{prospect_id}"
    response = requests.get(url)
    return response.json()

def get_schedule(start_date: Optional[str] = None, end_date: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/schedule"
    params = {}
    if start_date:
        params['startDate'] = start_date
    if end_date:
        params['endDate'] = end_date
    response = requests.get(url, params=params)
    return response.json()

def get_seasons(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/seasons"
    response = requests.get(url)
    return response.json()

def get_season(season_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/seasons/{season_id}"
    response = requests.get(url)
    return response.json()

def get_current_season(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/seasons/current"
    response = requests.get(url)
    return response.json()

def get_standings(season: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/standings"
    if season:
        url += f"?season={season}"
    response = requests.get(url)
    return response.json()

def get_standings_types(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/standingsTypes"
    response = requests.get(url)
    return response.json()

def get_team_stats(team_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/teams/{team_id}/stats"
    response = requests.get(url)
    return response.json()

def get_teams(team_id: Optional[int] = None, expand: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/teams"
    if team_id:
        url += f"/{team_id}"
    params = {}
    if expand:
        params['expand'] = expand
    response = requests.get(url, params=params)
    return response.json()

def get_team_roster(team_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/teams/{team_id}/roster"
    response = requests.get(url)
    return response.json()

def get_configurations(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{API_BASE_URL}/configurations"
    response = requests.get(url)
    return response.json()