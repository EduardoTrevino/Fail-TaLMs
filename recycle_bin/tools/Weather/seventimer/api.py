import requests

def get_astro_forecast(lon: float, lat: float, output: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the 3-day astronomical weather forecast
    """
    url = f"http://www.7timer.info/bin/api.pl"
    querystring = {'lon': lon, 'lat': lat, 'product': 'astro', 'output': output}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_civil_forecast(lon: float, lat: float, output: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the 8-day civil weather forecast
    """
    url = f"http://www.7timer.info/bin/api.pl"
    querystring = {'lon': lon, 'lat': lat, 'product': 'civil', 'output': output}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation