import requests
from typing import Optional

def application_json(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Request known enumerated parameter values for the interface.
    """
    url = "https://earthquake.usgs.gov/fdsnws/event/1/application.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def application_wadl(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Request WADL for the interface.
    """
    url = "https://earthquake.usgs.gov/fdsnws/event/1/application.wadl"
    response = requests.get(url)
    try:
        return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def catalogs(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Request available catalogs.
    """
    url = "https://earthquake.usgs.gov/fdsnws/event/1/catalogs"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def contributors(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Request available contributors.
    """
    url = "https://earthquake.usgs.gov/fdsnws/event/1/contributors"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def count(format: Optional[str] = "geojson", starttime: Optional[str] = None, endtime: Optional[str] = None, minmagnitude: Optional[float] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Perform a count on a data request.
    """
    url = "https://earthquake.usgs.gov/fdsnws/event/1/count"
    params = {
        'format': format,
        'starttime': starttime,
        'endtime': endtime,
        'minmagnitude': minmagnitude
    }
    response = requests.get(url, params=params)
    try:
        if format == 'geojson':
            return response.json()
        else:
            return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def query(format: Optional[str] = "geojson", starttime: Optional[str] = None, endtime: Optional[str] = None, minmagnitude: Optional[float] = None, maxmagnitude: Optional[float] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Submit a data request.
    """
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        'format': format,
        'starttime': starttime,
        'endtime': endtime,
        'minmagnitude': minmagnitude,
        'maxmagnitude': maxmagnitude
    }
    response = requests.get(url, params=params)
    try:
        if format == 'geojson':
            return response.json()
        else:
            return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def version(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Request full service version number.
    """
    url = "https://earthquake.usgs.gov/fdsnws/event/1/version"
    response = requests.get(url)
    try:
        return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}