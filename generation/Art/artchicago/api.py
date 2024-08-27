import requests
from typing import Optional, List

BASE_URL = "https://api.artic.edu/api/v1"

def artworks(ids: Optional[str] = None, limit: Optional[int] = 2, page: Optional[int] = 1, fields: Optional[str] = None, include: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve artworks data.
    """
    url = f"{BASE_URL}/artworks"
    params = {
        'ids': ids,
        'limit': limit,
        'page': page,
        'fields': fields,
        'include': include
    }
    response = requests.get(url, params=params)
    return response.json()

def artworks_search(q: str, query: Optional[str] = None, sort: Optional[str] = None, from_: Optional[int] = 0, size: Optional[int] = 10, facets: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search Artworks at the chicago museum
    """
    url = f"{BASE_URL}/artworks/search"
    params = {
        'q': q,
        'query': query,
        'sort': sort,
        'from': from_,
        'size': size,
        'facets': facets
    }
    response = requests.get(url, params=params)
    return response.json()

def artwork_by_id(artwork_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve artwork by ID.
    """
    url = f"{BASE_URL}/artworks/{artwork_id}"
    response = requests.get(url)
    return response.json()

def artwork_manifest(artwork_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve artwork manifest in IIIF format.
    """
    url = f"{BASE_URL}/artworks/{artwork_id}/manifest.json"
    response = requests.get(url)
    return response.json()

def agents(ids: Optional[str] = None, limit: Optional[int] = 2, page: Optional[int] = 1, fields: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve agents data. "agents" likely refers to entities such as organizations, artists, or other relevant individuals associated with the data being provided. The structure includes metadata about the entities, such as titles, alternative titles, and descriptions, along with pagination information.
    """
    url = f"{BASE_URL}/agents"
    params = {
        'ids': ids,
        'limit': limit,
        'page': page,
        'fields': fields
    }
    response = requests.get(url, params=params)
    return response.json()

def agents_search(q: str, query: Optional[str] = None, sort: Optional[str] = None, from_: Optional[int] = 0, size: Optional[int] = 10, facets: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search agents. "agents" likely refers to entities such as organizations, artists, or other relevant individuals associated with the data being provided. The structure includes metadata about the entities, such as titles, alternative titles, and descriptions, along with pagination information.
    """
    url = f"{BASE_URL}/agents/search"
    params = {
        'q': q,
        'query': query,
        'sort': sort,
        'from': from_,
        'size': size,
        'facets': facets
    }
    response = requests.get(url, params=params)
    return response.json()

def agent_by_id(agent_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for agents by ID.
    """
    url = f"{BASE_URL}/agents/{agent_id}"
    response = requests.get(url)
    return response.json()

def places(ids: Optional[str] = None, limit: Optional[int] = 2, page: Optional[int] = 1, fields: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Paginated List of Places
    """
    url = f"{BASE_URL}/places"
    params = {
        'ids': ids,
        'limit': limit,
        'page': page,
        'fields': fields
    }
    response = requests.get(url, params=params)
    return response.json()

def places_search(q: str, query: Optional[str] = None, sort: Optional[str] = None, from_: Optional[int] = 0, size: Optional[int] = 10, facets: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search Results for Places
    """
    url = f"{BASE_URL}/places/search"
    params = {
        'q': q,
        'query': query,
        'sort': sort,
        'from': from_,
        'size': size,
        'facets': facets
    }
    response = requests.get(url, params=params)
    return response.json()

# def place_by_id(place_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
#     url = f"{BASE_URL}/places/{place_id}"
#     response = requests.get(url)
#     return response.json()

# More functions for other endpoints should follow the same pattern