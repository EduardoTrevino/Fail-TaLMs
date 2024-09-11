import requests
from typing import Optional, Any, Dict

# Configuring the base URL
BASE_URL = "https://aviationweather.gov/api"

def get_metar(
    ids: Optional[str] = None, 
    format: Optional[str] = 'json', 
    taf: Optional[bool] = False, 
    hours: Optional[int] = 1, 
    bbox: Optional[str] = None, 
    date: Optional[str] = None, 
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """Fetch METAR data"""
    endpoint = f"{BASE_URL}/data/metar"
    params = {
        "ids": ids,
        "format": format,
        "taf": taf,
        "hours": hours,
        "bbox": bbox,
        "date": date
    }
    response = requests.get(endpoint, params=params, headers={"Accept": "*/*"})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_taf(
    ids: Optional[str] = None, 
    format: Optional[str] = 'json', 
    metar: Optional[bool] = False, 
    bbox: Optional[str] = None, 
    time: Optional[str] = None, 
    date: Optional[str] = None, 
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """Fetch TAF data"""
    endpoint = f"{BASE_URL}/data/taf"
    params = {
        "ids": ids,
        "format": format,
        "metar": metar,
        "bbox": bbox,
        "time": time,
        "date": date
    }
    response = requests.get(endpoint, params=params, headers={"Accept": "*/*"})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_pirep(
    id: Optional[str] = None, 
    format: Optional[str] = 'raw', 
    age: Optional[int] = 1, 
    distance: Optional[int] = 0, 
    level: Optional[int] = 0, 
    inten: Optional[str] = None, 
    date: Optional[str] = None, 
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """Fetch PIREP data"""
    endpoint = f"{BASE_URL}/data/pirep"
    params = {
        "id": id,
        "format": format,
        "age": age,
        "distance": distance,
        "level": level,
        "inten": inten,
        "date": date
    }
    response = requests.get(endpoint, params=params, headers={"Accept": "*/*"})
    try:
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_airsigmet(
    format: Optional[str] = 'json', 
    type: Optional[str] = None, 
    hazard: Optional[str] = None, 
    level: Optional[int] = 0, 
    date: Optional[str] = None, 
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """Fetch AIRMET/SIGMET data"""
    endpoint = f"{BASE_URL}/data/airsigmet"
    params = {
        "format": format,
        "type": type,
        "hazard": hazard,
        "level": level,
        "date": date
    }
    response = requests.get(endpoint, params=params, headers={"Accept": "*/*"})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_isigmet(
    format: Optional[str] = 'json', 
    hazard: Optional[str] = None, 
    level: Optional[int] = 0, 
    date: Optional[str] = None, 
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """Fetch international SIGMETs"""
    endpoint = f"{BASE_URL}/data/isigmet"
    params = {
        "format": format,
        "hazard": hazard,
        "level": level,
        "date": date
    }
    response = requests.get(endpoint, params=params, headers={"Accept": "*/*"})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_gairmet(
    type: Optional[str] = None, 
    hazard: Optional[str] = None, 
    date: Optional[str] = None, 
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """Fetch Graphical AIRMETs"""
    endpoint = f"{BASE_URL}/data/gairmet"
    params = {
        "type": type,
        "hazard": hazard,
        "date": date
    }
    response = requests.get(endpoint, params=params, headers={"Accept": "*/*"})
    try:
        return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_cwa(
    hazard: Optional[str] = None, 
    date: Optional[str] = None, 
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """Fetch CWSU Center Advisories"""
    endpoint = f"{BASE_URL}/data/cwa"
    params = {
        "hazard": hazard,
        "date": date
    }
    response = requests.get(endpoint, params=params, headers={"Accept": "*/*"})
    try:
        return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_windtemp(
    region: Optional[str] = 'all', 
    level: Optional[str] = 'low', 
    fcst: Optional[str] = '06', 
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """Fetch Wind/Temp data"""
    endpoint = f"{BASE_URL}/data/windtemp"
    params = {
        "region": region,
        "level": level,
        "fcst": fcst
    }
    response = requests.get(endpoint, params=params, headers={"Accept": "*/*"})
    try:
        return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_areafcst(
    region: str,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """Fetch Area Forecasts"""
    endpoint = f"{BASE_URL}/data/areafcst"
    params = {
        "region": region
    }
    response = requests.get(endpoint, params=params, headers={"Accept": "*/*"})
    try:
        return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_fcstdisc(
    cwa: Optional[str] = None,
    type: Optional[str] = 'af',
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """Fetch Forecast Discussions"""
    endpoint = f"{BASE_URL}/data/fcstdisc"
    params = {
        "cwa": cwa,
        "type": type
    }
    response = requests.get(endpoint, params=params, headers={"Accept": "*/*"})
    try:
        return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_mis(
    loc: Optional[str] = None,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """Fetch Meteorological Information Statement"""
    endpoint = f"{BASE_URL}/data/mis"
    params = {
        "loc": loc
    }
    response = requests.get(endpoint, params=params, headers={"Accept": "*/*"})
    try:
        return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_stationinfo(
    ids: Optional[str] = None,
    bbox: Optional[str] = None,
    format: Optional[str] = 'json',
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """Fetch Station Info"""
    endpoint = f"{BASE_URL}/data/stationinfo"
    params = {
        "ids": ids,
        "bbox": bbox,
        "format": format
    }
    response = requests.get(endpoint, params=params, headers={"Accept": "*/*"})
    try:
        return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_airport(
    ids: Optional[str] = None,
    bbox: Optional[str] = None,
    format: Optional[str] = 'json',
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """Fetch Airport Info"""
    endpoint = f"{BASE_URL}/data/airport"
    params = {
        "ids": ids,
        "bbox": bbox,
        "format": format
    }
    response = requests.get(endpoint, params=params, headers={"Accept": "*/*"})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_feature(
    bbox: str,
    format: Optional[str] = 'json',
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """Fetch Feature Info"""
    endpoint = f"{BASE_URL}/data/feature"
    params = {
        "bbox": bbox,
        "format": format
    }
    response = requests.get(endpoint, params=params, headers={"Accept": "*/*"})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_obstacle(
    bbox: str,
    format: Optional[str] = 'json',
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """Fetch Obstacle Info"""
    endpoint = f"{BASE_URL}/data/obstacle"
    params = {
        "bbox": bbox,
        "format": format
    }
    response = requests.get(endpoint, params=params, headers={"Accept": "*/*"})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}