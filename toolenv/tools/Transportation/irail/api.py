import requests
from typing import Optional, Dict, List

def liveboard(station: str, id: Optional[str] = None, arrdep: str = 'departure', date: Optional[str] = None, 
              time: Optional[str] = None, format: str = 'json', lang: str = 'en', alerts: bool = False, 
              toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve real-time information on arriving and departing trains for a specific station.
    """
    url = "https://api.irail.be/liveboard/"
    querystring = {
        'station': station,
        'id': id,
        'arrdep': arrdep,
        'date': date,
        'time': time,
        'format': format,
        'lang': lang,
        'alerts': alerts
    }
    headers = {
        "X-RapidAPI-Key": toolbench_rapidapi_key
    }

    response = requests.get(url, headers=headers, params={k: v for k, v in querystring.items() if v is not None})
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def connections(from_station: str, to_station: str, timesel: str = 'departure', typeOfTransport: str = 'automatic', 
                alerts: bool = False, results: int = 6, time: Optional[str] = None, date: Optional[str] = None, 
                format: str = 'json', lang: str = 'en', 
                toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get routes between two stations, including real-time data on delays.
    """
    url = "https://api.irail.be/connections/"
    querystring = {
        'from': from_station,
        'to': to_station,
        'timesel': timesel,
        'typeOfTransport': typeOfTransport,
        'alerts': alerts,
        'results': results,
        'time': time,
        'date': date,
        'format': format,
        'lang': lang
    }
    headers = {
        "X-RapidAPI-Key": toolbench_rapidapi_key
    }

    response = requests.get(url, headers=headers, params={k: v for k, v in querystring.items() if v is not None})
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def vehicle(id: str, date: Optional[str] = None, format: str = 'json', lang: str = 'en', alerts: bool = False, 
            toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a vehicle, including stops, occupancy, current location, and delays.
    """
    url = "https://api.irail.be/vehicle/"
    querystring = {
        'id': id,
        'date': date,
        'format': format,
        'lang': lang,
        'alerts': alerts
    }
    headers = {
        "X-RapidAPI-Key": toolbench_rapidapi_key
    }

    response = requests.get(url, headers=headers, params={k: v for k, v in querystring.items() if v is not None})
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation