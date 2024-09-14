import requests
from typing import Optional, Dict, List

def topstocks(limit: int = 10, timeframe: str = 'day', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve the top stocks discussed on Wallstreetbets.
    
    Parameters:
    - limit: The number of top stocks to retrieve.
    - timeframe: The timeframe for the data (e.g., 'day', 'week', 'month').
    """
    url = "https://redditstocks.api/topstocks"
    querystring = {'limit': limit, 'timeframe': timeframe}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stockdetails(ticker: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve detailed information about a specific stock.
    
    Parameters:
    - ticker: The ticker symbol of the stock.
    """
    url = "https://redditstocks.api/stockdetails"
    querystring = {'ticker': ticker}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
