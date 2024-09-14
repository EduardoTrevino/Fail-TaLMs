import requests
from typing import Optional

BASE_URL = "https://finalspaceapi.com/api/v0/"

def get_all_characters(sort: Optional[str] = None, limit: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves all characters, with options to sort and limit the results.
    
    Parameters:
    sort [Optional]: string - Sort the list in 'asc' (ascending) or 'desc' (descending) order.
    limit [Optional]: integer - Limits the number of characters returned.
    
    Returns:
    JSON response with characters details.
    """
    url = f"{BASE_URL}character"
    params = {}
    if sort:
        params['sort'] = sort
    if limit:
        params['limit'] = limit
    
    response = requests.get(url, params=params)
    return response.json()

def get_character_by_id(character_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves a character by its ID.
    
    Parameters:
    character_id [Required]: integer - The ID of the character to retrieve.
    
    Returns:
    JSON response with character details for the specified ID.
    """
    url = f"{BASE_URL}character/{character_id}"
    response = requests.get(url)
    return response.json()

def get_all_episodes(sort: Optional[str] = None, limit: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves all episodes, with options to sort and limit the results.
    
    Parameters:
    sort [Optional]: string - Sort the list in 'asc' (ascending) or 'desc' (descending) order.
    limit [Optional]: integer - Limits the number of episodes returned.
    
    Returns:
    JSON response with episodes details.
    """
    url = f"{BASE_URL}episode"
    params = {}
    if sort:
        params['sort'] = sort
    if limit:
        params['limit'] = limit
    
    response = requests.get(url, params=params)
    return response.json()

def get_episode_by_id(episode_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves an episode by its ID.
    
    Parameters:
    episode_id [Required]: integer - The ID of the episode to retrieve.
    
    Returns:
    JSON response with episode details for the specified ID.
    """
    url = f"{BASE_URL}episode/{episode_id}"
    response = requests.get(url)
    return response.json()

def get_all_locations(sort: Optional[str] = None, limit: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves all locations, with options to sort and limit the results.
    
    Parameters:
    sort [Optional]: string - Sort the list in 'asc' (ascending) or 'desc' (descending) order.
    limit [Optional]: integer - Limits the number of locations returned.
    
    Returns:
    JSON response with locations details.
    """
    url = f"{BASE_URL}location"
    params = {}
    if sort:
        params['sort'] = sort
    if limit:
        params['limit'] = limit
    
    response = requests.get(url, params=params)
    return response.json()

def get_location_by_id(location_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves a location by its ID.
    
    Parameters:
    location_id [Required]: integer - The ID of the location to retrieve.
    
    Returns:
    JSON response with location details for the specified ID.
    """
    url = f"{BASE_URL}location/{location_id}"
    response = requests.get(url)
    return response.json()

def get_all_quotes(sort: Optional[str] = None, limit: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves all quotes, with options to sort and limit the results.
    
    Parameters:
    sort [Optional]: string - Sort the list in 'asc' (ascending) or 'desc' (descending) order.
    limit [Optional]: integer - Limits the number of quotes returned.
    
    Returns:
    JSON response with quotes details.
    """
    url = f"{BASE_URL}quote"
    params = {}
    if sort:
        params['sort'] = sort
    if limit:
        params['limit'] = limit
    
    response = requests.get(url, params=params)
    return response.json()