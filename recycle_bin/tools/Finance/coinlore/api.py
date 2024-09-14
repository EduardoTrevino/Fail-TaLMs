import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List

def global_stats(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get global crypto statistics, including the total count of coins, overall market capitalization, BTC dominance, total trading volume, ATH market capitalization, and more.
    """
    url = "https://api.coinlore.net/api/global/"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def tickers(start: Optional[int] = 0, limit: Optional[int] = 100, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve tick data for multiple crypto coins, sorted by market cap. The data includes details such as name, ID, symbol, price, price change, market cap, volume, and supply for each ticker.
    """
    url = f"https://api.coinlore.net/api/tickers/?start={start}&limit={limit}"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def coin_markets(id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve top 50 exchanges and markets for a specific coin.
    """
    url = f"https://api.coinlore.net/api/coin/markets/?id={id}"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
