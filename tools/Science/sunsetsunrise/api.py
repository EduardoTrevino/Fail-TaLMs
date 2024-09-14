import requests
from typing import Optional


def get_sunrise_sunset_times(lat: float, lng: float, date: Optional[str] = 'today', timezone: Optional[str] = None, 
                             date_start: Optional[str] = None, date_end: Optional[str] = None, 
                             time_format: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve sunrise and sunset times for a specific location based on latitude and longitude.
    
    Parameters:
    lat [Required]: float - Latitude of the location in decimal degrees.
    lng [Required]: float - Longitude of the location in decimal degrees.
    date [Optional]: str - Date in YYYY-MM-DD format or relative formats such as “today” and “tomorrow”. Defaults to today.
    timezone [Optional]: str - Timezone of the returned times. Defaults to the location's timezone.
    date_start [Optional]: str - Start date in YYYY-MM-DD format for a range.
    date_end [Optional]: str - End date in YYYY-MM-DD format for a range.
    time_format [Optional]: str - Time format such as "24", "military", or "unix".
    """
    url = "https://api.sunrisesunset.io/json"
    params = {
        'lat': lat,
        'lng': lng,
        'date': date
    }
    if timezone:
        params['timezone'] = timezone
    if date_start:
        params['date_start'] = date_start
    if date_end:
        params['date_end'] = date_end
    if time_format:
        params['time_format'] = time_format
    
    response = requests.get(url, params=params)
    
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}