import requests
import json
from typing import Optional, Dict, Union, List

def get_user(results: Optional[int] = 1, gender: Optional[str] = None, nat: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Generate a random user
    """
    url = 'https://randomuser.me/api/'
    querystring = {'results': results}
    if gender:
        querystring['gender'] = gender
    if nat:
        querystring['nat'] = nat

    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_multiple_users(results: int = 10, gender: Optional[str] = None, nat: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Generate multiple random users
    """
    url = 'https://randomuser.me/api/'
    querystring = {'results': results}
    if gender:
        querystring['gender'] = gender
    if nat:
        querystring['nat'] = nat

    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
