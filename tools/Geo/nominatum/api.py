import requests
from typing import Optional, List

BASE_URL = "https://nominatim.openstreetmap.org"

def search(
    q: Optional[str] = None,
    amenity: Optional[str] = None,
    street: Optional[str] = None,
    city: Optional[str] = None,
    county: Optional[str] = None,
    state: Optional[str] = None,
    country: Optional[str] = None,
    postalcode: Optional[str] = None,
    format: str = "jsonv2",
    limit: int = 10,
    addressdetails: int = 0,
    extratags: int = 0,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff',
    **kwargs
):
    """
    Search OSM objects by name or type.
    Parameters:
    - q: Free-form query string to search for
    - amenity, street, city, county, state, country, postalcode: structured query parameters
    - format: Desired format of the response (default is jsonv2)
    - limit: Maximum number of results to return (default is 10)
    - addressdetails: Include a breakdown of the address into elements (default is 0)
    - extratags: Include additional information if available (default is 0)
    """
    if q and (amenity or street or city or county or state or country or postalcode):
        raise ValueError("Cannot use both free-form query 'q' and structured query parameters.")
    
    url = f"{BASE_URL}/search"
    params = {
        "format": format,
        "limit": limit,
        "addressdetails": addressdetails,
        "extratags": extratags,
    }
    if q:
        params["q"] = q
    else:
        params.update({
            "amenity": amenity,
            "street": street,
            "city": city,
            "county": county,
            "state": state,
            "country": country,
            "postalcode": postalcode,
        })
    params.update(kwargs)
    
    response = requests.get(url, params=params)
    return response.text

def reverse(
    lat: float,
    lon: float,
    format: Optional[str] = "jsonv2",
    addressdetails: int = 1,
    extratags: int = 0,
    namedetails: int = 0,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff',
    **kwargs
):
    """
    Reverse search OSM object by their location.
    Parameters:
    - lat: Latitude of the location
    - lon: Longitude of the location
    - format: Desired format of the response (default is jsonv2)
    - addressdetails: Include a breakdown of the address into elements (default is 1)
    - extratags: Include additional information if available (default is 0)
    - namedetails: Include a full list of names for the result (default is 0)
    """
    url = f"{BASE_URL}/reverse"
    params = {
        "lat": lat,
        "lon": lon,
        "format": format,
        "addressdetails": addressdetails,
        "extratags": extratags,
        "namedetails": namedetails,
    }
    params.update(kwargs)
    
    response = requests.get(url, params=params)
    return response.text

def lookup(
    osm_ids: List[str],
    format: Optional[str] = "jsonv2",
    addressdetails: int = 0,
    extratags: int = 0,
    namedetails: int = 0,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff',
    **kwargs
):
    """
    Look up address details for OSM objects by their ID.
    Parameters:
    - osm_ids: List of OSM ids, prefixed by type (N, W, R)
    - format: Desired format of the response (default is jsonv2)
    - addressdetails: Include a breakdown of the address into elements (default is 0)
    - extratags: Include additional information if available (default is 0)
    - namedetails: Include a full list of names for the result (default is 0)
    """
    if not osm_ids:
        raise ValueError("At least one OSM ID is required.")
    
    url = f"{BASE_URL}/lookup"
    params = {
        "osm_ids": ','.join(osm_ids),
        "format": format,
        "addressdetails": addressdetails,
        "extratags": extratags,
        "namedetails": namedetails,
    }
    params.update(kwargs)
    
    response = requests.get(url, params=params)
    return response.text

def status(
    format: Optional[str] = "text",
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
):
    """
    Query the status of the server.
    Parameters:
    - format: Desired format of the response (default is text)
    """
    url = f"{BASE_URL}/status"
    params = {
        "format": format
    }
    
    response = requests.get(url, params=params)
    if format == "json":
        return response.json()
    return response.text