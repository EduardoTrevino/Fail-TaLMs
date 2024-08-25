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


def mass_geocode_csv(file_path: str, columns: Optional[List[str]] = None, citycode: Optional[str] = None, postcode: Optional[str] = None, result_columns: Optional[List[str]] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Perform mass geocoding from a CSV file.
    Parameters:
    file_path [Required]: string - Path to the CSV file.
    columns [Optional]: list of strings - Columns to use for forming the address.
    citycode [Optional]: string - Column containing INSEE city code.
    postcode [Optional]: string - Column containing postal code.
    result_columns [Optional]: list of strings - Fields expected in the response.
    """
    url = "https://api-adresse.data.gouv.fr/search/csv/"
    files = {'data': open(file_path, 'rb')}
    data = {}

    if columns:
        for column in columns:
            data['columns'] = column

    if citycode:
        data['citycode'] = citycode

    if postcode:
        data['postcode'] = postcode

    if result_columns:
        for result_column in result_columns:
            data['result_columns'] = result_column

    response = requests.post(url, files=files, data=data)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def mass_reverse_geocode_csv(file_path: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Perform mass reverse geocoding from a CSV file.
    Parameters:
    file_path [Required]: string - Path to the CSV file.
    """
    url = "https://api-adresse.data.gouv.fr/reverse/csv/"
    files = {'data': open(file_path, 'rb')}
    
    response = requests.post(url, files=files)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}