import requests
from typing import Optional, Dict

def dataexport(user: str, format: str = 'json', limit: Optional[int] = 20, after: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Download the list of tracks of any user profile posted publicly on Openwhyd.
    """
    url = f"https://openwhyd.org/{user}"
    params = {'format': format, 'limit': limit}
    if after:
        params['after'] = after
    
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def userapi(id: str, isSubscr: Optional[bool] = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get details about a user by user ID.
    """
    url = f"https://openwhyd.org/api/user"
    params = {'id': id}
    if isSubscr:
        params['isSubscr'] = isSubscr
    
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
