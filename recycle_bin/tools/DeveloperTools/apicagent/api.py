import requests
import json
from typing import Optional, Dict, Union, List

def getuseragentdata(ua: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Union[Dict, str]:
    """
    Get browser, OS, and device information by parsing a user-agent string.
    """
    url = "https://api.apicagent.com/"
    querystring = {'ua': ua}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except json.JSONDecodeError:
        observation = response.text
    return observation

def postuseragentdata(ua: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Union[Dict, str]:
    """
    Send a user-agent string inside a JSON object to retrieve browser, OS, and device information.
    """
    url = "https://api.apicagent.com/"
    payload = {'ua': ua}
    
    response = requests.post(url, json=payload)
    try:
        observation = response.json()
    except json.JSONDecodeError:
        observation = response.text
    return observation
