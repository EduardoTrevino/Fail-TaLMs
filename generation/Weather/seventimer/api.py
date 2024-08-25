import requests
from typing import Optional

def get_graphical_forecast(lon: float, lat: float, ac: int = 0, lang: str = 'en', unit: str = 'metric', output: str = 'internal', tzshift: int = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves an image-based weather forecast for a specified location using the graphical API.
    
    Parameters:
    - lon: Longitude of the location (float, required)
    - lat: Latitude of the location (float, required)
    - ac: Altitude Correction, applicable in ASTRO (int, optional, default 0)
    - lang: Language (str, optional, default 'en')
    - unit: Unit system, either 'metric' or 'british' (str, optional, default 'metric')
    - output: Output format, either 'internal' for graphical (str, optional, default 'internal')
    - tzshift: Timezone adjustment (int, optional, default 0)

    Returns:
    - Binary content of the PNG image
    """
    url = "http://www.7timer.info/bin/astro.php"
    params = {
        'lon': lon,
        'lat': lat,
        'ac': ac,
        'lang': lang,
        'unit': unit,
        'output': output,
        'tzshift': tzshift
    }
    response = requests.get(url, params=params)
    return response.content

def get_machine_readable_forecast(lon: float, lat: float, product: str = 'astro', output: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves machine-readable weather forecast data for a specified location.
    
    Parameters:
    - lon: Longitude of the location (float, required)
    - lat: Latitude of the location (float, required)
    - product: Forecast product type ('astro', 'civil', 'civillight', 'meteo', or 'two') (str, optional, default 'astro')
    - output: Output format ('xml' or 'json') (str, optional, default 'json')

    Returns:
    - JSON or XML formatted weather data
    """
    url = "http://www.7timer.info/bin/api.pl"
    params = {
        'lon': lon,
        'lat': lat,
        'product': product,
        'output': output
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if output == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}