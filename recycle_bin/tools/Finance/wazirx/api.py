import requests
from typing import Optional, Dict, Union, List

def ticker24hr(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get 24-hour rolling window price change statistics for a specific cryptocurrency pair.
    """
    url = "https://api.wazirx.com/sapi/v1/ticker/24hr"
    querystring = {'symbol': symbol}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def depth(symbol: str, limit: Optional[int]=5, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the current order book depth for a specific cryptocurrency pair.
    """
    url = "https://api.wazirx.com/sapi/v1/depth"
    querystring = {'symbol': symbol, 'limit': limit}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
