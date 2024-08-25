import requests
from typing import Optional, List, Union


def get_representatives_by_postal_code(postal_code: str, sets: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Find representatives and boundaries by postal code, optionally limiting results to a specific boundary set.
    
    :param postal_code: The postal code in uppercase letters with no spaces.
    :param sets: Optional boundary set to limit results.
    :return: JSON response from the API.
    """
    url = f"https://represent.opennorth.ca/postcodes/{postal_code}/"
    params = {'sets': sets} if sets else {}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_boundary_sets(limit: Optional[int] = 20, offset: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get one page of boundary sets.
    
    :param limit: Optional number of results per page.
    :param offset: Optional number for page offset.
    :return: JSON response from the API containing the boundary sets.
    """
    url = "https://represent.opennorth.ca/boundary-sets/"
    params = {
        'limit': limit,
        'offset': offset
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_boundaries(sets: Optional[str] = None, name: Optional[str] = None, contains: Optional[str] = None, limit: Optional[int] = 20, offset: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get one page of boundaries, optionally filtering by boundary sets, names, or geospatial queries.
    
    :param sets: Optional comma-separated list of boundary sets.
    :param name: Optional name to filter boundaries.
    :param contains: Optional latitude and longitude for geospatial query.
    :param limit: Optional number of results per page.
    :param offset: Optional number for page offset.
    :return: JSON response from the API.
    """
    url = "https://represent.opennorth.ca/boundaries/"
    params = {
        'sets': sets,
        'name': name,
        'contains': contains,
        'limit': limit,
        'offset': offset
    }
    response = requests.get(url, params={key: value for key, value in params.items() if value is not None})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_representative_sets(limit: Optional[int] = 20, offset: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get one page of representative sets.
    
    :param limit: Optional number of results per page.
    :param offset: Optional number for page offset.
    :return: JSON response from the API.
    """
    url = "https://represent.opennorth.ca/representative-sets/"
    params = {
        'limit': limit,
        'offset': offset
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_representatives(limit: Optional[int] = 20, offset: Optional[int] = 0, last_name: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get one page of representatives, optionally filtering by last name.
    
    :param limit: Optional number of results per page.
    :param offset: Optional number for page offset.
    :param last_name: Optional last name of the representative to filter results.
    :return: JSON response from the API.
    """
    url = "https://represent.opennorth.ca/representatives/"
    params = {
        'limit': limit,
        'offset': offset,
        'last_name': last_name
    }
    response = requests.get(url, params={key: value for key, value in params.items() if value is not None})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_elections(limit: Optional[int] = 20, offset: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get one page of elections.
    
    :param limit: Optional number of results per page.
    :param offset: Optional number for page offset.
    :return: JSON response from the API.
    """
    url = "https://represent.opennorth.ca/elections/"
    params = {
        'limit': limit,
        'offset': offset
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_candidates(limit: Optional[int] = 20, offset: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get one page of candidates.
    
    :param limit: Optional number of results per page.
    :param offset: Optional number for page offset.
    :return: JSON response from the API.
    """
    url = "https://represent.opennorth.ca/candidates/"
    params = {
        'limit': limit,
        'offset': offset
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}