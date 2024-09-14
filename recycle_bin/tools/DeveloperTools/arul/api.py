import requests
from typing import Optional


def getiptext(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the user's IP address in plain text format.
    """
    url = "https://api.aruljohn.com/ip"
    
    response = requests.get(url)
    try:
        ip_address = response.text.strip()
    except:
        ip_address = "Error fetching IP address"
    return ip_address


def getipjson(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the user's IP address in JSON format.
    """
    url = "https://api.aruljohn.com/ip/json"
    
    response = requests.get(url)
    try:
        ip_data = response.json()
    except:
        ip_data = {"error": "Error fetching IP address"}
    return ip_data
