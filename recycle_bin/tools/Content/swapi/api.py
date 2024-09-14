import requests
from typing import Optional, Dict, Union, List

def get_all_planets(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all planets in the Star Wars universe.
    """
    url = "https://swapi.dev/api/planets/"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_person_details(id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get details of a specific person by ID.
    """
    url = f"https://swapi.dev/api/people/{id}/"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_film_details(id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get details of a specific film by ID.
    """
    url = f"https://swapi.dev/api/films/{id}/"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
