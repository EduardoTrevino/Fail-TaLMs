import requests
from typing import Optional, List


# def get_area_by_id(area_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
#     """
#     Get details of one particular area by its ID.
    
#     Parameters:
#     area_id (int): The ID of the area.
#     """
#     url = f"https://api.football-data.org/v4/areas/{area_id}"
#     headers = {
#         'X-Auth-Token': toolbench_rapidapi_key
#     }
#     response = requests.get(url, headers=headers)
#     try:
#         return response.json()
#     except Exception as e:
#         return {"error": str(e), "response": response.text}


# def list_areas(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
#     """
#     List all available areas.
#     """
#     url = "https://api.football-data.org/v4/areas"
#     headers = {
#         'X-Auth-Token': toolbench_rapidapi_key
#     }
#     response = requests.get(url, headers=headers)
#     try:
#         return response.json()
#     except Exception as e:
#         return {"error": str(e), "response": response.text}


# def get_competition_by_code(competition_code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
#     """
#     Get details of one particular competition by its code.
    
#     Parameters:
#     competition_code (str): The code of the competition.
#     """
#     url = f"https://api.football-data.org/v4/competitions/{competition_code}"
#     headers = {
#         'X-Auth-Token': toolbench_rapidapi_key
#     }
#     response = requests.get(url, headers=headers)
#     try:
#         return response.json()
#     except Exception as e:
#         return {"error": str(e), "response": response.text}


def list_competitions(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', areas: Optional[str] = None):
    """
    List all available competitions.
    
    Parameters:
    areas (str): Comma separated list of area IDs.
    """
    url = "https://api.football-data.org/v4/competitions"
    params = {}
    if areas:
        params['areas'] = areas
    
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


# def get_competition_standings(competition_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', season: Optional[int] = None):
#     """
#     Show standings for a particular competition.
    
#     Parameters:
#     competition_id (int): The ID of the competition.
#     season (int): The starting year of the season.
#     """
#     url = f"https://api.football-data.org/v4/competitions/{competition_id}/standings"
#     headers = {
#         'X-Auth-Token': toolbench_rapidapi_key
#     }
#     params = {}
#     if season:
#         params['season'] = season
    
#     response = requests.get(url, headers=headers, params=params)
#     try:
#         return response.json()
#     except Exception as e:
#         return {"error": str(e), "response": response.text}


# def get_matches_for_competition(competition_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', matchday: Optional[int] = None):
#     """
#     List all matches for a particular competition.
    
#     Parameters:
#     competition_id (int): The ID of the competition.
#     matchday (int): The matchday to retrieve matches for.
#     """
#     url = f"https://api.football-data.org/v4/competitions/{competition_id}/matches"
#     headers = {
#         'X-Auth-Token': toolbench_rapidapi_key
#     }
#     params = {}
#     if matchday:
#         params['matchday'] = matchday
    
#     response = requests.get(url, headers=headers, params=params)
#     try:
#         return response.json()
#     except Exception as e:
#         return {"error": str(e), "response": response.text}


# def get_team_info(team_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
#     """
#     Show information about one particular team by its ID.
    
#     Parameters:
#     team_id (int): The ID of the team.
#     """
#     url = f"https://api.football-data.org/v4/teams/{team_id}"
#     headers = {
#         'X-Auth-Token': toolbench_rapidapi_key
#     }
#     response = requests.get(url, headers=headers)
#     try:
#         return response.json()
#     except Exception as e:
#         return {"error": str(e), "response": response.text}


# def list_teams(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', limit: Optional[int] = 10, offset: Optional[int] = 0):
#     """
#     List all teams with pagination.
    
#     Parameters:
#     limit (int): Number of teams to retrieve.
#     offset (int): Number of teams to skip.
#     """
#     url = "https://api.football-data.org/v4/teams/"
#     headers = {
#         'X-Auth-Token': toolbench_rapidapi_key
#     }
#     params = {
#         'limit': limit,
#         'offset': offset
#     }
    
#     response = requests.get(url, headers=headers, params=params)
#     try:
#         return response.json()
#     except Exception as e:
#         return {"error": str(e), "response": response.text}


# def get_player_info(player_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
#     """
#     Show information about one particular player by their ID.
    
#     Parameters:
#     player_id (int): The ID of the player.
#     """
#     url = f"https://api.football-data.org/v4/persons/{player_id}"
#     headers = {
#         'X-Auth-Token': toolbench_rapidapi_key
#     }
#     response = requests.get(url, headers=headers)
#     try:
#         return response.json()
#     except Exception as e:
#         return {"error": str(e), "response": response.text}


# def list_matches_across_competitions(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', date_from: Optional[str] = None, date_to: Optional[str] = None, competitions: Optional[str] = None):
#     """
#     List matches across a set of competitions.
    
#     Parameters:
#     date_from (str): The start date for matches.
#     date_to (str): The end date for matches.
#     competitions (str): Comma separated list of competition IDs.
#     """
#     url = "https://api.football-data.org/v4/matches"
#     headers = {
#         'X-Auth-Token': toolbench_rapidapi_key
#     }
#     params = {}
#     if date_from:
#         params['dateFrom'] = date_from
#     if date_to:
#         params['dateTo'] = date_to
#     if competitions:
#         params['competitions'] = competitions
    
#     response = requests.get(url, headers=headers, params=params)
#     try:
#         return response.json()
#     except Exception as e:
#         return {"error": str(e), "response": response.text}


# def get_match_by_id(match_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
#     """
#     Show one particular match by its ID.
    
#     Parameters:
#     match_id (int): The ID of the match.
#     """
#     url = f"https://api.football-data.org/v4/matches/{match_id}"
#     headers = {
#         'X-Auth-Token': toolbench_rapidapi_key
#     }
#     response = requests.get(url, headers=headers)
#     try:
#         return response.json()
#     except Exception as e:
#         return {"error": str(e), "response": response.text}


# def list_head2head_matches(match_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', limit: Optional[int] = 10):
#     """
#     List previous encounters for the teams of a match.
    
#     Parameters:
#     match_id (int): The ID of the match.
#     limit (int): Number of encounters to retrieve.
#     """
#     url = f"https://api.football-data.org/v4/matches/{match_id}/head2head"
#     headers = {
#         'X-Auth-Token': toolbench_rapidapi_key
#     }
#     params = {'limit': limit}
    
#     response = requests.get(url, headers=headers, params=params)
#     try:
#         return response.json()
#     except Exception as e:
#         return {"error": str(e), "response": response.text}