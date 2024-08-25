import requests
from typing import Optional, List

def get_brewery_by_id(obdb_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a single brewery by its OBDB ID.
    """
    url = f"https://api.openbrewerydb.org/v1/breweries/{obdb_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_breweries(page: Optional[int] = 1, per_page: Optional[int] = 50, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a list of breweries with pagination.
    """
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {
        'page': page,
        'per_page': per_page
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_random_brewery(size: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a random brewery.
    """
    url = "https://api.openbrewerydb.org/v1/breweries/random"
    params = {
        'size': size
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search_breweries(query: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for breweries based on a search term.
    """
    url = "https://api.openbrewerydb.org/v1/breweries/search"
    params = {
        'query': query
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def autocomplete_breweries(query: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Return a list of names and ids of breweries for autocomplete.
    """
    url = "https://api.openbrewerydb.org/v1/breweries/autocomplete"
    params = {
        'query': query
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_breweries_metadata(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get metadata for breweries.
    """
    url = "https://api.openbrewerydb.org/v1/breweries/meta"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}