import requests
from typing import Optional

def get_elevation(dataset_name: str, locations: str, samples: Optional[int] = None, 
                  interpolation: Optional[str] = 'bilinear', nodata_value: Optional[str] = 'null', 
                  format: Optional[str] = 'json', 
                  toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches elevation data for specific locations using a specified dataset.
    
    Parameters:
    dataset_name [Required]: string - The name of the dataset to query.
    locations [Required]: string - Either latitude,longitude pairs separated by | or a Google polyline.
    samples [Optional]: int - Number of samples to query along the path specified by locations.
    interpolation [Optional]: string - Interpolation method (nearest, bilinear, cubic). Default is 'bilinear'.
    nodata_value [Optional]: string - What to return for NODATA values (null, nan, or an integer like -9999).
    format [Optional]: string - Response format (json or geojson). Default is 'json'.
    """
    url = f"https://api.opentopodata.org/v1/{dataset_name}"
    params = {
        'locations': locations,
        'samples': samples,
        'interpolation': interpolation,
        'nodata_value': nodata_value,
        'format': format,
    }
    
    # Clean up optional parameters if they are not provided
    params = {k: v for k, v in params.items() if v is not None}
    
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_health(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Healthcheck endpoint for the Open Topo Data API.
    """
    url = "https://api.opentopodata.org/health"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_datasets(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves a list of available datasets on the Open Topo Data server.
    """
    url = "https://api.opentopodata.org/datasets"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}