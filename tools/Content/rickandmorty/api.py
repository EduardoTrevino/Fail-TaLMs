import requests
from typing import Optional, List, Union, Dict

def get_characters(page: Optional[int] = 1, name: Optional[str] = None, status: Optional[str] = None, species: Optional[str] = None, gender: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Endpoint to get all characters or filter them.
    
    Parameters:
    - page: Optional; the page of results to retrieve (default is 1).
    - name: Optional; filter by the given character name.
    - status: Optional; filter by the character's status ('alive', 'dead', or 'unknown').
    - species: Optional; filter by the character's species.
    - gender: Optional; filter by the character's gender ('female', 'male', 'genderless', or 'unknown').
    
    Returns: JSON response from the API containing characters data.
    """
    url = "https://rickandmortyapi.com/api/character"
    params = {
        "page": page,
        "name": name,
        "status": status,
        "species": species,
        "gender": gender
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_character_by_id(character_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Endpoint to get a single character by id.
    
    Parameters:
    - character_id: Required; ID of the character to be retrieved.

    Returns: JSON response from the API containing character data.
    """
    url = f"https://rickandmortyapi.com/api/character/{character_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_locations(page: Optional[int] = 1, name: Optional[str] = None, type: Optional[str] = None, dimension: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Endpoint to get all locations or filter them.
    
    Parameters:
    - page: Optional; the page of results to retrieve (default is 1).
    - name: Optional; filter by the given location name.
    - type: Optional; filter by the location type.
    - dimension: Optional; filter by the dimension.
    
    Returns: JSON response from the API containing locations data.
    """
    url = "https://rickandmortyapi.com/api/location"
    params = {
        "page": page,
        "name": name,
        "type": type,
        "dimension": dimension
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_location_by_id(location_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Endpoint to get a single location by id.
    
    Parameters:
    - location_id: Required; ID of the location to be retrieved.

    Returns: JSON response from the API containing location data.
    """
    url = f"https://rickandmortyapi.com/api/location/{location_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_episodes(page: Optional[int] = 1, name: Optional[str] = None, episode: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Endpoint to get all episodes or filter them.
    
    Parameters:
    - page: Optional; the page of results to retrieve (default is 1).
    - name: Optional; filter by the given episode name.
    - episode: Optional; filter by the episode code.
    
    Returns: JSON response from the API containing episodes data.
    """
    url = "https://rickandmortyapi.com/api/episode"
    params = {
        "page": page,
        "name": name,
        "episode": episode
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_episode_by_id(episode_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Endpoint to get a single episode by id.
    
    Parameters:
    - episode_id: Required; ID of the episode to be retrieved.

    Returns: JSON response from the API containing episode data.
    """
    url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}