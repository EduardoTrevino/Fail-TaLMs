import requests
from typing import Optional

def wayback_availability(url: str, timestamp: Optional[str] = None, callback: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: This API checks if a given url is archived and currently accessible in the Wayback Machine.

    Parameters:
    url [Required]: string [Description: The URL to check for availability in Wayback Machine.]
    timestamp [Optional]: string [Description: Timestamp to look up in Wayback in YYYYMMDDhhmmss format.]
    callback [Optional]: string [Description: Callback function for JSONP response.]
    """
    api_url = "http://archive.org/wayback/available"
    params = {
        'url': url
    }
    if timestamp:
        params['timestamp'] = timestamp
    if callback:
        params['callback'] = callback

    response = requests.get(api_url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}