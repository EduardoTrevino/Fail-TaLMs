import requests
from typing import Optional, List


def search_address(q: str, limit: Optional[int] = 10, autocomplete: Optional[int] = 1, lat: Optional[float] = None, lon: Optional[float] = None, type_filter: Optional[str] = None, postcode: Optional[str] = None, citycode: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Perform a full-text address search with optional parameters.
    Parameters:
    q [Required]: string - The query string.
    limit [Optional]: integer - Maximum number of results to return.
    autocomplete [Optional]: integer - Enable or disable autocomplete processing.
    lat [Optional]: float - Latitude for geographic priority.
    lon [Optional]: float - Longitude for geographic priority.
    type_filter [Optional]: string - Filter by type (e.g., 'street').
    postcode [Optional]: string - Filter by postal code.
    citycode [Optional]: string - Filter by INSEE city code.
    """
    url = "https://api-adresse.data.gouv.fr/search/"
    params = {
        'q': q,
        'limit': limit,
        'autocomplete': autocomplete
    }
    if lat and lon:
        params.update({'lat': lat, 'lon': lon})
    if type_filter:
        params['type'] = type_filter
    if postcode:
        params['postcode'] = postcode
    if citycode:
        params['citycode'] = citycode

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def reverse_geocode(lat: float, lon: float, type_filter: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Perform reverse geocoding to get address from coordinates.
    Parameters:
    lat [Required]: float - Latitude of the point to reverse geocode.
    lon [Required]: float - Longitude of the point to reverse geocode.
    type_filter [Optional]: string - Type filter for the result.
    """
    url = "https://api-adresse.data.gouv.fr/reverse/"
    params = {
        'lat': lat,
        'lon': lon
    }
    if type_filter:
        params['type'] = type_filter

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}
