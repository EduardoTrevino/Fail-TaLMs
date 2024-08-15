import requests
import json
from typing import Optional, Dict, Union, List

def search(query: str, type: Optional[str] = None, exact: Optional[bool] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for board games by name or keyword.
    """
    url = "https://boardgamegeek.com/xmlapi2/search"
    params = {'query': query}
    if type:
        params['type'] = type
    if exact is not None:
        params['exact'] = '1' if exact else '0'

    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def thing(id: str, stats: Optional[bool] = True, comments: Optional[bool] = True, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve detailed information about a specific board game, including statistics and comments.
    """
    url = "https://boardgamegeek.com/xmlapi2/thing"
    params = {'id': id}
    if stats:
        params['stats'] = '1'
    if comments:
        params['comments'] = '1'

    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
