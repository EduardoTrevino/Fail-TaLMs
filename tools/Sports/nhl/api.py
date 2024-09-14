import requests
from typing import Optional

# Function to get player spotlight data
def get_player_spotlight(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Sends a GET request to the /v1/player-spotlight endpoint to retrieve player spotlight data.

    Returns:
        Response object containing the player spotlight data in JSON format.
    """
    url = 'http://api-web.nhle.com/v1/player-spotlight'
    response = requests.get(url)
    return response

# Function to get standings for a specific date
def get_standings(date: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Sends a GET request to the /v1/standings/{date} endpoint to retrieve standings for the given date.

    Args:
        date (str): The date for which the standings are requested (format: YYYY-MM-DD).

    Returns:
        Response object containing the standings data in JSON format.
    """
    url = f'http://api-web.nhle.com/v1/standings/{date}'
    response = requests.get(url)
    return response

# Function to get season standings
def get_standings_season(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Sends a GET request to the /v1/standings-season endpoint to retrieve season standings data.

    Returns:
        Response object containing the season standings data in JSON format.
    """
    url = 'http://api-web.nhle.com/v1/standings-season'
    response = requests.get(url)
    return response

# Function to get player game log
def get_player_game_log(player_id: int, season: int, game_type: int,toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Sends a GET request to the /v1/player/{player_id}/game-log/{season}/{game_type} endpoint 
    to retrieve game log data for the specified player, season, and game type.

    Args:
        player_id (int): The ID of the player.
        season (int): The season for which the game log is requested.
        game_type (int): The type of game (e.g., regular season, playoffs).

    Returns:
        Response object containing the player game log data in JSON format.
    """
    url = f'http://api-web.nhle.com/v1/player/{player_id}/game-log/{season}/{game_type}'
    response = requests.get(url)
    return response

# Function to get player landing data
def get_player_landing(player_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Sends a GET request to the /v1/player/{player_id}/landing endpoint to retrieve player landing data.

    Args:
        player_id (int): The ID of the player.

    Returns:
        Response object containing the player landing data in JSON format.
    """
    url = f'http://api-web.nhle.com/v1/player/{player_id}/landing'
    response = requests.get(url)
    return response

# Function to get score data for a specific date
def get_score(date: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Sends a GET request to the /v1/score/{date} endpoint to retrieve score data for the given date.

    Args:
        date (str): The date for which the score data is requested (format: YYYY-MM-DD).

    Returns:
        Response object containing the score data in JSON format.
    """
    url = f'http://api-web.nhle.com/v1/score/{date}'
    response = requests.get(url)
    return response

# Function to get location data
def get_location(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Sends a GET request to the /v1/location endpoint to retrieve location data.

    Returns:
        Response object containing the location data in JSON format.
    """
    url = 'http://api-web.nhle.com/v1/location'
    response = requests.get(url)
    return response

# Function to get schedule data for a specific date
def get_schedule(date: str,toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Sends a GET request to the /v1/schedule/{date} endpoint to retrieve schedule data for the given date.

    Args:
        date (str): The date for which the schedule data is requested (format: YYYY-MM-DD).

    Returns:
        Response object containing the schedule data in JSON format.
    """
    url = f'http://api-web.nhle.com/v1/schedule/{date}'
    response = requests.get(url)
    return response

# Function to get schedule calendar data for a specific date
def get_schedule_calendar(date: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Sends a GET request to the /v1/schedule-calendar/{date} endpoint to retrieve schedule calendar data for the given date.

    Args:
        date (str): The date for which the schedule calendar data is requested (format: YYYY-MM-DD).

    Returns:
        Response object containing the schedule calendar data in JSON format.
    """
    url = f'http://api-web.nhle.com/v1/schedule-calendar/{date}'
    response = requests.get(url)
    return response