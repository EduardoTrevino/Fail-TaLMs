import requests
from typing import Optional, Dict

def ticker_24hr(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Get 24-hour price change statistics.
    """
    url = f"https://api.binance.com/api/v3/ticker/24hr"
    querystring = {'symbol': symbol}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ticker_price(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Get the latest price for a symbol.
    """
    url = f"https://api.binance.com/api/v3/ticker/price"
    querystring = {'symbol': symbol}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def avg_price(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Get the current average price for a symbol.
    """
    url = f"https://api.binance.com/api/v3/avgPrice"
    querystring = {'symbol': symbol}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
