import requests
import json
from typing import Optional, Dict, Union, List

def amiibo(name: str=None, id: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns information of all amiibos or a specific amiibo based on filters such as name or id.
    """
    url = f"https://www.amiiboapi.com/api/amiibo/"
    querystring = {}
    if name:
        querystring['name'] = name
    if id:
        querystring['id'] = id

    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def showgames(name: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the games that the specified amiibo can be used in. 
    """
    url = f"https://www.amiiboapi.com/api/amiibo/"
    querystring = {}
    if name:
        querystring['name'] = name
        querystring['showgames'] = ''

    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
