import requests
from typing import Optional

def get_public_ip(format: Optional[str] = None, callback: Optional[str] = None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the user's public IPv4 or IPv6 address in the specified format.
    
    :param format: The response format: 'text', 'json', or 'jsonp'.
    :param callback: The name of the JSONP callback function (used only when format is 'jsonp').
    :return: The public IP address.
    """
    url = "https://api.ipify.org"
    querystring = {}
    if format:
        querystring['format'] = format
    if callback:
        querystring['callback'] = callback

    response = requests.get(url, params=querystring)
    try:
        observation = response.json() if format == 'json' or format == 'jsonp' else response.text
    except:
        observation = response.text
    return observation

def get_geolocation(ip: Optional[str] = None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve geolocation information based on the user's public IP address.
    
    :param ip: The public IP address for which geolocation data is to be retrieved.
    :return: Geolocation information.
    """
    url = f"https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey=your_api_key&ipAddress={ip}"

    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
