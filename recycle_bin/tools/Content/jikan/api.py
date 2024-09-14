import requests
import json
from typing import Optional, Dict, List

def get_anime_by_id(id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve information about a specific anime by its MyAnimeList ID.
    """
    url = f"https://api.jikan.moe/v4/anime/{id}"
    
    response = requests.get(url)
    try:
        data = response.json()
    except:
        data = response.text
    return data

def get_anime_characters(id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve the characters of a specific anime by its MyAnimeList ID.
    """
    url = f"https://api.jikan.moe/v4/anime/{id}/characters"
    
    response = requests.get(url)
    try:
        data = response.json()
    except:
        data = response.text
    return data

def get_anime_staff(id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve the staff of a specific anime by its MyAnimeList ID.
    """
    url = f"https://api.jikan.moe/v4/anime/{id}/staff"
    
    response = requests.get(url)
    try:
        data = response.json()
    except:
        data = response.text
    return data
