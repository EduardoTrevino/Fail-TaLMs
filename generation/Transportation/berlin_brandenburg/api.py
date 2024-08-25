import requests
from typing import Optional

def locations(query: str, fuzzy: bool = True, results: int = 10, stops: bool = True, addresses: bool = True, poi: bool = True, linesOfStops: bool = False, language: str = 'en', pretty: bool = True, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Find stops/stations, POIs and addresses matching a query.
    """
    url = "https://v6.vbb.transport.rest/locations"
    params = {
        'query': query,
        'fuzzy': fuzzy,
        'results': results,
        'stops': stops,
        'addresses': addresses,
        'poi': poi,
        'linesOfStops': linesOfStops,
        'language': language,
        'pretty': pretty
    }
    response = requests.get(url, params=params)
    return response.json()

def locations_nearby(latitude: float, longitude: float, results: int = 8, distance: Optional[int] = None, stops: bool = True, poi: bool = False, linesOfStops: bool = False, language: str = 'en', pretty: bool = True, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Find stops/stations close to a given geolocation.
    """
    url = "https://v6.vbb.transport.rest/locations/nearby"
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'results': results,
        'distance': distance,
        'stops': stops,
        'poi': poi,
        'linesOfStops': linesOfStops,
        'language': language,
        'pretty': pretty
    }
    response = requests.get(url, params=params)
    return response.json()

def stops_reachable_from(latitude: float, longitude: float, address: str, when: Optional[str] = None, maxTransfers: int = 5, maxDuration: Optional[int] = None, language: str = 'en', suburban: bool = True, subway: bool = True, tram: bool = True, bus: bool = True, ferry: bool = True, express: bool = True, regional: bool = True, pretty: bool = True, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Find stops/stations reachable within a certain time from an address.
    """
    url = "https://v6.vbb.transport.rest/stops/reachable-from"
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'address': address,
        'when': when,
        'maxTransfers': maxTransfers,
        'maxDuration': maxDuration,
        'language': language,
        'suburban': suburban,
        'subway': subway,
        'tram': tram,
        'bus': bus,
        'ferry': ferry,
        'express': express,
        'regional': regional,
        'pretty': pretty
    }
    response = requests.get(url, params=params)
    return response.json()

def stop_info(stop_id: str, linesOfStops: bool = False, language: str = 'en', pretty: bool = True, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Find a stop/station by ID.
    """
    url = f"https://v6.vbb.transport.rest/stops/{stop_id}"
    params = {
        'linesOfStops': linesOfStops,
        'language': language,
        'pretty': pretty
    }
    response = requests.get(url, params=params)
    return response.json()

def stop_departures(stop_id: str, when: Optional[str] = None, direction: Optional[str] = None, duration: int = 10, results: Optional[int] = None, linesOfStops: bool = False, remarks: bool = True, language: str = 'en', suburban: bool = True, subway: bool = True, tram: bool = True, bus: bool = True, ferry: bool = True, express: bool = True, regional: bool = True, pretty: bool = True, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get departures at a stop/station.
    """
    url = f"https://v6.vbb.transport.rest/stops/{stop_id}/departures"
    params = {
        'when': when,
        'direction': direction,
        'duration': duration,
        'results': results,
        'linesOfStops': linesOfStops,
        'remarks': remarks,
        'language': language,
        'suburban': suburban,
        'subway': subway,
        'tram': tram,
        'bus': bus,
        'ferry': ferry,
        'express': express,
        'regional': regional,
        'pretty': pretty
    }
    response = requests.get(url, params=params)
    return response.json()

def journeys(from_id: str, to_id: str, departure: Optional[str] = None, arrival: Optional[str] = None, results: int = 3, stopovers: bool = False, transfers: Optional[int] = None, transferTime: int = 0, accessibility: str = 'not accessible', bike: bool = False, startWithWalking: bool = True, walkingSpeed: str = 'normal', tickets: bool = False, polylines: bool = False, subStops: bool = True, entrances: bool = True, remarks: bool = True, scheduledDays: bool = False, language: str = 'en', suburban: bool = True, subway: bool = True, tram: bool = True, bus: bool = True, ferry: bool = True, express: bool = True, regional: bool = True, pretty: bool = True, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Find journeys from A to B.
    """
    url = "https://v6.vbb.transport.rest/journeys"
    params = {
        'from': from_id,
        'to': to_id,
        'departure': departure,
        'arrival': arrival,
        'results': results,
        'stopovers': stopovers,
        'transfers': transfers,
        'transferTime': transferTime,
        'accessibility': accessibility,
        'bike': bike,
        'startWithWalking': startWithWalking,
        'walkingSpeed': walkingSpeed,
        'tickets': tickets,
        'polylines': polylines,
        'subStops': subStops,
        'entrances': entrances,
        'remarks': remarks,
        'scheduledDays': scheduledDays,
        'language': language,
        'suburban': suburban,
        'subway': subway,
        'tram': tram,
        'bus': bus,
        'ferry': ferry,
        'express': express,
        'regional': regional,
        'pretty': pretty
    }
    response = requests.get(url, params=params)
    return response.json()

def radar(north: float, west: float, south: float, east: float, results: int = 256, duration: int = 30, frames: int = 3, polylines: bool = True, language: str = 'en', pretty: bool = True, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Find all vehicles currently in an area and their movements.
    """
    url = "https://v6.vbb.transport.rest/radar"
    params = {
        'north': north,
        'west': west,
        'south': south,
        'east': east,
        'results': results,
        'duration': duration,
        'frames': frames,
        'polylines': polylines,
        'language': language,
        'pretty': pretty
    }
    response = requests.get(url, params=params)
    return response.json()

def lines(id: Optional[str] = None, name: Optional[str] = None, operator: Optional[str] = None, variants: bool = True, mode: Optional[str] = None, product: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Filter the lines available.
    """
    url = "https://v6.vbb.transport.rest/lines"
    params = {
        'id': id,
        'name': name,
        'operator': operator,
        'variants': variants,
        'mode': mode,
        'product': product
    }
    response = requests.get(url, params=params)
    return response.json()