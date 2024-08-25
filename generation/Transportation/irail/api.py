import requests
from typing import Optional, List

BASE_URL = "https://api.irail.be"

def stations(format: str = "json", lang: str = "en", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a list of all stations.

    :param format: The response format (json, xml, jsonp).
    :param lang: The language of any text or names in the response.
    """
    url = f"{BASE_URL}/stations/"
    params = {
        'format': format,
        'lang': lang,
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def liveboard(station: str, id: Optional[str] = None, date: Optional[str] = None, time: Optional[str] = None,
              arrdep: str = "departure", lang: str = "en", format: str = "json", alerts: bool = False,
              toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a liveboard for a specified station.

    :param station: The name of the station to query.
    :param id: Optional station ID.
    :param date: Date for query, formatted as ddmmyy.
    :param time: Time for query, formatted as hhmm.
    :param arrdep: Whether to retrieve departures or arrivals.
    :param lang: The language of the response.
    :param format: The output format (json, xml, jsonp).
    :param alerts: Whether to include alerts.
    """
    url = f"{BASE_URL}/liveboard/"
    params = {
        'station': station,
        'id': id,
        'date': date,
        'time': time,
        'arrdep': arrdep,
        'lang': lang,
        'format': format,
        'alerts': alerts
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def connections(from_station: str, to_station: str, date: str, time: str, timesel: str = "departure",
                format: str = "json", lang: str = "en", typeOfTransport: str = "automatic", alerts: bool = False,
                results: int = 6, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get routes between two stations, including realtime data on delays.

    :param from_station: The departure station.
    :param to_station: The destination station.
    :param date: Date for the query, formatted as ddmmyy.
    :param time: Time for the query, formatted as hhmm.
    :param timesel: Whether results should show arrivals or departures.
    :param format: The response format.
    :param lang: The language of the response.
    :param typeOfTransport: Types of transport to include.
    :param alerts: Include alerts or not.
    :param results: Number of results to return.
    """
    url = f"{BASE_URL}/connections/"
    params = {
        'from': from_station,
        'to': to_station,
        'date': date,
        'time': time,
        'timesel': timesel,
        'format': format,
        'lang': lang,
        'typeOfTransport': typeOfTransport,
        'alerts': alerts,
        'results': results
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def vehicle(id: str, date: Optional[str] = None, format: str = "json", lang: str = "en", alerts: bool = False,
            toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a vehicle including stops and delays.

    :param id: The ID of the vehicle.
    :param date: Date for the query, formatted as ddmmyy.
    :param format: The response format.
    :param lang: The language of the response.
    :param alerts: Include alerts or not.
    """
    url = f"{BASE_URL}/vehicle/"
    params = {
        'id': id,
        'date': date,
        'format': format,
        'lang': lang,
        'alerts': alerts
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def composition(id: str, format: str = "json", data: str = "", lang: str = "en",
                toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the composition of a train, i.e., carriages and locomotives.

    :param id: The ID of the train.
    :param format: The response format.
    :param data: To get all raw unfiltered data use 'all'.
    :param lang: The language of the response.
    """
    url = f"{BASE_URL}/composition/"
    params = {
        'id': id,
        'format': format,
        'data': data,
        'lang': lang
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def disturbances(format: str = "json", lineBreakCharacter: str = "", lang: str = "en",
                 toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about current disturbances.

    :param format: The response format.
    :param lineBreakCharacter: Character for line breaks in text.
    :param lang: The language of the response.
    """
    url = f"{BASE_URL}/disturbances/"
    params = {
        'format': format,
        'lineBreakCharacter': lineBreakCharacter,
        'lang': lang
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}