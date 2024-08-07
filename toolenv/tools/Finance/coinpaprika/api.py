import requests
from typing import Optional, List, Dict, Union

def get_global_market_overview(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Returns current cryptocurrencies market overview metrics, such as global market capitalization, total 24h volume of all cryptocurrencies, number of active cryptocurrencies on coinpaprika.com, ATH of 24h volume and market capitalization, and more.
    """
    url = "https://api.coinpaprika.com/v1/global"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_ticker_for_specific_coin(coin_id: str, quotes: Optional[str] = "USD", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Returns price data of a single cryptocurrency on coinpaprika.com including identity, ranking, supplies, beta coefficient, price data in a given currency, and more.
    """
    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
    params = {"quotes": quotes}
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_historical_ohlcv(coin_id: str, start: str, end: Optional[str] = None, quote: Optional[str] = "USD", interval: Optional[str] = "24h", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict]:
    """
    Returns Open/High/Low/Close values with volume and market capitalization for a given cryptocurrency over a specified date range.
    """
    url = f"https://api.coinpaprika.com/v1/coins/{coin_id}/ohlcv/historical"
    params = {"start": start, "quote": quote, "interval": interval}
    if end:
        params["end"] = end
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
