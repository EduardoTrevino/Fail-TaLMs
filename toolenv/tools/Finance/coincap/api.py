import requests

from typing import Optional, Dict, Union, List

def assets(limit: Optional[int] = 100, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a list of all available assets with their current market data.
    """
    url = "https://api.coincap.io/v2/assets"
    params = {
        'limit': limit
    }
    
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def markets(asset_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve market data for a specific asset across different exchanges.
    """
    url = f"https://api.coincap.io/v2/markets"
    params = {
        'baseId': asset_id
    }
    
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
