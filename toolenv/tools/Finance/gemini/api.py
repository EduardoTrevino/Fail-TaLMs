import requests
import json
from typing import Optional, Dict, Union, List


def symbols(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve all available trading symbols.
    """
    url = "https://api.gemini.com/v1/symbols"
    
    response = requests.get(url)
    try:
        symbols = response.json()
    except:
        symbols = response.text
    return symbols


def ticker_v2(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve recent trading activity for the provided symbol.
    """
    url = f"https://api.gemini.com/v2/ticker/{symbol}"
    
    response = requests.get(url)
    try:
        ticker_data = response.json()
    except:
        ticker_data = response.text
    return ticker_data


def candles(symbol: str, time_frame: str='15m', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve time-intervaled data for the provided symbol.
    """
    url = f"https://api.gemini.com/v2/candles/{symbol}/{time_frame}"
    
    response = requests.get(url)
    try:
        candles_data = response.json()
    except:
        candles_data = response.text
    return candles_data
