import requests
from typing import Optional, Dict

BASE_URL = "https://www.freetogame.com/api"


def list_games(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve a list of all free-to-play games.
    """
    url = f"{BASE_URL}/games"
    response = requests.get(url)
    return response.json()


def game_details(game_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve details of a specific game by its ID.
    
    Parameters:
    - game_id: int : The ID of the game.
    """
    url = f"{BASE_URL}/game"
    params = {'id': game_id}
    response = requests.get(url, params=params)
    return response.json()


def games_by_category(category: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve a list of all available games from a specific genre.
    
    Parameters:
    - category: str : The category name (e.g., mmorpg, shooter).
    """
    url = f"{BASE_URL}/games"
    params = {'category': category}
    response = requests.get(url, params=params)
    return response.json()


def games_by_platform(platform: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve a list of all available games from a specific platform.
    
    Parameters:
    - platform: str : The platform name (e.g., pc, browser).
    """
    url = f"{BASE_URL}/games"
    params = {'platform': platform}
    response = requests.get(url, params=params)
    return response.json()


def sorted_games(sort_by: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Sort games by release date, alphabetical or relevance.
    
    Parameters:
    - sort_by: str : Sort criteria (e.g., release-date, popularity, alphabetical).
    """
    url = f"{BASE_URL}/games"
    params = {'sort-by': sort_by}
    response = requests.get(url, params=params)
    return response.json()


def games_by_filters(tag: Optional[str] = None, platform: Optional[str] = None, sort: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Filter games by multiple tags, platform, and sort.
    
    Parameters:
    - tag: str : Comma-separated list of tags (optional).
    - platform: str : Platform name (optional).
    - sort: str : Sort criteria (optional).
    """
    url = f"{BASE_URL}/filter"
    params = {}
    if tag:
        params['tag'] = tag
    if platform:
        params['platform'] = platform
    if sort:
        params['sort'] = sort

    response = requests.get(url, params=params)
    return response.json()