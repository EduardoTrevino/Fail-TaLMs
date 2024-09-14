import requests
from typing import Optional, List, Dict

BASE_URL = "https://data.police.uk/api"

def available_datasets(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Returns a list of available datasets.
    """
    url = f"{BASE_URL}/crimes-street-dates"
    response = requests.get(url)
    return response.json()

def list_forces(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict]:
    """
    Returns a list of all the police forces available via the API except the British Transport Police.
    """
    url = f"{BASE_URL}/forces"
    response = requests.get(url)
    return response.json()

def specific_force(force_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Returns detailed information about a specific police force given its ID.
    """
    url = f"{BASE_URL}/forces/{force_id}"
    response = requests.get(url)
    return response.json()

def force_senior_officers(force_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict]:
    """
    Returns a list of senior officers for a specific police force given its ID.
    """
    url = f"{BASE_URL}/forces/{force_id}/people"
    response = requests.get(url)
    return response.json()

def street_level_crimes(lat: float, lng: float, date: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict]:
    """
    Returns crimes at street-level for a given latitude and longitude, optionally limited to a specific date.
    """
    url = f"{BASE_URL}/crimes-street/all-crime"
    params = {
        "lat": lat,
        "lng": lng,
        "date": date
    }
    response = requests.get(url, params=params)
    return response.json()

def crimes_at_location(location_id: Optional[int] = None, lat: Optional[float] = None, lng: Optional[float] = None, date: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict]:
    """
    Returns crimes which occurred at a specified location ID or nearest pre-defined location for given latitude/longitude.
    """
    url = f"{BASE_URL}/crimes-at-location"
    params = {
        "date": date
    }
    if location_id:
        params["location_id"] = location_id
    elif lat and lng:
        params["lat"] = lat
        params["lng"] = lng
    
    response = requests.get(url, params=params)
    return response.json()

def crimes_with_no_location(category: str, force: str, date: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict]:
    """
    Returns a list of crimes that could not be mapped to a location for a specified category and police force.
    """
    url = f"{BASE_URL}/crimes-no-location"
    params = {
        "category": category,
        "force": force,
        "date": date
    }
    response = requests.get(url, params=params)
    return response.json()

def crime_categories(date: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict]:
    """
    Returns a list of valid crime categories for a given date.
    """
    url = f"{BASE_URL}/crime-categories"
    params = {
        "date": date
    }
    response = requests.get(url, params=params)
    return response.json()

def crime_last_updated(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Returns the date when the crime data was last updated.
    """
    url = f"{BASE_URL}/crime-last-updated"
    response = requests.get(url)
    return response.json()

def outcomes_for_specific_crime(crime_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Returns the outcomes for a specific crime by its crime ID.
    """
    url = f"{BASE_URL}/outcomes-for-crime/{crime_id}"
    response = requests.get(url)
    return response.text

def neighbourhoods_by_force(force_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict]:
    """
    Returns a list of neighbourhoods for a specified police force.
    """
    url = f"{BASE_URL}/{force_id}/neighbourhoods"
    response = requests.get(url)
    return response.json()

def specific_neighbourhood(force_id: str, neighbourhood_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Returns detailed information about a specific neighbourhood in a police force.
    """
    url = f"{BASE_URL}/{force_id}/{neighbourhood_id}"
    response = requests.get(url)
    return response.json()

def neighbourhood_boundary(force_id: str, neighbourhood_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict]:
    """
    Returns a list of latitude/longitude pairs that make up the boundary of a neighbourhood.
    """
    url = f"{BASE_URL}/{force_id}/{neighbourhood_id}/boundary"
    response = requests.get(url)
    return response.json()

def neighbourhood_team(force_id: str, neighbourhood_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict]:
    """
    Returns a list of team members for a specific neighbourhood in a police force.
    """
    url = f"{BASE_URL}/{force_id}/{neighbourhood_id}/people"
    response = requests.get(url)
    return response.json()

def neighbourhood_events(force_id: str, neighbourhood_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict]:
    """
    Returns a list of upcoming events for a specific neighbourhood in a police force.
    """
    url = f"{BASE_URL}/{force_id}/{neighbourhood_id}/events"
    response = requests.get(url)
    return response.json()

def neighbourhood_priorities(force_id: str, neighbourhood_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict]:
    """
    Returns a list of priorities for a specific neighbourhood in a police force.
    """
    url = f"{BASE_URL}/{force_id}/{neighbourhood_id}/priorities"
    response = requests.get(url)
    return response.json()

def locate_neighbourhood(lat: float, lng: float, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Finds the neighbourhood policing team responsible for a particular area based on latitude and longitude.
    """
    url = f"{BASE_URL}/locate-neighbourhood"
    params = {
        "q": f"{lat},{lng}"
    }
    response = requests.get(url, params=params)
    return response.json()

def stop_and_searches_by_area(lat: Optional[float] = None, lng: Optional[float] = None, poly: Optional[str] = None, date: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict]:
    """
    Returns stop and searches at street-level for a given latitude and longitude or within a custom area.
    """
    url = f"{BASE_URL}/stops-street"
    params = {
        "lat": lat,
        "lng": lng,
        "poly": poly,
        "date": date
    }
    response = requests.get(url, params=params)
    return response.json()

def stop_and_searches_by_location(location_id: int, date: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict]:
    """
    Returns stop and searches at a particular location ID, optionally limited to a specific date.
    """
    url = f"{BASE_URL}/stops-at-location"
    params = {
        "location_id": location_id,
        "date": date
    }
    response = requests.get(url, params=params)
    return response.json()

def stop_and_searches_no_location(force: str, date: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict]:
    """
    Returns stop and searches that could not be mapped to a location for a specific force.
    """
    url = f"{BASE_URL}/stops-no-location"
    params = {
        "force": force,
        "date": date
    }
    response = requests.get(url, params=params)
    return response.json()

def stop_and_searches_by_force(force: str, date: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict]:
    """
    Returns stop and searches reported by a particular force, optionally limited to a specific date.
    """
    url = f"{BASE_URL}/stops-force"
    params = {
        "force": force,
        "date": date
    }
    response = requests.get(url, params=params)
    return response.json()