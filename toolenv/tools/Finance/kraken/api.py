import requests
from typing import Optional, Dict, Union

def getTicker(pair: str='XBTUSD', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Union[Dict, str]:
    """
    Get ticker information for all or requested markets.
    """
    url = f"https://api.kraken.com/0/public/Ticker"
    querystring = {'pair': pair}

    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getOHLCData(pair: str='XBTUSD', interval: int=60, since: Optional[int]=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Union[Dict, str]:
    """
    Get OHLC (open/high/low/close, also known as candle) data for a given market.
    """
    url = f"https://api.kraken.com/0/public/OHLC"
    querystring = {'pair': pair, 'interval': interval}
    if since:
        querystring['since'] = since

    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
