import requests
from typing import Optional

def forward_geocode(location: str, output_format: Optional[str] = "json", region: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Perform forward geocoding to convert a place name into geographic coordinates.
    Parameters:
    location [Required]: The location as a string (e.g., street address, postal code).
    output_format [Optional]: Format of the output (default is "json"). Allowed values: "xml", "json", "csv".
    region [Optional]: Limit search to a specific region (e.g., "UK").
    """
    url = "https://geocode.xyz/"
    params = {
        'locate': location,
        'auth': toolbench_rapidapi_key
    }
    
    if output_format == "json":
        params['json'] = 1
    elif output_format:
        params['geoit'] = output_format
        
    if region:
        params['region'] = region

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def reverse_geocode(latitude: float, longitude: float, output_format: Optional[str] = "json", region: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Perform reverse geocoding to convert geographic coordinates into a descriptive location.
    Parameters:
    latitude [Required]: The latitude as a float.
    longitude [Required]: The longitude as a float.
    output_format [Optional]: Format of the output (default is "json"). Allowed values: "xml", "json", "csv".
    region [Optional]: Limit search to a specific region (e.g., "UK").
    """
    url = "https://geocode.xyz/"
    params = {
        'locate': f"{latitude},{longitude}",
        'auth': toolbench_rapidapi_key
    }
    
    if output_format == "json":
        params['json'] = 1
    elif output_format:
        params['geoit'] = output_format
        
    if region:
        params['region'] = region

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def geoparse(scantext: str, output_format: Optional[str] = "json", sentiment: Optional[bool] = False, region: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Geoparse free-text descriptions to extract and geocode place names.
    Parameters:
    scantext [Required]: Free-form text containing locations.
    output_format [Optional]: Format of the output (default is "json"). Allowed values: "xml", "json", "geojson".
    sentiment [Optional]: Perform sentiment analysis as well (default is False). Allowed values: True, False.
    region [Optional]: Limit search to a specific region (e.g., "NL").
    """
    url = "https://geocode.xyz/"
    params = {
        'scantext': scantext,
        'auth': toolbench_rapidapi_key
    }
    
    if output_format == "json":
        params['json'] = 1
    elif output_format == "geojson":
        params['geojson'] = 1
    elif output_format:
        params['geoit'] = output_format
    
    if sentiment:
        params['sentiment'] = 1
        
    if region:
        params['region'] = region

    response = requests.post(url, data=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}