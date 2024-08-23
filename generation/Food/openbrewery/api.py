import requests
from typing import Optional, List

def single_brewery(obdb_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a single brewery by ID.
    Parameters:
     - obdb_id [Required]: string [The ID of the brewery]
    """
    url = f"https://api.openbrewerydb.org/v1/breweries/{obdb_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_breweries(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a list of breweries.
    """
    url = "https://api.openbrewerydb.org/v1/breweries"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def random_brewery(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a random brewery.
    """
    url = "https://api.openbrewerydb.org/v1/breweries/random"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search_breweries(query: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search breweries by a search term.
    Parameters:
     - query [Required]: string [The search term]
    """
    url = f"https://api.openbrewerydb.org/v1/breweries/search?query={query}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def autocomplete(query: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Return a list of names and ids of breweries based on a search term.
    Parameters:
     - query [Required]: string [The search term]
    """
    url = f"https://api.openbrewerydb.org/v1/breweries/autocomplete?query={query}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def breweries_by_city(city: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Filter breweries by city.
    Parameters:
     - city [Required]: string [The city to filter by]
    """
    url = f"https://api.openbrewerydb.org/v1/breweries?by_city={city}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def breweries_by_state(state: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Filter breweries by state (full state name).
    Parameters:
     - state [Required]: string [The state to filter by]
    """
    url = f"https://api.openbrewerydb.org/v1/breweries?by_state={state}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def breweries_by_postal(postal: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Filter breweries by postal code.
    Parameters:
     - postal [Required]: string [The postal code to filter by]
    """
    url = f"https://api.openbrewerydb.org/v1/breweries?by_postal={postal}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def breweries_by_type(brewery_type: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Filter breweries by type.
    Parameters:
     - brewery_type [Required]: string [The type of brewery to filter by]
    """
    url = f"https://api.openbrewerydb.org/v1/breweries?by_type={brewery_type}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def breweries_by_name(name: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Filter breweries by name.
    Parameters:
     - name [Required]: string [The name to filter by]
    """
    url = f"https://api.openbrewerydb.org/v1/breweries?by_name={name}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def breweries_by_dist(lat: float, lon: float, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Sort the results by distance from an origin point, denoted by latitude and longitude.
    Parameters:
     - lat [Required]: float [The latitude]
     - lon [Required]: float [The longitude]
    """
    url = f"https://api.openbrewerydb.org/v1/breweries?by_dist={lat},{lon}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def breweries_by_ids(ids: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Filter breweries by a comma-separated list of brewery IDs.
    Parameters:
     - ids [Required]: string [Comma-separated list of brewery IDs]
    """
    url = f"https://api.openbrewerydb.org/v1/breweries?by_ids={ids}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def breweries_metadata(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get breweries metadata.
    """
    url = "https://api.openbrewerydb.org/v1/breweries/meta"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}