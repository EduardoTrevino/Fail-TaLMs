import requests

BASE_URL = "https://finalspaceapi.com/api/v0/"

def get_all_characters(sort: str = None, limit: int = None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all characters from Final Space.
    """
    url = f"{BASE_URL}character"
    params = {}
    if sort:
        params['sort'] = sort
    if limit:
        params['limit'] = limit
    
    response = requests.get(url, params=params)
    return response.json()

def get_single_character(character_id: int):
    """
    Get details of a single character by ID.
    """
    url = f"{BASE_URL}character/{character_id}"
    response = requests.get(url)
    return response.json()

def get_all_episodes(sort: str = None, limit: int = None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all episodes from Final Space.
    """
    url = f"{BASE_URL}episode"
    params = {}
    if sort:
        params['sort'] = sort
    if limit:
        params['limit'] = limit
    
    response = requests.get(url, params=params)
    return response.json()

# Example usage:
# print(get_all_characters(sort="desc", limit=5))
# print(get_single_character(1))
# print(get_all_episodes(sort="asc", limit=3))
