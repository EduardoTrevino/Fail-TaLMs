import requests
from typing import Optional

BASE_URL = "https://swapi.dev/api/"

def fetch_resource(resource: str, resource_id: Optional[int] = None, search: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Generic function to fetch a resource from the SWAPI.

    Parameters:
    resource (str): The type of resource to fetch ('people', 'films', 'starships', 'vehicles', 'species', 'planets').
    resource_id (Optional[int]): The specific ID of the resource.
    search (Optional[str]): Search query to filter resources.
    """
    url = BASE_URL + resource + '/' + (str(resource_id) + '/' if resource_id else '')
    params = {}
    if search:
        params['search'] = search
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_people(resource_id: Optional[int] = None, search: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch people resources or a specific person.
    """
    return fetch_resource('people', resource_id, search, toolbench_rapidapi_key)

def get_films(resource_id: Optional[int] = None, search: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch film resources or a specific film.
    """
    return fetch_resource('films', resource_id, search, toolbench_rapidapi_key)

def get_starships(resource_id: Optional[int] = None, search: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch starship resources or a specific starship.
    """
    return fetch_resource('starships', resource_id, search, toolbench_rapidapi_key)

def get_vehicles(resource_id: Optional[int] = None, search: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch vehicle resources or a specific vehicle.
    """
    return fetch_resource('vehicles', resource_id, search, toolbench_rapidapi_key)

def get_species(resource_id: Optional[int] = None, search: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch species resources or a specific species.
    """
    return fetch_resource('species', resource_id, search, toolbench_rapidapi_key)

def get_planets(resource_id: Optional[int] = None, search: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch planets resources or a specific planet.
    """
    return fetch_resource('planets', resource_id, search, toolbench_rapidapi_key)