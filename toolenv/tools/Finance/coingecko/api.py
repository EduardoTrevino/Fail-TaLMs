import requests
from typing import Optional, Dict

def coins_list(include_platform: Optional[bool] = False, status: Optional[str] = "active", toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve all supported coins with their id, name, and symbol.
    """
    url = "https://pro-api.coingecko.com/api/v3/coins/list"
    querystring = {}
    
    if include_platform:
        querystring['include_platform'] = include_platform
    if status:
        querystring['status'] = status
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def coin_data_by_id(id: str, localization: Optional[bool] = True, tickers: Optional[bool] = True, market_data: Optional[bool] = True, community_data: Optional[bool] = True, developer_data: Optional[bool] = True, sparkline: Optional[bool] = False, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve data for a specific coin by its id.
    """
    url = f"https://pro-api.coingecko.com/api/v3/coins/{id}"
    querystring = {
        "localization": localization,
        "tickers": tickers,
        "market_data": market_data,
        "community_data": community_data,
        "developer_data": developer_data,
        "sparkline": sparkline
    }
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
