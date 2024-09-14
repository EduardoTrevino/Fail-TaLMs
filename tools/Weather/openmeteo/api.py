import requests
from typing import Optional, List


def get_weather_forecast(latitude: float, longitude: float, hourly: Optional[List[str]] = None,
                         daily: Optional[List[str]] = None, current: Optional[List[str]] = None, 
                         temperature_unit: Optional[str] = "celsius", wind_speed_unit: Optional[str] = "kmh", 
                         precipitation_unit: Optional[str] = "mm", timeformat: Optional[str] = "iso8601", 
                         timezone: Optional[str] = "GMT", past_days: Optional[int] = 0, 
                         forecast_days: Optional[int] = 7, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Provides weather forecast for a given location. You can request hourly, daily, and/or current weather data.

    Parameters:
    latitude [Required]: float [Description: Geographical WGS84 coordinates of the location.]
    longitude [Required]: float [Description: Geographical WGS84 coordinates of the location.]
    hourly [Optional]: list [Description: A list of weather variables which should be returned hourly.]
    daily [Optional]: list [Description: A list of daily weather variable aggregations which should be returned.]
    current [Optional]: list [Description: A list of weather variables to get current conditions.]
    temperature_unit [Optional]: string [Description: Temperature units like celsius or fahrenheit.]
    wind_speed_unit [Optional]: string [Description: Wind speed units like km/h, m/s, mph, or knots.]
    precipitation_unit [Optional]: string [Description: Precipitation units like mm or inch.]
    timeformat [Optional]: string [Description: Time format like iso8601 or unixtime.]
    timezone [Optional]: string [Description: Timezone like GMT or location-based timezone.]
    past_days [Optional]: int [Description: Number of past days to include in the weather data.]
    forecast_days [Optional]: int [Description: Number of forecast days to include in the weather data.]
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "temperature_unit": temperature_unit,
        "wind_speed_unit": wind_speed_unit,
        "precipitation_unit": precipitation_unit,
        "timeformat": timeformat,
        "timezone": timezone,
        "past_days": past_days,
        "forecast_days": forecast_days
    }
    
    if hourly:
        params["hourly"] = ",".join(hourly)
    if daily:
        params["daily"] = ",".join(daily)
    if current:
        params["current"] = ",".join(current)

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}