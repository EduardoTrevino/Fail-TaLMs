import requests
from typing import Optional, List

def character(id: Optional[int] = None, page: Optional[int] = 1, name: Optional[str] = None, status: Optional[str] = None, species: Optional[str] = None, type: Optional[str] = None, gender: Optional[str] = None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all characters or a single character by ID.
    """
    url = "https://rickandmortyapi.com/api/character"
    if id:
        url += f"/{id}"
    querystring = {
        "page": page,
        "name": name,
        "status": status,
        "species": species,
        "type": type,
        "gender": gender
    }
    response = requests.get(url, params={k: v for k, v in querystring.items() if v is not None})
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def location(id: Optional[int] = None, name: Optional[str] = None, type: Optional[str] = None, dimension: Optional[str] = None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all locations or a single location by ID.
    """
    url = "https://rickandmortyapi.com/api/location"
    if id:
        url += f"/{id}"
    querystring = {
        "name": name,
        "type": type,
        "dimension": dimension
    }
    response = requests.get(url, params={k: v for k, v in querystring.items() if v is not None})
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def episode(id: Optional[int] = None, name: Optional[str] = None, episode: Optional[str] = None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all episodes or a single episode by ID.
    """
    url = "https://rickandmortyapi.com/api/episode"
    if id:
        url += f"/{id}"
    querystring = {
        "name": name,
        "episode": episode
    }
    response = requests.get(url, params={k: v for k, v in querystring.items() if v is not None})
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
