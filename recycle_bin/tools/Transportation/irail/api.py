import requests
from typing import Optional

def liveboard(station: str, id: Optional[str] = None, arrdep: Optional[str] = "departure",
              date: Optional[str] = None, time: Optional[str] = None, format: Optional[str] = "json",
              lang: Optional[str] = "en", alerts: Optional[bool] = False, 
              toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve real-time information on arriving and departing trains for a specific station.
    """
    url = f"https://api.irail.be/liveboard/"
    params = {
        'station': station,
        'id': id,
        'arrdep': arrdep,
        'date': date,
        'time': time,
        'format': format,
        'lang': lang,
        'alerts': str(alerts).lower()
    }
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def connections(from_station: str, to_station: str, timesel: Optional[str] = "departure", typeOfTransport: Optional[str] = "automatic",
                alerts: Optional[bool] = False, results: Optional[int] = 6, time: Optional[str] = None, date: Optional[str] = None,
                format: Optional[str] = "json", lang: Optional[str] = "en",
                toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get routes between two stations, including real-time data on delays.
    """
    url = f"https://api.irail.be/connections/"
    params = {
        'from': from_station,
        'to': to_station,
        'timesel': timesel,
        'typeOfTransport': typeOfTransport,
        'alerts': str(alerts).lower(),
        'results': results,
        'time': time,
        'date': date,
        'format': format,
        'lang': lang
    }
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def vehicle(id: str, date: Optional[str] = None, format: Optional[str] = "json", lang: Optional[str] = "en", 
            alerts: Optional[bool] = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a vehicle, including stops, occupancy, current location and delays.
    """
    url = f"https://api.irail.be/vehicle/"
    params = {
        'id': id,
        'date': date,
        'format': format,
        'lang': lang,
        'alerts': str(alerts).lower()
    }
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
