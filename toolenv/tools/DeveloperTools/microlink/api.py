import requests
from typing import Optional, Dict, Union, List

def metadata(url: str, adblock: Optional[bool] = True, audio: Optional[bool] = False, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve metadata from any URL.
    """
    api_url = "https://api.microlink.io"
    querystring = {
        "url": url,
        "adblock": adblock,
        "audio": audio
    }
    
    response = requests.get(api_url, params=querystring)
    try:
        data = response.json()
    except ValueError:
        data = response.text
    return data

def screenshot(url: str, fullscreen: Optional[bool] = False, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Take a screenshot of the target website.
    """
    api_url = "https://api.microlink.io"
    querystring = {
        "url": url,
        "screenshot": True,
        "fullscreen": fullscreen
    }
    
    response = requests.get(api_url, params=querystring)
    try:
        data = response.json()
    except ValueError:
        data = response.text
    return data
